# amazoncrawler
Simple Crawler For Amazon Stock Information Gathering.

If you like my project, "Star" in the corresponding project right corner, please. If you want to buy me a cup of coffee, use the Bitcoin QR Code right below.

<div align="center">
![alt text](btcdonatewallet.jpg "BTC-Wallet")
<div/>



Please send BTC to the Bitcoin address 14pmyZZrFfCCEK49FC7jKWj1WGzhUP4rsQ.

## Installation

## Adapt Config.xml

The xml file contains all the items to be observed. All items should be
enclosed within the <data> tag. Each item on the other hand should be
enclosed within an <item> tag, as shown in the following:


```xml
<item name="ITEM-NAME">
  <path>
    <!-- URL TO ITEM -->
  </path>
</item>
```

### Create Virtualenvironment

```bash
source venv/bin/activate
pip install -r requirements.txt
```


### Usage

There are two main files in this project, namely *amazoncrawler.py* and
*plotter.py*. First run amazoncrawler, which retrieves the current
stocks of all items in the config. Second run *plotter.py* to plot all
resulting csv files.

```bash
python amazoncrawler.py
python plotter.py
```
