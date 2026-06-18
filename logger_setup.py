import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/system_trace.log',
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s -> %(message)s'
)
logger = logging.getLogger("ExpressDelivery")
