import sqlite3
import json

class Transactions:


    def __init__(self, database = "evedb.sqlite"):

        self.conn = sqlite3.connect(database)
        self.conn.text_factory = lambda x: str(x, 'latin1')
        self.cur = self.conn.cursor()


    def searchByItemName(self, name):
        cur = self.cur

        cur.execute("""
            SELECT typeID as id, typeName as name, description FROM invTypes i
            LEFT OUTER JOIN invGroups ig ON ig.groupID = i.groupID
            LEFT OUTER JOIN invCategories ic ON ic.categoryID = ig.categoryID
            WHERE ic.categoryID IS NOT 9
            AND i.published = 1
            AND i.typeName LIKE ?
            ORDER BY i.typeName
            """, ("%"+name+"%",))
        '''
        cur.execute("""
            SELECT typeID as id, typeName as name, description FROM invTypes i
            WHERE i.published = 1
            AND i.typeName LIKE ?
            ORDER BY i.typeName
            """, ("%"+name+"%",))
        '''
        list = [dict(zip(map(lambda x:x[0], cur.description), row)) for row in cur.fetchall()]

        data = {
            "items":True,
            "package":list
        }

        return json.dumps(data)

    def cook(self, ingredients):
        cur = self.cur

        cauldron = []

        for ingredient in ingredients:
            cur.execute("SELECT typeID FROM industryActivityMaterials WHERE materialTypeID = ? ORDER BY typeID", (ingredient,))

            listOfBlueprints = [row[0] for row in cur.fetchall()]

            cauldron.append(set(listOfBlueprints))

        blueprints = cauldron.pop(0)

        for spit in cauldron:
            blueprints = blueprints.intersection(spit)

        if blueprints :
            query = "SELECT typeID as id, typeName as name, description FROM invTypes WHERE published=1 AND (" + " OR ".join(("typeID = " + str(blueprint) for blueprint in blueprints)) + ") ORDER BY name"
            cur.execute(query)

            list = [dict(zip(map(lambda x:x[0], cur.description), row)) for row in cur.fetchall()]
        else:
            list = []

        data = {
            "blueprints":True,
            "package":list
        }

        return json.dumps(data)