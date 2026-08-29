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

⛔ INVOCATION DISCIPLINE -- READ THIS BEFORE QUOTING AN rc.
   `python ratify_sma_live.py | tail` REPORTS THE PIPE'S EXIT STATUS, NOT THIS SCRIPT'S.
   Measured 2026-08-28 at this seat: the run printed NOT RATIFIED and `$?` read 0, because
   `$?` after a pipeline is `tail`'s. At the acceptance moment that is a FALSE RATIFIED.
       WRONG   python ratify_sma_live.py | tail -14 ; rc=$?      <- rc is tail's. Always 0.
       RIGHT   python ratify_sma_live.py > out.txt 2>&1 ; rc=$?  <- capture BEFORE any pipe
   Then CROSS-CHECK the rc against the printed VERDICT line; if they disagree, trust NEITHER
   until resolved. The verdict text is authoritative and greppable:
       VERDICT: RATIFIED | VERDICT: NOT RATIFIED | VERDICT: INDETERMINATE

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

# ⛔ THESE LITERALS ARE TRUE ONLY AT as_of 2026-08-27. 0.4.0_DS_ClientPlatform~Z measured
# why (D1_CATVIEWS.TM1-AC1_TON1-AC3-AC7_score_served.py:27-33): the figure is the sum of two
# MARKET-VALUED balances, opal_div_sma 18,783,379.81 + opal_growth_sma 4,011,386.44, which
# move ~$170k-$250k per TRADING DAY across the 455-date series. Applying the literal to a
# later artifact returns FAIL ON A CORRECT FIX. Scored only at LITERAL_AS_OF; otherwise
# NA_BY_DATE -- never PASS, never FAIL. Adopting that seat's two-track design rather than
# re-inventing it.
LITERAL_AS_OF = "2026-08-27"
SMA_EXPECTED = 22794766.25
CLIENT_EXPECTED = 267632047.22
CONSERVATION = 290426813.47
SMA_SCOPES = ("global", "49financial")
ZERO_SCOPES = ("cottonwood", "inflection")
ALL_SCOPES = SMA_SCOPES + ZERO_SCOPES
CENT = 0.01

# The scope(s) whose Client L1 split is SUPPLIED BY THE CALLER rather than
# computed from a declared rule -- i.e. what item 1 (CATV2-a-1) actually wires.
# DERIVED AT SOURCE, NOT CHOSEN: mdpf_gold_consolidator :1417-1421 supplies only
# where CLIENT_L1_RULE[scope] == CLIENT_L1_DERIVED. Measured in the registry:
# CLIENT_L1_RULE has 3 keys (49financial, inflection, cottonwood) and
# CLIENT_L1_HELD has exactly 1 (cottonwood).
SUPPLY_SCOPES = ("cottonwood",)


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


# ---------------------------------------------------------------------------
# PROSE CONSISTENCY (added 2026-08-28 ~23:2xZ, after a served FALSEHOOD passed a
# 28/28 ratification). This artifact family carries PROSE IN THE PAYLOAD by design,
# and a criterion set that enumerates VALUES cannot see a wrong SENTENCE beside them.
# Measured instance: the global object's own `scope_note` reads "The global scope
# carries NO category-views object -- absent, not empty" while carrying 5 populated
# nodes. Nobody had named it, so nothing scored it.
# Each rule is (field, contradicting-substring, predicate-that-makes-it-false).
PROSE_CONTRADICTIONS = (
    ("scope_note", "carries NO category-views object",
     lambda d: bool(d.get("nodes"))),
    ("scope_note", "absent, not empty",
     lambda d: bool(d.get("nodes"))),
)


def check_prose(doc, scope, plane, out):
    """A served prose field must not contradict the object's own data."""
    for field, phrase, is_contradicted_by in PROSE_CONTRADICTIONS:
        text = doc.get(field)
        if not isinstance(text, str):
            continue
        bad = phrase.lower() in text.lower() and is_contradicted_by(doc)
        out.append(("%s/%s %s does not contradict the data" % (plane, scope, field),
                    not bad,
                    "carries %r while nodes=%d" % (phrase, len(doc.get("nodes") or {}))
                    if bad else "no contradiction found"))


