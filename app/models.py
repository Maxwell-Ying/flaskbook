from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True, unique = True)
    author = db.Column(db.String(128), index = True)
    
    def __repr__(self):
        return '<Book %r>' % (self.name)
    
class books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), index = True)
    author = db.Column(db.String(60))
    age = db.Column(db.Integer)
    public = db.Column(db.String(20))
    home = db.Column(db.String(20))
    pages = db.Column(db.Integer)
    
    def __repr__(self):
        return '<book %r>' % (self.name)
