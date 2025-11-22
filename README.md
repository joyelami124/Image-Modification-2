# Image-Modification-2

⸻

Overview

This project repairs a broken 4-quadrant frame image by detecting the color-coded sections, cropping them, rotating them into their correct orientation, and recombining them into a fixed frame.
After repairing the frame, the program draws a custom “Angry Robot” illustration using PIL and places it neatly inside the corrected frame.

Features

Frame Repair
	•	Opens the original broken image.
	•	Detects four specific colors:
	•	Green
	•	Yellow
	•	Blue
	•	Red
	•	Locates the minimum and maximum x and y coordinates for each color.
	•	Crops out each quadrant using these coordinates.
	•	Resizes all quadrants to match the green section.
	•	Rotates each section to its proper orientation.
	•	Reassembles all sections into a new corrected frame.

Custom Drawing
	•	Creates a 400×400 digital illustration featuring:
	•	A robot head with eyes, mouth, antenna, and facial features.
	•	Geometric shapes such as rectangles, ellipses, lines, and polygons.
	•	Uses PIL’s ImageDraw module.

Final Composition
	•	Resizes the robot drawing to 80% of the repaired frame’s dimensions.
	•	Centers the drawing perfectly inside the frame.
	•	Displays the completed composite image.


Function Breakdown

1. repair_frame(frame)
	•	Loads an image and scans every pixel.
	•	Identifies the bounding box for each target color.
	•	Crops out each colored quadrant.
	•	Resizes and rotates each section.
	•	Reassembles them into a final corrected frame.
	•	Returns the repaired frame as a new image.

2. draw_image()
	•	Creates a blank 400×400 canvas.
	•	Draws a stylized “Angry Robot” using:
	•	rectangle
	•	ellipse
	•	polygon
	•	line
	•	text
	•	Returns the completed drawing.

3. frame_image(frame)
	•	Runs repair_frame(frame) to fix the broken image.
	•	Generates the robot drawing.
	•	Resizes the drawing to 80% of the frame.
	•	Centers the drawing using simple offset calculations.
	•	Shows the final composited image.

⸻

Dependencies

This project uses the Python Imaging Library (Pillow):

pip install pillow

⸻

Purpose of the Project
	•	Practice working with image manipulation.
	•	Apply cropping, resizing, and rotation using PIL.
	•	Detect pixel regions based on RGB values.
	•	Create and layer custom digital artwork.
	•	Combine multiple functions into a cohesive program.

⸻
