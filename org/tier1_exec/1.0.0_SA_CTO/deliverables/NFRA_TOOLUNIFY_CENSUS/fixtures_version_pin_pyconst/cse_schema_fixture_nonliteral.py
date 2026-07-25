"""Fail-closed fixture: the constant is COMPUTED -- unevaluable without executing the module."""
def _compute():
    return "0.9"
SCHEMA_VERSION = _compute()
