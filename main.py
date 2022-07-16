
solicitudes = {}
aprobados = {}


def solicitud_prestamos():
    clienteSolicitud = input("¿A nombre de quien se procesara el prestamo?: ")
    cedulaSolicitante = input("¿cual es la cedula del solicitante?: ")
    montoSolicitado = int(input("¿cual es el monto a prestar?: "))
    plazoPago = int(input("¿Cual es el plazo de pago? (ingresar el tiempo de pago en meses): "))
    Intereses = int(input("ingresa la taza de interes a cobrar (base a 100%): "))
    diasPago = input("¿que dias seran los pagos del prestamo?: ")
    montodeuda = montoSolicitado
    solicitudes = [clienteSolicitud, cedulaSolicitante, montoSolicitado, plazoPago, Intereses, diasPago, montodeuda]
    return solicitudes



while True:
    menu = input("""menu
                1. solicitud de prestamos
                2. aprobacion de prestamos
                3. pagos
                4. cancelaciones
                5. Consulta de clientes
                6. salir
                : """)
    print("")
    
        
    if menu == "1":
        datosSolicitudes = solicitud_prestamos()
        solicitudes[datosSolicitudes[1]] = datosSolicitudes


    elif menu == "2":
        if solicitudes == {}:
            print("no existen clientes en esta seccion")
            print("")
        else:
            print(solicitudes)
            seleccionSolicitante = input("selecciona un solicitante escribiendo su cedula o RNC: ")
            print("")
            solicitanteSeleccionado = solicitudes[seleccionSolicitante]
            decision = input("""¿desea aprobar esta solicitud de prestamo?: 
            1. si
            2. no:
            """)
            print("")
            if decision == "1":
                aprobados[solicitanteSeleccionado[1]] = solicitanteSeleccionado
                del(solicitudes[seleccionSolicitante])
                print("este usuario ha sido aprobado")
                print("")
            elif decision == "2":
                print("este usuario ha sido denegado")
                print("")
                del(solicitudes[seleccionSolicitante])
            else:
                print("esto no es una opcion")
                print("")


    elif menu == "3":
        usuarioPago = input("ingrese la cedula o RNC del usuario a cobrar: ")
        print("")
        datosUsuario = aprobados[usuarioPago]
        if datosUsuario[6] == 0:
            print("este usuario ya no debe")
            print("")
            del(aprobados[usuarioPago])
        else:
            interesesUsuario = (datosUsuario[4] / 100) * datosUsuario[2]
            montoPago = (datosUsuario[2] + interesesUsuario) / datosUsuario[3]
            pago = input(f"""el monto a pagar es de {montoPago}, ¿el usuario desea pagar?:
            1. si
            2. no:
            """)
            print("")


            if pago == "1":
                deuda = datosUsuario[6]
                deudaActual = datosUsuario[6] - montoPago
                print(f"""el pago ha sido realizado con exito, el monto restante a pagar es de {datosUsuario[6]}""")
                print("")
                for x in range(len(datosUsuario)):
                    if datosUsuario[x] == deuda:
                        datosUsuario[x] = deudaActual
                        del(aprobados[usuarioPago])
                        aprobados[usuarioPago] = datosUsuario
                        f = open("pagos.txt", "a")
                        f.write(f"""el cliente llamado {datosUsuario[0]} realizado su pago el {datosUsuario[5]} de este mes,
                        el usuario ha pagado {montoPago} pesos, restando una deuda de {deudaActual}
                        
                        """)
                        f.close()


            elif pago == "2":
                deuda = datosUsuario[6]
                deudaActual = datosUsuario[6] + 200
                for x in range(len(datosUsuario)):
                    if datosUsuario[x] == deuda:
                        datosUsuario[x] = deudaActual
                        del(aprobados[usuarioPago])
                        aprobados[usuarioPago] = datosUsuario
                        f = open("pagos.txt", "a")
                        f.write(f"""el usuario llamado {datosUsuario[0]} no ha realizado su pago a tiempo, por tanto,
                        el usuario posee una multa de mora, pasando de deber {deuda} a deber {deudaActual}
                        
                        """)
                        f.close()


                print("se ha aplicado una penitencia de 200 pesos al usuario por mora")
                print("")
                del(aprobados[usuarioPago])
                aprobados[usuarioPago] = datosUsuario
            else:
                print("esta no es una opcion")
                print("")

    elif menu == "4": 
        usuarioCancelacion = input("ingrese la cedula o RNC del usuario a cancelar parte del monto prestado: ")
        print("")
        datosUsuario = aprobados[usuarioCancelacion]
        montoCancelado = int(input("¿que monto desea cancelar el usuario?: "))
        print("")
        deuda = datosUsuario[6]
        if montoCancelado > deuda:
            print("no puede cancelar mas de la cantidad prestada")
            print("")
        else:
            deudaActual = deuda - montoCancelado
            for x in range(len(datosUsuario)):
                if datosUsuario[x] == deuda:
                    datosUsuario[x] = deudaActual
                    del(aprobados[usuarioPago])
                    aprobados[usuarioPago] = datosUsuario
                    f = open("pagos.txt", "a")
                    f.write(f"""el usuario {datosUsuario[0]} ha tenido una cancelacion de {montoCancelado}
                    en su deuda de {deuda}, quedando un monto de {deudaActual} a pagar""")
                    f.close()

    elif menu == "5":
        print(aprobados)
        idclientes = input("¿que cliente desea consultar?: ")
        print("")
        datosUsuario = aprobados[idclientes]
        print(f"""datos del usuario:
        1. Nombre del cliente: {datosUsuario[0]}
        2. Cedula del cliente: {datosUsuario[1]}
        3. Monto solicitado: {datosUsuario[2]}
        4. plazo de pago: {datosUsuario[3]}
        5. taza de interes: {datosUsuario[4]}%
        6. dias de pago: {datosUsuario[5]} de cada mes
        7. monto en deuda: {datosUsuario[6]}
        8. monto pagado hasta la actualidad: {datosUsuario[2] - datosUsuario[6]}
        9. cuotas: {(datosUsuario[4] / 100) * datosUsuario[2]}""")
        print("")


    elif menu == "6":
        print("gracias por confiar en nuestro sistema de prestamos")
        break

    else:
        print("elija una opcion existente")
        print("")