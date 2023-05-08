from modules import *
from constants import *

def init_pwmdriver():
	i2c_0 = busio.I2C(board.SCL7, board.SDA7)
	kit = ServoKit(channels=no_chnls, i2c=i2c_0)
	for i in range(no_chnls):
		kit.continuous_servo[i].set_pulse_width_range(min_pw, max_pw)
	return kit

def set_thrusters(thrust_values):
    for t in range(len(thrust_values)):
        kit.continuous_servo[t].throttle = thrust_values[t]

def init_imu()
    mpu = MPU6500(i2c, busnum=1,  address=0x68,
        gyro_offset=(3.732, -1.407, -3.589))
    ak = AK8963(i2c, 
        offset=(12.210, 12.825, -23.183),
        scale=(0.966, 1.132, 0.924))
    return MPU9250(mpu, ak)

def main()
    pwm_driver = init_pwmdriver()

if __name__ == "__main__":
    main()