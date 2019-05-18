BAD_CHARS = {'ș': 's', 'ü': 'u', '"': '', 'è': 'e', 'š': 's', '—': '', '-': '', 'ã': 'a', 'É': 'E', 'é': 'e',
             ',': '', "'": '', ')': '', '(': '', 'ó': 'o', '&apos;': ''}


def normalize(name):
    while name[0] == ' ':
        name = name[1:]
    while name[-1] == ' ':
        name = name[:-1]
    for key in BAD_CHARS:
        name = name.replace(key, BAD_CHARS[key])
    return name.lower()
