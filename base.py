import pyodbc
import os
import sys

server = 'INKWAVE'
database = 'ecommerce'
username = 'pedro'
password = 'Juandejesus2930'


class DatabaseConnection:
    def __init__(self):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self._create_connection()
        self.cursor = self.conn.cursor()

    def _create_connection(self):
        try:
            conn_str = f'DRIVER=SQL Server;SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};charset=UTF-8'
            return pyodbc.connect(conn_str)
        except pyodbc.Error as e:
            # Lanza un error personalizado
            raise Exception("Error al conectar a la base de datos")

    def execute_query(self, query, id_client):
        try:
            if (id_client == 0):
                self.cursor.execute(query)
                results = self.cursor.fetchall()
                return results
            else:
                self.cursor.execute(query, id_client)
                results = self.cursor.fetchall()
                return results
        except pyodbc.Error as e:
            # Lanza un error personalizado
            raise Exception("Error al ejecutar la consulta")

    def close(self):
        self.conn.close()
