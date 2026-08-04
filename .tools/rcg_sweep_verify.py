"""RCG sweep-batch verifier -- the mechanism of ruling CTOB-RCG-001 (2026-08-04).

Enforces that a sweep commit is EXACTLY a ratified, pre-committed, content-bound
ARCHIVE batch and nothing else. The ruling's principle in one line:

    AUTHORITY ATTACHES TO THE BATCH, NOT TO THE SEAT.

which is why a broad delete lane for the sweep-executor identity is safe: this
gate makes that lane unusable for anything but an exact ratified batch, and it
fires on the AUTHOR IDENTITY rather than on a declared trailer, so there is no
un-gated commit shape available to that seat.

EVERY SAFETY PROPERTY IS RE-DERIVED HERE FROM THE LEDGER AND THE TREE. The batch
says WHICH paths; it is never trusted about WHETHER they may go. A proposal
authored by the executing seat cannot also be the evidence the proposal is safe.

Checks (all must hold; see the ruling s.5 for rationale):
  C1 deletion-only            C5 re-derived charter handling == SCORE
  C2 exact set equality       C6 cohort-ratification supremacy  (the pyiceberg check)
  C3 batch prior-committed    C7 package coherence              (the click check)
  C4 re-derived label==ARCHIVE C8 size cap

rc: 0 permit | 2 DENY | 3 cannot-evaluate. THERE IS NO WARN MODE AND NO
CANNOT-EVALUATE PASS -- if the gate cannot establish a property, that is a DENY.

Usage:
  python .tools/rcg_sweep_verify.py --batch-id B-0001 [--cap N] [--staged-from-head-commit REF]

Ruling: org/tier1_exec/1.0.0_SA_CTO/deliverables/RCG_SWEEP_MECHANICS_RULING_20260804.md
Author: 1.0.0_SA_CTO~B (NFRA_REPOCOHERENCEGRAPH D-0001 item 5 / D-0004 / R-0021).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

# WS is a module global so the exercise matrix can point the verifier at a
# synthetic fixture repo (--workspace / RCG_SWEEP_WS). This is a TEST SEAM, the
# same pattern the pre-commit chain already uses (PRECOMP_REPO_ROOT,
# OWNED_PATHS_STAGED_FILES). It exists because the deny paths of this gate cannot
# otherwise be exercised without either mutating the live estate or waiting for a
# real ratified batch -- and a gate whose DENY paths have never been watched fire
# is indistinguishable from a gate that cannot fire.
WS = Path(__file__).resolve().parents[1]
LABELS = "rcg/ledger/LABELS.jsonl"
CHARTERS = "rcg/charters.yaml"
BATCHES = "rcg/ledger/BATCHES.jsonl"

PERMIT, DENY, CANNOT_EVAL = 0, 2, 3

# NUL separator for git -z output. Built with chr(0) DELIBERATELY: writing the
# two-character backslash-zero escape through a heredoc put a REAL null byte
# in this file and python refused to parse it ("source code cannot contain
# null bytes") -- twice, the second time inside the comment warning about it.
# writing that escape through a heredoc put a REAL null byte in this file and
# python refused to parse it ("source code cannot contain null bytes").
NUL = chr(0)


class CannotEvaluate(Exception):
    """Raised when a property cannot be established. Always becomes a DENY."""


def git(*args: str, allow_fail: bool = False) -> str:
    out = subprocess.run(["git", *args], cwd=WS, capture_output=True, text=True)
    if out.returncode != 0:
        if allow_fail:
            return ""
        raise CannotEvaluate(f"git {' '.join(args)} rc={out.returncode}: {out.stderr.strip()}")
    return out.stdout


def git_paths(*args: str) -> set[str]:
    """Read a PATH LIST from git with -z. Never parse paths by line or whitespace.

    Two hazards, both closed by -z:
      * a path containing a SPACE breaks any .split() consumer -- live in this
        estate right now: B-0004 deleted
        '.../session_diagfix012_leaderboard_joe_brandenbur g_fix.md', and my own
        verification script (which used .split()) reported it as 3 spurious
        non-ARCHIVE paths. B-0001..B-0003 had passed the same script by LUCK OF
        PATH CONTENT, which is the third "passed by luck of the input" of this
        session (after the xargs arg-limit and the 93-path single invocation).
      * a path with non-ASCII or control characters is C-QUOTED by git under
        core.quotepath ("a\\303\\251b"), so the emitted string is not the literal
        path and would never match the ledger entry -- a C2 set-equality FALSE
        DENY. Fail-closed, therefore safe, but it would read as batch/tree
        divergence and send an operator hunting the wrong thing, exactly like the
        xargs split did. -z suppresses quoting entirely.
    """
    return {p for p in git(*args, "-z").split("\0") if p}


def show_at_head(path: str) -> str:
    """Read a file as of HEAD. C3/C4/C5/C6 all read HEAD, never the worktree --
    the worktree is writable by the same act being judged."""
    out = subprocess.run(["git", "show", f"HEAD:{path}"], cwd=WS,
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise CannotEvaluate(f"{path} not readable at HEAD: {out.stderr.strip()}")
    return out.stdout


# ---------------------------------------------------------------- charters
def _charter_regex(key: str) -> re.Pattern:
    subtree, parts, i = key.endswith("/"), [], 0
    while i < len(key):
        if key.startswith("**/", i):
            parts.append("(?:[^/]+/)*")
            i += 3
        elif key.startswith("**", i):
            parts.append(".*")
            i += 2
        elif key[i] == "*":
            parts.append("[^/]*")
            i += 1
        else:
            parts.append(re.escape(key[i]))
            i += 1
    return re.compile("^" + "".join(parts) + (".*" if subtree else "") + "$")


def load_charters() -> list[tuple[tuple[int, int], re.Pattern, dict]]:
    try:
        import yaml
    except ImportError as e:  # fail-closed: no silent skip of the protected-class fence
        raise CannotEvaluate(f"PyYAML unavailable, cannot evaluate charters: {e}")
    spec = yaml.safe_load(show_at_head(CHARTERS))
    out = []
    for key, val in spec["charters"].items():
        # specificity: more segments + more literal chars wins; bare '*' is the floor
        sp = (-1, -1) if key == "*" else (key.count("/"), len(key.replace("*", "")))
        out.append((sp, _charter_regex(key), {"key": key, **val}))
    return out


def charter_for(path: str, compiled) -> dict:
    hits = [(sp, v) for sp, rx, v in compiled if rx.match(path)]
    if not hits:
        raise CannotEvaluate(f"no charter matches {path} -- the residual '*' rule is missing")
    hits.sort(key=lambda t: t[0])
    return hits[-1][1]


# ---------------------------------------------------------------- ledger
def load_labels() -> tuple[dict[str, dict], int]:
    """Resolve LAST ROW PER PATH -- the semantics ratified at R-0022, mechanically
    consistent with model.py's dict ingestion so no two readers diverge."""
    resolved, n = {}, 0
    for line in show_at_head(LABELS).splitlines():
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        if "label" not in row or "path" not in row:
            continue  # genesis / schema rows
        n += 1
        resolved[row["path"]] = row
    return resolved, n


