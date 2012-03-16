from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class CedPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import ced.policy
        xmlconfig.file('configure.zcml',
                       ced.policy,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ced.policy:default')

CED_POLICY_FIXTURE = CedPolicy()
CED_POLICY_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(CED_POLICY_FIXTURE, ),
                       name="CedPolicy:Integration")