SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 14  # (2 weeks, in seconds)
SESSION_CACHE_ALIAS = "sessions"
SESSION_ENGINE = "django.contrib.sessions.backends.db"
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# Be attentive when using signed cookies, as they are not encrypted and can be
# read by the client. This opens some attack vector for [replay-attacks](https://en.wikipedia.org/wiki/Replay_attack).
# SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
