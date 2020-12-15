#"Escribir un programa que permita que el usuario ingrese"

def encripta(msg):
    chars_x = "abcdefeghijklmnopqrstuvwxyz,;.-"
    chars_y = "VCHPRZGJNTLSKFBDQWAXEUYMOI;.,-"
    msg_cifrado=" "
    for x in msg:
        for n in range (len(chars_x)):
            if x==chars_x[n]:
                msg_cifrado += chars_y[n]
    return msg_cifrado 

msg =  "hello, world"            
msg_cifrado = encripta(msg) 
print(msg)
print(msg_cifrado)

