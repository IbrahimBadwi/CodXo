import time
import datetime
import os
import threading

def play_sound(sound_file):
    
    if os.name == 'nt':  
        os.system(f'start {sound_file}')
    elif os.name == 'posix':  
        os.system(f'afplay {sound_file}' if os.uname().sysname == 'Darwin' else f'aplay {sound_file}')

def set_alarm(alarm_time, sound_file):
    print(f"Alarm set for {alarm_time}.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        remaining_time = (datetime.datetime.strptime(alarm_time, "%H:%M:%S") - datetime.datetime.strptime(current_time, "%H:%M:%S")).seconds
        if current_time == alarm_time:
            print("⏰ Time to wake up!")
            play_sound(sound_file)
            break
        elif remaining_time < 3600: 
            print(f"Remaining time: {remaining_time // 60} minutes and {remaining_time % 60} seconds", end='\r')
        time.sleep(1)

def main():
    alarms = []

    while True:
        alarm_time = input("Enter alarm time in HH:MM:SS format (or 'done' to finish): ")
        if alarm_time.lower() == 'done':
            break
        sound_choice = input("Choose an alarm sound (1: default, 2: bird, 3: beep): ")
        sound_file = {
            '1': 'default_alarm.mp3',
            '2': 'bird_chirp.mp3',
            '3': 'beep.mp3'
        }.get(sound_choice, 'default_alarm.mp3')

        alarms.append((alarm_time, sound_file))

    for alarm in alarms:
        alarm_thread = threading.Thread(target=set_alarm, args=alarm)
        alarm_thread.start()

if __name__ == "__main__":
    main()