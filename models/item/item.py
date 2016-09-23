from models.shared              import db, Auditable, Serializable
from models.item.type           import ItemType
from models.item.recipe         import RecipeItem


class Item(db.Model, Serializable, Auditable):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    lvl = db.Column(db.Integer)
    type = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)


    def recipe(self):
        dct = {}
        for recipe_item in self.recipe_items:
            dct.update(recipe_item.serialize())
        return dct

    def serialize(self, **kwargs):
        attrs = Serializable.serialize(self, **kwargs)
        del attrs['recipe_items']
        del attrs['recipes_using']

        with_recipe = kwargs.get('recipe', False)
        if with_recipe:
            attrs['recipe'] = self.recipe()

        return attrs


    @staticmethod
    def get_or_create(name, type_str=None):
        item_type = ItemType.from_string(type_str)
        item = Item.query.filter_by(name=name).first()

        if item is None:
            item = Item(name=name)
            db.session.add(item)
        item.type = item_type
        return item

    @staticmethod
    def from_dict(dct):
        item = Item.get_or_create(dct['name'], type_str=dct['type'])
        item.lvl = dct['lvl']
        item.image_url = dct['image']

        recipe_string = dct['recipe']
        if recipe_string is not None:
            for (count, name) in map(lambda s: s.split(' x ', 1), recipe_string.split(' + ')):
                dest_item = Item.get_or_create(name)
                RecipeItem.make_recipe(item, dest_item, int(count))

        # Do something from recipe
        return item
