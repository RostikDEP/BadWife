import os
from dotenv import load_dotenv
import config

load_dotenv()
TOKEN = os.getenv("TEST_TOKEN")
