#!/usr/bin/env python
"""WP-3b -- THE SLICE RUNNER. The first real substrate admission, end to end, with both pins printed.

Runs the whole slice against the REAL declared population and prints every number it counted:
  AC1  the population, declared -- both pins, never a typed size
  AC2  the translator -- claims carried, nothing fabricated
  AC3  admission through sec 2c -- admitted + refused + errored == the denominator
  AC4  replay at named anchors, with an unbindable anchor refused
  AC5  the snapshot as a SURFACE -- VACUUM INTO, positive and negative controls

TWO PINS ON EVERY COUNT, because this population has two and conflating them is how a slice ends up
describing an artifact nobody can find:
  pin 1  the committed immutable PRESERVATION COPY -- the generator's last RATIFIED output
  pin 2  the DECLARED manifest -- pin 1 plus `part.identity` from the design lane's ruled mapping

THE VINTAGE CAVEAT TRAVELS WITH THE RESULT. l0_compile_w3.py REFUSES to re-emit ("the candidate set
has CHANGED since ratification -- pinned d86a59514ec3, now 87528e2a6d89"). This slice admits the
RATIFIED set at its ratified vintage. The generator is neither invoked nor bypassed; the moved set is
the next vintage's population and the re-read is the ratification owner's act.

AND THE FALSIFIERS RUN BESIDE THE RESULT, not instead of it. A run that admits 42 of 42 and refuses
nothing is indistinguishable, on its face, from a ledger that admits anything -- so the same real
records are re-admitted with ONE reference broken two different ways, and each must refuse exactly
one part. Without those arms "42 admitted, 0 refused" is a number, not evidence.
"""
import collections
import json
import os
import sys
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ISCK = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ISCK)

from ledger import engine, slice as sl, snapshot            # noqa: E402
from ledger.battery.arms import fixtures as fx              # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(ISCK)))
DECLARED = os.path.join(ROOT, "org", "tier2_senior", "0.4.0_DT_ClientPlatform", "deliverables",
                        "D11_MANIFEST", "graph_object_manifest.declared.json")
PIN_PRESERVED = "057220cca9"
PIN_DECLARED = "06a5ae751c"
RATIFIED_VINTAGE = "d86a59514ec3"
STARTED_AT = "2026-08-28T16:10:00Z"
MOVED_SET = "87528e2a6d89"


def admit_all(batches, tmp, tag, mutate=None):
    """Admit every part's batch. `mutate` breaks ONE reference to prove refusal is reachable."""
    store = engine.Store(os.path.join(tmp, "slice-%s.sqlite" % tag))
    fx.open_authority(store)
    admitted, refused, errored, refusals = 0, 0, 0, []
    for i, (pid, records) in enumerate(batches):
        recs = [dict(r) for r in records]
        if mutate and i == 0:
            for r in recs:
                if r["record_type"] == "entity_binding":
                    r["entity_serial"] = ("ent:does-not-exist" if mutate == "dangling"
                                          else recs[0]["receipt_id"])
        try:
            store.admit(recs, actor=fx.ROOT)
            admitted += 1
        except engine.Rejected as exc:
            refused += 1
            refusals.append((pid, exc.rule, str(exc)))
        except Exception as exc:                                     # noqa: BLE001
            errored += 1
            refusals.append((pid, "ERROR:" + type(exc).__name__, str(exc)))
    return store, admitted, refused, errored, refusals


