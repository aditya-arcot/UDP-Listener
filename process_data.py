'''Take actions based on content of message'''

import subprocess

def main(data):
    if data == 'wake desktop':
        process = subprocess.Popen(['wakeonlan', 'A4:BB:6D:54:ED:8C'], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate() # wait till process complete
        
        print('ran command')
        print(f'stdout: {stdout.decode().strip()}')
        print(f'stderr:{stderr.decode().strip()}')
        print()


    else:
        print('no matching pipeline\n')
