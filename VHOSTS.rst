Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess modelbouwdag-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/modelbouwdag/log/apache2/error.log"
        CustomLog "/srv/sites/modelbouwdag/log/apache2/access.log" common

        WSGIProcessGroup modelbouwdag-<target>

        Alias /media "/srv/sites/modelbouwdag/media/"
        Alias /static "/srv/sites/modelbouwdag/static/"

        WSGIScriptAlias / "/srv/sites/modelbouwdag/src/modelbouwdag/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-modelbouwdag-<target>]
    user = <user>
    command = /srv/sites/modelbouwdag/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/modelbouwdag/src/modelbouwdag/wsgi/wsgi_<target>.py
    home = /srv/sites/modelbouwdag/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/modelbouwdag/log/uwsgi_err.log
    stdout_logfile = /srv/sites/modelbouwdag/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_modelbouwdag_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/modelbouwdag/log/nginx-access.log;
      error_log /srv/sites/modelbouwdag/log/nginx-error.log;

      location /500.html {
        root /srv/sites/modelbouwdag/src/modelbouwdag/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/modelbouwdag/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/modelbouwdag/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_modelbouwdag_<target>;
      }
    }