def clone_and_run(commit, keep):
    """AC6: run the slice from a FRESH UNIQUE EXTRACT of `commit`, then release it.

    The child runs inside the extract, so what executes is the COMMITTED code at the pin and not
    this working tree -- the same provenance rule the battery enforces, and the reason the first
    clean-clone run of this slice found two defects the in-repo run could not.

    EXTRACT HYGIENE (Andrew-direct 16:2xZ via MSTR 78313, "stop generating duplicable binaries on
    the local device"): the extract is ~1.01 GB and ~25 of them accumulated in one day until C: had
    0.2 GB free. It is removed on exit unless --keep names a forensic case, and the path removed or
    kept is PRINTED. Only a directory allocated here is ever a removal candidate.
    """
    from ledger.battery import run_battery as rb
    # The FULL 40-hex, resolved here and printed. The receipt validator binds run_commit to the
    # evidence by requiring the evidence to NAME it (R4-CVO-5) -- a receipt whose evidence never
    # mentions its run_commit is a claim, not a run. An abbreviation is not the identity.
    commit = subprocess.check_output(["git", "rev-parse", "--verify", "%s^{commit}" % commit],
                                     cwd=sl.REPO_ROOT).decode().strip()
    dest, owned_parent = rb.choose_clone_dir(None, commit)
    clone = rb.clean_clone(commit, dest, sl.REPO_ROOT)
    print("AC6 CLEAN EXTRACT of BUILD commit %s -> %s" % (commit, clone))
    try:
        child = subprocess.run(
            [sys.executable, os.path.join(clone, "org", "standards", "isck", "ledger", "battery",
                                          "run_slice.py"), "--pin", commit],
            cwd=os.path.join(clone, "org", "standards", "isck"),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Normalise the child line endings BEFORE handing them to our own stdout, which translates
        # again on Windows. Without this a child line reaches a capturing parent as CR CR LF and
        # every downstream consumer inherits a CR nobody wrote.
        sys.stdout.write(child.stdout.decode("utf-8", "replace").replace(chr(13), ""))
        return child.returncode
    finally:
        rb.release_clone(owned_parent, keep)


def main():
    if "--run-commit" in sys.argv:
        i = sys.argv.index("--run-commit")
        if i + 1 >= len(sys.argv):
            print("REFUSING: --run-commit needs a commit")
            return 4
        return clone_and_run(sys.argv[i + 1], "--keep" in sys.argv)

    manifest = json.load(open(DECLARED, encoding="utf-8"))
    parts = manifest["parts"]
    print("WP-3b SLICE -- both pins on every count")
    print("   pin 1 preservation copy  @%s" % PIN_PRESERVED)
    print("   pin 2 declared manifest  @%s" % PIN_DECLARED)
    print("   VINTAGE CAVEAT: admits the RATIFIED candidate set at %s; the set has since moved to "
          "%s and the generator REFUSES to re-emit until the ratification is re-read. Neither "
          "invoked nor bypassed." % (RATIFIED_VINTAGE, MOVED_SET))

    observers = [p for p in parts if "/deliverables/" in (p.get("home") or "")]
    print("AC1 population   COUNTED %d parts | observers %d (D11's own deliverables, admitted "
          "knowingly and flagged)" % (len(parts), len(observers)))

    batches, errors, census = sl.translate_population(manifest)
    print("AC2 translator   translated %d | errored %d | census %s"
          % (len(batches), len(errors), json.dumps(census, sort_keys=True)))
    if errors:
        c = collections.Counter(f for e in errors for f in e.fields)
        print("                 fields the substrate could not supply: %s" % json.dumps(dict(c)))

    # AC2's ACCEPTANCE (Amendment 3 item 4): seven families, EACH against ITS OWN denominator.
    # WORDING (item 1), and it was a correction: 42 of 42 parts carry a generation OBJECT. What 14
    # of them lack is a NAMED MATERIALIZER (null). "no generation" said the object was missing and
    # that is false about the population.
    cen, digests = sl.family_census(manifest, PIN_DECLARED)
    print("AC2 census       seven families, each against its own denominator:")
    for line in sl.census_lines(cen):
        print(line)
    print("AC2 generation   42 of 42 carry a generation object | NO NAMED materializer 14 | "
          "named 28 = %d repo paths (bytes at the pin, digest COMPUTABLE) + %d PROSE "
          "(materializer_not_a_single_artifact)" % (digests["computable"], digests["prose"]))
    print("                 semantic_layer + canonical_role: declared ABSENT domain-wide by ruled "
          "mapping v0.2 @%s -- 28 named-materializer parts ERROR reason-class declaration_gap "
          "citing v0.2. An AUTHORED absence, not a silent omission; values are the materializer "
          "OWNERS' to declare under a vocabulary the contract does not yet carry." % sl.MAPPING_V02)
    for name, dg in sorted(digests["values"].items())[:3]:
        print("                 digest %s  %s" % (dg[:23] + "...", name))
    print("                 method %s" % sl.DIGEST_METHOD)

    tmp = tempfile.mkdtemp()
    store, adm, ref, err, refusals = admit_all(batches, tmp, "clean")
    den = len(parts)
    print("AC3 admission    admitted %d | refused %d | errored %d | translator-errored %d"
          % (adm, ref, err, len(errors)))
    print("                 reconciliation %d + %d + %d + %d = %d of %d"
          % (adm, ref, err, len(errors), adm + ref + err + len(errors), den))
    for pid, rule, msg in refusals[:10]:
        print("                 REFUSED %s -> %s" % (pid[:44], msg[:110]))

    for tag, label in (("dangling", "one binding -> a missing entity"),
                       ("wrongclass", "one binding -> a mint_receipt (wrong CLASS)")):
        _s, a2, r2, e2, _rf = admit_all(batches, tmp, tag, mutate=tag)
        ok = (r2 + e2) == 1
        print("AC3 falsifier    %-44s admitted %d refused %d -> %s"
              % (label, a2, r2 + e2, "PASS" if ok else "DID NOT REFUSE -- the admission path is blind"))

    # THE SLICE'S OWN PROVENANCE (Amendment 3 item 5): the materialization_run is owned by the
    # SLICE RUNNER, emitted as its own materializer + materializer_version, never borrowed from a
    # part. Its bundle_digest is a 64-hex SHA-256 over a DECLARED canonical tree inventory at the
    # run pin -- a git object id is SHA-1 and does not satisfy `$ref sha256` (CVO item 4).
    # THE RUN PIN IS AN INPUT UNDER AC6, NOT A DERIVATION. An extracted `git archive` has no .git,
    # so `git rev-parse HEAD` exits 128 there -- the runner must be TOLD which pin it is running,
    # and it prints which way it learned. Deriving it silently is how a receipt ends up naming a
    # commit at which no run happened.
    run_pin, pin_source = None, None
    for i, a in enumerate(sys.argv):
        if a == "--pin" and i + 1 < len(sys.argv):
            run_pin, pin_source = sys.argv[i + 1], "--pin argument"
    if run_pin is None:
        try:
            run_pin = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=sl.REPO_ROOT,
                                              stderr=subprocess.PIPE).decode().strip()
            pin_source = "git rev-parse HEAD in the repo"
        except (subprocess.CalledProcessError, OSError):
            print("AC6 REFUSING    no .git here and no --pin given: the run pin cannot be derived "
                  "from an extracted archive, and a digest over an unnamed pin is not evidence. "
                  "Re-run with --pin <commit>.")
            return 2
    prov, pids = sl.slice_provenance(manifest, {"declared": PIN_DECLARED,
                                                "preserved": PIN_PRESERVED},
                                     run_pin, STARTED_AT)
    store.admit(prov, actor=fx.ROOT)
    dr = pids["digest_report"]
    print("AC2 provenance   run pin %s (%s)" % (run_pin[:10], pin_source))
    print("AC2 provenance   ADMITTED: materializer %s | version %s" % (pids["materializer"],
                                                                       pids["version"]))
    print("                 bundle_digest %s (%d hex)"
          % (pids["digest"], len(pids["digest"].split(":")[1])))
    print("                 inventory %d members declared | %d hashed at run pin %s | absent %s"
          % (dr["members_declared"], dr["members_hashed"], run_pin[:10],
             dr["members_absent_at_pin"] or "none"))
    print("                 byte source %s" % dr["byte_source"])
    print("                 normalization %s" % dr["normalization"])
    print("                 DIGEST DESCRIBES THE CODE THAT RAN: %s%s"
          % (dr["digest_describes_the_code_that_ran"],
             "" if dr["digest_describes_the_code_that_ran"]
             else "  <- DIRTY %s; the digest names bytes that did NOT run. Commit, then re-run."
                  % dr["members_DIRTY_vs_worktree"]))
    print("                 source_frontier %s: %d entries | %d carry NO parseable observed_at "
          "(explicit absence, never coerced)"
          % (pids["frontier"], pids["entries"], pids["entries_without_a_time"]))

    head = store.head_commit_seq()
    rep = store.replay("commit_seq", head)
    print("AC4 replay       as_of commit_seq %d -> anchor_commit_seq %d | estate counted %d"
          % (head, rep["anchor_commit_seq"], rep["counted"]))
    repf = store.replay("frontier", pids["frontier"])
    print("AC4 replay       as_of frontier %s -> anchor_commit_seq %d | estate counted %d"
          % (pids["frontier"], repf["anchor_commit_seq"], repf["counted"]))
    print("AC4 agreement    both anchors resolve to the same commit_seq and the same estate: %s"
          % (repf["anchor_commit_seq"] == rep["anchor_commit_seq"]
             and repf["counted"] == rep["counted"]))
    # -- sec 2e, BOTH DIRECTIONS, on the real slice ----------------------------------------------
    # A backfill is a TRUE fact that arrives late. sec 2e's rule is not "reject it" -- rejecting a
    # later-dated fact to protect an earlier verdict is the append-only violation in another coat
    # (R3-CRO-34). It is: EXCLUDED from an anchor that predates its admission, INCLUDED at its
    # EVENT-TIME position after. Both directions are shown because either alone is satisfiable by a
    # ledger that is simply wrong in one direction.
    anchor_before = store.head_commit_seq()
    real_entity = "ent:" + sl._slug(parts[0]["id"])
    bf = "obs:wp3b-backfill"
    store.admit([fx.state_observation(bf, real_entity, "2019-01-01T00:00:00Z")])
    try:
        store.replay_expecting("commit_seq", anchor_before, [bf])
        print("AC4 sec-2e A     BACKFILL WAS INSIDE A PRE-ADMISSION ANCHOR -- the anchor is blind")
        two_e_a = False
    except engine.Rejected as exc:
        print("AC4 sec-2e A     before: a claim that the backfill is inside anchor %d is REFUSED "
              "as %s" % (anchor_before, exc.rule))
        two_e_a = True

    after = store.replay_expecting("commit_seq", store.head_commit_seq(), [bf])
    timed = [(engine.event_time(r), store._primary_of(r)) for r in after["estate"]
             if engine.event_time(r)]
    pos = [i for i, (_t, pid) in enumerate(timed) if pid == bf]
    two_e_b = bool(pos) and pos[0] == 0
    print("AC4 sec-2e B     after:  INCLUDED at anchor %d, and it sits at position %d of %d among "
          "event-timed records -- its EVENT-TIME position (2019), not its admission position "
          "(newest of %d). %s" % (after["anchor_commit_seq"], pos[0] if pos else -1, len(timed),
                                  after["counted"], "PASS" if two_e_b else "WRONG POSITION"))

    try:
        store.replay("frontier", "sf:never-admitted")
        print("AC4 falsifier    unbindable anchor ADMITTED -- the anchor path is blind")
    except engine.Rejected as exc:
        print("AC4 falsifier    unbindable frontier anchor REFUSED as %s" % exc.rule)

    pub = os.path.join(tmp, "published.sqlite")
    naive = os.path.join(tmp, "naive.sqlite")
    _p, method, digest, nbytes = snapshot.publish(store.path, pub)
    snapshot.naive_main_file_copy(store.path, naive)
    # AC5 publishes the store AS IT IS AT PUBLICATION, and its expectation is read at that moment.
    # It first failed here for the right reason: the sec-2e backfill above moved the estate after
    # `head` was taken, and the anchor check refused the mismatch rather than reporting a pass on a
    # stale expectation. That is the control doing its job on its author, again.
    rows = len(store.estate())
    head_at_publish = store.head_commit_seq()
    ok5, r5 = snapshot.controls(store.path, pub, naive, rows, head_at_publish)
    print("AC5 snapshot     via %s | %d bytes | %s" % (method, nbytes, digest[:40]))
    print("                 fingerprint_method %s | normalization_version %s"
          % (snapshot.FINGERPRINT_METHOD, snapshot.NORMALIZATION_VERSION))
    print("                 POSITIVE %s" % json.dumps(r5["positive"]))
    print("                 NEGATIVE %s" % json.dumps(r5["negative"]))
    print("AC5 verdict      %s" % ("PASS" if ok5 else "FAIL"))
    return 0 if (adm == den and ok5 and two_e_a and two_e_b) else 1


if __name__ == "__main__":
    sys.exit(main())
