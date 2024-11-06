from flask import Flask, request, g
from readings_db import ReadingsDB
import bcrypt
from session_store import SessionStore
from passlib.hash import bcrypt

session_store = SessionStore()

class MyFlask(Flask):
    def add_url_rule(self,rule,endpoint=None,view_func=None,**options):
        return super().add_url_rule(rule,endpoint,view_func,provide_automatic_options=False,**options)
    


    # Check if the session ID is present in cookie data
def load_session_data():
    session_id = request.cookies.get("session_id")

    # if the session ID is present:
    if session_id:
        # load the session data using the session ID 
        session_data = session_store.getSession(session_id)


    # if the session ID is missing or invalid data could not be loaded:
    if session_id == None or session_data == None:
        # create a new session & session ID 
        session_id = session_store.createSession()
        # load the session data using the session ID 
        session_data = session_store.getSession(session_id)

    #save both session id and session data for use in other functions
    #so we can send with cookie
    g.session_id = session_id
    #how we manipulate/use the users session storage
    g.session_data = session_data








    
app = MyFlask(__name__)

@app.before_request
def before_request_func():
    load_session_data()

#decorator 
@app.after_request
def after_request_func(response):
    print("session ID:", g.session_id)
    print("session data:", g.session_data)
    # send a cookie to the client with the session ID
    response.set_cookie("session_id",g.session_id, samesite = "None", secure= True)
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin")
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response


#@app.route("/readings/<int:readings>",methods=["OPTIONS"])
@app.route("/<path:path>",methods=["OPTIONS"])
def cors_preflight(path):
    return "", {
        # one,
        #"Access-Control-Allow-Origin": "*",
        # two,
        "Access-Control-Allow-Headers": "Content-Type",
        # three headers
        "Access-Control-Allow-Methods": "GET, POST, DELETE, PUT, OPTIONS"
    }

