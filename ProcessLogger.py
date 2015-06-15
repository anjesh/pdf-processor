import logging
import logging.handlers
import os
import sys

LOG_DIR = 'logs'

def getLogger(loggername, filename = 'processing.log'):
  scriptPath = os.path.dirname(os.path.abspath(__file__))

  if not os.path.exists(os.path.join(scriptPath, LOG_DIR)):
      os.makedirs(os.path.join(scriptPath, LOG_DIR))
  logfile = os.path.join(scriptPath, LOG_DIR, filename)

  logger = logging.getLogger(loggername)
  logger.setLevel(logging.DEBUG)

  handler = logging.FileHandler(logfile)
  handler.setLevel(logging.DEBUG)

  consolehandler = logging.StreamHandler()
  consolehandler.setLevel(logging.INFO)

  formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  consolehandler.setFormatter(formatter)

  logger.addHandler(handler)
  logger.addHandler(consolehandler)
  return logger