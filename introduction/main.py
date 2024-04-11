import datetime
import math

def compute_proccess(endIn=50_000_000, start=1):
  position = start
  some_feature = 1000 * 1000

  while(position < endIn):
    position += 1
    math.sqrt((position - some_feature) * (position - some_feature))

def main():
  start = datetime.datetime.now()

  compute_proccess(endIn=50_000_000)
  
  proccess_time = datetime.datetime.now() - start
  print(f"Script end in {proccess_time.total_seconds():.2f} seconds.")

if __name__ == '__main__':
  main()

# Script end in 12.84 seconds.