# src/screengenie/watchers/screenshot_trigger.py
from pathlib import Path
from PIL import Image

from screengenie.capture.capture_screen import capture_from_file
from screengenie.core.pipeline import run_pipeline_from_image


def run():
    print("⚙️  Running pipeline with hardcoded test image...")

    # ⚠️ Update this to point to your actual test image path
    test_image_path = Path("/mnt/c/Users/pc/Pictures/Screenshots/Screenshot 2025-05-14 090506.png")

    if not test_image_path.exists():
        print(f"❌ File does not exist: {test_image_path}")
        return

    try:
        image = capture_from_file(test_image_path)
        suggestions = run_pipeline_from_image(image)
        print("\n✅ Suggestions:")
        for line in suggestions:
            print(f" - {line}")
    except Exception as e:
        print(f"❌ Error processing image: {e}")


if __name__ == "__main__":
    run()