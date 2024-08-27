#!/usr/bin/env python3
"""Flask app with internationalization support"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route for the home page"""
    home_title = gettext('home_title')
    home_header = _('home_header')
    return render_template('3-index.html',
                           home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run(debug=True)
