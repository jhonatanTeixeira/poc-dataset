from container import container

db = container.db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DataSetColumn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DataSetAttribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DataSetValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('data_set_attribute.id'), nullable=False)
    column_id = db.Column(db.Integer, db.ForeignKey('data_set_column.id'), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
    name = db.Column(db.String)

    attribute = db.relationship(DataSetAttribute, backref=db.backref('values'))
    item = db.relationship(Item, backref=db.backref('values'))
    column = db.relationship(DataSetColumn, backref=db.backref('values'))
