# ToiLaser

Made for SwampHacks 2021

## Illumination for Urination

[![](http://img.youtube.com/vi/Jrh0NJqjG1E/0.jpg)](http://www.youtube.com/watch?v=Jrh0NJqjG1E "")

## Setup
A comprehensive guide to setup is provided in [`README_setup.md`](README_setup.md).  
TODO: finish setup guide.

### Database

Create a CockroachDB instance, following [steps 1-3](https://www.cockroachlabs.com/docs/v20.2/build-a-python-app-with-cockroachdb) creating a database named `toilaser`, a user named `db_user` with password `password`.  

Copy your port number and paste it in the value for `PORT` in `db_interface.py`.

Install the libraries needed in `requirements.txt`.

Open a python3 session in the root of this directory. and run the following:

```python
from db_interface import  *

conn = create_connection()
create_table(conn)
```

Your database is now initialized!


### MQTT server

Ensure you have `mosquitto` installed and running on the computer you are hosting your CockroachDB instance on.

Run `mqtt_server.py`

### Microcontroller

Configure `microcontrollers/src/toilaser.ino`, you will need to enter your WiFi information and the IP address of the server that you have `mqtt_server.py` running on.  
Wouldn't a circuit diagram be nice? If only there were more time!

After configuration, install the file to any MCU with an ESP8266 chip (a NodeMCU was used in development). Attach hardware to pins listed in the file. Plug in your MCU, aim the laser at the bottom of your toilet bowl, and enjoy!

## Low-tech Solution
If you are ok with missing out on data collection, this can be accomplished with batteries, a PIR sensor
