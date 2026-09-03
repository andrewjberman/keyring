# Session log — NFRA_COMPEFFICACY.TO-CE-T-6 — 2026-09-03

- Seat: `0.8.0_AE_CloudComp~G`; GO Msg-ID `93784`; cell CE-t-6, round 6b.
- Archetype: VALIDATE/BUILD. Exact GO was ACKed, full TO and bounds read before write, then the GO file moved to inbox `read/`.
- Mandated `comp-read` ran on `.tools/comp-blast`, `.tools/comp-trace`, and the shim-named engine. The rail returned rc=0 but no content on Windows; direct marked reads supplied the required evidence. `comp-trace` remained untouched.

## Implementation

- `org/modules/graph/cli.py`: added shared `_compbudget` traversal carrier, deterministic direction:node cursor, `--budget`, `--cursor`, `--exact`, `--all`, trace direction aliases, partial rc=6, and answer-state outputs.
- `.tools/tests/test_comp_blast_battery.py`: six production tests plus four source-mutant controls.
- Added the T-6 s.4 report and proof instance under the lane deliverables directory.

## Evidence

- `python .tools/tests/test_comp_blast_battery.py` — 6/6 PASS.
- `python -m pytest -q .tools/tests/test_comp_blast_battery.py` — 6 passed.
- `bash .tools/commit-gate.sh org/modules/graph/cli.py .tools/tests/test_comp_blast_battery.py` — clean for 2/2 Python files.
- Real subject `arn:aws:s3:::opal-data-bd`: rc 0, 158 depth-1 downstream results, Kuzu built vintage and 27134-node denominator.
- Exact absent subject: rc 3, `SUBJECT_ABSENT_FROM_CORPUS`, no radius claim.
- Budget cut: rc 6, `PARTIAL_OR_BLIND`, BUDGET REACHED, scanned 1/158, deterministic cursor.
- Cursor resume: unbounded rc 0, WITHIN BUDGET, remaining traversal completed.
- Overlap empty population: `NOT_APPLICABLE` token.
- `comp-trace` SHA-256-equivalent blob stayed `9bcf128cf6ff4b7e95f6ed2e6869526b9588fd2d`.
- Distinct-seat FWD-9 from `2.0.0_SA_COO` at HEAD `9879a8d5ab`: carried `--exact --all --budget 0`, rc 0, 507/507 traversal, Kuzu 27134 nodes / 58432 edges, `WITHIN BUDGET`; `--budget 0` is explicitly UNBOUNDED and is not the expiry arm.

## Controls and handoff

- Comp-similar overlap recorded BY NAME ONLY; no merge or rescope.
- No graph rebuild, deployment, caller redirect, or push performed.
- T6-AC6 requires proof validation before complete flip and a post-commit carried-flag run from a seat other than this lane; COO seat was asked to run that FWD-9 after commit.

## AC-7 addendum

- Exact CRO Base addendum Msg-ID 93847 was ACKed; it identified S31 (stale-universe rebuild outside Rule-T) as an immediate T6-AC7 act.
- `comp_blast_universe.load_kuzu_universe()` now skips canonical refresh for bounded calls, serves the existing projection, and appends `BUDGETED CALL: SERVING EXISTING GRAPH STALE` with age and `needs_refresh` reason. `cmd_blast()` starts one Rule-T clock before loading and passes it through `_blast_budget_walk()`.
- Live stale-pin probe: `--budget 60` returned rc 0 in 8.5 s, stale age 0.5h / BEHIND Nessie HEAD disclosure, no `kuzu_nessie_load.py` child and no refresh launch. `--budget 0` and `--force` disclose the retained unbudgeted path.
- Battery now passes 7/7 direct and 7 pytest tests, with 5/5 source-mutant controls including the budgeted-refresh ambush mutant; commit gate clean for `cli.py`, `comp_blast_universe.py`, and the battery.
- S31 was disarmed by this seat through appended carrier row S32 in `INVESTIGATION_v1.md`; proof refreshed with T6-AC7 and its surprise reference. J’s G-2 lane was coordinated as non-overlapping and will rebase after the local commit.
