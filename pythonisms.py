class myShoppingList:
    def __init__(self):
        self.shoppingList = []
        self.current = 0
    
    def addItem(self, name, count, price):
        self.shoppingList.append(shoppingItem(name, count, price))
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.shoppingList):
            item = self.shoppingList[self.current]
            amount = int(item.count) * float(item.price)
            self.current+=1
            return amount
        else:
            self.current = 0
            raise StopIteration

def mother_visiting(amount):
    return_string = "You spent a whole $" + str(amount) + " and couldn't even bother to find something that was on sale?"
    return return_string

def self_care(amount):
    return_string = "Meh, $" + str(amount) + " isn't that much to spend and you're worth it!"
    return return_string

def is_it_worth_it(func, shopping_list):
    for item_amount in shopping_list:
        inner_dialogue = func(item_amount)
        print(inner_dialogue)



class shoppingItem:
    def __init__(self, name, count, price):
        self.name = name
        self.count = count
        self.price = price


if __name__ == "__main__":
    yankeeCandle = myShoppingList()
    yankeeCandle.addItem("rose candle", 2, 15.99)
    yankeeCandle.addItem("sandlewood", 1, 12.99)
    yankeeCandle.addItem("bubble bath", 3, 9.99)
    is_it_worth_it(mother_visiting, yankeeCandle)
    is_it_worth_it(self_care, yankeeCandle)