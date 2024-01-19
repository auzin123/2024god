def check_password(password: str) -> bool:
    if len(password) < 10:
        return False
    isdigit = "False"
    islower = "False"
    isupper = "False"
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
    if has_lower and has_digit and has_upper:
        return True
    

    """
    elif password.isupper():
        return False
    elif password.islower():
        return False
    elif password.isdigit():
        return False
    return True
    """

assert check_password('..........') is False