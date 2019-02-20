
sudo apt-get update
sudo apt-get install git
cd /opt
sudo git clone https://github.com/sidhu177/Anagramic.git
cd Anagramic/
sudo git checkout Develop
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
sudo ufw allow 5000
sudo apt install python-pip
sudo pip install pipenv
sudo pipenv install
sudo pipenv shell
gunicorn --bind 0.0.0.0:5000 wsgi:app