"""MDPF_HEALGAP round 4, HG-t-16 criterion (b): the characteristics producer's handler serves a RE-ATTEMPT fire
(event {"require_partition": true}) only when its holdings input is final for today, the T-1 Bloomberg partition has landed
and its own output is older than that holdings, and leaves the scheduled 13:25Z fire (event without the key) exactly as it was.
Pure stub test: no AWS call, no network.

Handler under test: infra/aws/lambda/cot-pipeline/cot-satellites-characteristics-producer/lambda_function.py
(override with HG_T16_HANDLER to grade a control copy).

Contract the handler must meet (the order's worker face states the same):
  - event without require_partition (the scheduled fire): NO S3 call; producer.main runs once.
  - event {"require_partition": true}: all S3 reads are list_objects_v2 calls made at CALL time, with the bucket and keys
    DERIVED from the producer module's own constants (producer.HOLDINGS_BUCKET, HOLDINGS_KEY, OUT_BUCKET, OUT_KEY,
    BBG_BUCKET, BBG_CHARACTERISTICS_KEY, BBG_MANIFEST_KEY) and the day from producer.resolve_bbg_as_of(). It makes NO
    head_object / get_object call. Presence of a key means an object whose Key equals it exactly (a sibling is not it).
      1. list HOLDINGS_KEY (MaxKeys 1): not listed, or its LastModified UTC date != today UTC
                                         -> exactly one log line starting HOLDINGS-NOT-FINAL; producer.main NOT called.
                                            (The registry producer's stamp-gated 13:15Z fire has not made today's
                                            holdings.json; the scheduled 13:25Z fire is the only run until it has.)
      2. list OUT_KEY: listed with LastModified >= the holdings' LastModified
                                         -> exactly one log line starting SKIP-COMPLETE; producer.main NOT called.
      3. list BBG_CHARACTERISTICS_KEY % <T-1> and BBG_MANIFEST_KEY % <T-1>: either not listed
                                         -> exactly one log line starting PARTITION-ABSENT; producer.main NOT called.
      4. otherwise                       -> producer.main runs once.
    No raise on a not-final holdings, an absent partition or a complete day. AccessDenied on any listing propagates (a
    grant fault is loud, never read as "absent"); producer.main NOT called.

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
COT = "opal-data-cot"
OUT_KEY, HOLDINGS_KEY = "platinum/satellites/characteristics.json", "platinum/satellites/holdings.json"
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

    midnight = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    t_hold = midnight + timedelta(minutes=10)      # today 00:10Z: the holdings the 13:15Z fire wrote (stand-in time)
    t_out_new = midnight + timedelta(minutes=20)   # an output written after it
    t_old = midnight - timedelta(minutes=10)       # yesterday 23:50Z
    state = {"list": [], "other": [], "main": 0, "hold": "today", "out": "older", "part": "both", "deny": None}

    class FakeS3:
        def list_objects_v2(self, **kw):
            state["list"].append(kw)
            bucket, key = kw.get("Bucket"), kw.get("Prefix", "")
            if state["deny"] == bucket:
                raise ClientError({"Error": {"Code": "AccessDenied", "Message": "denied"}}, "ListObjectsV2")
            if bucket == COT and key == HOLDINGS_KEY:
                mode = state["hold"]
                if mode == "absent":
                    return {"KeyCount": 0}
                return {"KeyCount": 1, "Contents": [{"Key": key, "LastModified": t_hold if mode == "today" else t_old}]}
            if bucket == COT and key == OUT_KEY:
                mode = state["out"]
                if mode == "absent":
                    return {"KeyCount": 0}
                if mode == "sibling-newer":
                    return {"KeyCount": 1, "Contents": [{"Key": key + ".bak", "LastModified": t_out_new}]}
                lm = {"newer": t_out_new, "same": t_hold, "older": t_old,
                      "older-today": midnight + timedelta(minutes=5)}[mode]
                return {"KeyCount": 1, "Contents": [{"Key": key, "LastModified": lm}]}
            if bucket == BBG_BUCKET:
                mode = state["part"]
                if mode == "sibling":
                    return {"KeyCount": 1, "Contents": [{"Key": key + ".tmp", "LastModified": midnight}]}
                present = {"both": {BBG_CHAR % T1, BBG_MAN % T1}, "parquet-only": {BBG_CHAR % T1},
                           "manifest-only": {BBG_MAN % T1}, "none": set()}.get(mode, set())
                if key in present:
                    return {"KeyCount": 1, "Contents": [{"Key": key, "LastModified": midnight}]}
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
    fake.HOLDINGS_BUCKET, fake.HOLDINGS_KEY = COT, HOLDINGS_KEY
    fake.OUT_BUCKET, fake.OUT_KEY = COT, OUT_KEY
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
        state.update({"list": [], "other": [], "main": 0, "hold": "today", "out": "older", "part": "both", "deny": None})
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

    def expect_skip(tag, token, **kw):
        reset(**kw)
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"{tag}: raised {type(exc).__name__}, want a clean skip")
        if state["main"] != 0 or len(lines(token)) != 1:
            bad.append(f"{tag}: main ran {state['main']}x, {len(lines(token))} {token} lines (want 0 and 1)")

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

        # B: re-attempt, holdings final today, output older than it, partition landed -> runs; reads are listings with derived keys
        reset()
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"B: a due re-attempt raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"B: due re-attempt, producer.main ran {state['main']} times, want 1")
        got = sorted((h.get("Bucket"), h.get("Prefix")) for h in state["list"])
        want = sorted([(COT, HOLDINGS_KEY), (COT, OUT_KEY), (BBG_BUCKET, BBG_CHAR % T1), (BBG_BUCKET, BBG_MAN % T1)])
        if got != want:
            bad.append(f"B: list calls {got} != {want}")
        if state["other"]:
            bad.append("B: a head_object/get_object call was made (the grants allow a listing only)")

        expect_skip("C", "PARTITION-ABSENT", part="parquet-only")      # manifest absent: both objects are required
        expect_skip("D", "PARTITION-ABSENT", part="none")
        expect_skip("E", "SKIP-COMPLETE", out="newer")                 # output written after the holdings
        expect_skip("E2", "SKIP-COMPLETE", out="same")                 # equal LastModified counts as complete
        expect_skip("F", "HOLDINGS-NOT-FINAL", hold="yesterday")       # 13:15Z fire has not made today's holdings
        expect_skip("N", "HOLDINGS-NOT-FINAL", hold="yesterday", part="none")   # the holdings test comes first
        expect_skip("G", "HOLDINGS-NOT-FINAL", hold="absent")

        # H, I: AccessDenied on a listing -- loud
        for tag, bucket in (("H", COT), ("I", BBG_BUCKET)):
            reset(deny=bucket)
            exc = call({"require_partition": True})
            if not isinstance(exc, ClientError):
                bad.append(f"{tag}: AccessDenied on {bucket} raised {type(exc).__name__ if exc else 'nothing'}, want the ClientError")
            if state["main"] != 0:
                bad.append(f"{tag}: denied, producer.main ran {state['main']} times, want 0")

        # J: a SIBLING of the output key is listed with a newer time -- it is not the output, so the day is not complete
        reset(out="sibling-newer")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"J: a sibling output listing raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"J: only a sibling of the output listed, producer.main ran {state['main']} times, want 1 (exact key match)")

        expect_skip("K", "PARTITION-ABSENT", part="sibling")           # a sibling of the partition keys is not the partition

        # M: the output was written TODAY but BEFORE the holdings were made final: not complete (a same-day test would skip)
        reset(out="older-today")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"M: an output older than its holdings raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"M: output written today but before the holdings, producer.main ran {state['main']} times, want 1")

        # L: no output at all (first run) with holdings final and the partition landed -> runs
        reset(out="absent")
        exc = call({"require_partition": True})
        if exc is not None:
            bad.append(f"L: an absent output raised {type(exc).__name__}")
        if state["main"] != 1:
            bad.append(f"L: output absent, producer.main ran {state['main']} times, want 1")
    finally:
        boto3.client = real_client
        logging.getLogger().removeHandler(cap)

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(scheduled, no S3) B(runs, listings only) C(half partition) D(no partition) E(output newer) "
          "E2(equal) F(holdings yesterday) G(holdings absent) H(403 cot loud) I(403 etfs loud) J(sibling output) "
          "K(sibling partition) L(no output) M(output today, older than holdings) N(holdings tested first)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
