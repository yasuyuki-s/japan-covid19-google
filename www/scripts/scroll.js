$(function() {
    var TopBtn = $('#PageTopBtn');    
    TopBtn.hide();
    // スクロール位置が100でボタンを表示
    $(window).scroll(function() {
        if ($(this).scrollTop() > 500) {
            TopBtn.fadeIn();
        } 
        else {
            TopBtn.fadeOut();
        }
    });
    // ボタンを押下するとトップへ移動
    TopBtn.click(function() {
        const position = $('#list').offset().top;
        $('body,html').animate({
            scrollTop: position
        }, 800);
        return false;
    });
});