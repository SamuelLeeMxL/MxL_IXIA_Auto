if 'py' not in dir():
    class TestFailedError(Exception): pass
    class Py: pass
    py = Py()
    #ports = [('192.168.88.88', 2, 7), ('192.168.88.88', 2, 8)]
    py.ixTclServer = '127.0.0.1'
    py.ixTclPort = 8009

################################################################################
# Import the IxNet library
################################################################################
import IxNetwork
import time
import globals
import logging
import datetime
import os


################################################################################
# Logging function
################################################################################
filename = globals.str1
log_filename = datetime.datetime.now().strftime(filename + '_Forwarding_%Y-%m-%d_%H_%M_%S.log')
formatter = logging.Formatter('%(asctime)s %(levelname)-5s %(message)s')
logger = logging.getLogger('Forwarding:')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

handler1 = logging.FileHandler(log_filename)
handler1.setLevel(logging.INFO)
handler1.setFormatter(formatter)
logger.addHandler(handler1)

################################################################################
# IXIA port
################################################################################
IXIAip = '192.168.88.88'
chassis = 2
IXIAports = [""]
IXIAports.clear()
IXIAport = globals.str2
for i in range(0,len(IXIAport)):
    j = i + int(IXIAport[0])
    IXIAports.append([IXIAip, 2, j])
logger.info (IXIAports)

################################################################################
# Import the IxNet library
################################################################################
ixNet = IxNetwork.IxNet()

################################################################################
# Connect to IxNet client
################################################################################
ixNet.connect(py.ixTclServer, '-port', py.ixTclPort, '-version', '8.40')

