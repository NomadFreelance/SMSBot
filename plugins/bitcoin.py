from util.plugin import Plugin
from util import http


class Bitcoin(Plugin):
    def __init__(self):
        super(Bitcoin, self).__init__()

        self.add_command("bitcoin", self.com_bitcoin, has_arg=False)

    def com_bitcoin(self):
        try:
            data = http.get_json("https://mtgox.com/api/0/data/ticker.php")
        except:
            return 'Error retrieving prices.'

        ticker = data['ticker']
        high = float(ticker['high'])
        low = float(ticker['low'])
        volume = float(ticker['vol'])
        current = float(ticker['buy'])
        
        return ("Current Price: $%.2f - High: $%.2f - Low: $%.2f - Bitcoins Sold Today: %s" % (current, high, low, volume))

ExportPlugin = Bitcoin