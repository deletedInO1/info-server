linux = True

if linux:
    LLAMA_CPP_POS = "/media/lol/Data/storage/Programming/infoProjektServer/llama.cpp/build/bin/main"
    MODEL_POS = "/media/lol/Data/storage/Programming/infoProjektServer/models/llama-2-7b-chat.ggmlv3.q2_K.gguf"

else:
    LLAMA_CPP_POS = "F:\\storage\\Programming\\infoProjektServer\winllama\\main.exe"
    MODEL_POS = "C:\\Users\\Admin\Desktop\\llm_models\\llama-2-7b-chat.ggmlv3.q2_K.bin"