import time

light = "red"

while True:
    if light == "red":
        print("🔴 Red Light - STOP")
        time.sleep(3)
        light = "green"

    elif light == "green":
        print("🟢 Green Light - GO")
        time.sleep(3)
        light = "yellow"

    elif light == "yellow":
        print("🟡 Yellow Light - READY")
        time.sleep(2)
        light = "red"