from pyshorteners import Shortener
import urllib.request

s = Shortener()

def shorten_url(link):
    shortened_link = s.tinyurl.short(link)
    print("The shortened link is: " + shortened_link)


def expand_url(link):
    expanded_link = s.tinyurl.expand(link)
    print("The original link is: " + expanded_link)


link = input("Give your link: ")
response = urllib.request.urlopen(link)
final_url = response.geturl()
if final_url != link:
    expand_url(link)
else:
    shorten_url(link)
