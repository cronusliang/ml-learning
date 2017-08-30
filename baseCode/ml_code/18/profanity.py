import urllib


def read_txt():
   quests =   open("C:\Users\Administrator\Desktop\movie_quotes\movie_quotes.txt")
   content =   quests.read()
   print content
   quests.close()
   check(content)

def check(check_text):
 connection =  urllib.urlopen("http://www.wdylike.appspot.com/?q="+check_text)
 value =  connection.read()
 print value
 connection.close()
read_txt()