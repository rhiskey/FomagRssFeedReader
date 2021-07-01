# settings.py
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path  # Python 3.6+ only


load_dotenv()

load_dotenv(verbose=True)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

db_server = os.getenv("DB_SERVER")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_driver = os.getenv("DB_DRIVER")

debug = os.getenv("DEBUG")

hours_delay = int(os.getenv("HOURS_DELAY"))
weeks_delay = int(os.getenv("WEEKS_DELAY"))
minutes_delay = int(os.getenv("MINUTES_DELAY"))
