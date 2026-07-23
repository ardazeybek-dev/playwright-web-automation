# Playwright Web Automation Bot

A web automation bot built with Python and the Playwright library.

## About
- Automatically navigates to the Ege University Bergama Vocational School website.
- Reads the page title and prints it to the terminal.
- Captures a full-page screenshot and saves it as `bergama_myo.png`.

## Run with Docker
The project is fully Dockerized:
1. Make sure Docker is running on your machine.
2. In the project folder:
   ```bash
   docker-compose up --build
   ```
3. The bot runs headless in the background and outputs `bergama_myo.png` to the project root.

## Run Locally (without Docker)
```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# macOS / Linux:
# source venv/bin/activate

pip install -r requirements.txt
playwright install chromium

python proje.py
```

## Configuration (optional)
The target site and output file can be changed via environment variables:

| Variable      | Default                           | Description                       |
|---------------|-----------------------------------|-----------------------------------|
| `TARGET_URL`  | `https://bergamamyo.ege.edu.tr/`  | Address to visit                  |
| `OUTPUT_PATH` | `bergama_myo.png`                 | Where to save the screenshot      |

Example:
```bash
TARGET_URL="https://ege.edu.tr" OUTPUT_PATH="ege.png" python proje.py
```
