from base import DatabaseConnection


class Searches:

    def __init__(self):
        self.db_connection = DatabaseConnection()

    def get_searches(self, id_client):
        try:
            query = "SELECT id_cliente, termino_busqueda FROM Busquedas WHERE id_cliente = ?"
            busquedas_data = self.db_connection.execute_query(
                query, id_client)

            # Preprocesamiento de datos
            # Eliminar duplicados y normalizar términos de búsqueda
            unique_searches = list(set((user_id, term.lower())
                                   for user_id, term in busquedas_data))

            # Conversión de datos a formato útil
            user_searches = {}  # Diccionario de usuarios y sus búsquedas únicas
            for user_id, term in unique_searches:
                if user_id not in user_searches:
                    user_searches[user_id] = []
                user_searches[user_id].append(term)

            # Ahora tienes un diccionario 'user_searches' que mapea usuarios a sus búsquedas únicas
            return user_searches

        except Exception as e:
            print("Error:", e)

        finally:
            # Cierra la conexión y el cursor al finalizar
            self.db_connection.close()
