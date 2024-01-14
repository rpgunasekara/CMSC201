"""
File: network.py
Author: Ravindu Gunasekara
Date: 12/04-11/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Using a nested dictionary and some lists,
    create a phone network that can add 
    switchboards, add phones, and make calls.
"""
import json

HYPHEN = "-"
QUIT = 'quit'
SWITCH_CONNECT = 'switch-connect'
SWITCH_ADD = 'switch-add'
PHONE_ADD = 'phone-add'
NETWORK_SAVE = 'network-save'
NETWORK_LOAD = 'network-load'
START_CALL = 'start-call'
END_CALL = 'end-call'
DISPLAY = 'display'


# Connects two area codes with each other.
def connect_switchboards(switchboards, area_1, area_2):
    if area_1 in switchboards and area_2 in switchboards:
        if area_2 not in switchboards[area_1]["trunk-lines"]:
            switchboards[area_1]["trunk-lines"].append(area_2)
        
        if area_1 not in switchboards[area_2]["trunk-lines"]:
            switchboards[area_2]["trunk-lines"].append(area_1)

        # Adds additional connections via transitive property.
        for area_a in switchboards[area_1]["trunk-lines"]:
            if area_a not in switchboards[area_2]["trunk-lines"] and area_a != area_2:
                switchboards[area_2]["trunk-lines"].append(area_a)
        
            for area_b in switchboards[area_1]["trunk-lines"]:
                if area_b not in switchboards[area_a]["trunk-lines"] and area_b != area_a:
                    switchboards[area_a]["trunk-lines"].append(area_b)

        for area_a in switchboards[area_2]["trunk-lines"]:
            if area_a not in switchboards[area_1]["trunk-lines"] and area_a != area_1:
                switchboards[area_1]["trunk-lines"].append(area_a)

            for area_b in switchboards[area_2]["trunk-lines"]:
                if area_b not in switchboards[area_a]["trunk-lines"] and area_b != area_a:
                    switchboards[area_a]["trunk-lines"].append(area_b)
    else:   
        print('Error: Could not connect {} and {}'.format(area_1, area_2))


# Adds a switchboards for the area code.
def add_switchboard(switchboards, area_code):
    # Add some keys with lists as values to track connection information.
    if area_code not in switchboards:
        switchboards[area_code] = {}
        switchboards[area_code]["trunk-lines"] = []
        switchboards[area_code]["phone-numbers"] = []
        switchboards[area_code]["phone-active"] = []
        switchboards[area_code]["phone-connection"] = []
    else:
        print('Error: A switchboard for {} already exists.'.format(area_code))


# Adds a phone for the area code.
def add_phone(switchboards, area_code, phone_number):
    # Sets values for the other lists for that phone's index.
    if area_code in switchboards:
        switchboards[area_code]["phone-numbers"].append(phone_number)
        switchboards[area_code]["phone-active"].append(False)
        switchboards[area_code]["phone-connection"].append('None')
    else:
        print('Error: A switchboard for {} does not exist.'.format(area_code))


# Saves a network.
def save_network(switchboards, file_name):
    with open(file_name, 'w') as file:
        json.dump(switchboards, file)


# Loads a network.
def load_network(file_name):
    with open(file_name, 'r') as file:
        switchboards = json.load(file)
        return switchboards


# Starts a call between two numbers.
def start_call(switchboards, start_area, start_number, end_area, end_number):    
    visited_area = {}
    visited_phone = {}
    for area_code in switchboards:
        visited_area[area_code] = False
        
        for phone_number in switchboards[area_code]["phone-numbers"]:
            visited_phone[phone_number] = False

    valid_connection = start_call_rec(switchboards, start_area, start_number, end_area, end_number, visited_area, visited_phone)

    if valid_connection:
        # Update the information in the other lists.
        for i in range(len(switchboards[start_area]["phone-numbers"])):
            if switchboards[start_area]["phone-numbers"][i] == start_number:
                if switchboards[start_area]["phone-active"][i] == False:
                    switchboards[start_area]["phone-active"][i] = True
                    switchboards[start_area]["phone-connection"][i] = '{}-{}-{}'.format(end_area, str(end_number)[:3], str(end_number)[3:])

        for i in range(len(switchboards[end_area]["phone-numbers"])):
            if switchboards[end_area]["phone-numbers"][i] == end_number:
                if switchboards[end_area]["phone-active"][i] == False:
                    switchboards[end_area]["phone-active"][i] = True
                    switchboards[end_area]["phone-connection"][i] = '{}-{}-{}'.format(start_area, str(start_number)[:3], str(start_number)[3:])
        
        print('Connecting...')
        print('{}-{}-{} and {}-{}-{} are now connected.'.format(start_area, str(start_number)[:3], str(start_number)[3:], end_area, str(end_number)[:3], str(end_number)[3:]))
    else:
        print('Connecting...')
        print('{}-{}-{} and {}-{}-{} were not connected.'.format(start_area, str(start_number)[:3], str(start_number)[3:], end_area, str(end_number)[:3], str(end_number)[3:]))


