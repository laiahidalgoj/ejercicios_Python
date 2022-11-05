import pickle

class Vehicle:
    model = ''
    price = 0.0

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def getModel(self):
        return self.model

    def getPrice(self):
        return self.price


audiQ3 = Vehicle('AudiQ3', 60000)

f = open('data.bin', 'wb')
pickle.dump(audiQ3, f)
f.close()

f = open('data.bin', 'rb')
audi = pickle.load(f)
f.close()

print(audi.getModel(), audi.getPrice())



