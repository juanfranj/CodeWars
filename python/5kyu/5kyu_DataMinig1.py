
class Datamining:

    def __init__(self, train_set):

        self.N = len(train_set)
        self.x = [point[0] for point in train_set]
        self.y = [point[1] for point in train_set]
        #self.xy = [point[0]*point[1] for point in zip(self.x,self.y)]
        self.xy = [point[0]*point[1] for point in train_set]
        self.x2 = [point[0]*point[0] for point in train_set]
        self.mediax = sum(self.x)/(self.N)
        self.mediay = sum(self.y)/(self.N)
        #coeficientes de recta de regresion y = a + bx
        self.b = self.calculoCoeficienteB()
        self.a = self.calculoCoeficienteA()


    def predict(self, x):
        y = self.a + (self.b * x)
        return y

    def calculoCoeficienteB(self):
        b = (sum(self.xy)-(sum(self.x)*sum(self.y)/self.N))/(sum(self.x2)-(sum(self.x)*sum(self.x)/self.N))
        return b
    def calculoCoeficienteA(self):
        a = self.mediay-(self.mediax * self.b)
        return a


if __name__ == '__main__':
    example_train_set = [(8, 3),
    (2, 10),
    (11, 3),
    (6, 6),
    (5, 8),
    (4,12),
    (12,1),
    (9,4),
    (6,9),
    (1,14)
    ]

    dm = Datamining(example_train_set)
    predicted = [round(dm.predict(point[0]),2) for point in example_train_set]
    print("\n-------Solucion al problema de aproximacion lineal--------")
    for i in zip(example_train_set, predicted):
        print(f"X: {i[0][0]}, Y: {i[0][1]}, Ypred: {i[1]}")
    print("----------------------------------------------------------")
    #print(predicted)
    #print(a.N,sum(a.x), sum(a.y), sum(a.xy), sum(a.x2), a.mediax, a.mediay, a.b, a.a)

    
