# The Simple Amazon Stock Crawler 
Simple Crawler For Amazon Stock Information Gathering.

If you like my project, "Star" in the corresponding project right corner, please. If you want to buy me a cup of coffee, use the Bitcoin QR Code right below.

<div align="center">
  <img src="btcdonatewallet.jpg" />
</div>

ETH Address: 0xF3Ed337358e57552317A77dEcCA4Ad48D0D128Db

## Installation

## Adapt Config.xml

The xml file contains all the items to be observed. All items should be
enclosed within the <data> tag. Each item on the other hand should be
enclosed within an <item> tag, as shown in the following:


```xml
<?xml version="1.0" encoding="utf-8"?>
<data>
    <selenium-options>
        <headless-mode>
            True
        </headless-mode>
    </selenium-options>
    <item name="flamingo-ball">
        <path>
            https://www.amazon.de/ballonfritz%C2%AE-Flamingo-Ballon-Riesenballon-Geburtstagsgeschenk/dp/B07D24S144/ref=sr_1_5?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91
            keywords=flamingo+ballon qid=1561379051 s=gateway sr=8-5
        </path>
    </item>
</data>
```

If you are going to base your config file on *example_config.xml* do not
forget to rename it to *config.xml*. The given chromedriver in
*bin/chromedriver* is actually the one for macos. Depending on your
operating system you might have to replace it by the correct one, see <a
href="http://chromedriver.chromium.org/downloads">Chromedriver
Chromium</a>.

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
exit  help  quit  retrieve_stock_of_all_items_in_config  save_plots  show_plots
```


### Telegram-Bot

There is an additional main file called *amazoncrawler_bot.py* which makes it possible to interact with *amazoncrawler.py* via Telegram. Use BotFather to generate your unique private API token and add your private chat-id to the config file. The bot only grants admission to those users who's ids are listed in the XML.

```bash
python amazoncrawler_bot.py
```