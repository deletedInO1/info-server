import threading
import subprocess
import time
import config

cmd = rf"{config.LLAMA_CPP_POS} -ins -t 3 -ngl 1 -m {config.MODEL_POS} -c 2048 --temp 0.7 --repeat_penalty 1.1 -s 42 -n -1" \
#       r"--gpu-layers 40"
#cmd = "py popentest_cmd.py"
#cmd = config.LLAMA_CPP_POS
process: subprocess.Popen = None
clock = 0

def start_program():
    global process
    process = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

def input_message(inp: str)->str:
    process.stdin.write(inp + "\n")
    process.stdin.flush()
    return _readstream()

def __readstream(_queue: list):
    global clock
    print("listening...")
    bigger_than_count = 0
    while True:
        character = process.stdout.read(1)
        clock = 0
        if not character:
            break
        if character == ">":
            bigger_than_count += 1
            if bigger_than_count >= 2:
                break
        _queue.append(character)


def _readstream():
    global clock
    _queue = []
    thread = threading.Thread(target=__readstream, args=(_queue, ))
    thread.start()
    while clock < 500 and thread.is_alive():
        clock += 1
        time.sleep(10/1000)
        # if clock % 100 == 0:
        #     print(clock)
    print("kill thread")
    if thread.is_alive():
        thread.join(0.1)
    s = ""
    for a in _queue:
        s += a
    return s

if __name__ == "__main__":
    start_program()
    print("output: ", input_message("hi, how are you"))
    print("output: ", input_message("hey, how are you"))
    exit(0)