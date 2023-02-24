import logging
import os

from dotenv import load_dotenv

try:
    load_dotenv()
except:
    logging.debug("Could not load .env file")


BOT_NAME = "coffeereview"

SPIDER_MODULES = ["coffeereview.spiders"]
NEWSPIDER_MODULE = "coffeereview.spiders"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0"

ROBOTSTXT_OBEY = False

# HTTPCACHE_ENABLED = True
# HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 400, 401, 402, 403, 404]

DOWNLOADER_MIDDLEWARES = {"scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610}
ZYTE_SMARTPROXY_ENABLED = True
ZYTE_SMARTPROXY_APIKEY = os.environ.get("ZYTE_SMARTPROXY_APIKEY")

SPIDERMON_ENABLED = True
EXTENSIONS = {
    "spidermon.contrib.scrapy.extensions.Spidermon": 500,
}
SPIDERMON_SPIDER_OPEN_MONITORS = {
    "coffeereview.monitors.SpiderOpenMonitorSuite",
}
SPIDERMON_SPIDER_CLOSE_MONITORS = {
    "coffeereview.monitors.SpiderCloseMonitorSuite",
}
SPIDERMON_PERIODIC_MONITORS = {
    "coffeereview.monitors.PeriodicMonitorSuite": 3600,  # time in seconds
}
SPIDERMON_MIN_ITEMS = 5
SPIDERMON_MAX_ERRORS = 1

SPIDERMON_TELEGRAM_SENDER_TOKEN = os.environ.get("SPIDERMON_TELEGRAM_SENDER_TOKEN")
SPIDERMON_TELEGRAM_RECIPIENTS = [os.environ.get("SPIDERMON_TELEGRAM_RECIPIENTS")]


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
