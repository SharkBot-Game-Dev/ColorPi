from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
async def index():
    return render_template()

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)