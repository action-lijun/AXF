$(function () {
        $('#imgCode').click(function () {
    //    jquery中如何给标签的属性赋值
        $(this).attr('src','/axfuser/get_code/?'+Math.random());
    })
})