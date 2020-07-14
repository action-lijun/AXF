$(function () {
    $('#tologin').click(function () {

        window.location.href = '/axfuser/login/';
    })


    $('#regis').click(function () {
        window.open('/axfuser/register/',target='_self')

    })
})