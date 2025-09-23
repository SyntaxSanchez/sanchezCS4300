def countWords(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(len(words))
            return len(words)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filepath}' does not exist.")
    
