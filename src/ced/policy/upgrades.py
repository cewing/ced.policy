import logging

from zope.app.component.hooks import getSite

from Products.CMFCore.utils import getToolByName


logger = logging.getLogger('ced.policy')


def install_discussion(context):
    portal = getSite()
    setup_tool = getToolByName(portal, 'portal_setup');
    profile = 'profile-plone.app.discussion:default'
    setup_tool.runAllImportStepsFromProfile(profile)