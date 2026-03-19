# python-contact-manager-cli
This ia simple and user friendly command-line contact manager built using python.

This project allows users to add, view, search and remove contacts, with data stored permanently using a JSON file.

## Features
- Add new contacts
- View all the contacts in a formatted table
- Search contact details by name
- Remove contacts
- Save contacts permanently using JSON
- Clean table formatting using f-strings
- Error handeling with try/except

## Concepts Used
- Function
- Dictionaries
- Nested dictionaries
- Loops (for, while)
- Conditional statements (if/elif/else)
- User input handling
- Exception handling (try/except)
- File handling
- JSON (json.load, json.dump)
- String formatting (f-string)
- enumerate() for indexing

## Data Structure
Contacts are stored as nested dictionary:

contacts = {
   "John Doe": {
  
      "phone": "1234567890"
      
      "email": "john@gmail.com"
      
      "city": "New York" 
  } 
}

## Data Persistance
contacts are saved in a file called:

contacts.json

Example:

{
   "John Doe": {
  
      "phone": "1234567890"
      
      "email": "john@gmail.com"
      
      "city": "New York" 
  } 
}

- json.load() -> reads data from file
- json.dump() -> saves data to file

This allows the program to remember contacts even afer closing.


## How to Run
- Make sure Python is installed
- Download or clone this repository
- Open terminal in the project folder
- Run: Personal-Contact-Manager.py

## Author
Mosfaka Shorna - University of Michigan
