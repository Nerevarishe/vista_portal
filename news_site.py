from app import app, db, cli
from app.models import User, News


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'News': News}