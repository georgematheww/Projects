import re

def check_password_strength(password):
    # Criteria checks
    length_criteria = 1 <= len(password) <= 16
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[@#$%^&+=]', password) is not None

    criteria_met = sum([upper_criteria, lower_criteria, digit_criteria, special_criteria])

    if len(password) < 8:
        if criteria_met == 0:
            return "Very Weak"
        elif criteria_met == 1:
            return "Weak"
        elif criteria_met == 2:
            return "Moderate"
        else:
            return "Strong"
    else:
        if criteria_met == 0:
            return "Weak"
        elif criteria_met == 1:
            return "Moderate"
        elif criteria_met == 2:
            return "Strong"
        else:
            return "Very Strong"

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    print("Password strength:", check_password_strength(password))
