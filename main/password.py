import re

def check_password_strength(password):
    """Checks the strength of a given password."""
    strength = 0
    criteria = [
        (r".{8,}", "At least 8 characters"),
        (r"[A-Z]", "At least one uppercase letter"),
        (r"[a-z]", "At least one lowercase letter"),
        (r"[0-9]", "At least one digit"),
        (r"[\W_]", "At least one special character (!@#$%^&*)")
    ]

    print("Checking password strength...")
    
    for pattern, msg in criteria:
        if re.search(pattern, password):
            strength += 1
        else:
            print(f"❌ {msg}")

    if strength == 5:
        return True
    else:
        print("❌ Weak Password - Improve security!")
        return False

if __name__ == "__main__":
    while True:
        password = input("Enter a strong password: ")
        if check_password_strength(password):
            print("✅ Strong Password Accepted")
            break
