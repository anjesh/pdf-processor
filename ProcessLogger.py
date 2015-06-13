import logging
import logging.handlers
import os
import sys

LOG_DIR = 'logs'

def getLogger(loggername, filename = 'processing.log'):
  if not os.path.exists(LOG_DIR):
      os.makedirs(LOG_DIR)

  logger = logging.getLogger(loggername)
  logger.setLevel(logging.DEBUG)

  handler = logging.FileHandler(os.path.join(LOG_DIR, filename))
  handler.setLevel(logging.DEBUG)

  consolehandler = logging.StreamHandler()
  consolehandler.setLevel(logging.INFO)

  formatter = logging.Formatter('%(name)s %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  consolehandler.setFormatter(formatter)

  logger.addHandler(handler)
  logger.addHandler(consolehandler)
  return logger