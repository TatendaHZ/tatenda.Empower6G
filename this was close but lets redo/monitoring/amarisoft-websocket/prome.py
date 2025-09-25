import prometheus_client as prom
import time
import logging


# Tutorial from https://yonahdissen.medium.com/monitoring-custom-metrics-using-python-and-prometheus-98e6758c7cf9

AMARISOFT_COUNTER = prom.Gauge('counter', 'Naive counter')
AMARISOFT_DL_BITRATE_GAUGE = prom.Gauge('dl_bitrate', 'DL bitrate in Mbps', ["ue"])
AMARISOFT_UL_BITRATE_GAUGE = prom.Gauge('ul_bitrate', 'UL bitrate in Mbps', ["ue"])

UE_LIST = ["1", "2", "3"]

INTERVAL = 5

def get_amari():
    counter = 0
    while True:
        counter = counter + 1
        AMARISOFT_COUNTER.set(counter)
        for ue_name in UE_LIST:
            # Read from logs.
            dl_bitrate = 10.56
            AMARISOFT_DL_BITRATE_GAUGE.labels(ue=ue_name).set(dl_bitrate)
            ul_bitrate = 36.20
            AMARISOFT_UL_BITRATE_GAUGE.labels(ue=ue_name).set(ul_bitrate)
        time.sleep(INTERVAL)

def get_module_logger(mod_name):
    """
    To use this, do logger = get_module_logger(__name__)
    """
    logger = logging.getLogger(mod_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    
    get_module_logger(__name__).info("Prometheus Sergio :DD:D:D:D")
    prom.start_http_server(80)
    get_amari()