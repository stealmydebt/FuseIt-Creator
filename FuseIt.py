from PIL import Image
import csv

def image_to_csv(image_path, output_csv):
    # Open the image file
    img = Image.open(image_path)
    img = img.convert("RGB")  # Convert to RGB mode if not already
    
    # Get image dimensions
    width, height = img.size
    
    # Create a CSV writer object
    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write header row
        csvwriter.writerow(['Row', 'Column', 'Red', 'Green', 'Blue'])
        
        # Iterate through each pixel
        for y in range(height):
            for x in range(width):
                # Get RGB values of the pixel
                r, g, b = img.getpixel((x, y))
                
                # Write pixel information to CSV
                csvwriter.writerow([y+1, x+1, r, g, b])

# Example usage
if __name__ == "__main__":
    # Specify input image path
    input_image = "example_image.jpg"
    
    # Specify output CSV path
    output_csv = "image_pixels.csv"
    
    # Convert image to CSV
    image_to_csv(input_image, output_csv)
    
    print("CSV grid of pixels generated successfully!")
