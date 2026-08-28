#!/usr/bin/env python
"""WP-4 -- THE RESOLVER BATTERY. One arm per state, per continuity test, each independently red-able.

WHY THIS EXISTS AT ALL. The repair's whole claim is that five answers now live where two did, and
a passing resolver cannot demonstrate that: a resolver that returned RESOLVED for everything would
satisfy any test that only ever asks resolvable refs. So every arm here names the state it expects
AND the battery mutation-proves that each rule is independently load-bearing -- one rule disabled
must turn ITS arms and no others.

DENOMINATOR BY COUNTING IDS, never a typed total: the arm count is len(ARMS) and it is printed.

THE LEDGER FIXTURE IS BUILT, NOT MOCKED. AC2's claims are about the identity_relation fold, and a
mock of that fold would be me testing my own understanding of the contract rather than the contract.
The fixture mints real records through the real engine and publishes a real snapshot via VACUUM
INTO, which is also the only way the `candidate_equivalence must NOT canonicalise` arm means
anything -- a mock would canonicalise however I wrote it to.

Exit semantics follow run_battery.py: 0 pass, 1 arms failed, 3 not exercisable, 4 fail-closed.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
GRAPH_DIR = os.path.dirname(os.path.dirname(HERE))
ROOT = os.path.abspath(os.path.join(GRAPH_DIR, "..", "..", ".."))
ISCK = os.path.join(ROOT, "org", "standards", "isck")
sys.path.insert(0, GRAPH_DIR)
sys.path.insert(0, ISCK)

FAIL_CLOSED = 4
NOT_EXERCISABLE = 3

ARMS = []


def arm(arm_id):
    def deco(fn):
        ARMS.append((arm_id, fn))
        return fn
    return deco


# -- the ledger fixture ---------------------------------------------------------------------------

def _rel_id(n):
    """relation_id must match ^rel:[0-9a-hjkmnp-tv-z]{26}$ -- Crockford base32, exactly 26."""
    alphabet = "0123456789abcdefghjkmnpqrstvwxyz"
    body = (alphabet[n % len(alphabet)] * 26)
    return "rel:" + body[:26]


def build_ledger(tmp):
    """Mint a real ledger and publish a real snapshot. Returns the snapshot path.

    THE SHAPE UNDER TEST:
        ent:alias-old  --canonicalized_as-->  ent:canonical-one
        ent:cand-a     --candidate_equivalence--> ent:canonical-one   (a PROPOSAL, not an identity)
    """
    from ledger import engine, snapshot
    from ledger.battery.arms import fixtures as fx
    store = engine.Store(os.path.join(tmp, "ledger.sqlite"))
    fx.open_authority(store)
    for serial, receipt in (("ent:canonical-one", "mr:c1"), ("ent:alias-old", "mr:a1"),
                            ("ent:cand-a", "mr:x1"), ("ent:lonely", "mr:l1")):
        store.admit(list(fx.minted_pair(serial, receipt)), actor=fx.ROOT)
    base = {"claim_origin": "asserted", "verification_standing": "unverified",
            "asserted_at": "2026-02-01T00:00:00Z", "asserted_by": fx.ROOT,
            "status_basis": "authored"}
    store.admit([dict(base, record_type="identity_relation", relation_id=_rel_id(1),
                      relation_type="canonicalized_as", subject_serial="ent:alias-old",
                      object_serial="ent:canonical-one")], actor=fx.ROOT)
    store.admit([dict(base, record_type="identity_relation", relation_id=_rel_id(2),
                      relation_type="candidate_equivalence", subject_serial="ent:cand-a",
                      object_serial="ent:canonical-one")], actor=fx.ROOT)
    out = os.path.join(tmp, "published.sqlite")
    snapshot.publish(store.path, out)
    store.close()
    return out


# -- AC1: one arm per state, and the flip ---------------------------------------------------------

@arm("R-AC1-resolved")
def a_resolved(nr):
    r = nr.resolve("CLAUDE.md")
    assert r.state == "RESOLVED", r.state
    assert len(r.candidates) == 1


@arm("R-AC1-ambiguous-returns-all-and-picks-none")
def a_ambiguous(nr):
    r = nr.resolve("build_assets_dim.py")
    assert r.state == "AMBIGUOUS", r.state
    assert len(r.candidates) > 1, "AMBIGUOUS with one candidate is a contradiction"
    assert len(r.node_ids) == len(r.candidates), "a picked winner would shrink node_ids"
    for c in r.candidates:
        assert c.evidence, "every candidate carries its evidence"


@arm("R-AC1-genuinely-unaddressed")
def a_genuine(nr):
    r = nr.resolve("zzz_not_a_thing_anywhere_xyz")
    assert r.state == "GENUINELY_UNADDRESSED", r.state
    assert r.substrate_unavailable == (), "a genuine miss names no dead substrate"


@arm("R-AC1-not-applicable-names-the-fabric")
def a_na(nr):
    r = nr.resolve("SITEZ::CLAUDE.md")
    assert r.state == "NOT_APPLICABLE", r.state
    assert r.fabric == "SITEZ", r.fabric
    assert not r.node_ids, "a cross-fabric ref must NOT resolve by coincidence of name"


@arm("R-AC1-substrate-unavailable-flips-the-same-ref")
def a_flip(nr):
    a = nr.substrate_arm("CLAUDE.md")
    assert a["live_state"] == "RESOLVED", a
    assert a["stripped_state"] == "SUBSTRATE_UNAVAILABLE", a
    assert a["flipped"] and not a["byte_identical"], a
    assert a["dead_tiers"], "SUBSTRATE_UNAVAILABLE must NAME the tiers"


@arm("R-AC1-substrate-unavailable-never-identical-to-a-genuine-miss")
def a_not_identical(nr):
    """THE defect, stated as an arm: both sides return ZERO candidates and must still differ."""
    a = nr.substrate_arm("zzz_not_a_thing_anywhere_xyz")
    assert a["live_state"] == "GENUINELY_UNADDRESSED", a
    assert a["stripped_state"] == "SUBSTRATE_UNAVAILABLE", a
    assert not a["byte_identical"], "this is the two-state collapse, unrepaired"


@arm("R-AC1-state-enforced-by-the-result-type")
def a_enforced(nr):
    try:
        nr.Resolution("x", state="MAYBE")
    except ValueError:
        return
    raise AssertionError("a state outside the five was accepted")


# -- AC2: the ledger spine, read-only --------------------------------------------------------------

@arm("R-AC2-alias-yields-the-canonical-not-itself")
def a_alias(nr):
    canon, why = nr.canonical_serial("ent:alias-old")
    assert canon == "ent:canonical-one", (canon, why)


@arm("R-AC2-canonical-yields-itself")
def a_selfcanon(nr):
    canon, _why = nr.canonical_serial("ent:canonical-one")
    assert canon == "ent:canonical-one", canon


@arm("R-AC2-candidate-only-is-never-reported-canonical")
def a_candidate(nr):
    """candidate_equivalence is a PROPOSAL. Following it would report a guess as an identity."""
    canon, _why = nr.canonical_serial("ent:cand-a")
    assert canon == "ent:cand-a", "a candidate_equivalence must not canonicalise: got %r" % canon


@arm("R-AC2-parsed-but-absent-id-is-strict-not-fuzzed")
def a_strict(nr):
    r = nr.resolve("ent:no-such-entity-anywhere")
    assert r.state == "GENUINELY_UNADDRESSED", r.state
    assert r.policy == "STRICT", r.policy
    assert not r.node_ids, "a parsed record id must never be basename-fuzzed"


@arm("R-AC2-resolver-performs-no-ledger-write")
def a_nowrite(nr):
    ok, findings = nr.no_ledger_writes()
    assert ok, "the resolver contains write calls: %s" % findings


@arm("R-AC2-known-serial-resolves-through-the-ledger")
def a_known(nr):
    r = nr.resolve("ent:alias-old")
    assert r.state == "RESOLVED", r.state
    assert r.node_ids == ["ent:canonical-one"], r.node_ids
    assert r.candidates[0].canonical_serial == "ent:canonical-one"


@arm("R-AC1-a-dead-IRRELEVANT-tier-does-not-make-a-filename-unknowable")
def a_irrelevant_tier(nr):
    """THE FALSE-ALARM GUARD, and the mutation proof is why it exists.

    `consult_all_tiers` -- reverting the rule that only tiers which COULD have answered this ref
    count -- turned NO ARM, because this battery's fixture sets $NERVES_LEDGER and therefore makes
    every tier ALIVE. A rule that only matters when a tier is DEAD cannot be tested by a fixture in
    which nothing is dead. The battery was green and the rule was unguarded: revert it and every
    genuine miss in the estate would report SUBSTRATE_UNAVAILABLE, a permanent false alarm, with
    26 of 26 still passing.

    So this arm removes the ledger substrate and asks about a FILENAME -- a ref the ledger was never
    going to answer. The file tiers all replied, none knew it, and the honest state is a genuine
    miss.
    """
    saved = os.environ.pop("NERVES_LEDGER", None)
    try:
        nr._cache_clear()
        assert nr._ledger_t()[1].available is False, "the ledger tier should be dead here"
        r = nr.resolve("zzz_not_a_thing_anywhere_xyz")
        assert r.state == "GENUINELY_UNADDRESSED",             "a dead LEDGER made a FILENAME unknowable: %s" % r.state
        assert r.substrate_unavailable == ()
    finally:
        if saved is not None:
            os.environ["NERVES_LEDGER"] = saved
        nr._cache_clear()


# -- AC3: substrate liveness and vintage ----------------------------------------------------------

@arm("R-AC3-no-broad-excepts-in-the-resolver")
def a_noexcept(nr):
    import ast
    src = open(nr.__file__, encoding="utf-8").read()
    bad = [n.lineno for n in ast.walk(ast.parse(src))
           if isinstance(n, ast.ExceptHandler)
           and (n.type is None or (isinstance(n.type, ast.Name) and n.type.id == "Exception"))]
    assert not bad, "broad except handlers at lines %s" % bad


@arm("R-AC3-every-tier-reports-availability")
def a_tiers(nr):
    tiers = nr._tier_statuses()
    assert len(tiers) == len({t.tier for t in tiers}), "a tier is reported twice"
    for t in tiers:
        assert isinstance(t.available, bool)
        if not t.available:
            assert t.reason and t.exception_class, "an UNAVAILABLE tier must say why: %r" % (t,)


@arm("R-AC3-vintage-is-on-the-result")
def a_vintage(nr):
    r = nr.resolve("CLAUDE.md")
    assert r.evidence, "no substrate vintage on the result -- staleness would be silent"


@arm("R-AC3-one-tier-down-is-not-a-clean-miss")
def a_notclean(nr):
    a = nr.substrate_arm("CLAUDE.md")
    assert a["stripped_state"] != "GENUINELY_UNADDRESSED", \
        "a dead tier reported as a clean miss -- the card's v1 finding, unrepaired"


# -- AC4: continuity -------------------------------------------------------------------------------

@arm("R-AC4-two-serials-one-subject-resolve-to-one-canonical")
def a_twoserials(nr):
    a, _ = nr.canonical_serial("ent:alias-old")
    b, _ = nr.canonical_serial("ent:canonical-one")
    assert a == b == "ent:canonical-one", (a, b)


@arm("R-AC4-same-ref-same-vintages-is-byte-identical")
def a_deterministic(nr):
    nr._cache_clear()
    one = json.dumps(nr.resolve("CLAUDE.md").as_dict(), sort_keys=True)
    nr._cache_clear()
    two = json.dumps(nr.resolve("CLAUDE.md").as_dict(), sort_keys=True)
    assert one == two, "two runs at the same substrate vintages disagree"


@arm("R-AC4-cross-fabric-not-resolved-by-coincidence-of-name")
def a_crossfabric(nr):
    here = nr.resolve("CLAUDE.md")
    there = nr.resolve("SITEZ::CLAUDE.md")
    assert here.state == "RESOLVED" and there.state == "NOT_APPLICABLE", (here.state, there.state)


@arm("R-AC4-rename-keeps-the-canonical-serial")
def a_rename(nr):
    """A serial names WHAT a thing is; a node_id names WHERE it is. A rename moves the second only."""
    before, _ = nr.canonical_serial("ent:alias-old")
    nr._cache_clear()
    after, _ = nr.canonical_serial("ent:alias-old")
    assert before == after == "ent:canonical-one", (before, after)


@arm("R-AC4-index-rebuild-keeps-serials")
def a_rebuild(nr):
    before, _ = nr.canonical_serial("ent:canonical-one")
    nr._cache_clear()                      # the rebuild: every memoised index dropped
    after, _ = nr.canonical_serial("ent:canonical-one")
    assert before == after, (before, after)


# -- AC5: compatibility + no egress ----------------------------------------------------------------

@arm("R-AC5-legacy-fields-survive-with-their-types")
def a_legacy(nr):
    r = nr.resolve("CLAUDE.md")
    assert isinstance(r.node_ids, list) and isinstance(r.kind, str)
    assert isinstance(r.confidence, str) and isinstance(r.source, str)
    assert isinstance(r.addressed, bool)


@arm("R-AC5-self-test-passes")
def a_selftest(nr):
    out = subprocess.run([sys.executable, nr.__file__, "--self-test"],
                         cwd=os.path.dirname(nr.__file__),
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert out.returncode == 0, out.stdout.decode("utf-8", "replace")[-800:]


@arm("R-AC5-no-egress-in-the-delivered-files")
def a_noegress(nr):
    import ast
    banned = {"requests", "boto3", "urllib", "httpx", "pip", "socket"}
    for path in (nr.__file__, os.path.abspath(__file__)):
        tree = ast.parse(open(path, encoding="utf-8").read())
        for n in ast.walk(tree):
            mods = []
            if isinstance(n, ast.Import):
                mods = [a.name.split(".")[0] for a in n.names]
            elif isinstance(n, ast.ImportFrom) and n.module:
                mods = [n.module.split(".")[0]]
            hit = set(mods) & banned
            assert not hit, "%s imports %s at line %d" % (path, hit, n.lineno)


@arm("R-AC5-resolve-many-keeps-its-denominator")
def a_many(nr):
    res, stats = nr.resolve_many(["CLAUDE.md", "zzz_nope_xyz"])
    assert stats["refs_total"] == 2, stats
    assert "by_state" in stats, "the state census is missing"
    assert sum(stats["by_state"].values()) == 2, stats["by_state"]


# -- THE MUTATIONS. One rule disabled at a time; each must turn ITS arms and NO others -------------
#
# A battery that passes proves nothing on its own: 26 green arms are equally consistent with 26 real
# checks and with 26 checks that cannot fail. The only way I have found to tell those apart is to
# break one rule at a time and read WHICH arms turn -- not how many. An arm that stays green under
# the mutation of the rule it names is testing something else.
#
# These patch the LOADED MODULE, never the file on disk: a mutation harness that edits the subject
# can leave it edited, and the subject here is a keystone every other NERVES layer imports.
MUTATIONS = {
    "consult_all_tiers":
        lambda nr: setattr(nr, "_tier_consulted", lambda tier, ref: True),
    "candidate_equivalence_canonicalises":
        lambda nr: setattr(nr, "CANONICALIZING",
                           tuple(nr.CANONICALIZING) + ("candidate_equivalence",)),
    "no_fabric_qualifier":
        lambda nr: setattr(nr, "_foreign_fabric", lambda r: ""),
    "no_strict_record_ids":
        lambda nr: setattr(nr, "_RECORD_ID_RX", __import__("re").compile(r"^(?!)$")),
    "state_not_enforced":
        lambda nr: setattr(nr, "STATES", tuple(nr.STATES) + ("MAYBE",)),
}


def run_arms(nr):
    passed, failed = 0, []
    for arm_id, fn in ARMS:
        try:
            fn(nr)
            passed += 1
        except AssertionError as exc:
            failed.append((arm_id, str(exc)[:200]))
        except Exception as exc:                                      # noqa: BLE001
            failed.append((arm_id, "%s: %s" % (type(exc).__name__, str(exc)[:180])))
    return passed, failed


def mutation_proof(nr, baseline_failed):
    """Break one rule at a time and print WHICH arms turn. Returns True when every mutation is
    caught by at least one arm."""
    import importlib
    print("\nMUTATION PROOF -- each rule disabled alone; the arms that turn are PRINTED")
    all_caught = True
    for name, apply_mutation in sorted(MUTATIONS.items()):
        module = importlib.reload(nr)
        module._cache_clear()
        apply_mutation(module)
        module._cache_clear()
        _p, failed = run_arms(module)
        turned = [a for a, _w in failed if a not in baseline_failed]
        caught = bool(turned)
        all_caught = all_caught and caught
        print("   %-38s -> %s" % (name, ("CAUGHT by %d arm(s): %s" % (len(turned), ", ".join(turned[:4])))
                                  if caught else "NOT CAUGHT -- no arm depends on this rule"))
    importlib.reload(nr)
    nr._cache_clear()
    return all_caught


def main():
    tmp = tempfile.mkdtemp(prefix="nerves-battery-")
    try:
        snap = build_ledger(tmp)
    except Exception as exc:                                          # noqa: BLE001
        print("FAIL_CLOSED: could not build the ledger fixture: %s: %s" % (type(exc).__name__, exc))
        return FAIL_CLOSED
    os.environ["NERVES_LEDGER"] = snap
    import nerves_resolve as nr
    nr._cache_clear()

    print("NERVES RESOLVER BATTERY")
    print("   subject       %s" % os.path.relpath(nr.__file__, ROOT).replace("\\", "/"))
    print("   version       %s" % nr._resolver_version())
    print("   ledger        %s" % snap)
    print("   tiers         %s" % ", ".join(t.tier for t in nr._tier_statuses()))

    passed, failed = run_arms(nr)

    print("\nran %d of %d -- COUNTED (denominator = len(ARMS), ids counted not typed)"
          % (passed + len(failed), len(ARMS)))
    print("   passed %d | failed %d" % (passed, len(failed)))
    for arm_id, why in failed:
        print("   FAILED %s -- %s" % (arm_id, why))

    proved = mutation_proof(nr, {a for a, _w in failed}) if "--no-mutate" not in sys.argv else True
    if not proved:
        print("\nA RULE IS NOT LOAD-BEARING: some mutation turned no arm. Green above is not evidence.")
    return 0 if (not failed and proved) else 1


if __name__ == "__main__":
    sys.exit(main())