def load_batch(batch_id: str) -> dict:
    """Resolve LAST ROW PER ID -- the same semantics load_labels() uses.

    CORRECTED 2026-08-04 (found by 4.0.0_SA_CRO on the live execution attempt).
    This returned the FIRST matching row, which on an APPEND-ONLY ledger is
    strictly wrong and broke the design in two places at once:

      * a batch could never leave DRAFT -- an appended RATIFIED row was
        unreachable, so C3 denied a properly ratified batch; and
      * `executed_commit` could NEVER become readable BY CONSTRUCTION, because
        it is appended AFTER the deletion commit. R3, and therefore the entire
        revert leg, was unreachable on any live ledger.

    Worse than either bug: this file's two ledgers had OPPOSITE resolution rules
    -- labels last-wins (R-0022), batches first-wins -- a latent trap for every
    future reader of either. They are now harmonized.

    WHY THE 16/16 SUITE MISSED IT: the fixture MUTATED the batch row in place
    instead of APPENDING a new one, so it never exercised the append-only shape
    the real ledger actually has. A fixture that violates the contract under test
    cannot test the contract. Third instance tonight of the same class -- CRO's
    prose-vs-ledger gap, my C6/revert PERMIT gap, and now fixture-vs-live -- and
    each one was found by running the real sequence, never by reading.

    NO FIELD MERGING: the last row wins WHOLESALE and must be complete. Merging
    would let a partial row silently inherit stale paths/sha/count from an
    earlier one, which is precisely the kind of quiet inheritance a
    delete-authorizing ledger must not have. An incomplete last row fails LOUD
    below.
    """
    resolved: dict | None = None
    seen = 0
    for line in show_at_head(BATCHES).splitlines():
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        if row.get("id") == batch_id:
            resolved = row
            seen += 1
    if resolved is None:
        raise CannotEvaluate(f"batch {batch_id} not found in {BATCHES} at HEAD")
    if seen > 1:
        print(f"  batch {batch_id}: {seen} rows, resolved to the LAST (append-only evolution)")
    if "paths" not in resolved:
        raise CannotEvaluate(
            f"batch {batch_id}'s LAST row carries no 'paths' -- resolution is last-row-wins "
            f"WHOLESALE with no field merging, so every appended row must be COMPLETE "
            f"(paths + sha256 + count + status). Append a full row, not a delta.")
    return resolved


