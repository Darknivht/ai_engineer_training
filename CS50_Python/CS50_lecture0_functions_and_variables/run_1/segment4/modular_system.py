"""Task Requirements:

Define main() at the top.
Define a helper function get_credentials(). It takes no parameters. 
Inside, prompt the user for a "Username" and an "API Key". Sanitize them. Return both values.
(Hint: Just like you unpacked .split() earlier, Python lets you return two variables at once by separating them with a comma: return username, key. 
You can unpack them in main() the exact same way: u, k = get_credentials()).
Define a second helper function format_endpoint(user, key). It takes two parameters. 
Inside, return an f-string that looks exactly like this: https://api.ai-provider.com/v1/models?user=[user]&token=[key]
Inside main():
Call get_credentials() and save the returned values.
Pass those values into format_endpoint() and save the returned URL.
print the final URL.
Call main() at the bottom."""

# Define main() func
def main():
    # Call get_credentials func and unpack values
    username, apikey = get_credentials()
    # Pass values gotten from get_credentials func to format_endpoint func and Save returned values
    url = format_endpoint(username, apikey)
    # Print returned values
    print(url)

# Define get_credentials() func
def get_credentials():
    # Prompt user for username and apikey and sanitize both
    username, apikey = input("Enter Username and Apikey: ").strip().split(" ")
    # return both values
    return username, apikey    


# Define format_endpoint(user, key) func
def format_endpoint(user, key):
    # Return an f-string
    return (f"https://api.ai-provider.com/v1/models?user={user}&token={key}")
    
# Call main func
main()