class User:
    def __init__(self,DisplayName, UserPrincipalName, Username, Department):
        self.DisplayName = DisplayName
        self.UserPrincipalName = UserPrincipalName
        self.Username = Username.strip()
        self.Department = Department
    
    def __str__(self):
        return f"{self.Username}"
    
    def __repr__(self):
        return f"UserClass:{self.Username}"