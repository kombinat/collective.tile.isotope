from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.cover.tiles.collection import ICollectionTile, CollectionTile
from collective.cover.tiles.configuration_view import IDefaultConfigureForm
from plone import api
from plone.autoform import directives as form
from zope import schema
from zope.interface.declarations import implements


class IIsotopeTile(ICollectionTile):
    """ """


class IsotopeTile(CollectionTile):
    implements(IIsotopeTile)
    index = ViewPageTemplateFile('tile.pt')
    short_name = u'Isotope Collection tile'
