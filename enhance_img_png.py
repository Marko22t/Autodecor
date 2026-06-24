from PIL import Image, ImageEnhance, ImageFilter
import os

img_path = 'img/autodecor1.jpg'
out_path = 'img/autodecor1-upscaled.png'

if os.path.exists(img_path):
    img = Image.open(img_path)
    
    # Resize to 3x resolution using Lanczos filter
    new_size = (img.width * 3, img.height * 3)
    img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Apply a slight blur to reduce JPEG compression artifacts before sharpening
    img_smoothed = img_resized.filter(ImageFilter.GaussianBlur(radius=0.5))
    
    # Apply unsharp mask to bring back edges cleanly
    img_sharpened = img_smoothed.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    # Save as PNG to avoid any compression loss
    img_sharpened.save(out_path, 'PNG')
    print("Image enhanced and saved as PNG successfully!")
else:
    print("Image not found")
