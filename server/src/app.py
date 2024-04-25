from flask import Flask, render_template, redirect, url_for

import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("erm-bb-firebase-adminsdk-ynhd3-bfa08f7368.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = [
    {
    'etappe': 0,
    'afstand': 2000,
    'steden': "Wetterwille - Start",
    'stuur': "Abe",
    'slag': "Joes",
    'boeg': "Simon"
    },
        {
    'etappe': 1,
    'afstand': 12800,
    'steden': "Leeuwarden - Birdaard",
    'stuur': "Koen",
    'slag': "Jochem",
    'boeg': "Bram"
    },
        {
    'etappe': 2,
    'afstand': 11000,
    'steden': "Birdaard - Dokkum",
    'stuur': "Koen",
    'slag': "Thomas",
    'boeg': "Mats"
    },
        {
    'etappe': 3,
    'afstand': 10900,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 4,
    'afstand': 12550,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 5,
    'afstand': 12500,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 6,
    'afstand': 7500,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 7,
    'afstand': 9700,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 8,
    'afstand': 11200,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 9,
    'afstand': 11350,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 10,
    'afstand': 11100,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 11,
    'afstand': 8000,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 12,
    'afstand': 8300,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 13,
    'afstand': 10125,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 14,
    'afstand': 11700,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 15,
    'afstand': 10500,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 16,
    'afstand': 8400,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 17,
    'afstand': 9100,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 18,
    'afstand': 10000,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 19,
    'afstand': 10000,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
        {
    'etappe': 20,
    'afstand': 8500,
    'steden': "",
    'stuur': "",
    'slag': "",
    'boeg': ""
    },
]

set_stages = False

if set_stages:
    for d in data:
        print(d)
        doc_ref = db.collection('etappeCollection').document()
        doc_ref.set(d)

collection_ref = db.collection('etappeCollection')
stages = collection_ref.stream()

# Convert the generator object to a dictionary
stages = dict((doc.id, doc.to_dict()) for doc in stages)
stages = dict(sorted(stages.items(), key=lambda item: item[1]['etappe']))
print(stages)

current_stage = db.collection('currentStage')
current_stage = current_stage.stream()

# Convert the generator object to a dictionary
current_stage = dict((doc.id, doc.to_dict()) for doc in current_stage)
current_stage = current_stage['current']['stage']
print(current_stage)

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = int(os.environ.get('PORT', 8080)))

@app.route('/')
def etappe():
    #return render_template("etappe0.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[0]], stage_info_next = stages[list(stages.keys())[1]])
    return render_template("etappe0.html", stage_info = stages[list(stages.keys())[current_stage]], stage_info_next = stages[list(stages.keys())[current_stage + 1]])

#@app.route('/etappe0')
#def etappe0():
    #return render_template("etappe0.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[0]], stage_info_next = stages[list(stages.keys())[1]])
#    return render_template("etappe0.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[current_stage]], stage_info_next = stages[list(stages.keys())[current_stage + 1]])


#@app.route('/etappe1')
#def etappe1():
    #return render_template("etappe1.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[1]], stage_info_next = stages[list(stages.keys())[2]])
#    return render_template("etappe0.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[current_stage]], stage_info_next = stages[list(stages.keys())[current_stage + 1]])

#@app.route('/etappe2')
#def etappe2():
#    return render_template("etappe2.html", refreshing = current_refresh, stage_info = stages[list(stages.keys())[2]], stage_info_next = stages[list(stages.keys())[3]])

