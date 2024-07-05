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
    return mapping.get(c, '0')

def filter_and_deduplicate(soundex_codes):
    filtered_codes = []
    prev_code = ''
    for code in soundex_codes:
        if code != '0' and code != prev_code:
            filtered_codes.append(code)
            prev_code = code
    return filtered_codes

def pad_or_trim(soundex):
    return soundex[:4].ljust(4, '0')

def generate_soundex(name):
    if not name:
        return ""

    first_letter = name[0].upper()
    soundex_codes = [get_soundex_code(char) for char in name[1:]]

    filtered_codes = filter_and_deduplicate(soundex_codes)
    soundex = first_letter + ''.join(filtered_codes)

    return pad_or_trim(soundex)
