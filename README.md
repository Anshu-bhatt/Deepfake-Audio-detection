# 🎤 AI Voice Detection System

> **Professional deepfake audio detection with beautiful gradient UI**  
> Detect AI-generated voices vs. Human voices across multiple languages using advanced Wav2Vec2 embeddings and acoustic analysis.

---

## 🌟 Features

- **Beautiful Gradient UI** - Modern Flask web interface with blue-to-pink gradient design
- **AI Detection** - Hybrid approach combining Wav2Vec2 embeddings + acoustic features
- **Multi-Language Support** - Tamil, English, Hindi, Malayalam, Telugu
- **Real-time Processing** - Upload audio and get instant classification results
- **Client-side Trimming** - Automatically trim audio > 30 seconds using Web Audio API
- **Confidence Scoring** - HIGH/MEDIUM/LOW confidence levels with detailed metrics

---

## 🛠️ Tech Stack

**Frontend:** Flask, HTML5, CSS3, JavaScript, Web Audio API  
**Backend:** Python 3.10+, Flask, Wav2Vec2 (HuggingFace)  
**ML Models:** facebook/wav2vec2-base, Custom HybridDetector  
**Audio Processing:** librosa, soundfile, numpy  
**Deployment:** Railway, Docker-ready

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/Anshu-bhatt/Deepfake-Audio-detection.git
cd Deepfake-Audio-detection

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🚀 Quick Start

1. **Upload Audio** - Drag & drop or click to browse (MP3, WAV, OGG, M4A)
2. **Auto-Trim** - Audio > 30s will show trim option
3. **Detect** - Click "Detect Voice" button
4. **View Results** - See classification, confidence score, and processing time

---

## 📡 API Endpoints

### **Flask UI Endpoint**
```
POST /detect
- Upload audio file directly
- Returns: classification, confidence, details
```

### **FastAPI Backend** (Optional)
```
POST /classify
- Base64 encoded audio
- Returns: detailed classification with probabilities
```

---

## 🎯 Detection Logic

**Hybrid Detection System:**
- **70% Weight:** Wav2Vec2 embedding analysis (temporal variance, smoothness, consistency)
- **30% Weight:** Acoustic features (MFCC, spectral, zero-crossing rate)
- **Threshold:** Dynamic adjustment for short audio (<2s)

**Classification Thresholds:**
- AI_GENERATED: Combined score ≥ 0.60 (HIGH), ≥ 0.55 (MEDIUM)
- UNCERTAIN: 0.45-0.55 (LOW confidence)
- HUMAN: Combined score < 0.45

---

## 🌐 Deployment

**Railway (Recommended):**
- Push to GitHub → Auto-deploy
- Uses `Procfile` and `railway.json`
- Environment: `PORT` variable auto-configured

**Docker:**
```bash
docker build -t voice-detection .
docker run -p 5000:5000 voice-detection
```

---

## 📂 Project Structure

```
├── app.py                  # Flask web application
├── model_detector.py       # Wav2Vec2 + HybridDetector
├── audio_preprocessor.py   # Audio processing pipeline
├── templates/
│   └── index.html         # Gradient UI
├── requirements.txt        # Dependencies
├── Procfile               # Railway/Heroku config
└── railway.json           # Railway deployment config
```

---

## 🧪 Testing Locally

```bash
# Start Flask server
python app.py

# Test with sample audio
# Upload any audio file through the web UI at http://localhost:5000
```

---

## 📊 Performance

- **Processing Time:** ~2-3 seconds per audio file
- **Memory Usage:** ~1.5GB (Wav2Vec2 model loaded)
- **Supported Duration:** Up to 30 seconds
- **Audio Formats:** MP3, WAV, OGG, M4A, FLAC

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:
1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open Pull Request

---

## 📄 License

This project is developed for educational purposes as part of GUVI AI Hackathon.

---

## 👥 Authors

**Project Team:** AI Voice Detection  
**Institution:** GUVI AI Hackathon  
**Year:** 2026

---

## 🙏 Acknowledgments

- HuggingFace for Wav2Vec2 pre-trained models
- Facebook AI Research for Wav2Vec2 architecture
- GUVI for hosting the AI Hackathon

---

**⭐ Star this repo if you find it helpful!**
