# When you put classes into models.py, there is a circular import
# models imports app, app imports model
# so imports don't work
# Fix: in app, from models import ... after db