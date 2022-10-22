# Compor-Project

## Requirements
```
sudo apt install -y apache2, apache2-dev, mysql-server, make
sudo apt install -y python3, python3-pip, python3-dev, python3-venv
sudo apt install -y wkhtmltopdf
```
## Setup
##### Copy files to `/var/www/compor-project`

##### Configure database: 
```bash
mysql -u<user> -p<password> < compor-project.structure.mysql.sql
mysql -u<user> -p<password> < compor-project.data.mysql.sql

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
cd /var/www/compor-project
python3 -m venv /venv
./venv/bin/python3 -m pip install -r requirements.txt
```

##### Add ComporPlus to Apache VirtualHost:
```
WSGIScriptAlias /compor+ /var/www/compor-project/app.wsgi
WSGIProcessGroup compor-project
WSGIDaemonProcess compor-project python-home=/var/www/compor-project/venv/ user=www-data group=www-data threads=5
```
