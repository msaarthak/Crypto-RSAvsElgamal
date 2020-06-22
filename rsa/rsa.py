import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import time

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

fp = open("150kb")
text = []
encrypt = []
start_time = time.time()


while 1:
    #text.append(line)
    k =  fp.read(60)
    if k == "":
        break
    encrypted = publickey.encrypt(k.encode('utf-8'), 32)
    #print (encrypted)	
    encrypt.append(str(encrypted))	
#text = "".join(text)


#message to encrypt is in the above line 'encrypt this message'
print("---150kbEncryption  %s seconds ---" % (time.time() - start_time))

text = "".join(encrypt)

#print ('encrypted message:', text) #ciphertext
f = open ('encryption150.txt', 'w')
f.write(str(text)) #write ciphertext to file
f.close()

#decrypted code below


decrypt = []
start_time = time.time()
for en in encrypt:
    #text.append(line)
    decrypted = key.decrypt(ast.literal_eval(str(en)))
    decrypt.append(str(decrypted))

print("---150kbDecryption  %s seconds ---" % (time.time() - start_time))
#print ('decrypted', decrypted)

text = "".join(decrypt)
f = open ('decryption150.txt', errors='ignore')
f.write(str(text))
f.close()
