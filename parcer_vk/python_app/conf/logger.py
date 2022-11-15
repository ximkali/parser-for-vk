import logging
import sys
from logging import StreamHandler
from logging import Formatter

dbug_logger = logging.getLogger('debug_logger')
info_logger = logging.getLogger('info_logger')
warning_logger = logging.getLogger('warning_logger')
exception_logger = logging.getLogger('exception_logger')

dbug_logger.setLevel(10)
info_logger.setLevel(20)
warning_logger.setLevel(30)
exception_logger.setLevel(40)

debug_handler = StreamHandler(stream=sys.stdout)
info_handler = StreamHandler(stream=sys.stdout)
warning_handler = StreamHandler(stream=sys.stdout)
exception_handler = StreamHandler(stream=sys.stdout)

debug_handler.setFormatter(Formatter(fmt='[%(active_time)s :: %(name):: %(level_name)s] %(funcName)s %(massage)s'))
info_handler.setFormatter(Formatter(fmt='[%(active_time) s:: %(level_name)s] %(massage)s'))
warning_handler.setFormatter(Formatter(fmt='[%(active_time)s :: %(level_name)s] %(funcName)s %(massage)s'))
exception_handler.setFormatter(Formatter(fmt='[%(active_time)s :: %(level_name)s] %(funcName)s %(massage)s'))

dbug_logger.addHandler(debug_handler)
info_logger.addHandler(info_handler)
warning_logger.addHandler(warning_handler)
exception_logger.addHandler(exception_handler)

