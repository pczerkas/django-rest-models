__VERSION__ = '1.1.0'

try:
    from rest_models.checks import register_checks
    register_checks()
except ImportError:
    pass