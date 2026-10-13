"""MDPF_HEALGAP round 4, HG-t-16 criterion (b): the characteristics producer's handler serves a RE-ATTEMPT fire
(event {"require_partition": true}) only when the T-1 Bloomberg partition has landed and today's run is not already done,
and leaves the scheduled 13:25Z fire (event without the key) exactly as it was. Pure stub test: no AWS call, no network.

Handler under test: infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py
(override with HG_T16_HANDLER to grade a control copy).

Contract the handler must meet (the order's worker face states the same):
  - event without require_partition (the scheduled fire): NO S3 call; producer.main runs once.
  - event {"require_partition": true}: all S3 reads are list_objects_v2 calls made at CALL time, with the bucket and keys
    DERIVED from the producer module's own constants (producer.OUT_BUCKET, producer.OUT_KEY, producer.BBG_BUCKET,
    producer.BBG_CHARACTERISTICS_KEY, producer.BBG_MANIFEST_KEY) and the day from producer.resolve_bbg_as_of(). It makes NO
    head_object / get_object call. Presence of a key means an object whose Key equals it exactly (a sibling is not it).
      1. list OUT_KEY in OUT_BUCKET (MaxKeys 1): the object's LastModified UTC date == today UTC
                                                -> exactly one log line starting SKIP-COMPLETE; producer.main NOT called.
      2. list BBG_CHARACTERISTICS_KEY % <T-1> and BBG_MANIFEST_KEY % <T-1> in BBG_BUCKET: either absent
                                                -> exactly one log line starting PARTITION-ABSENT; producer.main NOT called.
      3. otherwise                              -> producer.main runs once.
    No raise on an absent partition or a complete day. AccessDenied on any listing propagates (a grant fault is loud, never
    read as "absent"); producer.main NOT called.

Last line: GATE-OK or GATE-BAD <reasons>. At the base this is GATE-BAD.
"""
from __future__ import annotations

import importlib.util
import logging
import os
import sys
import types
from datetime import datetime, timedelta, timezone
from pathlib import Path

HANDLER = Path(os.environ.get("HG_T16_HANDLER") or
               "infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py")
