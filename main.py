from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# creating dictionary
pets = [{"pet": "birdo", "owner": "max", "breed": "parakeet", "color": "blue", "check-in": "no" },
        {"pet": "charles", "owner": "robert", "breed": "snake", "color": "green", "check-in": "yes" },
        {"pet": "bruce", "owner": "tom", "breed": "falcon", "color": "brown", "check-in": "no" },
        {"pet": "tang", "owner": "robert", "breed": "cat", "color": "orange", "check-in": "yes" }]


class PetHotel(Resource):
# defining GET
  def get(self):
    # setting return with KEY and VALUE
    return pets
  
  def post(self):
    pets.append({"pet": "dexter", "owner": "nick", "breed": "robot", "color": "purple", "check-in": "yes" })
    return 201

  def delete(self):
    if len(pets) > 0:    
      del pets[len(pets)-1]
      
    return '', 204 

  def patch(self):
    pets[0] = {"pet": 'TEST'}

    return 201   
   
api.add_resource(PetHotel, "/")

# @app.route("/")

if __name__ == "__main__":
  app.run(debug=True)

