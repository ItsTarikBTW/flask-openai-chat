from flask import Flask, render_template, request, Response, session
from modules.openai_handler import OpenAIHandler
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key'
openai_handler = OpenAIHandler()

@app.route('/')
def index():
    if 'api_key' not in session:
        return render_template('setup.html')
    return render_template('chat.html')

@app.route('/setup', methods=['POST'])
def setup():
    api_key = request.form['api_key']
    session['api_key'] = api_key
    openai_handler.initialize(api_key)
    return {'success': True}

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    message = request.args.get('message')
    if not message:
        return Response(
            f"data: {json.dumps({'error': 'No message provided'})}\n\n", 
            mimetype='text/event-stream'
        )

    if 'api_key' not in session:
        return Response(
            f"data: {json.dumps({'error': 'API key not set'})}\n\n",
            mimetype='text/event-stream'
        )

    try:
        openai_handler.initialize(session['api_key'])
        
        def generate():
            try:
                stream = openai_handler.get_stream_response(message)
                for chunk in stream:
                    if chunk.choices[0].delta.content is not None:
                        yield f"data: {json.dumps({'content': chunk.choices[0].delta.content})}\n\n"
            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return Response(generate(), mimetype='text/event-stream')
        
    except Exception as e:
        return Response(
            f"data: {json.dumps({'error': str(e)})}\n\n",
            mimetype='text/event-stream'
        )

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    except Exception as e:
        print(f"Error starting server: {e}")
        # Try alternate port if first fails
        try:
            app.run(host='0.0.0.0', port=8080, debug=True)
        except Exception as e:
            print(f"Could not start server on alternate port: {e}")