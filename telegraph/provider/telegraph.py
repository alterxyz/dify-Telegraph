from typing import Any

from ytelegraph import TelegraphAPI

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class TelegraphProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            IMPLEMENT YOUR VALIDATION HERE
            """
            pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
