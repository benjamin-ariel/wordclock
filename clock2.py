import board
from time import localtime
from adafruit_ht16k33.matrix import Matrix8x8
from time import sleep

i2c = board.I2C()
matrix = Matrix8x8(i2c)
hour = localtime().tm_hour
minutes = localtime().tm_min

print(hour)
print(minutes)

def clear():
 for i in range(8):
  for j in range(8):
   matrix[i,j] = 0
   

while True:
  clear()
  sleep(30)
  
  hour = localtime().tm_hour
  minutes = localtime().tm_min
  
  if hour == 1 or hour == 13:
      clear()

      matrix[0, 1] = 1
      matrix[0, 4] = 1
      matrix[0, 7] = 1

  if hour == 2 or hour == 14:
      clear()
      matrix[0, 1] = 1
      matrix[1, 1] = 1
      matrix[1, 0] = 1

  if hour == 3 or hour == 15:
      clear()
      matrix[2, 3] = 1
      matrix[2, 4] = 1
      matrix[2, 5] = 1
      matrix[2, 6] = 1
      matrix[2, 7] = 1

  if hour == 4 or hour == 16:
      clear()
      matrix[0, 0] = 1
      matrix[0, 1] = 1
      matrix[0, 2] = 1
      matrix[0, 3] = 1

  if hour == 5 or hour == 17:
      clear()
      matrix[3, 0] = 1
      matrix[3, 1] = 1
      matrix[3, 2] = 1
      matrix[3, 3] = 1

  if hour == 6 or hour == 18:
      clear()
      matrix[2, 0] = 1
      matrix[2, 1] = 1
      matrix[2, 2] = 1

  if hour == 7 or hour == 19:
      clear()
      matrix[2, 0] = 1
      matrix[1, 4] = 1
      matrix[1, 5] = 1
      matrix[1, 6] = 1
      matrix[1, 7] = 1

  if hour == 8 or hour == 20:
      clear()
      matrix[3, 3] = 1
      matrix[3, 4] = 1
      matrix[3, 5] = 1
      matrix[3, 6] = 1
      matrix[3, 7] = 1

  if hour == 9 or hour == 21:
      clear()
      matrix[4, 0] = 1
      matrix[5, 0] = 1
      matrix[6, 0] = 1
      matrix[7, 0] = 1

  if hour == 10 or hour == 22:
      clear()
      matrix[2,3] = 1
      matrix[1,4] = 1
      matrix[0,4] = 1

  if hour == 11 or hour == 23:
      clear()
      matrix[1,2] = 1
      matrix[1,3] = 1
      matrix[1,4] = 1
      matrix[1,5] = 1
      matrix[1,6] = 1
      matrix[1,7] = 1

  if hour == 12 or hour == 24:
      clear()
      matrix[1, 0] = 1
      matrix[1, 1] = 1
      matrix[1,2] = 1
      matrix[1,3] = 1
      matrix[1,4] = 1
      matrix[1,5] = 1
      matrix[1,6] = 1

  if minutes >=23 and minutes <=27:
  #twenty five past
      clear()
      matrix[7, 2] = 1
      matrix[7, 1] = 1
      matrix[7, 3] = 1
      matrix[7, 4] = 1
      matrix[7, 5] = 1
      matrix[7, 6] = 1
      matrix[4, 3] = 1
      matrix[4, 2] = 1
      matrix[4,1] = 1
      matrix[4,4] = 1
      matrix[5,3] = 1
      matrix[5,2] = 1
      matrix[5,1] = 1
      matrix[5,0] = 1

  if minutes >= 18 and minutes <=22:
      clear()
      matrix[7,2] = 1
      matrix[7, 3] = 1
      matrix[7,4] = 1
      matrix[7,1] = 1
      matrix[7,5] = 1
      matrix[7,6] = 1
      matrix[4,3] = 1
      matrix[4,4] = 1
      matrix[4,2] = 1
      matrix[4,1] = 1

  if minutes >= 13 and minutes <=17:
      clear()
      matrix[4,1] = 1
      matrix[4, 2] = 1
      matrix[4,3] = 1
      matrix[4,4] = 1
      matrix[6,0] = 1
      matrix[6,1] = 1
      matrix[6,2] = 1
      matrix[6,3] = 1
      matrix[6, 4] = 1
      matrix[6, 5] = 1
      matrix[6,6] = 1

  if minutes >= 8 and minutes <=12:
      clear()
      matrix[7,1] = 1
      matrix[7, 3] = 1
      matrix[7,4] = 1
      matrix[4,1] = 1
      matrix[4,2] = 1
      matrix[4,3] = 1
      matrix[4,4] = 1
      matrix[4,4] = 1

  if minutes >= 2 and minutes <= 7:
      clear()
      matrix[5,2] = 1
      matrix[5, 3] = 1
      matrix[5,0] = 1
      matrix[5,1] = 1
      matrix[4,1] = 1
      matrix[4,2] = 1
      matrix[4,3] = 1
      matrix[4,4] = 1

  if minutes >= 33 and minutes <=37:
      clear()
      matrix[7,2] = 1
      matrix[7, 3] = 1
      matrix[7,4] = 1
      matrix[7,1] = 1
      matrix[7,5] = 1
      matrix[7,6] = 1
      matrix[5,0] = 1
      matrix[5,1] = 1
      matrix[5,2] = 1
      matrix[5,3] = 1
      matrix[4,5] = 1
      matrix[4,4] = 1

  if minutes >= 28 and minutes <=32:
      clear()
      matrix[5,4] = 1
      matrix[5, 5] = 1
      matrix[5,6] = 1
      matrix[5,7] = 1
      matrix[4,3] = 1
      matrix[4,2] = 1
      matrix[4,1] = 1
      matrix[4,4] = 1

  if minutes >= 38 and minutes <=42:
      clear()
      matrix[7,2] = 1
      matrix[7, 3] = 1
      matrix[7,4] = 1
      matrix[7,1] = 1
      matrix[7,5] = 1
      matrix[7,6] = 1
      matrix[4,5] = 1
      matrix[4,4] = 1

  if minutes >= 43 and minutes <=47:
      clear()
      matrix[6,0] = 1
      matrix[6, 1] = 1
      matrix[6,2] = 1
      matrix[6,3] = 1
      matrix[6,4] = 1
      matrix[6,5] = 1
      matrix[6,6] = 1
      matrix[4,5] = 1
      matrix[4,4] = 1

  if minutes >= 48 and minutes <=52:
      clear()
      matrix[7,1] = 1
      matrix[7, 3] = 1
      matrix[7,4] = 1
      matrix[4,5] = 1
      matrix[4,4] = 1

  if minutes >= 53 and minutes <=59:
      clear()
      matrix[5,2] = 1
      matrix[5, 3] = 1
      matrix[5,0] = 1
      matrix[5,1] = 1
      matrix[4,5] = 1
      matrix[4,4] = 1
