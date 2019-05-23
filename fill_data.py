from user import Users
import time
users_handler = Users()
users_handler.addUser("Juan", time.strftime("%x"))
users_handler.addUser("Paco", time.strftime("%x"))
users_handler.addUser("Pepe", time.strftime("%x"))
