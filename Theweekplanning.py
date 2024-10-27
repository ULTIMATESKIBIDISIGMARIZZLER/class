class planning:
    maandag=7
    dinsdag=8
    woensdag=8
    donderdag=7
    vrijdag=6

    def __init__(self, maandag, dinsdag, woensdag, donderdag, vrijdag):
        self.maandag=maandag
        self.dinsdag=dinsdag
        self.woensdag=woensdag
        self.donderdag=donderdag
        self.vrijdag=vrijdag
        print("Making a new weekinfo.")
        
        #methode-function
        #methode for showing details
    def showDetails(self):
            print("weekplanning:")
            print("maandag is",self.maandag)
            print("dinsdag is",self.dinsdag)
            print("woensdag is",self.woensdag)
            print("donderdag is",self.donderdag)
            print("vrijdag is",self.vrijdag)
            
#input
studentM=input("Your dayschedule(maandag)?")
studentD=input("Your dayschedule(dinsdag)?")
studentW=input("Your dayschedule(woensdag)?")
studentD=input("Your dayschedule(donderdag)?")
studentV=input("Your dayschedule(vrijdag)?")

     #object
weekend=planning(studentM, studentD, studentW, studentD, studentV)
print(weekend)
print(weekend.showDetails())

list=[]
list.append(studentM)
print(list)















