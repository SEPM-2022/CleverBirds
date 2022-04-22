from app import db 


class GameInstance(db.Model):
    GaI_Id = db.Column(db.Integer, primary_key=True)
    GaI_user_id = db.Column(db.String(80), unique=False, nullable=False)
    GaI_date = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<UserID %r>' % self.GaI_user_id

