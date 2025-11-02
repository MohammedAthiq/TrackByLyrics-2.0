# 🎧 TrackByLyrics 2.0

_Developed by [Syed Mohammed Athiq](https://github.com/MohammedAthiq)_

TrackByLyrics 2.0 is a **full-stack Flask web app** that lets users find songs from partial lyrics using the **Spotify Web API**.  
It now uses **Neon PostgreSQL** for cloud database storage, includes **user authentication**, and features a modern UI with **Dark/Light mode** support.

---

## 🚀 Features

- 🔐 User login and signup (Flask + Neon PostgreSQL)  
- 🎵 Search songs by partial lyrics using Spotify API  
- 💾 Stores user search history in Neon cloud database  
- 🌙 Dark/Light mode toggle   
- 🎧 Displays song name, artist, album art, and Spotify link  
- ☁️ Fully deployed on Render  

---

## 🧠 Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Flask (Python)  
**Database:** Neon PostgreSQL  
**API:** Spotify Web API  
**Deployment:** Render  

---


## ⚙️ Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MohammedAthiq/TrackByLyrics-2.0.git
   cd trackbylyrics2.0
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add environment variables**
   Create a `.env` file in the project root:
   ```env
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   SECRET_KEY=your_flask_secret_key
   DATABASE_URL=your_neon_postgres_url
   ```

5. **Initialize the database**
   ```bash
   python test_db.py
   ```

6. **Run the app**
   ```bash
   python app.py
   ```
   Visit **http://127.0.0.1:5001**

---

## 📂 Project Structure

```bash
trackbylyrics2.0/
├── app.py
├── utils.py
├── database.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── header.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
├── .env (ignored)
├── .gitignore
└── README.md
```

---

## 🚀 Deployment (Render + Neon)

1. Connect your GitHub repo to Render.  
2. Add environment variables in **Settings → Environment**.  
3. Use **Neon PostgreSQL** for database (no disk required).  
4. **Build Command**
   ```bash
   pip install -r requirements.txt
   ```
5. **Start Command**
   ```bash
   gunicorn app:app
   ```

---

## 🧩 Environment Variables on Render

| Key | Description |
|-----|--------------|
| `SPOTIFY_CLIENT_ID` | Your Spotify API client ID |
| `SPOTIFY_CLIENT_SECRET` | Your Spotify API secret |
| `DATABASE_URL` | Your Neon PostgreSQL connection string |
| `SECRET_KEY` | Flask secret key |

---

## 🌟 Future Enhancements

- Add AI-based lyric similarity search  
- Personalized recommendations  
- “My History” dashboard  
- Improved UI animations  

---

## 📜 License

Open source under the [MIT License](LICENSE).

---
