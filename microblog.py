from application import create_app, db, cli
from application.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shall_context():
    return {'db': db, 'User': User, 'Post': Post}