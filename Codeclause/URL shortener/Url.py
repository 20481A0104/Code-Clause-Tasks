import pyshorteners

link = input("Enter a Link : ")

shortener = pyshorteners.Shortener()

x=shortener.tinyurl.short(link)
print("Short Link : ",x)