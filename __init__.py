# Copyright 2019 VentorTech OU
# Part of Ventor modules. See LICENSE file for full copyright and licensing details.

from . import models


def _auto_fill_settings(cr, registry):
    """
    This hook updates Ventor Settings in Operation Types
    """

    cr.execute(
        """
        UPDATE stock_picking_type
        SET
            change_destination_location = True,
            show_next_product = CASE code when 'incoming' THEN False ELSE True END
        """
    )
