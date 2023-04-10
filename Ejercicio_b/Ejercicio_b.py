class Yin: pass
class Yang:
    def __del__(self):
        print("Yang destruido")
yin = Yin()
yang = Yang()
yin.yang = yang

print(yang)
print(yang is yin.yang)

del(yang)

del(yin.yang)

print("?")
# La diferencia es que ahora el yang no está ligado con el yin, por lo tanto, al borrar el yin, el yang no tiene la referencia borrada,
# y este aparece delante de la interrogación.