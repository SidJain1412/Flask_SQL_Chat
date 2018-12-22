

$('#messageForm').submit(function(e){
    e.preventDefault();
    var msg = $('input[name=message]').val();
    $('input[name=message]').val("");
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
        success:function(result){
            $('#message').append(result.sender+":&emsp;"+result.message+"<br>");
            console.log("called send_message");
        },
        error:function(err){
            console.log("Empty message");
        }
    });
});