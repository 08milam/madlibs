

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def defalt_page():
    return render_template("index.html")

@app.route('/madlibs', methods=["POST", "GET"])
def ml_game():
    if request.method == "POST":
        place = request.form["pl"]
        adjective = request.form["ad"]
        noun = request.form["nn"]
        name_one = request.form["no"]
        name_two = request.form["nt"]
        pronoun = request.form["pr"]
        verb = request.form["ve"]
        adverb = request.form["av"]

        ibs_one = "Once upon a time in a " + adjective + " town, there lived a " + noun + " named "  + name_one +  ". One " + adverb + " day, " + pronoun + " decided to " + verb + " to the mysterious " + place + " on the outskirts of town. Armed with nothing but a sense of " + adjective + " curiosity, " + pronoun + " set off on the adventure of a lifetime. The journey took " + name_one + " through " + adjective + " forests, across " + adjective + " streams, and over " + adjective + " hills. Along the way, " + name_one + " encountered a peculiar old " + noun +" named "+ name_two + " who offered " + name_one + " cryptic advice. To reach the heart of the " + place + " , follow the " + adjective + " path and beware of the mischievous " + noun + ", the old " + noun + " whispered with a sly smile. Undeterred, " + pronoun + " continued " + adverb + " through the " + adjective + " landscape. The air was filled with the scent of the " + place + " , and the distant sound of " + adjective + " birds added to the mysterious atmosphere. With each step, the anticipation in " + name_one + "'s heart grew. Finally, " + noun + " arrived at the entrance of the " + place + ". The " + adjective + " gates creaked open, revealing a world of wonder. " + pronoun + " marveled at the " + place + " landscapes, filled with sparkling " + place + " and ancient " + noun + " that seemed to whisper tales of times long ago. As " + pronoun + " explored deeper into the " + place + " , " + pronoun + " discovered a hidden chamber filled with " + adjective + " artifacts. The room echoed with the sounds of " + adjective + " footsteps as " + pronoun + " examined the curious objects. Lost in the enchantment of the " + place + " , " + pronoun + " almost didn't notice the appearance of a friendly " + noun + " who guided " + name_one + " through the labyrinthine corridors. Together, they uncovered the secrets of the " + place + " , solving " + adjective + " puzzles and unlocking the mysteries that lay hidden. As the day " + verb + " to a close, " + pronoun + " made the way back to the " + adjective + " town, carrying with " + name_one + " a heart full of stories and a newfound appreciation for the magic that could be found in the most unexpected " + place + ". And so, " + pronoun + " vowed to share the tales of the curious exploration with the fellow townsfolk, inspiring others to embark on their own journeys of discovery."


        return render_template("index.html", ml_game=ibs_one)
    else:
        return render_template("index.html" )





# place = input('Enter a place: ')
# adjective = input('Enter a adjactive: ')
# noun = input('Enter a noun: ')
# name_one = input('Enter a name: ')
# name_two = input('Enter a second name: ')
# pronoun = input('Enter a pronoun: ')
# verb = input('Enter a verb: ')
# adverb = input('Enter a adverb: ')




# def fill_in_the_black(place, adjective, noun, name_one, name_two, pronoun, verb, adverb):
#     libs_one = "Once upon a time in a " + adjective + " town, there lived a " + noun + " named "  + name_one +  ". One " + adverb + " day, " + pronoun + " decided to " + verb + " to the mysterious " + place + " on the outskirts of town. Armed with nothing but a sense of " + adjective + " curiosity, " + pronoun + " set off on the adventure of a lifetime. The journey took " + name_one + " through " + adjective + " forests, across " + adjective + " streams, and over " + adjective + " hills. Along the way, " + name_one + " encountered a peculiar old " + noun +" named "+ name_two + " who offered " + name_one + " cryptic advice. To reach the heart of the " + place + " , follow the " + adjective + " path and beware of the mischievous " + noun + ", the old " + noun + " whispered with a sly smile. Undeterred, " + pronoun + " continued " + adverb + " through the " + adjective + " landscape. The air was filled with the scent of the " + place + " , and the distant sound of " + adjective + " birds added to the mysterious atmosphere. With each step, the anticipation in " + name_one + "'s heart grew. Finally, " + noun + " arrived at the entrance of the " + place + ". The " + adjective + " gates creaked open, revealing a world of wonder. " + pronoun + " marveled at the " + place + " landscapes, filled with sparkling " + place + " and ancient " + noun + " that seemed to whisper tales of times long ago. As " + pronoun + " explored deeper into the " + place + " , " + pronoun + " discovered a hidden chamber filled with " + adjective + " artifacts. The room echoed with the sounds of " + adjective + " footsteps as " + pronoun + " examined the curious objects. Lost in the enchantment of the " + place + " , " + pronoun + " almost didn't notice the appearance of a friendly " + noun + " who guided " + name_one + " through the labyrinthine corridors. Together, they uncovered the secrets of the " + place + " , solving " + adjective + " puzzles and unlocking the mysteries that lay hidden. As the day " + verb + " to a close, " + pronoun + " made the way back to the " + adjective + " town, carrying with " + name_one + " a heart full of stories and a newfound appreciation for the magic that could be found in the most unexpected " + place + ". And so, " + pronoun + " vowed to share the tales of the curious exploration with the fellow townsfolk, inspiring others to embark on their own journeys of discovery."