# ---------------------------------------------------------------- checks
def run_revert_checks(batch_id: str) -> tuple[int, list[str]]:
    """REVERT mode -- the restore leg of the ruling's s.7 exercise.

    WHY THIS EXISTS, and it is a defect in the original design rather than an
    enhancement: s.7 makes an exercised `git revert` the batch-1 acceptance
    condition, because the PRD's entire safety case for `git rm` over
    move-to-archive is that reversal is one git command. But a revert of a
    deletion batch is ADDITIONS, which C1 (deletion-only) denies -- and the
    sweep identity is the ONLY identity that can reach those paths, because
    granting it the delete lanes is what made it so. Measured on B-0001:
    ~SWEEP 93/93, every exec seat 0/93.

    So the recovery path was STRUCTURALLY UNAUTHORABLE from the moment the grant
    landed: the one seat able to restore was the one seat forbidden to. Nobody
    would have found that by reading, because the deny suite was complete and
    correct -- it is the PERMIT side of the revert leg that was never driven.
    Found by 4.0.0_SA_CRO reading the source before executing, who declined to
    resolve it by overriding the gate. Same lesson as this file's own C6.

    SAFE BY CONSTRUCTION, the same way C2 is: revert mode cannot introduce
    content. Every added path must be in the ratified batch AND its staged blob
    must be hash-identical to the blob at the parent of the execution commit.
    You may restore exactly what was deleted, and nothing else.
    """
    fail: list[str] = []
    batch = load_batch(batch_id)
    declared = set(batch.get("paths") or [])
    executed = batch.get("executed_commit")
    print(f"rcg-sweep-check: REVERT mode, batch {batch_id} status={batch.get('status')} "
          f"declared={len(declared)} executed_commit={executed}")

    # --- R3 the execution commit must be recorded -------------------------
    if not executed:
        raise CannotEvaluate(
            "R3 batch has no executed_commit recorded -- there is nothing to restore FROM. "
            "Record it (in a separate commit) before reverting.")
    parent = git("rev-parse", f"{executed}^").strip()

    # --- R1 addition-only --------------------------------------------------
    nonadd = git_paths("diff", "--cached", "--name-only", "--diff-filter=DMRTUXB")
    if nonadd:
        fail.append(f"R1 NOT addition-only -- {len(nonadd)} non-addition change(s): "
                    + ", ".join(sorted(nonadd)[:5]) + (" ..." if len(nonadd) > 5 else ""))

    added = git_paths("diff", "--cached", "--name-only", "--diff-filter=A")
    print(f"  DENOMINATOR: {len(added)} staged addition(s) vs {len(declared)} declared in batch; "
          f"restoring from {parent[:12]} (parent of {str(executed)[:12]})")

    # --- R2 exact set equality, both directions ---------------------------
    extra, missing = added - declared, declared - added
    if extra:
        fail.append(f"R2 {len(extra)} path(s) added but NOT in the batch: "
                    + ", ".join(sorted(extra)[:5]) + (" ..." if len(extra) > 5 else ""))
    if missing:
        fail.append(f"R2 {len(missing)} batch path(s) NOT restored -- a partial restore leaves "
                    "the tree in neither state: " + ", ".join(sorted(missing)[:5])
                    + (" ..." if len(missing) > 5 else ""))

    # --- R4 CONTENT IDENTITY -- the check that makes this mode safe --------
    staged_blob: dict[str, str] = {}
    # --abbrev=40 IS LOAD-BEARING: `--raw` abbreviates blob shas by default, and
    # `git rev-parse <tree>:<path>` returns the full 40. Without it every single
    # path compares unequal and a PERFECT restore is denied as tampered -- which
    # is exactly how this line was first written, and what RV1 caught.
    for line in git("diff", "--cached", "--raw", "--abbrev=40",
                    "--diff-filter=A").splitlines():
        if not line.startswith(":"):
            continue
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) >= 4 and path:
            staged_blob[path] = parts[3]

    mismatched, unresolvable = [], []
    for p in sorted(added & declared):
        want = subprocess.run(["git", "rev-parse", f"{parent}:{p}"], cwd=WS,
                              capture_output=True, text=True)
        if want.returncode != 0:
            unresolvable.append(p)
            continue
        if staged_blob.get(p) != want.stdout.strip():
            mismatched.append(p)
    if unresolvable:
        fail.append(f"R4 {len(unresolvable)} path(s) did not exist at {parent[:12]} -- this is not "
                    "a restore of that deletion: " + ", ".join(unresolvable[:5]))
    if mismatched:
        fail.append(f"R4 {len(mismatched)} path(s) restored with CONTENT THAT DIFFERS from what was "
                    "deleted (revert mode may restore, never author): "
                    + ", ".join(mismatched[:5]) + (" ..." if len(mismatched) > 5 else ""))

    if not fail:
        print(f"  PERMIT -- addition-only, exactly the ratified batch, all {len(added)} blob(s) "
              f"hash-identical to {parent[:12]}. A true restore.")
    return (DENY if fail else PERMIT), fail


