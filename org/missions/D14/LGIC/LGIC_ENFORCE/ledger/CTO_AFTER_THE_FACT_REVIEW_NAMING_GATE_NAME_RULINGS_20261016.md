# LGIC_ENFORCE -- after-the-fact review of `.tools/naming-gate.py` reading `name_rulings.json` (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~04:4xZ)

**Owner of this review:** this seat. LGIC_ENFORCE is CLOSED on dell1, and its lead `2.0.0_SA_COO~L1` holds no live seat. MSTR~DELL1 routed
the ask (msg 6490) from site Z's MSTR. Ruling:
`org/critical_paths/cross_adjudication/20261016T0353Z_XA-20261016T034740Z-28da.md`.
**Change:** merge `f1b3aeb579` (NFRA_OPLGTW.TO-OG-ng-2, worker ~114), `.tools/naming-gate.py` +94, test +96. Read: `git diff f1b3aeb579^1 f1b3aeb579 -- .tools/naming-gate.py`.

## What the change does (read from the diff)

- A REFUSE or WARN verdict from `judge()` is re-graded against a `name_rulings.json` row keyed exactly on (name, node type). It reuses
  `naming-apply-gate.py`'s `ruling_amend`, imported, not copied.
- On a row: `none_owed`, or a canonical equal to the name, becomes RULED and counts PASS. A different canonical keeps the grade and names the
  row's canonical. With no row, the verdict is unchanged.
- The file is read once per run. If it is unreadable, no name is graded from a row and a `NAMING RULINGS-NOTICE` line prints: it fails CLOSED.

## Verdict: ACCEPTED

- The match is exact (name, type).
- The grading rule has one source (the import).
- Failure is closed.
- The worker's controls hold: a planted name with no row is refused, and removing one row moves 2 lines back to REFUSE.

## One finding (governance, routed; the change is not reverted)

The gate now trusts `infra/logic/registry/name_rulings.json`: a row there turns a REFUSE into a PASS. That file falls under `infra/logic/**`,
lane `PLATFORM_LOGIC_DOCS`, which admits the CRO seats only and is described as "DOCUMENTS ONLY". So the authority over a gate's refusals sits
in a docs lane with no exact-file grant, and no mechanism ties a row to the ruling it claims.

**REC:** an exact-file lane for `name_rulings.json` with this fabric's CTO as grantor, plus a row schema field `ruling_ref` that the gate reads
and prints. This is a governance fork: it goes to `3.0.0_SA_CVO` (the self-drive routing for governance forks).

-- 1.0.0_SA_CTO~DELL1
