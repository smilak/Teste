from cryptography.fernet import Fernet

def criar_chave():
    # Gera uma chave
    key = Fernet.generate_key()

    # Salva a chave em um arquivo
    with open('chave.key', 'wb') as chave_arquivo:
        chave_arquivo.write(key)

    print("Chave gerada e salva em 'chave.key'.")

def criptografar_mensagem():  
    # Carrega a chave do arquivo
    with open('chave.key', 'rb') as chave_arquivo:
        key = chave_arquivo.read()

    cipher = Fernet(key)

    # Mensagem original
    mensagem= input("Digite a mensagem que deseja criptografar: ")
    mensagem_bytes = mensagem.encode('utf-8')  # Codifica a string em bytes


    # Criptografa a mensagem
    mensagem_encriptada = cipher.encrypt(mensagem_bytes)

    # Salva a mensagem criptografada
    with open('mensagem_encriptada.bin', 'wb') as encrypted_file:
        encrypted_file.write(mensagem_encriptada)

    print("Mensagem criptografada e salva em 'mensagem_encriptada.bin'.")

def descriptografar():
    # Carrega a chave do arquivo
    with open('chave.key', 'rb') as chave_arquivo:
        key = chave_arquivo.read()

    cipher = Fernet(key)

    # Lê a mensagem criptografada
    with open('mensagem_encriptada.bin', 'rb') as encrypted_file:
        mensagem_encriptada = encrypted_file.read()

    # Descriptografa a mensagem
    mensagem_decriptada = cipher.decrypt(mensagem_encriptada)

    print("Mensagem descriptografada:", mensagem_decriptada.decode())

#criptografar_mensagem()
descriptografar()
