import secrets

from flask import Flask, jsonify, render_template, send_from_directory, redirect, request, session
import dotenv
import os
import requests

from flask_caching import Cache

dotenv.load_dotenv()

DISCORD_CLIENT_ID = os.environ.get('DISCORD_CLIENT_ID')
DISCORD_CLIENT_SECRETS = os.environ.get('DISCORD_CLIENT_SECRETS')
DISCORD_REDIRECT_URI = os.environ.get('DISCORD_REDIRECT_URI')

app = Flask(
    __name__,
    static_folder="dist/assets",
    template_folder="dist"
)
app.secret_key = os.environ.get('SESSION_KEY')

cache = Cache(app, config={'CACHE_TYPE': 'FileSystemCache', 'CACHE_DIR': "flask_cache"})

@app.route("/")
def index():
    return send_from_directory("dist", "index.html")

@app.route("/<path:path>")
def react_app(path):
    return send_from_directory("dist", "index.html")

@app.route("/favicon.png")
def favicon():
    return send_from_directory("dist", "favicon.png")

@app.get("/api/login")
def api_login():
    code = secrets.token_urlsafe(32)
    response = redirect(f"https://discord.com/oauth2/authorize?client_id={DISCORD_CLIENT_ID}&response_type=code&redirect_uri={DISCORD_REDIRECT_URI}&scope=identify+email+guilds&state={code}")
    response.set_cookie("state", code, max_age=60 * 5)
    return response

@app.get("/api/logout")
def api_logout():
    session.pop('user_info', None)
    session.pop('access_token', None)
    return redirect("/")

@app.get("/api/callback")
def api_callback():
    params = request.args
    if not params:
        return redirect("/")

    state = request.cookies.get("state")
    if params.get("state") != state:
        return redirect("/")

    authorization_code = params.get("code")

    request_postdata = {
        "client_id": DISCORD_CLIENT_ID,
        "client_secret": DISCORD_CLIENT_SECRETS,
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": DISCORD_REDIRECT_URI,
    }
    accesstoken_request = requests.post(
        "https://discord.com/api/oauth2/token", data=request_postdata
    )
    responce_json = accesstoken_request.json()

    if "access_token" not in responce_json:
        return jsonify(
            {"status": "error", "reason": "Discord OAuth token request failed"}
        ), 400

    access_token = responce_json["access_token"]

    user_info = requests.get(
        "https://discord.com/api/users/@me",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()

    if user_info is None:
        return redirect("/api/login")

    guilds = requests.get(
        "https://discord.com/api/users/@me/guilds",
        headers={"Authorization": f"Bearer {access_token}"},
    ).json()

    session['user_info'] = user_info
    session['access_token'] = access_token
    return redirect("/?login=true")

@app.get("/api/user_info")
def api_userinfo():
    user_info = session.get('user_info')
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({
            "status": "error",
            "error": "ログインしていません。"
        }), 401

@app.get("/api/guilds")
@cache.cached(timeout=30) 
def api_guilds():
    access_token = session.get('access_token')
    if access_token:
        guilds = requests.get(
            "https://discord.com/api/users/@me/guilds",
            headers={"Authorization": f"Bearer {access_token}"},
        ).json()
        return jsonify(guilds)
    else:
        return jsonify({
            "status": "error",
            "error": "サーバーが不明"
        }), 401

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)