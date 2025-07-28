# 🎵 Music RAG AI - Intelligent Music Recommendation System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

**An AI-powered music recommendation system using Retrieval-Augmented Generation (RAG) with cultural intelligence and advanced analytics.**

## ✨ Features

### 🧠 **AI-Powered Recommendations**
- **Semantic Search**: Natural language queries for music discovery
- **Audio Feature Matching**: Recommendations based on musical characteristics  
- **Hybrid Approach**: Combines multiple recommendation strategies
- **Cultural Intelligence**: Genre-aware artist similarity matching

### 📊 **Advanced Analytics**
- **Real-time Analysis**: Interactive music data exploration
- **Clustering**: K-means clustering of music tracks
- **PCA Visualization**: Principal component analysis of audio features
- **Statistical Insights**: Comprehensive genre and popularity analysis

### 🤖 **RLHF Integration**
- **Reinforcement Learning**: Learns from user feedback
- **Continuous Improvement**: Adapts recommendations over time
- **Personalized Ranking**: Optimizes for individual preferences

### 🎨 **Modern Interface**
- **Streamlit Dashboard**: Beautiful, responsive web interface
- **Interactive Visualizations**: Plotly-powered charts and graphs
- **Multi-page Navigation**: Organized feature exploration
- **Real-time Updates**: Dynamic content based on user input

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/psr0049/music-rag-ai.git
   cd music-rag-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
music-rag-ai/
├── src/                          # Source code
│   ├── core/                     # Core RAG system
│   │   ├── rag_system.py        # Main RAG implementation
│   │   ├── data_loader.py       # Data loading and preprocessing
│   │   └── evaluator.py         # Recommendation evaluation
│   ├── apps/                     # Streamlit applications
│   │   └── streamlit_app.py     # Main web interface
│   ├── utils/                    # Utility modules
│   │   └── user_simulator.py    # User behavior simulation
│   └── rlhf/                     # RLHF components
│       └── trainer.py           # Reinforcement learning trainer
├── data/                         # Data directory
├── tests/                        # Test suite
├── requirements.txt              # Python dependencies
├── setup.py                     # Package setup
└── README.md                    # This file
```

## 🎵 Dataset

The system works with a comprehensive music dataset containing:
- **4,630+ tracks** from diverse artists
- **35+ genres** including Bollywood, Hollywood, K-pop, and more
- **Audio features** like energy, danceability, valence, acousticness
- **Rich metadata** including artist, album, popularity, and release year

## 🔧 Usage Examples

### Basic Recommendation
```python
from src.core.rag_system import MusicRAGSystem
from src.core.data_loader import MusicDataLoader

# Load data
loader = MusicDataLoader()
tracks_df = loader.load_final_dataset('final_dataset.csv')

# Initialize RAG system
rag_system = MusicRAGSystem()
rag_system.setup_vector_store(tracks_df)

# Get recommendations
recommendations, _ = rag_system.get_recommendations(
    preference_text="upbeat dance music for parties",
    n_recommendations=10
)

print(f"Recommended tracks: {recommendations}")
```

### Audio Feature-Based Recommendations
```python
# Define target audio features
target_features = {
    'energy': 0.8,        # High energy
    'danceability': 0.9,  # Very danceable
    'valence': 0.7        # Positive mood
}

# Get feature-based recommendations
feature_recs = rag_system.get_recommendations_by_audio_features(
    target_features=target_features,
    n_recommendations=10
)
```

## 🎨 Web Interface Features

### 📊 Dataset Overview
- Track and artist statistics
- Genre distribution analysis
- Popularity trends
- Sample data exploration

### 🎨 Audio Features Analysis
- Feature correlation heatmaps
- Genre-based feature distributions
- Interactive scatter plots
- Radar chart comparisons

### 🔍 Music Discovery
- Advanced filtering options
- Real-time search results
- Audio feature visualization
- Sorting and ranking

### 🎯 Recommendations
- **Audio Features Based**: Customize musical preferences
- **Artist Similarity**: Discover similar artists with cultural intelligence
- **Genre Exploration**: Explore music by genre with audio profiles

## 🤖 RLHF Training

The system includes Reinforcement Learning from Human Feedback capabilities:

```python
from src.rlhf.trainer import RLHFTrainer

# Initialize RLHF trainer
rlhf_trainer = RLHFTrainer(rag_system)

# Train with user feedback
rlhf_trainer.train_rlhf(tracks_df, num_epochs=1)

# The system automatically improves recommendations based on feedback
```

## 📊 Evaluation Metrics

The system includes comprehensive evaluation:
- **Diversity**: Genre and audio feature diversity
- **Novelty**: How different recommendations are from user history
- **Relevance**: Alignment with user preferences
- **Overall Score**: Weighted combination of all metrics

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Quality
```bash
flake8 src/
black src/
```

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py
```

### Docker Deployment
```bash
docker build -t music-rag-ai .
docker run -p 8501:8501 music-rag-ai
```

### Cloud Deployment
- **Streamlit Cloud**: Connect your GitHub repository
- **Heroku**: Use provided `Procfile`
- **AWS/GCP/Azure**: Use containerized deployment

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Spotify** for audio feature definitions and inspiration
- **Hugging Face** for transformer models and embeddings
- **Streamlit** for the amazing web framework
- **ChromaDB** for vector database capabilities
- **Plotly** for interactive visualizations

## 📈 Performance

- **Dataset Size**: 4,630 tracks
- **Loading Time**: ~2-3 seconds
- **Recommendation Speed**: <1 second per query
- **Memory Usage**: ~50MB for full dataset
- **Scalability**: Handles datasets up to 100K+ tracks

## 🔮 Future Enhancements

- [ ] Real-time Spotify API integration
- [ ] User authentication and profiles
- [ ] Collaborative filtering
- [ ] Mobile app development
- [ ] Multi-language support
- [ ] Advanced RLHF algorithms

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/psr0049/music-rag-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/psr0049/music-rag-ai/discussions)

---

**🎵 Discover music with AI-powered recommendations! 🎵**

Made with ❤️ by the Music RAG AI Team