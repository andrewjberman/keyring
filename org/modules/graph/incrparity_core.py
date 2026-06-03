"""Core diff logic for comp-incrparity.

Importable from tests without the CLI wrapper. S3 client is always injected
(tests pass a fake). The CLI constructs the real boto3 client.

Canonical spec: docs/architecture/INCREMENTAL_RUNS_DESIGN.md Section 5.
"""

from __future__ import annotations

import dataclasses
import io
import json
import math
from dataclasses import dataclass, field

S3_BUCKET = "opal-data-bd"
PARITY_PREFIX = "gold/_parity"
PARITY_REPORTS_PREFIX = "gold/_parity_reports"
PROMOTED_LIST_KEY = "gold/meta/incremental_promoted.json"

NUMERIC_TOLERANCE_DEEP = 0.01  # $0.01 per PRD Section 5


@dataclass
class Divergence:
    path: str                # JSON path or parquet (row,col) coordinate
    kind: str                # "value_diff" | "key_missing_left" | "key_missing_right" | "byte_diff"
    left: object = None
    right: object = None
    detail: str = ""

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclass
class DiffResult:
    script_id: str
    mode: str
    full_prefix: str
    incremental_prefix: str
    divergences: list[Divergence] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    # absence != PASS: a script with NO dual-run parity comparison performed
    # (not registered) is UNVERIFIED, not "PARITY OK". Distinct from passed/failed.
    unverified: bool = False

    @property
    def passed(self) -> bool:
        # Unverified is NOT passed -- no comparison ran, so we cannot assert parity.
        return not self.divergences and not self.errors and not self.unverified

    def summary(self) -> str:
        if self.unverified:
            return (f"PARITY UNVERIFIED: {self.script_id} ({self.mode}) - "
                    f"no dual-run comparison performed (not registered); NOT a pass")
        if self.passed:
            return f"PARITY OK: {self.script_id} ({self.mode}) - 0 divergences"
        return (
            f"PARITY FAIL: {self.script_id} ({self.mode}) - "
            f"{len(self.divergences)} divergences, {len(self.errors)} errors"
        )

    def to_dict(self) -> dict:
        return {
            "script_id": self.script_id,
            "mode": self.mode,
            "full_prefix": self.full_prefix,
            "incremental_prefix": self.incremental_prefix,
            "passed": self.passed,
            "unverified": self.unverified,
            "divergences": [d.to_dict() for d in self.divergences],
            "errors": list(self.errors),
        }


# --------------------------------------------------------------------------
# S3 listing + fetching (inject-friendly)
# --------------------------------------------------------------------------

def list_keys(bucket: str, prefix: str, s3) -> list[str]:
    out: list[str] = []
    token: str | None = None
    while True:
        kwargs = {"Bucket": bucket, "Prefix": prefix}
        if token:
            kwargs["ContinuationToken"] = token
        resp = s3.list_objects_v2(**kwargs)
        for entry in resp.get("Contents", []) or []:
            out.append(entry["Key"])
        if not resp.get("IsTruncated"):
            break
        token = resp.get("NextContinuationToken")
    return sorted(out)


def fetch_bytes(bucket: str, key: str, s3) -> bytes:
    resp = s3.get_object(Bucket=bucket, Key=key)
    return resp["Body"].read()


# --------------------------------------------------------------------------
# Diff semantics
# --------------------------------------------------------------------------

def _within_tolerance(a: float, b: float, tol: float) -> bool:
    if a == b:
        return True
    if any(math.isnan(x) or math.isinf(x) for x in (a, b)):
        return False
    return abs(a - b) <= tol


def diff_json_bodies(left: bytes, right: bytes, mode: str, *, path_prefix: str = "") -> list[Divergence]:
    """Diff two JSON bodies.

    quick: byte-diff (fast fail on any JSON encoding change).
    deep:  value-by-value walk with $0.01 numeric tolerance.
    """
    if mode == "quick":
        if left == right:
            return []
        return [Divergence(path=path_prefix or "<root>", kind="byte_diff", detail="JSON byte-diff")]

    if mode != "deep":
        raise ValueError(f"unknown mode: {mode!r}")

    try:
        a = json.loads(left)
        b = json.loads(right)
    except json.JSONDecodeError as e:
        return [Divergence(path=path_prefix or "<root>", kind="value_diff",
                           detail=f"JSON parse failed: {e}")]

    return _deep_walk(a, b, path_prefix or "$", NUMERIC_TOLERANCE_DEEP)


