from models.shared          import db, Serializable

class RecipeItem(db.Model, Serializable):
    from_item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    dest_item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    count = db.Column(db.Integer)

    from_item = db.relationship('Item', foreign_keys=[from_item_id],
        backref=db.backref('recipe_items', lazy="dynamic", cascade="all, delete-orphan"))
    dest_item = db.relationship('Item', foreign_keys=[dest_item_id],
        backref=db.backref('recipes_using', lazy="dynamic", cascade="all, delete-orphan"))

    @staticmethod
    def make_recipe(from_item, dest_item, count):
        recipe = RecipeItem.query.filter(RecipeItem.from_item == from_item,
                                         RecipeItem.dest_item == dest_item).first()
        if recipe is None:
            print('Create recipe from %s : %d %s' % (from_item.name, count, dest_item.name))
            recipe = RecipeItem(from_item=from_item, dest_item=dest_item)
            db.session.add(recipe)
        recipe.count = count
        return recipe

    def serialize(self, **kwargs):
        return { self.dest_item.name: self.count }
