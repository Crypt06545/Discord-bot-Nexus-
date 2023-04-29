from flask import Flask, render_template, request, redirect, session,flash
from dotenv import load_dotenv
from Oauth import Oauth
import os
import json

from threading import Thread

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def getInfo():
    code =request.args.get("code")
    token=Oauth.get_access_token(code)
    user=Oauth.get_user_json(token)
    guilds=Oauth().get_guilds(token)

    session['user']=user
    session['servers']=guilds
    return redirect("/dashboard")


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if session.get("user") is None:
        return redirect("/auth")

    user=session.get("user")
    servers=session.get("servers")

    if request.method=='POST':
        server=request.form['server']
        prefix=request.form['prefix']
        channel=request.form['channel']

        # set welcome channle and message
        if channel :
            with open("channel.json") as f:
                data=json.load(f)
            with open("channel.json", "w") as f:
                data[server]=channel
                json.dump(data, f)

        # set prefix 
        if  prefix :
            with open("prefixes.json") as f:
                prefixJson=json.load(f)
            with open("prefixes.json", 'w') as f:
                prefixJson[server]=prefix
                json.dump(prefixJson, f)
        


        flash("Saved changess")

    return render_template("index.html", username=f"{user.get('username')}#{user.get('discriminator')}", id=user.get('id'), avatar=user.get('avatar'), servers=servers)



@app.route("/auth")
def auth():
    return render_template("auth.html",discord_url=Oauth.discord_login_url)

@app.route("/logout")
def logout():
    user=session.pop("user", None)
    user=session.pop("servers", None)
    return redirect("/auth")


@app.route("/about")
def about():
    return render_template("about.html")

def run():
  app.run(

	port=5000
	)


def keep_alive():

	t = Thread(target=run)
	t.start()