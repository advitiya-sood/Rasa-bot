from typing import Any, Text, Dict, List
from urllib import response

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd

class ValidateForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["name", "number","location", "email", "age" ,"time", "doc_spec"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]
    
class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"
    
    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        # userinfo(tracker.get_slot("name"), tracker.get_slot("number"), tracker.get_slot("email"),
        #          tracker.get_slot("age"),  tracker.get_slot("time"))
        # Name=tracker.get_slot("name")
        # Mobile_number=tracker.get_slot("number")
        # Email=tracker.get_slot("email")
        # Age=tracker.get_slot("age")
        # Time=tracker.get_slot("time")
        Specialisation = tracker.get_slot("doc_spec")
        df = pd.read_csv("doctor.csv")

        doc = df.where(df['Specialization'].str.lower() == Specialisation.lower())
        doc = doc.dropna()

        if not doc.empty:
            doctor_name = doc.iloc[0,0]
            # print(doctor_name)
            
        dispatcher.utter_message(doctor_name)
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Location = tracker.get_slot("location"),
                                 Mobile_number=tracker.get_slot("number"),
                                 Email=tracker.get_slot("email"),
                                 Age=tracker.get_slot("age"),
                                 Time=tracker.get_slot("time"), 
                                 Specialisation = tracker.get_slot('doc_spec'))

        # result = email(tracker.get_slot("name"), tracker.get_slot("number"), tracker.get_slot("email"),
        #                tracker.get_slot("age"), tracker.get_slot("time"))
        # if result == "success":
            
        dispatcher.utter_message(text="Your appointment is confirmed and you will receive a mail")
        # dispatcher.utter_message(response="utter_details_thanks")