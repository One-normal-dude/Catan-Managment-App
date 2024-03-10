import time
class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
        self.settlements = 0
        self.cities = 0
        self.roads = 0
        self.ships = 0
        self.victory_points = 0
        self.dev_cards = {'Kartica razvoja': 0}  # New attribute for development cards

    def build_settlement(self):
        if self.has_enough_resources({'wood': 1, 'brick': 1, 'sheep': 1, 'wheat': 1}):
            self.pay_resources({'wood': 1, 'brick': 1, 'sheep': 1, 'wheat': 1})
            self.settlements += 1
            self.victory_points += 1
            print(f"{self.name} built a Selo!")
        else:
            print("Not enough resources to build a Selo.")

    def build_road(self):
        if self.has_enough_resources({'wood': 1, 'brick': 1}):
            self.pay_resources({'wood': 1, 'brick': 1})
            self.roads += 1
            print(f"{self.name} built a Cesta!")
        else:
            print("Not enough resources to build a Cesta.")

    def build_city(self):
        if self.has_enough_resources({'ore': 3, 'wheat': 2}):
            self.pay_resources({'ore': 3, 'wheat': 2})
            self.settlements -= 1
            self.cities += 1
            self.victory_points += 2  # A Grad is worth 2 points
            print(f"{self.name} built a Grad!")
        else:
            print("Not enough resources to build a Grad.")

    def build_ship(self):
        if self.has_enough_resources({'wood': 1, 'sheep': 1}):
            self.pay_resources({'wood': 1, 'sheep': 1})
            self.ships += 1
            print(f"{self.name} built a Brod!")
        else:
            print("Not enough resources to build a Brod.")

    def add_resources(self, resources):
        for resource, amount in resources.items():
            self.resources[resource] += amount

    def remove_resources(self, resources):
        for resource, amount in resources.items():
            self.resources[resource] -= amount

    def purchase_dev_card(self):
        if self.has_enough_resources({'wheat': 1, 'ore': 1, 'sheep': 1}):
            self.pay_resources({'wheat': 1, 'ore': 1, 'sheep': 1})
            self.dev_cards['Kartica razvoja'] += 1
            print(f"{self.name} purchased a Kartica razvoja!")
        else:
            print("Not enough resources to purchase a Kartica razvoja.")

    def activate_dev_card(self):
        if self.dev_cards['Kartica razvoja'] > 0:
            self.dev_cards['Kartica razvoja'] -= 1
            # Logic to activate the effect of the development card goes here
            print(f"{self.name} activated a Kartica razvoja!")
        else:
            print("You don't have any Kartica razvoja to activate.")

    def has_enough_resources(self, cost):
        for resource, amount in cost.items():
            if self.resources.get(resource, 0) < amount:
                return False
        return True

    def pay_resources(self, cost):
        for resource, amount in cost.items():
            self.resources[resource] -= amount

    def get_points(self):
        return self.victory_points


class CatanGame:
    def __init__(self, players):
        self.players = players

    def play(self):
        longest_road_player = None
        longest_road_length = 0
        for player in self.players:
            while True:
                print(f"{player.name}'s turn:")
                print(f"Resources: {player.resources}")
                action = input("Choose an action (Selo, Cesta, Grad, Brod, Dobivanje, Gubljenje, "
                               "Kartica razvoja, Aktivacija, bodovi, Sljedeči): ")
                if action == "Selo":
                    player.build_settlement()
                elif action == "Cesta":
                    player.build_road()
                elif action == "Grad":
                    player.build_city()
                elif action == "Brod":
                    player.build_ship()
                elif action == "Dobivanje":
                    resources = input("Enter resources to add (e.g., wood:3 brick:2): ").split()
                    resources_dict = {}
                    for resource_str in resources:
                        resource, amount = resource_str.split(':')
                        resources_dict[resource] = int(amount)
                    player.add_resources(resources_dict)
                elif action == "Gubljenje":
                    resources = input("Enter resources to remove (e.g., wood:3 brick:2): ").split()
                    resources_dict = {}
                    for resource_str in resources:
                        resource, amount = resource_str.split(':')
                        resources_dict[resource] = int(amount)
                    player.remove_resources(resources_dict)
                elif action == "Kartica razvoja":
                    player.purchase_dev_card()
                elif action == "Aktivacija":
                    player.activate_dev_card()
                elif action == "bodovi":
                    points = int(input("Enter the number of points to gain: "))
                    player.victory_points += points
                    print(f"{player.name} gained {points} points.")
                elif action == "Sljedeči":
                    if player.roads > longest_road_length:
                        longest_road_length = player.roads
                        longest_road_player = player
                    break
                if player.victory_points >= 12:
                    print(f"{player.name} has won with {player.victory_points} points!")
                    time.sleep(10)
                    return
            if longest_road_player is not None and longest_road_length > 5:
                print(f"{longest_road_player.name} has got a reward for najduža cesta!")
            longest_road_player = None
            longest_road_length = 0


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter player {i + 1}'s name: ")
        players.append(Player(name))

    game = CatanGame(players)
    game.play()
