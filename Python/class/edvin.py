class Student():
    def __init__ (self, name, age, year, rabota):
        self.name = name
        self.age = age
        self.year = year
        self.rabota = rabota
    def info(self):
        print( "Имя: " + self.name )
        print( "Возраст: " + str( self.age ) )
        print( "Курс: " + str( self.year) )
        print( "Проффесия: " + self.rabota )
    def sleep(self):
        print( self.name + ", лег(-ла) спать..." )
        print( self.name + " выспался(-ась)." )
        
studend = Student( "EdvinGay",18,3,"Programmer" )
studend.sleep()
studend.info()
