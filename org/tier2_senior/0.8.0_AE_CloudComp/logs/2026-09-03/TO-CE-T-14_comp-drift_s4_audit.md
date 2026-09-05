# Session log — NFRA_COMPEFFICACY.TO-CE-T-14 — 2026-09-03

- Seat: `0.8.0_AE_CloudComp~G`; issuer: `2.0.0_SA_COO`; GO Msg-ID: `93706`.
- Archetype: VALIDATE. Scope: `comp-drift` orchestrator, Rule-T budget/cursor semantics, answer-state controls, and s.4 evidence.
- Startup: exact serial loaded with repository-local `$load`; readiness oracle GREEN; exact root inbox file ACKed, acted on, then moved to `org/mcp/inbox/0.8.0_AE_CloudComp/~G/read/`.
- First required action: explicit `.tools/comp-read` invocation for `drift_cli.py` and `drift-topology.yaml`; both returned rc=0 without content, so direct marked inspection supplied the evidence. No seam engine was edited.

## Implementation

- `org/modules/graph/drift_cli.py`: consumed shared `.tools/_compbudget.py`; added deterministic 15-unit cursor accounting, `--budget`, `--cursor`, `EXIT_NOT_DECIDABLE=3`, and four ratified answer-state tokens.
- `.tools/tests/test_comp_drift_battery.py`: five production tests plus four source-mutant controls covering answer states, carrier, cursor, expiry rc, and help disclosure.
- Deliverable and proof instance written under the lane deliverables directory.

## Evidence

- `python .tools/tests/test_comp_drift_battery.py` — 5/5 PASS.
- `python -m pytest -q .tools/tests/test_comp_drift_battery.py` — 5 passed.
- `bash .tools/commit-gate.sh org/modules/graph/drift_cli.py .tools/tests/test_comp_drift_battery.py` — clean for 2/2 Python files.
- `sweep --budget 0.001` — rc=3, BUDGET REACHED, scanned 4/15, cursor `seam-2:iam`, `PARTIAL_OR_BLIND`.
- `sweep --budget 0 --cursor seam-2:iam` — rc=2 true seam verdict, 11/11 remaining units, no partial state.
- `sweep --deep --budget 0.001` — rc=3, scanned 0/15, `NO CURSOR YET`, `PARTIAL_OR_BLIND`.
- `--self-test` — all four exact answer-state tokens in one invocation.

## Controls and handoff

- Comp-similar overlap is BY NAME ONLY; different corpus/question, no merge or rescope.
- Surprises: none; no investigation row required.
- Proof checker is required before the complete status flip. Push state is measured after the lane commit with `git ls-remote origin refs/heads/CLOUD` and `git merge-base --is-ancestor`.
