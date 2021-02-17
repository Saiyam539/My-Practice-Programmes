import time

from plyer import notification


if __name__ == "__main__":
    # while True:
    notification.notify(
        title = 'Please drink water!!',
        message = 'Drinking water is good for your health Saiyam sir.\nThankyou',
        # app_icon = 'D:\water drinking\icon.ico.ico',
        timeout = 5
    )
time.sleep(6)
