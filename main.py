import threading
import time

from prod import create_app
from prod.game.game import Game
from flask_cors import CORS

app, socketio = create_app()
CORS(app)


class GameThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        Game.start()
        while True:
            # TODO : if datetime.now().minute == 30: --> next turn
            time.sleep(5)
            Game.next_turn()

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    # Game thread
    GameThread().start()

    # Web server running on the main thread
    #app.run(debug=True, host="localhost", port=80)
    socketio.run(app, debug=True, host="localhost", port=80)
    #socketio.run(app, debug=False, host="5.196.27.195", port=80)
