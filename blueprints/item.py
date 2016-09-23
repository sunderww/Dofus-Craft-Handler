from flask                  import *
from models.item.item       import Item

item_bp = Blueprint('item', __name__)

@item_bp.route('/items/<type_str>', methods=['GET'])
def get_items_by_type(type_str):
    min_lvl = request.args.get('min', 1)
    max_lvl = request.args.get('max', 200)

    items = Item.query.filter(Item.type == type_str,
                              Item.lvl >= min_lvl,
                              Item.lvl <= max_lvl)
    return jsonify(items=Item.serialize_list(items))


@item_bp.route('/items', methods=['GET'])
def get_items_by_name():
    name = request.args.get('name', None)
    min_lvl = request.args.get('min', 1)
    max_lvl = request.args.get('max', 200)
    if name is None:
        return jsonify(items={})

    name_format = '%{0}%'.format(name)
    items = Item.query.filter(Item.name.like(name_format),
                              Item.lvl >= min_lvl,
                              Item.lvl <= max_lvl)
    return jsonify(items=Item.serialize_list(items))

@item_bp.route('/items/<id>/recipe', methods=['GET'])
def get_item_recipes(id):
    item = Item.query.get(id)
    return jsonify(item.serialize(recipe=True))
