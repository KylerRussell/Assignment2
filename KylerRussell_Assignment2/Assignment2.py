'''
Name of program contained in the file: 348 Assignment 2
Brief description of the program: This program was made to take in 33 lines of text and output a filtered version of the text which was filtered through regex
Inputs: Assignment2_Test_File.txt
Output: 
All collaborators: None
Other sources for the code: 
Author’s full name: Kyler Russell
Creation date: 2/13/2025
'''
import re # Import statement for Regex

class Executive: # The executive class used to execute funcitonality
    def __init__(self, file): # Magic method which is called when Executive is created
        self.file = open(file) # Open the test file
        
def main(): # Declare the main function
    file_name = "Assignment2_Test_File.txt" # Set the test file
    my_executive = Executive(file_name) # Initialize the executive class with the test file
    my_executive.run() # Run the executive program

main() # Run the python main program 