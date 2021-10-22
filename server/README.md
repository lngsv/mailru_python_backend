# My (almost) first web server

## Prepare environment

### Install nginx
(For macOS): 
`$ brew install nginx`

### Activate virtual environment
```console
server $ python3 -m venv <venv_dir_name>
server $ source <venv_dir_name>/bin/activate
```

### Install requirements
`server $ pip install -r requirements.txt`

### Copy configuration
(For macOS) 
```console
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

