"""
"""
import logging

import ckan.model as model
from ckan.lib.base import h, BaseController, abort
from ckan.plugins.toolkit import (render, c, request, _,
                                         ObjectNotFound, NotAuthorized,
                                         get_action, check_access)

log = logging.getLogger(__name__)

class WebhookController(BaseController):

    def index(self):
        context = {'model':model,'user': c.user}

        return render('webhook_list.html')
