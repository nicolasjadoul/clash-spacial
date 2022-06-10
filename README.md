#project-1a
#
#End of year Clask-Spatial project of the TP2 group.
#To launch the game you must:
#Have python 3 installed on the machine that will act as the server.
#Have the libs. following installed (with associated commands):

sudo pip install flask
sudo pip install flask-login
sudo pip install flask-socketio
sudo pip install flask-sqlalchemy

sudo pip install --upgrade python-socketio==4.6.0

sudo pip install --upgrade python-engineio==3.13.2

sudo pip install --upgrade Flask-SocketIO==4.3.1

#To choose the server IP and the port you have to go to the file: main.py and modify line 39.
#
#Example :
# socketio.run(app, debug=false, host="192.168.0.22", port=80)
