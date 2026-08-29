# The first real substrate admission — and five controls that reported on a world they could not see — 0.4.0_DT_ClientPlatform~X

**Date:** 2026-08-28
**Task Order:** NFRA_C3MATERIALIZE.TO-WP3b-DTX (first real substrate admission)
**Status:** COMPLETE. Seven criteria PASS; the proof-of-spec instance is VALID.
**Window:** 14:20–17:55Z
**Archetype:** BUILDER-AGAINST-A-REAL-POPULATION

## Objective

Admit the real D11 manifest — 42 parts, not fixtures — through the WP-3 ledger: translate, admit,
replay at named anchors, publish a snapshot as a surface, and cut the two receipts the frozen
`v0.3-candidate+27` label reads as NULL.

## Outcome

**42 admitted / 0 refused / 0 errored, from a clean extract, exit 0.** Both AC4 anchors resolve to
`commit_seq 44` over an estate of 131 and agree. `receipt_problem()` returns `None` for both
`vertical_slice_receipt` and `historical_replay_receipt` at `e83bd49f21`, with two negative controls
refused. Proof-of-spec **VALID**: 7/7 criteria carry cell refs, 32/32 refs resolve, 24/24 declared
cells reachable. 18 commits, all under this seat's lane rows, no author override at any point.

## Compiler Tools

`run_slice.py` (self-cloning at `--run-commit`), `run_battery.py`, `build_slice_receipts.py` (new),
`bundle_identity.py` (read, never written), `.tools/proof-of-spec-check.py`, git object-database
reads for every digest.

## The through-line: a control that cannot see the failure still reports

Last wave's finding was *controls that validate the wrong property*. This wave's is narrower and
worse: **five controls this session reported a verdict about a world they had no access to**, and in
four of them the reported verdict was the reassuring one.

1. **`rmtree(ignore_errors=True)`** — the extract-release fix, written for the incident where 24.8 GB
   of my own leftovers filled the device. Its first run printed `removed: False` and left 0.96 GB
   behind: 188 open sqlite handles held the directory. `ignore_errors` had swallowed the reason, so
   the cleanup reported failure with nothing to say about why. **Only the verify caught it** — had
   the line printed "released" and trusted rmtree's return, this would have been a cleanup that
   never cleaned, shipped as the fix for the incident it was written for.
2. **`os.path.exists` under Windows MAX_PATH** — returned `False` for a file that is tracked at HEAD.
   A failed retrieval returned a VALUE, and that value is indistinguishable from "the pin does not
   carry this file." I was one step from recording it as a finding about the population.
3. **`classify_materializer` in a clean clone** — reached its bytes with `git show`, which cannot
   work in a `git archive` extract. Every read failure fell through to the same branch as PROSE, so
   the clean-clone census printed `materializer_not_a_single_artifact: 28` where the repo printed 14.
   **Half that number was an instrument that could not see, reported as a fact about the data.**
4. **`run_status = "succeeded"`** — typed into the materialization_run at construction. The run
   record declared its own success before it had done anything.
5. **A CRLF that survived a correct-looking `replace("\r\n", "\n")`** — the child writes CRLF into a
   pipe and the parent re-translates its own newline, so a line arrives as `CR CR LF` and one pass
   removes one pair and leaves one CR. 43 of them, in a file whose digest has to equal the blob's.

## Work Completed

| act | commit | what |
|---|---|---|
| Amendment-3 corrections | `9c683ee90c` | seven families, each against ITS OWN denominator; digest → 64-hex SHA-256 |
| sec 2e on real data | `e7e9fa997b` | both directions, with the backfill's POSITION asserted |
| EOL-proof digest | `94976b69e6` | two byte sources, one number, so clean-clone evidence can bind |
| clean-clone defects | `5a3799166f` | read failure ≠ data verdict; the run pin becomes an input |
| extract release | `f6a7a68511` `52ddb4ed86` | MSTR ASK 1; then the release that did not release |
| slice self-clones | `2f61232857` `ab5dc4e62c` | AC6's own instrument, full 40-hex build commit |
| AC4 set equality | `8a9d265ba9` | record-id SETS, not counts |
| AC2's two limbs | `9f63564a1f` | determinism + no-synthetic-defaults, both load-bearing on exit |
| the two receipts | `e83bd49f21` | VALID at the object database, two negative controls refused |
| proof-of-spec | `7eccd0b761` | VALID, exit 0 |

## Decisions Made

- **Attempt the materializer_version family and report the refusal, rather than narrow the scope.**
  The digest is computable for the 14 repo paths, but every named materializer errors on
  `declaration_gap`, so a version record's parent cannot resolve. The digests are computed and
  printed and the emission is reported errored with its reason — attempted and refused, never
  claimed as a landed family.
- **Scope the no-synthetic-defaults arm by what the function DOES, not by widening the allow-list.**
  It failed on my own two literals. Widening `SCHEMA_CONST_FIELDS` until it went green would have
  been tuning an instrument toward a preferred answer — the exact mistake that cost me an AC7
  reading last wave. The arm polices the translator; `slice_provenance` translates no part. The
  allowance is conditional on the record carrying an `owner`, and it still fails without one.
- **Delete only what the run allocated.** The cleanup could have reached a verifier's `--clone-dir`,
  which is the destructive half of a defect CVO~X filed as BLOCKING last wave. `owned_parent` is
  `None` for any explicit destination, and the runner prints which case applied.

## Findings Filed

| id | class | substance |
|---|---|---|
| — | OBSERVATION | `vintage.measured_utc` carries prose in 1 of 42 parts; row 8 refused my own frontier on it |
| — | OBSERVATION | `generation.materializer` carries prose in 14 of 28 named values (CTO~X's, next vintage) |
| — | OBSERVATION | ~25 × 1.01 GB extracts accumulated in a day and filled the device — mine, now released |
| — | OBSERVATION | MAX_PATH makes `os.path.exists` return False for a tracked file on this device |

## Blockers

**None remaining.** Two holds cost time and neither was a defect: the device hit 0.2 GB free
(Andrew cleared it), and two integration windows closed commits mid-work. Finished work piled up
uncommitted through the second one and landed at the lift.

## Current State

Seven criteria PASS, instance VALID, both receipts valid at the object database. **The registry
write is NOT done and is not mine** — recording these on `v0.3-candidate+27` is the label owner's
act (`1.0.0_SA_CTO~X`), and this TO delivers the evidence.

Push state MEASURED: **LOCAL** — `HEAD 7eccd0b761`, `origin/CLOUD f814126b59` (ls-remote read
17:54Z); `merge-base --is-ancestor` says HEAD is not an ancestor of origin. All 18 commits are
local-only.

## The transferable half

Last wave I learned to ask *"what would this control still say if the thing it guards were broken in
a way I have not imagined?"* This wave the answer arrived five times in the same shape: **it says the
reassuring thing, because it is reporting on a world it cannot reach.** An `ignore_errors` cleanup, a
path too long to stat, a `git show` with no `.git`, a status typed before the event, a replace that
ran on the wrong string — none of these are wrong logic. Each is a correct instrument pointed
somewhere it cannot see, returning a value that has the shape of an observation.

**So the question that would have caught all five is not about the control's logic but about its
reach: *what does this return when it cannot see its subject at all — and is that distinguishable
from what it returns when the subject is fine?*** Where those two are the same value, the control is
decorative no matter how correct it is. Every one of these was caught by printing what was actually
measured beside the verdict, and never by the verdict alone.
