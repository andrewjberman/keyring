"""The one real run of AR-t-32: the real handler entry (lambda_handler.lambda_handler) on a fake queue message, with the root logger
set the way the Lambda Python runtime sets it (WARNING, one handler that prints). Nothing else is configured: no caplog, no level on
the module logger. Prints what the runtime's handler would write to CloudWatch."""
import logging
import sys

sys.path.insert(0, ".")


class _Runtime(logging.Handler):
    def __init__(self):
        super().__init__()
        self.lines = []

    def emit(self, record):
        self.lines.append("[%s] %s" % (record.levelname, record.getMessage()))


root = logging.getLogger()
root.setLevel(logging.WARNING)
runtime = _Runtime()
root.addHandler(runtime)

from data.transcripts.scripts.commentary import lambda_handler as lh  # noqa: E402  (imported AFTER the root is set, as the runtime does)
from data.transcripts.scripts.tests.test_commentary_composition_port import _ports, _ready_body, _sqs  # noqa: E402
from data.transcripts.scripts.tests.test_commentary_route_switch import DRAFT_TEXT, Poster, _store  # noqa: E402

store, _ = _store()
ports, _ = _ports(lambda prompt: DRAFT_TEXT, store=store)
ports["post"], ports["token_reader"] = Poster(200), lambda: "tok"
out = lh.lambda_handler(_sqs(_ready_body()), None, ports=ports)
print("stage:", out["results"][0]["stage"])
print("root level:", logging.getLevelName(root.level), "| module logger effective level:", logging.getLevelName(lh.LOG.getEffectiveLevel()))
for line in runtime.lines:
    print("runtime handler wrote:", line)
ok = any("COMMENTARY-POST" in ln and "outcome=POSTED" in ln for ln in runtime.lines)
print("R42-REAL-RUN-" + ("OK" if ok else "FAIL"))
sys.exit(0 if ok else 1)
