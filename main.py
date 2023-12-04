import socket
import time
import flask

import command_executer

stream = False
def process(x):
    answer = command_executer.input_message(x, stream)
    if not stream:
        print(answer)
    return answer

def interpret_request(x):
    prompt = x["prompt"]
    prompt = str(prompt)
    print("-Input:", prompt)
    while prompt.endswith("\n"):
        prompt = prompt[:-1]
    while prompt.startswith("\n"):
        prompt = prompt[1:]
    t1 = time.time()
    answer = process(prompt)
    t2 = time.time()
    t = t2-t1
    print("-processing time:", t)
    return {"answer": answer}

def run_flask():
    f = flask.Flask(__name__) # Server erstellen

    #definieren der relativen Addresse, POST / GET - Requests
    #zulassen
    @f.route("/", methods=["GET", "POST"])
    def server():
        try:
            x = flask.request.json #Abrufen des Requests
            answer = interpret_request(x) #Weiterverarbeitung
            return answer #zurückschicken der Antwort
        except Exception as e:
            print(e)\

    @f.route("/test") # Test-Seite: Server online?
    def test():
        return "<h1>hi</h1>"

    @f.route("/online", methods=["POST", "GET"])
    def online():
        return "xonline"

    f.run(HOST, PORT)

HOST = "localhost"
PORT = 3000
if __name__ == "__main__":
    command_executer.start_program()
    #
    run_flask()

    # for x in ["hi", "how are you", "hey"]:
    #     process(x)

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.bind((HOST, PORT))
    #     s.listen()
    #     while True:
    #         conn, addr = s.accept()
    #         with conn:
    #             print(f"Connected by {addr}")
    #             while True:
    #                 print("-listening to user...")
    #                 data = conn.recv(1024)
    #                 if not data:
    #                     break
    #                 try:
    #                     data_dec = data.decode()
    #                 except UnicodeDecodeError as e:
    #                     print(e)
    #                     continue
    #                 while data_dec.startswith("\n"):
    #                     data_dec = data_dec[1:]
    #                 while data_dec.endswith("\n"):
    #                     data_dec = data_dec[:-1]
    #                 if "!close" in data_dec:
    #                     command_executer.stop_program()
    #                     conn.close()
    #                     exit(0)
    #                 print("-Input: ", data)
    #                 t1 = time.time()
    #                 answer = process(data_dec)
    #                 print("-answer")
    #                 if stream:
    #                     while True:
    #                         if len(answer) == 0:
    #                             continue
    #                         x = answer.pop(0)
    #                         print(x, end="")
    #                         if x is None:
    #                             print("time:",t1-time.time())
    #                             conn.sendall(0x03.to_bytes(1, "big", signed=False)) #END OF TEXT ASCII SYMBOL
    #                             print("-break")
    #                             break
    #                         conn.sendall(x.encode())
    #                 else:
    #                     conn.sendall(answer.encode())
    #                     print("time:",t1-time.time())
    #                     conn.sendall(0x03.to_bytes(1, "big", signed=False)) #END OF TEXT ASCII SYMBOL

