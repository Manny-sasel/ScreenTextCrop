#!/usr/bin/env python3
"""
Installation Test Script for Live Screen Text Extractor
This script verifies that all dependencies are properly installed
"""

import sys
import subprocess
import importlib
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*50}")
    print(f" {title}")
    print(f"{'='*50}")

def print_result(test_name, success, message=""):
    """Print test result with formatting"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{test_name:<30} {status}")
    if message:
        print(f"    {message}")

def test_python_version():
    """Test Python version compatibility"""
    print_header("Python Version Check")
    
    version = sys.version_info
    required_version = (3, 7)
    
    success = version >= required_version
    message = f"Python {version.major}.{version.minor}.{version.micro}"
    
    if not success:
        message += f" (requires {required_version[0]}.{required_version[1]}+)"
    
    print_result("Python Version", success, message)
    return success

def test_dependencies():
    """Test if all required Python packages are installed"""
    print_header("Python Dependencies Check")
    
    dependencies = [
        ('tkinter', 'GUI framework'),
        ('cv2', 'OpenCV for image processing'),
        ('PIL', 'Pillow for image handling'),
        ('numpy', 'Numerical computing'),
        ('pytesseract', 'Tesseract OCR wrapper')
    ]
    
    all_success = True
    
    for module_name, description in dependencies:
        try:
            importlib.import_module(module_name)
            print_result(f"{module_name} ({description})", True)
        except ImportError as e:
            print_result(f"{module_name} ({description})", False, str(e))
            all_success = False
    
    return all_success

def test_tesseract():
    """Test Tesseract OCR installation"""
    print_header("Tesseract OCR Check")
    
    try:
        # Try to run tesseract command
        result = subprocess.run(['tesseract', '--version'], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print_result("Tesseract Command", True, version_line)
            
            # Test pytesseract integration
            import pytesseract
            try:
                version = pytesseract.get_tesseract_version()
                print_result("Pytesseract Integration", True, f"Version: {version}")
                return True
            except Exception as e:
                print_result("Pytesseract Integration", False, str(e))
                return False
        else:
            print_result("Tesseract Command", False, "Command failed")
            return False
            
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print_result("Tesseract Command", False, "Tesseract not found in PATH")
        
        # Provide installation instructions
        print("\n📋 Tesseract Installation Instructions:")
        if sys.platform.startswith('win'):
            print("  Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
        elif sys.platform.startswith('darwin'):
            print("  macOS: brew install tesseract")
        else:
            print("  Linux: sudo apt install tesseract-ocr")
            
        return False

def test_screen_capture():
    """Test screen capture capability"""
    print_header("Screen Capture Test")
    
    try:
        from PIL import ImageGrab
        
        # Try to capture a small portion of the screen
        test_image = ImageGrab.grab(bbox=(0, 0, 100, 100))
        
        if test_image and test_image.size == (100, 100):
            print_result("Screen Capture", True, f"Captured {test_image.size} image")
            return True
        else:
            print_result("Screen Capture", False, "Failed to capture screen")
            return False
            
    except Exception as e:
        print_result("Screen Capture", False, str(e))
        return False

def test_file_structure():
    """Test if all required files are present"""
    print_header("File Structure Check")
    
    required_files = [
        'screen_text_extractor.py',
        'requirements.txt',
        'README.md',
        'LICENSE'
    ]
    
    all_present = True
    current_dir = Path('.')
    
    for filename in required_files:
        file_path = current_dir / filename
        exists = file_path.exists()
        print_result(f"File: {filename}", exists)
        if not exists:
            all_present = False
    
    return all_present

def run_comprehensive_test():
    """Run all tests and provide summary"""
    print("🧪 Live Screen Text Extractor - Installation Test")
    print("=" * 60)
    
    tests = [
        ("Python Version", test_python_version),
        ("Dependencies", test_dependencies),
        ("Tesseract OCR", test_tesseract),
        ("Screen Capture", test_screen_capture),
        ("File Structure", test_file_structure)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_result(test_name, False, f"Test error: {str(e)}")
            results.append((test_name, False))
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! Your installation is ready.")
        print("You can now run: python screen_text_extractor.py")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please fix the issues above.")
        print("\nFailed tests:")
        for test_name, result in results:
            if not result:
                print(f"  - {test_name}")
    
    return passed == total

if __name__ == "__main__":
    success = run_comprehensive_test()
    sys.exit(0 if success else 1)