# Recursive helper function for start_call().
def start_call_rec(switchboards, current_area, current_number, end_area, end_number, visited_area, visited_phone):
    current_phone = '{}{}'.format(current_area, current_number)
    end_phone = '{}{}'.format(end_area,end_number)

    # Base case.
    if current_phone == end_phone:
        return [end_phone]
    
    visited_area[current_area] = True
    visited_phone[current_phone] = True

    if current_area not in switchboards:
        return []

    # Recursion occurs if the next phone number hasn't been visited.
    for next_area in switchboards[current_area]["trunk-lines"]:
         for next_number in switchboards[next_area]["phone-numbers"]:  
             next_phone = '{}{}'.format(next_area, next_number) 
             
             if next_phone not in visited_phone and not visited_area[next_area]:
                 path = start_call_rec(switchboards, next_area, next_number, end_area, end_number, visited_area, visited_phone)
                 
                 if path:
                     return [current_phone] + path

    visited_area[current_area] = False
    visited_phone[current_phone] = False
    return []


# Ends a call between two numbers.
def end_call(switchboards, start_area, start_number):
    # Update the infromation in other lists.

    if str(start_area) in switchboards:
        for i in range(len(switchboards[str(start_area)]["phone-numbers"])):
            if switchboards[str(start_area)]["phone-numbers"][i] == start_number:
                if switchboards[str(start_area)]["phone-active"][i] == True:
                    switchboards[str(start_area)]["phone-active"][i] = False
                    switchboards[str(start_area)]["phone-connection"][i] = 'None'

        for area_code in switchboards:
            for i in range(len(switchboards[area_code]["phone-numbers"])):
                if switchboards[area_code]["phone-connection"][i] == '{}-{}-{}'.format(str(start_area), str(start_number)[:3], str(start_number)[3:]):
                    if switchboards[area_code]["phone-active"][i] == True:
                        switchboards[area_code]["phone-active"][i] = False
                        switchboards[area_code]["phone-connection"][i] = 'None'

        print('Hanging up...')
        print('Connection terminated.')
    else:
        print('Hanging up...')
        print('Error: Unable to disconnect.')


# Displays the network information.
def display(switchboards):
    for area_code in switchboards:
        print('\nSwitchboard with area code: {}'.format(area_code))

        print('\tTrunk lines are:')
        for trunk_line in switchboards[area_code]["trunk-lines"]:
            print('\t\tTrunk line connection to: {}'.format(trunk_line))

        # Use the information in other lists to determine the output.
        print('\tLocal phone numbers are:')
        for i in range(len(switchboards[area_code]["phone-numbers"])):
            if switchboards[area_code]["phone-active"][i] == True:
                print('\t\tPhone with number: {}-{} is connected to {}.\n'.format(str(switchboards[area_code]["phone-numbers"][i])[:3], str(switchboards[area_code]["phone-numbers"][i])[3:], switchboards[area_code]["phone-connection"][i]))
            else:
                print('\t\tPhone with number: {}-{} is not in use.\n'.format(str(switchboards[area_code]["phone-numbers"][i])[:3], str(switchboards[area_code]["phone-numbers"][i])[3:]))


# Main function, provided with the starter code.
if __name__ == '__main__':
    switchboards = {}
    s = input('Enter command: ')
    while s.strip().lower() != QUIT:
        split_command = s.split()
        if len(split_command) == 3 and split_command[0].lower() == SWITCH_CONNECT:
            area_1 = int(split_command[1])
            area_2 = int(split_command[2])
            connect_switchboards(switchboards, area_1, area_2)
        elif len(split_command) == 2 and split_command[0].lower() == SWITCH_ADD:
            add_switchboard(switchboards, int(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == PHONE_ADD:
            number_parts = split_command[1].split('-')
            area_code = int(number_parts[0])
            phone_number = int(''.join(number_parts[1:]))
            add_phone(switchboards, area_code, phone_number)
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_SAVE:
            save_network(switchboards, split_command[1])
            print('Saving...')
            print('Network save to {}'.format(split_command[1]))
        elif len(split_command) == 2 and split_command[0].lower() == NETWORK_LOAD:
            switchboards = load_network(split_command[1])
            print('Loading...')
            print('Network loaded from {}'.format(split_command[1]))
        elif len(split_command) == 3 and split_command[0].lower() == START_CALL:
            src_number_parts = split_command[1].split(HYPHEN)
            src_area_code = int(src_number_parts[0])
            src_number = int(''.join(src_number_parts[1:]))

            dest_number_parts = split_command[2].split(HYPHEN)
            dest_area_code = int(dest_number_parts[0])
            dest_number = int(''.join(dest_number_parts[1:]))
            start_call(switchboards, src_area_code, src_number, dest_area_code, dest_number)
        elif len(split_command) == 2 and split_command[0].lower() == END_CALL:
            number_parts = split_command[1].split(HYPHEN)
            area_code = int(number_parts[0])
            number = int(''.join(number_parts[1:]))
            end_call(switchboards, area_code, number)
        elif len(split_command) >= 1 and split_command[0].lower() == DISPLAY:
            display(switchboards)

        s = input('Enter command: ')
