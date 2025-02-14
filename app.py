from flask import Flask, request, render_template, jsonify
import git  # GitPython library

app = Flask(__name__)

@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./lcaifu')
    origin = repo.remotes.origin
    repo.create_head('main',
                     origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200

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
            <h1>Hello, Flask! Update123333/h1>
            <button onclick="showMessage()">Click Me</button>
            <p id="content"></p>
        </body>
    </html>
    """
