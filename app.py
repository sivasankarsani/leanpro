from flask import Flask
from flask_restful import Resource, Api, jsonify,request, reqparser
from flask_jwt import JWT, jwt_required

from security import authenticate, identify

app = Flask(__name__)

app.secret_key = "sankar"

api = Api(app)

jwt = JWT(app, authenticate,identify) # /auth it created new endpoint

items = []

class ItemList(Resource):
	def get(self):
		return {"items": items}

class Item(Resource):
	parser = reqparser.RequestParser()
		parser.add_argument('price',
			type = float,
			required = True,
			help = "This field can not empty"
		)

	@jwt_required()
	def get(self,name):
		item_data = next(list(filter(lambda item: item['name']==name , items)),None)
		return {'item':item_data}, 200 if item_data else 404

	def post(self,name):
		if next(filter(lambda item: item['name'] in name , items),None):
			return {"msg":"item was already exists {}".format(name)}, 401

		body_data = Item.parser.parse_args() 
		item 	  = {'name':name,"price":body_data['price']}
		items.append(item)

	def delete(self,name):
		global items
		items = list(filter(lambda item: item['name']!= name, items))
		return {"msg": "{} is deleted".format(item['name'])},200

	def put(self,name):
		
		body_data = Item.parser.parse_args() 
		item 	  = next(filter(lambda item: item['name'] in name , items),None)

		items.append({"name":name,"price":body_data['price']}) if not item else item.update(body_data)

		return item


#localhost:port/student/sankar
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/getitems/')


# To the server 
app.run(port=8000)

	

