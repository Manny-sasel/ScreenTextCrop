# Changelog

All notable changes to the Live Screen Text Extractor project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Hotkey support for quick cropping
- Batch processing multiple screen areas
- OCR language selection
- Export to various formats (PDF, Word, etc.)
- Cloud OCR integration
- Text translation features
- History of extracted texts
- Custom OCR preprocessing options

## [1.0.0] - 2025-08-29

### Added
- **Core Features**
  - Floating control panel with draggable interface
  - Screen area cropping with visual overlay
  - OCR text extraction using Tesseract
  - Editable text results window
  - Copy to clipboard functionality
  
- **User Interface**
  - Always-on-top floating control panel
  - Visual crop selection with crosshair cursor
  - Intuitive three-button workflow (Crop → Extract → Reset)
  - Resizable and draggable text editor window
  - Real-time button state management
  
- **Cross-Platform Support**
  - Windows 10+ compatibility
  - macOS 10.14+ compatibility
  - Linux (Ubuntu 18.04+) compatibility
  - Automatic Tesseract path detection
  
- **OCR Features**
  - Image preprocessing for better accuracy
  - Thresholding and grayscale conversion
  - Configurable PSM (Page Segmentation Mode)
  - Error handling and user feedback
  
- **Text Processing**
  - Full text editing capabilities
  - Select all, copy, and clear functions
  - Automatic text area focus
  - Scrollable text display for long content
  
- **Installation & Setup**
  - Comprehensive installation test script
  - Automatic dependency checking
  - Cross-platform Tesseract detection
  - Detailed error messages and suggestions
  
- **Development Tools**
  - Professional project structure
  - Requirements.txt with version specifications
  - Setup.py for package distribution
  - Comprehensive documentation

### Technical Implementation
- **Dependencies**
  - tkinter for GUI framework
  - opencv-python for image processing
  - Pillow for image handling
  - pytesseract for OCR integration
  - numpy for numerical operations
  
- **Architecture**
  - Object-oriented design with single main class
  - Event-driven GUI with proper state management
  - Modular functions for each major feature
  - Error handling with user-friendly messages
  
- **Performance**
  - Efficient screen capture using ImageGrab
  - Optimized image preprocessing pipeline
  - Minimal memory footprint for GUI elements
  - Fast OCR processing with configurable settings

### Documentation
- **README.md**: Comprehensive user guide with installation instructions
- **CONTRIBUTING.md**: Detailed contributor guidelines and development setup
- **LICENSE**: MIT license for open-source distribution
- **CHANGELOG.md**: Version history and feature tracking
- **requirements.txt**: Python dependency specifications
- **setup.py**: Package installation and distribution setup
- **test_installation.py**: Automated installation verification

### Known Limitations
- Requires Tesseract OCR to be installed separately
- OCR accuracy depends on image quality and text clarity
- Minimum crop area size of 20x20 pixels required
- Single-threaded processing (OCR runs on main thread)
- Limited to rectangular selection areas only

### System Requirements
- Python 3.7 or higher
- Tesseract OCR engine
- Screen capture capabilities
- Minimum 4GB RAM recommended
- Display resolution 1024x768 or higher

---

## Version History Notes

### Versioning Strategy
- **Major versions (x.0.0)**: Breaking changes or significant feature additions
- **Minor versions (1.x.0)**: New features, improvements, non-breaking changes
- **Patch versions (1.0.x)**: Bug fixes, small improvements, documentation updates

### Release Planning
- **1.1.0**: Planned features include hotkey support and improved UI
- **1.2.0**: Batch processing and export functionality
- **2.0.0**: Major architecture changes or breaking API modifications

### Contributing to Changelog
When contributing, please update this changelog with:
- New features in the **Added** section
- Improvements in the **Changed** section
- Bug fixes in the **Fixed** section
- Removed features in the **Removed** section
- Security updates in the **Security** section

For more details on contributing, see [CONTRIBUTING.md](CONTRIBUTING.md).