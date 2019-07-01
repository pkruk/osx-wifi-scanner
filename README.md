# Mac OS Wifi-Scanner

There is no `iwlist` on Mac OS, that is why I created my own script to get all SSID around me via cli ;) 


## How to use it:

First of all, install requirements:

```bash
pip install -r requirements.txt
```

Then run a script:

```bash

python3 wifi-scan

```


## Example:

How to use it:

```bash
python3 wifi-scan.py

{'SOME WIFI': {'BSSID': '11:11:11:11:11:11', 'RSSI': -45},
 'ANOTHER_WIFI': {'BSSID': '11:11:11:11:11:11', 'RSSI': -57}}

```

Wifi-scan.py support `filter` argument, which can be used to find any particular SSID.

```bash
python3 wifi-scan.py -f SOME_WIFI

{'SOME WIFI': {'BSSID': '11:11:11:11:11:11', 'RSSI': -45}

```
