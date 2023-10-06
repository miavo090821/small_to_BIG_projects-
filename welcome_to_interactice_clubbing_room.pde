Line[] lines = new Line[10];
int x, y, size;
boolean isOn = false;
boolean isIn = false;
int frameCountStart = 0;
int frameDuration = 5; // 1 second at 5 frames per second
float xPos = width; // Declare global xPos

void setup() {
  size(400, 400);
  x = width / 4;
  y = height / 4;
  size = width / 15;
  for (int i = 0; i < lines.length; i++) {
    lines[i] = new Line();
  }

  xPos = width;
}

void draw() {
  rect(x, y, size, size);
  fill(64, 200);

  if (isOn) {
    rect(x + size * 0.25, y + size * 0.25, size * 0.5, size * 0.5);

    int currentFrame = frameCount - frameCountStart;
    if (currentFrame >= frameDuration) {
      frameCountStart = frameCount;
      for (Line line : lines) {
        line.changePositionAndColor();
      }
    }
    background(255);
    strokeWeight(0.5);

    for (Line line : lines) {
      line.update();
      line.display();
    }
  } else {
    background(255);

    // Display scrolling message
    textSize(60);
    fill(164, 205, 78);
    String message = "HELLO, WELCOME TO INTERACTIVE CLUBBING ROOM.";
    text(message, xPos, height / 2);

    // Scroll the message continuously
    xPos -= 1;
    if (xPos < -textWidth(message)) {
      xPos = width;
    }

    textSize(30);
    strokeWeight(2);
    fill(200, 150, 89);
    String message1 = "PLEASE TURN ME OFF BEFORE YOU LEAVE.";
    text(message1, xPos, (height / 2) + 100);

    // Scroll the second message continuously
    xPos -= 1.5;
    if (xPos < -textWidth(message1)) {
      xPos = width;
    }
  }

  rectMode(CENTER);
  rect(x, y, size, size);

  fill(64, 200);
  text(isOn ? "On" : "Off", x + size * 1.5, 15 + height / 4);
}

void mouseMoved() {
  isIn = (mouseX > x - size / 2) && (mouseY > y - size / 2) && (mouseX < x + size / 2) && (mouseY < y + size / 2);
}

void mouseClicked() {
  if (isIn) {
    isOn = !isOn;
  }
}

class Line {
  float x1, y1, x2, y2;
  color col;

  Line() {
    changePositionAndColor();
  }

  void display() {
    stroke(col);
    line(x1, y1, x2, y2);
  }

  void update() {
    if (x1 < -500 || x1 > width + 500 || y1 < -500 || y1 > height + 500) {
      x1 = random(width);
      y1 = 0;
    }
    if (x2 < -500 || x2 > width + 500 || y2 < -500 || y2 > height + 500) {
      x2 = random(-500, width + 500); // Allow x2 to be negative
      y2 = random(height);
    }
  }

  void changePositionAndColor() {
    x1 = random(width);
    y1 = 400;
    x2 = random(-500, width + 500); // Allow x2 to be negative
    y2 = -250;
    col = color(random(255), random(255), random(255));
  }
}
