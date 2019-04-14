#!/usr/bin/env python3
## Pi-hole Sync
import pihole as ph # MY FORK!!!!!!!!!!

## Global Variables
domain = "pi-hole4all.net"
instances = {
    "pd": {"port": 443},
    #"orange": {"port": 443},
    "red": {"port": 443},
    "tjj": {"port": 443}
}
templist = []

## Functions
def getInfo(instance, port):
    if domain:
        hostname = '.'.join([instance, domain])
        pihole = ph.PiHole(hostname, port = port)
        blacklist = pihole.getList("black")[1]
        print(blacklist)
    
def main():
    for instance in instances: 
        host = instance
        instance = instances[instance]
        port = instance['port']
        getInfo(host, port)


## Explicitly Called?
if __name__ == "__main__":
    main()
