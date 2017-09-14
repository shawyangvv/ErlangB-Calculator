import decimal
import math
decimal.getcontext().prec = 100

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def erlangb_s(a,b):
    denominator=decimal.Decimal(0)
    for r in range(0, serverNum):
        denominator = denominator + (load ** r) / math.factorial(r)
    numerator=decimal.Decimal(0)
    numerator = (load ** serverNum) / math.factorial(serverNum)
    return numerator/denominator


load = float(input("Input the load: "))
load = str(load)
load=decimal.Decimal(load)
qos = float(input("Input the Qos: "))
qos = str(qos)
qos=decimal.Decimal(qos)
serverNum=2975;
while(erlangb_s(load,serverNum)>qos):
    currentQos = float(erlangb_s(load,serverNum))
    print ("With %d Servers current QoS: %.4f" %(serverNum,currentQos))
    serverNum=serverNum+1
else:
    currentQos = float(erlangb_s(load, serverNum))
    print ("With %d Servers current QoS: %.4f" %(serverNum,currentQos))

