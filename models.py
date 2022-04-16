from app import db


# name, username, password, email, avatar, gender
class CleverUsers(db.Model):
    U_Id = db.Column(db.Integer, primary_key=True)
    U_Name = db.Column(db.String(40), unique=False, nullable=False)
    U_Username = db.Column(db.String(20), unique=False, nullable=False)
    U_Password = db.Column(db.String(120), unique=False, nullable=False)
    U_Email = db.Column(db.String(80), unique=False, nullable=False)
    U_Score = db.Column(db.String(20), unique=False, nullable=True)
    U_CharacterName = db.Column(db.String(20), unique=False, nullable=False)
    U_Gender = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<UserID %r>' % self.U_Id


class GameInstance(db.Model):
    GaI_Id = db.Column(db.Integer, primary_key=True)
    GaI_user_id = db.Column(db.String(80), unique=False, nullable=False)
    GaI_date = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<UserID %r>' % self.GaI_user_id


class Music(db.Model):
    Mus_Id = db.Column(db.Integer, primary_key=True)
    Mus_Name = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Lenght = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Artist = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Licence = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<MusicId %r>' % self.Mus_Id


db.create_all()
