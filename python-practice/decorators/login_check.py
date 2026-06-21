def login_required(func):
    def wrapper():
        print("Login Verified")
        func()
    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard()