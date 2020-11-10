import os
from flask import Flask
from fbapp.views import app
from fbapp import models

# Connect sqlalchemy to app
models.db.init_app(app)


@app.cli.command("init_db")
def init_db():
    models.init_db()
