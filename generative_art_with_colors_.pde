Particle[] particles;    // Declare array of particles.
 
void setup()
{
  size(400, 300);
 
  // Initialise 500 particle objects.
  particles = new Particle[500];
  for (int i=0; i<particles.length; i++)
  {
    particles[i] = new Particle();
  }
 
  // Use Hue Saturation Brightness colour mode
  colorMode(HSB,1,1,1);
  background(0.12, 0.11, 0.95);
}
 
void draw()
{
  // Draw and move each of the particles.
  strokeWeight(0.2);
  for (Particle p : particles)
  {
    // Set line colour using 2d Perlin noise.
    stroke(noise(0.04*p.x,0.04*p.y)*1.4,0.7,0.6);
    line(p.prevX, p.prevY, p.x, p.y);
    p.move();
  }
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
 
      // now we have it moving 
      //Use noise() to change direction.
      float noiseScale = 0.05;
      direction = noise(noiseScale*x, noiseScale*y)*radians(360);
 
      // Move to new location based on new direction.
      x = x + cos(direction);
      y = y + sin(direction);
    }
  }
}
