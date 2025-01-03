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
        self.current_color_name = None
        self.is_color_name = False
        self.is_hex_value = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'class' in attrs and ('tw' in attrs['class'] or 'tb' in attrs['class']):
            self.is_color_name = True
        elif tag == 'td' and not self.is_color_name:
            self.is_hex_value = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.is_color_name = False
        elif tag == 'td':
            self.is_hex_value = False

    def handle_data(self, data):
        if self.is_color_name:
            self.current_color_name = data.strip()
        elif self.is_hex_value and self.current_color_name:
            self.colours[self.current_color_name] = data.strip()
            self.current_color_name = None

if __name__ == "__main__":
    parser = ColourHTMLParser()

    # Fetch and parse the HTML content
    with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
        parser.feed(response.read().decode('utf-8'))

    # Print the results
    for name, hex_value in parser.colours.items():
        print(f"{name} {hex_value}")

    print(f"\nTotal colors #: {len(parser.colours)}")
