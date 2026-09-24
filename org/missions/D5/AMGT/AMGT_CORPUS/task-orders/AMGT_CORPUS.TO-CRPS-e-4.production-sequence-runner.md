# AMGT_CORPUS task order -- `CRPS-e-4` -- ROUND 3: ONE runner executes the drain's production sequence in the ruled order (the backlog scan vintage before the two name-enumerating producers, the coverage census last), each step's denominators printed, stop on refusal; and the dossier interface's stale coordinate re-pointed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-e-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell writes nothing to S3 (the runner is built and listed, never run for real by a worker).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 3 (a second order, `CRPS-e-5`, follows on this slot). Serves **FWD-19**
(the re-ingest's production sequence, row `AMGT_CORPUS-Z-S18`) and the dossier interface's coordinate (round-2 analysis s.7 item 5).

## 1. THE CELL -- `CRPS-e-4`

**Where this came from.** Round 2's drain ran the producers by hand in the decomposition's order and that order omitted `backlog
--write`: `continuation` and `dossier` enumerate names from `backlog.read_latest()` (the newest research-backlog scan vintage), so
the first pass rebuilt 33 names and none of the 20 newly resolved ones (Z-S18). The corrected order, run by hand at 13:04Z, worked.
Separately, `DOSSIER_INTERFACE.md` cites `portal/src/pages/SecurityAnalysis/types.ts:955` for `ThesisBundle`; the live file's
`export interface ThesisBundle {` is at :969 (1,037 lines).

**RULED -- what you build:**
- New `lib/research/corpus/production_sequence.py`: `STEPS`, in this order and no other: `extract --write`, `extract --run-v2`,
  `typed --write`, `backlog --write`, `continuation --write`, `sector_template --write`, `fund_form --write`, `typecast --write`,
  `dossier --write`, `backlog --coverage`. `--list` prints `N <module> <flag>` one per line in order. `--run` executes each step
  as a subprocess (`python -m lib.research.corpus.<module> <flag>`) in order, streams its output, prints `=== STEP <n> <module>
  <flag> rc=<rc> <seconds>s` after each, STOPS at the first non-zero rc (the remaining steps printed `SKIPPED`), and ends with
  `production_sequence steps_run R steps_ok K stopped_at <step|none>`; `--run --from <n>` resumes at step n. It writes nothing
  itself; every write is the producer's own.
- `tests/test_production_sequence.py`: the order is asserted literally (index of `backlog --write` < `continuation --write` <
  `dossier --write` < `backlog --coverage`); a fake subprocess runner proves stop-on-refusal and `--from`; `--list`'s output
  is byte-stable.
- `DOSSIER_INTERFACE.md`: the `types.ts:955` citation becomes the live coordinate of `export interface ThesisBundle {` (read the
  live file; do not assume 969), one-line change, nothing else in the sheet moves.

## 3. SURFACES

<paths>
lib/research/corpus/production_sequence.py
lib/research/corpus/tests/test_production_sequence.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/DOSSIER_INTERFACE.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-e-4.production-sequence-runner.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module, `portal/src/pages/SecurityAnalysis/types.ts`. Scratch `.scratch/e4/`.

## 4. BOUNDS
- Pure ASCII source, LF, Python 3.9-compatible; stdlib subprocess only. NEVER run `--run` for real in this cell (it would run
  every producer against the live store); the tests fake the runner.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e4_AC1.sh</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e4_AC2.sh</invocation><expect>(?s)1 extract --write.*2 extract --run-v2.*3 typed --write.*4 backlog --write.*5 continuation --write.*6 sector_template --write.*7 fund_form --write.*8 typecast --write.*9 dossier --write.*10 backlog --coverage</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-e-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round3/e4_AC3.sh</invocation><expect>(?s)citation types\.ts:\d+ live: export interface ThesisBundle \{.*citations 1</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour (order, stop-on-refusal, resume); AC2 the seam probe: the runner's own `--list` states the ruled order;
  AC3 the coordinate: every `types.ts:<n>` the sheet cites reads `ThesisBundle` at the live line, and there is exactly one.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-e-4.production-sequence-runner.proof_of_spec.json`
   (keep the shape of your d-4 instance in that dir).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: the `--list` output and AC3's citation line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the runner is what the issuer runs at this round's drain (decomposition v3.0 s.5 duty 4) so the sequence text
and the act are one object; `backlog --coverage` last carries e-5's fourth disposition once e-5 drains. Checks dry-run at the base:
AC1 FAIL (no such test file), AC2 FAIL (no such module), AC3 FAIL (the sheet cites :955, whose live line is not ThesisBundle) --
recorded in the issuance commit.

<risk>LOCAL</risk>
<status>complete</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
