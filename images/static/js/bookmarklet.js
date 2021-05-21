//jQuery loader script
(function(){
    var jquery_version = '3.3.1';    // jquery version to load
    var site_url = 'http://2f32691c7987.ngrok.io/';   //the base url for our website
    var static_url = site_url + 'static/';   //base static files url
    var min_width = 100;   //min width & height in px for images
    var min_height = 100;
    function bookmarklet(msg){
        // here goes our bookmarklet code
};

//check if jquery is loaded
if(typeof window.jQuery != 'undefined'){
    bookmarklet();
}
else{
    //check for conflicts
    var conflict = typeof window.$ != 'undefined';
    //create the script and point to google API
    var script = document.createElement('script');
    script.src = '//ajax.googleapis.com/ajax/libs/jquery' + jquery_version + '/jquery.min.js';

    // add the script to the 'head' for processing
    document.head.appendChild(script);
    // create a way to wait until script loading
    var attempts = 15;
    (function(){
        //check again if jquery is undefined
        if(typeof window.jQuery == 'undefined'){
            if(--attempts > 0){
                //calls himself in a few milliseconds
                window.setTimeout(arguments.callee, 250)
            }
            else{
                //too much attempts to load, send error
                alert('an error ocurred while loading jquery')
            }
         } else{
                bookmarklet();
            }
        })();
    }
})()

function bookmarklet(msg)
{
    //load Css
    var css = jQuery('<link>');
    css.attr({
        rel: 'stylesheet',
        type: 'text/css',
        href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random()*99999999999999999999)
    });
    jQuery('head').append(css);

    //load HTML
    box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="iamges"></div></div>';
    jQuery('body').append(box_html);

    //close event- removes html from doc when user click close link
    jQuery('#bookmarklet #close').click(function(){
        jQuery('#bookmarklet').remove();
    });


//find images and display them
jQuery.each(jQuery('img[src$="jpg"]'), function(index, image){
    if (jQuery(image).width() >= min_width && jQuery(image).height()>=min_height)
    {
        image_url = jQuery(image).attr('src');
        jQuery('#bookmarklet .images').append('<a href="#"><img src="'+ image_url +'" /></a>');
    }
});

//when an image is selected open URL with it
jQuery('#bookmarklet .images a').click(function(e){   //click event to imgs link element
    selected_image = jQuery(this).children('img').attr('src');  // variable selected_image contains the url of selected img
    //hide bookmarklet
    jQuery('#bookmarklet').hide();
    //open new window to submit the image
    window.open(site_url + 'images/create/?url=' + encodeURIComponent(jQuery('title').text())
    + '&title=' + encodeURIComponent(jQuery('title').text()),'_blank');
});
};
