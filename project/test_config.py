from src.config import load_env, get_key

# Load .env file
load_env()

print("API_KEY:", get_key("API_KEY"))
print("DATA_DIR:", get_key("DATA_DIR"))


