from PIL import Image

def capture_from_file(path):
    """Load an image from a file path."""
    return Image.open(path)
