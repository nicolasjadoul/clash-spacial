# projet-1a
#
#Projet de fin d'année Clask-Spatial du groupe TP2.
#Pour lancer le jeu il faut :
#Avoir python 3 installer sur la machine qui fera office de serveur.
#Avoir les lib. suivantes d'installées (avec les commandes associées):

sudo pip install flask
sudo pip install flask-login
sudo pip install flask-socketio
sudo pip install flask-sqlalchemy

sudo pip install --upgrade python-socketio==4.6.0

sudo pip install --upgrade python-engineio==3.13.2

sudo pip install --upgrade Flask-SocketIO==4.3.1

#Pour choisir l'IP du serveur et le port il faut aller dans le fichier : main.py et modifier la ligne 39.
#
#Exemple :
#       socketio.run(app, debug=false, host="192.168.0.22", port=80)
