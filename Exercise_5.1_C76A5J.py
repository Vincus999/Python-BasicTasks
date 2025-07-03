import time


def convert_time():
    current_time = time.time()

    seconds_since_epoch = int(current_time)

    minutes_since_epoch = seconds_since_epoch // 60

    hours_since_epoch = seconds_since_epoch // 3600

    days_since_epoch = seconds_since_epoch // 86400

    seconds_today = seconds_since_epoch % 86400
    hours_today = seconds_today // 3600
    minutes_today = (seconds_today % 3600) // 60
    seconds_today = seconds_today % 60

    print(f"Seconds since the epoch: {seconds_since_epoch}")
    print(f"Minutes since the epoch: {minutes_since_epoch}")
    print(f"Hours since the epoch: {hours_since_epoch}")
    print(f"Days since the epoch: {days_since_epoch}")
    print(f"Current time of day: {hours_today:02}:{minutes_today:02}:{seconds_today:02}")


convert_time()
