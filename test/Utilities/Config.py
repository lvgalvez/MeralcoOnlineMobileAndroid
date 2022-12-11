from pathlib import Path

import os

root_dir = Path(__file__).parent

# Appium Remote
host = "http://localhost:4723/wd/hub"

# meralco_online
meralco_online = f"{root_dir}/Move-75.apk"

# Screenshot location
screenshot_folder = f"{root_dir.parent}/Screenshots/"

# Desired Capabilities
desired_cap = {
    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
    "app": meralco_online,
    "noReset": "false",
    "autoGrantPermissions": "true"
}


def create_folder(ss_folder, folder_name):
    folder_loc = os.path.join(ss_folder, folder_name)
    if not os.path.exists(folder_loc):
        os.mkdir(folder_loc)

