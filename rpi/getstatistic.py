# test BLE Scanning software

import blescan
import sys

import bluetooth._bluetooth as bluez
import math
import requests

port = 8000
ip = '192.168.0.76'

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def distance(txPower, rssi):
    if rssi == 0:
	return -1.0 # if we cannot determine accuracy, return -1.
    #return math.pow(10,(float(txPower)/float(rssi))/20.0)
    ratio = rssi*1.0/txPower
    if ratio < 1.0:
	return math.pow(ratio,10)
    else:
	accuracy =  (0.89976)*math.pow(ratio,7.7095) + 0.111
	return accuracy


if len(sys.argv) < 3:
	print("You should input distance as an argument\n")
	exit()

f = open(sys.argv[2], 'a')
dev_id = 0
try:
    sock = bluez.hci_open_dev(dev_id)
    print("ble thread started")
except:
    print("error accessing bluetooth device...")
    sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)
rssi_dict = {"00000000-0000-0000-0000-000000000303":0}#, "00000000-0000-0000-0000-000000000317":0,"00000000-0000-0000-0000-000000001717":0,"00000000-0000-0000-0000-000000001703":0}
tx_dict = {"00000000-0000-0000-0000-000000000303":0}#, "00000000-0000-0000-0000-000000000317":0,"00000000-0000-0000-0000-000000001717":0,"00000000-0000-0000-0000-000000001703":0}
l = ["00000000-0000-0000-0000-000000000303"]#, "00000000-0000-0000-0000-000000000317","00000000-0000-0000-0000-000000001717","00000000-0000-0000-0000-000000001703"]

while True:
    returnedList = blescan.parse_events(sock, 10)
    #print("----------")
    for beacon in returnedList:
        #l = ["00000000-0000-0000-0000-000000000303", "00000000-0000-0000-0000-000000000317","00000000-0000-0000-0000-000000001717","00000000-0000-0000-0000-000000001703"]
	for ll in l:
		bb = beacon.getUID()
		if bb == ll:
			#print(ll)
			#print(beacon)
			rssi_dict[ll] = int(beacon.getRSSI())
			tx_dict[ll] = int(beacon.getTxPower())
    #r = requests.post("http://{}:{}/".format(ip, port), data=rssi_dict)
    for ll in l:
	#print(tx_dict[ll])
	#print(rssi_dict[ll])
	f.write('{};{};{}\n'.format(tx_dict[ll],rssi_dict[ll], sys.argv[1]))
	print('{};{};{}'.format(tx_dict[ll],rssi_dict[ll], sys.argv[1]))
	#print('{} : tx: {} rssi: {} distance: {}'.format(ll,tx_dict[ll],rssi_dict[ll], distance(tx_dict[ll],rssi_dict[ll])))
    	#print('{} : {}'.format(ll,distance(tx_dict[ll],rssi_dict[ll])))
	#print('{} : {}'.format(ll,tx_dict[ll]-rssi_dict[ll]))
	#rssi_dict[ll] = rssi_dict[ll] - tx_dict[ll]
    #r = requests.post("http://{}:{}/req/".format(ip, port), data=rssi_dict)
    #r = requests.Request('POST',"http://{}:{}/".format(ip, port), data=rssi_dict)
    #print(pretty_print_POST(r.prepare()))
