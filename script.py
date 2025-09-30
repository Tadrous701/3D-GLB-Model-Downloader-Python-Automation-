import json
import requests
import os

HAR_FILE = "floorplanner.com.har"   # HAR file you exported
SAVE_DIR = "downloads"

os.makedirs(SAVE_DIR, exist_ok=True)

# Load HAR file
with open(HAR_FILE, "r", encoding="utf-8") as f:
    har_data = json.load(f)

urls = []
for entry in har_data["log"]["entries"]:
    url = entry["request"]["url"]
    mime = entry["response"]["content"].get("mimeType", "")
    if url.endswith(".glb") or "gltf-binary" in mime:
        urls.append(url)

print(f"Found {len(urls)} GLB files.")

# Download files
for i, url in enumerate(urls, start=1):
    filename = os.path.join(SAVE_DIR, f"model_{i}.glb")
    try:
        print(f"Downloading {url} -> {filename}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"[OK] Saved {filename}")
    except Exception as e:
        print(f"[ERROR] Could not download {url}: {e}")
