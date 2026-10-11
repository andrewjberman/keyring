"""MDPF_HEALGAP round 3, HG-t-9 criterion (b): the satellites producer's handler gates the 13:15Z fire on the runner's
completion stamp, and leaves the 07:00Z fire unchanged. Pure stub test: no AWS call, no network.

Handler under test: infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py

Contract the handler must meet (the order's worker face states the same):
  - event {} (the 07:00Z fire): NO S3 call; producer.main runs once.
  - event {"require_stamp": true} (the 13:15Z fire): head_object(Bucket=producer.ASSETS_BUCKET,
    Key="<ROSTER_KEY prefix before /bronze/>/meta/<today UTC>-complete.json") is called at CALL time. The handler DERIVES
    the bucket and the prefix from the producer module's own constants and types no firm or bucket literal (naming gate).
      present            -> producer.main runs once.
      404 / NoSuchKey    -> producer.main is NOT called; exactly one log line starting STAMP-ABSENT; the handler returns.
      any other error    -> the error propagates (a grant fault is loud, never read as an absent stamp); main NOT called.

Last line: GATE-OK or GATE-BAD <reasons>. At the base (no stamp logic) this prints GATE-BAD.
"""
from __future__ import annotations

import importlib.util
import logging
import os
import sys
import types
from datetime import datetime, timezone
from pathlib import Path

HANDLER = Path(os.environ.get("HG_T9_HANDLER") or "infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py")
BUCKET = "opal-data-assets"


def _today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


class _Capture(logging.Handler):
    def __init__(self) -> None:
        super().__init__()
        self.lines: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.lines.append(record.getMessage())


def main() -> int:
    if not HANDLER.is_file():
        print(f"GATE-BAD no handler file {HANDLER}")
        return 1
    import boto3
    from botocore.exceptions import ClientError

    state = {"head": [], "main": 0, "mode": "present"}

    class FakeS3:
        def head_object(self, **kw):
            state["head"].append(kw)
            mode = state["mode"]
            if mode == "present":
                return {"ContentLength": 1}
            code = {"absent": "404", "denied": "403"}[mode]
            raise ClientError({"Error": {"Code": code, "Message": mode}}, "HeadObject")

    real_client = boto3.client
    boto3.client = lambda *a, **k: FakeS3()  # import-time AND call-time client creation both land on the fake

    fake_producer = types.ModuleType("build_satellites_registry")
    fake_producer.ASSETS_BUCKET = "opal-data-assets"
    fake_producer.ROSTER_KEY = "blackdiamond/cottonwood/bronze/rebalancer_models/%s/page_000.json"
    fake_producer.REGISTRY_BUCKET = "opal-data-cot"
    fake_producer.REGISTRY_KEY = "platinum/satellites/registry.json"
    fake_producer.HOLDINGS_KEY = "platinum/satellites/holdings.json"

    def _main(argv):
        state["main"] += 1
        return 0

    fake_producer.main = _main
    sys.modules["build_satellites_registry"] = fake_producer

    try:
        spec = importlib.util.spec_from_file_location("hg_t9_handler_under_test", str(HANDLER))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as exc:  # noqa: BLE001 - report, never mask
        boto3.client = real_client
        print(f"GATE-BAD handler does not import: {type(exc).__name__}: {exc}")
        return 1
    finally:
        pass

    cap = _Capture()
    logging.getLogger().addHandler(cap)
    bad: list[str] = []
    try:
        # A: the 07:00Z fire -- no stamp read at all
        state.update(head=[], main=0, mode="present")
        mod.lambda_handler({}, None)
        if state["head"]:
            bad.append("A: the 07:00Z event made an S3 call")
        if state["main"] != 1:
            bad.append(f"A: producer.main ran {state['main']} times, want 1")

        # B: the 13:15Z fire, stamp present
        state.update(head=[], main=0, mode="present")
        mod.lambda_handler({"require_stamp": True}, None)
        want = {f"blackdiamond/cottonwood/meta/{_today()}-complete.json"}
        got = {h.get("Key") for h in state["head"]}
        if not got or not got <= want | {f"blackdiamond/cottonwood/meta/{_today()}-complete.json"}:
            bad.append(f"B: head_object keys {sorted(got)} != {sorted(want)}")
        if any(h.get("Bucket") != BUCKET for h in state["head"]):
            bad.append("B: head_object bucket is not opal-data-assets")
        if state["main"] != 1:
            bad.append(f"B: stamp present, producer.main ran {state['main']} times, want 1")

        # C: stamp absent (404) -- one log line, nothing rebuilt
        state.update(head=[], main=0, mode="absent")
        cap.lines.clear()
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except Exception as exc:  # noqa: BLE001
            bad.append(f"C: an absent stamp raised {type(exc).__name__}")
        absent_lines = [ln for ln in cap.lines if ln.startswith("STAMP-ABSENT")]
        if state["main"] != 0:
            bad.append(f"C: stamp absent, producer.main ran {state['main']} times, want 0")
        if len(absent_lines) != 1:
            bad.append(f"C: {len(absent_lines)} log lines start STAMP-ABSENT, want exactly 1")

        # D: any other error (403) -- loud, nothing rebuilt
        state.update(head=[], main=0, mode="denied")
        raised = None
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except ClientError as exc:
            raised = exc
        except Exception as exc:  # noqa: BLE001
            bad.append(f"D: raised {type(exc).__name__}, want the ClientError itself")
        if raised is None and not any(b.startswith("D: raised") for b in bad):
            bad.append("D: a 403 on the stamp read did not raise (a grant fault read as an absent stamp)")
        if state["main"] != 0:
            bad.append(f"D: 403, producer.main ran {state['main']} times, want 0")
    finally:
        boto3.client = real_client
        logging.getLogger().removeHandler(cap)

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(no stamp read) B(present) C(404 absent) D(403 loud)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
