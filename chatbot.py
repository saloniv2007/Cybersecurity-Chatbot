def chatbot():
    print("Welcome to My Cybersecurity Chatbot!")
    print("Type 'help' to see commands")
    print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Bot: Hello! How can i help you?")
    

    elif user == "How are you?":
        print("Bot: I am doing great!, Thanks for asking? ")
        
    elif user == "help":
        print("Available commands: ")
        print("phishing")
        print("malware")
        print("password")
        print("firewall")
        print("vpn")
        print("bye!")

    elif user == "phishing":
        print(" Bot: Phishing is a fake email or message used to steal personal information.")

    elif user == "malware":
        print("Bot: Malware is harmful software that can damage your computer.")

    elif user ==  "password":
        print("Bot: Use a strong password with letters, numbers, and special characters.")

    elif user == "firewall":
        print("Bot: A firewall protects your computer from unauthorized access.")

    elif user == "vpn":
        print("Bot: A vpn keeps your internet connection private and secure.")

    elif user == "bye":
        print("Bot: Good bye! Have a nice day")
        break
    
    else:
        print("Bot: Sorry! I don't understand. Type 'help' for available commands.")