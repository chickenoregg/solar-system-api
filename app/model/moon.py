from app import db


class Moon(db.Model):
    moon_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String) 
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)


    def to_dict(self):
        return {
            "id": self.moon_id,
            "name": self.name,

        }

    @classmethod
    def from_dict(cls, moon_data):  
        return cls(
            name=moon_data["name"],

        )
