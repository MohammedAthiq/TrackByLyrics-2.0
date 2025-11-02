import requests
import base64
import os
import time
from dotenv import load_dotenv

# Load environment variables only if .env exists
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Cached token storage
access_token = None
token_expires_in = 0


def get_access_token():
    """Generate Spotify access token using Client Credentials Flow (cached for 1 hour)."""
    global access_token, token_expires_in

    # Reuse token if it's still valid
    if access_token and time.time() < token_expires_in:
        return access_token

    if not client_id or not client_secret:
        return None

    try:
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            "Authorization": f"Basic {b64_auth_str}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
        if response.status_code != 200:
            return None

        token_data = response.json()
        access_token = token_data.get("access_token")
        expires_in = token_data.get("expires_in", 3600)
        token_expires_in = time.time() + expires_in - 60  # refresh 1 min early
        return access_token

    except Exception:
        return None


def search_song(lyrics):
    """Search for a song on Spotify using lyrics as a query, with detailed debugging."""
    token = get_access_token()
    if not token:
        print("❌ Failed to obtain Spotify token. Check your credentials.")
        return {"error": "Failed to obtain Spotify token. Check your credentials."}

    try:
        headers = {"Authorization": f"Bearer {token}"}
        params = {"q": lyrics, "type": "track", "limit": 1}

        print(f"🔍 Searching Spotify for lyrics: {lyrics}")
        response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
        print(f"Spotify response status: {response.status_code}")

        if response.status_code != 200:
            print(f"❌ Spotify API error: {response.text}")
            return {"error": f"Spotify API returned {response.status_code}: {response.text}"}

        result = response.json()
        tracks = result.get("tracks", {}).get("items", [])

        if not tracks:
            print("⚠️ No song found for this query.")
            return {"error": "No song found with those lyrics"}

        track = tracks[0]
        print(f"✅ Found song: {track['name']} by {track['artists'][0]['name']}")

        return {
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
            "image": track["album"]["images"][0]["url"],
            "preview": track.get("preview_url")
        }

    except Exception as e:
        print(f"❌ Exception in search_song: {e}")
        return {"error": f"Unexpected error: {e}"}