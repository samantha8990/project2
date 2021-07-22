def create_classes(db):
    class Combined_table(db.Model):
        __tablename__ = 'Combined_table'

        state = db.Column(db.String(255), primary_key=True)
        Solved = db.Column(db.String(30))
        Year = db.Column(db.Integer)

        def __repr__(self):
            return '<Murders %r>' % (self.name)
    return Combined_table
