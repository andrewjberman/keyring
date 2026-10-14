"""MDPF_SECHIST round 6, FWD-9 QA replay (CTO ADDENDUM 1 of round 5, corrected @f443ae70d2 by msg 5542): drive the money-market null arm
without waiting on the vendor, and never write a served key.

Runs the DEPLOYED rule (data/etfs/scripts/gold/etf_positioning_gold.py: load_history + compute_returns, same blob as the pin deployed to
etf-positioning-producer) over the real bbg history, with SALXX and FXFXX blanked on D in an IN-MEMORY copy. Reads S3; the S3 client is wrapped so
any call other than get_object / list_objects_v2 / head_object raises. Output is a local JSON file only (no QA prefix: a new S3 address is a
naming-registry matter, and a local sink is stricter than the prefix the ruling allowed).

  python r6_fwd9_replay.py run <D> <out.json>
  python r6_fwd9_replay.py verify <out.json>   (reads a recorded run; last line FWD9-QA-VERIFY-OK or FWD9-QA-VERIFY-BAD <reason>)
Arms (C-MMF: a null day blanks every window that contains it, never estimated, until a later partition fills it):
  b   control: the unmodified history -> SALXX/FXFXX windows equal the SERVED page's returns for D (data_as_of == D required).
  a   D blanked for SALXX/FXFXX -> every window of those two funds reads None; a non-money-market ticker is unchanged.
  a2  D blanked, then a later row fills it (the re-request) -> windows equal the control.
  c   a fund absent from the history -> all windows None, recorded as-is (no reason field exists in compute_returns).
Also: the deployed blob identity (HEAD blob == blob at pin 09b6a7d580; live CodeSha256 printed) and served-prefix listing equal before and after.
Last line: FWD9-QA-OK ... or FWD9-QA-BAD <reason>.
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import boto3
import pandas as pd

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "gold"))
sys.path.insert(0, str(ROOT / "data" / "etfs" / "scripts" / "silver"))
import etf_positioning_gold as M  # noqa: E402

SERVED_BUCKET = "opal-data-portal-v2"
SERVED_PREFIX = "platinum/etfs/"
SERVED_KEY = "platinum/etfs/positioning_data.json"
PIN = "09b6a7d580"
GOLD_PATH = "data/etfs/scripts/gold/etf_positioning_gold.py"
MMF = ("SALXX", "FXFXX")
RET = M.MMF_DAILY_RETURN_COL
WINDOWS = M.RETURN_WINDOWS
ALLOWED = ("get_object", "list_objects_v2", "head_object", "exceptions", "meta")


class ReadOnlyS3:
    def __init__(self, real):
        self._real = real
        self.calls = []

    def __getattr__(self, name):
        if name not in ALLOWED:
            raise RuntimeError("READ-ONLY GUARD: refused S3 call " + name)
        self.calls.append(name)
        return getattr(self._real, name)


def _blob(ref):
    return subprocess.check_output(["git", "rev-parse", ref + ":" + GOLD_PATH], text=True, cwd=ROOT).strip()


def _served_listing(s3):
    rows, token = [], None
    while True:
        kw = {"Bucket": SERVED_BUCKET, "Prefix": SERVED_PREFIX}
        if token:
            kw["ContinuationToken"] = token
        r = s3.list_objects_v2(**kw)
        rows += [(o["Key"], o["ETag"], o["LastModified"].isoformat()) for o in r.get("Contents", [])]
        if not r.get("IsTruncated"):
            break
        token = r.get("NextContinuationToken")
    return sorted(rows)


def _tkr(sec):
    return str(sec).split(" ")[0].strip().upper()


def main(day, out_path):
    d = dt.date.fromisoformat(day)
    real = boto3.client("s3")
    guard = ReadOnlyS3(real)
    M._s3 = lambda: guard
    out = {"D": day, "arms": {}}

    head_blob, pin_blob = _blob("HEAD"), _blob(PIN)
    out["gold_blob_head"], out["gold_blob_pin"] = head_blob, pin_blob
    lam = boto3.client("lambda", region_name="us-east-1").get_function_configuration(FunctionName="etf-positioning-producer")
    out["lambda_code_sha256"], out["lambda_last_modified"] = lam["CodeSha256"], lam["LastModified"]
    print("gold blob HEAD=" + head_blob + " pin=" + pin_blob + " lambda CodeSha256=" + lam["CodeSha256"] + " " + lam["LastModified"])
    if head_blob != pin_blob:
        print("FWD9-QA-BAD gold-blob-head-differs-from-deployed-pin")
        return 1

    before = _served_listing(guard)
    print("served prefix " + SERVED_PREFIX + " objects before: " + str(len(before)))

    # in-memory cache + per-arm transform of the D partition's history_topup
    d_key = M._bbg_key(d, "history_topup.parquet")
    orig_read = M._read_parquet
    cache = {}
    mode = {"m": "control"}

    def read(bucket, key, required=True):
        if key not in cache:
            cache[key] = orig_read(bucket, key, required)
        df = cache[key]
        if key != d_key or df is None or mode["m"] == "control":
            return df
        df = df.copy()
        is_mmf = df["security"].map(_tkr).isin(MMF) & (pd.to_datetime(df["date"]).dt.date == d)
        if int(is_mmf.sum()) == 0:
            raise RuntimeError("no SALXX/FXFXX row on D in " + key)
        blanked = df.copy()
        blanked.loc[is_mmf, RET] = float("nan")
        if mode["m"] == "blank":
            return blanked
        return pd.concat([blanked, df[is_mmf]], ignore_index=True)  # a later row fills D (the re-request)

    M._read_parquet = read
    gap = M.load_gap_record(d)

    def windows(label):
        hist = M.load_history(d)
        res = {t: M.compute_returns(t, d, hist, gap) for t in MMF}
        other = next(t for t in sorted(hist["tkr"].unique()) if t not in MMF and M.compute_returns(t, d, hist, gap)["1D"] is not None)
        res[other] = M.compute_returns(other, d, hist, gap)
        res["ZZQAABSENT"] = M.compute_returns("ZZQAABSENT", d, hist, gap)
        print(label + ": " + json.dumps(res, sort_keys=True))
        windows.hist = hist
        return res, other

    mode["m"] = "control"
    ctl, other = windows("control")
    ctl_hist = windows.hist
    mode["m"] = "blank"
    blk, other_b = windows("blank")
    mode["m"] = "fill"
    fil, _ = windows("fill")
    out["control"], out["blank"], out["fill"], out["non_mmf_ticker"] = ctl, blk, fil, other

    # served page for D
    page = json.loads(real.get_object(Bucket=SERVED_BUCKET, Key=SERVED_KEY)["Body"].read())
    out["served_data_as_of"] = page.get("data_as_of")
    if page.get("data_as_of") != day:
        print("FWD9-QA-BAD served-as_of-not-D served=" + str(page.get("data_as_of")))
        return 1
    seen = {}
    for code, p in (page.get("portfolios") or {}).items():
        for h in p.get("holdings") or []:
            if h.get("ticker") in MMF:
                seen.setdefault(h["ticker"], []).append((code, p.get("data_as_of"), h.get("returns") or {}))
    out["served_mmf_holdings"] = {t: [(c, a) for c, a, _ in v] for t, v in seen.items()}
    if "SALXX" not in seen:
        print("FWD9-QA-BAD SALXX-not-in-served-page")
        return 1

    bad = []
    compared = 0
    for t, rows in seen.items():  # (b) control equals served, at each book's OWN as_of (the gold computes a book at its own as_of)
        for code, book_as_of, rets in rows:
            ref = ctl[t] if book_as_of == day else M.compute_returns(t, dt.date.fromisoformat(book_as_of), ctl_hist, gap)
            for w in WINDOWS:
                sv, cv = rets.get(w), ref[w]
                compared += 1
                if (sv is None) != (cv is None) or (sv is not None and abs(float(sv) - cv) > 1e-6):
                    bad.append("b:" + t + "/" + code + "@" + str(book_as_of) + "/" + w + " served=" + str(sv) + " control=" + str(cv))
    out["b_compared_cells"] = compared
    print("arm b compared " + str(compared) + " served cells to the control at each book's own as_of")
    for t in MMF:  # (a) blanked -> every window None
        if any(blk[t][w] is not None for w in WINDOWS):
            bad.append("a:" + t + " window not blank")
        if fil[t] != ctl[t]:  # (a2) later fill -> equal to the control
            bad.append("a2:" + t + " fill != control")
    if blk[other_b] != ctl[other]:
        bad.append("a:non-mmf " + other + " moved when MMF blanked")
    if ctl["SALXX"]["1D"] is None:
        bad.append("b:control SALXX 1D is None (control must be populated)")
    if any(v is not None for v in ctl["ZZQAABSENT"].values()):
        bad.append("c:absent fund not all-null")

    after = _served_listing(guard)
    writes = 0 if after == before else len(set(after) ^ set(before))
    out["served_objects_before"], out["served_objects_after"], out["served_writes"] = len(before), len(after), writes
    out["s3_calls"] = sorted(set(guard.calls))
    print("served prefix objects after: " + str(len(after)) + " writes=" + str(writes) + " s3 calls used: " + ",".join(out["s3_calls"]))
    if writes:
        bad.append("served prefix changed during the replay")
    out["problems"] = bad
    Path(out_path).write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if bad:
        print("FWD9-QA-BAD " + "; ".join(bad))
        return 1
    print("FWD9-QA-OK D=" + day + " arms=b,a,a2,c served_writes=0")
    return 0


def verify(path):
    try:
        o = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print("FWD9-QA-VERIFY-BAD cannot-read " + str(path) + " " + type(exc).__name__)
        return 1
    why = []
    if o.get("problems") != []:
        why.append("problems=" + str(o.get("problems")))
    if o.get("served_writes") != 0:
        why.append("served_writes=" + str(o.get("served_writes")))
    if o.get("gold_blob_head") != o.get("gold_blob_pin") or not o.get("gold_blob_head"):
        why.append("gold blob head!=pin")
    for t in MMF:
        if not o.get("control") or not o.get("blank") or not o.get("fill"):
            why.append("missing arm")
            break
        if any(v is not None for v in o["blank"][t].values()):
            why.append("blank arm not blank for " + t)
        if o["fill"][t] != o["control"][t]:
            why.append("fill != control for " + t)
    if not o.get("b_compared_cells"):
        why.append("arm b compared no cells")
    if why:
        print("FWD9-QA-VERIFY-BAD " + "; ".join(why))
        return 1
    print("FWD9-QA-VERIFY-OK D=" + str(o.get("D")) + " cells=" + str(o["b_compared_cells"]) + " served_writes=0")
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "verify":
        sys.exit(verify(sys.argv[2]))
    if len(sys.argv) != 4 or sys.argv[1] != "run":
        print("FWD9-QA-BAD usage: r6_fwd9_replay.py run <D> <out.json>")
        sys.exit(2)
    sys.exit(main(sys.argv[2], sys.argv[3]))
