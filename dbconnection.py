from datetime import date, datetime
from turtle import textinput

import PeopleCounterMain

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initializations
date = datetime.now()


# adding first data
cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)


def databaseConnection(textIn, textOut):
    db = firestore.client()
    doc_ref = db.collection('PeopleCounting').document('live')

    doc_ref.set({

            'countOut': textOut,
            'countIn': textIn
        })


# def databaseConnection1(textIn):
#
#     db = firestore.client()
#     doc_ref = db.collection('PeopleCounting').document('live')
#
#     doc_ref.set({
#         'countOut': textIn
#     })
