from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.cover.tiles.collection import ICollectionTile, CollectionTile
from zope.interface.declarations import implements


class IIsotopeTile(ICollectionTile):
    """ """


class IsotopeTile(CollectionTile):
    implements(IIsotopeTile)
    index = ViewPageTemplateFile('tile.pt')
    short_name = u'Isotope Collection tile'
