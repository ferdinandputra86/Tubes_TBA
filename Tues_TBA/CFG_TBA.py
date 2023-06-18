CppFor = """for ( int i = 5 ; i > 10 ; i ++ ) { c = b + c ; }"""

# Regular expressions for token matching
REGEX_FOR = ["for"]
REGEX_INT = ["int"]
REGEX_VAR = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
REGEX_ANGKA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
REGEX_CREMENT = ["++", "--"]
REGEX_OPERATOR = ["+", "-", "*", "/"]
REGEX_OPERATORPEMBANDING = [">=", "<=", "<", ">"]

# Token definition
TOKENS = [
    ("FOR", REGEX_FOR),
    ("INT",REGEX_INT),
    ("VAR", REGEX_VAR),
    ("ANGKA", REGEX_ANGKA),
    ("CREMENT", REGEX_CREMENT),
    ("OPERATOR", REGEX_OPERATOR),
    ("OPERATORPEMBANDING", REGEX_OPERATORPEMBANDING),
    ("{", ["{"]),
    ("}", ["}"]),
    (";", [";"]),
    ("=", ["="]),
    ("(",["("]),
    (")",[")"]),
]

CppFor = CppFor.replace(" ", "")  # Remove whitespace from the input string

tokens = []

while CppFor:
    found_token = False
    for token_type, regex_list in TOKENS:
        for regex in regex_list:
            if CppFor.startswith(regex):
                tokens.append((CppFor[:len(regex)], token_type))
                CppFor = CppFor[len(regex):]
                found_token = True
                break
        if found_token:
            break
    if not found_token:
        print(f"Error: Invalid token '{CppFor[0]}'")
        break

for token, token_type in tokens:
    print(f"Token: {token:15} Type: {token_type}")