from Acquisition import aq_inner
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.customerize import registration
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from oxford.intranet.folder.interfaces.intranetfolder import IIntranetFolder

from base import OXFORD_INTRANET_FOLDER_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Test intranet folder content type"""
    layer = OXFORD_INTRANET_FOLDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('IntranetFolder', 'if1')
        if1 = getattr(self.portal, 'if1')
        assert 'if1' in self.portal.objectIds()
