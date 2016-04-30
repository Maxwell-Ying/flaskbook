CSRF_ENABLE = True
SECRET_KEY = '952167878'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://ytw@localhost/ex5'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
