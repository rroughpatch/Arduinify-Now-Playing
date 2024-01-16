#include <LiquidCrystal.h>

LiquidCrystal lcd(13, 8, 9, 10, 11, 12);

struct SongInfo {
  String title;
  String artist;
};

String receivedData = "";

SongInfo getSongInfo(const String& data) {
  int tildePos = data.indexOf('~');
  int plusPos = data.indexOf('+');
  if (tildePos != -1 && plusPos != -1) {
    return {data.substring(0, tildePos), data.substring(tildePos + 1, plusPos)};
  }
  return {"Unknown", "Unknown"};
}

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void displayScrollingText(String text, int row, int& scrollPos, bool& scrollDirection) {
  if (text.length() <= 16) {
    lcd.setCursor(0, row);
    lcd.print(text);
    for (int i = text.length(); i < 16; i++) {
      lcd.print(" "); // Clear the rest of the line
    }
  } else {
    int endPos = min(scrollPos + 16, text.length());
    lcd.setCursor(0, row);
    for (int i = scrollPos; i < endPos; i++) {
      lcd.print(text[i]);
    }
    for (int i = endPos; i < scrollPos + 16; i++) {
      lcd.print(" "); // Clear the rest of the line
    }

    unsigned long currentMillis = millis();
    static unsigned long previousMillis = 0;
    if (currentMillis - previousMillis >= 500) { // Scroll every 500 ms
      previousMillis = currentMillis;
      scrollDirection ? scrollPos++ : scrollPos--;
      if (scrollPos == text.length() - 16 || scrollPos == 0) {
        scrollDirection = !scrollDirection;
      }
    }
  }
}

void loop() {
  while (Serial.available() > 0) {
    char receivedChar = Serial.read();
    receivedData += receivedChar;
  }

  static int titleScrollPos = 0, artistScrollPos = 0;
  static bool titleScrollDirection = true, artistScrollDirection = true;
  static SongInfo currentSong;

  if (receivedData.indexOf('+') != -1) {
    currentSong = getSongInfo(receivedData);
    titleScrollPos = artistScrollPos = 0;
    titleScrollDirection = artistScrollDirection = true;
    receivedData = "";
    lcd.clear();
  }

  displayScrollingText(currentSong.title, 0, titleScrollPos, titleScrollDirection);
  displayScrollingText(currentSong.artist, 1, artistScrollPos, artistScrollDirection);
}
