"""
This is a merge of roughly a dozen articles I found on
rolling your own JSON Logger instead of using a 3rd party
Library.
"""

import json
import logging

class JSONFormatter(logging.Formatter):
    """
    Output log messages in JSON format
    """
    def __init__(self, *args, **kwargs):
    # primarily to allow datetime formatting
        super().__init__(*args, **kwargs)

    def format(self, record: logging.LogRecord) -> str:
        message = record.__dict__.copy()
        message["message"] = record.getMessage()
        message["timestamp"] = self.formatTime(record, self.datefmt)

        for key in ("msg", "args"):
            message.pop(key, None)

        if record.exc_info and record.exc_text is None:
            record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            message["exc_info"] = record.exc_text
        else:
            message.pop("exc_text", None)

        # eliminate null records from the output so as to not 
        # muddle it with nonsensical information
        if not record.exc_info:
            message.pop("exc_info", None)

        if record.stack_info:
            message["stack_info"] = self.formatStack(record.stack_info)
        else:
            message.pop("stack_info", None)

        return json.dumps(message)
