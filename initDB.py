'''
Initializes Postgres database tables. Use after creating the
Postgres database and before running the server for the first time.
'''
from strabo import schema

from strabo import db

if __name__ == '__main__':
    # This function loads in the proper sql
    schema.Base.metadata.create_all(db.engine)
    db.session.commit()
