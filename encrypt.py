from string import printable



def encrypt_message(message: str, shift: int) -> str:
    alphabet = 'аьвгджзийклмнопрсуфхцшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += printable
    encrypted_message = ''
    for char in message:
        index = alphabet.find(char)
        encrypted_message += alphabet[index + shift]
    return encrypted_message


print(encrypt_message('Вася', 1))
