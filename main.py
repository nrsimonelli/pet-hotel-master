from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
# import psycopg2 to use Python with PostgreSQL
import psycopg2
# assign database name & location to variable "db"
db = "dbname=%s host=%s " % ('pet_hotel', 'localhost')
#  ???
schema = "schema.sql"
# initializes connection to PostgreSQL
def get_connection():
    connection = psycopg2.connect(db)
    return connection

# closes connection to PostgreSQL
def close_connection(connection):
    if connection:
        connection.close()
        print("Postgres connection is now closed")

# prints database version
def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connect to PostgreSQL version: ", db_version)
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

# runs read_database_version and tests connection to PostgreSQL
print("Printing Database version:")
read_database_version()

def select_all_pets():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """SELECT * FROM owner JOIN pet ON owner.id = pet.owner_id ORDER BY pet.id;"""
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Printing all pets")
        for row in records:
            print("Owner's name: ", row[1])
            print("Pet's name: ", row[4])
            print("Animal Breed: ", row[5])
            print("Color: ", row[6])
            print("Checked In: ", row[7])
        return records
    except (Exception, psycopg2.Error) as error:
        print("Error getting pets", error)
    finally:
        close_connection(connection)

def insert_new_pet(pet):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_insert_query = """INSERT INTO pet (owner_id, pet, breed, color, check_in) VALUES 
	(%s, %s, %s, %s, %s);"""
        cursor.execute(sql_insert_query, (pet["owner-id"], pet["pet"], pet["breed"], pet["color"], pet["check-in"]))
        connection.commit()
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting doctor's data", error)

# runs function to get all rows from pet table when server is spun up
# print("Getting all pets:")
# select_all_pets()

def delete_pet(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_delete_query = """DELETE FROM pet WHERE pet.id=%s;"""
        cursor.execute(sql_delete_query, (id,))
        connection.commit()
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error deleting pet from database", error)

def edit_checkin(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_update_query = """UPDATE pet SET check_in = False WHERE pet.id=%s;"""
        cursor.execute(sql_update_query, (id,))
        connection.commit()
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error updating checkin from database", error)



# creating dictionary
pets = [{"pet": "birdo", "owner": "max", "breed": "parakeet", "color": "blue", "check-in": "no" },
        {"pet": "charles", "owner": "robert", "breed": "snake", "color": "green", "check-in": "yes" },
        {"pet": "bruce", "owner": "tom", "breed": "falcon", "color": "brown", "check-in": "no" },
        {"pet": "tang", "owner": "robert", "breed": "cat", "color": "orange", "check-in": "yes" }]


class PetHotel(Resource):
# defining GET
  def get(self):
    # setting return with KEY and VALUE
    return select_all_pets()
  
  def post(self):
    # pets.append({"pet": "dexter", "owner": "nick", "breed": "robot", "color": "purple", "check-in": "yes" })
    pet = {"pet": "dexter", "owner-id": 1, "breed": "robot", "color": "purple", "check-in": "yes" }
    insert_new_pet(pet)
    return 201

  def delete(self, id):
    delete_pet(id)
    return '', 204 

  def patch(self, id):
    edit_checkin(id)
    return 201   
   
api.add_resource(PetHotel, "/", "/<int:id>")

# @app.route("/")

if __name__ == "__main__":
  app.run(debug=True)

