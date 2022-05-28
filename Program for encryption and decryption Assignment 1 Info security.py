generateKeys()
privateKey, publicKey =loadKeys()

message = input('Write your message here:')
ciphertext = encrypt(message, publicKey)

signature = sign(message, privateKey)

text = decrypt(ciphertext, privateKey)

print(f'Cipher text: {ciphertext}')
print(f'Signature: {signature}')

if text:
    print(f'Message text: {text}')
else:
    print(f'Unable to decrypt the message.')

if verify(text, signature, publicKey):
    print(Successfully verified signature)
else:
    print('The message signature could not be verified')