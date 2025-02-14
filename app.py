from flask import Flask, request, render_template, jsonify

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
            <h1>Hello, Flask! Check on Update. New CICD/h1>
            <button onclick="showMessage()">Click Me</button>
            <p id="content"></p>
        </body>
    </html>
    """
