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
GLOBAL_SCOPE = "global"

# ⛔ READ FROM THE PRODUCER, NOT HARDCODED HERE. A second copy of a declared set is a
# divergence surface: it would keep passing after the producer's set changed, and the
# row would then certify against a constituent list nobody uses. Parsed at runtime
# from the module that DECLARES it, beside the non_model construction it must not
# drift from. Falls back to an empty set, which DISABLES the scored row rather than
# guessing -- an absent declaration must never become an assumed one.
_GCC_SRC = "data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py"


def _declared_client_constituents():
    """(tuple, provenance-string). Empty tuple => the scored row is skipped."""
    try:
        import re as _re
        with open(os.path.join(_repo_root(), _GCC_SRC), encoding="utf-8") as fh:
            m = _re.search(r"^GLOBAL_CLIENT_CONSTITUENTS\s*=\s*\((.*?)\)",
                           fh.read(), _re.S | _re.M)
        if not m:
            return (), "NOT FOUND in %s -- row skipped, not assumed" % _GCC_SRC
        vals = tuple(_re.findall(r"[\"']([^\"']+)[\"']", m.group(1)))
        return vals, "declared at %s" % _GCC_SRC
    except Exception as exc:  # noqa: BLE001
        return (), "UNREADABLE (%s) -- row skipped, not assumed" % exc


def _repo_root():
    here = os.path.abspath(os.path.dirname(__file__))
    while here != os.path.dirname(here):
        if os.path.isdir(os.path.join(here, ".git")):
            return here
        here = os.path.dirname(here)
    return os.getcwd()


GLOBAL_CLIENT_CONSTITUENTS, GCC_PROVENANCE = _declared_client_constituents()


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


