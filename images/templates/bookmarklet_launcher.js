/* a bookmarklet is bookmark stored in web browser that contains JS code to extend browser's functionality */
// for bookmarklet

(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='http://2f32691c7987.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();
