import board
import busio
from robohat_mpu9250.mpu9250 import MPU9250
from robohat_mpu9250.mpu6500 import MPU6500
from robohat_mpu9250.ak8963 import AK8963

from time import sleep

i2c = busio.I2C(board.SCL2, board.SDA2)

mpu = MPU6500(i2c, busnum=1,  address=0x68,
	gyro_offset=(3.732, -1.407, -3.589))
ak = AK8963(i2c, 
	offset=(12.210, 12.825, -23.183),
	scale=(0.966, 1.132, 0.924))

sensor = MPU9250(mpu, ak)

print("Reading in data from IMU.")
print("MPU9250 id: " + hex(sensor.read_whoami()))

while True:
    print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.read_acceleration()))
    print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.read_magnetic()))
    print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.read_gyro()))
    print('Temperature: {0:0.3f}C'.format(sensor.read_temperature()))
    sleep(2)
