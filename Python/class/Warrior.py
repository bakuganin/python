"""Модуль содержит классы воинов"""
import random
import time
class Warrior():
    """Класс Воин.
Конструктор принимает данные имен лет и рассы"""
    def __init__ (self, name, age, race):
       
        self.name = name
        self.age = age
        self.race = race
        self.healthy = 100
        self.unhealthy = 20
       
    def info(self):
        """Инструкция для вывода характеристик воина."""
        time.sleep(0.6)
        print( "Имя: " + self.name )
        time.sleep(0.8)
        print( "Возраст: " + str( self.age ) )
        time.sleep(0.7)
        print( "Раса: " + self.race )
        time.sleep(0.8)
        print( "Здоровье: " + str( self.healthy ) )
        time.sleep(0.6)
        print()
           

    def fight(self):
        
        """Инструкция для вычисления рандомного удара."""
        rando = random.randint(1,2)
        x = rando
        
        if x == 1:
            print( "<----------------------------------------------->" )
            time.sleep(0.6)
            print( voin1.name, ", наносит удар игроку:", voin2.name )
            time.sleep(0.7)
            print( "14%" )
            time.sleep(0.9)
            print( "48%" )
            time.sleep(0.6)
            print( "100%" )
            voin2.healthy -= self.unhealthy
            time.sleep(0.8)
            print( "Здоровье " + voin2.name + " отнялось на: " + str( self.unhealthy ) )
            print()
            time.sleep(0.7)
            print( "Текущее здоровье " + voin2.name + ": " + str( voin2.healthy ) )
            print( "<----------------------------------------------->" )
            time.sleep(0.6)
            
            if voin2.healthy == 0:
                print("Здоровье игрока " + voin2.name + " закончилось!")
                time.sleep(0.7)
                print()
                time.sleep(0.7)
                print("Победил: " + voin1.name + " со здровьем: " + str( voin1.healthy ) )
                time.sleep(0.7)
                print()
                print("Нажмите \"ENTER\" чтобы завершить сеанс.")
                input()
                exit()
               
        elif x == 2:
            print( "<----------------------------------------------->" )
            time.sleep(0.6)
            print( voin2.name , ", наносит удар игроку:" , voin1.name )
            time.sleep(0.7)
            print( "14%" )
            time.sleep(0.9)
            print( "48%" )
            time.sleep(0.6)
            print( "100%" )
            voin1.healthy -= self.unhealthy
            time.sleep(0.8)
            print( "Здоровье " + voin1.name + " отнялось на: " + str( self.unhealthy ) )
            print()
            time.sleep(0.7)
            print( "Текущее здоровье " + voin1.name + ": " + str( voin1.healthy ) )
            print( "<----------------------------------------------->" )
            time.sleep(0.6)

            if voin1.healthy == 0:
                print("Здоровье игрока " + voin1.name + " закончилось!")
                time.sleep(0.7)
                print()
                time.sleep(0.7)
                print("Победил: " + voin2.name + " со здровьем: " + str( voin2.healthy ) )
                time.sleep(0.7)
                print()
                print("Нажмите \"ENTER\" чтобы завершить сеанс.")
                input()
                exit()
        else:
            print("Такого варианта нет.")
            exit()
           
"""Входные данные"""        
voin1 = Warrior( "Egor", 18, "Воин Омута" )
voin2 = Warrior( "Чепушила", 50, "Чернокнижник" )
"""Для тех кто не в теме в консколь надо писать voin1.fight() или voin2.fight()""" 
