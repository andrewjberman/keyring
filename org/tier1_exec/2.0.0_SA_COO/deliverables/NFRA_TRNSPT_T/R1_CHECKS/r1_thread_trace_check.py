"""TR-t-5 AC2 -- validate the FWD-1 round-1 thread trace (issuer's check, dry-run at the base: FAIL as expected).

usage: python r1_thread_trace_check.py <trace.json>
Prints TRACE-VALID on success, else TRACE-INVALID <reason>. Exit 0 only on TRACE-VALID.
"""
import json
import sys
from datetime import datetime


def _iso(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main(path):
    try:
        t = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print("TRACE-INVALID unreadable: %s" % e)
        return 1
    hops = t.get("hops") or []
    if len(hops) != 3:
        print("TRACE-INVALID hops=%d (want 3: land-probe, parse, read)" % len(hops))
        return 1
    last = None
    for h in hops:
        for k in ("hop", "ran_by", "started_utc", "ended_utc", "s3_keys", "exit"):
            if k not in h:
                print("TRACE-INVALID hop %r missing %s" % (h.get("hop"), k))
                return 1
        if h["ran_by"] != "data/transcripts/scripts/teams/thread_trace.py":
            print("TRACE-INVALID hop %r ran_by=%r (a person or another script)" % (h["hop"], h["ran_by"]))
            return 1
        s, e = _iso(h["started_utc"]), _iso(h["ended_utc"])
        if e < s or (last and s < last):
            print("TRACE-INVALID hop %r timestamps not monotonic" % h["hop"])
            return 1
        last = e
        if h["exit"] != 0:
            print("TRACE-INVALID hop %r exit=%r" % (h["hop"], h["exit"]))
            return 1
        if not h["s3_keys"] or not all(k.startswith("s3://opal-data-transcripts/teams/transcripts/") for k in h["s3_keys"]):
            print("TRACE-INVALID hop %r s3_keys not under the builder's address" % h["hop"])
            return 1
    neg = t.get("negative_arm") or {}
    if neg.get("result") != "NOT-HELD" or not neg.get("cause"):
        print("TRACE-INVALID negative arm absent or without a cause")
        return 1
    if t.get("no_person") is not True:
        print("TRACE-INVALID no_person is not true")
        return 1
    for banned in ("cue_text", "text", "spoken"):
        if banned in json.dumps(t):
            print("TRACE-INVALID carries transcript text (%s)" % banned)
            return 1
    print("TRACE-VALID hops=3 negative_arm=NOT-HELD no_person=true transcript=%s" % t.get("transcript_id"))
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("TRACE-INVALID usage")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
