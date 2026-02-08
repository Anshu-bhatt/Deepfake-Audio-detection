"""
Quick test to see what the detection is actually returning
"""
import sys
import numpy as np
from model_detector import HybridDetector
from audio_preprocessor import AudioProcessor
import soundfile as sf

print("=" * 60)
print("DETECTION DEBUG TEST")
print("=" * 60)

# Initialize
print("\n1. Initializing models...")
audio_processor = AudioProcessor()
hybrid_detector = HybridDetector(ai_threshold=0.5)

# Load a test audio file
test_files = [
    "test_samples/Namami_30s.mp3",
    "test_samples/sample voice 1.mp3",
]

for test_file in test_files:
    try:
        print(f"\n{'='*60}")
        print(f"Testing: {test_file}")
        print('='*60)
        
        # Load audio
        audio, sr = sf.read(test_file)
        if len(audio.shape) > 1:
            audio = np.mean(audio, axis=1)
        
        print(f"✓ Loaded: {len(audio)/sr:.2f}s at {sr}Hz")
        
        # Resample if needed
        if sr != 16000:
            import librosa
            audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
            sr = 16000
        
        # Preprocess
        audio_processed = audio_processor.preprocess_audio(audio)
        print(f"✓ Preprocessed: {len(audio_processed)} samples")
        
        # Extract features
        features = audio_processor.extract_features(audio)
        print(f"✓ Extracted {len(features)} features")
        print(f"   - spectral_centroid_std: {features.get('spectral_centroid_std', 0):.4f}")
        print(f"   - zcr_std: {features.get('zcr_std', 0):.6f}")
        print(f"   - rms_std: {features.get('rms_std', 0):.6f}")
        
        # Detect
        classification, confidence, details = hybrid_detector.detect(
            audio_processed,
            features,
            sr
        )
        
        print(f"\n🎯 RESULT:")
        print(f"   Classification: {classification}")
        print(f"   Confidence: {confidence:.4f}")
        print(f"   Combined Score: {details['combined_score']:.4f}")
        print(f"   Wav2Vec2 AI Score: {details['wav2vec2'].get('ai_score', 0):.4f}")
        print(f"   Acoustic AI Score: {details['acoustic_ai_score']:.4f}")
        
    except Exception as e:
        print(f"❌ Error with {test_file}: {e}")
        import traceback
        traceback.print_exc()

print(f"\n{'='*60}")
print("TEST COMPLETE")
print('='*60)
