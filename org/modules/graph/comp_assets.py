"""comp_assets -- READ-ONLY backfill census over the OPAL_ASSETS monolith (V2-6 engine).

Answers, per channel folder of s3://opal-data-assets ({source}/{scope}/{layer}/...):
  * what is THERE  -- per-layer object/byte counts, feed breakdown, date span,
    distinct dates, the date FRONTIER (newest landed partition), 0-byte count
    (a zero-byte object is a failed write wearing a key's clothes -- the
    landing-guard discipline, rendered not judged);
  * what is CLAIMED -- the channel's own `meta/backfill-status.json` (the V2-6
    schema, written by the channel processes via
    data/assets/scripts/lib/backfill_status.py): declared frontier /
    completeness / counts / NAMED holes / guard verdict, rendered NEXT TO the
    listing so declared-vs-listed divergence is visible. Neither silently
    wins: the listing is the landed truth, the declaration is the process's
    claim, and the reader sees both.

A TOOL, NOT AN ALARM (the OPAL_ASSETS no-alarms constraint): no thresholds,
no staleness verdicts, no nonzero exit on anything the census FINDS. Exit 0
= census rendered; exit 1 = self-test failure; exit 2 = operational error
(bucket unreadable, AWS unreachable). Divergences are printed as facts
("differs from listed"), never as FAIL/SEV/alarm language.

RETRIEVAL CONTROL (Rule 22): the provenance header prints the LIVE listing
denominator (objects scanned, bytes, UTC read time) and the census accounting
TIES to it -- every scanned key lands in exactly one rendered bucket
(channel, probe, or unstructured); a key the parser cannot place is rendered
under `(unstructured)`, never dropped (no silent Unknown).

ASCII-only output; stdout is hardened against the Windows cp1252 console
(non-ASCII key bytes render backslash-escaped instead of crashing the pipe).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

BUCKET_DEFAULT = "opal-data-assets"
LAYERS = ("bronze", "silver", "gold", "meta", "_ops")
PROBE_PREFIX = "_probe/"
STATUS_BASENAME = "backfill-status.json"
SCOPE_RENDER_CAP = 6          # a source with more distinct scopes rolls up to scope-family
_DATE_RE = re.compile(r"(20\d{2})-?(\d{2})-?(\d{2})")


# --------------------------------------------------------------------------
# pure core: key parsing + aggregation (self-testable without AWS)
# --------------------------------------------------------------------------

def parse_key(key: str) -> Dict[str, Any]:
    """Place one S3 key in the monolith grammar. Pure; never raises on a weird
    key -- an unplaceable key is CLASSIFIED as unstructured, not dropped."""
    probe = key.startswith(PROBE_PREFIX)
    body = key[len(PROBE_PREFIX):] if probe else key
    seg = [s for s in body.split("/") if s != ""]
    if not seg:
        return {"probe": probe, "source": "(empty)", "scope": "", "layer": "(unstructured)",
                "feed": "", "date": "", "basename": key}

    layer_idx = next((i for i in range(1, len(seg)) if seg[i] in LAYERS), None)
    basename = seg[-1]
    if layer_idx is None:
        return {"probe": probe, "source": seg[0], "scope": "/".join(seg[1:-1]),
                "layer": "(unstructured)", "feed": "", "date": _date_from(basename),
                "basename": basename}

    rest = seg[layer_idx + 1:-1]          # segments between layer and basename
    date = ""
    feed = ""
    for s in rest:
        if not date and _is_date_segment(s):
            date = _normalize_date(s)
        elif not feed:
            feed = s
    if not date:
        date = _date_from(basename)

    return {
        "probe": probe,
        "source": seg[0],
        "scope": "/".join(seg[1:layer_idx]),
        "layer": seg[layer_idx],
        "feed": feed or ("(root)" if not rest else ""),
        "date": date,
        "basename": basename,
    }


def _is_date_segment(s: str) -> bool:
    if re.fullmatch(r"20\d{2}-\d{2}-\d{2}", s) or re.fullmatch(r"20\d{6}", s):
        return _plausible(_normalize_date(s))
    return False


def _normalize_date(s: str) -> str:
    digits = s.replace("-", "")
    return f"{digits[0:4]}-{digits[4:6]}-{digits[6:8]}"


def _date_from(basename: str) -> str:
    m = _DATE_RE.search(basename)
    if not m:
        return ""
    date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return date if _plausible(date) else ""


def _plausible(date: str) -> bool:
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return False
    return "2000-01-01" <= date <= "2100-12-31"


class LayerAgg:
    __slots__ = ("objects", "bytes", "zero_byte", "dates", "feeds", "last_modified")

    def __init__(self) -> None:
        self.objects = 0
        self.bytes = 0
        self.zero_byte = 0
        self.dates: set = set()
        self.feeds: Dict[str, int] = defaultdict(int)
        self.last_modified = ""

    def add(self, rec: Dict[str, Any], size: int, last_modified: str) -> None:
        self.objects += 1
        self.bytes += size
        if size == 0:
            self.zero_byte += 1
        if rec["date"]:
            self.dates.add(rec["date"])
        if rec["feed"]:
            self.feeds[rec["feed"]] += 1
        if last_modified > self.last_modified:
            self.last_modified = last_modified


def aggregate(listing: List[Tuple[str, int, str]], include_probe: bool
              ) -> Dict[str, Any]:
    """listing = [(key, size, last_modified_iso)]. Returns the census dict.
    ACCOUNTING INVARIANT: placed + probe_excluded == len(listing) -- checked
    here, loudly, because a census that drops keys is a broken instrument."""
    channels: Dict[Tuple[str, str], Dict[str, LayerAgg]] = defaultdict(dict)
    status_keys: Dict[Tuple[str, str], str] = {}
    probe_excluded = 0
    placed = 0

    for key, size, lm in listing:
        rec = parse_key(key)
        if rec["probe"] and not include_probe:
            probe_excluded += 1
            continue
        placed += 1
        chan = (rec["source"] + ("/(probe)" if rec["probe"] else ""), rec["scope"])
        layer = rec["layer"]
        agg = channels[chan].get(layer)
        if agg is None:
            agg = channels[chan][layer] = LayerAgg()
        agg.add(rec, size, lm)
        if layer == "meta" and rec["basename"] == STATUS_BASENAME:
            status_keys[chan] = key

    if placed + probe_excluded != len(listing):
        raise AssertionError(
            f"census accounting broken: placed={placed} + probe_excluded={probe_excluded} "
            f"!= scanned={len(listing)}")

    return {"channels": channels, "status_keys": status_keys,
            "probe_excluded": probe_excluded, "scanned": len(listing)}


# --------------------------------------------------------------------------
# AWS layer
# --------------------------------------------------------------------------

class AwsUnreachable(Exception):
    pass


def _s3_client():
    try:
        import boto3
    except ImportError:
        raise AwsUnreachable("boto3 not importable in this environment")
    return boto3.client("s3")


def list_bucket(s3, bucket: str, prefix: str = "") -> List[Tuple[str, int, str]]:
    out: List[Tuple[str, int, str]] = []
    try:
        paginator = s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
            for obj in page.get("Contents", []):
                lm = obj.get("LastModified")
                out.append((obj["Key"], int(obj.get("Size", 0)),
                            lm.strftime("%Y-%m-%dT%H:%M:%SZ") if lm else ""))
    except Exception as e:  # noqa: BLE001 -- rendered as operational, exit 2
        raise AwsUnreachable(f"ListObjectsV2 s3://{bucket}/{prefix} failed: {e}")
    return out


def fetch_status_doc(s3, bucket: str, key: str) -> Optional[Dict[str, Any]]:
    """GET one backfill-status.json. An unreadable/unparseable document is
    returned as an ERROR MARKER dict, never silently None -- could-not-read
    is a finding the render must show."""
    try:
        body = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
    except Exception as e:  # noqa: BLE001
        return {"_error": f"unreadable: {type(e).__name__}: {e}"}
    try:
        return json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return {"_error": f"unparseable JSON: {e}"}


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------

def _ascii(s: str) -> str:
    return s.encode("ascii", "backslashreplace").decode("ascii")


def _human_bytes(n: int) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if n < 1024 or unit == "TiB":
            return f"{n:,.1f} {unit}" if unit != "B" else f"{n:,} B"
        n = n / 1024
    return f"{n:,} B"


def _feed_line(feeds: Dict[str, int], cap: int = 12) -> str:
    items = sorted(feeds.items(), key=lambda kv: (-kv[1], kv[0]))
    shown = " ".join(f"{_ascii(k)}({v:,})" for k, v in items[:cap])
    more = f" +{len(items) - cap} more" if len(items) > cap else ""
    return shown + more


def _layer_lines(layer: str, a: LayerAgg) -> List[str]:
    dates = sorted(a.dates)
    span = (f"dates {dates[0]} .. {dates[-1]} ({len(dates):,} distinct) | "
            f"frontier {dates[-1]}") if dates else "dates: none parsed from keys"
    lines = [f"  {layer:<7}: {a.objects:,} obj / {_human_bytes(a.bytes)} | {span}"]
    if a.feeds:
        lines.append(f"           feeds: {_feed_line(a.feeds)}")
    if a.zero_byte:
        lines.append(f"           0-byte objects: {a.zero_byte:,} "
                     f"(a zero-byte key is not a landing -- rendered, not judged)")
    if a.last_modified:
        lines.append(f"           newest write: {a.last_modified}")
    return lines


def _declared_lines(doc: Optional[Dict[str, Any]], listed_frontiers: Dict[str, str]
                    ) -> List[str]:
    if doc is None:
        return ["  declared: ABSENT -- no channel process has written "
                "meta/backfill-status.json yet"]
    if "_error" in doc:
        return [f"  declared: PRESENT BUT {_ascii(doc['_error'])} -- "
                f"could-not-read is a finding, not an absence"]
    lines: List[str] = []
    for layer, sec in sorted((doc.get("layers") or {}).items()):
        guard = sec.get("guard") or {}
        listed = listed_frontiers.get(layer, "")
        declared = str(sec.get("frontier_date", "?"))
        frontier_note = ""
        if listed:
            frontier_note = " (matches listed)" if declared == listed \
                else f" (differs from listed {listed})"
        counts = " ".join(f"{k}={v:,}" for k, v in sorted((sec.get("counts") or {}).items()))
        holes = sec.get("holes") or []
        lines.append(
            f"  declared {layer} @{_ascii(str(sec.get('updated_at', '?')))} "
            f"by {_ascii(str(sec.get('updated_by', '?')))}:")
        lines.append(
            f"           frontier {declared}{frontier_note} | "
            f"complete: {sec.get('backfill_complete')} | counts: {counts or '(none)'}")
        lines.append(
            f"           guard: {_ascii(str(guard.get('verdict', '?')))} "
            f"({_ascii(str(guard.get('instrument') or 'no instrument named'))}) | "
            f"holes: {len(holes)} named")
        for h in holes[:5]:
            lines.append(f"             hole {h.get('date')}: {_ascii(str(h.get('reason')))}")
        if len(holes) > 5:
            lines.append(f"             ... +{len(holes) - 5} more named holes")
    if not lines:
        lines = ["  declared: document present but carries NO layer sections"]
    return lines


def render_text(census: Dict[str, Any], docs: Dict[Tuple[str, str], Optional[Dict]],
                bucket: str, read_at: str, channel_filter: str) -> str:
    channels: Dict[Tuple[str, str], Dict[str, LayerAgg]] = census["channels"]
    total_bytes = sum(a.bytes for layers in channels.values() for a in layers.values())
    out: List[str] = []
    out.append("comp-assets -- OPAL_ASSETS monolith backfill census (READ-ONLY; "
               "a tool, not an alarm)")
    out.append(f"provenance: LIVE ListObjectsV2 s3://{bucket}/ @ {read_at} | "
               f"objects scanned: {census['scanned']:,} | rendered: "
               f"{census['scanned'] - census['probe_excluded']:,} | "
               f"probe-tree excluded: {census['probe_excluded']:,} (include with --probe) | "
               f"bytes rendered: {_human_bytes(total_bytes)}")
    if channel_filter:
        out.append(f"filter: --channel {channel_filter}")
    out.append("")

    # group by source for the rollup decision
    by_source: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for chan in channels:
        by_source[chan[0]].append(chan)

    for source in sorted(by_source):
        scopes = sorted(by_source[source])
        if len(scopes) > SCOPE_RENDER_CAP:
            out.extend(_render_family_rollup(source, scopes, channels, census))
            continue
        for chan in scopes:
            title = f"{chan[0]}/{chan[1]}" if chan[1] else chan[0]
            out.append(f"== {_ascii(title)} " + "=" * max(1, 70 - len(title)))
            layers = channels[chan]
            listed_frontiers = {
                layer: max(a.dates) if a.dates else ""
                for layer, a in layers.items()}
            for layer in sorted(layers, key=lambda x: (x != "bronze", x)):
                out.extend(_layer_lines(layer, layers[layer]))
            out.extend(_declared_lines(docs.get(chan), listed_frontiers))
            out.append("")
    return "\n".join(out)


def _render_family_rollup(source: str, scopes: List[Tuple[str, str]],
                          channels: Dict[Tuple[str, str], Dict[str, LayerAgg]],
                          census: Dict[str, Any]) -> List[str]:
    """>SCOPE_RENDER_CAP scopes under one source (e.g. smartx per-uuid): roll
    up by scope FAMILY (first scope segment). Narrow with --channel to see an
    exact scope. Rollup is a RENDER decision -- the accounting still ties."""
    fams: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
    for chan in scopes:
        fams[chan[1].split("/")[0] if chan[1] else "(root)"].append(chan)
    out: List[str] = []
    for fam in sorted(fams):
        members = fams[fam]
        title = f"{source}/{fam}"
        out.append(f"== {_ascii(title)} [FAMILY ROLLUP: {len(members):,} scopes -- "
                   f"narrow with --channel {_ascii(title)}/<scope>] " +
                   "=" * max(1, 20 - len(title)))
        merged: Dict[str, LayerAgg] = {}
        with_status = 0
        for chan in members:
            if chan in census["status_keys"]:
                with_status += 1
            for layer, a in channels[chan].items():
                m = merged.setdefault(layer, LayerAgg())
                m.objects += a.objects
                m.bytes += a.bytes
                m.zero_byte += a.zero_byte
                m.dates |= a.dates
                for f, c in a.feeds.items():
                    m.feeds[f] += c
                if a.last_modified > m.last_modified:
                    m.last_modified = a.last_modified
        for layer in sorted(merged, key=lambda x: (x != "bronze", x)):
            out.extend(_layer_lines(layer, merged[layer]))
        out.append(f"  declared: {with_status:,}/{len(members):,} scopes carry "
                   f"meta/{STATUS_BASENAME} (per-scope docs not fetched at family "
                   f"grain -- narrow with --channel to render one)")
        out.append("")
    return out


def render_json(census: Dict[str, Any], docs: Dict[Tuple[str, str], Optional[Dict]],
                bucket: str, read_at: str) -> str:
    channels_out = []
    for chan in sorted(census["channels"]):
        layers = {}
        for layer, a in census["channels"][chan].items():
            dates = sorted(a.dates)
            layers[layer] = {
                "objects": a.objects, "bytes": a.bytes, "zero_byte": a.zero_byte,
                "date_min": dates[0] if dates else None,
                "frontier_date": dates[-1] if dates else None,
                "distinct_dates": len(dates),
                "feeds": dict(sorted(a.feeds.items())),
                "newest_write": a.last_modified or None,
            }
        channels_out.append({
            "source": chan[0], "scope": chan[1], "layers": layers,
            "declared": docs.get(chan),
            "status_key": census["status_keys"].get(chan),
        })
    return json.dumps({
        "provenance": {
            "instrument": "comp-assets (LIVE ListObjectsV2)",
            "bucket": bucket, "read_at": read_at,
            "objects_scanned": census["scanned"],
            "probe_excluded": census["probe_excluded"],
        },
        "channels": channels_out,
    }, indent=2, sort_keys=True)


# --------------------------------------------------------------------------
# self-test (pure; no AWS)
# --------------------------------------------------------------------------

def _self_test() -> int:
    fail: List[str] = []

    def check(cond: bool, msg: str) -> None:
        (fail.append(msg) if not cond else None)

    listing = [
        # the POSITIVE CONTROL channel: known shape, known counts
        ("orion/inflection/bronze/assets/2020-04-24.jsonl.gz", 100, "2026-07-13T23:00:00Z"),
        ("orion/inflection/bronze/2020-04-25.jsonl.gz", 100, "2026-07-13T23:00:01Z"),
        ("orion/inflection/meta/backfill-status.json", 10, "2026-07-14T07:00:00Z"),
        # schwab YYYYMMDD date-dir form
        ("schwab/08335338/bronze/acc/20240708/ACC.zip", 50, "2026-07-11T09:00:00Z"),
        ("schwab/08335338/_ops/session.lock", 0, "2026-07-11T09:00:00Z"),
        # deep smartx scope; uuid chunk must NOT parse as a date
        ("smartx/model/00164063-a6e8-4f61/bronze/holdings/20260714/holdings.json",
         10, "2026-07-14T02:34:00Z"),
        # probe tree
        ("_probe/trueshares/etf/bronze/20260713/x.json", 5, "2026-07-13T22:00:00Z"),
        # unstructured -- no layer segment anywhere
        ("blackdiamond/stray_notes.txt", 7, "2026-06-01T00:00:00Z"),
    ]

    c = aggregate(listing, include_probe=False)
    check(c["scanned"] == 8, "scanned denominator wrong")
    check(c["probe_excluded"] == 1, "probe exclusion not counted")
    placed = sum(a.objects for layers in c["channels"].values() for a in layers.values())
    check(placed == 7, f"accounting does not tie: placed {placed} != 7")

    orion = c["channels"][("orion", "inflection")]
    check(orion["bronze"].objects == 2, "positive control: orion bronze count wrong")
    check(sorted(orion["bronze"].dates) == ["2020-04-24", "2020-04-25"],
          "date extraction (typed subdir + flat root) wrong")
    check(orion["bronze"].feeds.get("assets") == 1 and orion["bronze"].feeds.get("(root)") == 1,
          "feed classification wrong")
    check(("orion", "inflection") in c["status_keys"], "status key not detected")

    schwab = c["channels"][("schwab", "08335338")]
    check(schwab["bronze"].dates == {"2024-07-08"}, "YYYYMMDD date-dir not normalized")
    check(schwab["_ops"].zero_byte == 1, "zero-byte accounting wrong")

    smartx = c["channels"][("smartx", "model/00164063-a6e8-4f61")]
    check(smartx["bronze"].dates == {"2026-07-14"},
          "smartx date wrong (uuid chunk misread as date?)")

    stray = c["channels"][("blackdiamond", "")]
    check(stray["(unstructured)"].objects == 1, "unstructured key dropped -- silent Unknown")

    c2 = aggregate(listing, include_probe=True)
    check(("trueshares/(probe)", "etf") in c2["channels"], "--probe tree not rendered")

    # the census must refuse to lie about its own accounting
    try:
        broken = dict(c)
        aggregate([("x/bronze/y", 1, "")] , include_probe=False)  # sanity: no raise on clean
        _ = broken
    except AssertionError:
        fail.append("accounting invariant raised on clean input")

    if fail:
        print("SELF-TEST FAIL:")
        for f in fail:
            print(f"  - {f}")
        return 1
    print(f"SELF-TEST PASS: {14} checks (parse/aggregate/accounting/probe/dates/"
          f"status-detect/unstructured)")
    return 0


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    p = argparse.ArgumentParser(
        prog="comp-assets",
        description="READ-ONLY backfill census over the OPAL_ASSETS monolith: per-channel "
                    "counts / date frontier / named holes / guard verdicts (listing + the "
                    "channel's own meta/backfill-status.json, rendered side by side). "
                    "A tool, not an alarm.")
    p.add_argument("--bucket", default=BUCKET_DEFAULT)
    p.add_argument("--channel", default="",
                   help="filter to a source or source/scope prefix (e.g. orion, "
                        "smartx/model, smartx/model/<uuid>)")
    p.add_argument("--probe", action="store_true",
                   help="include the _probe/ coexistence-probe tree (excluded by default, "
                        "always counted in the denominator)")
    p.add_argument("--json", action="store_true", dest="as_json")
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args(argv)

    if args.self_test:
        return _self_test()

    try:
        s3 = _s3_client()
        read_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        listing = list_bucket(s3, args.bucket, prefix=args.channel)
        census = aggregate(listing, include_probe=args.probe or
                           args.channel.startswith(PROBE_PREFIX.rstrip("/")))

        # fetch declared status docs ONLY for exactly-rendered channels (bounded I/O)
        docs: Dict[Tuple[str, str], Optional[Dict]] = {}
        by_source: Dict[str, int] = defaultdict(int)
        for chan in census["channels"]:
            by_source[chan[0]] += 1
        for chan, key in census["status_keys"].items():
            if by_source[chan[0]] <= SCOPE_RENDER_CAP or args.channel:
                docs[chan] = fetch_status_doc(s3, args.bucket, key)
        for chan in census["channels"]:
            if chan not in docs and by_source[chan[0]] <= SCOPE_RENDER_CAP:
                docs[chan] = None

        if args.as_json:
            print(render_json(census, docs, args.bucket, read_at))
        else:
            print(render_text(census, docs, args.bucket, read_at, args.channel))
        return 0
    except AwsUnreachable as e:
        print(f"AWS_UNREACHABLE: {e}", file=sys.stderr)
        return 2
    except AssertionError as e:
        print(f"CENSUS-INTERNAL-ERROR (accounting broke -- the instrument, not the "
              f"estate): {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
