def read_passwords(file_path):
    with open(file_path, 'r') as file:
        passwords = [line.strip() for line in file if line.strip()]
    return passwords

def attempt_open_pdf(pdf_path, password):
    try:
        with pikepdf.open(pdf_path, password=password):
            return True
    except (pikepdf.PasswordError, pikepdf.PdfError):
        return False

def crack_pdf_password(pdf_path, wordlist_path):
    passwords = read_passwords(wordlist_path)
    for password in passwords:
        if attempt_open_pdf(pdf_path, password):
            return password
    return None