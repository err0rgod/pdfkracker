import argparse
import pikepdf
from utils import read_passwords, attempt_open_pdf

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