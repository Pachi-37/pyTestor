from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello, World!'


@app.route('/<username>')
def hello_user(username):
    return 'Hello, {}!'.format(username)


@app.route('/args')
def hello_user_args():
    return 'Hello, {}! Key: {}.'.format(request.args.get('username'), request.args.get("key"))


if __name__ == '__main__':
    app.run(debug=True)
