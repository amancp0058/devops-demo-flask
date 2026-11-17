from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory sample data: this demo does not need MySQL or Redis.
tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Test the DevOps platform", "completed": False},
]

@app.route("/")
def home():
    return """
    <h1>Developer Demo Application</h1>
    <p>This Flask application is ready to be analyzed and deployed.</p>
    <ul>
      <li><a href="/tasks">View tasks</a></li>
      <li><a href="/health">Health check</a></li>
    </ul>
    """

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"count": len(tasks), "tasks": tasks})

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A non-empty title is required"}), 400

    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title.strip(),
        "completed": False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
