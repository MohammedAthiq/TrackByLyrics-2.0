# 🎧 TrackByLyrics 2.0

_Developed by [Syed Mohammed Athiq](https://github.com/MohammedAthiq)_

TrackByLyrics 2.0 is a **full-stack Flask web app** that helps users find songs from partial lyrics using the **Spotify Web API**.  
It includes **user authentication**, **personalized search history**, and a clean, responsive interface.

---

## 🚀 Features

- 🔐 User login and signup (Flask + SQLite)  
- 🎵 Search songs by entering partial lyrics  
- 🌙 Light/Dark theme toggle  
- 🎧 Displays song name, artist and album art
- 🔗 Direct Spotify link integration  

---

## 🧠 Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Flask (Python)  
**Database:** SQLite  
**API:** Spotify Web API  
**Deployment:** Render  

---

## 🌐 Live Demo

**Live:** [https://trackbylyrics2-0.onrender.com](https://trackbylyrics2-0.onrender.com)

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
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   SECRET_KEY=your_secret_key
   DATABASE_PATH=trackbylyrics.db
   ```

5. **Initialize the database**
   ```bash
   python database.py
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
│   └── login.html
├── static/
│   ├── style.css
│   └── script.js
├── requirements.txt
├── .env (ignored)
├── .gitignore
└── README.md
```

---

## 🚀 Deployment (Render)

1. Connect your GitHub repo to Render.  
2. Add environment variables in **Settings**.  
3. Add a **persistent disk** for SQLite:
   - Mount path: `/opt/render/project/data`
   - Env var: `DATABASE_PATH=/opt/render/project/data/trackbylyrics.db`
4. **Build Command**
   ```bash
   pip install -r requirements.txt && python database.py
   ```
5. **Start Command**
   ```bash
   gunicorn app:app
   ```

---

## 🌟 Future Enhancements

- Migrate from SQLite to PostgreSQL  
- Add a “My Search History” dashboard  
- Integrate AI-based lyric suggestions  
- Improve responsive UI  

---

## 📜 License

Open source under the [MIT License](LICENSE).

---
