#!/usr/bin/env python

import nmap

nm = nmap.PortScanner() 
cidr2='192.168.0.1/24'

a=nm.scan(hosts=cidr2, arguments='-sP') 

for k,v in a['scan'].items(): 
    if str(v['status']['state']) == 'up':
        print (str(v))
        try: 
            print (str(v['addresses']['ipv4']) + ' => ' + str(v['addresses']['mac']))
        except: 
            print (str(v['addresses']['ipv4']))