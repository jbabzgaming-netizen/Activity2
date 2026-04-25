def save_name():
    try:
        username = input("Enter your mothapaking name: ")
        if not username:
            raise ValueError("Name cannot be empty.")
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        with open("mothapaking_names.txt", "a") as file:
            file.write(f"{username}, {age}\n")
        print("Name and age saved successfully!")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":    save_name()
   


             