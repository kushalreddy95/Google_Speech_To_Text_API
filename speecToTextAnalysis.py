import speech_recognition as sr
import os
from textblob import TextBlob

r = sr.Recognizer()

os.chdir("AudioClips")
text = ""
try:
    for files in os.walk("./"):
        for file in files:
            if file:
                for item in file:
                    try:
                        if str(item).split('.')[1] == "wav":
                            audio = item
                            with sr.AudioFile(audio) as source:
                                audio = r.record(source)
                            try:
                                print("Transcribing {}".format(str(item)))
                                # text += r.recognize_google(audio)
                                # print(text)

                            except Exception as e:
                                print("Could Not Transcribe Audio {}".format(e))
                    except Exception as e:
                        print("file could not be Split: {}: {}".format(str(item, e)))
except Exception as e:
    print("main: {}\n".format(e))
text = '''
the Birch canoe slid on the smooth planks glue the seat
to the dark blue background it is easy to tell the depth of a well these days
a chicken leg is a verb dish rice is often served in round Bowls the juice of lemons makes 
fine punch the box was the one beside the pump truck the Hogs are such hot corn and garbage 4 hours of 
study workswhat if somebody decides to break it be careful
that you keep adequate coverage but look for places to save money baby it's
taking longer to get things squared away than the bankers expected during the Y for one's company may win
her tax faded retirement income to boost is helpful but receiving Rags are hers Lee tossed on the two naked bones
'''

text += "I hate this movie It is bad very bad"
# print(text)

text = '.'.join(text[i:i + 62] for i in range(0, len(text), 62))

para = text.split('.')
total_polarity = 0
for item in para:
    print(item)

    blob1 = TextBlob(item)
    total_polarity += blob1.sentiment.polarity
    print(total_polarity)
    print("\n")
print(total_polarity)
