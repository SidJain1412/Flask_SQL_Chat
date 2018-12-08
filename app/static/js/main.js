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

// var username = document.getElementById('username').value;

$('#messageForm').submit(function(e){
    e.preventDefault();
    var msg = $('input[name=message]').val();
    var username = $('#username').text();
    data = {};
    data['message'] = msg;
    data['username'] = username;
    console.log(data)
    console.log(msg);
    $.ajax({
        contentType: "application/json; charset=utf-8",
        url:'/send_message',
        type:'post',
        data: JSON.stringify(data),
        success:function(){
            console.log("called send_message");
        }
    });
    // $.ajax({
    // 	url:'/send_message',
    // 	type:'get',
    // 	success: function(msg){
    //         console.log("getting message")
    // 		$('#message').html()=$('#message').html+msg.sentBy.username+":&emsp;"+msg.message+"<br>";
    // 	}
    // })
});