
class Canvas:
  def __init__(self,w,h):
    self.w=w
    self.h=h
    self.canvas = [[' ' for _ in range(w)] for _ in range(h)] #start with a blank canvas matrix
  
  def show(self): #to draw the updated canvas
    print('-' * (self.w + 2))
    for row in self.canvas:
        print('|' + ''.join(row) + '|')
    print('-' * (self.w + 2))

  #check input
  def check (self,x1,y1,x2,y2):
    if x1 <1 or x2 > len(self.canvas[0]) or y1<1 or y2 > len (self.canvas):
        print ("Error: Coordinates are out of canvas bounds.")
        return False
    if x1>x2 or y1>y2:
        print("Error: Invalid coordinates order.")
        return False
    return True
  
  def line(self, x1, y1, x2, y2, is_show):
    #check input first
    if not self.check(x1, y1, x2, y2):
        return
    #vertical line
    if x1==x2:
        for i in range (y1-1,y2):
            self.canvas[i][x1-1]='x'
    #horizontal line
    elif y1==y2:
        for j in range (x1-1,x2):
            self.canvas[y1-1][j]='x'
    else:
        print("Error: Only horizontal or vertical lines are supported.")
        return
    if is_show:
        self.show()

  
  def rectangle(self,x1,y1,x2,y2):
    #check input first
    if not self.check(x1, y1, x2, y2):
        return
     #draw up side
    self.line(x1,y1,x2,y1,False)
    #draw down side
    self.line(x1,y2,x2,y2,False)
    #draw left side
    self.line(x1,y1,x1,y2,False)
    #draw right side
    self.line(x2,y1,x2,y2,False)
    #update and show canvas
    self.show()

  def fill(self, x, y, c):
    x -= 1
    y -= 1
    #check input
    if not (0 <= x < self.w and 0 <= y < self.h):
        print("Error: Coordinates are out of canvas bounds.")
        return
    if self.canvas[y][x] == c: # no need to further check
        return
    start_point=self.canvas[y][x]

    def flood_fill(x, y):
        if x < 0 or x >= self.w or y < 0 or y >= self.h: #stop condition 1
            return
        if self.canvas[y][x] != start_point: # stop condition 2
            return
        self.canvas[y][x] = c #othervise, fill in with color c
        flood_fill(x + 1, y)
        flood_fill(x - 1, y)
        flood_fill(x, y + 1)
        flood_fill(x, y - 1)

    flood_fill(x, y)
    self.show()


#define main function
def main():
    canvas = None
    print("Please draw your canvas!")
    print("Available commands: \n1) draw a new canvas with width w and height h: C w h\n2) draw a line start from (x1,y1) to (x2,y2): L x1 y1 x2 y2\n3) draw a rectangle with upper left corner (x1,y1) and lower right corner (x2,y2): R x1 y1 x2 y2\n4) bucket fill using c from (x,y): B x y c\n5) quit: Q.")
    print("Remind: x1 <= x2 & y1 <= y2.\nAll the coordinates should be within the canvas width and height!")

    def create_canvas(params):
        nonlocal canvas
        if len(params) != 2:
            return "Invalid parameters, please use: C w h"
        w, h = map(int, params)
        if w <= 0 or h <= 0:
            return "Please enter positive integers for width and height."
        canvas = Canvas(w, h)
        canvas.show()
        return None

    def draw_line(params):
        if not canvas:
            return "Error: No canvas found. Create a canvas first."
        if len(params) != 4:
            return "Invalid parameters, please use: L x1 y1 x2 y2"
        x1, y1, x2, y2 = map(int, params)
        canvas.line(x1, y1, x2, y2,True)
        return None

    def draw_rectangle(params):
        if not canvas:
            return "Error: No canvas found. Create a canvas first."
        if len(params) != 4:
            return "Invalid parameters, please use: R x1 y1 x2 y2"
        x1, y1, x2, y2 = map(int, params)
        canvas.rectangle(x1, y1, x2, y2)
        return None

    def bucket_fill(params):
        if not canvas:
            return "Error: No canvas found. Create a canvas first."
        if len(params) != 3:
            return "Invalid parameters, please use: B x y c"
        x, y, c = int(params[0]), int(params[1]), params[2]
        canvas.fill(x, y, c)
        return None

    def quit_program(_):
        print("Exiting the drawing program.")
        exit()

    # construct a command dictionary
    commands = {
        'C': create_canvas,
        'L': draw_line,
        'R': draw_rectangle,
        'B': bucket_fill,
        'Q': quit_program,
    }

    while True:
        try:
            command = input("Enter command: ").split()
            if not command:
                print("You didn't enter anything. Please try again.")
                continue

            type = command[0].upper()
            params = command[1:]

            if type in commands:
                error = commands[type](params)
                if error:
                    print(error)
            else:
                print("Undefined command type. Please use C, L, R, B, or Q.")

        except ValueError:
            print("Invalid input. Please ensure coordinates and dimensions are integers.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
