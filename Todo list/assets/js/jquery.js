$("ul").on("click","li",function(){
$(this).toggleClass("completed");

});
$("ul").on("click","span",function(event){
    $(this).parent().fadeOut();
    event.stopPropagation();
});
$("input[type='text']").keypress(function(event){
if(event.which === 13  ){
    var todotext = $(this).val();
    $(this).val("");
    $("ul").append('<li><span><img src="assets/css/delete-737-475058.webp"></span> ' + todotext + "</li>")


}

});