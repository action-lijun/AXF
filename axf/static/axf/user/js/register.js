$(function () {

    var flagname = false;
    var flagpassword = false;

    $('#name').blur(function () {

        //    获取文本框中的内容
        var name = $('#name').val();

        //    定义一个正则表达式
        var reg = /^[a-zA-Z0-9_-]{4,8}$/;

        //    判断某字符串是否符合某正则  test方法会判断某字符串是否符合某正则 如果符合则返回true
        //    如果不符合则返回false
        var b = reg.test(name);

        if (b) {
            // $('#nameinfo').html('用户名字符合要求').css('color','green');
            //  $.getJSON(
            //          请求资源路径
            //          请求参数
            //          响应的数据
            // )
            //data就是视图函数的返回值
            $.getJSON(
                '/axfuser/checkName',
                {'name': name},
                function (data) {
                    if (data['status'] == 200) {

                        flagname = true;
                        $('#nameinfo').html(data['msg']).css('color', 'green');
                    } else {
                        $('#nameinfo').html(data['msg']).css('color', 'red');
                    }
                }
            )
        } else {
            $('#nameinfo').html('用户名字错误！').css('color', 'red');
        }
    })
    //密码一致性校验
    $('#pwdConfirm').blur(function () {
        var pwd = $('#pwd').val();
        var pwdConfirm = $('#pwdConfirm').val();

        if (pwd == pwdConfirm) {
            flagpassword = true;
            $('#pwdinfo').html('密码一致').css('color', 'green');
        } else {
            $('#pwdinfo').html('密码不一致').css('color', 'red');
        }

    })

    // query.submit(function(){
    // })
    // 如果返回的是true 那么就允许提交 如果返回的是false 那么就不允许提交
    $('form').submit(function () {
        var name = $('#name').val();
        if (!name) {
            $('#nameinfo').html('用户名字不可以为空').css('color', 'red');
        }

        var password = $('#password').val();
        if (!password) {
            $('#passwordinfo').html('密码不能为空').css('color', 'red');
        }

        //什么情况下允许提交?   是所有的验证都通过之后
        // alert(flagname);
        // alert(flagpassword);

        //true 和 true 返回的是1    true和false返回的是0  false 和 false返回的是0
        var b = flagname & flagpassword;

        if (b) {
            return true;
        } else {
            return false;
        }
    })


})