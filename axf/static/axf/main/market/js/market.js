$(function () {

    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#type_select').hide()
        $('#all_type_container').toggle()
    })


    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up')
        $('#type_select').hide()
        $('#sort_rule_container').toggle()
    })

    
})