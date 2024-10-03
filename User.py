from datetime import datetime

class User:
    def __init__(self, name, password, birthday, native_language, learn_language, hobbies):
        self.name = name
        self.password = password
        self.birthday = birthday 
        self.native_language = native_language
        self.learn_language = learn_language
        self.hobbies = hobbies

    def age_verification(self):
        birthday_parts = self.birthday.split("-") 
        day = int(birthday_parts[0])
        month = int(birthday_parts[1])
        year = int(birthday_parts[2])

        # Calcular la edad
        birth_date = datetime(year, month, day)
        current_date = datetime.now()
        age = (current_date - birth_date).days 

        return age >= 18


#============ Main ===============#
if __name__ == "__main__":
    user = User("Juan", "1234", "13-09-1987", "Español", "Inglés", "Leer")

    if user.age_verification():
        print(f"{user.name} is of legal age.")
    else:
        print(f"{user.name} not of legal age.")