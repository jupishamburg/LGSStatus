# How to run LgsStatePlotter locally:

* sudo apt-get install ruby ruby-dev rubygems
* pip install -r requirements.txt
* gem install sass listen
* gem install --version '~> 0.8.8' rb-inotify
* wget http://lgs-hh.geheimorganisation.org/lgs.db
* cp config.json.example config.json
* Maybe you want to edit config.json with editor of your choice ...
* python2 run.py

Open browser of your choice and open:
http://0.0.0.0:8080/

Profit!

# API

Posting:
* curl -d 'key=ieSohc0oochie6Reequungoo7quoza8NuRaing9una&value=42' '0.0.0.0:8080/append/clients'

Accepted types:

clients
temperature
door


