import logging
import os
import sys
from datetime import datetime

# Create log file name with current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Set log file path inside a "logs" directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)

# Use logging.getLogger() if you want to import it in other modules
logger = logging.getLogger(__name__)

# Corrected __name__ check
if __name__ == "__main__":
    logger.info("Logging has been set up.")
