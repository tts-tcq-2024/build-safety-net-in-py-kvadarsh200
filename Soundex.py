def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def generate_soundex(name):
    if not name:
        return ""

    first_letter = name[0].upper()
    soundex_codes = [get_soundex_code(char) for char in name[1:].upper()]

    # Filter out '0' codes and remove consecutive duplicates
    filtered_codes = [code for i, code in enumerate(soundex_codes) if code != '0' and (i == 0 or code != soundex_codes[i - 1])]

    soundex = first_letter + ''.join(filtered_codes)
    return soundex[:4].ljust(4, '0')
