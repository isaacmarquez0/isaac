from gpiozero import LED, PWMLED, Servo
import time

# LEDs
red_led = LED(3)
yellow_led = LED(4)
green_led = LED(17)

# RGB (Optional Test)
r_red_pwm_pin = PWMLED(14)
r_green_pwm_pin = PWMLED(15)
r_blue_pwm_pin = PWMLED(18)

l_red_pwm_pin = PWMLED(27)
l_green_pwm_pin = PWMLED(22)
l_blue_pwm_pin = PWMLED(23)  # Keep this for LED

# Servo moved to GPIO 19 to avoid conflict
servo = Servo(19)

try:
    print("Turning on red LED")
    red_led.on()
    yellow_led.off()
    green_led.off()

    print("Setting RGB Left Eye")
    l_red_pwm_pin.value = 1
    l_green_pwm_pin.value = 0.5
    l_blue_pwm_pin.value = 0.2

    print("Starting Servo Sweep")
    for i in range(3):  # Sweep servo 3 times
        for val in range(0, 21):
            pos = (val - 10) / 10
            servo.value = pos
            print(f"Servo Pos: {pos}")
            time.sleep(0.2)
        for val in range(20, -1, -1):
            pos = (val - 10) / 10
            servo.value = pos
            print(f"Servo Pos: {pos}")
            time.sleep(0.2)

    print("Test Complete")

finally:
    print("Cleaning up")
    red_led.off()
    yellow_led.off()
    green_led.off()
    l_red_pwm_pin.off()
    l_green_pwm_pin.off()
    l_blue_pwm_pin.off()
    servo.value = None  # Release the servo
