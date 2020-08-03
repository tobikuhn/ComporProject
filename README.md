#Compor-Plus

## Requirements
```
sudo apt install -y mysql-server, python3, python3-pip, python3-dev, python3-venv, curl, make
```
## Setup
##### Copy files to `/var/www/compor-plus`

##### Configure database: 
```bash
mysql -u<root> -p<password> <database> < compor-plus.mysql.sql
```


##### Create virtualenv
```bash
python3 -m venv /var/www/compor-plus/venv
cd /var/www/compor-plus
./venv/bin/python3 install -r requirements.txt
```

##### Install mod_wsgi for Python 3
```bash
cd /opt
curl mod_wsgi.4.7.1.tar.gz https://github.com/GrahamDumpleton/mod_wsgi/archive/4.7.1.tar.gz
tar -xzf mod_wsgi.4.7.1.tar.gz

cd mod_wsgi.4.7.1.tar.gz
./configure --with-python=/usr/bin/python3
make install

echo "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" >> /etc/apache2/mods-available/mod_wsgi.load
a2enmod mod_wsgi
```

##### Add ComporPlus to Apache VirtualHost:
```
WSGIScriptAlias /compor+/ /var/www/compor-plus
```