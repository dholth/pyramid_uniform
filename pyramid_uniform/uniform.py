from webob import Response
from wsgiref import simple_server
from pyramid.configuration import Configurator
from pkg_resources import resource_filename

import formish
import schemaish
import zope.component
import pyramid_formish

def sample_form(request):
    import logging
    log = logging.getLogger(__name__)

    schema = schemaish.Structure()
    schema.add('email', schemaish.String())
    # schema.add('birthday', schemaish.Date())
    schema.add('textarea', schemaish.String())
    schema.add('country', schemaish.String())
    schema.add('accept', schemaish.Boolean())

    form = formish.Form(schema, name="uni-form", renderer=pyramid_formish.get_default_renderer())

    form['email'].description = u'Your e-mail address.'
    # form['birthday'].widget = formish.DateParts()
    form['textarea'].widget = formish.TextArea()
    form['country'].widget = formish.SelectChoice(options=['UK', 'US'])
    form['accept'].description = u'Do you accept?'
    form['accept'].widget = formish.Checkbox()

    try:
        form.validate(request)
    except formish.FormError, e:
        log.debug(e)
    except Exception, e:
        log.debug(e)

    return {'form':form, 'form2':form}

def goodbye_world(request):
    return Response('Goodbye world!')

class QuietHandler(simple_server.WSGIRequestHandler):
    def log_message(self, format, *args): pass

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    config = Configurator(settings={'reload_templates':True})
    config.begin()
    sm = zope.component.getSiteManager()
    sm.registerUtility([resource_filename('pyramid_uniform', 'templates/zpt')],
            pyramid_formish.IFormishSearchPath)
    config.add_static_view('static', 'pyramid_uniform:templates/static')
    config.add_view(sample_form, renderer="pyramid_uniform:templates/index.pt")
    config.end()
    app = config.make_wsgi_app()
    simple_server.make_server('', 9876, app, handler_class=QuietHandler).serve_forever()

