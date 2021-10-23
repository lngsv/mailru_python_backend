# Simple web server

## Prepare environment

### Install nginx
(For macOS): 
`$ brew install nginx`

### Copy configuration
(For macOS) 
```
server $ mkdir /usr/local/etc/nginx/servers
server $ cp my_first_server.conf /usr/local/etc/nginx/servers/my_first_server.conf
```
Change path prefix to yours, it should point to this project directory `server/public`

## Play with server

### Start nginx
(For macOS) `$ nginx`

### Send GET request via browser or console
`localhost:8089/get_static/google.jpeg`
`localhost:8089/get_static/my.html`

## Application server

### Activate virtual environment
```
server $ python3 -m venv <venv_dir_name>
server $ source <venv_dir_name>/bin/activate
```

### Install requirements
`server $ pip install -r requirements.txt`

### Start gunicorn
`server $ gunicorn --workers 4 app_server:app`

### Send request via browser or console
`http://127.0.0.1:8000/blablab/sflkdf?a=234&c=15`

## Proxy
1. Start gunicorn
1. (re)Start nginx
1. `localhost:8089/get_static/' -> static from `public/`
1. `localhost:8089/api/` -> proxy gunicorn

## Little help
(For macOS) \
To stop nginx `nginx -s stop` \
Nginx access log `/usr/local/var/log/nginx/access.log` \
Nginx error log `/usr/local/var/log/nginx/error.log` \
Load testing with ApacheBench `ab -k -c 958 -n 10000 'http://127.0.0.1:8089/get_static/google.jpeg'` \
DoS for static documents with `c=958`, `n=10000`
