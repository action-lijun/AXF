// 对swiper进行初始化
//<script>
//   var mySwiper = new Swiper ('.swiper-container', {
//     direction: 'vertical',
//     loop: true,
//
//     // 如果需要分页器
//     pagination: '.swiper-pagination',
//
//     // 如果需要前进后退按钮
//     nextButton: '.swiper-button-next',
//     prevButton: '.swiper-button-prev',
//
//     // 如果需要滚动条
//     scrollbar: '.swiper-scrollbar',
//   })
//   </script>


$(function () {
    init_mySwiper();
    init_mySwiper1();

});

function init_mySwiper() {
    var mySwiper = new Swiper('#topSwiper', {
        loop: true,
        autoplay: 3000,
        autoplayDisableOnInteraction: false,
        pagination: '.swiper-pagination',

    })
}

function init_mySwiper1() {
    var mySwiper1 = new Swiper('#swiperMenu', {
        slidesPerView: 3
    })
}