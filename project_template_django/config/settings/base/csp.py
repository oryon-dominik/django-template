# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# --------------------

# The project_url will use the PROJECT_FQDN and the PROJECT_FRONTEND_FQDN normally.
# We hardcode it here, since we don't want to depend on environs in this file.
# AND: it is not used anywhere anyways for now (because relying on 'self' usally is enough).
project_url = "http://localhost:8000"

# Content-Security-Policy: https://www.w3.org/TR/CSP/
# See https://django-csp.readthedocs.io/en/latest/configuration.html
# Using: https://github.com/mozilla/django-csp
SELF = "'self'"
# CSP: default-src
# serves as a fallback for the other CSP fetch directives. For each of the following directives that are absent, the
# user agent looks for the default-src directive and uses this value for it:
# child-src, connect-src, font-src, frame-src, img-src, manifest-src, media-src, object-src, prefetch-src, script-src,
# script-src-elem, script-src-attr, style-src, style-src-elem, style-src-attr, worker-src
# example: ("'self'", f"ws://{PROJECT_FQDN.netloc}")
CSP_DEFAULT_SRC = ("'none'",)  # be as strict as possible
# CSP_DEFAULT_SRC = (SELF, project_url)
# CSP: connect-src
# connect-src directive restricts the URLs which can be loaded using script interfaces.
# The APIs that are restricted are:
# <a> ping, fetch(), XMLHttpRequest, WebSocket, EventSource, and Navigator.sendBeacon().
# Note: connect-src 'self' does not resolve to websocket schemes in all browsers, more info in this issue.
# example: (f"ws://{PROJECT_FQDN.netloc}",)
CSP_CONNECT_SRC = (SELF,)
# CSP_CONNECT_SRC = (SELF, project_url)
# CSP: style-src
# The HTTP Content-Security-Policy (CSP) style-src directive specifies valid sources for stylesheets.
# ! Tailwind needs unsafe-inline. TBD: add the nonce to the style tag. ({% verbatim {{request.csp_nonce}}{% endverbatim %})
CSP_STYLE_SRC = (
    "'unsafe-inline'",
    SELF,
    # project_url,
)  # "https://fonts.googleapis.com/",)
# CSP: img-src
# The HTTP Content-Security-Policy img-src directive specifies valid sources of images and favicons.
CSP_IMG_SRC = (SELF,)  # project_url)
# CSP: font-src
# The HTTP Content-Security-Policy (CSP) font-src directive specifies valid sources for fonts loaded with @font-face.
CSP_FONT_SRC = (SELF,)  # 'fonts.gstatic.com')
# CSP: script-src
# The HTTP Content-Security-Policy (CSP) script-src directive specifies valid sources for JavaScript. This includes not
# only URLs loaded directly into <script> elements, but also things like inline script event handlers (onclick) and
# XSLT stylesheets which can trigger script execution.
CSP_SCRIPT_SRC = (SELF,)  # project_url)
CSP_SCRIPT_SRC = (
    # SELF,
    # Alpine and tailwind both need unsafe-inline CSP.
    # Alpine-js needs unsafe-eval as well.
    # Alpine.js [offers a mitigation for unsafe-eval](https://alpinejs.dev/advanced/csp)
    # this is not yet implemented and you will loose some features of alpine.
    # "'unsafe-inline'",
    "'unsafe-eval'",
    # f"{project_url}",
    # "cdn.tailwindcss.com",  # tailwind cdn
    # "cdn.jsdelivr.net",  # alpine cdn
    # "unpkg.com",  # htmx cdn
)
# CSP: worker-src
# The HTTP Content-Security-Policy (CSP) worker-src directive specifies valid sources for Workers or SharedWorkers.
CSP_WORKER_SRC = (SELF,)
