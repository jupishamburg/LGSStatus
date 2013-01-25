LGSStatus
=========

[![Build Status](https://travis-ci.org/jupishamburg/LGSStatus.png)](https://travis-ci.org/jupishamburg/LGSStatus)

This is a project of the youth organization Junge Piraten Hamburg (Young Pirates Hamburg).

In times of the Internet of things, we made made our branch office realize:

* if it is open
* if the state of the office changes (open/closed) it will tweet about it
* how much heat is generated
* how many clients are connected to the local network

The whole project consists of three aspects:

* Arduino with photosensor
 * measures the photons and sends the data to the Raspberry Pi
 * measures the heat
* Raspberry Pi
 * Posts all the relevant things to the webservice
* Webservice
 * stores all the data in a SQLite database
 * generates nice graphic representation of the aggregated data
 * Tweets all the things

The Twitter account is: https://twitter.com/LGSHH

The webservice can be found: http://lgs-hh.geheimorganisation.org/
