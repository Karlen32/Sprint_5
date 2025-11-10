import random

def generate_random_email():
    return f"test_{random.randint(1000000000, 9999999999)}@gmail.com"

def generate_random_password():
    return f"test_{random.randint(1000000000, 9999999999)}"

def generate_book_data():
    title = f"Test Book {random.randint(1000, 9999)}"
    description = f"Test Description {random.randint(1000, 9999)}"
    return title, description