def _deep_walk(a, b, path: str, tol: float) -> list[Divergence]:
    out: list[Divergence] = []
    if type(a) is not type(b):
        # Allow int vs float cross-type numeric comparison.
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if not _within_tolerance(float(a), float(b), tol):
                out.append(Divergence(path=path, kind="value_diff", left=a, right=b,
                                      detail=f"numeric diff > {tol}"))
            return out
        out.append(Divergence(path=path, kind="value_diff", left=a, right=b,
                              detail=f"type diff: {type(a).__name__} vs {type(b).__name__}"))
        return out

    if isinstance(a, dict):
        for k in sorted(set(a) - set(b)):
            out.append(Divergence(path=f"{path}.{k}", kind="key_missing_right", left=a[k]))
        for k in sorted(set(b) - set(a)):
            out.append(Divergence(path=f"{path}.{k}", kind="key_missing_left", right=b[k]))
        for k in sorted(set(a) & set(b)):
            out.extend(_deep_walk(a[k], b[k], f"{path}.{k}", tol))
        return out

    if isinstance(a, list):
        if len(a) != len(b):
            out.append(Divergence(path=path, kind="value_diff", left=len(a), right=len(b),
                                  detail="list length diff"))
            # Walk the shared prefix to give more signal.
        for i in range(min(len(a), len(b))):
            out.extend(_deep_walk(a[i], b[i], f"{path}[{i}]", tol))
        return out

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if not _within_tolerance(float(a), float(b), tol):
            out.append(Divergence(path=path, kind="value_diff", left=a, right=b,
                                  detail=f"numeric diff > {tol}"))
        return out

    if a != b:
        out.append(Divergence(path=path, kind="value_diff", left=a, right=b))
    return out


def diff_parquet_bodies(left: bytes, right: bytes, mode: str, *, path_prefix: str = "") -> list[Divergence]:
    """Diff two parquet bodies.

    quick: byte-diff.
    deep:  value-wise using pandas; $0.01 tolerance on numeric columns; reports (row, col).
    """
    if mode == "quick":
        if left == right:
            return []
        return [Divergence(path=path_prefix or "<root>", kind="byte_diff", detail="parquet byte-diff")]

    if mode != "deep":
        raise ValueError(f"unknown mode: {mode!r}")

    try:
        import pandas as pd
    except ImportError:
        return [Divergence(path=path_prefix or "<root>", kind="value_diff",
                           detail="pandas not available for deep parquet diff")]

    try:
        a = pd.read_parquet(io.BytesIO(left))
        b = pd.read_parquet(io.BytesIO(right))
    except Exception as e:
        return [Divergence(path=path_prefix or "<root>", kind="value_diff",
                           detail=f"parquet parse failed: {e}")]

    out: list[Divergence] = []
    if list(a.columns) != list(b.columns):
        out.append(Divergence(path=path_prefix, kind="value_diff",
                              left=list(a.columns), right=list(b.columns),
                              detail="column set diff"))
        return out

    if len(a) != len(b):
        out.append(Divergence(path=path_prefix, kind="value_diff",
                              left=len(a), right=len(b), detail="row count diff"))
        # Still walk shared prefix to surface value-level hints.

    n = min(len(a), len(b))
    for col in a.columns:
        la = a[col].iloc[:n]
        lb = b[col].iloc[:n]
        if pd.api.types.is_numeric_dtype(la) and pd.api.types.is_numeric_dtype(lb):
            diff = (la.astype(float) - lb.astype(float)).abs()
            bad = diff > NUMERIC_TOLERANCE_DEEP
            for idx in bad[bad].index[:20]:
                out.append(Divergence(
                    path=f"{path_prefix}({idx},{col})", kind="value_diff",
                    left=la.iloc[int(idx)] if isinstance(idx, int) else la.loc[idx],
                    right=lb.iloc[int(idx)] if isinstance(idx, int) else lb.loc[idx],
                    detail=f"numeric diff > {NUMERIC_TOLERANCE_DEEP}",
                ))
        else:
            ne = la.astype(str) != lb.astype(str)
            for idx in ne[ne].index[:20]:
                out.append(Divergence(
                    path=f"{path_prefix}({idx},{col})", kind="value_diff",
                    left=la.iloc[int(idx)] if isinstance(idx, int) else la.loc[idx],
                    right=lb.iloc[int(idx)] if isinstance(idx, int) else lb.loc[idx],
                ))
    return out


