#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 15:35:36 2018

@author: israel
"""

def main(conn):
    import functMenu
    while True:
        print "\n\t\t===== Menu Principal ====="
        print "\n\t1) Imprimir 'Atributos' de una 'Tabla'\n\t2) Editar Objeto o Agregar Tabla",
        print "\n\t3) Eliminar Objeto o Tabla\n\t4) Salir",
        opc = int(input("> Selecciona una opcion: "))
        if(opc==1): functMenu.funcionesMenu.imprimirData(conn)
        elif(opc==2): functMenu.funcionesMenu.crearActualizarTabla(conn)
        elif(opc==3): functMenu.funcionesMenu.eliminarData(conn)
        elif(opc==4):
            print "\t\t<**FIN DEL PROGRAMA**>"
            conn.commit()
            conn.close()
            break
        else: print "¡ERROR! ... Selecciona una de las opciones"
    
    
if __name__ == '__main__':
    import functEmpresas
    print "\n\t==========<Base de Datos para Empresas>=========="
    conn = functEmpresas.funcionesEmpresa.start_dataBase()
    main(conn)
