def main():
    # File Creation
    try:
        # Creating a new text file in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Writing three lines of text to the file
            file.write("Hello, this is line 1\n")
            file.write("12345\n")
            file.write("This is line 3 with a mix of text and numbers\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    
    # File Reading and Display
    try:
        # Opening the file in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Reading and printing the contents of the file
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to access 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
    
    # File Appending
    try:
        # Opening the file in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Appending three additional lines of text
            file.write("This is line 4 added by appending\n")
            file.write("67890\n")
            file.write("Appending another line, this is line 6\n")
        print("Three lines appended to 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("Execution completed.")


if __name__ == "__main__":
    main()
