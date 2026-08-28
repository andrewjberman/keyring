#!/usr/bin/env python
"""WP3 AC6 -- the CLEAN-CLONE battery runner. Executes every arm; withholds every verdict it
has not earned.

WHAT IT DOES
  1. clones an EXPLICIT build commit into a FRESH directory (never the working tree -- a working
     tree is not atomic, and a battery that reads one measures whatever another seat is mid-landing)
  2. imports the ledger and the arm registry FROM THAT CLONE, and proves it did (see the
     provenance control below)
  2b. clones into a dir unique to (run-commit, pid), or to `--clone-dir` when one is named. The
     fresh-dir refusal applies either way. A dir keyed only by commit collides between two seats on
     one workstation, and the seat that arrives second cannot replay at all -- which turns a
     completion claim into a self-report with a control standing in front of it (issuer 115237Z).
  3. runs every manifest arm as write-then-query, comparing the OBSERVED verdict against the
     manifest's DECLARED kind
  4. prints `ran N of N` where both numbers are COUNTED at run time -- never a literal
  5. exits 0 only when every arm executed AND every verdict matched

-- TWO VINTAGES, NEVER CONFLATED (CVO~X 104802Z, issuer 77686). The MANIFEST carries the CENSUS
vintage: the commit whose design text the denominator was derived from (d0398b977d). The RUNNER
needs the BUILD commit: the wave-2 commit whose ledger code is under test. Wave 1 passed the
manifest's `derived_at` to the clone, which pins the clone to a commit that PREDATES ALL LEDGER
CODE -- so the engine could never be found and the execution branch was unreachable forever. The
build commit is now an explicit `--run-commit`, and an absent or unresolvable one FAILS CLOSED
(exit 4), which is neither NOT_EXERCISABLE (3) nor a pass (0).

NOTE: THE FAILURE SHAPE WAVE 1'S CONTROL LIST MISSED, named here so the next reader sees the class.
That list hunted three shapes: a numerator counted from arms FOUND rather than the manifest's
length; a reused clone dir; exit 0 with zero arms run. All three were sound and all three held.
The shape it did not name is the one that was actually present: **the numerator is real, the
denominator is real, and the arms were never executed.** Wave 1's loop appended every id to `ran`
unconditionally, so a satisfied guard would have printed `ran 190 of 190` and exited 0 over an
EMPTY engine.py. A count printed by a loop that ran nothing is a typed count in the runner's voice,
and it would have been quoted in good faith under a TO that says "quote the runner's own line".
The general form: **a control list written by the author of the thing it controls tends to cover
the shapes the author was already thinking about.** That is why the falsifiers below are run, not
described -- a declared-but-unrun falsifier is a promise, not a control.

-- WHAT MAKES A NUMBER REAL HERE. `ran` is appended ONLY for an arm that executed AND whose
observed verdict matched its declared kind. A reject that did not reject and an accept that did not
accept land in `wrong`. An arm the registry cannot construct lands in `unimplemented`, and an arm
that raises anything other than the engine's own Rejected lands in `errored`. None of the three is
ever folded into `ran`, and any of the three is a hard failure. A silent skip cannot happen: the
denominator comes from the manifest file, the numerator from executions, and every id is accounted
for in exactly one bucket -- the runner prints the reconciliation.

-- FIXTURES ONLY (WP3-mech-5). Every store this runner opens is a file inside its own clone
directory. It has no credential, no network call and no path outside the clone; the production
substrate is unreachable from it by construction, not by intention.

SPEC ANCHOR: WP3_LEDGER_DESIGN.md sec 3 (the arms) + sec 7 (battery FIRST, code SECOND;
completion = this battery passing FROM A CLEAN CLONE); the manifest is the denominator (AC5);
the engine is ../ENGINE_CHOICE.md (AC4).
"""
import argparse
import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "MANIFEST.json")
NOT_EXERCISABLE = 3
FAIL_CLOSED = 4


class FailClosed(Exception):
    """The runner could not establish what it was asked to measure. Never a verdict."""


def load_manifest():
    with open(MANIFEST, "r", encoding="utf-8") as fh:
        doc = json.load(fh)
    return doc["derived_at"], doc["arms"]


