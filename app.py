# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, request


SERVE_DOMAINS = [
    '1byte.click',
    'www.poofpayment.com',
    'www.generativeblock.com'
]

app = Flask(__name__, host_matching=True, static_host = SERVE_DOMAINS[0])


def index():
    return f'Host recognized: {request.headers["Host"]}'

for domain in SERVE_DOMAINS:
    app.add_url_rule('/', 'index', index, host=domain)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)

