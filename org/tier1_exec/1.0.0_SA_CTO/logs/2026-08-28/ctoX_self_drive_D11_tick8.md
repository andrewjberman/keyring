# 1.0.0_SA_CTO~X — `/self-drive D11` tick 8: ARM-1 disposed, R2-2 LANDED, Round 3 OPENED

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE

**Window:** 02:1xZ (tick-7 log @cf42d5f02b) -> 02:4xZ. Ticks covered: 8 (the cron's 02:41Z fire was
absorbed into this continuous turn). **State: ARMED** (cron `e17cfef7`; paired `/drive D11` at
`2.0.0_SA_COO~X` ticked 9 @86693abbb0, rows 3-6 consumed).

## WHAT LANDED THIS TICK (three commits, each atomic, each gated at its own hash)

1. **ARM-1 ADJUDICATED @9869831971** — `ARM1_ADJUDICATION.md`: 13 of 13 unreached values across 9
   fields (COUNT CORRECTION: tick-7 said 12 — typed beside derived; the record carries it). 2 CUT
   (`open -> valid_to null`; `partial -> evidence_refs`), 1 DEFERRED (`disputed`, R2-2), 10 NO by
   contract citation. Atomic gates: six of six exit 0 | 10 open (ARM1 8, ARM3 0, ARM4 2 of 21).
   Re-verified: CVO~X 20260828T023042Z (CUTs + sidecar + NOs PASS), CRO~X 20260828T023113Z (both
   cuts hold; strongest NO-row attack — `human_adjudicated` with `asserted_by=model:gpt` — does not
   reopen rows 5/9/11 because CVO~X's rubric commit 881a9e225e is the named external control),
   DT~X 77201 (my numbers re-derived, all hold; my 13/9 count confirmed by re-derivation).
2. **R2-2 LANDED @bf6fbe53d9** — checklist (a)-(h) in ONE commit (inventory in the commit body and
   `ISCK_CONTRACT.md` §7). Headlines: `verification_standing` 3-value; `contest_event` +
   `migration_receipt` record types; `retirement` kind + CLOSED direction table; `status_basis`
   exact-key maps REQUIRED on 5 records / 6 axes; `partial_legacy -> partial`; §3.19–3.23 five-label
   records (labels 20 of 20); §6 limit 11. Atomic gates at bf6fbe53d9: validate 4/4 + 18/18 + 83/83 +
   11/11 + meta; ablation OK; collisions 6/6; isolation 79 of 83; labels 20/20; probes ARM1 8 / ARM3
   0 / ARM4 21 live 0 NEW; **overall exit 0 | 8 open candidates (ARM1 8 by record, ARM3 0, ARM4 0 of
   21)**. C2's verdict EXECUTED (ledger row 7).
3. **ROUND 3 OPENED** (this commit) — `ROUND3_CHARTER.md` (C3 verdict: after R2-2; bounded to
   source_frontier / surface_version / consume-gate suppression / refutation specificity / bundle
   identity; CVO~X's precision adopted verbatim: a PREDECLARED deliberately-false claim, sealed
   `sha256 402da6e06c5d…` in §7, text held in this session's scratchpad only — a session death
   before the boundary yields "specificity UNMEASURED", declared). `bundle_identity.py` +
   `BUNDLE_IDENTITY.json`: every field DERIVED from git at bf6fbe53d9 —
   `bundle:sha256:0291e2ac0d2f…`, schema sha256 `0ab7bf605485…`, 8 post-boundary amendments
   enumerated (the `--check` mode fails when the record and the derivation disagree).

## THE ATTRIBUTION INCIDENT (on the record, not rewritten)

DT~X's 63-line ARM-3 fix sat uncommitted in the shared tree; its lane gate refuses `org/standards`
(ANY_EXEC). I attributed it to CVO~X from the message that NAMED the drift instead of measuring, and
asked CVO~X to commit it (77198). Before my measured stand-down (77200) arrived, CVO~X committed it
as **f2281ce7cb under the CVO~X author line** — a false attribution of a GOOD act, the kind that
survives because credit is never contested. Correction: the R2-2 landing's commit body records
f2281ce7cb content author = `0.4.0_DT_ClientPlatform~X`, committer = `3.0.0_SA_CVO~X`; DT~X's
9-line `retirement` repair and my 5 contest repairs are attributed by serial in the same body; CVO~X
is EXCLUDED from re-verifying the ARM-3 half (CRO~X carries it); COO~X's 77208 clause 2 stands and
DT~X holds a scoped `GIT_COMMIT_AUTHOR_OVERRIDE` for the ARM-1 sidecar (77214 is the authorization
record). Measured, confirmed by DT~X 77209 and COO~X 20260828T024111Z from git, not from my report.
**Lesson banked (my own):** attribute from `git status` + telemetry + liveness, never from who
described the defect; and a hands-off issued to ONE seat does not protect a file that TWO seats
are writing — DT~X's item 5 was right and the second writer was me.

## VERDICTS / CALLS

Pitched this tick: none new (C1–C3 consumed; R1 at Andrew). Ledger row 7 = C2 EXECUTED. C3's
condition MET → charter cut (driver's own act, no TO). Completion test: NOT DONE — 0 of 1 projects
`complete`; REACHABLE 1 / UNREACHABLE 0. No RESERVED card beyond R1.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `run_gates.sh 9869831971` / `bf6fbe53d9` (atomic) | exit 0 \| 10 open → exit 0 \| 8 open | the two landings, each at its own hash |
| `validate_isck.py --self-test` (tree, 5 runs) | 15/15→18/18 positive; 69→83 mutants; one ULID alphabet slip caught (`i`,`l` not Crockford) | branch-validator read gave the real reason where the top-level oneOf error lied |
| `isck_coverage_probes.py` (tree, 6 runs) | ARM1 9→8; ARM4 2 NEW → ruled class A; ARM3 5 OPEN → repaired; 8 UNSCOREABLE → fixture keyed by record type | DT~X's new cross-arm control FIRED on my first contest repair (it overwrote the value under test) — a control that earned its keep within 10 minutes of landing |
| `check_rule_ablation` / `isolation` / `collisions` / `labels` | OK / 79 of 83 / 6 of 6 / 20 of 20 | collisions 7→6: `superseded` is single-domain now |
| `bundle_identity.py bf6fbe53d9 --write --check` | OK | derived, not typed |
| `render_round2_register.py --check` | OK (63 rows) | unchanged this tick |
| `comp-find` (contract anchors, ARM4 rows, sidecar generator, partial_legacy refs) | 5 runs; one BRE-pipe warning (`\|`) taught the bare-pipe form | Andrew's 02:07Z word applied; two raw greps carried `# rail-checked` (single-file text-local); one shell comment swallowed a command tail — re-run |
| `git merge-base --is-ancestor`, `git diff --stat`, liveness.json, telemetry mtimes | the attribution measurement | after the mis-attribution, not before — the order is the lesson |
| `safe-commit -F` ×3 | 9869831971, bf6fbe53d9, (this) | ruff gate caught one unused import on the first try |

## Blockers

None at this seat. Re-verifications of bf6fbe53d9 in flight at CRO~X / CVO~X / DT~X (RAVC open).

## Next Steps

1. **[1.0.0_SA_CTO~X]** integrate round-3 findings as they arrive (register built DURING the round);
   dispositions at cited commits; boundary when both attackers declare dry. Then WP-3 design (the
   ledger's object model per memo §8) — NOT before Round 3 closes.
2. **[4.0.0_SA_CRO~X]** ARM-3 half of the bf6fbe53d9 re-verify; round-3 attacks on frontier /
   surface / bundle identity.
3. **[3.0.0_SA_CVO~X]** (a)-(h) presence audit; consume-gate suppression attack; refutation-
   specificity adjudication.
4. **[0.4.0_DT_ClientPlatform~X]** owner's probes + gates at bf6fbe53d9; ARM-1 sidecar under the
   scoped override; instrument-side attacks.
5. **[2.0.0_SA_COO~X]** row 7 consumption; gates; register denominator audit; seats if a finding
   needs one.
6. **[0.0.0_AB_MSTR]** integration window: local CLOUD is now well ahead of origin (36+ commits at
   the tick-7 read; measure at the window).

**state: ARMED** · push state of this log: LOCAL (integrator-only branch)
