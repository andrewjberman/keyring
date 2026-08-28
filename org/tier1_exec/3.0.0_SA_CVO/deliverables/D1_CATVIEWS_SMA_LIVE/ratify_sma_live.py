#!/usr/bin/env python3
"""D1_CATVIEWS_SMA_LIVE ratification instrument -- 3.0.0_SA_CVO~Z.

Checks AC1 (gold), AC2 (platinum) and the provenance bound at the ARTIFACT, per
scope, with the denominator printed. AC4 is evaluated but scored as a CONTROL
ONLY -- it passes on the pre-fix artifact and therefore evidences nothing alone
(msg 14091).

BUILT AND NEGATIVE-CONTROLLED BEFORE THE WORK LANDED: run against the current
pre-reland plane it MUST report FAIL. An instrument that passes on the broken
world is the defect this whole session is about, so its refusal is exercised
first and its pass is only meaningful afterwards.

Usage:
  python ratify_sma_live.py            # gold + platinum, all scopes
  python ratify_sma_live.py --expect-fail   # negative-control mode: rc=0 iff it FAILS
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

# DERIVED AT SOURCE, NOT GUESSED. The first build assumed platinum lived beside
# gold in opal-data-assets and got NoSuchKey x4 -- a TRUE absence at a key the
# object never occupied. Publisher lambda_function.py:66-67 is the authority:
#   SERVE_BUCKET = "opal-data-portal-v2"   SERVE_ROOT = "platinum/mdpf"
GOLD_BUCKET = "opal-data-assets"
PLAT_BUCKET = "opal-data-portal-v2"
GOLD = "portal/gold/mdpf/{scope}/category-views/{as_of}.json"
# PLATINUM IS UNDATED -- publisher :282 serve_key = f"{SERVE_ROOT}/{scope}/{atype}.json".
# Gold is dated-immutable; platinum is a MUTABLE latest-style key. So a STALE platinum
# object is byte-indistinguishable from a relanded one BY KEY, and the as_of must be
# read from the BODY. Guessed twice before reading the source: first the bucket+prefix,
# then the dated shape -- both by analogy from gold, which is the same cross-plane
# analogy that made the B0 sibling-copy wrong.
PLAT = "platinum/mdpf/{scope}/category-views.json"

SMA_EXPECTED = 22794766.25
CLIENT_EXPECTED = 267632047.22
CONSERVATION = 290426813.47
SMA_SCOPES = ("global", "49financial")
ZERO_SCOPES = ("cottonwood", "inflection")
ALL_SCOPES = SMA_SCOPES + ZERO_SCOPES
CENT = 0.01


def fetch(bucket, key):
    """Read an S3 object to a real temp file. Returns (doc, err) -- never raises.

    NOT /dev/stdout: that returned rc=255 under MSYS and the first build of this
    script scored the retrieval failure as a substantive FAIL, so its negative
    control PASSED while the instrument had never read a single object. A failed
    retrieval returns a VALUE; UNREADABLE and WRONG-VALUE must stay distinguishable
    or a broken fetch is indistinguishable from a correct refusal.
    """
    fd, tmp = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        r = subprocess.run(
            ["aws", "s3api", "get-object", "--bucket", bucket, "--key", key, tmp],
            capture_output=True, text=True)
        if r.returncode != 0:
            tail = (r.stderr or "").strip().splitlines()
            return None, "get-object rc=%d %s" % (r.returncode, tail[-1][:80] if tail else "")
        with open(tmp, encoding="utf-8") as fh:
            return json.load(fh), None
    except Exception as e:
        return None, "parse: %s" % e
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def check_scope(doc, scope, plane, out, post_reland, as_of):
    """AC1/AC2 assertions for one scope. Appends (label, ok, detail) to out."""
    if plane == "platinum":
        body_as_of = doc.get("as_of") or doc.get("_provenance", {}).get("data_as_of")
        out.append(("platinum/%s body as_of == %s (key is UNDATED)" % (scope, as_of),
                    body_as_of == as_of,
                    "body as_of=%r -- a stale object has the SAME key" % (body_as_of,)))
    nodes = doc.get("nodes", {})
    sma = nodes.get("SMA", {})
    client = nodes.get("Client", {})
    sma_aum = sma.get("aum")
    client_aum = client.get("aum")
    has_reason = "absent_reason" in sma
    p = "%s/%s" % (plane, scope)

    if scope in SMA_SCOPES:
        out.append(("%s SMA.aum == %.2f" % (p, SMA_EXPECTED),
                    sma_aum is not None and abs(sma_aum - SMA_EXPECTED) < CENT,
                    "read %r" % (sma_aum,)))
        out.append(("%s Client.aum == %.2f" % (p, CLIENT_EXPECTED),
                    client_aum is not None and abs(client_aum - CLIENT_EXPECTED) < CENT,
                    "read %r" % (client_aum,)))
        out.append(("%s absent_reason ABSENT" % p, not has_reason,
                    "present" if has_reason else "absent"))
    else:
        out.append(("%s SMA.aum == 0.00 (correct here)" % p,
                    sma_aum is not None and abs(sma_aum) < CENT,
                    "read %r" % (sma_aum,)))
        out.append(("%s absent_reason PRESENT" % p, has_reason,
                    "present" if has_reason else "absent"))

    # TRIGGER: informational by default. The first build asserted `trigger !=
    # scheduled` unconditionally, which REFUSED today's objects for carrying an
    # HONEST scheduled stamp -- a blacklist where a positive expectation belongs.
    # Only AFTER the reland is `adhoc` the required value; a `scheduled` claim on a
    # relanded object is the forgery, and that is the only case worth refusing.
    trig = doc.get("_provenance", {}).get("trigger")
    if post_reland:
        out.append(("%s trigger == adhoc (honest reland provenance)" % p,
                    isinstance(trig, str) and "adhoc" in trig,
                    "trigger=%r -- a scheduled claim here would be FORGED" % (trig,)))
    else:
        print("  INFO %-58s trigger=%r" % ("%s provenance (not scored pre-reland)" % p, trig))
    return client_aum, sma_aum


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", default="2026-08-27")
    ap.add_argument("--expect-fail", action="store_true",
                    help="negative-control mode: exit 0 only if ratification FAILS")
    ap.add_argument("--post-reland", action="store_true",
                    help="score _provenance.trigger: adhoc REQUIRED, a scheduled claim is FORGED")
    a = ap.parse_args()

    rows = []
    unreadable = []
    for plane, bucket, tmpl in (("gold", GOLD_BUCKET, GOLD),
                                ("platinum", PLAT_BUCKET, PLAT)):
        for scope in ALL_SCOPES:
            key = tmpl.format(scope=scope, as_of=a.as_of)
            doc, err = fetch(bucket, key)
            if doc is None:
                unreadable.append("%s s3://%s/%s: %s" % (plane, bucket, key, err))
                continue
            client_aum, sma_aum = check_scope(doc, scope, plane, rows, a.post_reland, a.as_of)
            if plane == "gold" and scope == "global" and None not in (client_aum, sma_aum):
                ok = abs((client_aum + sma_aum) - CONSERVATION) < CENT
                rows.append(("[CONTROL ONLY] conservation Client+SMA == %.2f" % CONSERVATION,
                             ok, "PASSES PRE-FIX TOO -- evidences nothing alone (14091)"))

    scored = [r for r in rows if not r[0].startswith("[CONTROL ONLY]")]
    passed = [r for r in scored if r[1]]
    failed = [r for r in scored if not r[1]]

    print("== D1_CATVIEWS_SMA_LIVE ratification -- as_of %s ==" % a.as_of)
    for label, ok, detail in rows:
        print("  %-4s %-58s %s" % ("OK:" if ok else "FAIL", label, detail))
    print()
    print("  DENOMINATOR: %d scored assertions across %d planes x %d scopes"
          % (len(scored), 2, len(ALL_SCOPES)))
    print("  PASS %d / FAIL %d   (controls excluded from scoring: %d)"
          % (len(passed), len(failed), len(rows) - len(scored)))
    if unreadable:
        print("  UNREADABLE OBJECTS (a failed retrieval returns a VALUE -- not an absence):")
        for u in unreadable:
            print("    %s" % u)

    # UNREADABLE is INDETERMINATE, never a refusal: a broken fetch must not be
    # able to masquerade as a correct rejection (or as a correct pass).
    if unreadable:
        print()
        print("  INDETERMINATE -- %d object(s) UNREADABLE. This is NOT a refusal and NOT"
              " a pass; the instrument did not see the artifact." % len(unreadable))
        return 2
    ratified = not failed
    if a.expect_fail:
        print()
        if ratified:
            print("  NEGATIVE CONTROL FAILED: the instrument PASSED on a plane that should")
            print("  not satisfy it. The instrument is not trustworthy. Do not use it.")
            return 1
        print("  NEGATIVE CONTROL OK: the instrument REFUSES the pre-fix plane, so a later")
        print("  pass is informative rather than automatic.")
        return 0
    print()
    print("  RATIFIED" if ratified else "  NOT RATIFIED")
    return 0 if ratified else 1


if __name__ == "__main__":
    sys.exit(main())
