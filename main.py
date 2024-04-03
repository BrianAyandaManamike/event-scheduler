import datetime

class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time

def add_event(events):
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date_str = input("Enter event date (YYYY-MM-DD): ")
    time_str = input("Enter event time (HH:MM): ")

    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        time = datetime.datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return

    event = Event(title, description, date, time)
    events.append(event)
    print("Event added successfully!")

def display_events(events):
    if not events:
        print("No events to display.")
        return

    events_sorted = sorted(events, key=lambda x: (x.date, x.time))
    print("All Events:")
    for event in events_sorted:
        print_event(event)

def print_event(event):
    print(f"Title: {event.title}")
    print(f"Description: {event.description}")
    print(f"Date: {event.date}")
    print(f"Time: {event.time}")
    print()

def delete_event(events):
    title = input("Enter the title of the event you want to delete: ")
    for event in events:
        if event.title == title:
            events.remove(event)
            print(f"Event '{title}' deleted successfully!")
            return
    print(f"Event '{title}' not found.")

def search_events(events):
    search_term = input("Enter date (YYYY-MM-DD) or keyword to search events: ")
    found_events = []
    for event in events:
        if search_term in event.title or search_term in event.description or str(event.date) == search_term:
            found_events.append(event)
    if found_events:
        print("Search Results:")
        for event in found_events:
            print_event(event)
    else:
        print("No events found matching the search term.")

def edit_event(events):
    title = input("Enter the title of the event you want to edit: ")
    for event in events:
        if event.title == title:
            print("Event found. Please provide new details:")
            event.title = input("Enter event title: ")
            event.description = input("Enter event description: ")
            event.date = datetime.datetime.strptime(input("Enter event date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            event.time = datetime.datetime.strptime(input("Enter event time (HH:MM): "), "%H:%M").time()
            print("Event updated successfully!")
            return
    print(f"Event '{title}' not found.")

def main():
    events = []

    while True:
        print("\nOptions:")
        print("1. Add Event")
        print("2. Display All Events")
        print("3. Delete Event")
        print("4. Search Events")
        print("5. Edit Event")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_event(events)
        elif choice == '2':
            display_events(events)
        elif choice == '3':
            delete_event(events)
        elif choice == '4':
            search_events(events)
        elif choice == '5':
            edit_event(events)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
