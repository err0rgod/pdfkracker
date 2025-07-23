import argparse
import pikepdf

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



def main():
    parser = argparse.ArgumentParser(description="PDF Password Cracker")
    parser.add_argument("-p","--pdf_file", help="Path to the PDF file to crack")
    parser.add_argument("-w","--wordlist", help="Path to the password wordlist file", default="passwords.txt", nargs="?")

    args = parser.parse_args()
    
    passwords = read_passwords(args.wordlist)
    
    for password in passwords:
        if attempt_open_pdf(args.pdf_file, password):
            print(f"Password found: {password}")
            return
    
    print("Password not found in the provided wordlist.")

if __name__ == "__main__":
    main()