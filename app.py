
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
next_id = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if title:
            tasks.append({
                "id": next_id,
                "title": title,
                "completed": False
            })
            next_id += 1

        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
