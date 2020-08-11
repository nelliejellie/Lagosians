function bookmarklet(msg) {
    // load CSS
    var css = $('<link>');
    css.attr({
    rel: 'stylesheet',
    type: 'text/css',
    href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.
    random()*99999999999999999999)
    });
$('head').append(css);
// load HTML
box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark</h1><div class="images"></div>';
$('body').append(box_html);
// close event
$('#bookmarklet #close').click(function(){
    $('#bookmarklet').remove();
    });
};
// find images and display them
$.each($('img[src$="jpg"]'), function(index, image) {
    if ($(image).width() >= min_width && $(image).height()
    >= min_height)
    {
    image_url = $(image).attr('src');
    $('#bookmarklet .images').append('<a href="#"><img src="'+
    image_url +'" /></a>');
    }
    });