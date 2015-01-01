from zope.i18nmessageid import MessageFactory
from oxford.intranet.folder import config

from Products.Archetypes.atapi import listTypes, process_types
from Products.CMFCore.utils import ContentInit

# Define a message factory for when this product is internationalised.
# This will be imported with the special name "_" in most modules. Strings
# like _(u"message") will then be extracted by i18n tools for translation.

academicMessageFactory = MessageFactory('oxford.intranet.folder')


def initialize(context):
    """Initializer called when used as a Zope 2 product.

    This is referenced from configure.zcml. Regstrations as a "Zope 2 product"
    is necessary for GenericSetup profiles to work, for example.

    Here, we call the Archetypes machinery to register our content types
    with Zope and the CMF.
    """

    import content.intranetfolder.IntranetFolder  # noqa

    content_types, constructors, ftis = process_types(
        listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    # Now initialize all these content types. The initialization process takes
    # care of registering low-level Zope 2 factories, including the relevant
    # add-permission. These are listed in config.py. We use different
    # permissions for each content type to allow maximum flexibility of who
    # can add which content types, where. The roles are set up in rolemap.xml
    # in the GenericSetup profile.

    for atype, constructor in zip(content_types, constructors):
        ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
                    content_types=(atype, ),
                    permission=config.ADD_PERMISSIONS[atype.portal_type],
                    extra_constructors=(constructor,),
                    ).initialize(context)
