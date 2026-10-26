# Password Suggestion Tool

A simple desktop password generator built with **Python** and **Tkinter**. It provides a graphical interface to choose a password length, generate a random password, copy it to the clipboard, and clear the output.

## Features

- Enter a password length (1–256 characters)
- Generate a random password using letters, digits, and symbols
- Copy the generated password to the clipboard
- Clear the generated password
- Input validation and error messages
- Dark-themed desktop GUI

## Tech stack

- Python 3
- Tkinter (Python GUI toolkit)
- `random` module (used by the current implementation)
- VS Code (recommended editor)

## Requirements

- Python 3 installed
- Tkinter available with your Python installation (commonly included with standard Python on Windows)

No third-party Python packages are required.

## Run the project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Run:

   ```bash
   python pass_frontend.py
   ```

5. Enter a password length and click **Generate password**.
6. Click **Copy password** to copy the generated password.

On some systems, use `python3 pass_frontend.py` instead of `python`.

## Project files

- `pass_frontend.py` — desktop GUI application.
- `pass.py` — original command-line version (included if present).

## Security note

This project is intended for learning and demonstration. The current implementation uses Python's `random` module, which is **not recommended for generating passwords for real accounts**. For real-world password generation, use Python's `secrets` module and consider storing passwords only in a trusted password manager. Do not commit real passwords, API keys, or other secrets to GitHub.

## Future improvements

- Replace `random` with `secrets` for cryptographically secure generation
- Add options to include/exclude character types
- Add password strength estimation
- Add automated tests

## License

This project is released under the MIT License. See [LICENSE](LICENSE).
