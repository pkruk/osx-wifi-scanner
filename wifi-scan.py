import objc
import argparse
from pprint import pprint


parse = argparse.ArgumentParser("Hello, I'm wifi scanner for mac-os-x")
parse.add_argument("--filter", '-f', help="Looking for a concrete network?", default=None)

args = parse.parse_args()
filter_ssid = args.filter


def scan(concrete_ssid=None):
    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'
    objc.loadBundle('CoreWLAN',
                    bundle_path=bundle_path,
                    module_globals=globals())

    iface = CWInterface.interface()
    networks = iface.scanForNetworksWithName_includeHidden_error_(concrete_ssid, True, None)
    return {
        i.ssid(): {
            'RSSI': i.rssiValue(),
            'BSSID': i.bssid()
        }
        for i in networks[0].allObjects() if i.ssid() is not None
    }


result = scan(filter_ssid)

if result is None:
    print("Couldn't find this SSID")

pprint(result)
