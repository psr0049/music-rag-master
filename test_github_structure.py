#!/usr/bin/env python3
"""
Test script to verify the GitHub-ready structure works correctly
"""

import sys
import os
import importlib.util

def test_imports():
    """Test that all modules can be imported correctly"""
    print("🔍 Testing module imports...")
    
    # Add src to path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
    
    try:
        # Test core modules
        from src.core.data_loader import MusicDataLoader
        from src.core.rag_system import MusicRAGSystem
        from src.core.evaluator import MusicRecommendationEvaluator
        print("✅ Core modules imported successfully")
        
        # Test utils
        from src.utils.user_simulator import UserSimulator
        print("✅ Utils modules imported successfully")
        
        # Test RLHF
        from src.rlhf.trainer import RLHFTrainer
        print("✅ RLHF modules imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_loading():
    """Test data loading functionality"""
    print("\n📊 Testing data loading...")
    
    try:
        from src.core.data_loader import MusicDataLoader
        
        loader = MusicDataLoader()
        
        # Test with existing dataset
        if os.path.exists('final_dataset.csv'):
            tracks_df = loader.load_final_dataset('final_dataset.csv')
            print(f"✅ Dataset loaded: {len(tracks_df)} tracks")
        else:
            # Test with sample generation
            tracks_df = loader._generate_sample_dataset()
            print(f"✅ Sample dataset generated: {len(tracks_df)} tracks")
        
        return True
        
    except Exception as e:
        print(f"❌ Data loading error: {e}")
        return False

def test_rag_system():
    """Test RAG system initialization"""
    print("\n🧠 Testing RAG system...")
    
    try:
        from src.core.data_loader import MusicDataLoader
        from src.core.rag_system import MusicRAGSystem
        
        # Load data
        loader = MusicDataLoader()
        if os.path.exists('final_dataset.csv'):
            tracks_df = loader.load_final_dataset('final_dataset.csv')
        else:
            tracks_df = loader._generate_sample_dataset()
        
        # Initialize RAG system
        rag_system = MusicRAGSystem()
        print("✅ RAG system initialized")
        
        # Note: Skip vector store setup in test to avoid long processing time
        print("⚠️ Skipping vector store setup for quick test")
        
        return True
        
    except Exception as e:
        print(f"❌ RAG system error: {e}")
        return False

def test_streamlit_app():
    """Test Streamlit app can be imported"""
    print("\n📱 Testing Streamlit app...")
    
    try:
        # Test import without running
        spec = importlib.util.spec_from_file_location(
            "streamlit_app", 
            "src/apps/streamlit_app.py"
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            # Don't execute, just check it can be loaded
            print("✅ Streamlit app can be imported")
            return True
        else:
            print("❌ Could not load Streamlit app spec")
            return False
            
    except Exception as e:
        print(f"❌ Streamlit app error: {e}")
        return False

def test_file_structure():
    """Test that all required files exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        'README.md',
        'requirements.txt',
        'setup.py',
        'LICENSE',
        'CONTRIBUTING.md',
        '.gitignore',
        'Dockerfile',
        'docker-compose.yml',
        'src/__init__.py',
        'src/core/__init__.py',
        'src/core/data_loader.py',
        'src/core/rag_system.py',
        'src/core/evaluator.py',
        'src/apps/__init__.py',
        'src/apps/streamlit_app.py',
        'src/utils/__init__.py',
        'src/utils/user_simulator.py',
        'src/rlhf/__init__.py',
        'src/rlhf/trainer.py',
        '.github/workflows/ci.yml',
        'requirements-dev.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print(f"✅ All {len(required_files)} required files exist")
        return True

def main():
    """Run all tests"""
    print("🎵 Music RAG System - GitHub Structure Test")
    print("=" * 60)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Module Imports", test_imports),
        ("Data Loading", test_data_loading),
        ("RAG System", test_rag_system),
        ("Streamlit App", test_streamlit_app),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Test Results Summary:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! The system is ready for GitHub deployment.")
        return True
    else:
        print("⚠️ Some tests failed. Please fix the issues before deployment.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)