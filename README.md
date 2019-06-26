# amazoncrawler
Simple Crawler For Amazon Stock Information Gathering

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
python amazoncrawler.py && python plotter.py
```
