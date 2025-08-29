import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageGrab
import pytesseract
import threading
import time

class ScreenTextExtractor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen Text Extractor")
        self.root.geometry("180x160")
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.9)
        self.root.resizable(False, False)
        
        # Variables
        self.crop_coords = None
        self.cropped_image = None
        self.is_cropping = False
        self.overlay_window = None
        
        # Create floating control panel
        self.create_control_panel()
        
        # Position window at top-right corner
        self.root.geometry("+{}+50".format(self.root.winfo_screenwidth() - 220))
        
    def create_control_panel(self):
        """Create the main floating control panel"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Text Extractor", font=("Arial", 10, "bold"))
        title_label.pack(pady=(0, 10))
        
        # Buttons
        self.crop_btn = ttk.Button(main_frame, text="📷 Crop", command=self.start_crop, width=15)
        self.crop_btn.pack(pady=2)
        
        self.extract_btn = ttk.Button(main_frame, text="🔍 Extract", command=self.extract_text, 
                                    width=15, state='disabled')
        self.extract_btn.pack(pady=2)
        
        self.reset_btn = ttk.Button(main_frame, text="🔄 Reset", command=self.reset_crop, 
                                   width=15, state='disabled')
        self.reset_btn.pack(pady=2)
        
        # Make window draggable
        self.make_draggable()
        
    def make_draggable(self):
        """Make the control panel draggable"""
        def start_drag(event):
            self.root.x = event.x
            self.root.y = event.y
            
        def drag(event):
            x = self.root.winfo_pointerx() - self.root.x
            y = self.root.winfo_pointery() - self.root.y
            self.root.geometry(f"+{x}+{y}")
            
        self.root.bind("<Button-1>", start_drag)
        self.root.bind("<B1-Motion>", drag)
        
    def start_crop(self):
        """Start the screen cropping process"""
        self.is_cropping = True
        self.crop_btn.config(state='disabled')
        
        # Hide main window temporarily
        self.root.withdraw()
        
        # Create fullscreen overlay for cropping
        self.create_crop_overlay()
        
    def create_crop_overlay(self):
        """Create fullscreen overlay for area selection"""
        self.overlay_window = tk.Toplevel()
        self.overlay_window.attributes('-fullscreen', True)
        self.overlay_window.attributes('-alpha', 0.3)
        self.overlay_window.attributes('-topmost', True)
        self.overlay_window.configure(bg='black')
        self.overlay_window.cursor = "crosshair"
        
        # Variables for rectangle drawing
        self.start_x = None
        self.start_y = None
        self.rect_id = None
        
        # Create canvas for drawing selection rectangle
        self.canvas = tk.Canvas(self.overlay_window, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_crop_start)
        self.canvas.bind("<B1-Motion>", self.on_crop_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_crop_end)
        self.canvas.bind("<Escape>", self.cancel_crop)
        
        # Instructions
        instruction_text = "Click and drag to select area. Press Escape to cancel."
        self.canvas.create_text(self.overlay_window.winfo_screenwidth()//2, 50,
                              text=instruction_text, fill="white", font=("Arial", 16))
        
        self.canvas.focus_set()
        
    def on_crop_start(self, event):
        """Handle crop area selection start"""
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        
    def on_crop_drag(self, event):
        """Handle crop area dragging"""
        if self.start_x and self.start_y:
            # Remove previous rectangle
            if self.rect_id:
                self.canvas.delete(self.rect_id)
            
            # Draw new rectangle
            cur_x = self.canvas.canvasx(event.x)
            cur_y = self.canvas.canvasy(event.y)
            
            self.rect_id = self.canvas.create_rectangle(
                self.start_x, self.start_y, cur_x, cur_y,
                outline="red", width=2, fill="", stipple="gray25"
            )
            
    def on_crop_end(self, event):
        """Handle crop area selection end"""
        if self.start_x and self.start_y:
            end_x = self.canvas.canvasx(event.x)
            end_y = self.canvas.canvasy(event.y)
            
            # Store coordinates (ensure positive dimensions)
            x1, x2 = min(self.start_x, end_x), max(self.start_x, end_x)
            y1, y2 = min(self.start_y, end_y), max(self.start_y, end_y)
            
            if abs(x2 - x1) > 10 and abs(y2 - y1) > 10:  # Minimum size check
                self.crop_coords = (int(x1), int(y1), int(x2), int(y2))
                
                # Capture the selected area
                self.capture_cropped_area()
                
                # Close overlay and show main window
                self.close_crop_overlay()
                self.crop_completed()
            else:
                messagebox.showwarning("Selection Too Small", "Please select a larger area.")
                self.cancel_crop()
                
    def capture_cropped_area(self):
        """Capture the cropped screen area"""
        if self.crop_coords:
            x1, y1, x2, y2 = self.crop_coords
            # Capture screenshot of the selected area
            self.cropped_image = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
    def close_crop_overlay(self):
        """Close the crop overlay window"""
        if self.overlay_window:
            self.overlay_window.destroy()
            self.overlay_window = None
            
    def cancel_crop(self, event=None):
        """Cancel cropping operation"""
        self.close_crop_overlay()
        self.root.deiconify()
        self.crop_btn.config(state='normal')
        self.is_cropping = False
        
    def crop_completed(self):
        """Handle successful crop completion"""
        self.root.deiconify()
        self.crop_btn.config(state='normal')
        self.extract_btn.config(state='normal')
        self.reset_btn.config(state='normal')
        self.is_cropping = False
        
        # Show success message
        messagebox.showinfo("Crop Complete", "Area selected! Click Extract to get text.")
        
    def extract_text(self):
        """Extract text from cropped image using OCR"""
        if not self.cropped_image:
            messagebox.showerror("Error", "No cropped area available.")
            return
            
        try:
            # Disable extract button during processing
            self.extract_btn.config(state='disabled', text="Processing...")
            self.root.update()
            
            # Convert PIL image to OpenCV format for preprocessing
            img_array = np.array(self.cropped_image)
            img_cv = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
            
            # Preprocess image for better OCR
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            
            # Apply thresholding to get better text recognition
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            # Convert back to PIL Image
            processed_image = Image.fromarray(thresh)
            
            # Extract text using Tesseract
            extracted_text = pytesseract.image_to_string(processed_image, config='--psm 6')
            
            # Re-enable extract button
            self.extract_btn.config(state='normal', text="🔍 Extract")
            
            if extracted_text.strip():
                self.show_text_editor(extracted_text.strip())
            else:
                messagebox.showwarning("No Text Found", "No text could be extracted from the selected area.")
                
        except Exception as e:
            self.extract_btn.config(state='normal', text="🔍 Extract")
            messagebox.showerror("Error", f"Text extraction failed: {str(e)}")
            
    def show_text_editor(self, text):
        """Show extracted text in an editable window"""
        editor_window = tk.Toplevel(self.root)
        editor_window.title("Extracted Text - Edit & Copy")
        editor_window.geometry("500x400")
        editor_window.attributes('-topmost', True)
        
        # Position near the main window
        main_x = self.root.winfo_x()
        main_y = self.root.winfo_y()
        editor_window.geometry(f"+{main_x - 520}+{main_y}")
        
        # Create text editor frame
        main_frame = ttk.Frame(editor_window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Extracted Text", font=("Arial", 12, "bold"))
        title_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Text area with scrollbar
        self.text_area = scrolledtext.ScrolledText(
            main_frame, 
            wrap=tk.WORD, 
            width=60, 
            height=18,
            font=("Consolas", 10)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        self.text_area.insert(tk.END, text)
        
        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        # Buttons
        copy_btn = ttk.Button(button_frame, text="📋 Copy to Clipboard", 
                            command=lambda: self.copy_to_clipboard(editor_window))
        copy_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        select_all_btn = ttk.Button(button_frame, text="Select All", 
                                  command=lambda: self.text_area.tag_add(tk.SEL, "1.0", tk.END))
        select_all_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        clear_btn = ttk.Button(button_frame, text="Clear", 
                             command=lambda: self.text_area.delete("1.0", tk.END))
        clear_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        close_btn = ttk.Button(button_frame, text="Close", 
                             command=editor_window.destroy)
        close_btn.pack(side=tk.RIGHT)
        
        # Focus on text area
        self.text_area.focus_set()
        
    def copy_to_clipboard(self, window):
        """Copy text from editor to clipboard"""
        try:
            text_content = self.text_area.get("1.0", tk.END).strip()
            window.clipboard_clear()
            window.clipboard_append(text_content)
            messagebox.showinfo("Copied", "Text copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy text: {str(e)}")
            
    def reset_crop(self):
        """Reset the crop selection"""
        self.crop_coords = None
        self.cropped_image = None
        self.extract_btn.config(state='disabled')
        self.reset_btn.config(state='disabled')
        messagebox.showinfo("Reset", "Crop selection cleared. Ready for new selection.")
        
    def run(self):
        """Start the application"""
        # Check if Tesseract is available
        try:
            pytesseract.get_tesseract_version()
        except Exception:
            messagebox.showerror(
                "Tesseract Not Found", 
                "Tesseract OCR is required. Please install it:\n\n"
                "Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki\n"
                "Mac: brew install tesseract\n"
                "Linux: sudo apt install tesseract-ocr"
            )
            return
            
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        """Handle application closing"""
        if messagebox.askokcancel("Quit", "Do you want to quit the Text Extractor?"):
            self.root.destroy()

if __name__ == "__main__":
    app = ScreenTextExtractor()
    app.run()