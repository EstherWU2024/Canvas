# A simple drawing tool

## Introduction
This project is designed to demonstrate basic graphics concepts using Python, while also showcasing techniques such as object-oriented programming and recursion. It includes features such as:
- **Create a Canvas**: Generate a blank canvas by specifying width and height.
- **Draw a line**: Only support horizontal and vertical lines by giving two pairs of coordinates.
- **Draw a rectangle**: By specifying two corners.
- **Bucket fill**: Fill an area that connected to a given point (x,y) with a specified color.
- **Interactive Commands**: Provide commands in a user-friendly manner to draw and manipulate the canvas.

## Installation
Follow the steps below to set up the project on your local machine:
### 1. Prerequisites
Before installing, make sure you have the following installed on your system:
- **Python 3.6+**: You can download it from [python.org](https://www.python.org/downloads/).
- **Git** (optional): To clone the repository. You can download it from [git-scm.com](https://git-scm.com/).
---
### 2. Clone the Repository
1. Open a terminal or command prompt.
2. Run the following command to clone the project repository:
git clone <repository-url>


## Code Structure

The program is organized into the following components:

### **1. `Canvas` Class**
The `Canvas` class encapsulates all the operations related to drawing and manipulating the canvas. It contains methods to create, display, and modify the canvas.

- **Attributes:**
  - `w`: Width of the canvas.
  - `h`: Height of the canvas.
  - `canvas`: A 2D list representing the drawing area.

- **Methods:**
  - `__init__(self, w, h)`: Initializes a blank canvas of width `w` and height `h`.
  - `show(self)`: Displays the current state of the canvas in the terminal.
  - `check(self, x1, y1, x2, y2)`: Validates that the given coordinates are within the canvas boundaries and correctly ordered.
  - `line(self, x1, y1, x2, y2, is_show)`: Draws a horizontal or vertical line on the canvas.
  - `rectangle(self, x1, y1, x2, y2)`: Draws a rectangle by combining four lines.
  - `fill(self, x, y, c)`: Implements the bucket-fill operation using a recursive flood-fill algorithm.

### **2. `main` Function**
The `main` function provides the entry point for the program. It sets up the command-line interface and handles user inputs.

- **Key Responsibilities:**
  - Displays instructions and command syntax to the user.
  - Processes user commands and delegates them to the appropriate methods in the `Canvas` class.
  - Handles input validation and errors gracefully.

- **Available Commands:**
  - `C w h`: Creates a new canvas of width `w` and height `h`.
  - `L x1 y1 x2 y2`: Draws a line from `(x1, y1)` to `(x2, y2)` (only horizontal or vertical lines are supported).
  - `R x1 y1 x2 y2`: Draws a rectangle with the upper-left corner at `(x1, y1)` and bottom-right corner at `(x2, y2)`.
  - `B x y c`: Fills the area connected to `(x, y)` with the character `c`.
  - `Q`: Exits the program.

### **3. Command Handlers**
The program uses a dictionary to map command types to specific handler functions:
- `create_canvas`: Initializes a new canvas.
- `draw_line`: Draws a line on the canvas.
- `draw_rectangle`: Draws a rectangle on the canvas.
- `bucket_fill`: Fills a region on the canvas with a specified character.
- `quit_program`: Exits the application.

Each handler function validates the input, performs the requested operation, and handles any errors.

### **4. Recursive Flood-Fill Algorithm**
The `fill(self, x, y, c)` method uses recursion to implement the bucket-fill feature:
- It starts from a given point `(x, y)`.
- It recursively fills all connected blank spaces with the specified character `c`.
- The algorithm stops when it encounters the canvas boundary or a previously filled region.

---

If you have specific formatting requirements or need additional details about the code structure, let me know!




