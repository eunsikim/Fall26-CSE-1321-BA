import os

def main():
    print(os.getcwd()) # Get Current Working Directory

    print()

    print(os.listdir()) # List Directories
    
    print()

    print(os.listdir("C:\\"))

    os.mkdir("C:\Stuff\Test File 2") # Make directory

    os.rename("Test File 1", "File 1")

    os.rmdir("C:\Stuff\Test File 2") # Remove Directory

if __name__ == "__main__":
    main()