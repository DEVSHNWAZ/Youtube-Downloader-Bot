import os

# Load environment variables with validation
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Validate required environment variables
if not BOT_TOKEN:
    raise ValueError(
        "Missing required environment variable: BOT_TOKEN. "
        "Please configure it in your deployment environment."
    )

if not API_ID:
    raise ValueError(
        "Missing required environment variable: API_ID. "
        "Please configure it in your deployment environment."
    )

if not API_HASH:
    raise ValueError(
        "Missing required environment variable: API_HASH. "
        "Please configure it in your deployment environment."
    )

# Convert API_ID to integer
try:
    APP_ID = int(API_ID)
except (ValueError, TypeError) as e:
    raise ValueError(
        f"API_ID must be a valid integer, got: {API_ID}. Error: {e}"
    )

youtube_next_fetch = 0  # time in minutes
EDIT_TIME = 5
