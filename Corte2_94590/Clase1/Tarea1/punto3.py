def encontrar_posiciones(a, b, pos=0, result=[]):
    if pos >= len(a):
        return result
    elif a[pos:pos+len(b)] == b:
        result.append(pos)
    return encontrar_posiciones(a, b, pos+1, result)
a = "camaleon"
b = "on"
posiciones = encontrar_posiciones(a, b)
print("Las posiciones donde se encuentra", b, "en", a, "son:", posiciones)

if __name__=='__main__':
    encontrar_posiciones=[]