from models.event import Event

event1 = Event("19/05/2022", "End of week 3 party", 25, "clockwise", "Relief Central")
event2 = Event("20/05/2022", "Simonas Birthday", 100, "Mango", "Friday Funday")
event3 = Event("22/05/2022", "Sunday Scaries", 50, "Edinburgh Dungeon", "Spook Fest")

event_list = [event1, event2, event3]

def add_event(event):
    event_list.append(event)