cards = [{
    "tarotName": "Death",
    "imagePath": "images/death.jpeg",
    "tarotDescription": "Death represents transformation, endings and new beginnings. When the Death card shows up it tells you that things will not be the same again. A transformation is taking place, you are growing and changing with the circumstances you find yourself in."
}, {
    "tarotName": "Judgement",
    "imagePath": "images/judgement.jpeg",
    "tarotDescription": "Judgement represents taking responsibility for your actions and your life, being a good judge of character, seeing the truth and knowing what you want. The Judgement card often shows up when you need to step up and be a leader, speaking the truth and being more assertive."
}, {
    "tarotName": "Justice",
    "imagePath": "images/justice.jpeg",
    "tarotDescription": "Justice represents all kinds of legal matters, the spiritual laws of truth and cause and effect. When the Justice card shows up it reminds us to be lawful and fair to achieve the best result."
}, {
    "tarotName": "Strength",
    "imagePath": "images/strength.jpeg",
    "tarotDescription": "Strength represents our courage, passions, strength, self-confidence, patience, and compassion. Strength reminds us to follow our passions, to take the time to do the things that make us tick, that makes us strong within ourselves and which builds confidence and self-worth."
}, {
    "tarotName": "Temperance",
    "imagePath": "images/temperance.jpeg",
    "tarotDescription": "Temperance represents a balanced interaction between the elements to create something new and fresh. Temperance includes all the elements in such a way that it brings out the best of each substance. When the Temperance card shows up in your life there is great balance and strength between the different areas and people in your life that are working together."
}, {
    "tarotName": "The Chariot",
    "imagePath": "images/theChariot.jpeg",
    "tarotDescription": "Chariot represents your willpower and determination. It represents victory. The Chariot gives you the green light to charge ahead and take control of your life or an area of your life that needs your attention."
}, {
    "tarotName": "The Devil",
    "imagePath": "images/theDevil.jpeg",
    "tarotDescription": "Devil represents the primal source of behaviour that shows itself in the form of our desires and earthly needs. It also represents our fears that cause addiction and compulsive behaviour."
}, {
    "tarotName": "The Emperor",
    "imagePath": "images/theEmperor.jpeg",
    "tarotDescription": "Emperor represents masculine energy, the ruler, the head of the household, head of a company, organisation, and communities. The Emperor is an authority figure that creates a solid foundation to build and create on."
}, {
    "tarotName": "The Empress",
    "imagePath": "images/theEmpress.jpeg",
    "tarotDescription": "Empress represents feminine power, a nurturer and a family oriented person, our mother or a mother figure, abundance, femininity, fertility and the love of the home and family."
}, {
    "tarotName": "The Fool",
    "imagePath": "images/theFool.jpeg",
    "tarotDescription": "Fool represents new beginnings, having faith in the future, being inexperienced, not knowing what to expect, having beginners luck, improvising, believing that the Universe provides, having no strings attached, being carefree."
}, {
    "tarotName": "The Hanged Man",
    "imagePath": "images/theHangedMan.jpeg",
    "tarotDescription": "Hanged Man represents being temporarily suspended. Life is on hold, but it serves a purpose. You will have a realisation that will show you what is truly important in your life."
}, {
    "tarotName": "The Heirophant",
    "imagePath": "images/theHeirophant.jpeg",
    "tarotDescription": "Hierophant represents group consciousness, religion, your belief system, ceremony, traditions, kindness, charity, giving guidance in the form of spiritual counseling."
}, {
    "tarotName": "The Hermit",
    "imagePath": "images/theHermit.jpeg",
    "tarotDescription": "Hermit represents spending time alone, being a lone wolf, soul-searching, seeking spiritual guidance, introspection."
}, {
    "tarotName": "The High Priestess",
    "imagePath": "images/theHighPriestess.jpeg",
    "tarotDescription": "High Priestess represents secrets, mystery, intuition, wisdom, making the impossible become possible, and magic."
}, {
    "tarotName": "The Lovers",
    "imagePath": "images/theLovers.jpeg",
    "tarotDescription": "Lovers represent love and relationship, soul mates, physical attractions, choices to be made, The Lovers represents doing the things that make us feel whole, being with the people who make us feel whole."
}, {
    "tarotName": "The Magician",
    "imagePath": "images/theMagician.jpeg",
    "tarotDescription": "Magician represents your ability to communicate clearly, to sell yourself, and to be innovative. The Magician has all the tools and resources available to manifest his desired outcome, so it is a good card to get if you want to create."
}, {
    "tarotName": "The Moon",
    "imagePath": "images/theMoon.avif",
    "tarotDescription": "Moon represents illusions, intuition, fantasies, fears and anxiety. When the Moon appears things might not be quite as they seem. Your insecurities might be running high or you find yourself on the receiving end of other people's insecurities."
}, {
    "tarotName": "The Star",
    "imagePath": "images/theStar.jpeg",
    "tarotDescription": "Star represents hope, a bright future, joy, optimism, guidance, having answers to your questions, being and feeling the connection to the divine, serenity and inspiration. The Star shines so brightly that when it shows up in a reading it tells you that you are being the light in someone's life."
}, {
    "tarotName": "The Sun",
    "imagePath": "images/theSun.jpeg",
    "tarotDescription": "Sun represents success, joy, sunshine, day, warmth and happiness. The Sun shows up when life is sunny and you are enjoying your time with the people you love. Life is simple rather than complicated. Relationships are blossoming and you are feeling loved."
}, {
    "tarotName": "The Tower",
    "imagePath": "images/theTower.jpeg",
    "tarotDescription": "Tower represents disaster, emotional 'meltdowns' and/or tantrums, anger issues, upheaval, sudden change that is caused by disruption and revelations that rock the foundation of the person, household, organisation or even country, depending on the nature of the question."
}, {
    "tarotName": "The Wheel of Fortune",
    "imagePath": "images/theWheelOfFortune.jpeg",
    "tarotDescription": "Wheel of Fortune is the Big destiny card in the tarot deck. What is meant to be is meant to be. In the tarot when the Wheel of Fortune turns up, it means that the events and people in your life are in your life due to it being pre-decided by destiny."
}, {
    "tarotName": "The World",
    "imagePath": "images/theWorld.jpeg",
    "tarotDescription": "World is the final Major Arcana card and represents fulfillment and successful completion of a cycle. You know your place in the world, and your life lessons have made you smart and accomplished. The World shows up when the world is ready for you and want what you have to offer."
}]

#previous_readings = {}



@app.route("/cards", methods = ["GET"])
def retrieve_cards_collection():
    return cards#, {"Access-Control-Allow-Origin": "*"}

@app.route("/previous_readings", methods = ["GET"])
def retrieve_previous_readings_collection():
    #THESE 2 LINES ARE SUPER IMPORTANT, DO NOT WRITE THIS ON POST USERS OR POST SESSIONS
    if "user_id" not in g.session_data:
        return "Unauthorized", 401
    #db = DummyDB('mydatabase.db')
    db = ReadingsDB()
    allreadings = db.getReadings()
    return allreadings#, {"Access-Control-Allow-Origin": "*"}


#CLIENT SUDO CODE FOR DISPLAYING LOGIN/REGISTER BUTTONS this is in JS probably definitely

# when the page loads:
# 1. load readings collection
# if (response.status == 401) {
#   hide readings UI 
#   show login and register UI
#   when user logs in successfully:
#   call load function again to restart the process, will go to the 200 response status code
# } else if (response.status == 200) {
#   show readings UI and hide login/register
# }

