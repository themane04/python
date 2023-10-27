class Person:
    def __init__(self, name, age, mood, is_boss=None):
        self.name = name
        self.age = age
        self.mood = mood
        self.isboss = is_boss


class Boss(Person):
    def __init__(self, name, age, mood):
        self.subordinates = []
        super().__init__(name, age, mood, is_boss=True)

    def list_workers(self):
        print(f"The boss is: {self.name} and he is {self.mood}")
        woker_info = [{'Worker Name': worker.name, 'Work Done': worker.work_done, 'Mood': worker.mood} for worker in
                      self.subordinates]
        return woker_info


class Worker(Person):
    def __init__(self, name, age, mood):
        self.work_done = 0
        super().__init__(name, age, mood, is_boss=False)

    def work(self, amount):
        self.work_done += amount


boss_instance = Boss("Mark", 53, "happy")
worker1 = Worker("John", 44, "tired")
worker2 = Worker("Tim", 31, "dead")

worker1.work(-30)
worker2.work(60)

boss_instance.subordinates.append(worker1)
boss_instance.subordinates.append(worker2)

worker_info = boss_instance.list_workers()
print("Worker 1", worker_info[0])
print("Worker 2", worker_info[1])
