from framework import request

from website.project.decorators import must_be_contributor_or_public
from website.project.decorators import must_have_addon
from website.util import rubeus

from ..api import Figshare
from ..utils import article_to_hgrid, project_to_hgrid

@must_be_contributor_or_public
@must_have_addon('figshare', 'node')
def figshare_hgrid_data_contents(*args, **kwargs):
    node_settings = kwargs.get('node_addon')
    node = node_settings.owner
    fs_type = kwargs.get('type', node_settings.figshare_type)
    fs_id = kwargs.get('id', node_settings.figshare_id)

    connect = Figshare.from_settings(node_settings.user_settings)

    if fs_type == 'article':
        return article_to_hgrid(node, connect.article(node_settings, fs_id)['items'][0], expand=True)
    elif fs_type == 'project':
        return project_to_hgrid(node, connect.project(node_settings, fs_id))
    else:
        return []


def figshare_hgrid_data(node_settings, auth, parent=None, **kwargs):
    if not node_settings.figshare_id:
        return
    node = node_settings.owner
    return [
        rubeus.build_addon_root(
            node_settings, node_settings.figshare_id, permissions=auth,
            nodeUrl=node.url, nodeApiUrl=node.api_url,
        )
    ]


@must_be_contributor_or_public
@must_have_addon('figshare', 'node')
def figshare_dummy_folder(node_settings, auth, parent=None, **kwargs):
    if not node_settings.figshare_id:
        return

    node_settings = kwargs.get('node_addon')
    auth = kwargs.get('auth')
    data = request.args.to_dict()

    parent = data.pop('parent', 'null')

    return figshare_hgrid_data(node_settings, auth, None, contents=False, **data)
