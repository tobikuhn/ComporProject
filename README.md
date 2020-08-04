# Compor-Plus

## Requirements
```
sudo apt install -y apache2, apache2-dev, mysql-server, python3, python3-pip, python3-dev, python3-venv, make
```
## Setup
##### Copy files to `/var/www/compor-plus`

##### Configure database: 
```bash
mysql -u<user> -p<password> < compor-plus.structure.mysql.sql
mysql -u<user> -p<password> < compor-plus.data.mysql.sql

```

##### Install mod_wsgi for Python 3
```bash
cd /opt
wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.7.1.tar.gz
tar -xzf 4.7.1.tar.gz

cd mod_wsgi-4.7.1
./configure --with-python=/usr/bin/python3
make install

echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" > /etc/apache2/mods-available/mod_wsgi.load
a2enmod mod_wsgi
```

##### Create virtualenv
```bash
cd /var/www/compor-plus
python3 -m venv /venv
./venv/bin/python3 install -r requirements.txt
```

##### Add ComporPlus to Apache VirtualHost:
```
WSGIScriptAlias /compor+ /var/www/compor-plus/app.wsgi
WSGIProcessGroup compor-plus
WSGIDaemonProcess compor-plus python-home=/var/www/compor-plus/venv/ user=www-data group=www-data threads=5
```
