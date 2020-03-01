#!/usr/bin/env python
# encoding: utf-8
# Pull settings from environment
import os
import base64

USERNAME = os.environ['SF_USERNAME']
PASSWORD = os.environ['SF_PASSWORD']
FROMADDR = os.environ['SF_FROMADDR']
TOADDR = os.environ['SF_TOADDR']
# FIgure redirection to another SMTP server
if 'SF_SMTPSERVER' in os.environ:
  SMTPSERVER = os.environ['SF_SMTPSERVER']
if 'SF_SMTPPORT' in os.environ:
  SMTPPORT = os.environ['SF_SMTPPORT']

# Email message with be base64 encoded to allow 
EMAIL_MESSAGE = base64.b64decode(os.environ['SF_MESSAGE'])
# example message
#EMAIL_MESSAGE = """Subject: Surprise Flowers!\n\n
#    <Flower Recipient> is great.\n
#    I love <Flower Recipient>.\n
#    You know how I can tell them they're great?  FLOWERS!\n
#    I should buy them flowers."""
