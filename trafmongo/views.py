from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from trafmongo import resources

@view_config(name='', context=resources.Root)
def root(context, request):
    """
    Redirects to ARPViz
    """
    return HTTPFound(location="/arpviz")

@view_config(name='', renderer='trafmongo:templates/arpviz.pt',
             context=resources.ARPViz)
def arpvizpage(context, request):
    return {}
