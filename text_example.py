# Simple Python Script to test static code analysis

def greet(name):
    """Function to greet the user."""
    print("Hello", name)

greet("Shubh")

# Let's add some intentional "warnings" to check bug detection
def unused_function():
    pass  # This function is unused and should trigger a warning in the analysis

x = 10
if x == 10:
    print("This is a simple check.")
