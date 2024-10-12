from flask import request, jsonify, current_app
from . import db
from .models import QuestionAnswer
import openai

def register_routes(app):
    @app.route('/ask', methods=['POST'])
    def ask_question():
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided'}), 400

        question = data['question']
        openai.api_key = current_app.config['OPENAI_API_KEY']

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}]
            )
            answer = response.choices[0].message['content'].strip()
        except Exception as e:
            return jsonify({'error': str(e)}), 500

        qa = QuestionAnswer(question=question, answer=answer)
        db.session.add(qa)
        db.session.commit()

        return jsonify({'question': question, 'answer': answer}), 200
