from plone.portlets.interfaces import IPortletDataProvider
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope import schema

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets.portlets import base
from urlparse import parse_qs, urlparse
        

class ISearchPortlet(IPortletDataProvider):
    """ A portlet displaying a (live) search box
    """

    enableLivesearch = schema.Bool(
            title = _(u"Enable LiveSearch"),
            description = _(u"Enables the LiveSearch feature, which shows "
                             "live results if the browser supports "
                             "JavaScript."),
            default = True,
            required = False)

    portlet_title = schema.TextLine(
        title=_(u"Title"),
        required=False)

    search_parameter = schema.TextLine(
        title=_(u"Location"),
        required=False)

    search_placeholder = schema.TextLine(
        title=_(u"Placeholder"),
        required=False)

class Assignment(base.Assignment):
    implements(ISearchPortlet)

    portlet_title = u""

    def __init__(self, enableLivesearch=True, portlet_title=u'', search_parameter=u'', search_placeholder=u''):
        self.enableLivesearch=enableLivesearch
        self.portlet_title=portlet_title
        self.search_parameter=search_parameter
        self.search_placeholder=search_placeholder

    @property
    def title(self):
        return self.portlet_title or _(u"Search")


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('search.pt')
    action = '@@search'
    livesearch_action = 'livesearch_reply'

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        portal_state = getMultiAdapter((context, request), name='plone_portal_state')
        self.navigation_root_url = portal_state.navigation_root_url()

    def enable_livesearch(self):
        return self.data.enableLivesearch

    def search_action(self):
        return '{0}/{1}'.format(self.navigation_root_url, self.action)

    def portlet_title(self):
        return self.data.portlet_title or _(u"Search")

    def search_parameter(self):
        params = parse_qs(urlparse(self.data.search_parameter).query, keep_blank_values=True)
        params_keys = params.keys()

        inputs = []

        for key in params:
            inputs.append({'name': key, 'values': params[key]})

        if len(inputs) > 0:
            return inputs

        return self.data.search_parameter or _(u"")

    def search_placeholder(self):
        return self.data.search_placeholder or _(u"")


class AddForm(base.AddForm):
    form_fields = form.Fields(ISearchPortlet)
    label = _(u"Add Search Portlet")
    description = _(u"This portlet shows a search box.")

    def create(self, data):
        return Assignment(
            enableLivesearch=data.get('enableLivesearch', u''),
            portlet_title=data.get('portlet_title', u''),
            search_parameter=data.get('search_parameter', u''),
            search_placeholder=data.get('search_placeholder', u'')
        )


class EditForm(base.EditForm):
    form_fields = form.Fields(ISearchPortlet)
    label = _(u"Edit Search Portlet")
    description = _(u"This portlet shows a search box.")
