import sys
from LinkedListFile import LinkedList

def main():
    args = input("Enter the inventory file name and update file name -> ")
    args = args.split()
    
    inventory_filename = args[0]    # simple.txt
    update_filename = args[1]       # update.txt
    
    inventory_file_contents = open_file(inventory_filename)     # open simple.txt
    update_file_contents = open_file(update_filename)           # open update.txt
    
    # This initializes the Linked List
    database = LinkedList()
    
    print("processing " + inventory_filename)
    # You may want to add more inputs to the function, in which casae
    # you should modify the following line.
    read_inventory_file(inventory_file_contents, database)
    
    print("processing " + update_filename)
    # You may want to add more inputs to the function, in which casae
    # you should modify the following line.
    read_update_file(update_file_contents, database)
    
    
def read_inventory_file(contents, database):
    # code goes here
    
def read_update_file(contents, database):
    # code goes here

def open_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print("Error in opening " + filename)
        sys.exit()

main()