class IXIA():
    def my_func(self, portspeed, mode):
        if mode == 'master':
            ################################################################################
            # Cleaning up IxNetwork
            ################################################################################
            logger.info ("Create a new config")
            ixNet.execute('newConfig')

            ################################################################################
            # Adding ports to configuration
            ################################################################################
            logger.info ("Adding ports to configuration")
            root = ixNet.getRoot()      #::ixNet::OBJ-/
            ixNet.add(root, 'vport')
            ixNet.add(root, 'vport')
            if len(IXIAport) == 4:
                ixNet.add(root, 'vport')
                ixNet.add(root, 'vport')
            ixNet.commit()
            vPorts = ixNet.getList(root, 'vport')
            vport1 = vPorts[0]                  #::ixNet::OBJ-/vport:1
            vport2 = vPorts[1]                  #::ixNet::OBJ-/vport:2
            if len(IXIAport) == 4:
                vport3 = vPorts[2]              #::ixNet::OBJ-/vport:3
                vport4 = vPorts[3]              #::ixNet::OBJ-/vport:4

            ################################################################################
            # Configuring Ethernet Endpoints
            ################################################################################
            logger.info ("Add topologies")
            ixNet.add(root, 'topology')
            ixNet.add(root, 'topology')
            if len(IXIAport) == 4:
                ixNet.add(root, 'topology')
                ixNet.add(root, 'topology')
            ixNet.commit()
            topo1 = ixNet.getList(root, 'topology')[0]          #::ixNet::OBJ-/topology:1
            topo2 = ixNet.getList(root, 'topology')[1]          #::ixNet::OBJ-/topology:2
            if len(IXIAport) == 4:
                topo3 = ixNet.getList(root, 'topology')[2]      #::ixNet::OBJ-/topology:3
                topo4 = ixNet.getList(root, 'topology')[3]      #::ixNet::OBJ-/topology:4
            logger.info ("Add ports to topologies")
            ixNet.setAttribute(topo1, '-vports', vport1)        #::ixNet::OBJ-/topology:1-vports::ixNet::OBJ-/vport:1
            ixNet.setAttribute(topo2, '-vports', vport2)        #::ixNet::OBJ-/topology:2-vports::ixNet::OBJ-/vport:2
            if len(IXIAport) == 4:
                ixNet.setAttribute(topo3, '-vports', vport3)    #::ixNet::OBJ-/topology:3-vports::ixNet::OBJ-/vport:3
                ixNet.setAttribute(topo4, '-vports', vport4)    #::ixNet::OBJ-/topology:4-vports::ixNet::OBJ-/vport:4
            ixNet.commit()
            logger.info ("Add device groups to topologies")
            ixNet.add(topo1, 'deviceGroup')
            ixNet.add(topo2, 'deviceGroup')
            if len(IXIAport) == 4:
                ixNet.add(topo3, 'deviceGroup')
                ixNet.add(topo4, 'deviceGroup')
            ixNet.commit()
            dg1 = ixNet.getList(topo1, 'deviceGroup')[0]        #::ixNet::OBJ-/topology:1/deviceGroup
            dg2 = ixNet.getList(topo2, 'deviceGroup')[0]        #::ixNet::OBJ-/topology:2/deviceGroup
            if len(IXIAport) == 4:
                dg3 = ixNet.getList(topo3, 'deviceGroup')[0]    #::ixNet::OBJ-/topology:3/deviceGroup
                dg4 = ixNet.getList(topo4, 'deviceGroup')[0]    #::ixNet::OBJ-/topology:4/deviceGroup
            logger.info ("Add Ethernet stacks to device groups")
            ixNet.add(dg1, 'ethernet')
            ixNet.add(dg2, 'ethernet')
            if len(IXIAport) == 4:
                ixNet.add(dg3, 'ethernet')
                ixNet.add(dg4, 'ethernet')
            ixNet.commit()
            mac1 = ixNet.getList(dg1, 'ethernet')[0]            #::ixNet::OBJ-/topology:1/deviceGroup:1/ethernet
            mac2 = ixNet.getList(dg2, 'ethernet')[0]            #::ixNet::OBJ-/topology:2/deviceGroup:1/ethernet
            if len(IXIAport) == 4:
                mac3 = ixNet.getList(dg3, 'ethernet')[0]        #::ixNet::OBJ-/topology:3/deviceGroup:1/ethernet
                mac4 = ixNet.getList(dg4, 'ethernet')[0]        #::ixNet::OBJ-/topology:4/deviceGroup:1/ethernet

            ################################################################################
            # Configure Ethernet Traffic
            ################################################################################
            logger.info ("Creating Traffic for Ethernet")
            ixNet.add(root + 'traffic', 'trafficItem')
            if len(IXIAport) == 4:
                ixNet.add(root + 'traffic', 'trafficItem')
            ixNet.commit()
            
            trafficItem = ixNet.getList(root + 'traffic', 'trafficItem')[0]         #::ixNet::OBJ-/traffic/trafficItem:1
            if len(IXIAport) == 4:
                trafficItem2 = ixNet.getList(root + 'traffic', 'trafficItem')[1]    #::ixNet::OBJ-/traffic/trafficItem:2
            
            ixNet.setMultiAttribute( trafficItem,
                    '-name'                 ,'Traffic Ethernet',
                    '-trafficType'          ,'ethernetVlan',
                    '-allowSelfDestined'    ,False,
                    '-trafficItemType'      ,'L2L3',
                    '-mergeDestinations'    ,True,
                    '-egressEnabled'        ,False,
                    '-srcDestMesh'          ,'oneToOne',  #manyToMany, oneToOne
                    '-enabled'              ,True,
                    '-routeMesh'            ,'oneToOne',    #fullMesh, oneToOne
                    '-transmitMode'         ,'interleaved',
                    '-biDirectional'        ,True,
                    '-hostsPerNetwork'      ,1)
            ixNet.commit()
            
            ixNet.setAttribute(trafficItem, '-trafficType', 'ethernetVlan')
            ixNet.commit()
            ixNet.add(trafficItem, 'endpointSet',
                    '-sources',             mac1,
                    '-destinations',        mac2,
                    '-name',                'ep-set1',
                    '-sourceFilter',        '',
                    '-destinationFilter',   '')
            ixNet.commit()
            if len(IXIAport) == 4:
                ixNet.setMultiAttribute( trafficItem2,
                        '-name'                 ,'Traffic Ethernet2',
                        '-trafficType'          ,'ethernetVlan',
                        '-allowSelfDestined'    ,False,
                        '-trafficItemType'      ,'L2L3',
                        '-mergeDestinations'    ,True,
                        '-egressEnabled'        ,False,
                        '-srcDestMesh'          ,'oneToOne',  #manyToMany, oneToOne
                        '-enabled'              ,True,
                        '-routeMesh'            ,'oneToOne',    #fullMesh, oneToOne
                        '-transmitMode'         ,'interleaved',
                        '-biDirectional'        ,True,
                        '-hostsPerNetwork'      ,1)
                ixNet.commit()
                ixNet.setAttribute(trafficItem2, '-trafficType', 'ethernetVlan')
                ixNet.commit()
                ixNet.add(trafficItem2, 'endpointSet',
                        '-sources',             mac3,
                        '-destinations',        mac4,
                        '-name',                'ep-set2',
                        '-sourceFilter',        '',
                        '-destinationFilter',   '')
                ixNet.commit()
            
            ################################################################################
            # Assign ports
            ################################################################################
            vports = ixNet.getList(root, 'vport')       #::ixNet::OBJ-/vport:1 , ::ixNet::OBJ-/vport:2
            logger.info ("Assigning ports to " + str(vports) + " ...")
            assignPorts = ixNet.execute('assignPorts', IXIAports, [], ixNet.getList("/","vport"), True)
            if assignPorts != vports:
                raise TestFailedError("FAILED assigning ports. Got %s" %assignPorts)
            else:
                logger.info("Connect PASSED assigning ports. Got %s" %assignPorts)
            
            ################################################################################
            # Port Speed
            ################################################################################
            logger.info ("Config port speed: " + portspeed)
            ixNet.setMultiAttribute( vport1 + "/l1Config/novusTenGigLan",
                    '-autoInstrumentation'          ,'floating',
                    '-loopback'                     ,'false',
                    '-txIgnoreRxLinkFaults'         ,'false',
                    '-loopbackMode'                 ,'none',
                    '-enablePPM'                    ,'false',
                    '-flowControlDirectedAddress'   ,'01 80 C2 00 00 01',
                    '-media'                        ,'copper',
                    '-speed'                        ,'speed10g',
                    '-enabledFlowControl'           ,'true',
                    # '-autoNegotiate'                ,'true',
                    # '-masterSlaveMode'              ,'master',          #slave mode
                    '-ppm'                          ,'0',
                    '-speedAuto'                    ,[portspeed],)
            ixNet.setMultiAttribute( vport2 + "/l1Config/novusTenGigLan",
                    '-autoInstrumentation'          ,'floating',
                    '-loopback'                     ,'false',
                    '-txIgnoreRxLinkFaults'         ,'false',
                    '-loopbackMode'                 ,'none',
                    '-enablePPM'                    ,'false',
                    '-flowControlDirectedAddress'   ,'01 80 C2 00 00 01',
                    '-media'                        ,'copper',
                    '-speed'                        ,'speed10g',
                    '-enabledFlowControl'           ,'true',
                    # '-autoNegotiate'                ,'true',
                    # '-masterSlaveMode'              ,'master',          #slave mode
                    '-ppm'                          ,'0',
                    '-speedAuto'                    ,[portspeed],)
            ixNet.commit()
            
            
        else:
            root = ixNet.getRoot()      #::ixNet::OBJ-/
            vPorts = ixNet.getList(root, 'vport')
            vport1 = vPorts[0]                  #::ixNet::OBJ-/vport:1
            vport2 = vPorts[1]                  #::ixNet::OBJ-/vport:2
            if len(IXIAport) == 4:
                vport3 = vPorts[2]              #::ixNet::OBJ-/vport:3
                vport4 = vPorts[3]              #::ixNet::OBJ-/vport:4
            
           
    def my_func2(self, passtimes, failtimes, transmissionControl_duration, transmissionControl_type, frameSize_fixedSize, frameSize_type, frameRate_rate, frameRate_rate2, display):
        logger.info ('DurationTime:' + str(transmissionControl_duration))
        logger.info ('TransmissionType:' + transmissionControl_type)
        logger.info ('FixedSize:' + str(frameSize_fixedSize))
        logger.info ('FrameSizeType:' + frameSize_type)
        logger.info ('FrameRate:' + str(frameRate_rate))
        logger.info ('FrameRate2:' + str(frameRate_rate2))

        globals.num1 = passtimes
        globals.num2 = failtimes
        root = ixNet.getRoot()
        
        trafficItem = ixNet.getList(root + 'traffic', 'trafficItem')[0]         #::ixNet::OBJ-/traffic/trafficItem:1
        if len(IXIAport) == 4:
            trafficItem2 = ixNet.getList(root + 'traffic', 'trafficItem')[1]    #::ixNet::OBJ-/traffic/trafficItem:2
        
        ixNet.setMultiAttribute( trafficItem,
                '-name'                 ,'Traffic Ethernet',
                '-trafficType'          ,'ethernetVlan',
                '-allowSelfDestined'    ,False,
                '-trafficItemType'      ,'L2L3',
                '-mergeDestinations'    ,True,
                '-egressEnabled'        ,False,
                '-srcDestMesh'          ,'oneToOne',  #manyToMany, oneToOne
                '-enabled'              ,True,
                '-routeMesh'            ,'oneToOne',    #fullMesh, oneToOne
                '-transmitMode'         ,'interleaved',
                '-biDirectional'        ,True,
                '-hostsPerNetwork'      ,1)
        ixNet.commit()
        ixNet.setAttribute(trafficItem, '-trafficType', 'ethernetVlan')
        ixNet.commit()

        if frameSize_type == 'fixed':
            ixNet.setMultiAttribute(trafficItem + "/configElement:1/frameSize",
                    '-type',          'fixed',
                    '-fixedSize',     frameSize_fixedSize)
        else:
            ixNet.setMultiAttribute(trafficItem + "/configElement:1/frameSize",
                    '-randomMax',       '1518',
                    '-randomMin',         '68',   
                    '-type',      'random')
        ixNet.setMultiAttribute(trafficItem + "/configElement:1/frameRate",
                '-type',        'percentLineRate',
                '-rate',        frameRate_rate)
        ixNet.setMultiAttribute(trafficItem + "/configElement:1/transmissionControl",
                '-duration'               ,transmissionControl_duration,
                '-iterationCount'         ,1,
                '-startDelayUnits'        ,'bytes',
                '-minGapBytes'            ,12,
                '-frameCount'             ,1000000,
                '-type'                   ,transmissionControl_type, #fixedDuration, fixedFrameCount , continuous
                '-interBurstGapUnits'     ,'nanoseconds',
                '-interBurstGap'          , 0,
                '-enableInterBurstGap'    ,False,
                '-interStreamGap'         ,0,
                '-repeatBurst'            ,1,
                '-enableInterStreamGap'   ,False,
                '-startDelay'             ,0,
                '-burstPacketCount'       ,1,)
        ixNet.setMultiAttribute(trafficItem + "/tracking", '-trackBy', ['sourceDestValuePair0'])
        ixNet.commit()

        if len(IXIAport) == 4:
            ixNet.setMultiAttribute( trafficItem2,
                    '-name'                 ,'Traffic Ethernet2',
                    '-trafficType'          ,'ethernetVlan',
                    '-allowSelfDestined'    ,False,
                    '-trafficItemType'      ,'L2L3',
                    '-mergeDestinations'    ,True,
                    '-egressEnabled'        ,False,
                    '-srcDestMesh'          ,'oneToOne',  #manyToMany, oneToOne
                    '-enabled'              ,True,
                    '-routeMesh'            ,'oneToOne',    #fullMesh, oneToOne
                    '-transmitMode'         ,'interleaved',
                    '-biDirectional'        ,True,
                    '-hostsPerNetwork'      ,1)
            ixNet.commit()
            ixNet.setAttribute(trafficItem2, '-trafficType', 'ethernetVlan')
            ixNet.commit()

            if frameSize_type == 'fixed':
                ixNet.setMultiAttribute(trafficItem2 + "/configElement:1/frameSize",
                        '-type',          'fixed',
                        '-fixedSize',     frameSize_fixedSize)
            else:
                ixNet.setMultiAttribute(trafficItem2 + "/configElement:1/frameSize",
                        '-randomMax',       '1518',
                        '-randomMin',         '68',   
                        '-type',      'random')
            ixNet.setMultiAttribute(trafficItem2 + "/configElement:1/frameRate",
                    '-type',        'percentLineRate',
                    '-rate',        frameRate_rate)
            ixNet.setMultiAttribute(trafficItem2 + "/configElement:1/transmissionControl",
                    '-duration'               ,transmissionControl_duration,
                    '-iterationCount'         ,1,
                    '-startDelayUnits'        ,'bytes',
                    '-minGapBytes'            ,12,
                    '-frameCount'             ,1000000,
                    '-type'                   ,transmissionControl_type, #fixedDuration, fixedFrameCount , continuous
                    '-interBurstGapUnits'     ,'nanoseconds',
                    '-interBurstGap'          , 0,
                    '-enableInterBurstGap'    ,False,
                    '-interStreamGap'         ,0,
                    '-repeatBurst'            ,1,
                    '-enableInterStreamGap'   ,False,
                    '-startDelay'             ,0,
                    '-burstPacketCount'       ,1,)
            ixNet.setMultiAttribute(trafficItem2 + "/tracking", '-trackBy', ['sourceDestValuePair0'])
            ixNet.commit()
        
        ################################################################################
        # Assign ports
        ################################################################################
        vports = ixNet.getList(root, 'vport')       #::ixNet::OBJ-/vport:1 , ::ixNet::OBJ-/vport:2
        logger.info ("Assigning ports to " + str(vports) + " ...")
        assignPorts = ixNet.execute('assignPorts', IXIAports, [], ixNet.getList("/","vport"), True)
        if assignPorts != vports:
            raise TestFailedError("FAILED assigning ports. Got %s" %assignPorts)
        else:
            logger.info("Connect PASSED assigning ports. Got %s" %assignPorts)

        i = 0
        while i < 1:
            count = 0
            ################################################################################
            # Start All Protocols
            ################################################################################
            logger.info ("Starting All Protocols")
            ixNet.execute('startAllProtocols')
            logger.info ("Sleep 5 sec for protocols to start")
            time.sleep(5)

            ################################################################################
            # Checking port Link up
            ################################################################################
            z = 1
            aa = 0
            while z < 20:
                viewName = "Port Statistics"
                views = ixNet.getList('/statistics', 'view')
                viewObj = ''
                editedViewName = '::ixNet::OBJ-/statistics/view:\"' + viewName + '\"'
                for view in views:
                    if editedViewName == view:
                         viewObj = view
                         break
                logger.info ("Getting the Link state values %s sec" %z)
                Linkup = ixNet.execute('getColumnValues', viewObj, 'Link State')
                Speed = ixNet.execute('getColumnValues', viewObj, 'Line Speed')
                k = 1
                for x , y in zip(Linkup,Speed):
                    logger.info ('P%s ' %k + x + " "+ y)
                    k += 1
                if z > 2:
                    if display == True:
                        aa += 1
                        logger.info ("Link up time over 10 seconds")
                    else:
                        logger.info ("Link up time over 10 seconds")
                if Linkup.count('Link Up') == len(IXIAport):
                    z += 20
                else:
                    time.sleep(1)
                z += 1
            if aa >= 1:
                globals.num4 += 1

            ################################################################################
            # Generate, apply and start traffic
            ################################################################################
            r = ixNet.getRoot()                             #::ixNet::OBJ-/
            ixNet.execute('generate', trafficItem)          #generate::ixNet::OBJ-/traffic/trafficItem:1
            if len(IXIAport) == 4:
                ixNet.execute('generate', trafficItem2)     #generate::ixNet::OBJ-/traffic/trafficItem:2
            ixNet.execute('apply', r + 'traffic')           #apply::ixNet::OBJ-/traffic
            ixNet.execute('start', r + 'traffic')           #start::ixNet::OBJ-/traffic
            logger.info ("Sleep 5 sec to send all traffic")
            time.sleep(5)

            ################################################################################
            # Checking Stats to see if traffic was sent OK
            ################################################################################
            logger.info ("Checking Stats to check if traffic was sent OK")
            logger.info ("Getting the object for view Traffic Item Statistics")
            viewName = "Port Statistics"
            views = ixNet.getList('/statistics', 'view')
            viewObj = ''
            editedViewName = '::ixNet::OBJ-/statistics/view:\"' + viewName + '\"'
            for view in views:
                if editedViewName == view:
                     viewObj = view
                     break
            logger.info ("Getting the Tx/Rx Frames values")

            time.sleep(transmissionControl_duration + 10)   #Delay 10 sec required value

            txFrames = ixNet.execute('getColumnValues', viewObj, 'Frames Tx.')
            rxFrames = ixNet.execute('getColumnValues', viewObj, 'Valid Frames Rx.')
            States = ixNet.execute('getColumnValues', viewObj, 'Stat Name')
            CRCs = ixNet.execute('getColumnValues', viewObj, 'CRC Errors')

            PortName = ["P1", "P2", "P3", "P4"]
            PortName2 = ["P2", "P1", "P4", "P3"]
            j = 0
            for txStat, rxStat, CRC, Stat in zip(txFrames, rxFrames, CRCs, States):
                logger.info (PortName[j] + " Tx Frames %s ," % txStat + PortName2[j] + " Rx Frames %s ," % rxStat + " CRC Errors %s ," % CRC + " PortName %s " % Stat)
                if txStat != rxStat:
                    logger.info ("P" + str(j + 1) + " Tx - Rx packet loss more than 3,Packet loss: " + str(int(txStat) - int(rxStat)))
                    globals.num3 += 1
                    if j == 0:
                        globals.num5 += 1
                        globals.str3 = "loss " + str(int(txStat) - int(rxStat))
                    elif j == 1:
                        globals.num6 += 1
                        globals.str4 = "loss " + str(int(txStat) - int(rxStat))
                else:
                    count += 1
                j += 1

            if count == len(IXIAport):          #pass
                globals.num1 += 1
                passtimes = globals.num1
                break
            else:                               #fail
                globals.num2 += 1
                failtimes = globals.num2
                i += 1

        if display == True:
            logger.info ("=================================================")
            logger.info ("       =======  Test PASSED = %s  =======" % str(passtimes))
            logger.info ("       =======  Test FAILED = %s  =======" % str(failtimes))
            logger.info ("=================================================")
        else:
            logger.info ("=================================================")
            logger.info ("=================================================")