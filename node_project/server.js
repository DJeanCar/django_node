var http = require('http')
var server = http.createServer().listen(3000)
var io = require('socket.io').listen(server)
var querystring = require('querystring');

io.on('connection', function (socket) {
	socket.on('dando like', function(datos){
		var values = querystring.stringify(datos);
		var options = {
			hostname : 'localhost',
			port : '8000',
			path : '/dando-like',
			method : 'POST',
			headers : {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': values.length
			}
		}

		var req = http.request(options, function (res){
			res.setEncoding('utf8');
			res.on('data', function (data) { 
				// Aqui vienen los datos de django
				console.log(data);
				io.emit('devolviendo like', data);
			});
		});
		req.write(values);
		req.end();
	});
});