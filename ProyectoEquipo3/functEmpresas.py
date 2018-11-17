#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:20:39 2018

@author: israel
"""
import sqlite3
from sqlite3 import Error
from os.path import realpath

class funcionesEmpresa:
    @classmethod
    def create_connection(cls,db_file):
        """ create a database connection to a SQLite database """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print e
            return None
    @classmethod
    def create_table(cls,conn, create_table_sql,nameBusiness):
        """create a table from create_table_sql"""
        try:
            c = conn.cursor()
            c.execute(create_table_sql.format(nameBusiness))
        except Error as e:
                print e

    @classmethod
    def create_dataBase(cls,conn):
        sql_create_business_table = ''' CREATE TABLE IF NOT EXISTS '{}' (
                                        id integer PRIMARY KEY,
                                        NOMBRE TEXT NOT NULL,
                                        DATO NULL
                                        ); '''
        tmp = raw_input("Dame el nombre de la Empresa: ")
        funcionesEmpresa.create_table(conn,sql_create_business_table,tmp)
        return tmp

    @classmethod
    def create_attribute(cls,conn,atributo,nombreEmpresa):
        sql = "INSERT INTO '{tb}'(NOMBRE, DATO) VALUES('{atr}',NULL);".format(tb=nombreEmpresa,atr=atributo)
        cur = conn.cursor()
        cur.execute(sql)

    @classmethod
    def print_allTable(cls,conn):
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
        tmp = c.fetchall()
        for i in tmp: print i
    
    @classmethod 
    def start_dataBase(cls):
        database = realpath("dataEmpresas.db")
        # create a database connection
        conn = funcionesEmpresa.create_connection(database)
        if conn is not None:
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master")
            tmp = cur.fetchone()
            if tmp is None:
                print "Estoy aqui"
                baseDeDatos = funcionesEmpresa.metaData(conn)
                return baseDeDatos
            else: return conn
        else:
            print("Error! cannot create the database connection.")
    @classmethod
    def metaData(cls,conn):
        archivo=open("BaseProto.txt","r")
        lines=archivo.readlines()
        archivo.close()
        sql_create_business_table = ''' CREATE TABLE IF NOT EXISTS '{}' (
                                        id integer PRIMARY KEY,
                                        NOMBRE TEXT NOT NULL,
                                        DATO NULL
                                        ); '''        
        print "\t\t<**Cargando BASE DE DATOS**>"
        bandera = 0
        for line in lines:
            line=line.strip()
            if bandera == 0:
                bandera = bandera + 1
                nombreEmpresa = line
                print nombreEmpresa
                funcionesEmpresa.create_table(conn,sql_create_business_table,line)
            else:
                print nombreEmpresa," ",line
                funcionesEmpresa.create_attribute(conn,line,nombreEmpresa)
                bandera = bandera + 1
                if bandera == 11: bandera = 0
        print "\t\t<**CARGADO CON EXITO**>"     
        return conn
        