def create_classes(db):
    class Combined_table(db.Model):
        __tablename__ = 'Combined_table'

        state = db.Column(db.String(255), primary_key=True)
        Solved = db.Column(db.String(30))
        Year = db.Column(db.Integer)
        CNTYFIPS=db.Coumn(db.String(255))
        Month=db.Coumn(db.String(255))
        Incident=db.Coumn(db.String(255))
        Homicide=db.Coumn(db.String(255))
        VicAge=db.Coumn(db.String(255))
        VicRace=db.Coumn(db.Integer)
        OffAge=db.Coumn(db.Integer)
        OffSex=db.Coumn(db.String(255))
        Weapon=db.Coumn(db.String(255))
        Relationship=db.Coumn(db.String(255))
        VicCount=db.Coumn(db.Integer)
        OffCount=db.Coumn(db.Integer)
        latitude=db.Coumn(db.Decimal)
        longitude=db.Coumn(db.Decimal)
        name=db.Coumn(db.String(255))

        def __repr__(self):
            return '<Murders %r>' % (self.name)
    return Combined_table
