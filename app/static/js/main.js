// $(document).ready(function() {
// 	$('#sendButton').click(function(){
// 		$("#message").append($('#messageInput').val()+ "<br>");
// 	}) 
// });

// $(document).ready(function(){
// 	$('#testButton').click(function(){
// 		fetch('/test').then(response => {
// 			return response.json();
// 		}).then(data => {
// 			console.log(data.message);
// 		})
// 	})
// })

$('#messageForm').submit(function(e){
    e.preventDefault();
    $.ajax({
        url:'/send_message',
        type:'post',
        data:$('#messageForm').serialize(),
        success:function(){
            console.log("called send_message");
        }
    });
});