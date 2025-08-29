# Contributing to Live Screen Text Extractor

Thank you for your interest in contributing to Live Screen Text Extractor! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **🐛 Bug Reports**: Found a bug? Let us know!
- **✨ Feature Requests**: Have an idea for improvement?
- **📝 Documentation**: Help improve our docs
- **💻 Code Contributions**: Submit bug fixes or new features
- **🧪 Testing**: Help test the application on different platforms
- **🌐 Translations**: Help make the app accessible in more languages

## 🚀 Getting Started

### 1. Fork the Repository
1. Fork the project on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/live-screen-text-extractor.git
   cd live-screen-text-extractor
   ```

### 2. Set Up Development Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

3. Test the installation:
   ```bash
   python test_installation.py
   ```

### 3. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

## 📝 Development Guidelines

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and reasonably sized
- Use type hints where appropriate

### Code Example
```python
def extract_text_from_image(image: Image.Image, config: str = '--psm 6') -> str:
    """
    Extract text from an image using OCR.
    
    Args:
        image: PIL Image object to extract text from
        config: Tesseract configuration string
        
    Returns:
        Extracted text as string
        
    Raises:
        OCRException: If text extraction fails
    """
    try:
        return pytesseract.image_to_string(image, config=config)
    except Exception as e:
        raise OCRException(f"Failed to extract text: {str(e)}")
```

### Commit Messages
Use clear, descriptive commit messages:

```bash
# Good
git commit -m "Add support for custom OCR configurations"
git commit -m "Fix window positioning on multi-monitor setups"
git commit -m "Update README with installation troubleshooting"

# Less ideal
git commit -m "Fix bug"
git commit -m "Update stuff"
git commit -m "Changes"
```

### Testing
- Test your changes on your local system
- Verify the application works on different screen resolutions
- Test with various types of text (different fonts, sizes, backgrounds)
- Run the installation test: `python test_installation.py`

## 🐛 Bug Reports

When reporting bugs, please include:

### Required Information
- **Operating System**: Windows 10, macOS Big Sur, Ubuntu 20.04, etc.
- **Python Version**: Output of `python --version`
- **Dependencies**: Run `pip list` and include relevant package versions
- **Tesseract Version**: Output of `tesseract --version`

### Bug Report Template
```markdown
**Describe the Bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**System Information**
- OS: [e.g. Windows 10]
- Python Version: [e.g. 3.9.7]
- Tesseract Version: [e.g. 5.0.1]

**Additional Context**
Add any other context about the problem here.
```

## ✨ Feature Requests

### Before Requesting
1. Check existing issues to avoid duplicates
2. Consider if the feature fits the project's scope
3. Think about how it would benefit other users

### Feature Request Template
```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Problem it Solves**
What problem does this feature address?

**Proposed Solution**
How do you envision this feature working?

**Alternatives Considered**
Have you considered alternative solutions?

**Additional Context**
Screenshots, mockups, or examples would be helpful.
```

## 💻 Pull Requests

### Before Submitting
1. Ensure your code follows the style guidelines
2. Test your changes thoroughly
3. Update documentation if necessary
4. Make sure all existing tests still pass

### Pull Request Process
1. **Create a Pull Request** with a clear title and description
2. **Reference any related issues**: "Closes #123" or "Fixes #456"
3. **Describe your changes**: What did you change and why?
4. **Include screenshots** for UI changes
5. **Be responsive** to feedback and review comments

### Pull Request Template
```markdown
**Description**
Brief description of the changes in this PR.

**Related Issue**
Closes #[issue number]

**Type of Change**
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

**Testing**
- [ ] I have tested these changes locally
- [ ] I have tested on multiple screen resolutions
- [ ] I have tested with different types of text/images

**Screenshots** (if applicable)
Add screenshots to demonstrate the changes.

**Checklist**
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly hard-to-understand areas
- [ ] I have updated the documentation accordingly
- [ ] My changes generate no new warnings
```

## 📋 Development Workflow

### Typical Development Cycle
1. **Choose an Issue**: Look for issues labeled "good first issue" if you're new
2. **Discuss**: Comment on the issue to discuss your approach
3. **Develop**: Create your branch and implement the changes
4. **Test**: Thoroughly test your changes
5. **Document**: Update docs and add comments as needed
6. **Submit**: Create a pull request
7. **Iterate**: Address feedback and make improvements

### Code Review Process
1. All submissions require review
2. Reviews focus on:
   - Code quality and style
   - Functionality and correctness
   - Performance implications
   - User experience impact
   - Documentation completeness

## 🎯 Priority Areas

We especially welcome contributions in these areas:

### High Priority
- **Cross-platform compatibility improvements**
- **OCR accuracy enhancements**
- **Performance optimizations**
- **UI/UX improvements**
- **Error handling and user feedback**

### Medium Priority
- **Additional OCR languages support**
- **Export format options**
- **Keyboard shortcuts**
- **Configuration options**
- **Batch processing features**

### Lower Priority
- **Advanced image preprocessing**
- **Cloud OCR integration**
- **Plugin system**
- **Advanced text processing features**

## 🏆 Recognition

Contributors will be:
- Listed in the project's README
- Mentioned in release notes for significant contributions
- Given credit in commit messages and pull requests

## 📞 Getting Help

If you need help contributing:

1. **Check existing documentation** in this repository
2. **Search closed issues** for similar questions
3. **Create a discussion** in the GitHub Discussions tab
4. **Contact maintainers** through GitHub issues

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a professional atmosphere

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or inflammatory comments
- Personal attacks
- Publishing others' private information

## 🎉 Thank You!

Every contribution, no matter how small, helps make this project better. We appreciate:
- Bug reports that help us improve quality
- Feature suggestions that enhance functionality  
- Code contributions that add capabilities
- Documentation improvements that help users
- Testing feedback that ensures reliability

**Happy Contributing!** 🚀