"""Task: API Credential Mockup: Build a mock API credential display that concatenates a base URL, API key, and
model name into a formatted string. Simulates real-world AI engineering variable usage"""

base_url = input("Enter Base Url: ").strip().lower()
api_key = input("Api key: ").strip()
model_name = input("Enter Model Name: ").strip()

print(f"Connecting to {base_url} using key {api_key} and model {model_name}")