def run_checks(batch_id: str, cap: int) -> tuple[int, list[str]]:
    fail: list[str] = []
    note = print

    batch = load_batch(batch_id)
    declared = list(batch.get("paths") or [])
    note(f"rcg-sweep-check: batch {batch_id} status={batch.get('status')} "
         f"declared={len(declared)} ruling={batch.get('ruling')}")

    # --- C3 batch prior-committed + RATIFIED -------------------------------
    # load_batch already read HEAD, so presence is proven. The remaining half is
    # that THIS commit does not also author it (SoD: the executor may not author
    # its own authorization in the same act).
    staged_all = git_paths("diff", "--cached", "--name-only")
    if BATCHES in staged_all:
        fail.append(f"C3 batch ledger {BATCHES} is MODIFIED in this commit -- the executor may "
                    f"not author its own authorization in the same act (SoD)")
    if str(batch.get("status")).upper() != "RATIFIED":
        fail.append(f"C3 batch status is {batch.get('status')!r}, not RATIFIED")

    # integrity of the declared list against its own recorded digest
    digest = hashlib.sha256("\n".join(sorted(declared)).encode("utf-8")).hexdigest()
    if batch.get("sha256") and batch["sha256"] != digest:
        fail.append(f"C3 batch sha256 MISMATCH -- recorded {batch['sha256'][:16]}..., "
                    f"computed {digest[:16]}... over {len(declared)} sorted paths")
    if batch.get("count") is not None and int(batch["count"]) != len(declared):
        fail.append(f"C3 batch count {batch['count']} != {len(declared)} declared paths")
    if any("*" in p or "?" in p for p in declared):
        fail.append("C3 batch contains a GLOB -- explicit paths only; a glob re-expands at "
                    "execution against a different tree (ruling s.5.1)")

    # --- C1 deletion-only ---------------------------------------------------
    nondel = git_paths("diff", "--cached", "--name-only", "--diff-filter=ACMRTUXB")
    if nondel:
        fail.append(f"C1 NOT deletion-only -- {len(nondel)} non-deletion change(s): "
                    + ", ".join(sorted(nondel)[:5]) + (" ..." if len(nondel) > 5 else ""))

    deleted = git_paths("diff", "--cached", "--name-only", "--diff-filter=D")
    note(f"  DENOMINATOR: {len(deleted)} staged deletion(s) vs {len(declared)} declared in batch")

    # --- C2 exact set equality, BOTH directions -----------------------------
    dset = set(declared)
    extra, missing = deleted - dset, dset - deleted
    if extra:
        fail.append(f"C2 {len(extra)} path(s) deleted but NOT in the batch (unratified): "
                    + ", ".join(sorted(extra)[:5]) + (" ..." if len(extra) > 5 else ""))
    if missing:
        # THE HINT IS LOAD-BEARING, added 2026-08-04 after it cost a live diagnosis.
        # This gate CANNOT distinguish "the batch and the tree genuinely diverged"
        # from "your commit only carried part of the batch" -- both present as
        # missing paths. On B-0002 a 500-path list piped through xargs split into
        # multiple git invocations (375/125); the gate correctly refused all three
        # partial commits, but the message sent the operator chasing divergence
        # theories for two rounds. A deny that names the wrong cause is a correct
        # verdict pointing at the wrong repair.
        hint = ""
        if len(declared) > 100:
            hint = (f"\n        NOTE: this batch has {len(declared)} paths. If you piped them to git, "
                    "CHECK FOR PATHSPEC SPLITTING FIRST -- past the arg limit xargs silently splits "
                    "into several invocations and each partial commit fails this check. Use "
                    "`git commit --only --pathspec-from-file=<file>` (one invocation). This gate "
                    "cannot tell a partial invocation from a real divergence.")
        fail.append(f"C2 {len(missing)} batch path(s) NOT deleted by this commit -- batch and tree "
                    "have diverged: " + ", ".join(sorted(missing)[:5])
                    + (" ..." if len(missing) > 5 else "") + hint)

    # --- C8 size cap --------------------------------------------------------
    if len(deleted) > cap:
        fail.append(f"C8 batch of {len(deleted)} exceeds the ramp cap of {cap} (ruling s.7)")

    # Everything below judges the DELETED set. If C2 already failed there is
    # still value in reporting label/charter violations, so continue.
    labels, nrows = load_labels()
    compiled = load_charters()
    note(f"  re-derived from HEAD: {nrows} label row(s) -> {len(labels)} resolved path(s); "
         f"{len(compiled)} charter rule(s)")

    # --- C4 re-derived label == ARCHIVE -------------------------------------
    bad_label, unlabelled = [], []
    for p in sorted(deleted):
        row = labels.get(p)
        if row is None:
            unlabelled.append(p)
        elif row.get("label") != "ARCHIVE":
            bad_label.append((p, row.get("label"), row.get("ruling")))
    if unlabelled:
        fail.append(f"C4 {len(unlabelled)} deleted path(s) have NO label at HEAD: "
                    + ", ".join(unlabelled[:5]) + (" ..." if len(unlabelled) > 5 else ""))
    if bad_label:
        fail.append(f"C4 {len(bad_label)} deleted path(s) are not ARCHIVE at HEAD: "
                    + ", ".join(f"{p}={lab}({rul})" for p, lab, rul in bad_label[:5])
                    + (" ..." if len(bad_label) > 5 else ""))

    # --- C5 re-derived charter handling == SCORE ----------------------------
    protected = []
    for p in sorted(deleted):
        ch = charter_for(p, compiled)
        if ch.get("handling") != "SCORE":
            protected.append((p, ch["key"], ch.get("handling")))
    if protected:
        fail.append(f"C5 {len(protected)} deleted path(s) sit under a PROTECTED charter: "
                    + ", ".join(f"{p}[{h} via {k}]" for p, k, h in protected[:5])
                    + (" ..." if len(protected) > 5 else ""))

    # --- C6 cohort-ratification supremacy (the pyiceberg check) -------------
    # An andrew_ratification verdict outranks a delegated file label (R-0020
    # reserves this: "Andrew retains override on everything"; R-0022 ruled the
    # precedence). The check: if a path is being deleted and a SIBLING IN ITS OWN
    # DIRECTORY carries an andrew-ratified non-ARCHIVE label, deny.
    #
    # SCOPED TO THE IMMEDIATE DIRECTORY, DELIBERATELY -- and the first draft of
    # this check was NOT, which is why the PERMIT control exists. Walking every
    # ANCESTOR let one andrew-ratified file at the top of a tree mark the whole
    # tree ratified: a single KEEP under data/ registered "data/" as a ratified
    # cohort and denied every path beneath it. Against the live ledger that would
    # have denied all 870 data/ archives -- a gate failing LOUD but WRONG, which
    # is survivable only because something drove it to permit a legitimate batch.
    # A deny-only test suite would have scored it 10/10.
    #
    # Directory scope is what the evidence actually supports: the click specimen
    # is exactly a same-directory contradiction (core.py ARCHIVE beside
    # decorators.py andrew-KEEP). Inferring a cohort BOUNDARY from scattered file
    # labels is guesswork; a declared cohort list is the sound way to bind a whole
    # subtree, and belongs in the ledger rather than in an inference here.
    ratified_dirs: dict[str, set] = {}
    for path, row in labels.items():
        if row.get("source") != "andrew_ratification":
            continue
        d = path.rsplit("/", 1)[0] + "/" if "/" in path else ""
        ratified_dirs.setdefault(d, set()).add(row.get("label"))

    contradictions = []
    for p in sorted(deleted):
        d = p.rsplit("/", 1)[0] + "/" if "/" in p else ""
        verdicts = ratified_dirs.get(d)
        if verdicts and "ARCHIVE" not in verdicts:
            contradictions.append((p, d, sorted(verdicts)))
    if contradictions:
        fail.append(f"C6 {len(contradictions)} deleted path(s) sit under an andrew-ratified "
                    f"non-ARCHIVE subtree (cohort ratification outranks a delegated file label): "
                    + ", ".join(f"{p} under {d}={v}" for p, d, v in contradictions[:5])
                    + (" ..." if len(contradictions) > 5 else ""))

    # --- C7 package coherence (the click check) -----------------------------
    # Deleting a package's __init__.py while retaining sibling modules leaves a
    # tree that LOOKS present and cannot import. Specimen, queued for execution
    # 2026-08-03 before R-0022 corrected it:
    #   ARCHIVE click/__init__.py, click/core.py  +  KEEP click/decorators.py
    tracked = git_paths("ls-files")
    survivors = tracked - deleted
    broken = []
    for p in sorted(deleted):
        if not p.endswith("/__init__.py"):
            continue
        d = p.rsplit("/", 1)[0] + "/"
        kept = [s for s in survivors if s.startswith(d) and s.endswith(".py")]
        if kept:
            broken.append((d, len(kept)))
    if broken:
        fail.append(f"C7 {len(broken)} package(s) would lose __init__.py while retaining .py "
                    f"siblings (incoherent -- keep the package or remove it): "
                    + ", ".join(f"{d} ({n} survive)" for d, n in broken[:5])
                    + (" ..." if len(broken) > 5 else ""))

    # --- UNIQUE-CONTENT ADVISORY (added 2026-08-04) --------------------------
    # Reports how much of the batch is content that survives NOWHERE else, by
    # blob hash. DENIES NOTHING -- it exists because a batch's stated WARRANT can
    # be wrong while its mechanics are perfect.
    #
    # Measured on B-0003, described in its own row as the "snapshot-copy mass":
    # 217 of 497 had a surviving identical copy, 280 did NOT. The batch was
    # mechanically flawless -- deletion-only, all ARCHIVE, no protected charter --
    # and its justification was 44% true. Nothing was destroyed (git history
    # retains, recovery is one command), but "these were copies" is a far stronger
    # warrant than "these are old records we judged archival", and a successor
    # inherits whichever one the row claims.
    #
    # So: print the true blast radius and let the operator state a warrant that
    # holds. A gate can only check what the batch IS; this is the cheapest signal
    # about what deleting it MEANS.
    try:
        tree: dict[str, str] = {}
        for line in git("ls-tree", "-r", "-z", "HEAD").split(NUL):
            meta, _, path = line.partition("\t")
            parts = meta.split()
            if len(parts) >= 3 and path:
                tree[path] = parts[2]
        surviving_blobs = {b for p, b in tree.items() if p not in deleted}
        uniq = [p for p in sorted(deleted) if tree.get(p) and tree[p] not in surviving_blobs]
        dup = len(deleted) - len(uniq)
        note(f"  ADVISORY -- content uniqueness: {dup} of {len(deleted)} have an identical copy "
             f"surviving elsewhere; {len(uniq)} do NOT (unique content leaving the tree).")
        if uniq:
            note("      state the batch's warrant on grounds that cover the unique half:")
            for p in uniq[:5]:
                note(f"        {p}")
            if len(uniq) > 5:
                note(f"        ... +{len(uniq) - 5} more")
    except CannotEvaluate:
        note("  ADVISORY -- content uniqueness: NOT COMPUTED (tree unreadable). Advisory only.")

    # partial-directory REPORT (advisory -- residual risk 2 in the ruling: the
    # general gutted-tree class is reported, not denied)
    dirs: dict[str, int] = {}
    for p in deleted:
        dirs[p.rsplit("/", 1)[0] + "/"] = dirs.get(p.rsplit("/", 1)[0] + "/", 0) + 1
    partial = []
    for d, ndel in sorted(dirs.items()):
        nsurv = sum(1 for s in survivors if s.startswith(d) and "/" not in s[len(d):])
        if nsurv:
            partial.append((d, ndel, nsurv))
    if partial:
        note(f"  ADVISORY -- {len(partial)} directory(ies) partially deleted (reported, not denied):")
        for d, ndel, nsurv in partial[:10]:
            note(f"      {d}  -{ndel} deleted, {nsurv} survive")
        if len(partial) > 10:
            note(f"      ... +{len(partial) - 10} more")

    return (DENY if fail else PERMIT), fail