def check_cross_scope(docs, plane, out):
    """CROSS-SCOPE: does global aggregate its constituents, per L0 node?

    ⛔ THIS AXIS DID NOT EXIST IN THIS INSTRUMENT UNTIL NOW, AND EVERY OTHER ROW IN
    IT IS SCOPED **WITHIN** ONE SCOPE. Not one compared a scope to another. So a
    MIXED-BASIS global -- Models and SMA aggregating three firms while Client
    aggregates one -- passed all 130 rows and would have passed 130 more of the
    same shape. Found by `0.4.0_DE_ClientPlatform~Z` at 06:0xZ, corroborated by me
    on the S3 plane against their CDN read, and NOT by this instrument.
    The gap is $359,773,356.74 and it flows into `sums.total_aua`, i.e. the $2.09B
    on the panel Andrew named as his canonical design reference.

    ⛔ AND THE L0 IDENTITY CANNOT SUBSTITUTE FOR THIS ROW. `sum(nodes) ==
    sums.total_aua` holds EXACTLY under the mixed basis, because it is assembled
    from the same per-node values it would have to validate. It is the mechanism
    of concealment, not evidence -- which is precisely why a cross-scope row has
    to be measured against the CONSTITUENTS and not against the total.

    ⚠ TWO DIFFERENT EVIDENCE GRADES, AND THEY ARE LABELLED SEPARATELY:
      Client  -- the constituent set is DECLARED at
                 dim_mdpf_aggregate_aua_timeseries.py:2214
                 GLOBAL_CLIENT_CONSTITUENTS = ("49financial",), read at BUILD time
                 beside the non_model construction so it cannot drift from basis B.
                 SCORED against that declaration.
      others  -- Models/SMA are REPORTED AS A CONTROL, NEVER SCORED.

    ⛔ AND DO NOT "FIX" THAT BY ADDING A TUPLE -- FOR A STRONGER REASON THAN I FIRST
    RECORDED. I wrote here that the membership "lives in the SIGNATURE" of
    `build_global_artifact(a49, ainf, acot)` and that a signature "cannot drift from
    itself". `2.0.0_SA_COO~Z` (16495) read the fold and that is WRONG, verified by me
    at `dim_mdpf_aggregate_aua_timeseries.py:2392-2399`:
        cot_in = d in cot_covered or cot_src is not None
        if cot_in: model_aua.append(round(m49 + minf + mcot, 2))   # THREE firms
        else:      model_aua.append(_sum2(m49, minf))              # TWO firms
    >> ⛔ MODELS' CONSTITUENCY IS **DATE-CONDITIONAL**. THE SIGNATURE BOUNDS WHICH
       FIRMS *MAY* PARTICIPATE; IT DOES NOT STATE WHICH DO ON A GIVEN DATE. A firm
       can sit IN the signature and OUT of the constituency -- cottonwood does
       exactly that on uncovered dates. So the signature is not the guarantee I
       offered it as, and I withdraw that claim. <<
    ⛔ WHICH MAKES A FIXED TUPLE WORSE, NOT MERELY REDUNDANT: it would assert a
    CONSTANT membership for a DATE-VARYING one and be wrong on exactly the dates
    that discriminate. It would look like consistency with :2214 and be a defect.
    ⚠ AND `GLOBAL_CLIENT_CONSTITUENTS` IS NOT THE SAME CASE: Client's basis genuinely
    IS fixed (basis B, 49F non_model only), which is why that one is a tuple and is
    scoreable. Copying the pattern across is not consistency.
    >> **THE CONTROL ROW IS THE CORRECT PERMANENT STATE because the thing is NOT A
       STATIC SET AT ALL -- not because it is undeclared, and not because it is
       declared somewhere unparseable.** <<
    ⛔ AND `GLOBAL_MODEL_KEYS` (:139) IS a declared tuple in that same file and is
    THE WRONG AXIS -- named here so nobody reaches for it because it is the only
    parseable thing nearby.

    ⚠ TOLERANCE, STATED RATHER THAN IMPLIED. The comparison is `< CENT`, the same
    tolerance every other row here uses, so a sub-cent difference PASSES. Exercised:
    a one-cent-high global still returns PASS (float64 at ~$2.7e8 renders the
    difference as 0.00999999, below the threshold). THIS ROW IS THEREFORE NOT A
    ROUNDING-BUG DETECTOR and must not be cited as one. It is sized for the defect
    it exists to catch -- a whole constituent summed in or dropped out, which is
    $359,773,356.74 here, seven orders of magnitude above the tolerance.
    ⛔ THAT LIMIT WAS FOUND BY THE REFUSE FIXTURE, NOT BY REVIEW -- and the fixture's
    THIRD control ("one cent must FAIL") was MY over-specification, not a code
    defect. The two controls that matter both behaved: the correct basis-B value
    PASSES and the three-firm sum FAILS.
    """
    g = (docs.get(GLOBAL_SCOPE) or {}).get("nodes") or {}
    firms = [s for s in ALL_SCOPES if s != GLOBAL_SCOPE and s in docs]
    if not g or not firms:
        return
    for node in ("Models", "SMA", "Client"):
        gv = (g.get(node) or {}).get("aum")
        if gv is None:
            continue
        terms = {f: float(((docs[f].get("nodes") or {}).get(node) or {}).get("aum") or 0.0)
                 for f in firms}
        p = "%s/x-scope %s" % (plane, node)
        if node == "Client":
            # DECLARED set. A constituent outside it must NOT be summed in.
            want = round(sum(v for f, v in terms.items()
                             if f in GLOBAL_CLIENT_CONSTITUENTS), 2)
            out.append(("%s == sum(DECLARED constituents) %s"
                        % (p, list(GLOBAL_CLIENT_CONSTITUENTS)),
                        abs(round(float(gv), 2) - want) < CENT,
                        "global %.2f vs declared-sum %.2f | all %d firms would give %.2f"
                        % (float(gv), want, len(terms), round(sum(terms.values()), 2))))
        else:
            allsum = round(sum(terms.values()), 2)
            # ⛔ A DELTA HERE IS NOT NECESSARILY A DEFECT. Models' fold is
            # DATE-CONDITIONAL (:2392-2399): three firms on cottonwood-covered
            # dates, TWO otherwise. So on an uncovered date global CORRECTLY
            # differs from the 3-firm sum, and a reader who takes this row as a
            # conservation check would file a finding against a correct build.
            # Reported so the numbers are visible, NEVER scored, and the reason
            # travels in the row itself rather than in a comment nobody opens.
            out.append(("[CONTROL ONLY] %s vs sum(all %d firms)" % (p, len(terms)),
                        abs(round(float(gv), 2) - allsum) < CENT,
                        "global %.2f vs %.2f -- membership is DATE-CONDITIONAL "
                        "(3 firms on cot-covered dates, 2 otherwise); a delta may be "
                        "CORRECT. Reported, NEVER scored" % (float(gv), allsum)))


