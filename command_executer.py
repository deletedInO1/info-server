import threading
import subprocess
import time
import config

#good results:  .\main.exe -m C:\\Users\\Admin\Desktop\\llm_models\\llama-2-7b-chat.ggmlv3.q2_K.bin -ins -ngl 1 --temp 0.7 --repeat_penalty 1.1 -s 42 -n -1 -c 2048 -p "This is a conversation between user and llama, a friendly chatbot. respond in simple markdown."

prompt = "This is a conversation between user and llama, a friendly chatbot. respond in simple markdown."


#cmd = rf"{config.LLAMA_CPP_POS} -ins -t 8 -ngl 1 -m {config.MODEL_POS} -c 512 --temp 0.7 --repeat_penalty 1.1 -s 42 -n -1"
#cmd = rf'{config.LLAMA_CPP_POS} -ins -t 8 -ngl 1 -m {config.MODEL_POS} -c 512 --temp 0.7 --repeat_penalty 1.1 -p "{prompt}" -s 42 -n -1'
cmd = rf'{config.LLAMA_CPP_POS} -ins -t 8 -ngl 1 -m {config.MODEL_POS} -c 512 --temp 0.7 --repeat_penalty 1.1 -f promptf3.txt -s 42 -n -1 --n-gpu-layers 35'

#cmd = rf'{config.LLAMA_CPP_POS} -ins -t 8 -ngl 1 -m {config.MODEL_POS} -c 512 --temp 0.7 --repeat_penalty 1.1 -f promptf3.txt -s 42 -n -1'

#cmd = rf'{config.LLAMA_CPP_POS} -ins -t 8 -ngl 1 -m {config.MODEL_POS} -c 2048 --temp 0.7 --repeat_penalty 1.1 -s 42 -n -1 ' \
#      rf'-p "{prompt}"'
print(cmd)
#n_threads":8,"total_threads":16,":"AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | VSX = 0 | "}
#vocab 32000
#n_ctx 512
#n_embd 5096
#n_mult 256
#n_head 32
#n_head_kv 32
#n_layer 32
#n_rot 128
#n_gqa 1
#rnorm_eps
#n_ff 11008

# args = ["--interactive-first",
#         "-t", "8",
#         "-p", #TODO
#         "-"
#         ]

#       r"--gpu-layers 40"
#cmd = "py popentest_cmd.py"
#cmd = config.LLAMA_CPP_POS
process: subprocess.Popen = None
clock = 0
history = []
def start_program():
    global process
    process = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    __readstream([])
    print("ready")


def stop_program():
    process.kill()

def input_message(inp: str, as_stream):
    process.stdin.write(inp + "\n")
    process.stdin.flush()
    return _readstream(as_stream)



def __readstream(_queue: list):
    global clock
    while True:
        try:
            character = process.stdout.read(1)
        except Exception as e:
            print(e)
            break
        clock = 0
        if not character:
            break
        if character == ">":
            _queue.append(None)
            break
        #print(character)
        _queue.append(character)


def _readstream(as_stream):
    global clock
    _queue = []
    thread = threading.Thread(target=__readstream, args=(_queue, ))
    thread.daemon = True
    thread.start()

    if as_stream:
        return _queue

    while clock < 500 and thread.is_alive():
        clock += 1
        time.sleep(10/1000)
        # if clock % 100 == 0:
        #     print(clock)
    if thread.is_alive():
        print("stop waiting for thread")
    q = _queue[:]
    s = ""
    for a in q:
        if a is not None:
            s += a
    return s

if __name__ == "__main__":
    start_program()
    # print("output: ", input_message("hi, how are you", False))
    # print("output: ", input_message("hey, how are you", False))
    # print("output: ", input_message("lol", False))
    print("output: ", input_message(input("Your input: "), False))
    exit(0)