def main() -> int:
    ap = argparse.ArgumentParser(description="RCG sweep-batch gate (ruling CTOB-RCG-001)")
    ap.add_argument("--batch-id", required=True)
    ap.add_argument("--cap", type=int, default=100,
                    help="ramp cap; ruling s.7 sets batch 1 at 100 until the revert is exercised")
    ap.add_argument("--mode", choices=("execute", "revert"), default="execute",
                    help="execute = the deletion batch (C1-C8); revert = the s.7 restore leg "
                         "(R1-R4, addition-only and blob-identical to the pre-deletion tree)")
    ap.add_argument("--workspace", default=None,
                    help="TEST SEAM ONLY -- run against a fixture repo. Production callers never "
                         "pass this; the pre-commit wrapper does not expose it.")
    args = ap.parse_args()

    global WS
    if args.workspace:
        WS = Path(args.workspace).resolve()

    try:
        if args.mode == "revert":
            rc, fail = run_revert_checks(args.batch_id)
        else:
            rc, fail = run_checks(args.batch_id, args.cap)
    except CannotEvaluate as e:
        print(f"rcg-sweep-check: CANNOT EVALUATE -- {e}")
        print("  A property that cannot be established is a DENY, never a pass.")
        return CANNOT_EVAL
    except Exception as e:  # noqa: BLE001 -- any unexpected failure is fail-closed
        print(f"rcg-sweep-check: CANNOT EVALUATE -- unexpected {type(e).__name__}: {e}")
        return CANNOT_EVAL

    if fail:
        print("  SWEEP DENIED:")
        for f in fail:
            print(f"    DENY [{f.split()[0]}] {f.split(' ', 1)[1]}")
        return rc
    print("  PERMIT -- deletion-only, exactly the ratified batch, every property re-derived at HEAD.")
    return PERMIT


if __name__ == "__main__":
    sys.exit(main())
