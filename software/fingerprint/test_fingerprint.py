from pyfingerprint.pyfingerprint import PyFingerprint

try:

    f = PyFingerprint(
        '/dev/ttyAMA5',
        19200,
        0xFFFFFFFF,
        0x00000000
    )

    if f.verifyPassword():

        print()
        print("=================================")
        print("LECTOR BIOMETRICO DETECTADO")
        print("=================================")

        print("Plantillas almacenadas:",
              f.getTemplateCount())

        print("Capacidad total:",
              f.getStorageCapacity())

    else:

        print("Password incorrecta")

except Exception as e:

    print("ERROR:")
    print(e)

