from tests2 import create_app

app, socketio = create_app()


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    #app.run(debug=True, host="localhost", port=80)
    socketio.run(app, debug=True, host="localhost", port=80)
    #socketio.run(app, debug=False, host="5.196.27.195", port=80)
