//jQuery loader script
(function(){
    var jquery_version = '3.3.1';    // jquery version to load
    var site_url = 'http://127.0.0.1:8000/';   //the base url for our website
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