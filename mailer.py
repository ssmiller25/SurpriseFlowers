#!/usr/bin/env python
# encoding: utf-8
"""Send email, managing all details such as authentication."""
import smtplib

username = None
password = None

try:
    import settings
    username = settings.USERNAME
    password = settings.PASSWORD
    fromaddr = settings.FROMADDR
    toaddr = settings.TOADDR
    if settings.SMTPSERVER:
      smtpserver=settings.SMTPSERVER
    else:
      smtpserver='smtp.gmail.com'

    if settings.SMTPPORT:
      smtpport=int(settings.SMTPPORT)
    else:
      smtpport=587

    msg = settings.EMAIL_MESSAGE
except ImportError as e:
    raise("COULDNT IMPORT LOCAL SETTINGS: %s" % e)


def send_email():
    """Generate and send email."""

    try:
        server = smtplib.SMTP(smtpserver, smtpport)
        server.starttls()
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddr, msg)
    except Exception as e:
        raise e
    finally:
        server.quit()
