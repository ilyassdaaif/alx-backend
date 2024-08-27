#!/usr/bin/env python3
"""Flask app with locale selector"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_local():
    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route for the home page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