#     print(libs_one)

# fill_in_the_black(place, adjective, noun, name_one, name_two, pronoun, verb, adverb)









# from flask import Flask, request, render_template, redirect, url_for

# app = Flask(__name__)


# @app.route("/")
# def defalt_page():
#     return render_template("index.html")

# @app.route('/login', methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("index.html" )

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"


# from flask import Flask, request, render_template, redirect, url_for

# app = Flask(__name__)


# @app.route("/")
# def defalt_page():
#     return render_template("index.html")

# @app.route('/madlibs', methods=["POST", "GET"])
# def ml_game():
#     if request.method == "POST":
#         place = request.form["pl"]
#         adjective = request.form["ad"]
#         noun = request.form["nn"]
#         name_one = request.form["no"]
#         name_two = request.form["nt"]
#         pronoun = request.form["pr"]
#         verb = request.form["ve"]
#         adverb = request.form["av"]

#         ibs_one = "Once upon a time in a " + adjective + " town, there lived a " + noun + " named "  + name_one +  ". One " + adverb + " day, " + pronoun + " decided to " + verb + " to the mysterious " + place + " on the outskirts of town. Armed with nothing but a sense of " + adjective + " curiosity, " + pronoun + " set off on the adventure of a lifetime. The journey took " + name_one + " through " + adjective + " forests, across " + adjective + " streams, and over " + adjective + " hills. Along the way, " + name_one + " encountered a peculiar old " + noun +" named "+ name_two + " who offered " + name_one + " cryptic advice. To reach the heart of the " + place + " , follow the " + adjective + " path and beware of the mischievous " + noun + ", the old " + noun + " whispered with a sly smile. Undeterred, " + pronoun + " continued " + adverb + " through the " + adjective + " landscape. The air was filled with the scent of the " + place + " , and the distant sound of " + adjective + " birds added to the mysterious atmosphere. With each step, the anticipation in " + name_one + "'s heart grew. Finally, " + noun + " arrived at the entrance of the " + place + ". The " + adjective + " gates creaked open, revealing a world of wonder. " + pronoun + " marveled at the " + place + " landscapes, filled with sparkling " + place + " and ancient " + noun + " that seemed to whisper tales of times long ago. As " + pronoun + " explored deeper into the " + place + " , " + pronoun + " discovered a hidden chamber filled with " + adjective + " artifacts. The room echoed with the sounds of " + adjective + " footsteps as " + pronoun + " examined the curious objects. Lost in the enchantment of the " + place + " , " + pronoun + " almost didn't notice the appearance of a friendly " + noun + " who guided " + name_one + " through the labyrinthine corridors. Together, they uncovered the secrets of the " + place + " , solving " + adjective + " puzzles and unlocking the mysteries that lay hidden. As the day " + verb + " to a close, " + pronoun + " made the way back to the " + adjective + " town, carrying with " + name_one + " a heart full of stories and a newfound appreciation for the magic that could be found in the most unexpected " + place + ". And so, " + pronoun + " vowed to share the tales of the curious exploration with the fellow townsfolk, inspiring others to embark on their own journeys of discovery."

#         return redirect(url_for("ibs_one", usr=ibs_one))
#     else:
#         return render_template("index.html" )

# @app.route("/<usr>")
# def ibs_one(usr):
#     return f"<h1>{usr}</h1>"
    
