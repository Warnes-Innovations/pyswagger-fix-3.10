__version__ = '0.8.39-patched'

from .getter import Getter
from .core import App, Security

# backward compatible
SwaggerApp = App
SwaggerSecurity = Security
SwaggerAuth = SwaggerSecurity

