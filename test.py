from propertytable import R134a


#################### Check for Temp Saturated Table####################

check_1=False

if check_1:
    print(R134a(Temperature=50))

###################### Check for Pressure Saturated Table  ###############

check_2=False

if check_2:
    print(R134a(Pressure=230))

#######################3 Check for Saturated liquid Temp ##################

check_3=False

if check_3:
    print(R134a(Temperature=40,Enthalpy=300))

####################### check for Saturated liquid Pressure ##############

check_4=False

if check_4:
    print(R134a(Pressure=1334,Enthalpy=223))

##################### check for Superheated Vapour #####################

check_5=False

pre=[60,100,140,180,200,240,280,320,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]

if check_5:
    print(R134a(Pressure=60,Superheated=True))

check_5_sub=False

if check_5_sub:
    for num in pre:
        print(R134a(Pressure=num,Superheated=True))


########################## Check for superheated pressure and Temperature#######

check_6=False

if check_6:
    print(R134a(Pressure=100,Temperature=95))

########################### Check for superheated pressure and enthalpy ##########

check_7=True

if check_7:
    print(R134a(Pressure=240,Enthalpy=331,Superheated=True))

########################### Check for superheated pressure and entropy ##########

check_8=False

if check_8:
    print(R134a(Pressure=400,Entropy=1.2,Superheated=True))

########################### Check for superheated pressure and specificvolume ##########

check_9=False

if check_9:
    print(R134a(Superheated=True,Pressure=400,specificvolume=0.06))