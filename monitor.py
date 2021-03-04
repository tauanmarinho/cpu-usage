import psutil
import time
import matplotlib.pyplot as plt
import argparse

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--width", "-w", help="set output width")
parser.add_argument("--stamp", "-s", help="set output width")

# Read arguments from the command line
args = parser.parse_args()

# Check for --width
if args.width:
    print("Set output width to %s" % args.width)
# Check for --stamp
if args.stamp:
    print("Set output stamp to %s" % args.stamp)

i = 0
cpu = []
mem = []
while i < int(args.width):
  mem.append(psutil.virtual_memory().percent)
  cpu.append(psutil.cpu_percent())
  time.sleep(int(args.stamp))
  i += 1

print(cpu)
print(mem)

plt.figure(figsize=(10, 4))

plt.subplot(231)
plt.plot(cpu, 'bo', cpu, 'k')
plt.ylabel('CPU')
plt.xlabel('Time')

plt.subplot(233)
plt.plot(mem, 'bo', mem, 'k')
plt.ylabel('Memory')
plt.xlabel('Time')

plt.suptitle('Status Monitor')
plt.show()