def check_member_conservation(doc, scope, plane, out):
    """L2 MEMBER RUNG: non-null members must sum to their L1 bucket, to the cent.

    ⛔ THIS INSTRUMENT HAD NO MEMBER RUNG AT ALL UNTIL NOW, AND THE MEMBER RUNG IS
    ITEM 2's ENTIRE DELIVERABLE. It scored L0 totals, L1 buckets and the Client
    split, and would have reported a fully RATIFIED build while all six SMA-family
    members served `aum: null` under a bucket holding $22.79M. A total cannot see a
    misallocation between its addends -- the blind-instrument class this whole
    deliverable exists to catch, sitting inside the catcher.

    ⭐ THE LAW IS NOT MINE AND IS NOT RE-DERIVED: `0.4.0_DS_ClientPlatform~Z`
    exercised it two-sided at `7f06a2ee40` after their own first harness shipped
    the vacuous form ("no null child under a funded bucket"), and it is stated in
    that commit message and in TO-P1-DS CATV2-TOP1-AC1's evidence field. This is
    its P2 clause, which is the half that needs no external membership data.
    ⛔ Their P1a/P1b clauses (in-by_model => NUMERIC, not-in => NULL) are NOT
    implemented here: they require the scope's `by_model` key set, which lives on a
    DIFFERENT artifact (aum-metrics). Implementing half a law and naming the half
    is honest; implementing it silently and calling it the law is not.

    ⚠ UNIVERSAL SCOPE VALIDATED BY MEASUREMENT, NOT ASSUMED. Run across 4 scopes x
    2 L0 nodes = 16 buckets before adoption: 14 MATCH, 2 MISMATCH, and the 2 are
    EXACTLY global + 49financial `SMA/ETF Strategies` -- the item-2 defect. Every
    Models bucket matches at every scope INCLUDING those with null members (global
    Custom 3/4, cottonwood Custom 1/4, 49financial Custom 0/4), which is what
    proves a null member is legitimately non-contributing and that this row does
    NOT fail a correct build. That check is why it is applied to every bucket
    rather than scoped to SMA by hand.
    """
    for l0, node in (doc.get("nodes") or {}).items():
        for l1, bucket in (node.get("children") or {}).items():
            members = bucket.get("members")
            if not isinstance(members, list) or not members:
                continue
            nonnull = [m for m in members
                       if isinstance(m, dict) and m.get("aum") is not None]
            got = round(sum(float(m["aum"]) for m in nonnull), 2)
            want = round(float(bucket.get("aum") or 0.0), 2)
            out.append(("%s/%s %s>%s members sum to bucket" % (plane, scope, l0, l1),
                        abs(got - want) < CENT,
                        "%d/%d non-null sum %.2f vs bucket %.2f"
                        % (len(nonnull), len(members), got, want)))


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
    gold_key = GOLD.format(scope=scope, as_of=as_of)
    if gold_key in WRITER_KINDS:
        # DERIVED, NOT DECLARED. The `--post-reland` form of this row asserted the
        # trigger must be manual/s3-marker, because a `scheduled` claim on a RELANDED
        # object is forged. On 2026-08-29 the 13:31Z SCHEDULED fire wrote
        # cottonwood/category-views/2026-08-28.json, and that row FAILED an HONEST
        # `scheduled` stamp -- a criterion failing a CORRECT build, which is the shape
        # this seat refused in three other lanes on the same night.
        # ROOT IS THE SAME AS THE VINTAGE BUG AT c9e94d0e3e: `--post-reland` is a fact
        # about ONE VINTAGE (the relanded 08-27 objects) and I applied it as a fact
        # about the RUN, across every scope and every as_of. A flag cannot know which
        # object it is looking at.
        # SO ASK THE PLANE THAT KNOWS: the artifact's trigger must EQUAL the kind of the
        # run whose manifest row WROTE this exact key. Forgery-proof in BOTH directions
        # -- it refuses `scheduled` on a manually-written object AND `manual` on a
        # scheduled one -- and the expectation is MEASURED rather than passed in.
        want = WRITER_KINDS[gold_key]
        out.append(("%s trigger MATCHES its writing run (manifest-derived)" % p,
                    trig == want,
                    "artifact trigger=%r vs the run that WROTE %s: kind=%r. A mismatch is "
                    "a forged stamp in whichever direction it points" % (trig, gold_key, want)))
    elif post_reland:
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


