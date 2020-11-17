# -*- coding: utf-8 -*-
# Part of addOons srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 addOons srl (<http://www.addoons.it>)

import logging

_logger = logging.getLogger(__name__)

# pyxb is referenced in several in top-level statements in
# fatturapa_v_1_1, so we guard the import of the entire file
try:
    from . import fatturapa
except ImportError:
    _logger.debug('Cannot `import pyxb`.')  # Avoid init error if not installed