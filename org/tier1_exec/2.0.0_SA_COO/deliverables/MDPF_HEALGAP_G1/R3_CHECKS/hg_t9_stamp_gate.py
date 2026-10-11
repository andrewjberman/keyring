"""MDPF_HEALGAP round 3, HG-t-9 criterion (b): the satellites producer's handler gates the 13:15Z fire on the runner's
completion stamp, and leaves the 07:00Z fire unchanged. Pure stub test: no AWS call, no network.

Handler under test: infra/aws/lambda/cot-pipeline/cot-satellites-registry-producer/lambda_function.py

Contract the handler must meet (the order's worker face states the same; v2 after the CTO half refusal, msg 3485):
  - event {} (the 07:00Z fire): NO S3 call; producer.main runs once.
  - event {"require_stamp": true} (the 13:15Z fire): list_objects_v2(Bucket=producer.ASSETS_BUCKET,
    Prefix="<ROSTER_KEY prefix before /bronze/>/meta/<today UTC>-complete.json") is called at CALL time. The handler reads
    presence from the LISTING (an object whose Key equals the stamp key exactly). It DERIVES the bucket and the prefix from the
    producer module's own constants and types no firm or bucket literal (naming gate). It makes NO head_object / get_object call.
      listed             -> producer.main runs once.
      not listed         -> producer.main is NOT called; exactly one log line starting STAMP-ABSENT; the handler returns.
                            A listed SIBLING key (stamp key + a suffix) is "not listed".
      AccessDenied (403) -> the error propagates (a grant fault is loud, never read as an absent stamp); main NOT called.

Why a listing: an absent key under a HEAD or GET answers 403 unless the request itself satisfies a ListBucket grant, and an
s3:prefix condition is only populated on a list request. Last line: GATE-OK or GATE-BAD <reasons>. At the base this is GATE-BAD.
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

    state = {"list": [], "other": [], "main": 0, "mode": "listed"}

    class FakeS3:
        def list_objects_v2(self, **kw):
            state["list"].append(kw)
            mode, key = state["mode"], kw.get("Prefix", "")
            if mode == "listed":
                return {"KeyCount": 1, "Contents": [{"Key": key}]}
            if mode == "absent":
                return {"KeyCount": 0}
            if mode == "sibling":
                return {"KeyCount": 1, "Contents": [{"Key": key + ".tmp"}]}
            raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "ListObjectsV2")

        def head_object(self, **kw):
            state["other"].append(("head_object", kw))
            raise ClientError({"Error": {"Code": "403", "Message": "forbidden"}}, "HeadObject")

        def get_object(self, **kw):
            state["other"].append(("get_object", kw))
            raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "GetObject")

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

    cap = _Capture()
    logging.getLogger().addHandler(cap)
    bad: list[str] = []

    def reset(mode: str) -> None:
        state.update({"list": [], "other": [], "main": 0, "mode": mode})
        cap.lines.clear()

    try:
        # A: the 07:00Z fire -- no S3 call at all
        reset("listed")
        mod.lambda_handler({}, None)
        if state["list"] or state["other"]:
            bad.append("A: the 07:00Z event made an S3 call")
        if state["main"] != 1:
            bad.append(f"A: producer.main ran {state['main']} times, want 1")

        # B: the 13:15Z fire, stamp listed
        reset("listed")
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except Exception as exc:  # noqa: BLE001 - a HEAD-based handler dies here on the fake's 403; report it as a defect
            bad.append(f"B: the 13:15Z event raised {type(exc).__name__} on a present stamp")
        want = f"blackdiamond/cottonwood/meta/{_today()}-complete.json"
        got = [h.get("Prefix") for h in state["list"]]
        if got != [want]:
            bad.append(f"B: list_objects_v2 Prefix {got} != [{want!r}]")
        if any(h.get("Bucket") != BUCKET for h in state["list"]):
            bad.append("B: the list bucket is not opal-data-assets")
        if state["other"]:
            bad.append("B: a head_object/get_object call was made (the grant allows a listing only)")
        if state["main"] != 1:
            bad.append(f"B: stamp listed, producer.main ran {state['main']} times, want 1")

        # C: stamp not listed -- one log line, nothing rebuilt, no raise
        reset("absent")
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except Exception as exc:  # noqa: BLE001
            bad.append(f"C: an absent stamp raised {type(exc).__name__}")
        lines = [ln for ln in cap.lines if ln.startswith("STAMP-ABSENT")]
        if state["main"] != 0:
            bad.append(f"C: stamp absent, producer.main ran {state['main']} times, want 0")
        if len(lines) != 1:
            bad.append(f"C: {len(lines)} log lines start STAMP-ABSENT, want exactly 1")

        # D: AccessDenied on the listing -- loud, nothing rebuilt
        reset("denied")
        raised = None
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except ClientError as exc:
            raised = exc
        except Exception as exc:  # noqa: BLE001
            bad.append(f"D: raised {type(exc).__name__}, want the ClientError itself")
        if raised is None and not any(b.startswith("D: raised") for b in bad):
            bad.append("D: AccessDenied on the listing did not raise (a grant fault read as an absent stamp)")
        if state["main"] != 0:
            bad.append(f"D: denied, producer.main ran {state['main']} times, want 0")

        # E: a SIBLING key is listed (stamp key + suffix) -- it is not the stamp
        reset("sibling")
        try:
            mod.lambda_handler({"require_stamp": True}, None)
        except Exception as exc:  # noqa: BLE001
            bad.append(f"E: a sibling listing raised {type(exc).__name__}")
        if state["main"] != 0:
            bad.append(f"E: only a sibling key listed, producer.main ran {state['main']} times, want 0 (exact key match)")
    finally:
        boto3.client = real_client
        logging.getLogger().removeHandler(cap)

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(no S3 call) B(listed) C(absent) D(403 loud) E(sibling not the stamp)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
