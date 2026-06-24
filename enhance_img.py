from PIL import Image, ImageEnhance, ImageFilter
import os

img_path = 'img/autodecor1.jpg'
out_path = 'img/autodecor1-hq.jpg'

if os.path.exists(img_path):
    img = Image.open(img_path)
    
    # Resize to 2x resolution using Lanczos filter (high quality resampling)
    new_size = (img.width * 2, img.height * 2)
    img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
    
    # Apply slight sharpening
    img_sharpened = img_resized.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    
    # Enhance contrast slightly
    enhancer = ImageEnhance.Contrast(img_sharpened)
    img_final = enhancer.enhance(1.05)
    
    # Save with high quality
    img_final.save(out_path, 'JPEG', quality=95)
    print("Image enhanced successfully!")
else:
    print("Image not found")
