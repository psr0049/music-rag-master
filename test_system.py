#!/usr/bin/env python3
"""
Test script to identify issues in the Music RAG system
"""

def test_data_loading():
    """Test data loading functionality"""
    print("🔍 Testing data loading...")
    try:
        from data_loader import MusicDataLoader
        loader = MusicDataLoader()
        tracks_df = loader.load_final_dataset('final_dataset.csv')
        print(f"✅ Data loading successful - Shape: {tracks_df.shape}")
        print(f"📊 Columns: {list(tracks_df.columns)[:10]}...")  # Show first 10 columns
        return tracks_df
    except Exception as e:
        print(f"❌ Data loading failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_rag_system(tracks_df):
    """Test RAG system initialization"""
    if tracks_df is None:
        print("⚠️ Skipping RAG test - no data loaded")
        return None
    
    print("\n🧠 Testing RAG system...")
    try:
        from music_rag_system import MusicRAGSystem
        rag_system = MusicRAGSystem()
        rag_system.setup_vector_store(tracks_df)
        print("✅ RAG system initialized successfully")
        return rag_system
    except Exception as e:
        print(f"❌ RAG system failed: {e}")
        import traceback
        traceback.print_exc()
        return None

def test_recommendations(rag_system):
    """Test recommendation functionality"""
    if rag_system is None:
        print("⚠️ Skipping recommendation test - RAG system not initialized")
        return
    
    print("\n🎵 Testing recommendations...")
    try:
        recommended_ids, _ = rag_system.get_recommendations(
            preference_text="upbeat dance music",
            n_recommendations=5
        )
        print(f"✅ Recommendations generated: {len(recommended_ids)} tracks")
        
        # Get track info
        recommended_tracks = rag_system.get_track_info(recommended_ids)
        print("📋 Sample recommendations:")
        for _, track in recommended_tracks.head(3).iterrows():
            print(f"  • {track['track_name']} by {track['artist_name']}")
        
    except Exception as e:
        print(f"❌ Recommendations failed: {e}")
        import traceback
        traceback.print_exc()

def test_streamlit_app():
    """Test if Streamlit app can be imported"""
    print("\n📱 Testing Streamlit app imports...")
    try:
        import app
        print("✅ Main app.py imports successfully")
    except Exception as e:
        print(f"❌ app.py import failed: {e}")
        import traceback
        traceback.print_exc()
    
    try:
        import enhanced_app
        print("✅ enhanced_app.py imports successfully")
    except Exception as e:
        print(f"❌ enhanced_app.py import failed: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Run all tests"""
    print("🎵 Music RAG System - Diagnostic Test")
    print("=" * 50)
    
    # Test data loading
    tracks_df = test_data_loading()
    
    # Test RAG system
    rag_system = test_rag_system(tracks_df)
    
    # Test recommendations
    test_recommendations(rag_system)
    
    # Test Streamlit apps
    test_streamlit_app()
    
    print("\n" + "=" * 50)
    print("🏁 Diagnostic test complete!")

if __name__ == "__main__":
    main()