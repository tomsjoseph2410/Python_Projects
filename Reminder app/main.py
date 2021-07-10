# Python-Reminder-App
# Python-Reminder-Application
import winsound
from win10toast import ToastNotifier


def timer (reminder,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=10)
    notificator.show_toast(f"Reminder",reminder,duration=10)

    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

if __name__=="__main__":
    reminder=input("What would you remindes of: ")
    print("hi")
    seconds=int(input("Enter seconds: "))
    timer(reminder,seconds)