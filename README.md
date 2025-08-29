# 📷 Live Screen Text Extractor

A powerful Python application that allows you to extract text from any part of your screen using OCR (Optical Character Recognition). Perfect for digitizing text from images, PDFs, videos, or any non-selectable content on your screen.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ Features

- **🎯 Precision Cropping**: Select any rectangular area on your screen with a visual overlay
- **🔍 Advanced OCR**: Extract text using Tesseract OCR with image preprocessing for better accuracy
- **✏️ Editable Results**: View and edit extracted text in a dedicated text editor window
- **🎈 Floating Control Panel**: Always-on-top, draggable interface that works with any application
- **📋 Quick Actions**: Copy to clipboard, select all, clear, and more
- **🔄 Workflow Management**: Intuitive crop → extract → edit → use workflow
- **🖥️ Cross-Platform**: Works on Windows, macOS, and Linux
- **⚡ Real-time Processing**: Fast text extraction with visual feedback

## 🚀 Demo

### Main Interface
The floating control panel stays on top of all applications:

```
┌─────────────────────┐
│    Text Extractor   │
├─────────────────────┤
│      📷 Crop        │
│      🔍 Extract     │
│      🔄 Reset       │
└─────────────────────┘
```

### Workflow
1. **Click "Crop"** → Screen overlay appears for area selection
2. **Draw rectangle** → Select the text area you want to extract from
3. **Click "Extract"** → OCR processes the selected area
4. **Edit & Use** → Text appears in an editable window for further use

## 📋 Requirements

### System Requirements
- Python 3.7 or higher
- Tesseract OCR engine
- Operating System: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)

### Python Dependencies
- `tkinter` (usually comes with Python)
- `opencv-python`
- `Pillow (PIL)`
- `pytesseract`
- `numpy`

## 🛠️ Installation

### 1. Install Tesseract OCR

**Windows:**
1. Download Tesseract installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Run the installer and install to default location (`C:\Program Files\Tesseract-OCR\`)
3. Add Tesseract to your system PATH (optional - the app will auto-detect it)

**macOS:**
```bash
# Using Homebrew (recommended)
brew install tesseract

# Using MacPorts
sudo port install tesseract3 +universal
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install tesseract-ocr
```

**Linux (CentOS/RHEL):**
```bash
sudo yum install tesseract
# or for newer versions
sudo dnf install tesseract
```

### 2. Clone the Repository
```bash
git clone https://github.com/yourusername/live-screen-text-extractor.git
cd live-screen-text-extractor
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python screen_text_extractor.py
```

## 🎮 Usage

### Basic Usage
1. **Launch the app**: Run `python screen_text_extractor.py`
2. **Position the control panel**: Drag it to your preferred location on screen
3. **Crop text area**: Click "Crop" and draw a rectangle around the text you want to extract
4. **Extract text**: Click "Extract" to process the selected area with OCR
5. **Edit and use**: The extracted text appears in an editable window where you can:
   - Edit and correct any OCR mistakes
   - Copy to clipboard
   - Select all text
   - Clear the content

### Advanced Tips
- **Better OCR accuracy**: Select areas with clear, high-contrast text
- **Minimum size**: Ensure your crop selection is at least 20x20 pixels
- **Multiple extractions**: Use "Reset" to clear and start a new extraction
- **Window management**: The control panel stays on top but can be moved anywhere

## ⚙️ Configuration

### Manual Tesseract Path (if auto-detection fails)
If the application can't find Tesseract automatically, you can set the path manually by editing the script:

```python
# Add this line after the imports in screen_text_extractor.py
pytesseract.pytesseract.tesseract_cmd = r'/path/to/your/tesseract'
```

**Common paths:**
- Windows: `r'C:\Program Files\Tesseract-OCR\tesseract.exe'`
- macOS: `r'/usr/local/bin/tesseract'` or `r'/opt/homebrew/bin/tesseract'`
- Linux: `r'/usr/bin/tesseract'`

### OCR Configuration
The application uses optimized OCR settings, but you can modify them in the `extract_text()` method:

```python
# Current configuration for better accuracy
extracted_text = pytesseract.image_to_string(processed_image, config='--psm 6')

# Alternative configurations:
# --psm 6: Uniform block of text (default)
# --psm 8: Single word
# --psm 13: Raw line. Treat as a single text line
```

## 🧪 Testing

### Verify Installation
Run the test script to check if everything is working:

```bash
python test_installation.py
```

### Test Tesseract
```bash
tesseract --version
```

This should output the Tesseract version information.

## 🐛 Troubleshooting

### Common Issues

**1. "Tesseract not found" error**
- Ensure Tesseract is installed correctly
- Check if Tesseract is in your system PATH
- Try setting the path manually (see Configuration section)

**2. Poor OCR accuracy**
- Select areas with clear, high-contrast text
- Avoid very small text selections
- Ensure good lighting in screenshots/photos

**3. App doesn't start**
- Check Python version: `python --version` (needs 3.7+)
- Install missing dependencies: `pip install -r requirements.txt`
- Try running with `python3` instead of `python`

**4. Crop overlay not working**
- Check if your system supports screen capture
- Try running as administrator (Windows) or with appropriate permissions
- Disable any screen recording blockers

### Getting Help
1. Check the [Issues](https://github.com/yourusername/live-screen-text-extractor/issues) page
2. Search for existing solutions
3. Create a new issue with:
   - Your operating system
   - Python version
   - Error messages (if any)
   - Steps to reproduce the problem

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Types of Contributions
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🧪 Test coverage
- 🌐 Translations
- 💡 Feature suggestions

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Coding Standards
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Include comments for complex logic
- Test your changes before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - The OCR engine that powers text extraction
- [OpenCV](https://opencv.org/) - Image processing capabilities
- [Pillow](https://pillow.readthedocs.io/) - Python imaging library
- [pytesseract](https://github.com/madmaze/pytesseract) - Python wrapper for Tesseract

## 📊 Project Stats

- **Language**: Python
- **Dependencies**: 4 main packages
- **Platforms**: Cross-platform (Windows, macOS, Linux)
- **License**: MIT
- **Status**: Active development

## 🔮 Future Enhancements

- [ ] Batch processing multiple screen areas
- [ ] OCR language selection
- [ ] Hotkey support for quick cropping
- [ ] Export to various formats (PDF, Word, etc.)
- [ ] Cloud OCR integration
- [ ] Text translation features
- [ ] History of extracted texts
- [ ] Custom OCR preprocessing options

## 📞 Support

If you find this project helpful, please:
- ⭐ Star this repository
- 🐛 Report any bugs
- 💡 Suggest new features
- 🤝 Contribute to the code

---

**Made with ❤️ by [Your Name]**

*Extract text from anywhere on your screen with ease!*