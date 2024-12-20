import json, os, random

file_path = "data/events.json"
kalendar = []

def main():
    try:
        while True:
            enter = int(input('What you wanna do:\n1. Add event\n2. Remove event\n3. Show events\n4. Exit\n'))
            match enter:
                case 1:
                    add_event(kalendar)
                case 2:
                    remove_event(kalendar)
                case 3:
                    show_events()
                case 4:
                    break
    except ValueError:
        print('Please enter correct values!')
            

def add_event(kalendar:list):
    id = random.randint(1, 100)
    
    name = str(input('Add your name: ')).capitalize()
    date = input('Add correct date (as year-month-day): ')
    event = str(input("Say what's gonna be done: "))
    
    new_thing = {
        
        "id": id,
        "name":name,
        "date":date, 
        "event":event
        
    }

    kalendar.append(new_thing)
    save_to_file(kalendar)

    print(f'Thanks {name}! You must do {event} at {date}. Your id is {id}.')
def save_to_file(kalendar):

    if os.path.exists(file_path):
        try:    
            with open(file_path, 'r') as file:
                x = json.load(file)
        except json.JSONDecodeError:
            print('Something went wrong D:')
            x = []
    else:
        x = []

    if not x:
        x.extend(kalendar)
    else:
        x= []
        x.extend(kalendar)

    with open(file_path, 'w') as file:
        json.dump(x, file, indent=4)

def remove_event(kalendar):
    event_id = int(input('Enter event id:'))

    if os.path.exists(file_path):

        with open(file_path, 'r') as file:
            events = json.load(file)

            event_to_remove = next((event for event in events if event['id'] == event_id))

            if event_to_remove:
                events.remove(event_to_remove)
                save_to_file(events)
            else:
                print('Ups, occured error')
    


def show_events():
    event_id = int(input('Enter your event id: '))

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                events = json.load(file)
                if events:
                    event_to_show = next((event for event in events if event['id'] == event_id))
                    if event_to_show:
                        print(f'Name: {event_to_show["name"]}, Date: {event_to_show["date"]}, Event: {event_to_show["event"]}')
                    else:
                        print(f'No event found with ID {event_id}.')
                else:
                    print('No events found.')
            except json.JSONDecodeError:
                print('error reading json file.')
    else:
        print('First you need to create event in kalendar.')

        
main()