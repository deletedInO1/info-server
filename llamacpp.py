
import os
import socket

import config
import subprocess
import time
#-m {config.USB_STICK}:\programs\gpt4all\mymodels\llama-2-7b-chat.ggmlv3.q2_K.bin

#print("D:\\programs\\lamacpp\\llama.cpp\\build\\bin\\Release\\main.exe  -m D:\programs\gpt4all\mymodels\llama-2-7b-chat.ggmlv3.q2_K.bin")
def command(main, model, threads = 3, context_size=2048, temp=0.7): #threads: 8 in video
    return f"{main} -ins -t {str(threads)} -ngl 1 -m {model} -c {str(context_size)} --temp {str(temp)} \
        --repeat_penalty 1.1 -s 42 -n -1"

def run(prompt): # doesn't use prompt yet
    with open("prompt_base.txt") as f:
        with open("prompts.txt", "w") as f2:
            f2.write(f.read().replace("%1", prompt))
    command = f"{config.LLAMA_CPP_POS} -m {config.MODEL_POS} -n 2000 \
                      -f ./prompts.txt"
    print(command)
    t :str = os.popen(command
                      ).read()[3:-1]
    with open("f.txt", "w") as f:
        f.write(t)
    #return t[t.find()]a
    return t

def print_console_other(x):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 1324))
        while True:
            s.sendall(x.encode())

def run_console():
    cmd = command(f"{config.LLAMA_CPP_POS}",
                  config.MODEL_POS)
    print("LOL1")
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print("LOL2")
    p.stdin.write("hey, how are you?".encode())
    print("LOL3")
    time.sleep(1)
    print("-------------------")
    print(p.communicate())
    # while True:
    #     print_console_other(p.stdout.readline().decode())
    #     print(p.stdout.readline().decode())


#t = run("hi")
run_console()
#print(t)

#run_console()