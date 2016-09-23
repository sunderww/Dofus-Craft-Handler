class ItemType(object):
    DEFAULT     = 'resource'

    AMULET      = 'amulette'
    BACKPACK    = 'sac'
    BELT        = 'ceinture'
    BOOTS       = 'botte'
    CLOAK       = 'cape'
    HAT         = 'chapeau'
    RING        = 'anneau'
    SHIELD      = 'bouclier'
    TROPHY      = 'trophee'

    class Weapons(object):
        AXE     = 'hache'
        BOW     = 'arc'
        DAGGER  = 'dague'
        HAMMER  = 'marteau'
        PICKAXE = 'pioche'
        SCYTHE  = 'faux'
        SHOVEL  = 'pelle'
        STAFF   = 'baton'
        SWORD   = 'epee'
        WAND    = 'baguette'

        ALL = [
            AXE,
            BOW,
            DAGGER,
            HAMMER,
            PICKAXE,
            SCYTHE,
            SHOVEL,
            STAFF,
            SWORD,
            WAND,
        ]

    ALL = [
        AMULET,
        BACKPACK,
        BELT,
        BOOTS,
        CLOAK,
        HAT,
        RING,
        SHIELD,
        TROPHY,
    ] + Weapons.ALL

    @classmethod
    def from_string(cls, string):
        for type_str in cls.ALL:
            if string == type_str:
                return string
        return cls.DEFAULT
