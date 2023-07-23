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
      
    print("processing: " + inventory_filename)
    read_inventory_file(inventory_file_contents, database)
    
    print("processing: " + update_filename)
    read_update_file(update_file_contents, database)
    
    
def read_inventory_file(contents, database):
    # code goes here
    
    
def read_update_file(contents, database):
    # code goes here


def open_file(filename):
    """
    Opens a file with an inputted filename and returns the contents
    of the file in a string.

    Parameters
    ----------
    filename : string
        The name of the file that will be opened.

    Returns
    -------
    List
        A list filled with the IDs in the file in string format.
        
        If no valid filename was entered, the program will print
        an error and exit.
    """
    try:
        with open(filename) as f:
            return f.read().split()
    except FileNotFoundError:
        print("Error in opening " + filename)
        sys.exit()

main()