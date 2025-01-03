# Topic Challenge - Module 7B - Web Scraping
# Student: Andres Roman
# Studen ID: 0374136
# Date: October 20, 2024

from html.parser import HTMLParser
import urllib.request

class ColourHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.colours = {}
        self.in_color_name = False
        self.in_hex_value = False
        self.current_color_name = None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'class' and ('tw' in attr[1] or 'tb' in attr[1]):
                    self.in_color_name = True
        elif tag == 'td' and not self.in_color_name:
            self.in_hex_value = True

    def handle_endtag(self, tag):
        if tag == 'a' and self.in_color_name:
            self.in_color_name = False
        elif tag == 'td' and self.in_hex_value:
            self.in_hex_value = False

    def handle_data(self, data):
        if self.in_color_name:
            self.current_color_name = data.strip()
        elif self.in_hex_value and self.current_color_name:
            hex_value = data.strip()
            self.colours[self.current_color_name] = hex_value
            self.current_color_name = None

parser = ColourHTMLParser()

with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = response.read().decode('utf-8')

parser.feed(html)

for name, hex_value in parser.colours.items():
    print(f"{name} {hex_value}")

# Print the total count of colors
print(f"\nTotal colors #: {len(parser.colours)}")
