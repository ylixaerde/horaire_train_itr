# Projet horaire train
## Objectif
Déployer une base de données permettant de supporter l'affichage d'horaire de trains.

## CRUD
### Create
* **fn_input_train_code** Input de l'utilisateur et vérification du format de la réponse
(function) def fn_input_train_code() -> str

* **fn_set_train_code** Encode dans la base données le code d'un nouveau train
(function) def fn_set_train_code(
    db_name: Any,
    train_code: Any
) -> None

* **fn_init_set_train_code_menu** Renvoie une liste contenant les choix du menu
(function) def fn_init_set_train_code_menu() -> list[str]

* **fn_set_train_code_menu** Affiche le menu et fait appel à fn_input_train_code, fn_get_db_name, fn_set_train_code
(function) def fn_set_train_code_menu(list_menu: Any) -> bool

* **fn_create_db** Fais appel à fn_init_set_train_code_menu et fn_set_train_code_menu
(function) def fn_create_db() -> bool

### Read

### Update
* **fn_input_train_code** Entrée de l'utilisateur du code du train à modifier et vérification du format de la réponse (déjà existante)
(function) def fn_input_train_code() -> str

* **fn_question_id** Entrée de l'utilisateur de l'ID du train à modifier et vérification du format de la réponse
(function) def fn_question_id(
    question: Any,
    erreur: Any
) -> str

* **fn_update_train_code** Encode dans la base données le code d'un nouveau train
(function) def fn_update_train_code(
    train_code: Any,
    train_id: Any,
    db_name: Any
) -> None

* **fn_init_update_train_code_menu** Renvoie une liste contenant les choix du menu
(function) def fn_init_update_train_code_menu() -> list[str]

* **fn_update_train_code_menu** Affiche le menu et fait appel à fn_get_db_name, fn_read_db, fn_input_train_code, fn_update_train_code
(function) def fn_update_train_code_menu(list_menu: Any) -> bool

* **fn_update_db** Fais appel à fn_init_update_train_code_menu et fn_update_train_code_menu
(function) def fn_update_db() -> bool