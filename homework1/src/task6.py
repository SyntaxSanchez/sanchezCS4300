# Task6
# Sebastian Sanchez
# CS4300

# function to count the number of words in a specified text file
def countWords(filename: str) -> int:
    try:
        # open the file to read mode
        with open(filename, 'r') as file:
            # read the entire file's content as a single string
            content = file.read()
            words = content.split()
            print(len(words))
            # return the number of words
            return len(words)
    except FileNotFoundError:
        # Raise an error if the file doesnt exist
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    
