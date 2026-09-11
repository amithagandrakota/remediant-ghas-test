from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(__name__)
DATABASE = "test.db"

def get_db():
    return sqlite3.connect(DATABASE)

@app.route("/user")
def get_user():
    # INTENTIONALLY VULNERABLE: SQL injection
    username = request.args.get("username", "")
    conn = get_db()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return {"users": rows}

@app.route("/run")
def run_command():
    # INTENTIONALLY VULNERABLE: command injection
    command = request.args.get("command", "")
    result = subprocess.check_output(command, shell=True, text=True)
    return {"output": result}

@app.route("/file")
def read_file():
    # INTENTIONALLY VULNERABLE: path traversal
    filename = request.args.get("filename", "")
    with open(os.path.join("/tmp", filename), "r") as f:
        return {"content": f.read()}

if __name__ == "__main__":
    app.run(debug=True)
