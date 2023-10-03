Particle particle;

void setup(){
  size(400,300);
  particle = new Particle();
  
  background(247,239,218);
}
void draw(){
  line(particle.prevX, particle.prevY, particle.x, particle.y);// line with 2
  // co=ordinates of previous and current 
  particle.move(); // particle will move 
}
 
class Particle
{
  float x, y;           // Position of particle
  float prevX, prevY;   // Previous position before it moved.
  float direction;      // Direction in which the particle moves (in radians).
 
  // Creates a new particle with a random location and direction of movement.
  Particle()
  {
    x = random(0, width); // the value of x is generated randomly from 0-> width values
    y = random(0, height);// same like x value
    prevX = x;
    prevY = y;
    direction = random(0, radians(360));
  }
 
  // Moves the particle after randomly modifying the direction of movement.
  void move()
  {
    if ((x < 0) || (y < 0) || (x > width) || (y > height))
    {
      // Particle has moved off screen so reset it in new random location.
      x = random(0, width);
      y = random(0, height);
      prevX = x;
      prevY = y;
      direction = random(0, radians(360));
    }
    else
    {
      // Store previous position before we move particle.
      prevX = x;
      prevY = y;
 
      // Use noise() to change direction.
      float noiseScale = 0.05;
      direction = noise(noiseScale*x, noiseScale*y)*radians(360);
 
      // Move to new location based on new direction.
      x = x + cos(direction);
      y = y + sin(direction);
    }
  }
}
