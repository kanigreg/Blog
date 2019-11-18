from application import app, db 
from application.models import User, Post
from application import cli


@app.shell_context_processor
def make_shall_context():
    return {'db': db, 'User': User, 'Post': Post}