def resolve_commit(commit, root):
    """A build commit must EXIST. Absent or unresolvable fails closed -- it is not a verdict."""
    if not commit:
        raise FailClosed("no --run-commit given; the runner will not guess a build commit, and "
                         "the manifest's derived_at is the CENSUS vintage, not a build")
    try:
        out = subprocess.check_output(["git", "rev-parse", "--verify", "%s^{commit}" % commit],
                                      cwd=root, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        raise FailClosed("run-commit %r does not resolve to a commit in this repository" % commit)
    return out.decode().strip()


def choose_clone_dir(explicit, build):
    """Pick a destination WITHOUT EVER DELETING ANYTHING.

    The wave-1 runner computed a deterministic path and then deleted it before cloning,
    which made the advertised fresh-dir refusal UNREACHABLE -- a control that cannot fire -- and
    would have silently deleted whatever a verifier named with --clone-dir. Both halves are
    defects and the second is destructive (CVO~X 115527Z; issuer 115237Z on the shared-host
    collision that surfaced it).

    Explicit dir: used as given, and refused by clean_clone if it exists -- never mutated.
    Default: a NEWLY ALLOCATED unique parent, so two concurrent invocations cannot collide and
    nothing pre-existing is ever a candidate.

    Returns (dest, owned_parent). `owned_parent` is non-None ONLY for a directory this function
    ALLOCATED on this run -- it is the sole thing the runner may later remove, and an explicit
    --clone-dir always yields None so a verifier's named directory can never be a deletion target.
    """
    if explicit:
        return explicit, None
    parent = tempfile.mkdtemp(prefix="wp3-battery-%s-" % build[:10])
    return os.path.join(parent, "clone"), parent


def clean_clone(commit, dest, root):
    if os.path.exists(dest):
        raise SystemExit("REFUSING: clone dir %s already exists -- a reused dir carries state "
                         "from the previous run and makes an arm pass for the wrong reason" % dest)
    os.makedirs(dest)
    archive = subprocess.check_output(["git", "archive", commit], cwd=root, stderr=subprocess.PIPE)
    tar = os.path.join(dest, "_pin.tar")
    with open(tar, "wb") as fh:
        fh.write(archive)
    subprocess.check_call(["tar", "-x", "-f", tar, "-C", dest], stderr=subprocess.DEVNULL)
    os.remove(tar)
    return dest


def import_from_clone(clone):
    """Import the ledger FROM THE CLONE, and PROVE it -- not from the working tree.

    Without the provenance assertion this is a silent trap: if `ledger` is already imported (the
    runner itself lives inside that package), Python reuses the working-tree module and the whole
    battery measures uncommitted code while reporting a clone commit.
    """
    pkg_root = os.path.join(clone, "org", "standards", "isck")
    for name in [n for n in list(sys.modules) if n == "ledger" or n.startswith("ledger.")]:
        del sys.modules[name]
    sys.path.insert(0, pkg_root)
    try:
        ledger = importlib.import_module("ledger")
        engine = importlib.import_module("ledger.engine")
        arms_mod = importlib.import_module("ledger.battery.arms")
    except ImportError as exc:
        raise FailClosed("the clone has no importable ledger package (%s)" % exc)
    resolved = os.path.abspath(ledger.__file__)
    if not resolved.startswith(os.path.abspath(pkg_root)):
        raise FailClosed("PROVENANCE: imported ledger from %s, which is OUTSIDE the clone %s -- "
                         "the run would have measured the working tree" % (resolved, pkg_root))
    return engine, arms_mod.load_all(), resolved


def execute(registry, arms, rejected_exc, store_factory):
    """Run every arm. THE ONE FUNCTION the falsifiers exercise, so they test the real path."""
    ran, wrong, unimplemented, errored = [], [], [], []
    for arm_id in sorted(arms):
        declared = arms[arm_id]["kind"]
        fn = registry.get(arm_id)
        if fn is None:
            unimplemented.append(arm_id)
            continue
        try:
            fn(store_factory(arm_id))
            observed = "accept"
        except rejected_exc:
            observed = "reject"
        except Exception as exc:                       # noqa: BLE001 -- reported, never absorbed
            errored.append((arm_id, "%s: %s" % (type(exc).__name__, exc)))
            continue
        if observed == declared:
            ran.append(arm_id)
        else:
            wrong.append((arm_id, declared, observed))
    return ran, wrong, unimplemented, errored


def report(arms, ran, wrong, unimplemented, errored):
    total = len(arms)
    print("ran %d of %d -- COUNTED (numerator: arms executed whose verdict matched their declared "
          "kind; denominator: distinct arm ids in the manifest)" % (len(ran), total))
    print("   reconciliation: %d matched + %d wrong + %d unimplemented + %d errored = %d of %d"
          % (len(ran), len(wrong), len(unimplemented), len(errored),
             len(ran) + len(wrong) + len(unimplemented) + len(errored), total))
    for arm_id, declared, observed in wrong[:20]:
        print("   WRONG: %s declared %s, observed %s" % (arm_id, declared, observed))
    for arm_id, msg in errored[:20]:
        print("   ERROR: %s raised %s" % (arm_id, msg))
    if unimplemented:
        print("   UNIMPLEMENTED (%d) e.g. %s" % (len(unimplemented), ", ".join(unimplemented[:5])))
    if not ran and not wrong and not errored:
        print("NOT_EXERCISABLE: zero arms executed; an empty run is never a pass.")
        return NOT_EXERCISABLE
    return 0 if (len(ran) == total and not wrong and not unimplemented and not errored) else 1


def self_test():
    """THE THREE REQUIRED FALSIFIERS plus a positive control, run against `execute` itself.

    Each drives the SAME function a real run drives, with a synthetic registry standing in for the
    engine -- so a green falsifier is evidence about the code path that actually counts, not about
    a parallel one written to agree with it.
    """
    class Rejected(Exception):
        pass

    arms = {"a-accept": {"kind": "accept", "rows": ["1"]},
            "b-reject": {"kind": "reject", "rows": ["1"]},
            "c-reject": {"kind": "reject", "rows": ["2"]}}
    rejects = [i for i, v in arms.items() if v["kind"] == "reject"]
    store = lambda _a: None                                             # noqa: E731
    ok = True

    def check(label, cond, detail):
        nonlocal ok
        print("   %-46s %s  %s" % (label, "PASS" if cond else "FAIL", detail))
        ok = ok and cond

    correct = {"a-accept": lambda s: None,
               "b-reject": lambda s: (_ for _ in ()).throw(Rejected()),
               "c-reject": lambda s: (_ for _ in ()).throw(Rejected())}
    ran, wrong, un, err = execute(correct, arms, Rejected, store)
    check("POSITIVE CONTROL correct engine", len(ran) == 3 and not (wrong or un or err),
          "ran %d of %d, wrong %d" % (len(ran), len(arms), len(wrong)))

    accept_all = {i: (lambda s: None) for i in arms}
    ran, wrong, un, err = execute(accept_all, arms, Rejected, store)
    check("FALSIFIER 1 accept-everything engine",
          len(wrong) == len(rejects) and len(ran) == 1,
          "every reject arm -> wrong (%d of %d), ran %d not %d" % (len(wrong), len(rejects),
                                                                   len(ran), len(arms)))

    ran, wrong, un, err = execute({}, arms, Rejected, store)
    check("FALSIFIER 2 empty engine (no arms)",
          len(ran) == 0 and len(un) == len(arms) and len(un) > 0,
          "0 executed, %d unimplemented -- not a pass, and not silently skipped" % len(un))

    try:
        resolve_commit("", ".")
        closed = False
    except FailClosed:
        closed = True
    try:
        resolve_commit("no-such-commit-xyzzy", ".")
        closed2 = False
    except FailClosed:
        closed2 = True
    check("FALSIFIER 3 absent/unresolvable run-commit", closed and closed2,
          "both fail closed (exit %d), neither is exit 0 or 3" % FAIL_CLOSED)

    reject_all = {i: (lambda s: (_ for _ in ()).throw(Rejected())) for i in arms}
    ran, wrong, un, err = execute(reject_all, arms, Rejected, store)
    check("CONTROL 4 reject-everything engine", len(wrong) == 1 and len(ran) == 2,
          "the accept arm -> wrong; a battery of rejects is not a pass")

    print("SELF-TEST:", "all controls behaved as declared" if ok else "A CONTROL DID NOT FIRE")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-commit", default=None,
                    help="the BUILD commit under test (NOT the manifest's census vintage)")
    ap.add_argument("--clone-dir", default=None,
                    help="where to clone. The FRESH-DIR refusal applies to whatever is named -- "
                         "the rule is kept, the shared-host collision is removed. Default is "
                         "per (run-commit, pid) so two seats on one workstation cannot collide.")
    ap.add_argument("--keep-clone", action="store_true",
                    help="keep the extract this run allocated (default: release it; an explicit "
                         "--clone-dir is never removed either way)")
    ap.add_argument("--manifest-only", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    census_vintage, arms = load_manifest()
    if args.manifest_only:
        rows = sorted({r for a in arms.values() for r in a["rows"]}, key=int)
        cites = sum(len(a["rows"]) for a in arms.values())
        print("MANIFEST census vintage %s -- COUNTED %d distinct arms / %d row citations "
              "across %d rows" % (census_vintage, len(arms), cites, len(rows)))
        return 0
    if args.self_test:
        return self_test()

    root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=HERE,
                                   stderr=subprocess.PIPE).decode().strip()
    try:
        build = resolve_commit(args.run_commit, root)
    except FailClosed as exc:
        print("FAIL_CLOSED: %s" % exc)
        print("no verdict is emitted; this is exit %d, which is neither NOT_EXERCISABLE (%d) nor "
              "a pass (0)" % (FAIL_CLOSED, NOT_EXERCISABLE))
        return FAIL_CLOSED

    dest, owned_parent = choose_clone_dir(args.clone_dir, build)
    clone = clean_clone(build, dest, root)
    print("CLEAN CLONE of BUILD commit %s -> %s" % (build, clone))
    print("MANIFEST census vintage %s (the denominator's provenance; NOT the clone)"
          % census_vintage)
    try:
        engine, registry, resolved = import_from_clone(clone)
    except FailClosed as exc:
        print("FAIL_CLOSED: %s" % exc)
        return FAIL_CLOSED
    print("IMPORTED ledger from %s (provenance asserted inside the clone)" % resolved)

    stores = os.path.join(clone, "_stores")
    os.makedirs(stores, exist_ok=True)
    factory = lambda arm_id: engine.Store(os.path.join(stores, "%s.sqlite" % arm_id))  # noqa: E731
    try:
        ran, wrong, unimplemented, errored = execute(registry, arms, engine.Rejected, factory)
        return report(arms, ran, wrong, unimplemented, errored)
    finally:
        release_clone(owned_parent, args.keep_clone)


def release_clone(owned_parent, keep):
    """Remove ONLY the parent this run allocated. Never an explicit --clone-dir. Always says which.

    MEASURED ROOT CAUSE (0.0.0_AB_MSTR 164131Z, device C: at 0.2 GB free of 255): each run leaves a
    ~1.01 GB extract in %TEMP% and ~25 of them accumulated in a single day -- 24.8 GB, alongside
    3 GB of replay extracts. The device filled, an Azure CLI install failed with MSI 1307, and this
    seat's own AC6 clean-clone run died on "No space left on device". The runner that produced the
    garbage is the right place to collect it.

    IT DELETES ONLY WHAT IT CREATED, and that narrowness is the whole design. The wave-1 runner
    deleted its destination BEFORE cloning, which both made the fresh-dir refusal unreachable and
    would have silently destroyed whatever a verifier named with --clone-dir (CVO~X 115527Z). So an
    explicit --clone-dir yields owned_parent=None here and is never a candidate; --keep-clone keeps
    even an allocated one, for the forensic case where the extract IS the evidence.
    """
    if owned_parent is None:
        print("CLONE          kept: not allocated by this run (explicit --clone-dir is never "
              "removed by the runner)")
        return
    if keep:
        print("CLONE          kept at %s (--keep-clone)" % owned_parent)
        return
    try:
        size = sum(os.path.getsize(os.path.join(dp, f))
                   for dp, _dn, fn in os.walk(owned_parent) for f in fn
                   if os.path.exists(os.path.join(dp, f)))
    except OSError:
        size = 0
    shutil.rmtree(owned_parent, ignore_errors=True)
    gone = not os.path.exists(owned_parent)
    print("CLONE          released %s (%.2f GB) -- removed: %s" % (owned_parent,
                                                                   size / 1024.0 ** 3, gone))


if __name__ == "__main__":
    sys.exit(main())
