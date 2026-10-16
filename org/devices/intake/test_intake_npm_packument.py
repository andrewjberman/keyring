#!/usr/bin/env python3
"""test_intake_npm_packument.py -- the npm packument read of the intake route (CT-cc-1 addendum 3 of the CTO ruling of
2026-10-16; row NFRA_CTLPLN-W147-S1), proven against a LOOPBACK registry. Nothing here contacts the public internet: every
registry is the ThreadingHTTPServer that test_intake_npm.py starts on 127.0.0.1, and every tarball is synthetic.

The fetch reads the packument at the same host, after the version document and before the tarball. Check 4 takes
time[<version>] as the publish time and the packument's other versions as the earlier releases, and passes or fails on those
measured facts. No WAIVE line is involved in any arm here.

Arms (each prints PASS or FAIL with its detail):
  a  check 4 reads the packument: an old time[<version>] with three earlier releases PASSES (unscoped and scoped names; the
     packument is requested before the tarball); a time[<version>] two days old FAILS with the measured age in the evidence,
     and the record reads not_checked (no waiver)
  b  a packument with NO time[<version>] is REFUSED before any tarball request (this arm disarms W147-S1); an absent
     packument is REFUSED the same way
  c  a packument whose versions[<version>].dist.integrity differs from the version document's is REFUSED, zero tarball requests
  d  control: a mutant that ignores the packument time (reads an old date instead) makes arm a's too-new case PASS, so the
     arm's expectation of a failure is what detects it; the real code FAILs the same case

Standard library plus the intake tools and the fixtures of test_intake_npm.py; temporary folders only; ASCII output.
Last line: INTAKE-NPM-PACKUMENT arms=<k>/<n> ok=<True|False>
"""
import datetime
import json
import os
import sys
import traceback
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_check as C  # noqa: E402
import test_intake_npm as T  # noqa: E402

TOO_NEW_DAYS = 2


def sri(data):
    return T.sri(data)


def packument_key(name):
    return "/%s" % urllib.parse.quote(name, safe="@")


