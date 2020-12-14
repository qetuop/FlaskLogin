from project import db, create_app

app = create_app() # this will call db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()