try:
   
    print("--- Part 1: Write ---")
    note1 = input("Enter a short note/message: ")
    
    with open("notes.txt", "w") as file:
        file.write(note1 + "\n")
        
    
    print("\n--- Part 2: Read ---")
    with open("notes.txt", "r") as file:
        content = file.read()
        print("Content of the file:")
        print(content)
        
   
    print("--- Part 3: Append ---")
    note2 = input("Enter another note: ")
    
    with open("notes.txt", "a") as file:
        file.write(note2 + "\n")
        
    print("\n--- Updated Content ---")
    with open("notes.txt", "r") as file:
        updated_content = file.read()
        print(updated_content)


except FileNotFoundError:
    print("\nError: The file 'notes.txt' was not found!")
except Exception as e:
    
    print(f"\nAn unexpected error occurred: {e}")