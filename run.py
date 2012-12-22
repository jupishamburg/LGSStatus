#!/usr/bin/env python2
import bottle
from LGSStatus import app

if __name__ == "__main__":
	bottle.run(app, host="0.0.0.0", port="8080", server="tornado")
