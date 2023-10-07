jQuery(function($){
    var $navbar=$('nav');
    $(window).scroll(function(event){
        var $current = $(this).scrollTop();
        if($current>100){
            $navbar.addClass('nav');
        }
        else{
            $navbar.removeClass('nav');
        }
    });
});

$(window).scroll(function(){
    if($(this).scrollTop()>100) {
        $('#header img').attr('src','/static/images/logo1.png');
    }
    else {
        $('#header img').attr('src','/static/images/logo2.png');
    }
})