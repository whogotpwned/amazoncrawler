# The Simple Amazon Stock Crawler 
Simple Crawler For Amazon Stock Information Gathering.

If you like my project, "Star" in the corresponding project right corner, please. If you want to buy me a cup of coffee, use the Bitcoin QR Code right below.

<div align="center">
  <img src="btcdonatewallet.jpg" />
</div>

BTC Address: 14pmyZZrFfCCEK49FC7jKWj1WGzhUP4rsQ

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

### Create Virtualenvironment and Install Dependencies

```bash
virtualenv -p python3 myenv
cd myenv
git clone https://github.com/localhostport80/amazoncrawler
source venv/bin/activate
pip install -r requirements.txt
```


### Usage

There is one main file in this project, namely *amazoncrawler.py*. Feel free to type "?" or "help" inside the CLI that opens when running it. You will find commands for retrieving the stock information as well as commands for plotting csv files.

```bash
python amazoncrawler.py
```

```bash
Starting prompt...
> ?

Documented commands (type help <topic>):
========================================
help  quit  retrieve_stock_of_all_items_in_config  show_plots
```