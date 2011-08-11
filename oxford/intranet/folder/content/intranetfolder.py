from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType

from oxford.intranet.folder.config import PROJECTNAME
from oxford.intranet.folder.interfaces.intranetfolder import IIntranetFolder

from schemata import IntranetFolderSchema

class IntranetFolder(ATFolder):
    """A protected folder"""

    security = ClassSecurityInfo()

    implements(IIntranetFolder)

    meta_type = 'IntranetFolder'
    _at_rename_after_creation = True

    schema = IntranetFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(IntranetFolder, PROJECTNAME)
