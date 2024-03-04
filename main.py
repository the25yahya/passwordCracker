def check_password_in_wordlist():
    # Open the wordlist.txt file in read mode
    with open('wordlist.txt', 'r') as file:
        # Read each line in the file
        for line in file:
            # Remove leading/trailing whitespaces and newlines
            password = line.strip()
            # Check if the current line matches the password 'sosecret'
            if password == 'sosecret':
                print("Password 'sosecret' found in the wordlist.")
                return True
    # If the password is not found after checking all lines
    print("Password 'sosecret' not found in the wordlist.")
    return False

# Call the function to check if 'sosecret' is present in the wordlist
check_password_in_wordlist()
