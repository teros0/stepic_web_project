sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart

sudo rm -f /etc/gunicorn.d/hello.py
sudo touch /home/box/web/gunicorn.log
sudo ln -sf /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'ask_user'@'localhost' IDENTIFIED BY '123456789';"
