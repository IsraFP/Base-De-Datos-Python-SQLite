#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:26:00 2018

@author: israel
"""
import functEmpresas

class funcionesMenu:
    @classmethod
    def imprimirData(cls,conn):
        print "\n\t..:Imprimir:..\n>> Base de Datos Tabla:\n",functEmpresas.funcionesEmpresa.print_allTable(conn)
        tablaBuscado = raw_input("\n>>> Selecciona la 'Tabla' para buscar tu atributo: ")
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{}';".format(tablaBuscado))
        id_exists = cur.fetchone()
        if id_exists:
            cur.execute("SELECT * FROM '{}' ".format(tablaBuscado))
            atributos = cur.fetchall()
            for atributo in atributos: print atributo
        else: print "¡ERROR! ... No existe esa 'Tabla' o fue mal escrita"
        
    @classmethod
    def busquedaConfirmada(cls,conn):
        cur = conn.cursor()
        tablaBuscado = raw_input(">>> Selecciona la 'Tabla' para buscar el atributo: ")
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{}';".format(tablaBuscado))
        id_exists = cur.fetchone()
        if id_exists:
            cur.execute("SELECT * FROM '{}'".format(tablaBuscado))
            getAtributo = cur.fetchall()
            for pr_atributo in getAtributo: print pr_atributo
            atributoBuscado = raw_input(">>> Selecciona el 'Atributo' a encontrar: ")
            cur.execute("SELECT * FROM '{}' WHERE NOMBRE = '{}';".format(tablaBuscado,atributoBuscado))
            id_existName = cur.fetchone()
            if id_existName:
                return tablaBuscado,atributoBuscado
            else:
                print "¡ERROR! ... No existe ese 'Atributo' o fue mal escrita"
                return False
        else: 
            print "¡ERROR! ... No existe esa 'Tabla' o fue mal escrita"
            return False

    @classmethod
    def eliminarData(cls,conn):
        while True:
            print '''\n\t..:Eliminar:..\n>> ¿Que desea realizar?
            \n\t1) Eliminar objeto\n\t2) Eliminar tabla\n\t3) Salir a 'Menu Principal' '''
            opc = int(input("> Selecciona una opcion: "))
            if(opc==1): funcionesMenu.eliminarObjeto(conn)
            elif(opc==2): funcionesMenu.eliminarTabla(conn)
            elif(opc==3): break
            else: print "¡ERROR! ... Elija una de la opciones"

    @classmethod 
    def eliminarObjeto(cls,conn):
        print "\n\t..*Eliminando Objeto*..\n>> Base de Datos Tabla:\n",functEmpresas.funcionesEmpresa.print_allTable(conn)
        bC = funcionesMenu.busquedaConfirmada(conn)
        if bC:
            cur = conn.cursor()
            cur.execute("DELETE FROM '{}' WHERE NOMBRE = '{}'".format(bC[0],bC[1]))
            print "\t\t<**OBJETO ELIMINADO CON EXITO**>"
            cur.execute("SELECT * FROM '{}' ;".format(bC[0]))
            tmp = cur.fetchone()
            if tmp is None:
                print "\t> No puede estar la lista: 'Vacia'"
                name = raw_input("\t> Dame el nombre del nuevo atributo: ")
                functEmpresas.funcionesEmpresa.create_attribute(conn,name,bC[0])
                print "\t\t<**ATRIBUTO AGREGADO CON EXITO**>"
                conn.commit()
        else:
            print "¡ERROR! ... No se encontro ese 'atributo' o no se escribio correctamente"
    
    @classmethod
    def eliminarTabla(cls,conn):
        print "\n\t..*Eliminando Tabla*..\n>> Base de Datos Tabla:\n", functEmpresas.funcionesEmpresa.print_allTable(conn)
        tablaBuscado = raw_input(">>> Selecciona la 'Tabla' para buscar a 'Eliminar': ")
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = '{}';".format(tablaBuscado))
        bC = cur.fetchone()
        if bC:
            cur.execute("DROP TABLE IF EXISTS '{}'".format(bC[0]))
            print "\t\t<**TABLA ELIMINADA CON EXITO**>"
            conn.commit()
        else:
            print "¡ERROR! ... No se encontro esa 'tabla' o no se escribio correctamente"
    
    @classmethod
    def crearActualizarTabla(cls,conn):
         while True:
            print '''\n\t..:Crear o Actualizar Tabla:..\n>> ¿Que desea realizar?
            \n\t1) Editar objeto\n\t2) Crear tabla\n\t3) Salir a 'Menu Principal' '''
            opc = int(input("> Selecciona una opcion: "))
            if(opc==1): funcionesMenu.actualizarData(conn)
            elif(opc==2): funcionesMenu.crearTabla(conn)
            elif(opc==3): break
            else: print "¡ERROR! ... Elija una de la opciones"
    
    @classmethod
    def actualizarData(cls,conn):
        print "\n\t..:Editar Objeto:..\n>> Base de Datos Tabla:\n",functEmpresas.funcionesEmpresa.print_allTable(conn)
        bC= funcionesMenu.busquedaConfirmada(conn)
        if bC:
            cur = conn.cursor()
            valor = raw_input(">>> Dame el 'valor' a agregar: ")
            cur.execute("UPDATE '{}' SET DATO = '{}' WHERE NOMBRE = '{}'".format(bC[0],valor,bC[1]))
            print "\t\t<**AGREGADO CON EXITO**>"
            conn.commit()
    @classmethod
    def crearTabla(cls,conn):
        print "\n\t..:Creando Tabla:.."
        nombreEmpresa = functEmpresas.funcionesEmpresa.create_dataBase(conn)
        with conn:
            for i in range(0,10):
                name = raw_input("\t >Dame el nombre del atributo[{}]: ".format(i))
                functEmpresas.funcionesEmpresa.create_attribute(conn,name,nombreEmpresa)
            print "\t\t<**TABLA CREADA CON EXITO**>"

        