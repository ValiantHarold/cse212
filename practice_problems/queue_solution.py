class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        value = self.queue.pop(0)
        return value

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result


class Uno_Queue:

    class Person:

        def __init__(self, name):
            self.name = name
            self.cards = 7

        def __str__(self):
            result = "{}:cards left {}".format(self.name, self.cards)
            return result

    def __init__(self):
        self.people = Queue()

    def add_person(self, name):
        person = Uno_Queue.Person(name)
        self.people.enqueue(person)

    def get_next_person(self):
        if self.people.is_empty():
            print("No one in the queue.")
        else:
            person = self.people.dequeue()
            card = input(f"{person}: ")

            if person.cards >= 1:
                person.cards -= 1
                if card == "s":
                    self.skip()
                elif card == "+2":
                    self.add_card(2)
                elif card == "+4":
                    self.add_card(4)
                self.people.enqueue(person)
                return False
            else:
                print(f"{person} won the game!")
                return True

    def __len__(self):
        return len(self.people)

    def __str__(self):
        return str(self.people)

    def skip(self):
        person = self.people.dequeue()
        self.people.enqueue(person)
        return person

    def add_card(self, num):
        person = self.skip()
        person.cards += num


print("Test 1")
players = Uno_Queue()
players.add_person("Bob")
players.add_person("Tim")
players.add_person("Sue")
players.add_person("Larry")
players.add_person("David")

winner = False
while not winner:
    winner = players.get_next_person()
