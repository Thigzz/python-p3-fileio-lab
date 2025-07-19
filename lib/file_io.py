def write_file(file_name: str, file_content: str):
    full_file_name = f"{file_name}.txt"
    try:
        with open(full_file_name, 'w') as f:
            f.write(file_content)
        print(f"Successfully wrote to '{full_file_name}'")
    except IOError as e:
        print(f"Error writing to file '{full_file_name}': {e}")

def append_file(file_name: str, append_content: str):
    full_file_name = f"{file_name}.txt"
    try:
        with open(full_file_name, 'a') as f:
            f.write(append_content)
        print(f"Successfully appended to '{full_file_name}'")
    except IOError as e:
        print(f"Error appending to file '{full_file_name}': {e}")

def read_file(file_name: str) -> str:
    full_file_name = f"{file_name}.txt"
    try:
        with open(full_file_name, 'r') as f:
            content = f.read()
        print(f"Successfully read from '{full_file_name}'")
        return content
    except FileNotFoundError:
        print(f"Error: File '{full_file_name}' not found.")
        return ""
    except IOError as e:
        print(f"Error reading file '{full_file_name}': {e}")
        return ""

if __name__ == "__main__":
    write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")
    append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")
    content = read_file(file_name="logfile")
    print("\nContent of 'logfile.txt':")
    print(content)
    write_file("my_notes", "This is my first note.\n")
    append_file("my_notes", "Adding another line to my notes.\n")
    notes_content = read_file("my_notes")
    print("\nContent of 'my_notes.txt':")
    print(notes_content)
    read_file("non_existent_file")
