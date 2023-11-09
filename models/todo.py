from app.database import db

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(200))
	complete = db.Column(db.Boolean)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return self.text

# from app import db

# class Todo(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # text = db.Column(db.String(200))
    # complete = db.Column(db.Boolean)

    # def __repr__(self):
    #     return self.text
