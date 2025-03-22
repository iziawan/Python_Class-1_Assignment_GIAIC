# **Part 4: Combining String Methods with F-Strings**

first_name = input("Enter your first name: ").strip().capitalize()
last_name = input("Enter your last name: ").strip().capitalize()
birth_year = input("Enter your birth year: ").strip()
current_year = 2025
age = current_year - int(birth_year)
username = f"{first_name[0].lower()}{last_name.lower()}{birth_year}"

profile_message = f"Profile: {first_name} {last_name}, Age: {age}, Username: {username}"
print(profile_message)
