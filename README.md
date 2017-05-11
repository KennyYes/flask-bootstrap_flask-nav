# flask-bootstrap_flask-nav
Werkzeug throws a werkzeug.routing.BuildError when flask_bootstrap is used with flask_nav and blueprints
Here's the traceback:
```Traceback (most recent call last):
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1997, in __call__
    return self.wsgi_app(environ, start_response)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1985, in wsgi_app
    response = self.handle_exception(e)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1540, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\_compat.py", line 33, in reraise
    raise value
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\_compat.py", line 33, in reraise
    raise value
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "D:\Users\kenny\Desktop\bpissue\app\blueprints\views.py", line 13, in fournotfive
    return render_template("405.html")
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\templating.py", line 134, in render_template
    context, ctx.app)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\templating.py", line 116, in _render
    rv = template.render(context)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\jinja2\environment.py", line 1008, in render
    return self.environment.handle_exception(exc_info, True)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\jinja2\environment.py", line 780, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\jinja2\_compat.py", line 37, in reraise
    raise value.with_traceback(tb)
  File "D:\Users\kenny\Desktop\bpissue\app\templates\405.html", line 1, in top-level template code
    {% extends "bootstrap/base.html" %}
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_bootstrap\templates\bootstrap\base.html", line 1, in top-level template code
    {% block doc -%}
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_bootstrap\templates\bootstrap\base.html", line 4, in block "doc"
    {%- block html %}
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_bootstrap\templates\bootstrap\base.html", line 20, in block "html"
    {% block body -%}
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_bootstrap\templates\bootstrap\base.html", line 21, in block "body"
    {% block navbar %}
  File "D:\Users\kenny\Desktop\bpissue\app\templates\405.html", line 4, in block "navbar"
    {{ nav.topbar.render() }}
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_nav\elements.py", line 24, in render
    self))
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\visitor\__init__.py", line 48, in visit
    return meth(node)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_bootstrap\nav.py", line 42, in visit_Navbar
    href=node.title.get_url()))
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask_nav\elements.py", line 77, in get_url
    return url_for(self.endpoint, **self.url_for_kwargs)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\helpers.py", line 333, in url_for
    return appctx.app.handle_url_build_error(error, endpoint, values)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\app.py", line 1805, in handle_url_build_error
    reraise(exc_type, exc_value, tb)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\_compat.py", line 33, in reraise
    raise value
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\flask\helpers.py", line 323, in url_for
    force_external=external)
  File "D:\Users\kenny\Desktop\proj\venv\lib\site-packages\werkzeug\routing.py", line 1768, in build
    raise BuildError(endpoint, values, method, self)
werkzeug.routing.BuildError: Could not build url for endpoint 'home'. Did you mean 'bp.home' instead?
```
