# PDF Password Cracker

A command-line tool for cracking PDF passwords using a wordlist.

## Features

- Attempts to unlock password-protected PDF files using a list of potential passwords.
- Utilizes the `pikepdf` library for handling PDF files.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pdf-password-cracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the PDF password cracker, run the following command in your terminal:

```
python src/main.py <path_to_pdf> <path_to_passwords>
```

- `<path_to_pdf>`: The path to the PDF file you want to crack.
- `<path_to_passwords>`: The path to the wordlist file (e.g., `passwords.txt`).

## Example

```
python src/main.py example.pdf passwords.txt
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.