MANIFEST_PREFIX = "portal/gold/mdpf/_manifests"

# {gold key -> trigger kind of the run that WROTE it}, read from the manifest plane.
# Empty unless --score-fire was passed. Primed BEFORE the scope loop by
# prime_writer_kinds(), because check_scope consumes it and check_run_fire runs later.
WRITER_KINDS = {}
CV_TYPE = "category-views"


def list_manifest_keys(as_of):
    """Every manifest key under one as_of folder. Returns (keys, err).

    NEVER headed: the CLI auto-paginates and the only sound denominator is a
    client-side count of the whole listing (CLAUDE.md retrieval law).
    """
    r = subprocess.run(
        ["aws", "s3api", "list-objects-v2",
         "--bucket", GOLD_BUCKET,
         "--prefix", "%s/%s/" % (MANIFEST_PREFIX, as_of),
         "--query", "Contents[].Key", "--output", "text"],
        capture_output=True, text=True)
    if r.returncode != 0:
        tail = (r.stderr or "").strip().splitlines()
        return None, "list rc=%d %s" % (r.returncode, tail[-1][:80] if tail else "")
    body = (r.stdout or "").strip()
    if not body or body == "None":
        return [], None
    return sorted(k for k in body.split() if k.endswith(".json")), None


def prime_writer_kinds(as_of, since):
    """Populate WRITER_KINDS from the manifest plane BEFORE any scope is scored.

    Ordering is the whole point: check_scope consumes the map and check_run_fire
    runs after the scope loop, so priming inside check_run_fire would leave every
    trigger row unscored while looking like it worked.
    """
    # SCAN EVERY MANIFEST FOLDER, NOT _manifests/{as_of}/. THIS WAS WRONG ON THE FIRST
    # BUILD AND IT IS THE SAME CATEGORY ERROR A THIRD TIME IN ONE HOUR: the manifest
    # FOLDER is keyed by the RUN's data_as_of, while the keys INSIDE it can carry ANY
    # vintage. The 13:31Z fire sits under _manifests/2026-08-27/ and WRITES
    # cottonwood/category-views/2026-08-28.json. Priming from the as_of folder therefore
    # found nothing for the very object the scheduled run had just written, and the row
    # silently fell back to the flag branch -- looking like it worked.
    # THE RUN'S VINTAGE AND THE OBJECT'S VINTAGE ARE DIFFERENT FACTS. Filter on the run
    # TIMESTAMP, which is what `since` actually means, and let the keys say their own.
    r = subprocess.run(
        ["aws", "s3api", "list-objects-v2",
         "--bucket", GOLD_BUCKET, "--prefix", MANIFEST_PREFIX + "/",
         "--query", "Contents[].Key", "--output", "text"],
        capture_output=True, text=True)
    if r.returncode != 0:
        return
    body = (r.stdout or "").strip()
    if not body or body == "None":
        return
    keys = sorted(k for k in body.split() if k.endswith(".json"))
    fresh = [k for k in keys if os.path.basename(k)[:16] >= since] if since else keys
    for k in sorted(fresh):
        d, _e = fetch(GOLD_BUCKET, k)
        if d is None:
            continue
        t = (d.get("run", {}) or {}).get("trigger")
        kd = t.get("kind") if isinstance(t, dict) else t
        for r in (d.get("artifacts") or d.get("rows") or d.get("writes") or []):
            if r.get("status") == "written" and r.get("key"):
                WRITER_KINDS[r["key"]] = kd


