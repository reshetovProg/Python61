class User:
    __user_counter = 1
    def __init__(self, name):
        self.id = User.__user_counter
        self.name = name
        self.__order = 0
        User.__user_counter+=1

    def __str__(self):
        return f"{self.id}: {self.name}| {self.__order}"

    def add_order(self):
        self.__order+=1

    @staticmethod
    def get_user_count():
        return (User.__user_counter)-1

if __name__ == '__main__':
    def show_all(users: list[User]):
        for i in users:
            print(i)

    print(f"текст в классе User: {__name__}")
    user1 = User("Pol")
    user2 = User("Alex")
    user3 = User("Genry")
    users = [user1, user2, user3]
    show_all(users)
    print("----")
    user3.add_order()
    show_all(users)
