from flask import Flask, request, render_template,jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "strawbebbies"


context = app.app_context()
context.push()
connect_db(app)
db.create_all()


@app.route('/')
def show_home_page():
    """Shows home page"""

    return render_template("home.html")




@app.route('/api/cupcakes', methods=["GET"])
def list_all_cupcakes():
    """Returns JSON data for all cupcakes"""

    cupcakes = [cupcake.serialize_cupcake() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)



@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Create new cupcake and returns JSON data """

    data = request.json


    cupcake = Cupcake(
    flavor = data['flavor'],
    size = data['size'],
    rating = data['rating'],
    image = data['image'] or None)

    

    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize_cupcake()),201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["GET"])
def show_cupcake(cupcake_id):
    """Returns JSON data for one cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    return jsonify(cupcake=cupcake.serialize_cupcake())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Updates cupcake data"""
    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

   
    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating'],
    cupcake.image = data['image'] 

    
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize_cupcake()))


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes cupcake data"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")




   
