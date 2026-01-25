# verify_setup.py

import sys

def verify_setup():
    """Verify all components are properly installed"""
    
    checks = []
    
    # Check 1: Python version
    try:
        assert sys.version_info >= (3, 8)
        checks.append(("✓", "Python version >= 3.8"))
    except:
        checks.append(("✗", "Python version >= 3.8"))
    
    # Check 2: Import FastAPI
    try:
        import fastapi
        checks.append(("✓", "FastAPI installed"))
    except:
        checks.append(("✗", "FastAPI installed"))
    
    # Check 3: Import Librosa
    try:
        import librosa
        checks.append(("✓", "Librosa installed"))
    except:
        checks.append(("✗", "Librosa installed"))
    
    # Check 4: Import PyTorch
    try:
        import torch
        checks.append(("✓", "PyTorch installed"))
    except:
        checks.append(("✗", "PyTorch installed"))
    
    # Check 5: Import config
    try:
        from config import config
        checks.append(("✓", "Config loaded"))
    except:
        checks.append(("✗", "Config loaded"))
    
    # Check 6: Directories exist
    import os
    dirs = ["models", "tests", "test_samples", "utils"]
    all_exist = all(os.path.exists(d) for d in dirs)
    if all_exist:
        checks.append(("✓", "All directories created"))
    else:
        checks.append(("✗", "All directories created"))
    
    # Print results
    print("\n" + "="*50)
    print("SETUP VERIFICATION")
    print("="*50 + "\n")
    
    for symbol, check in checks:
        print(f"{symbol} {check}")
    
    print("\n" + "="*50)
    
    # Final verdict
    all_passed = all(symbol == "✓" for symbol, _ in checks)
    if all_passed:
        print("✓ ALL CHECKS PASSED - Setup Complete!")
        print("Run 'python main.py' to start the server")
    else:
        print("✗ Some checks failed - Please fix the issues above")
    print("="*50 + "\n")

if __name__ == "__main__":
    verify_setup()