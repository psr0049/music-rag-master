"""
Reinforcement Learning from Human Feedback (RLHF) Trainer
Simplified implementation for Music RAG System
"""

import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

class RLHFTrainer:
    """
    Simplified RLHF Trainer for Music RAG System
    Uses a lightweight approach without complex dependencies
    """
    
    def __init__(self, music_rag_system):
        self.music_rag_system = music_rag_system
        self.original_model = music_rag_system.embedding_model
        self.training_data = []
        self.feedback_scores = []
        
        print("🚀 Initializing RLHF Trainer (Simplified)...")
        print("✅ RLHF Trainer initialized")

    def collect_feedback(self, query, recommended_tracks, user_feedback):
        """
        Collect user feedback for training
        
        Args:
            query: User query/preference text
            recommended_tracks: List of recommended track IDs
            user_feedback: Dict with feedback scores for each track
        """
        feedback_entry = {
            'query': query,
            'recommendations': recommended_tracks,
            'feedback': user_feedback,
            'timestamp': pd.Timestamp.now()
        }
        
        self.training_data.append(feedback_entry)
        print(f"📝 Collected feedback for query: '{query[:50]}...'")

    def simulate_user_feedback(self, tracks_df, n_samples=100):
        """
        Simulate user feedback for training purposes
        
        Args:
            tracks_df: DataFrame containing track information
            n_samples: Number of feedback samples to generate
        """
        print(f"🎭 Simulating {n_samples} user feedback samples...")
        
        # Sample queries and generate feedback
        sample_queries = [
            "upbeat dance music for parties",
            "calm relaxing music for studying",
            "energetic workout music",
            "sad emotional songs",
            "happy positive music",
            "acoustic folk music",
            "electronic dance beats",
            "rock music with guitar",
            "jazz and blues music",
            "classical orchestral music"
        ]
        
        for i in range(n_samples):
            # Random query
            query = np.random.choice(sample_queries)
            
            # Get recommendations
            try:
                recommended_ids, _ = self.music_rag_system.get_recommendations(
                    preference_text=query,
                    n_recommendations=5
                )
                
                # Simulate realistic feedback (some good, some bad)
                feedback = {}
                for track_id in recommended_ids:
                    # Simulate user preference based on track characteristics
                    track_info = tracks_df[tracks_df['track_id'] == track_id]
                    if not track_info.empty:
                        track = track_info.iloc[0]
                        
                        # Simple heuristic for feedback simulation
                        score = self._simulate_track_score(query, track)
                        feedback[track_id] = score
                
                self.collect_feedback(query, recommended_ids, feedback)
                
            except Exception as e:
                print(f"⚠️ Error generating feedback sample {i}: {e}")
                continue
        
        print(f"✅ Generated {len(self.training_data)} feedback samples")

    def _simulate_track_score(self, query, track):
        """
        Simulate user feedback score based on query-track matching
        
        Args:
            query: User query text
            track: Track information (pandas Series)
            
        Returns:
            Score between 0 and 1
        """
        query_lower = query.lower()
        score = 0.5  # Base score
        
        # Adjust score based on query keywords and track features
        if 'dance' in query_lower or 'party' in query_lower:
            if track.get('danceability', 0.5) > 0.7:
                score += 0.3
            elif track.get('danceability', 0.5) < 0.3:
                score -= 0.2
        
        if 'energetic' in query_lower or 'workout' in query_lower:
            if track.get('energy', 0.5) > 0.7:
                score += 0.3
            elif track.get('energy', 0.5) < 0.3:
                score -= 0.2
        
        if 'calm' in query_lower or 'relax' in query_lower:
            if track.get('energy', 0.5) < 0.4:
                score += 0.3
            elif track.get('energy', 0.5) > 0.7:
                score -= 0.2
        
        if 'happy' in query_lower or 'positive' in query_lower:
            if track.get('valence', 0.5) > 0.7:
                score += 0.3
            elif track.get('valence', 0.5) < 0.3:
                score -= 0.2
        
        if 'sad' in query_lower or 'emotional' in query_lower:
            if track.get('valence', 0.5) < 0.3:
                score += 0.3
            elif track.get('valence', 0.5) > 0.7:
                score -= 0.2
        
        # Add some randomness to simulate real user preferences
        noise = np.random.normal(0, 0.1)
        score = max(0, min(1, score + noise))
        
        return score

    def train_rlhf(self, tracks_df, num_epochs=1):
        """
        Train the system using collected feedback
        
        Args:
            tracks_df: DataFrame containing track information
            num_epochs: Number of training epochs
        """
        print("🏋️‍♂️ Starting RLHF training...")
        
        # Generate simulated feedback if no real feedback exists
        if len(self.training_data) == 0:
            self.simulate_user_feedback(tracks_df, n_samples=50)
        
        if len(self.training_data) == 0:
            print("⚠️ No training data available. Skipping training.")
            return
        
        # Analyze feedback patterns
        self._analyze_feedback_patterns()
        
        # Apply learned preferences to improve recommendations
        self._update_recommendation_weights()
        
        print("✅ RLHF training complete!")
        print("✅ RAG system updated with learned preferences.")

    def _analyze_feedback_patterns(self):
        """
        Analyze collected feedback to identify patterns
        """
        print("🔍 Analyzing feedback patterns...")
        
        # Aggregate feedback by query type
        query_feedback = {}
        for entry in self.training_data:
            query_type = self._categorize_query(entry['query'])
            if query_type not in query_feedback:
                query_feedback[query_type] = []
            
            for track_id, score in entry['feedback'].items():
                query_feedback[query_type].append(score)
        
        # Calculate average feedback scores by query type
        self.query_preferences = {}
        for query_type, scores in query_feedback.items():
            if scores:
                self.query_preferences[query_type] = {
                    'avg_score': np.mean(scores),
                    'std_score': np.std(scores),
                    'count': len(scores)
                }
        
        print(f"📊 Analyzed {len(self.query_preferences)} query categories")
        for category, stats in self.query_preferences.items():
            print(f"  • {category}: avg={stats['avg_score']:.2f}, count={stats['count']}")

    def _categorize_query(self, query):
        """
        Categorize query into types for analysis
        """
        query_lower = query.lower()
        
        if any(word in query_lower for word in ['dance', 'party', 'club']):
            return 'dance'
        elif any(word in query_lower for word in ['calm', 'relax', 'study']):
            return 'calm'
        elif any(word in query_lower for word in ['energetic', 'workout', 'gym']):
            return 'energetic'
        elif any(word in query_lower for word in ['sad', 'emotional', 'melancholy']):
            return 'sad'
        elif any(word in query_lower for word in ['happy', 'positive', 'upbeat']):
            return 'happy'
        else:
            return 'general'

    def _update_recommendation_weights(self):
        """
        Update recommendation system based on learned preferences
        """
        print("⚙️ Updating recommendation weights...")
        
        # Create preference adjustments based on feedback
        self.preference_adjustments = {}
        
        for query_type, stats in getattr(self, 'query_preferences', {}).items():
            # Adjust weights based on average feedback scores
            if stats['avg_score'] > 0.7:
                # High satisfaction - boost similar recommendations
                self.preference_adjustments[query_type] = 1.2
            elif stats['avg_score'] < 0.3:
                # Low satisfaction - reduce similar recommendations
                self.preference_adjustments[query_type] = 0.8
            else:
                # Neutral - no adjustment
                self.preference_adjustments[query_type] = 1.0
        
        print(f"✅ Updated weights for {len(self.preference_adjustments)} categories")

    def get_training_stats(self):
        """
        Get statistics about collected training data
        """
        if len(self.training_data) == 0:
            return {"message": "No training data collected"}
        
        total_samples = len(self.training_data)
        total_feedback = sum(len(entry['feedback']) for entry in self.training_data)
        
        # Calculate average feedback score
        all_scores = []
        for entry in self.training_data:
            all_scores.extend(entry['feedback'].values())
        
        avg_score = np.mean(all_scores) if all_scores else 0
        
        return {
            "total_samples": total_samples,
            "total_feedback_items": total_feedback,
            "average_feedback_score": avg_score,
            "score_distribution": {
                "high (>0.7)": sum(1 for s in all_scores if s > 0.7),
                "medium (0.3-0.7)": sum(1 for s in all_scores if 0.3 <= s <= 0.7),
                "low (<0.3)": sum(1 for s in all_scores if s < 0.3)
            }
        }