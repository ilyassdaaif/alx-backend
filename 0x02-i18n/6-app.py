#!/usr/bin/env python3
"""
This module implement an i18n (internationalization) system using Flask
and Flask-Babel.
It provides functionality to support multiple languages, user-specific
locales, and localized templates.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Application configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieves the user information based on the 'login_as' query parameter.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    A Flask before_request function that is executed before every request.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Determines the best locale to use for the current request."""
    # Check URL parameter
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    # Check request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index page for the application
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(debug=True)
