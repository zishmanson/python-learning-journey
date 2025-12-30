# profile_creator.py 
# A simple script that collects user info and saves it to a file

def create_profile(name, color):
    message = f"Hi {name}! Your favourite color is {color}"
    print(message)

    # Save to file 
    with open("profile.txt", "w") as file: 
        file.write(message + "\n") 
    
    print("Your profile has been saved to profile.txt")

def main(): 
    print("=== Welcome to Profile Creator ===") 
    name = input("What's your name? ").strip() 
    color = input("What's your favourite color? ").strip() 
    
    if not name or not color: 
        print("Both name and color are required. Please run the script again.") 
        return 
            
    create_profile(name, color) 
        
if __name__ == "__main__": 
    main()