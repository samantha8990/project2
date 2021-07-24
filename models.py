def create_classes(db):
    class Combined_table(db.Model):
        __tablename__ = 'Combined_table'

        State = db.Column(db.String(255), primary_key=True)
        CNTYFIPS=db.Column(db.String(255))
        Solved = db.Column(db.String(30))
        Year = db.Column(db.Integer)
        Month=db.Column(db.String(255))
        Incident=db.Column(db.String(255))
        Homicide=db.Column(db.String(255))
        VicAge=db.Column(db.String(255))
        VicRace=db.Column(db.Integer)
        OffAge=db.Column(db.Integer)
        OffSex=db.Column(db.String(255))
        Weapon=db.Column(db.String(255))
        Relationship=db.Column(db.String(255))
        VicCount=db.Column(db.Integer)
        OffCount=db.Column(db.Integer)
        latitude=db.Column(db.Float)
        longitude=db.Column(db.Float)
        name=db.Column(db.String(255))

        def __repr__(self):
            return '<Murders %r>' % (self.name)
    return Combined_table
