$(document).ready(function() {
	$('#sendButton').click(function(){
		$("#message").append($('#messageInput').val()+ "<br>");
	}) 
});

$(document).ready(function(){
	$('#testButton').click(function(){
		fetch('/test').then(response => {
			return response.json();
		}).then(data => {
			console.log(data.message);
		})
	})
})
