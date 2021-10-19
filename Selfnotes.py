import speech_recognition as sr
import time
import csv

r = sr.Recognizer()
run = True

print("Starting")
print("Environment ready to capture") 

while run:

    with sr.Microphone() as source:
        print("done")
        lecture = r.listen(source)

        try : 

            text = (r.recognize_google(lecture))

            time_stamp = time.strftime("%D , %H:%M:%S")

            print(time_stamp + " : " + text)

            note = {
                "time stamp" : time_stamp,
                "notes" : text
            }

            with open('notes.csv','a',newline='') as file:
                header = ['Time Stamp', 'Notes']
                writer = csv.DictWriter(file, fieldnames = header)

                writer.writerow({
                    'Time Stamp' : time_stamp,
                    'Notes' : text
                })


        except KeyboardInterrupt:
            print("Error")

        except: 
            print("Stopping the process")
            run = False            
