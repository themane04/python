class PenguinRaceCalculator:
    def __init__(self, race_snapshot, penguin_names, progress):
        self.progress = progress
        self.race_snapshot = race_snapshot
        self.penguin_names = penguin_names
        self.calculate_progress()

    def calculate_progress(self):
        self.progress = {}
        for i, snapshot in enumerate(self.race_snapshot):
            penguin_position = snapshot.find("p")
            total_distance = len(snapshot) - 1
            self.progress[self.penguin_names[i]] = penguin_position / total_distance

    def get_winners(self):
        winners = []
        sorted_progress = sorted(self.progress, key=lambda p: self.progress[p], reverse=True)

        for i in range(0, 3):
            if i < len(sorted_progress):
                winners.append(sorted_progress[i])

        formatted_result = f"GOLD: {winners[0]}: SILVER: {winners[1]} BRONZE: {winners[2]}"
        return formatted_result


# RACE 1
print("")
snapshot1 = ["|----p---~~---|", "|--~p-----~~~-|", "|~~~~----p~---|"]
names1 = ["Peter", "Max", "Hennrich"]
calculator1 = PenguinRaceCalculator(snapshot1, names1, progress=0)
print("The race is: ", snapshot1)
print("Winners in the first race:", calculator1.get_winners())
print("")

# RACE 2
snapshot2 = ["|p-------~~---|", "|p-~-----~~~--|", "|~~~~-p--~----|"]
names2 = ["Meinrad", "Alois", "Hanspeter"]
calculator2 = PenguinRaceCalculator(snapshot2, names2, progress=0)
print("The race is: ", snapshot2)
print("Winners in the second race:", calculator2.get_winners())
print("")

# RACE 3
snapshot3 = ["|-p------~~---|", "|--~-----~~p--|", "|~~~~p---~----|"]
names3 = ["Kaspar", "Jürg", "Urs"]
calculator3 = PenguinRaceCalculator(snapshot3, names3, progress=0)
print("The race is: ", snapshot3)
print("Winners i:", calculator1.get_winners())
