$(function () {
    $('.addToCart').click(function () {
        //    获取标签的属性的值的方法是 this就是当前点击的那个标签的对象
        var $button = $(this);

        var $goodsid = $button.attr('goodsid');
        $.get(
            '/axfcart/addToCart/',
            {'goodsid': $goodsid},
            function (data) {
                if (data['status'] == 200) {
                    $button.prev().html(data['c_goods_num']);
                } else {
                    window.location.href = '/axfuser/login/';
                }
            }
        )
        //attr 可以获取自定义的属性 也可以获取自带的属性
        // prop 不可以获取自定义属性 但是可以获取自带的属性
    });

    $('.subGoodsNum').click(function () {
        var $button = $(this);
        var $div = $button.parent().parent();
        var cartid = $div.attr('cartid');

        $.post(
            '/axfcart/subCart/',
            {'cartid':cartid},
            function (data) {
                if(data['status']==200) {
                    $button.next().html(data['c_goods_num']);
                    $('#total_price').html(data['totalprice']);

                }else{
                    $div.remove();
                }
            }
        )
    });

    $('.confirm').click(function () {
        var $div = $(this);
        var cartid = $div.parent().attr('cartid');

            $.ajax(
            {
                url:'/axfcart/changeStatus/',
                data:{'cartid':cartid},
                type:'get',
                dataType:'json',
                success:function (data) {
                    if(data['c_is_select']){
                        $div.find('span').find('span').html('✔');
                    }else{
                        $div.find('span').find('span').html('');
                    }
                    if(data['is_all_select']){
                        $('#is_all_select').find('span').find('span').html('✔');
                    }else{
                        $('#is_all_select').find('span').find('span').html('');
                    }

                    $('#total_price').html(data['totalprice']);

                }
            }
        )





    });

    $('#is_all_select').click(function () {
        var select_list = [];
        var unselect_list = [];
        //    判断购物车上有没有 对号  如果有对号 就添加到select_list中
        //    如果没有对号  那么就添加到unselect_list中
        var $div = $('.confirm');

        $div.each(function () {
            var cartid = $(this).parent().attr('cartid');

            if($(this).find('span').find('span').html()){
            //    要将谁存储到select_list中呢？ 假如存储进去之后 那么会将该存进去的数据
            //    获取对象 然后将对象的c_is_select的值修改为 not c_is_select
            //    cartid
                select_list.push(cartid);
            }else{
                unselect_list.push(cartid)
            }
        });

   //    传哪个列表过去到视图函数   传那个列表取决于谁  unselect_list是不是空
    //    如果unselect_list是空了 代表的是没有未选中的
    //    如果unselect_list不是空了 代表的是至少有一个未选中
        if(unselect_list.length > 0){
        //    如果未选中的列表大于0了 那么就要将未选中列表发送给视图函数
        //    join方法会将列中的每一个元素 使用（）中的字符进行拼接
            $.getJSON(
                '/axfcart/allSelect/',
                {'cartlist':unselect_list.join('#')},
                function(data){
                    $div.find('span').find('span').html('✔');
                    $('#is_all_select').find('span').find('span').html('✔');
                    $('#total_price').html(data['totalprice']);
                }
            )
        }else{
        //    否则就是未选中的列表==0  那么就要将选中的列表发送给视图函数
            $.getJSON(
                '/axfcart/allSelect/',
                {'cartlist':select_list.join('#')},
                function (data) {
                    $div.find('span').find('span').html('');
                    $('#is_all_select').find('span').find('span').html('');
                    $('#total_price').html(data['totalprice']);
                }
            )
        }

    });

    $('#make_order').click(function () {
        $.get(
            '/axforder/makeOrder',
            function (data) {
                if(data['status'] == 200){
                   window.location.href = '/axforder/orderDetail/?order_id='+data['order_id'];
                }
            }

        )
    })


});