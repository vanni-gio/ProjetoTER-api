from app import app


if __name__ == '__main__':
    app.run(debug=True, port=5683, ssl_context=('server-public-key.pem','server-private-key.pem'))