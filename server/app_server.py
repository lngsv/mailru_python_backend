import datetime
import json
import urllib.parse

def app(environ, start_response):
    now = datetime.datetime.now().isoformat()
    url = urllib.parse.urlunparse((
        'http', 
        environ['SERVER_NAME']+':'+environ['SERVER_PORT'], 
        environ['PATH_INFO'], 
        '', # params
        environ['QUERY_STRING'], 
        '' # fragment
    ))
    data = dict(time=now, url=url)
    data_bin = str.encode(json.dumps(data))
    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data_bin))),
    ])
    return iter([data_bin])

