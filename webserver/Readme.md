# How to run LgsStatePlotter locally:

* `bower install`
* `sudo apt-get install ruby ruby-dev rubygems`
* `pip install -r requirements.txt`
* `gem install sass listen`
* `gem install --version '~> 0.8.8' rb-inotify`
* `wget http://lgs-hh.geheimorganisation.org/lgs.db`
* `cp config.json.example config.json`
* Maybe you want to edit `config.json` with editor of your choice for setting up credentials
* `python2 run.py`

Open browser of your choice and open:
`http://0.0.0.0:8080/`

Profit!

# API

Posting:
* `curl -d 'key=YOUR_PERSONAL_WEBSERVER_ACCESS_TOKEN&value=THE_TYPE_VALUE' '0.0.0.0:8080/append/TYPE'`

Accepted types:

* `clients`
 * value is integer amount of registered clients in local network
* `temperature`
 * value is integer in degrees Celsius
* `door`
 * value is boolean, "1" for open, "0" for closed door state



