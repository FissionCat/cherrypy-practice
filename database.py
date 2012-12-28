from sqlalchemy import *

engine = create_engine("postgresql+pg8000://postgres:master@localhost/cherrypy", echo=True)
print(engine.execute("select 1").scalar())