OUT_BUCKET, OUT_KEY = "opal-data-cot", "platinum/satellites/characteristics.json"
BBG_BUCKET = "opal-data-etfs"
BBG_CHAR, BBG_MAN = "bbg/%s/characteristics.parquet", "bbg/%s/run_manifest.json"
T1 = "2026-10-12"


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

    now = datetime.now(timezone.utc)
    state = {"list": [], "other": [], "main": 0, "out": "yesterday", "part": "both", "deny": None}

    class FakeS3:
        def list_objects_v2(self, **kw):
            state["list"].append(kw)
            bucket, key = kw.get("Bucket"), kw.get("Prefix", "")
            if state["deny"] == bucket:
                raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "ListObjectsV2")
            if bucket == OUT_BUCKET:
                mode = state["out"]
                if mode == "absent":
                    return {"KeyCount": 0}
                if mode == "sibling-today":
                    return {"KeyCount": 1, "Contents": [{"Key": key + ".bak", "LastModified": now}]}
                lm = now if mode == "today" else now - timedelta(days=1)
                return {"KeyCount": 1, "Contents": [{"Key": key, "LastModified": lm}]}
            if bucket == BBG_BUCKET:
                mode = state["part"]
                present = {"both": {BBG_CHAR % T1, BBG_MAN % T1}, "parquet-only": {BBG_CHAR % T1},
                           "manifest-only": {BBG_MAN % T1}, "none": set()}.get(mode, set())
                if mode == "sibling":
                    return {"KeyCount": 1, "Contents": [{"Key": key + ".tmp", "LastModified": now}]}
                if key in present:
                    return {"KeyCount": 1, "Contents": [{"Key": key, "LastModified": now}]}
                return {"KeyCount": 0}
            return {"KeyCount": 0}

        def head_object(self, **kw):
            state["other"].append(("head_object", kw))
            raise ClientError({"Error": {"Code": "403", "Message": "forbidden"}}, "HeadObject")

        def get_object(self, **kw):
            state["other"].append(("get_object", kw))
            raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "GetObject")

    real_client = boto3.client
    boto3.client = lambda *a, **k: FakeS3()

    fake = types.ModuleType("build_satellites_characteristics")
    fake.OUT_BUCKET, fake.OUT_KEY = OUT_BUCKET, OUT_KEY
    fake.BBG_BUCKET, fake.BBG_CHARACTERISTICS_KEY, fake.BBG_MANIFEST_KEY = BBG_BUCKET, BBG_CHAR, BBG_MAN
    fake.resolve_bbg_as_of = lambda clock=None: T1

    def _main(argv):
        state["main"] += 1
        return 0

    fake.main = _main
    sys.modules["build_satellites_characteristics"] = fake

    try:
        spec = importlib.util.spec_from_file_location("hg_t16_handler_under_test", str(HANDLER))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as exc:  # noqa: BLE001 - report, never mask
        boto3.client = real_client
        print(f"GATE-BAD handler does not import: {type(exc).__name__}: {exc}")
        return 1

    cap = _Capture()
    logging.getLogger().addHandler(cap)
    bad: list[str] = []

    def reset(**kw) -> None:
        state.update({"list": [], "other": [], "main": 0, "out": "yesterday", "part": "both", "deny": None})
        state.update(kw)
        cap.lines.clear()

    def call(event):
        try:
            mod.lambda_handler(event, None)
            return None
        except Exception as exc:  # noqa: BLE001
            return exc

    def lines(prefix):
        return [ln for ln in cap.lines if ln.startswith(prefix)]

    try:
        # A: the scheduled fire -- no S3 call, the producer runs
        reset()
        exc = call({})
        if exc is not None:
            bad.append(f"A: the scheduled event raised {type(exc).__name__}")
        if state["list"] or state["other"]:
            bad.append("A: the scheduled event made an S3 call")
        if state["main"] != 1:
            bad.append(f"A: producer.main ran {state['main']} times, want 1")

        # B: re-attempt, partition landed, not yet served today -> runs; reads are listings with derived keys
        reset()
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"B: a landed partition raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"B: partition landed and not complete, producer.main ran {state['main']} times, want 1")
        got = sorted((h.get("Bucket"), h.get("Prefix")) for h in state["list"])
        want = sorted([(OUT_BUCKET, OUT_KEY), (BBG_BUCKET, BBG_CHAR % T1), (BBG_BUCKET, BBG_MAN % T1)])
        if got != want:
            bad.append(f"B: list calls {got} != {want}")
        if state["other"]:
            bad.append("B: a head_object/get_object call was made (the grants allow a listing only)")

        # C: parquet landed, manifest absent -> both objects are required
        reset(part="parquet-only")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"C: a half-landed partition raised {type(exc).__name__}")
        if state["main"] != 0 or len(lines("PARTITION-ABSENT")) != 1:
            bad.append(f"C: manifest absent: main ran {state['main']}x, {len(lines('PARTITION-ABSENT'))} PARTITION-ABSENT lines (want 0 and 1)")

        # D: neither landed
        reset(part="none")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"D: an absent partition raised {type(exc).__name__}")
        if state["main"] != 0 or len(lines("PARTITION-ABSENT")) != 1:
            bad.append(f"D: partition absent: main ran {state['main']}x, {len(lines('PARTITION-ABSENT'))} PARTITION-ABSENT lines (want 0 and 1)")

        # E: today's run already served -> complete day, no-op (even with the partition landed)
        reset(out="today")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"E: a complete day raised {type(exc).__name__}")
        if state["main"] != 0 or len(lines("SKIP-COMPLETE")) != 1:
            bad.append(f"E: complete day: main ran {state['main']}x, {len(lines('SKIP-COMPLETE'))} SKIP-COMPLETE lines (want 0 and 1)")

        # F: AccessDenied on the output listing -- loud
        reset(deny=OUT_BUCKET)
        exc = call({"require_partition": True})
        if not isinstance(exc, ClientError):
            bad.append(f"F: AccessDenied on the output listing raised {type(exc).__name__ if exc else 'nothing'}, want the ClientError")
        if state["main"] != 0:
            bad.append(f"F: denied, producer.main ran {state['main']} times, want 0")

        # G: AccessDenied on the partition listing -- loud
        reset(deny=BBG_BUCKET)
        exc = call({"require_partition": True})
        if not isinstance(exc, ClientError):
            bad.append(f"G: AccessDenied on the partition listing raised {type(exc).__name__ if exc else 'nothing'}, want the ClientError")
        if state["main"] != 0:
            bad.append(f"G: denied, producer.main ran {state['main']} times, want 0")

        # H: a SIBLING of the output key is listed with today's LastModified -- it is not the output
        reset(out="sibling-today")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"H: a sibling output listing raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"H: only a sibling of the output listed, producer.main ran {state['main']} times, want 1 (exact key match)")

        # I: a SIBLING of the partition keys is listed -- it is not the partition
        reset(part="sibling")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"I: a sibling partition listing raised {type(exc).__name__}")
        if state["main"] != 0:
            bad.append(f"I: only a sibling of the partition listed, producer.main ran {state['main']} times, want 0 (exact key match)")
    finally:
        boto3.client = real_client
        logging.getLogger().removeHandler(cap)

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(scheduled, no S3) B(runs, listings only) C(half partition) D(no partition) E(complete day) "
          "F(403 output loud) G(403 partition loud) H(sibling output) I(sibling partition)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