def check_run_fire(as_of, since, out):
    """THE RUN PLANE -- the question the ARTIFACT STRUCTURALLY CANNOT ANSWER.

    MEASURED 2026-08-29, denominator 47 manifests: every weekend run repeats the
    preceding FRIDAY's as_of (6 of 6 weekend runs, zero counterexamples), so a
    weekend fire re-enters an EXISTING dated key. There conditional_put refuses:
    category-views is ABSENT from the closed B0 artifact_types list (denominator
    3), so business_equal raises KeyError and the fail-closed outcome is
    `conflict` -- RECORDED, NEVER OVERWRITTEN (mdpf_gold_consolidator.py:1029).

    >> SO THE ARTIFACT AFTER A REFUSED FIRE IS BYTE-IDENTICAL TO THE ARTIFACT
       AFTER NO FIRE AT ALL. Same trigger, same LastModified. A seat scoring
       TM1-AC1 / CATV-TON1-AC7 on the artifact reads `manual` and cannot tell a
       PERFECTLY-BEHAVED floor from a dead one -- and the cheap reading is the
       wrong one, because it opens an infra investigation into a correct refusal.

    The manifest is the ONLY object that separates them, and it is also the only
    place the FULL trigger dict lives: :1148 writes {kind, detail.source,
    request_id} to the MANIFEST, :1398 writes trigger.get("kind") -- KIND ONLY --
    to the ARTIFACT. Two objects, two shapes.

    NON-APPLICATION (this rule costs a listing + one GET, and only here): skip it
    entirely when no scheduled fire is claimed. It scores a FIRE, never a build.
    """
    keys, err = list_manifest_keys(as_of)
    if keys is None:
        out.append(("[FIRE] manifest listing readable", None,
                    "UNREADABLE (%s) -- INDETERMINATE, never a refusal" % err))
        return
    fresh = [k for k in keys if os.path.basename(k)[:16] >= since] if since else keys
    out.append(("[FIRE] a run manifest exists at/after %s" % (since or "<any>"),
                bool(fresh),
                "%d of %d manifest(s) under as_of=%s. ABSENT here means the fire "
                "did NOT run -- that, and only that, is the infra question"
                % (len(fresh), len(keys), as_of)))
    if not fresh:
        return
    # PER-MANIFEST, NEVER UNIONED ACROSS RUNS. EXERCISING FOUND THIS, and the
    # first build of this function had the defect: it read sorted(fresh)[-1] --
    # the NEWEST manifest -- and on 2026-08-29 the 03:55:57Z run recorded
    # category-views `written` while the 03:56:08Z run 11s later recorded
    # `unchanged`. DIFFERENT request_ids, so two invocations, not two phases.
    # The newest is not the meaningful one: the AC row FAILED on a run that had
    # in fact written, which on Monday is a FALSE FAIL OF A CORRECT FIRE -- the
    # exact criterion-shape this seat has refused in three other lanes tonight.
    #
    # >> AND THE OBVIOUS REPAIR IS WORSE THAN THE BUG. Unioning statuses across
    #    manifests would pair a MANUAL run's `written` with a LATER SCHEDULED
    #    run's kind and report a scheduled write that never happened -- one
    #    evidence banner over two evidence classes. The pair (kind, status) MUST
    #    come from ONE manifest, so the lifting row is evaluated per-run and only
    #    then reduced.
    #
    # WHY A SAME-as_of SCHEDULED FIRE CANNOT LIFT IN PLACE: `_provenance.trigger`
    # is INSIDE the artifact bytes, and conditional_put compares raw sha256 first.
    # A scheduled run at an existing key therefore ALWAYS differs from a stored
    # `manual` stamp -> business_equal -> KeyError (category-views is absent from
    # the closed B0 list, denominator 3) -> `conflict`, not overwritten. The
    # trigger stamp can NEVER be advanced in place; only a NEW dated key carries
    # a new trigger. That is why the lift is Monday's key, not today's fire.
    seen = []
    for k in sorted(fresh):
        d, e = fetch(GOLD_BUCKET, k)
        if d is None:
            out.append(("[FIRE] manifest %s readable" % os.path.basename(k), None,
                        "UNREADABLE (%s) -- INDETERMINATE, never a refusal" % e))
            continue
        run = d.get("run", {}) or {}
        t = run.get("trigger")
        kd = t.get("kind") if isinstance(t, dict) else t
        sr = ((t or {}).get("detail") or {}).get("source") if isinstance(t, dict) else None
        rw = d.get("artifacts") or d.get("rows") or d.get("writes") or []
        cvr = [r for r in rw if CV_TYPE in (r.get("key") or "")]
        # THE VINTAGE LIMB, ADDED 2026-08-29 AFTER THIS INSTRUMENT PRINTED A FALSE
        # "RATIFIED" ON THE 13:31Z FIRE. The 132 CONTENT assertions read the objects at
        # --as-of; the AC row credited a `written` from ANY key in the manifest. The
        # scheduled run conflicted 49financial/inflection/global at 2026-08-27 and wrote
        # ONLY cottonwood at 2026-08-28 -- so content came from one vintage and provenance
        # from another, under one banner. That is the SAME defect as the kind/status split
        # repaired hours earlier, one level deeper: I fixed the shallow instance and the
        # deep one survived because both halves were individually true.
        # >> A PROVENANCE ROW MUST BE PINNED TO THE OBJECT WHOSE CONTENT WAS SCORED. <<
        at_asof = sorted(set(r.get("status") for r in cvr
                             if ("/" + as_of + ".json") in (r.get("key") or "")))
        seen.append((os.path.basename(k), kd, sr,
                     sorted(set(r.get("status") for r in cvr)), len(cvr), len(rw), at_asof))
    for name, kd, sr, st, ncv, ntot, at in seen:
        print("  INFO %-58s kind=%r src=%r all=%s at-%s=%s (%d of %d rows)"
              % ("[FIRE] " + name, kd, sr, st, as_of, at, ncv, ntot))
    out.append(("[FIRE] a SCHEDULED run is among them",
                any(s[1] == "scheduled" for s in seen),
                "kinds=%s across %d manifest(s). This is the ONLY plane carrying "
                "the full {kind, detail.source, request_id}; the artifact has KIND ONLY"
                % (sorted(set(str(s[1]) for s in seen)), len(seen))))
    sched = [s for s in seen if s[1] == "scheduled"]
    out.append(("[FIRE] %s emitted by the SCHEDULED run" % CV_TYPE,
                (all(s[4] > 0 for s in sched) if sched else None),
                "row counts=%s. ZERO means the type was not built by that run -- a "
                "DIFFERENT failure from a refused write"
                % ([s[4] for s in sched] or "no scheduled run in window -- NOT scored")))
    lift = [s[0] for s in sched if "written" in s[6]]
    out.append(("[TM1-AC1/CATV-TON1-AC7] %s WRITTEN by a SCHEDULED run" % CV_TYPE,
                bool(lift),
                "lifting manifest(s)=%s. Counts ONLY a `written` AT as_of %s -- a write "
                "at a DIFFERENT vintage is another object and cannot certify the one whose "
                "content was scored. `conflict` = the fire RAN and was CORRECTLY REFUSED."
                % (lift or "NONE", as_of)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", default="2026-08-27")
    ap.add_argument("--expect-fail", action="store_true",
                    help="negative-control mode: exit 0 only if ratification FAILS")
    ap.add_argument("--score-fire", metavar="SINCE", default=None,
                    help="score the RUN plane: newest manifest at/after SINCE (YYYYMMDDTHHMMSS, '' = any). The artifact CANNOT distinguish a refused fire from no fire; only the manifest can.")
    ap.add_argument("--post-reland", action="store_true",
                    help="score _provenance.trigger: adhoc REQUIRED, a scheduled claim is FORGED")
    a = ap.parse_args()

    rows = []
    unreadable = []
    if a.score_fire is not None:
        prime_writer_kinds(a.as_of, a.score_fire)
    for plane, bucket, tmpl in (("gold", GOLD_BUCKET, GOLD),
                                ("platinum", PLAT_BUCKET, PLAT)):
        plane_docs = {}
        for scope in ALL_SCOPES:
            key = tmpl.format(scope=scope, as_of=a.as_of)
            doc, err = fetch(bucket, key)
            if doc is None:
                unreadable.append("%s s3://%s/%s: %s" % (plane, bucket, key, err))
                continue
            client_aum, sma_aum = check_scope(doc, scope, plane, rows, a.post_reland, a.as_of)
            check_prose(doc, scope, plane, rows)
            check_client_l1(doc, scope, plane, rows, a.post_reland)
            check_member_conservation(doc, scope, plane, rows)
            plane_docs[scope] = doc
            if plane == "gold" and scope == "global" and None not in (client_aum, sma_aum):
                ok = abs((client_aum + sma_aum) - CONSERVATION) < CENT
                rows.append(("[CONTROL ONLY] conservation Client+SMA == %.2f" % CONSERVATION,
                             ok, "PASSES PRE-FIX TOO -- evidences nothing alone (14091)"))
        check_cross_scope(plane_docs, plane, rows)

    if a.score_fire is not None:
        check_run_fire(a.as_of, a.score_fire, rows)

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
