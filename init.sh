sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo rm -f /etc/gunicorn.d/hello.py
sudo touch /home/box/web/gunicorn.log
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
