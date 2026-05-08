"""Task: Prompt the user to set an "Agent Role". 
Sanitize it to lowercase. Check if the role is not equal (!=) to "admin". 
If it is not admin, print Access Granted. Role set to [role]. 
If they do type "admin", print Access Denied. You cannot claim the Admin role."""

# Define main func
def main():
    # Prompt user for agent_role and sanitise
    agent_role = input("Set Agent Role: ").strip().lower()
    role_checker(agent_role)

# Define role_checker func
def role_checker(role):
    denied_role = "admin"
    # Check if role is not equal to admin if admin access to be denied
    if role != denied_role:
        print(f"Access Granted. Role set to {role}")
    else:
        print("Access Denied. You cannot claim the Admin role")
        
main()