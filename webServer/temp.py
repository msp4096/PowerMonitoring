from wsgiref.simple_server import make_server, demo_app
import urllib.request, json

def application(environ,start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    linkweather = "http://api.openweathermap.org/data/2.5/weather?id=4930505&appid=6ab5a0a32767ee7008260b57269d8c34"
    weather = urllib.request.urlopen(linkweather)
    #return ["Eat my poo".encode("utf-8")]
    return [weather]

with make_server('0.0.0.0', 81, application) as httpd:
    print("Serving HTTP on port 81...")

    # Respond to requests until process is killed
    httpd.serve_forever()

    # Alternative: serve one request, then exit
    httpd.handle_request()
