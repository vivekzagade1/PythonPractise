import datetime
import schedule
import time


def schedule_minute():
    print("Schedule for a minute")
    print(f"time now {datetime.datetime.now()}")


def main():
    print("Automation in Python")

    schedule.every(1).minutes.do(schedule_minute)
    schedule.every(1).hour.do(schedule_minute)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
