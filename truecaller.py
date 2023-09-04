from flask import Flask, jsonify
from flask_restful import Api, Resource
from truecallerpy import search_phonenumber
import asyncio

app = Flask(__name__)
api = Api(app)
id = "a1i0U--hhlRXWkXFhHLbJRXiCLRKoWJFCYgfgotZqrsfl2JQK4NQwjpDp6x-cDrJ"

async def search_and_return(number):
    try:
        result = await search_phonenumber(number, 'IN', id)
        return result
    except Exception as e:
        return {"error": str(e)}

class TruecallerFind(Resource):
    def get(self, number):
        result = asyncio.run(search_and_return(number))
        return jsonify(result)

api.add_resource(TruecallerFind, "/truecaller/<int:number>")

if __name__ == "__main__":
    app.run(debug=True)


