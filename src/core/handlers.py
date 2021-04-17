from logging import Handler

from core.helper import send_email


DEV_EMAILS_LIST = []


class SendEmailToDevelopersHandler(Handler):
    def emit(self, record):
        log_entry = self.format(record)
        send_email('ERROR starnavi-test', log_entry, DEV_EMAILS_LIST, fail_silently=True)
