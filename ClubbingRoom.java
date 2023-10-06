import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.Line2D;
import javax.swing.Timer;
import java.util.Random;

public class ClubbingRoom extends JPanel {
    private int x, y, size;
    private boolean isOn = false;
    private float xPos;
    private Line[] lines;
    private Timer timer;
    private JButton clickButton;

    public ClubbingRoom() {
        // Constructor for ClubbingRoom class
        setPreferredSize(new Dimension(400, 400));
        x = getWidth() / 4;
        y = getHeight() / 4;
        size = getWidth() / 15;
        lines = new Line[10];
        for (int i = 0; i < lines.length; i++) {
            lines[i] = new Line();
        }
        xPos = getWidth();
        // Timer for animation when "isOn" is true


        timer = new Timer(1000 / 60, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (isOn) {
                    for (Line line : lines) {
                        line.changePositionAndColor(getWidth(), getHeight());
                    }
                    repaint();
                }
            }
        });
        timer.start();
        // Timer for scrolling text when "isOn" is false


        Timer scrollTimer = new Timer(16, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!isOn) {
                    xPos -= 1;
                    if (xPos < -getTextWidth("HELLO, WELCOME TO INTERACTIVE CLUBBING ROOM.")) {
                        xPos = getWidth();
                    }
                    repaint();
                }
            }
        });
        scrollTimer.start();

        // Mouse click event listener

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent evt) {
                mouseClick(evt.getX(), evt.getY());
            }
        });

        // Button creation and event listener
        clickButton = new JButton("CLICK ME");
        clickButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                isOn = !isOn;
                repaint();
            }
        });

        // Setting layout and adding the button to the panel
        setLayout(new BorderLayout());
        add(clickButton, BorderLayout.SOUTH);
    }

    @Override
    protected void paintComponent(Graphics g) {
        // Paints the component
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        if (isOn) {
            // Drawing components when "isOn" is true
            g2d.setColor(new Color(64, 200, 0));
            g2d.fillRect(x, y, size, size);
            g2d.setColor(new Color(255, 255, 255));
            g2d.fillRect(x + size / 4, y + size / 4, size / 2, size / 2);

            for (Line line : lines) {
                line.update(getWidth(), getHeight());
                line.display(g2d);
            }
        } else {
            // Drawing components when "isOn" is false
            g2d.setColor(new Color(255, 255, 255));
            g2d.fillRect(0, 0, getWidth(), getHeight());

            g2d.setFont(new Font("Arial", Font.PLAIN, 60));
            g2d.setColor(new Color(164, 205, 78));
            String message = "HELLO, WELCOME TO INTERACTIVE CLUBBING ROOM.";
            g2d.drawString(message, (int) xPos, getHeight() / 2);

            g2d.setFont(new Font("Arial", Font.PLAIN, 30));
            g2d.setColor(new Color(200, 150, 89));
            String message1 = "PLEASE TURN ME OFF BEFORE YOU LEAVE.";
            g2d.drawString(message1, (int) xPos, (getHeight() / 2) + 100);
        }

        g2d.setColor(new Color(64, 200, 0));
        g2d.fillRect(x, y, size, size);
        g2d.setColor(new Color(255, 255, 255));
        g2d.fillRect(x + size / 4, y + size / 4, size / 2, size / 2);
        g2d.setColor(new Color(64, 200, 0));
        
    }
    // Helper method to get text width
    private int getTextWidth(String text) {
        FontMetrics fm = getFontMetrics(getFont());
        return fm.stringWidth(text);
    }
    // Handle mouse click event
    private void mouseClick(int mouseX, int mouseY) {
        if (isIn(mouseX, mouseY)) {
            isOn = !isOn;
            repaint();
        }
    }
    // Check if mouse click is within a certain region
    private boolean isIn(int mouseX, int mouseY) {
        return (mouseX > x - size / 2) && (mouseY > y - size / 2) &&
               (mouseX < x + size / 2) && (mouseY < y + size / 2);
    }

    public static void main(String[] args) {
        //Main method for running the program
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Clubbing Room");
            ClubbingRoom clubbingRoom = new ClubbingRoom();
            frame.add(clubbingRoom);
            frame.pack();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}
// Line class for drawing animated lines
class Line {
    float x1, y1, x2, y2;
    Color col;

    Line() {
        changePositionAndColor(0, 0);
    }

    void display(Graphics2D g2d) {
        g2d.setColor(col);
        g2d.draw(new Line2D.Float(x1, y1, x2, y2));
    }

    void update(int screenWidth, int screenHeight) {
        if (x1 < -500 || x1 > screenWidth + 500 || y1 < -500 || y1 > screenHeight + 500) {
            x1 = new Random().nextFloat() * screenWidth;
            y1 = 0;
        }
        if (x2 < -500 || x2 > screenWidth + 500 || y2 < -500 || y2 > screenHeight + 500) {
            x2 = new Random().nextFloat() * (screenWidth + 1000) - 500;
            y2 = new Random().nextFloat() * screenHeight;
        }
    }

    void changePositionAndColor(int screenWidth, int screenHeight) {
        x1 = new Random().nextFloat() * screenWidth;
        y1 = 400;
        x2 = new Random().nextFloat() * (screenWidth + 1000) - 500;
        y2 = -250;
        col = new Color(new Random().nextInt(256), new Random().nextInt(256), new Random().nextInt(256));
    }
}