def check_client_l1(doc, scope, plane, out, post_reland):
    """The Client L1 fee split (D1_CATVIEWS.CATV2-a-1, item 1). DATE-INDEPENDENT.

    ⛔ KEYED ON `view_path`, NEVER ON THE CHILD'S DISPLAY LABEL. The label is
    `display_label(node_path)` (mdpf_category_registry.py:1088) and the label
    "Client - Opal Supervised" is under ACTIVE DISCUSSION to change, because
    0.4.0_DS_ClientPlatform~Z measured that it invites the reading a CVO already
    made twice tonight. An acceptance row keyed on a string somebody is about to
    correct FAILS ON THE FIX -- the same class as the market-valued literal.
    `view_path` is the stable grain and it is what the producer emits beside it.

    ⛔ AND `third_bucket` CHILDREN CARRY NO view_path. :1090-1092 emits
    kids["Unflagged"] with {label, axis, third_bucket} and NO view_path -- so a
    bare "every child has a view_path" row would FAIL A CORRECT BUILD the first
    time an unflagged bucket is non-zero. Read at source rather than assumed;
    the disjunction below is the producer's own shape.
    """
    client = doc.get("nodes", {}).get("Client", {})
    p = "%s/%s" % (plane, scope)
    pred = client.get("predicate")
    kids = client.get("children")

    # TWO-SIDED: a declared value either way. A MISSING predicate is neither
    # state and must not read as "unavailable" by default -- absent is not held.
    out.append(("%s Client.predicate is DECLARED" % p,
                pred in ("available", "unavailable"),
                "predicate=%r" % (pred,)))

    # ⛔ WITHOUT THIS ROW THE WHOLE FUNCTION IS UNDISCRIMINATING FOR ITEM 1, AND
    # I FOUND THAT BY RUNNING IT, NOT BY READING IT. Exercised pre-reland: every
    # shape row PASSES with cottonwood at `unavailable`, and every shape row
    # would PASS AGAIN at `available` -- so 20 green rows could not tell whether
    # item 1 had landed at all. A checker that validates the shape of WHICHEVER
    # state is served, rather than that the RIGHT state is served, is the exact
    # blind-instrument class this deliverable exists to catch. Eighth defect this
    # instrument has found in itself by being run.
    # SUPPLY_SCOPES is cottonwood ALONE, and it is derived, not preferred:
    # mdpf_gold_consolidator :1417-1421 supplies ONLY where CLIENT_L1_RULE is
    # CLIENT_L1_DERIVED, and 49financial (all_supervised) / inflection
    # (all_unsupervised) have computable rules and take the rule branch. global
    # AGGREGATES and stays held while any constituent is (registry :787).
    if post_reland and scope in SUPPLY_SCOPES:
        out.append(("%s [ITEM 1] predicate MUST be available post-reland" % p,
                    pred == "available",
                    "predicate=%r -- reads 'unavailable' PRE-reland, so this row "
                    "is falsifiable in both directions" % (pred,)))

    if pred == "available":
        out.append(("%s predicate available -> children NON-EMPTY" % p,
                    isinstance(kids, dict) and len(kids) > 0,
                    "children=%d" % (len(kids) if isinstance(kids, dict) else -1)))
        if isinstance(kids, dict) and kids:
            # c3 asserts this AT BUILD. Re-reading it on the SERVED body is a
            # DIFFERENT RUNG, not a repetition: it catches a body that was
            # shaped correctly and then mutated, truncated or partially written
            # on the way to the plane the reader actually hits.
            got = round(sum(float(k.get("aum") or 0.0) for k in kids.values()), 2)
            want = round(float(client.get("aum") or 0.0), 2)
            out.append(("%s children sum to Client.aum to the cent" % p,
                        abs(got - want) < CENT,
                        "children=%.2f vs Client=%.2f (SERVED plane, not build)"
                        % (got, want)))
            ident = [k for k in kids.values()
                     if not k.get("view_path") and not k.get("third_bucket")]
            out.append(("%s every child carries view_path OR third_bucket" % p,
                        not ident,
                        "%d child(ren) carry neither" % len(ident)))
            paths = [k.get("view_path") for k in kids.values() if k.get("view_path")]
            out.append(("%s child view_paths are UNIQUE" % p,
                        len(paths) == len(set(paths)),
                        "%d path(s), %d distinct" % (len(paths), len(set(paths)))))
            # ⛔ NO NEGATIVE FEE-LINE VALUE. Added 2026-08-29 ~02:4xZ after
            # 0.4.0_DS_ClientPlatform~Z measured that the specified global
            # aggregation shape yields Client > Opal Unsupervised =
            # -$2,253,034.08 -- a NEGATIVE on an advisor-facing fee line.
            # ⛔ AND c3 CANNOT CATCH IT: defining one leg as `client_aum - other`
            # makes `SUP + UNSUP == client_aum` true for EVERY value of SUP,
            # including values that make the complement negative. The guard
            # compares an expression to itself, so the negative passes it.
            # THIS ROW IS DELIBERATELY NOT SCOPED TO global OR TO THE AGGREGATION
            # QUESTION: it is a property of the NODE, it costs one line, and it
            # outlives whichever of (A)/(B) is chosen and whoever forgets why.
            # It cannot fail a correct build -- no correct fee split is negative.
            neg = [(k.get("view_path") or k.get("label") or "?", k.get("aum"))
                   for k in kids.values() if (k.get("aum") or 0.0) < 0.0]
            out.append(("%s NO Client child has aum < 0" % p, not neg,
                        "negative leg(s): %r" % (neg,) if neg
                        else "all %d child(ren) >= 0" % len(kids)))
    elif pred == "unavailable":
        # THE HELD SHAPE IS ALSO SCORED. `predicate: "unavailable"` with no
        # children IS the render instruction (registry :1066-1074, which removed
        # the prose field precisely because the STRUCTURE carries it). A held
        # scope that ships children would let a renderer draw a split nobody
        # derived -- the mirror of the defect this whole repair is about.
        out.append(("%s predicate unavailable -> children EMPTY" % p,
                    kids == {} or kids is None,
                    "children=%r" % (kids if not kids else len(kids),)))
        out.append(("%s held scope carries a predicate_reason" % p,
                    bool(client.get("predicate_reason")),
                    "reason %s" % ("present" if client.get("predicate_reason")
                                   else "ABSENT -- a held scope with no reason")))


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

    literal_ok = (as_of == LITERAL_AS_OF)
    if scope in SMA_SCOPES:
        # ⛔ THE NA BRANCH USED TO SWALLOW A DATE-INDEPENDENT ROW. Until this split,
        # `as_of != LITERAL_AS_OF` emitted ONE NA row and scored NOTHING at these
        # scopes -- including `absent_reason ABSENT`, which has no date content at
        # all. The gate I added to stop a market-valued literal failing a correct
        # build ALSO stopped the structural check that a correct build must pass.
        # That is the over-broad-remedy shape: a fix scoped by MESSAGE ("the SMA
        # rows") rather than by PROPERTY ("the rows that move with the market").
        # It would have bitten TONIGHT, not on Monday: if the reland advances the
        # frontier to 2026-08-28, the re-ratification would have scored 0 rows at
        # global and 49financial -- the two scopes the whole repair is about --
        # and still printed a VERDICT.
        # DATE-INDEPENDENT: ALWAYS SCORED, at any as_of.
        out.append(("%s SMA.aum > 0 (structural, date-independent)" % p,
                    sma_aum is not None and sma_aum > CENT,
                    "read %r -- the pre-fix defect served an affirmative 0.00 here"
                    % (sma_aum,)))
        out.append(("%s absent_reason ABSENT" % p, not has_reason,
                    "present" if has_reason else "absent"))
        # DATE-SCOPED: the two market-valued literals, and ONLY these.
        if literal_ok:
            out.append(("%s SMA.aum == %.2f" % (p, SMA_EXPECTED),
                        sma_aum is not None and abs(sma_aum - SMA_EXPECTED) < CENT,
                        "read %r" % (sma_aum,)))
            out.append(("%s Client.aum == %.2f" % (p, CLIENT_EXPECTED),
                        client_aum is not None and abs(client_aum - CLIENT_EXPECTED) < CENT,
                        "read %r" % (client_aum,)))
        else:
            out.append(("%s SMA/Client literals NA_BY_DATE (as_of %s != %s)"
                        % (p, as_of, LITERAL_AS_OF), None,
                        "market-valued, ~$170k-250k/trading day -- NOT scored, never FAIL. "
                        "The structural rows above ARE scored."))
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
    # TRIGGER IS A GOLD-PLANE FACT. Measured: gold carries trigger='scheduled';
    # platinum carries NO trigger at all (None on all 4 scopes). Asserting it on
    # platinum would raise a FALSE FAILURE on a correct republish -- caught by
    # running the instrument, which is the fourth defect exercising has found in it.
    trig = doc.get("_provenance", {}).get("trigger")
    if plane != "gold":
        return client_aum, sma_aum
    if post_reland:
        # ⛔ CORRECTED MID-RATIFICATION, and it was a GRAIN error of mine. I asserted
        # `"adhoc" in trigger` against the ARTIFACT. Measured at source, TWO OBJECTS CARRY
        # TWO SHAPES (0.7.0_AE_CloudOps~Z, msg 14329, confirmed independently here):
        #   :1148 RUN MANIFEST  "trigger": trigger            <- the whole dict; 'adhoc' IS here
        #   :1398 ARTIFACT      "trigger": trigger.get("kind") <- KIND ONLY
        # and :1469-70 fixes the kind vocabulary to EXACTLY three values:
        #   kind = "scheduled" if src == "aws.events" else ("s3-marker" if Records else "manual")
        # `adhoc` is the SOURCE, and source is the field that never reaches the artifact.
        # So 'adhoc' is UNEMITTABLE here: I required a value the producer cannot produce, which
        # is a criterion a correct build cannot satisfy. The PROPOSITION was always "the
        # provenance is honest, not forged as scheduled" -- asserted against the real enum now.
        HONEST_RELAND_KINDS = ("manual", "s3-marker")
        out.append(("%s trigger NOT forged-scheduled (artifact kind enum)" % p,
                    trig in HONEST_RELAND_KINDS,
                    "trigger=%r -- 'scheduled' here would be FORGED; 'adhoc' is the MANIFEST's "
                    "source field and is unemittable on the artifact" % (trig,)))
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
            check_prose(doc, scope, plane, rows)
            check_client_l1(doc, scope, plane, rows, a.post_reland)
            if plane == "gold" and scope == "global" and None not in (client_aum, sma_aum):
                ok = abs((client_aum + sma_aum) - CONSERVATION) < CENT
                rows.append(("[CONTROL ONLY] conservation Client+SMA == %.2f" % CONSERVATION,
                             ok, "PASSES PRE-FIX TOO -- evidences nothing alone (14091)"))

    na = [r for r in rows if r[1] is None]
    scored = [r for r in rows
              if not r[0].startswith("[CONTROL ONLY]") and r[1] is not None]
    passed = [r for r in scored if r[1]]
    failed = [r for r in scored if not r[1]]

    print("== D1_CATVIEWS_SMA_LIVE ratification -- as_of %s ==" % a.as_of)
    for label, ok, detail in rows:
        tag = "NA:" if ok is None else ("OK:" if ok else "FAIL")
        print("  %-4s %-58s %s" % (tag, label, detail))
    print()
    print("  DENOMINATOR: %d scored assertions across %d planes x %d scopes"
          % (len(scored), 2, len(ALL_SCOPES)))
    print("  PASS %d / FAIL %d   (controls excluded from scoring: %d)"
          % (len(passed), len(failed), len(rows) - len(scored) - len(na)))
    if na:
        print("  NA_BY_DATE %d row(s): date-scoped literals not applicable at this as_of"
              % len(na))
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
        print("VERDICT: INDETERMINATE")
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
    print("VERDICT: RATIFIED" if ratified else "VERDICT: NOT RATIFIED")
    return 0 if ratified else 1


if __name__ == "__main__":
    sys.exit(main())
