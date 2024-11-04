import segno

# Dados que você quer codificar no QR Code
data = "https://www.google.com.br"

# Gera o QR Code
qr = segno.make(data)

# Salva a imagem em um arquivo

qr.save("imagens_qrcode/qrcode.png", scale=10, dark='blue', light='white')

print("QR Code gerado e salvo como 'qrcode.png'")

