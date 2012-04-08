from sixfeetup.utils import helpers as sfutils 


def importVarious(context):
    """Run the setup handlers for the default profile"""
    if context.readDataFile('ced_policy-default.txt') is None:
        return
    # automagically run a plone migration if needed
    sfutils.runPortalMigration()
    # automagically run the upgrade steps for this package
    sfutils.runUpgradeSteps(u'ced.policy:default')
