import os

linux = os.name != "nt"

if linux:
    # LLAMA_CPP_POS = "/media/lol/Data/storage/Programming/infoProjektServer/llama.cpp/build2/bin/main"
    LLAMA_CPP_POS = "/media/lol/Data/storage/Programming/infoProjektServer/llama.cpp/buildgpu/bin2/main"
    MODEL_POS = "/media/lol/Data/storage/Programming/infoProjektServer/models/llama-2-7b-chat.ggmlv3.q2_K.gguf"

else:
    #LLAMA_CPP_POS = "F:\\storage\\Programming\\infoProjektServer\\winllama\\main.exe"
    LLAMA_CPP_POS = r"C:\Users\Admin\Desktop\lamacpp\llama.cpp\buildgpu\bin\Release\main.exe"
    MODEL_POS = "C:\\Users\\Admin\Desktop\\llm_models\\llama-2-7b-chat.ggmlv3.q2_K.bin"
    #MODEL_POS = "F:/storage/Programming/infoProjektServer/models/llama-2-7b-chat.ggmlv3.q2_K.bin"

    #LLAMA_CPP_POS = r"C:\Users\Admin\Desktop\winllama\main.exe"
    #MODEL_POS = "F:/storage/Programming/infoProjektServer/models/llama-2-7b-chat.ggmlv3.q2_K.gguf"