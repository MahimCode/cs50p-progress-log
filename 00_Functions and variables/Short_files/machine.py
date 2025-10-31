# setting global varriable
emoticon = "v.v"


def main():
    global emoticon
    say("hello? andybody there?")
    emoticon = ":D"
    say("there you are")

def say(phrase):
    print(phrase,emoticon)

main()
