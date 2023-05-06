import time
from adafruit_servokit import ServoKit
import board
import busio

# constants
min_pw = 1000 # minimum pulsewidth [us]
max_pw = 2000 # maximum pulsewidth [us]
no_chnls = 16


def init_servokit():
	i2c_0 = busio.I2C(board.SCL7, board.SDA7)
	kit = ServoKit(channels=no_chnls, i2c=i2c_0)
	for i in range(no_chnls):
		kit.continuous_servo[i].set_pulse_width_range(min_pw, max_pw)
	return kit


def main():
	kit = init_servokit()
	sign = -1
	throttle_val = -1
	while True:
		print("Throttle value: ", throttle_val)
		kit.continuous_servo[0].throttle = throttle_val
		throttle_val += sign*0.002
		if abs(throttle_val) >= 1:
			sign *= -1
			throttle_val = -sign
			print("Changed sign to: ", sign)
		time.sleep(0.01)


if __name__ == "__main__":
	main()
