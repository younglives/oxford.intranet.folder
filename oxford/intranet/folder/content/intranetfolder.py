from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.utils import getToolByName

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
        return True

    def at_post_create_script(self):
        self.applyLocalWorkflow()

    def at_post_edit_script(self):
        self.applyLocalWorkflow()

    security.declareProtected(ModifyPortalContent, 'applyLocalWorkflow')
    def applyLocalWorkflow(self):
        """
        Apply a local workflow policy to this intranet folder.
        """
        placeful_workflow_tool = getToolByName(self, 'portal_placeful_workflow')
        if WorkflowPolicyConfig_id not in self.objectIds():
            new_policy_id = 'intranet'
            policy = placeful_workflow_tool.getWorkflowPolicyById(new_policy_id)
            if not policy:
                return
            wf_config = WorkflowPolicyConfig(new_policy_id, new_policy_id)
            self._setObject(WorkflowPolicyConfig_id, wf_config)
            workflow_tool = getToolByName(self, 'portal_workflow')
            workflow_tool.updateRoleMappings()

registerType(IntranetFolder, PROJECTNAME)
