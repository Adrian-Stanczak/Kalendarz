import json, os, random

file_path = "data/events.json"
kalendar = []

def main():
    try:
        while True:
            enter = int(input('What you wanna do: '))
            match enter:
                case 1: add_event(kalendar)
                case 2: remove_event(kalendar)
                case 3: show_event(kalendar)
                case 4: break
    except ValueError:
        print('Please enter correct values!')
            

def add_event(kalendar:list):
    id = 1
    
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

    id =+ 1

    print(kalendar)

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

    x.extend(kalendar)

    with open(file_path, 'a') as file:
        json.dump(x, file, indent=4)

def remove_event(kalendar):
    pass

def show_event(kalendar):
    print(kalendar)

def modify_event(kalendar):
    pass

main()