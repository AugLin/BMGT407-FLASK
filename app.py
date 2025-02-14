from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <script>
                function showMessage() {
                    document.getElementById('content').innerHTML = "You clicked the button!";
                }
            </script>
        </head>
        <body>
            <h1>Hello, Flask! Update 1</h1>
            <button onclick="showMessage()">Click Me</button>
            <p id="content"></p>
        </body>
    </html>
    """

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data.get("a", 0) + data.get("b", 0)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
