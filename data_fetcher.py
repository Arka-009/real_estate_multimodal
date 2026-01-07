import requests
import os
from PIL import Image
from io import BytesIO

MAPBOX_TOKEN = "pk.eyJ1IjoiYXJrYXByYXZhYmlzd2FzOTE5IiwiYSI6ImNtazFjazh5YTA0anEzcHF3aTBmMWRvbTUifQ.hiIJnRAGojipNCvi2uuDMg"

def fetch_image(lat, lon, path, zoom=18, size=224):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    url = (
        f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},{zoom}/{size}x{size}"
        f"?access_token={MAPBOX_TOKEN}"
    )

    r = requests.get(url, timeout=10)
    if r.status_code == 200:
        img = Image.open(BytesIO(r.content)).convert("RGB")
        img.save(path)
    else:
        raise RuntimeError(f"Mapbox error {r.status_code}")
