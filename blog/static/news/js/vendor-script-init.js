document.addEventListener('DOMContentLoaded', () => {
    $('.owl-carousel').owlCarousel({
        loop:true,
        padding:20,
        margin: 20,
        nav:true,
        responsiveClass:true,
        responsive:{
        0:{
            items:1,
            nav:true
        },
        900:{
            items:3,
            nav:false
        }
    }
    });
});