@app.route("/previous_readings/<int:reading_id>", methods = ["GET"])
def retrieve_specific_reading(reading_id):
    if "user_id" not in g.session_data:
        return "Unauthorized", 401
    #print("retrieve reading member with id:",movie_id)
    db = ReadingsDB()
    specific_reading = db.getReading(reading_id)
    if specific_reading: 
        return specific_reading#, {"Access-Control-Allow_Origin": "*"}
    else: #else if restaurant is None, return a 404 response code
        return "Reading with ID {} not found".format(reading_id), 404#, {"Access-Control-Allow_Origin": "*"}


@app.route("/previous_readings", methods = ["POST"])
def create_previous_reading_collection():
    if "user_id" not in g.session_data:
        return "Unauthorized", 401
    print("the request data is:", request.form)
    #reading = {"card": request.form["card"], "question": request.form["question"]}
    db = ReadingsDB()
    card = request.form["card"]
    question = request.form["question"]
    rating= request.form["rating"]
    description = request.form["description"]
    image = request.form["image"]
    db.createReading(card, question, description, image, rating)
    return "Created", 201#, {"Access-Control-Allow-Origin": "*"}






@app.route("/users", methods = ["POST"])
def create_user():
    #if "user_id" not in g.session_data:
    print("the request data is:", request.form)
    db = ReadingsDB()
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    email = request.form["email"]
    password = request.form["password"]
    prePass = password
    saltRounds = 12
    #password.hashpw(prePass,saltRounds)
    #password = hash(prePass,saltRounds)
    password = bcrypt.hash(prePass)
    dbUser = db.getUserThroughEmail(email)
    if dbUser:
        return "Error processing request", 422#, {"Access-Control-Allow-Origin":"*"}
    db.createUser(firstname,lastname,email,password)
    return "Created", 201#, {"Access-Control-Allow-Origin": "*"}



@app.route("/sessions", methods = ["POST"])
def login():
    #if "user_id" not in g.session_data:
    db = ReadingsDB()
    email = request.form["email"]
    password = request.form["password"]
    dbUser = db.getUserThroughEmail(email)
    print("EMAIL IS:",email)
    print("DB USER IS:", dbUser)
    if dbUser:
        if bcrypt.verify(password,dbUser["password"]) == True:
            #LOG IN THE USER
            #create a session
            #save user id
            #g.session_data is a dictionary, dictionary[insert key]
            #g.session_id 
            #g.session_data = session_store.getSession(g.session_id)
            g.session_data["user_id"] = dbUser["id"]
            #print(dbUser)
            return "Session created", 201#, {"Access-Control-Allow-Origin":"*"}

        else:
            return "Error processing request", 401#, {"Access-Control-Allow-Origin":"*"}
    return "Error processing request", 401#, {"Access-Control-Allow-Origin":"*"}
    





@app.route("/previous_readings/<int:reading_id>", methods = ["DELETE"])
def delete_previous_reading(reading_id):
    if "user_id" not in g.session_data:
        return "Unauthorized", 401
    print("the request data is", request.form)
    db = ReadingsDB()
    reading = db.getReading(reading_id)
    if reading:
        db.deleteReading(reading_id)
        return "Deleted", 204#, {"Access-Control-Allow-Origin":"*"}
    else:
        return "Reading with ID {} not found".format(reading_id), 404#, {"Access-Control-Allow-Origin":"*"}

@app.route("/previous_readings/<int:reading_id>", methods = ["PUT"])
def update_reading(reading_id):
    if "user_id" not in g.session_data:
        return "Unauthorized", 401
    print("the request data is", request.form)
    db = ReadingsDB()
    reading = db.getReading(reading_id)
    if reading:
        question = request.form["question"]
        rating = request.form["rating"]
        db.updateReading(reading_id,question,rating)
        return "Updated", 204#, {"Access-Control-Allow-Origin":"*"}
    else:
        return "Reading with ID {} not found".format(reading_id), 404#, {"Access-Control-Allow-Origin":"*"}








def run():
    app.run(port=8080)



if __name__ == '__main__':
    run()



# @app.route("/cards", methods = ["POST"])
# def create_in_cards_collection():
#     print("the request datais :", request.form)
#     cards.append(request.form["name"])
#     return "Created", 201, {"Access-Control-Allow-Origin": "*"}
# fetch("https://api.jsonbin.io/v3/b/64efadcc9d312622a398a63a").then(function (response) {

# @app.route("/cards", methods=["POST"])
# def create_cards_collection():
#     print("the request details:", request.form)
#     previous_readings.append(request.form["name"])
#     return "Created", 201, {"Access-Control-Allow-Origin": "*"}


