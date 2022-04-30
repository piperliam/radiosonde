#balloon calculator ooga booga
#4/30/2022

#this is the balloon data setup



class Balloon:
    def __init__(self,name,mass,burstdiameter,coeffofdrag):
        self.name = name
        self.mass = mass
        self.burstdiameter = burstdiameter
        self.coeffofdrag = coeffofdrag



#this defines the balloon data
B1 = Balloon("Totex100",100,1.96,0.25)
B2 = Balloon("Totex200",200,3,0.25)
B3 = Balloon("Totex300",300,3.78,0.25)
B4 = Balloon('Totex350',350,4.12,0.25)
B5 = Balloon('Totex450',450,4.72,0.25)
B6 = Balloon('Totex500',500,4.99,0.25)
B7 = Balloon('Totex600',600,6.02,0.3)
B8 = Balloon('Totex700',700,6.53,0.3)
B9 = Balloon('Totex800',800,7,0.3)
B10 = Balloon('Totex1000',1000,7.86,0.3)
B11 = Balloon('Totex1200',1200,8.63,0.25)
B12 = Balloon('Totex1500',1500,9.44,0.25)
B13 = Balloon('Totex2000',2000,10.54,0.25)
B14 = Balloon('Totex3000',3000,13,0.25)

#hwotee balloon
B15 = Balloon('Hwoyee100',100,2,0.25)
B16 = Balloon('Hwoyee200',200,2.97,0.25)
B17 = Balloon('Hwoyee300',300,4.3,0.25)
B18 = Balloon('Hwoyee350',350,4.8,0.25)
B19 = Balloon('Hwoyee500',500,5.8,0.25)
B20 = Balloon('Hwoyee600',600,6.5,0.3)
B21 = Balloon('Hwoyee750',750,6.9,0.3)
B22 = Balloon('Hwoyee800',800,7,0.3)
B23 = Balloon('Hwoyee1000',1000,8,0.3)
B24 = Balloon('Hwoyee1200',1200,9.1,0.25)
B25 = Balloon('Hwoyee1600',1600,10,0.25)
B26 = Balloon('Hwoyee2000',2000,10,0.25)
B27 = Balloon('Hwoyee3000',3000,12,0.25)

#Pawan balloons
B28 = Balloon('Pawan100',100,1.85,0.25)
B29 = Balloon('Pawan350',350,4,0.25)
B30 = Balloon('Pawan600',600,5.8,0.3)
B31 = Balloon('Pawan800',800,6.6,0.3)
B32 = Balloon('Pawan900',900,7,0.3)
B33 = Balloon('Pawan1200',1200,8,0.25)
B34 = Balloon('Pawan1600',1600,9.5,0.25)
B35 = Balloon('Pawan2000',2000,10.2,0.25)

print('Hello zoomers, this is my awful balloon calculator for burst and rise speed and some other stuff, I ask you not to look too closely at this')

print('___________________________________________________________________________________________________')

#this prints out the information of the balloon
print('Here is the list of balloons, their # value is the # on the list:')
print('\/ B1-B14')
print(B1.name,B2.name,B3.name,B4.name,B5.name,B6.name,B7.name,B8.name,B9.name,B10.name,B11.name,B12.name,B13.name,B14.name)
print("\/ B15-B27")
print(B15.name,B16.name,B17.name,B18.name,B19.name,B20.name,B21.name,B22.name,B23.name,B24.name,B25.name,B26.name,B27.name)
print('\/ B28-B35')
print(B28.name,B29.name,B30.name,B31.name,B32.name,B33.name,B34.name,B35.name)
print('___________________________________________________________________________________________________')


#now testing calculatorns
#h = 4 * B1.mass
#print(h)


#gas data
#lift at stp
#mass per mole (kg/mol)
#molecular mass (kg)
#r spepefitic (J/kgK)
class Gas:
    def __init__(self,name,liftstp,masspmole,molecularmass,Rspecific):
        self.name = name
        self.liftstp = liftstp
        self.masspmole = masspmole
        self.molecularmass = molecularmass
        self.Rspecific = Rspecific
G1 = Gas('Helium',1.046,4.002602*10**-3,6.646*10**-27,2077.26)
G2 = Gas('Hydrogen',1.135,2.01588*10**-3,3.3474*10**-27,4124.48)

#constants
#0c in K
KCo = 273.1
#Accelration due to gravity
g = 9.807
#Gas Constant
Rc = 8.3144598

#__________________________________________________________________________________
#inputs
Balloontype = input('What type of balloon?')
BYT = Balloontype

print('Payload mass [g]:')
payloadmass = pM = input()
print(pM)

print('Launch Altitude [m]:')
launchaltitude = La = input()
print(La)

print('Type of gas? (He,H2):')
Gastype = GT = Gt = input()
print(Gt)

print('Temp at Launch [c]:')
TempL = Tl = input()
TLm = 10.5 #erm this is the model temp
print(Tl)

print('Pressure at Launch [kPa]:')
PressL = Pl = input()
PLm = 93.3 #model pressure @ launch
print(Pl)

print('Atmospheric density at Launch:')
DensityL = aDL = input()
aDLm = 1.146 #model atmospheric density at launch
print(aDL)

#ok now this is intresting #also this could be a problem in the below calculation
BMPli = input('Use normal Balloon Membrane Pressure @Launch?:')
if BMPli == ('yes') or BMPli == ('Yes'):
    BMPl = 0.150;
elif BMPli == ('no') or BMPli == ('No'):
     print('Ok then you boomer tellme cval')
     BMPlui = input()
     BMPl = BMPlui
#oh yeah balloon pressure at burst should be 0
BMPB = 0
#calculations:::::::::::::::::::::::::::::::::::::::::::::::::::


class BalloonInput:
    def __init__(self,massq,burstdiameterq,coeffofdragq):
        self.massq = massq
        self.burstdiameterq = burstdiameterq
        self.coeffofdragq = coeffofdragq
        
Balloontype.mass




#I think the data should be stored in a dictionary





print("Bm",Balloon.BYT.mass)


TM = pM + Bm




if GT == 'He' or 'he': 
    gasname = 'Helium'
    lift = 1.046 #liftstp
    mpm = 4.002602*10**-3 #masspmole
    mm = 6.646*10**-27 # molecularmass
    Rs = 2077.26 #Rspecific
elif GT == 'H2' or 'h2': 
    gasname = 'Hydrogen'
    lift = 1.135 #liftstp
    mpm = 2.01588*10**-3 #masspmole
    mm = 3.3474*10**-27 # molecularmass
    Rs = 4124.48 #Rspecific
#print(mpm) #ok this returns an error

#conversion moment
BMPl = float(BMPl)
Tl = float(Tl)
Pl = float(Pl)
BMPB = float(BMPB)


# C25
#Balloon Gas density at Launch: BGDl
BGDl = ((Pl+BMPl)*1000)*mpm/(Rc*(Tl+KCo))
print('BGDl',BGDl)

#C26
BurstA = input('What would you like the Burst altituide to be? [m]:')

#C27
BD = BYT.burstdiameter

#C28


#C29


#C30


#C31


#C32


#C33


#C34


#C35


#C36


#C37


#C38


#C39


#C40


#C41







