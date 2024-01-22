import sqlite3
import os
import re

class App:
    def __init__(self):
        self.file_path = os.path.realpath(__file__)
        self.work_dir = os.path.dirname(self.file_path)
        # print(f'Chemin du dossier script : {self.work_dir}')
        # print(f'Chemin de la db : {self.work_dir}/data.db')
        self.db_name = f'{self.work_dir}/data.db'
        self.sql_create_script = f'{self.work_dir}/create-horaire-train.sql'

    def fn_question(self, question, erreur):
        reponse = input(question)
        while not reponse.isalpha():
            print(erreur)
            reponse = input(question)
        return reponse

    def fn_question_int(self, question, erreur):
        reponse = input(question)
        while not reponse.isnumeric():
            print(erreur)
            reponse = input(question)
        return reponse
    
    def fn_question_code(self, question, erreur):
        reponse = input(question).upper()
        pattern = re.compile(r'^[A-Z]{2}\d{4}$')
        while not bool(pattern.match(reponse)):
            print(erreur)
            reponse = input(question).upper()
        return reponse
    
    def fn_create_train_code(self):
        q_status = "Entrer un code de 6 caractères pour le train (Ex : AB1234) : "
        e_status = "\nErreur : Codes invalides \nEntrer un code de 6 caractères pour le train (Ex : AB1234) : \n"
        self.train_code = self.fn_question_code(q_status, e_status)

    def fn_init_menu(self):
        q_choix_1 = "[1] Ajouter un train"
        q_choix_2 = "[2] Quitter"
        self.list_menu = [q_choix_1, q_choix_2]

    def fn_menu(self):
        print(f'\n----Menu - Projet Horaire train----')
        for item in self.list_menu:
            print(f'{item}')
        q_status = "Entrer votre choix (1-2) : "
        e_status = "\nErreur : Caractères invalides\n"
        status = int(self.fn_question_int(q_status, e_status))
        match status:
            case 1:
                self.fn_create_train_code()
                return True
            case 2:
                print(f'Fermeture de l\'application')
                return False
            case _:
                print(f'\nErreur : Choix non-valide\n')
                return True
    
    def fn_create_db(self):
        try:
            self.fn_init_menu()
            boucle = self.fn_menu()
        except Exception as error:
            print(f"{error}")

        sqliteConnection = None
        try:            
            with sqlite3.connect(self.db_name, timeout=10) as sqliteConnection:
                print(f"Connected to the database {self.db_name}")
                cursor = sqliteConnection.cursor()
                
                # try:
                    # with open(self.sql_create_script, "r") as sqlite_file:
                    #    try:
                    #        sql_script = sqlite_file.read()
                    #    except Exception as error:
                    #        print(f"Error while reading the SQL script: {error}")
                    #        return
                # except Exception as error:
                    # print(f"Error while opening the SQL file: {error}")
                    # return
                
                try:
                    print(f"Commande SQL exécutée : INSERT INTO TRAIN (code) VALUES ('{self.train_code}');")
                    cursor.execute(f"INSERT INTO TRAIN (code) VALUES ('{self.train_code}');")
                    # print("SQLite script executed successfully")
                    print("SQLite command executed successfully")
                except sqlite3.Error as error:
                    print(f"Error while executing SQLite script: {error}")
                finally:
                    cursor.close()
        except sqlite3.Error as error:
            print(f"Error while connecting to SQLite: {error}")
        except Exception as error:
            print(f"{error}")
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
            return boucle

if __name__ == "__main__":
    app = App()
    app.fn_create_db()