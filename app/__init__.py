from flask import Flask, request, redirect

app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False

app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    '9a32e65b0a283c022ff2f43a80211a2cac557516d3b60c2702ab940323806cde'

app.config['JSON_AS_ASCII'] = False

@app.before_request
def remove_trailing_slash():
   # Check if the path ends with a slash but is not the root "/"
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path[:-1], code=308)


from app import views  # noqa
