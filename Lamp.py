from asyncua.sync import Client
from asyncua import ua
import asyncio
import time

# Get Temperature
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrValueUser').get_value())

# Initialize the lamp
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())
    parent = client.get_node('ns=4;s=MAIN.Lamp001')
    method = parent.get_child("4:RPC_Init")
    # Show the needed input arguments
    inputs = method.get_child("0:InputArguments").get_value()
    arguments = []
    res = parent.call_method(method, *arguments)
    # Wait for 1 second
    time.sleep(1)
    # Show status
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())

# Enable the lamp
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())
    parent = client.get_node('ns=4;s=MAIN.Lamp001')
    method = parent.get_child("4:RPC_Enable")
    # Show the needed input arguments
    inputs = method.get_child("0:InputArguments").get_value()
    arguments = []
    res = parent.call_method(method, *arguments)
    # Wait for 1 second
    time.sleep(1)
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())

# Turn Lamp on
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())
    parent = client.get_node('ns=4;s=MAIN.Lamp001')
    method = parent.get_child("4:RPC_On")
    #inputs = method.get_child("0:InputArguments").get_value()
    #print(inputs)
    arguments = [100.0, ua.Variant(0, ua.VariantType.UInt32)]
    res = parent.call_method(method, *arguments)
    # Wait for 1 second
    time.sleep(1)
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())

# Get status of lamp
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())

# Get time on and time off of lamp
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.nTimeOn').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.nTimeOff').get_value())

# Turn lamp off
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())
    parent = client.get_node('ns=4;s=MAIN.Lamp001')
    method = parent.get_child("4:RPC_Off")
    #inputs = method.get_child("0:InputArguments").get_value()
    #print(inputs)
    arguments = []
    res = parent.call_method(method, *arguments)
    # Wait for 1 second
    time.sleep(1)
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Lamp001.stat.sSubstate').get_value())


# Initialize motor
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    parent = client.get_node('ns=4;s=MAIN.Stepper001')
    method = parent.get_child("4:RPC_Init")
    #inputs = method.get_child("0:InputArguments").get_value()
    #print(inputs)
    arguments = []
    res = parent.call_method(method, *arguments)

# Initialize motor
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    parent = client.get_node('ns=4;s=MAIN.Stepper001')
    method = parent.get_child("4:RPC_Enable")
    #inputs = method.get_child("0:InputArguments").get_value()
    #print(inputs)
    arguments = []
    res = parent.call_method(method, *arguments)

# Move motor in Velocity
with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
    print(client.get_node('ns=4;s=MAIN.Stepper001.stat.sState').get_value())
    print(client.get_node('ns=4;s=MAIN.Stepper001.stat.sStatus').get_value())
    print(client.get_node('ns=4;s=MAIN.Stepper001.stat.sSubstate').get_value())
    parent = client.get_node('ns=4;s=MAIN.Stepper001')
    method = parent.get_child("4:RPC_MoveVel")
    #inputs = method.get_child("0:InputArguments").get_value()
    #print(inputs)
    arguments = [20.0]
    res = parent.call_method(method, *arguments)

# Blink lamp1 every 5 seconds
while True:
    with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
        parent = client.get_node('ns=4;s=MAIN.Lamp001')
        method = parent.get_child("4:RPC_On")
        arguments = [100.0, ua.Variant(0, ua.VariantType.UInt32)]
        res = parent.call_method(method, *arguments)
        # Wait for 1 second
        time.sleep(5)
        method = parent.get_child("4:RPC_Off")
        arguments = []
        res = parent.call_method(method, *arguments)
        time.sleep(5)


# Blink lamp2 every 2 seconds
while True:
    with Client("opc.tcp://169.254.1.70:4840/freeopcua/server/") as client:
        parent = client.get_node('ns=4;s=MAIN.Lamp002')
        method = parent.get_child("4:RPC_On")
        arguments = [100.0, ua.Variant(0, ua.VariantType.UInt32)]
        res = parent.call_method(method, *arguments)
        # Wait for 1 second
        time.sleep(2)
        method = parent.get_child("4:RPC_Off")
        arguments = []
        res = parent.call_method(method, *arguments)
        time.sleep(2)
