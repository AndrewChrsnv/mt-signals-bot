from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '7692126891:AAHn7XXYsfoXFD_naFFKq7ROsCD28fkDkys'
CHAT_ID = '275651242'


def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=data)


@app.route('/alert', methods=['POST'])
def alert():
    token = request.args.get('token')
    if token != SECRET:
        return '❌ Доступ запрещён', 403
    try:
        if request.is_json:
            data = request.get_json()
            message = data.get('message', '🚨 (пустое сообщение)')
        else:
            message = request.data.decode('utf-8') or '🚨 (не JSON запрос)'
        send_telegram_message(message)
        return 'OK'
    except Exception as e:
        return f'Ошибка: {str(e)}', 500


@app.route('/')
def home():
    return 'Работает сервер!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

response = requests.get('https://api.github.com')
print("Status:", response.status_code)
