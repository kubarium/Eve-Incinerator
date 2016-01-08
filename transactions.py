import sqlite3
import json
from flask import g

class Transactions:


    def __init__(self, database = "sqlite-latest.sqlite"):

        self.conn = sqlite3.connect(database)
        self.conn.text_factory = lambda x: str(x, 'latin1')
        self.cur = self.conn.cursor()


    def searchByItemName(self, name):
        cur = self.cur

        cur.execute("SELECT typeID as id, typeName as name, description FROM invTypes WHERE typeName LIKE ? AND published = 1 ORDER BY typeID", ("%"+name+"%",))

        list = [dict(zip(map(lambda x:x[0], cur.description), row)) for row in cur.fetchall()]

        data = {
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


        query = "SELECT typeID as id, typeName as name, description FROM invTypes WHERE published=1 AND (" + " OR ".join(("typeID = " + str(blueprint) for blueprint in blueprints)) + ") ORDER BY name"
        cur.execute(query)

        #typeID IN (?) ORDER BY typeID", (",".join(str(blueprint) for blueprint in blueprints)))

        list = [dict(zip(map(lambda x:x[0], cur.description), row)) for row in cur.fetchall()]

        data = {
            "package":list
        }

        return json.dumps(data)