def days_ago(days):
    now = datetime.datetime.now(datetime.timezone.utc)
    return (now - datetime.timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def set_time(version, when):
    def edit(doc):
        doc["time"][version] = when
    return edit


def drop_time(version):
    def edit(doc):
        del doc["time"][version]
    return edit


def set_integrity(version, integrity):
    def edit(doc):
        doc["versions"][version]["dist"]["integrity"] = integrity
    return edit


def serve_packument(env, name, edit):
    """edit is None (the fixture as published), 'absent' (no packument at all), or a function over the decoded packument."""
    key = packument_key(name)
    if edit is None:
        return
    if edit == "absent":
        del env.reg.docs[key]
        return
    doc = json.loads(env.reg.docs[key].decode("ascii"))
    edit(doc)
    env.reg.docs[key] = json.dumps(doc).encode("ascii")


def mutant_check_4(ctx):
    """the mutant: check 4 ignores the packument's time[<version>] and reads an old date in its place"""
    fr = dict(ctx["fetch"])
    proj = dict(fr.get("project") or {})
    proj["this_release_at"] = "2001-01-01T00:00:00.000Z"
    fr["project"] = proj
    return C.check_4(dict(ctx, fetch=fr))


def run_case(name, version, data, edit=None, mutant=False):
    """One fetch and one check of name@version on the loopback registry. Returns (fetch record, check record or None, the
    registry's request paths in order, the path list of the tarball requests)."""
    env = T.Env()
    try:
        env.publish(name, version, data)
        serve_packument(env, name, edit)
        env.approve(["%s@%s" % (name, version)])
        env.write_lock([(name, version, sri(data))])
        orig = C.NPM_CHECKS
        try:
            if mutant:
                C.NPM_CHECKS = [orig[0], orig[1], orig[2], mutant_check_4] + list(orig[4:])
            _rc, fr, _o = env.fetch(name, version)
            rec = None
            if fr.get("outcome") == "held":
                _rc2, rec, _o2 = env.check(name, version, signed_lines=T.signed_lines(name, version))
        finally:
            C.NPM_CHECKS = orig
        return fr, rec, list(env.reg.requests), env.reg.tarball_requests(), os.path.isfile(env.held(name, version))
    finally:
        env.close()


def arm_a():
    """Check 4 reads the packument's time[<version>]: passes on an old release with earlier releases, fails on a too-new one."""
    details = []
    good = True
    for name, version in (T.UNSCOPED, T.SCOPED):
        data = T.std_tgz(name, version, extra={"description": "synthetic"})
        fr, rec, reqs, tgz, held = run_case(name, version, data)
        packument_path = packument_key(name)
        order_ok = (packument_path in reqs and tgz and reqs.index(packument_path) < reqs.index(tgz[0]))
        c4 = rec["checks"][3] if rec else {}
        ev4 = c4.get("evidence") or {}
        passed = (fr.get("outcome") == "held" and held and c4.get("verdict") == "passed" and ev4.get("earlier_releases") == 3
                  and ev4.get("age_days", 0) > 14 and rec.get("verdict") == "checked" and rec.get("waived_checks") == []
                  and order_ok)
        good = good and passed
        details.append("old time %s: packument read before the tarball=%s check 4=%s earlier=%s age_days=%s verdict=%s waived=%s" % (
            "%s@%s" % (name, version), order_ok, c4.get("verdict"), ev4.get("earlier_releases"), ev4.get("age_days"),
            rec.get("verdict") if rec else None, rec.get("waived_checks") if rec else None))
    name, version = T.UNSCOPED
    data = T.std_tgz(name, version)
    fr, rec, reqs, tgz, held = run_case(name, version, data, edit=set_time(version, days_ago(TOO_NEW_DAYS)))
    c4 = rec["checks"][3] if rec else {}
    ev4 = c4.get("evidence") or {}
    too_new = (fr.get("outcome") == "held" and c4.get("verdict") == "failed" and ev4.get("age_days", 99) < 14
               and "below the minimum" in c4.get("evidence", {}).get("summary", "") and rec.get("verdict") == "not_checked"
               and rec.get("waived_checks") == [])
    good = good and too_new
    details.append("too-new time (%d days): check 4=%s age_days=%s summary=%s verdict=%s waived=%s" % (
        TOO_NEW_DAYS, c4.get("verdict"), ev4.get("age_days"), (ev4.get("summary") or "")[:110],
        rec.get("verdict") if rec else None, rec.get("waived_checks") if rec else None))
    return good, details


def arm_b():
    """A packument with no time[<version>], and an absent packument, are REFUSED before any tarball request."""
    details = []
    good = True
    name, version = T.UNSCOPED
    data = T.std_tgz(name, version)
    cases = [("no time[version]", drop_time(version), "no time[%s] publish time" % version),
             ("packument absent", "absent", "packument unreadable")]
    for label, edit, want in cases:
        fr, rec, reqs, tgz, held = run_case(name, version, data, edit=edit)
        refused = fr.get("outcome") == "refused" and want in (fr.get("reason") or "")
        zero = tgz == [] and not held and rec is None
        good = good and refused and zero
        details.append("%s: outcome=%s reason=%s tarball_requests=%d held=%s" % (
            label, fr.get("outcome"), (fr.get("reason") or "")[:100], len(tgz), held))
    return good, details


def arm_c():
    """A packument whose versions[<version>].dist.integrity differs from the version document's is REFUSED, zero tarball requests."""
    name, version = T.UNSCOPED
    data = T.std_tgz(name, version)
    other = sri(b"the packument describes some other bytes")
    fr, rec, reqs, tgz, held = run_case(name, version, data, edit=set_integrity(version, other))
    refused = fr.get("outcome") == "refused" and "two stories" in (fr.get("reason") or "")
    zero = tgz == [] and not held
    packument_asked = packument_key(name) in reqs
    good = refused and zero and packument_asked
    return good, ["packument integrity differs: outcome=%s reason=%s" % (fr.get("outcome"), (fr.get("reason") or "")[:120]),
                  "tarball_requests=%d held=%s packument requested=%s" % (len(tgz), held, packument_asked)]


def arm_d():
    """Control: the mutant that ignores the packument time PASSES the too-new case (so arm a would fail on it); the real code FAILS it."""
    name, version = T.UNSCOPED
    data = T.std_tgz(name, version)
    edit = set_time(version, days_ago(TOO_NEW_DAYS))
    fr_r, rec_r, _a, _b, _c = run_case(name, version, data, edit=edit)
    fr_m, rec_m, _d, _e, _f = run_case(name, version, data, edit=edit, mutant=True)
    real_verdict = rec_r["checks"][3]["verdict"] if rec_r else None
    mutant_verdict = rec_m["checks"][3]["verdict"] if rec_m else None
    detected = real_verdict == "failed" and mutant_verdict == "passed"
    return detected, ["real code check 4 on the too-new case=%s" % real_verdict,
                      "mutant (ignores the packument time) check 4 on the too-new case=%s; arm a's expectation of a failure is "
                      "not met by the mutant, so the mutant is detected=%s" % (mutant_verdict, detected)]


ARMS = [
    ("a_check4_reads_packument_time", arm_a),
    ("b_no_time_or_absent_packument_refused", arm_b),
    ("c_packument_integrity_differs_refused", arm_c),
    ("d_control_mutant_ignoring_time_detected", arm_d),
]


def main():
    passed = 0
    for label, fn in ARMS:
        try:
            ok, details = fn()
        except Exception:  # an arm that cannot run is a failed arm
            ok, details = False, [traceback.format_exc(limit=3).strip()]
        for line in details:
            print("  " + line.encode("ascii", "backslashreplace").decode("ascii"))
        print(("PASS " if ok else "FAIL ") + label)
        passed += 1 if ok else 0
    ok_all = passed == len(ARMS)
    print("INTAKE-NPM-PACKUMENT arms=%d/%d ok=%s" % (passed, len(ARMS), ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
