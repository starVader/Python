# Enter your code here. Read input from STDIN. Print output to STDOUT
from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for i in attrs:
                print "->",i[0], ">",i[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for i in attrs:
                print "->",i[0], ">",i[1]


parser = MyHTMLParser() 
parser.feed('<!-- a comment -->')
    
