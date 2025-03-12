from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

app = Flask(__name__)

# Khởi tạo client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Route cho trang chủ
@app.route('/blogger/')
def blogger_home():
    return render_template('index.html')

# Route cho trang tools
@app.route('/blogger/apps/tools.html')
def tools():
    return render_template('tools.html')

# Route cho trang chatgpt
@app.route('/blogger/apps/tools/chatgpt.html')
def chatgpt():
    return render_template('tools/chatgpt.html')

# Route cho API chat
@app.route('/api/chat', methods=['POST'])
def chat():
    # Lấy tin nhắn từ người dùng
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Gửi tin nhắn đến GPT-4o
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Sử dụng GPT-4o
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Trả về phản hồi từ GPT-4o
        bot_message = response.choices[0].message.content
        return jsonify({"message": bot_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=10000, debug=False)
