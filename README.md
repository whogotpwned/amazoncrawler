# amazoncrawler
Simple Crawler For Amazon Stock Information Gathering.

<html>
  <head>
    <link rel="stylesheet" href="/path/to/css/btcdonate.css">
  </head>
  <body>

    <h1>My Awesome Web Page</h1>

    <p>Some stuff on your page and <a href="bitcoin:A_BITCOIN_ADDRESS">a donation link</a></p>
    <p>Some more stuff on your page</p>
    <p>
      Even more stuff on your page and
      <a href="bitcoin:ANOTHER_BITCOIN_ADDRESS?amount=0.01">
        another donation link, this time with a suggested amount
      </a>.
    </p>

    <script type="text/javascript" src="/path/to/js/jquery.js"></script>
    <script type="text/javascript" src="/path/to/js/jquery.qrcode.js"></script>
    <script type="text/javascript" src="/path/to/js/btcdonate.js"></script>
    <script>
      btcdonate();
    </script>

  </body>
</html>

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
