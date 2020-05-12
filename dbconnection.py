from datetime import date, datetime
from turtle import textinput

import PeopleCounterMain

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initializations
date = datetime.now()


# adding first data


def databaseConnection():
    cred = credentials.Certificate('firebase-sdk.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection('PeopleCounting').document('live')

    doc_ref.set({
        'countdate': date,
        'countin': PeopleCounterMain.testIntersectionIn(),
        'countout': PeopleCounterMain.testIntersectionOut()

    })

