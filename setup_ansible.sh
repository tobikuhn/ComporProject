sudo apt update
sudo apt install -y software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

sudo ansible-galaxy collection install community.mysql
pip3 install PyMySql
