import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from base import OXFORD_INTRANET_FOLDER_INTEGRATION_TESTING


class TestContentType(unittest.TestCase):
    """Test intranet folder content type"""
    layer = OXFORD_INTRANET_FOLDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('IntranetFolder', 'if1')
        assert 'if1' in self.portal.objectIds()
