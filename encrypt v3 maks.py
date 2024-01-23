from string import ascii_letters, digits, punctuation


def encrypt_message(message: str, shift: int) -> str:
    alphabet = 'аьвгджзийклмнопрсуфхцшщъыьэюя'
    alphabet += alphabet.upper()
    alphabet += ascii_letters
    alphabet += digits
    alphabet += punctuation
    alphabet = alphabet.replace('"', "")
    alphabet = alphabet.replace("'", '')
    alphabet += ' '
    encrypted_message = ''
    for char in message:
        index = alphabet.find(char)
        if index == -1:
            print(f'Ошибка! Символ {char} не найден в алфавите!')
            return ''
        new_index = (index + shift) % len(alphabet)
        encrypted_message += alphabet[new_index]
    return encrypted_message

for i in range(-1, -160, -1):
    print(i, encrypt_message('игрок ', i))
