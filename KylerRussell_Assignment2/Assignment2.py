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
        self.line_number = 1 # Initialize the current line the input file is on.
        
        
    def run(self): # Run function which starts the program when called
        '''
        The important thing to note with this program is that it will find all the matches instead of just the first match, as that is one of the displayed things within the slides,
        but this switches halfway through the slides, but I feel that it is better to leave it this way rather than swapping it like the slides did.
        '''
        for line in self.file: # for each line in the file do the following
            output = len(re.findall(self.expressions(self.line_number), line)) # Use the findall to return a list of all of the regex that matched the pattern to the text, and then count how many items are in the list
            output_text = ''.join(str(x) for x in re.findall(self.expressions(self.line_number), line)) # Store the regex that matched the the pattern to the text into a list, then combine the list into a string
            self.line_number += 1 # Set line number to the next line after finishing retriving from the line. 
            if output == 0: # If there is nothing in the list (aka no match found)
                print(f"string: {line.strip()}\nmatch: no match found\n") # display no match found
            else: # if a match was found
                print(f"string: {line.strip()}\nmatch: {output} matches\nmatched text: {output_text}\n") # Display the string that was taken in, the number of matches, and the text that was matched. 
        
    def expressions(self, line_number): # This function returns the pattern expression for a given line number. 
        if line_number <= 4: # If the line number is less than or equal to 4
            return r".." # Returns the pattern for lines 1-4
        
        elif line_number <=7: # If the line number is less than or equal to 7 but greater than 4
            return r"^a" # Returns the pattern for lines 5-7
        
        elif line_number <=9: # If the line number is less than or equal to 9 but greater than 7
            return r"^ab" # Returns the pattern for lines 8-9
        
        elif line_number <= 12: # If the line number is less than or equal to 12 but greater than 7
            return r"a$" # Returns the pattern for lines 10-12
        
        elif line_number <= 17: # If the line number is less than or equal to 17 but greater than 12
            return r"ma+n" # Returns the pattern for lines 13-17
        
        elif line_number == 18: # If the line number is equal to 18
            return r"b" # Returns the pattern for line 18
        
        elif line_number == 19: # If the line number is equal to 19
            return r"ac" # Returns the pattern for line 19
        
        elif line_number == 20: # If the line number is equal to 20
            return r"^abra" # Returns the pattern for line 20
        
        elif line_number == 21: # If the line number is equal to 21
            return r"abra$" # Returns the pattern for line 21
        
        elif line_number == 22: # If the line number is equal to 22
            return r"ca." # Returns the pattern for line 22
        
        elif line_number == 23: # If the line number is equal to 23
            return r"r.*b" # Returns the pattern for line 23
        
        elif line_number == 24: # If the line number is equal to 24
            return r"ac.+a" # Returns the pattern for line 24
        
        elif line_number == 25: # If the line number is equal to 25
            return r"cx?a" # Returns the pattern for line 25
        
        elif line_number == 26: # If the line number is equal to 26
            return r"[a-fXY0-9]" # Returns the pattern for line 26
        
        elif line_number == 27: # If the line number is equal to 27
            return r"[^a-fXY0-9]" # Returns the pattern for line 27
        
        elif line_number == 28: # If the line number is equal to 28
            return r"flea|tick" # Returns the pattern for line 28
        
        elif line_number == 29: # If the line number is equal to 29
            return r"(My|Your) (dog|cat)" # Returns the pattern for line 29
        
        elif line_number == 30: # If the line number is equal to 30
            return r"\bDogg\b" # Returns the pattern for line 30
        
        elif line_number == 31: # If the line number is equal to 31
            return r"\d" # Returns the pattern for line 31
        
        elif line_number == 32: # If the line number is equal to 32
            return r"\s" # Returns the pattern for line 32
        
        elif line_number == 33: # If the line number is equal to 33
            return r"\w+" # Returns the pattern for line 33
        
def main(): # Declare the main function
    file_name = "Assignment2_Test_File.txt" # Set the test file
    my_executive = Executive(file_name) # Initialize the executive class with the test file
    my_executive.run() # Run the executive program

main() # Run the python main program 