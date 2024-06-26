from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({"response": "Received", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
