class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f"«{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.»"

    def get_name_towm(self):
        return f"{self.name} {self.surname}. {self.city}."

client_1 = Client("Иван", "Петров", "Москва", 50)
print(client_1)
print("="*100)
pet_clients = [
    {"Name": "Вася", "Surname": "Иванов", "City": "Москва", "Money": 100},
    {"Name": "Варя", "Surname": "Пегова", "City": "Петроград", "Money": 1000},
    {"Name": "Константин", "Surname": "Силонов", "City": "Ванкувер", "Money": 1000},
    {"Name": "Анастасия", "Surname": "Мыскина", "City": "Тверь","Money": 900},
    {"Name": "Игорь", "Surname": "Сферинский", "City": "Киев", "Money": 50}
]

for client in pet_clients:
    tempClient = Client(client.get("Name"), client.get("Surname"),
                        client.get("City"), client.get("Money"))
    print(tempClient.get_name_towm())