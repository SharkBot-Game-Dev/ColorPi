from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    static_folder="dist/assets",
    template_folder="dist"
)

@app.route("/")
def index():
    return send_from_directory("dist", "index.html")

@app.route("/<path:path>")
def react_app(path):
    return send_from_directory("dist", "index.html")

@app.route("/favicon.png")
def favicon():
    return send_from_directory("dist", "favicon.png")

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)