def _classify(key: str) -> str:
    k = key.lower()
    if k.endswith(".parquet"):
        return "parquet"
    if k.endswith(".json"):
        return "json"
    return "other"


def diff_prefixes(
    script_id: str,
    full_prefix: str,
    incremental_prefix: str,
    mode: str,
    s3,
    *,
    bucket: str = S3_BUCKET,
) -> DiffResult:
    """Diff the file sets at two S3 prefixes.

    Keys are paired by their suffix relative to each prefix. Missing-on-one-side
    is a divergence. Quick vs deep drives per-file diff semantics.
    """
    result = DiffResult(
        script_id=script_id,
        mode=mode,
        full_prefix=full_prefix,
        incremental_prefix=incremental_prefix,
    )
    full_keys = list_keys(bucket, full_prefix.rstrip("/") + "/", s3)
    incr_keys = list_keys(bucket, incremental_prefix.rstrip("/") + "/", s3)

    def _suffix(k: str, prefix: str) -> str:
        p = prefix.rstrip("/") + "/"
        return k[len(p):] if k.startswith(p) else k

    full_map = {_suffix(k, full_prefix): k for k in full_keys}
    incr_map = {_suffix(k, incremental_prefix): k for k in incr_keys}

    for suf in sorted(set(full_map) - set(incr_map)):
        result.divergences.append(Divergence(
            path=suf, kind="key_missing_right",
            detail=f"present at {full_prefix}, absent at {incremental_prefix}",
        ))
    for suf in sorted(set(incr_map) - set(full_map)):
        result.divergences.append(Divergence(
            path=suf, kind="key_missing_left",
            detail=f"absent at {full_prefix}, present at {incremental_prefix}",
        ))

    for suf in sorted(set(full_map) & set(incr_map)):
        a = fetch_bytes(bucket, full_map[suf], s3)
        b = fetch_bytes(bucket, incr_map[suf], s3)
        kind = _classify(suf)
        try:
            if kind == "parquet":
                result.divergences.extend(diff_parquet_bodies(a, b, mode, path_prefix=suf))
            elif kind == "json":
                result.divergences.extend(diff_json_bodies(a, b, mode, path_prefix=suf))
            else:
                if a != b:
                    result.divergences.append(Divergence(
                        path=suf, kind="byte_diff", detail="non-parquet/non-json byte diff",
                    ))
        except Exception as e:
            result.errors.append(f"{suf}: {e}")

    return result


# --------------------------------------------------------------------------
# Promoted list + report write
# --------------------------------------------------------------------------

def load_promoted_list(s3, *, bucket: str = S3_BUCKET) -> list[str]:
    try:
        body = fetch_bytes(bucket, PROMOTED_LIST_KEY, s3)
    except Exception:
        return []
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return []
    return list(data) if isinstance(data, list) else []


def write_parity_report(result: DiffResult, run_ts: str, s3, *, bucket: str = S3_BUCKET) -> str:
    key = f"{PARITY_REPORTS_PREFIX}/{result.script_id}/{run_ts}/diff.json"
    body = json.dumps(result.to_dict(), indent=2).encode("utf-8")
    s3.put_object(
        Bucket=bucket, Key=key, Body=body,
        ContentType="application/json", ServerSideEncryption="AES256",
    )
    return f"s3://{bucket}/{key}"


# --------------------------------------------------------------------------
# Self-parity (smoke-gate for already-incremental scripts, pre-dual-run support)
# --------------------------------------------------------------------------

def self_parity(script_id: str, prefix: str, mode: str, s3, *, bucket: str = S3_BUCKET) -> DiffResult:
    """Self-parity: diff a prefix against itself.

    Exercises the full read + parse + diff pipeline without requiring the
    script to support dual-run parity mode. Trivially passes when the
    prefix's contents are internally consistent. Used as the W0.003 smoke
    gate for C_06 (already-incremental; dual-run parity mode lands per
    script at Wave 2+).
    """
    return diff_prefixes(
        script_id=script_id,
        full_prefix=prefix,
        incremental_prefix=prefix,
        mode=mode,
        s3=s3,
        bucket=bucket,
    )
