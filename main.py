import fn_horaire_train

class App:
    def fn_question(question, erreur):
        reponse = input(question)
        while not reponse.isalpha():
            print(erreur)
            reponse = input(question)
        return reponse

    def fn_question_int(question, erreur):
        reponse = input(question)
        while not reponse.isnumeric():
            print(erreur)
            reponse = input(question)
        return reponse

    def fn_init_menu():
        q_choix_1 = "[1] Créer une base de données"
        q_choix_2 = "[2] Encoder des données"
        q_choix_3 = "[3] Afficher des données"
        q_choix_4 = "[4] Mettre-à-jour des données"
        q_choix_5 = "[5] Supprimer des données"
        q_choix_6 = "[6] Quitter"
        list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4, q_choix_5, q_choix_6]
        return list_menu


    def fn_menu(list_menu):
        print(f'\n----Menu - Projet Horaire train----')
        for item in list_menu:
            print(f'{item}')
        q_status = "Entrer votre choix (1-6) : "
        e_status = "\nErreur : Caractères invalides\n"
        status = int(fn_question_int(q_status, e_status))
        match status:
            case 1:
                init_app = init_db.App()
                init_app.fn_init_db()
                return True
            case 2:
                create_app = create_db.App()
                boucle = True
                while boucle:
                    boucle = create_app.fn_create_db()
                return True
            case 3:
                read_app = read_db.App()
                read_app.fn_read_db()
                return True
            case 4:
                update_app = update_db.App()
                update_app.fn_update_db()
                return True
            case 5:
                delete_app = delete_db.App()
                delete_app.fn_delete_db()
                return True
            case 6:
                print(f'Fermeture de l\'application')
                return False
            case _:
                print(f'\nErreur : Choix non-valide\n')
                return True

    def fn_app():
        boucle = True
        list_menu = fn_init_menu()
        while boucle:
            boucle = fn_menu(list_menu)

if __name__ == "__main__":
    fn_app()