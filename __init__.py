# -*- coding: utf-8 -*-
"""
    __init__

    Initialize Module

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from .magento_ import (
    Instance, InstanceWebsite, WebsiteStore, WebsiteStoreView,
    TestConnectionStart, TestConnection,
)
from country import Country
from party import Party, MagentoWebsiteParty


def register():
    """
    Register classes
    """
    Pool.register(
        Instance,
        InstanceWebsite,
        WebsiteStore,
        WebsiteStoreView,
        TestConnectionStart,
        Country,
        Party,
        MagentoWebsiteParty,
        module='magento', type_='model'
    )
    Pool.register(
        TestConnection,
        module='magento', type_='wizard'
    )