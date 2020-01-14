import time
class Student():
    
    def __init__ (self, name, age, year, job):
        
        self.name = name
        self.age = age
        self.year = year
        self.job = job
        self.stamina = 100
        
    def info(self):
        
        time.sleep(0.6)
        print( "Имя: " + self.name )
        time.sleep(0.8)
        print( "Возраст: " + str( self.age ) )
        time.sleep(0.7)
        print( "Курс: " + str( self.year) )
        time.sleep(0.7)
        print( "Проффесия: " + self.job )
        time.sleep(0.8)
        print( "Стамина: " + str( self.stamina ) )
        time.sleep(0.6)
        print()
            
    def study(self):
        
        if self.stamina == 0:
            time.sleep(0.6)
            print( "Стамина: ", str(self.stamina) )
            time.sleep(0.6)
            print( "Идите спать, ваша энергия закончилась!" )
        else:
            
            if self.stamina >= 21:
                
                time.sleep(0.6)
                print( self.name + ", пошел учиться." )
                time.sleep(0.4)
                print( "10%" )
                time.sleep(0.7)
                print( "43%" )
                time.sleep(0.7)
                print( "74%" )
                time.sleep(0.6)
                print( "100%" )
                self.stamina -= 20
                time.sleep(0.7)
                print("Ваша стамина уменьшилась!")
                time.sleep(0.6)
                print( "Cтамина: ", str(self.stamina) )
                
            elif self.stamina == 20:
                
                time.sleep(0.6)
                print("Ваша стамина практически на 0, лучше идите спать!")
                time.sleep(0.9)
                print("Вы точно, желаете учится? (1) - Да, (2) - Нет")
                x = input()
                
                while True:
                    if x == "1":
                        
                        time.sleep(0.6)
                        print( self.name + ", пошел учиться." )
                        time.sleep(0.4)
                        print( "10%" )
                        time.sleep(0.7)
                        print( "43%" )
                        time.sleep(0.7)
                        print( "74%" )
                        time.sleep(0.6)
                        print( "100%" )
                        self.stamina -= 20
                        time.sleep(0.7)
                        print("Ваша стамина уменьшилась!")
                        time.sleep(0.7)
                        print( "Cтамина: ", str(self.stamina) )
                        break
                    
                    elif x == "2":
                        
                        print("Тогда идите спать!")
                        break
                    
                    else:
                        
                        print("Такого варианта ответа нет!")
                
    def endStudy(self):
        time.sleep(0.6)
        print( self.name + ", закончил(а) учиться и вернулся(-ась) домой." )

    def sleep(self):
        print( self.name + ", лег(-ла) спать..." )
        time.sleep(0.7)
        print( "14%" )
        time.sleep(0.9)
        print( "48%" )
        time.sleep(0.6)
        print( "100%" )
        time.sleep(0.6)
        print( self.name + " выспался(-ась)." )
        time.sleep(0.8)
        self.stamina = 100
        print( "Стамина: ", str(self.stamina) )
        
stud1 = Student( "Egor",18,3,"IT-Admin" )
print( "Привет! Мои комманды:" )
time.sleep(0.7)
print( "stud1.[sleep(), info(), study(), sleep()]" )
time.sleep(0.9)
print( "В течение n времени могут добавиться новые команды, если вам понравится :)" )
