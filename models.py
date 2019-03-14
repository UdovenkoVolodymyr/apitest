from app import db

class Auth(db.Model):
    __tablename__ = 'testdb'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    birthday = db.Column(db.String())
    timestamp = db.Column(db.Integer())

    def __init__(self, login, password, birthday, email, timestamp):
        self.login = login
        self.password = password
        self.birthday = birthday
        self.email = email
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.login,
            'author': self.password,
            'published':self.birthday
}
