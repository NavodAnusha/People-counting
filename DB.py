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
db = firestore.client()
doc_ref = db.collection('PeopleCounting').document('live')

doc_ref.set({
      'countDate': date,
       'countIn': "10",
       'countOut': "12"

})

doc_ref = db.collection('PeopleCounting').document('Weekly')

doc_ref.set({
    'countIn': "510",
    'countOut': "510"
})

doc_ref = db.collection('PeopleCounting').document('Per Day')

doc_ref.set({
    'countIn': "100",
    'countOut': "100"

})

doc_ref = db.collection('PeopleCounting_Weekdays').document('Monday')

doc_ref.set({
    'countIn': "80",
    'countOut': "80"
})

doc_ref = db.collection('PeopleCounting_Weekdays').document('Tuesday')

doc_ref.set({
    'countIn': "75",
    'countOut': "75"
})

doc_ref = db.collection('PeopleCounting_Weekdays').document('wednesday')

doc_ref.set({
    'countIn': "60",
    'countOut': "60"
})

doc_ref = db.collection('PeopleCounting_Weekdays').document('Thursday')

doc_ref.set ({
    'countIn': "78",
    'countOut': "78"
})

doc_ref = db.collection('PeopleCounting_Weekdays').document('Friday')
doc_ref.set({
    'countIn': "80",
    'countOut': "80"
})
