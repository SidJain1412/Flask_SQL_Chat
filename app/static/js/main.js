$(document).ready(function() {
	$('#sendButton').click(function(){
		$("#message").append($('#messageInput').val()+ "<br>");
	}) 
});