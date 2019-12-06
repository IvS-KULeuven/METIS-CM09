# Python scripts to interface with the PLC

## Setting up python environment

+ Install Anaconda
+ Create a new anaconda enviroment with python 3.7

```bash
conda create -n CM09 python=3.7
```

+ Activate the new environment

```bash
conda activate CM09
```

+ Install python asyncua to interface with the PLC using OPC UA

```bash
pip install asyncua
```

## Getting information on the available variables on the PLC

```bash
uals -u opc.tcp://169.254.1.70:4840
```

```bash
Browsing node Node(NumericNodeId(i=84)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                Value

LocalizedText(Encoding:3, Locale:en, Text:Views) i=87                      0:Views
LocalizedText(Encoding:3, Locale:en, Text:Objects) i=85                    0:Objects
LocalizedText(Encoding:3, Locale:en, Text:Types) i=86                      0:Types
```

The interesting information is in i=85 (0:Objects)

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85'
```

```bash
Browsing node Node(NumericNodeId(i=85)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                Value

LocalizedText(Encoding:3, Locale:en, Text:Server) i=2253                    0:Server
LocalizedText(Encoding:3, Locale:, Text:DeviceSet) ns=2;i=5001              2:DeviceSet
LocalizedText(Encoding:3, Locale:, Text:PLC1) ns=1;s=PLC1                   4:PLC1
LocalizedText(Encoding:3, Locale:en, Text:Configuration) ns=6;i=16          6:Configuration
```

All our variables are in PLC1

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1'
```

```bash
Browsing node Node(StringNodeId(ns=1;s=PLC1)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                    Value

LocalizedText(Encoding:3, Locale:, Text:DeviceManual) ns=1;s=PLC1.DeviceManual         2:DeviceManual           ,
LocalizedText(Encoding:3, Locale:, Text:DeviceRevision) ns=1;s=PLC1.DeviceRevision     2:DeviceRevision         ,
LocalizedText(Encoding:3, Locale:, Text:HardwareRevision) ns=1;s=PLC1.HardwareRevision 2:HardwareRevision       ,
LocalizedText(Encoding:3, Locale:, Text:Manufacturer) ns=1;s=PLC1.Manufacturer         2:Manufacturer           , LocalizedText(Encoding:3, Locale:, Text:Beckhoff)
LocalizedText(Encoding:3, Locale:, Text:Model) ns=1;s=PLC1.Model                       2:Model                  , LocalizedText(Encoding:0, Locale:None, Text:None)
LocalizedText(Encoding:3, Locale:, Text:RevisionCounter) ns=1;s=PLC1.RevisionCounter   2:RevisionCounter        , 0  
LocalizedText(Encoding:3, Locale:, Text:SerialNumber) ns=1;s=PLC1.SerialNumber         2:SerialNumber           ,
LocalizedText(Encoding:3, Locale:, Text:SoftwareRevision) ns=1;s=PLC1.SoftwareRevision 2:SoftwareRevision       ,
LocalizedText(Encoding:3, Locale:, Text:Programs) ns=1;s=PLC1.Programs                 3:Programs
LocalizedText(Encoding:3, Locale:, Text:Tasks) ns=1;s=PLC1.Tasks                       3:Tasks
LocalizedText(Encoding:3, Locale:en, Text:MAIN) ns=4;s=MAIN                            4:MAIN
LocalizedText(Encoding:3, Locale:, Text:DeviceState) ns=4;i=20737                      4:DeviceState
```

All the information is in the MAIN method (ns=4)

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1','4:MAIN'
```

```bash
Browsing node Node(StringNodeId(ns=4;s=MAIN)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                Value

LocalizedText(Encoding:3, Locale:, Text:Stepper001) ns=4;s=MAIN.Stepper001    4:Stepper001
LocalizedText(Encoding:3, Locale:, Text:Lamp001) ns=4;s=MAIN.Lamp001          4:Lamp001
LocalizedText(Encoding:3, Locale:, Text:Lamp002) ns=4;s=MAIN.Lamp002          4:Lamp002
LocalizedText(Encoding:3, Locale:, Text:IOPT100) ns=4;s=MAIN.IOPT100          4:IOPT100
```

We are interested in the IOPT100 (IO for PT100 sensors)

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1','4:MAIN','4:IOPT100'
```

```bash
Browsing node Node(StringNodeId(ns=4;s=MAIN.IOPT100)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                        Value

LocalizedText(Encoding:3, Locale:, Text:RPC_Reset) ns=4;s=MAIN.IOPT100#RPC_Reset           4:RPC_Reset
LocalizedText(Encoding:3, Locale:, Text:RPC_SetDebug) ns=4;s=MAIN.IOPT100#RPC_SetDebug     4:RPC_SetDebug
LocalizedText(Encoding:3, Locale:, Text:RPC_SetOutputs) ns=4;s=MAIN.IOPT100#RPC_SetOutputs 4:RPC_SetOutputs
LocalizedText(Encoding:3, Locale:, Text:RPC_Stop) ns=4;s=MAIN.IOPT100#RPC_Stop             4:RPC_Stop
LocalizedText(Encoding:3, Locale:, Text:RPC_SetLog) ns=4;s=MAIN.IOPT100#RPC_SetLog         4:RPC_SetLog
LocalizedText(Encoding:3, Locale:, Text:RPC_Disable) ns=4;s=MAIN.IOPT100#RPC_Disable       4:RPC_Disable
LocalizedText(Encoding:3, Locale:, Text:RPC_Enable) ns=4;s=MAIN.IOPT100#RPC_Enable         4:RPC_Enable
LocalizedText(Encoding:3, Locale:, Text:RPC_Init) ns=4;s=MAIN.IOPT100#RPC_Init             4:RPC_Init
LocalizedText(Encoding:3, Locale:en, Text:cfg) ns=4;s=MAIN.IOPT100.cfg                     4:cfg
LocalizedText(Encoding:3, Locale:en, Text:info) ns=4;s=MAIN.IOPT100.info                   4:info
LocalizedText(Encoding:3, Locale:en, Text:ctrl) ns=4;s=MAIN.IOPT100.ctrl                   4:ctrl
LocalizedText(Encoding:3, Locale:en, Text:stat) ns=4;s=MAIN.IOPT100.stat                   4:stat
```

We see the RPC calls here that can be used to control the device. The sensors are enabled at the start of the PLC, so we don't need to do something here. The information is in stat.

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1','4:MAIN','4:IOPT100','4:stat'
```

```bash
Browsing node Node(StringNodeId(ns=4;s=MAIN.IOPT100.stat)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                           Value

LocalizedText(Encoding:3, Locale:, Text:bLocal) ns=4;s=MAIN.IOPT100.stat.bLocal               4:bLocal                 , False
LocalizedText(Encoding:3, Locale:, Text:nState) ns=4;s=MAIN.IOPT100.stat.nState               4:nState                 , 2  
LocalizedText(Encoding:3, Locale:, Text:nSubstate) ns=4;s=MAIN.IOPT100.stat.nSubstate         4:nSubstate              , 200
LocalizedText(Encoding:3, Locale:, Text:nErrorCode) ns=4;s=MAIN.IOPT100.stat.nErrorCode       4:nErrorCode             , 0  
LocalizedText(Encoding:3, Locale:, Text:nLastCommand) ns=4;s=MAIN.IOPT100.stat.nLastCommand   4:nLastCommand           , 0  
LocalizedText(Encoding:3, Locale:, Text:nRpcErrorCode) ns=4;s=MAIN.IOPT100.stat.nRpcErrorCode 4:nRpcErrorCode          , 0  
LocalizedText(Encoding:3, Locale:, Text:nStatus) ns=4;s=MAIN.IOPT100.stat.nStatus             4:nStatus                , 0  
LocalizedText(Encoding:3, Locale:, Text:sState) ns=4;s=MAIN.IOPT100.stat.sState               4:sState                 , OPERATIONAL
LocalizedText(Encoding:3, Locale:, Text:sSubstate) ns=4;s=MAIN.IOPT100.stat.sSubstate         4:sSubstate              , MONITORING
LocalizedText(Encoding:3, Locale:, Text:sErrorText) ns=4;s=MAIN.IOPT100.stat.sErrorText       4:sErrorText             , OK
LocalizedText(Encoding:3, Locale:, Text:sRPCErrorText) ns=4;s=MAIN.IOPT100.stat.sRPCErrorText 4:sRPCErrorText          , OK
LocalizedText(Encoding:3, Locale:, Text:sStatus) ns=4;s=MAIN.IOPT100.stat.sStatus             4:sStatus                , OK
LocalizedText(Encoding:3, Locale:, Text:sLastCommand) ns=4;s=MAIN.IOPT100.stat.sLastCommand   4:sLastCommand           , NONE
LocalizedText(Encoding:3, Locale:, Text:sLibVersion) ns=4;s=MAIN.IOPT100.stat.sLibVersion     4:sLibVersion            , 1.1.0.1
LocalizedText(Encoding:3, Locale:, Text:sActionDesc) ns=4;s=MAIN.IOPT100.stat.sActionDesc     4:sActionDesc            , ActivityMonitoring
LocalizedText(Encoding:3, Locale:, Text:sEventDesc) ns=4;s=MAIN.IOPT100.stat.sEventDesc       4:sEventDesc             ,
LocalizedText(Encoding:3, Locale:, Text:nCycleCounter) ns=4;s=MAIN.IOPT100.stat.nCycleCounter 4:nCycleCounter          , 822808
LocalizedText(Encoding:3, Locale:en, Text:arrPT100) ns=4;s=MAIN.IOPT100.stat.arrAI            4:arrAI
```

The values of the PT100 sensors is in arrPT100.

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1','4:MAIN','4:IOPT100','4:stat','4:arrAI'
```

```bash
Browsing node Node(StringNodeId(ns=4;s=MAIN.IOPT100.stat.arrAI)) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                       Value

LocalizedText(Encoding:3, Locale:, Text:arrAI[0]) ns=4;s=MAIN.IOPT100.stat.arrAI[0]     4:arrAI[0]
LocalizedText(Encoding:3, Locale:, Text:arrAI[1]) ns=4;s=MAIN.IOPT100.stat.arrAI[1]     4:arrAI[1]
```

These are the two sensors. The temperature we are interested in is the first one.

```bash
uals -u opc.tcp://169.254.1.70:4840 -n 'i=85' -p '4:PLC1','4:MAIN','4:IOPT100','4:stat','4:arrAI','4:arrAI[0]'
```

```bash
Browsing node Node(StringNodeId(ns=4;s=MAIN.IOPT100.stat.arrAI[0])) at opc.tcp://169.254.1.70:4840

DisplayName                    NodeId                    BrowseName                                   Value

LocalizedText(Encoding:3, Locale:, Text:nConversion) ns=4;s=MAIN.IOPT100.stat.arrAI[0].nConversion 4:nConversion            , 2  
LocalizedText(Encoding:3, Locale:, Text:lrPar1) ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrPar1           4:lrPar1                 , 0.01
LocalizedText(Encoding:3, Locale:, Text:lrPar2) ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrPar2           4:lrPar2                 , 0.0
LocalizedText(Encoding:3, Locale:, Text:lrPar3) ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrPar3           4:lrPar3                 , 0.0
LocalizedText(Encoding:3, Locale:, Text:nValue) ns=4;s=MAIN.IOPT100.stat.arrAI[0].nValue           4:nValue                 , 2568
LocalizedText(Encoding:3, Locale:, Text:lrValueUser) ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrValueUser 4:lrValueUser            , 25.68
```

lrValueUser shows the temperature. In our python script, we need to use **ns=4;s=MAIN.IOPT100.stat.arrAI[0].lrValueUser**

## Getting information on the variable types (needed for calling a method)

```bash
$ uals -u opc.tcp://169.254.1.70:4840 -n 'i=86' -d 5 2>/dev/null | grep 'i=7 '
        LocalizedText(Encoding:3, Locale:, Text:UInt32) i=7                       0:UInt32                 
```

To create a UInt variable in python

```python
ua.Variant(0, ua.VariantType.UInt32)
```
