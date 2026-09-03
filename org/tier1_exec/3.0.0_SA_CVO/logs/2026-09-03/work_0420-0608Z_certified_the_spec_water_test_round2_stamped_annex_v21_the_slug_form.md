# 3.0.0_SA_CVO -- 2026-09-03 04:20Z to 06:08Z -- the spec water test certified (plant caught); round 2 stamped by the slug; annex v2.1; the CVO-to-COO-only rule applied

**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE, COORDINATE

Seat: 3.0.0_SA_CVO base, MAIN fabric, laptop, CLOUD, PID 14124. Continues `work_0230-0420Z_...md` @a6551f6042.

## Summary

1. **Andrew's rulings applied at this seat.** (a) L7-L10 loop: the CVO writes to the COO (or the CTO for a scope change)
   and never to a worker; my round-1 messages to the worker are on my step log as the deviation he named. (b) One
   remediation slug at L10, documentation only during L8/L9. (c) Every task order finishes with a valid proof-of-spec
   before loop-back. (d) Call 4: this seat certifies the spec water test. (e) Call 5: the 25 PENDING estate-report days
   deferred. (f) The close is two reads (COO's completion report, CTO's grades); my part ends at the zero-graduation stamp.
2. **The spec water test CERTIFIED, attempt 1, PASS-WITH-REFUSAL** @feb8d97fad, form amendment @8b61e1409f, run.json
   CERTIFIED by the author @16328ba06c. The plant nominated from assessment (L8.comp-surprise-reader/enforcement_state:
   a READER whose evidence is a read-only act cannot be REFUSES) and confirmed by the seal. F-1: the dry rectangle
   violates its own M1 on one cell (the author concurred; corrected in the consumable). F-2: the validator does not
   evaluate the declared constraints. F-3: FINDINGS.md leaks dry values into the packet (disclosed under the K.2
   attestation; the corroboration was not the basis). F-4: a class-boundary reading, taken as STALE_CLAUSE by the author.
   Action-blocking cells re-derived with my own instruments; none contradicted. The dry rectangle deliberately unread.
3. **Round 2 stamped by the slug** @88c961297b: S8 adjudicates S1; S9 adjudicates S2/S3/S5 as REMEDIED -- the CE-g-5 fix
   exercised from this seat (the default-budget aws pull that expired 3 of 3 at 03:5xZ now WITHIN BUDGET in 14.34 s over
   2,100 nodes; no kuzu process alive). 5 of 5 TOs terminal with VALID proofs (checked here); the gate's live census 9 items,
   0 undispositioned; 0 graduated, 0 routed -> next L6 is the COO's. The three in-deliverable findings read and not
   counted (the per-tool carrier is theirs).
4. **Annex v2.1** @450f7ecf2e mirrors spine v2.1; the as-built marker @b1f77d5d4d closes the one water-test item routed
   here; step logs for rounds 1 and 2 in the CTO's schema @a8b752df9f, @c2c2127f31 (one guessed message-id set caught
   and corrected before commit); CTO's compilation read, no dispute.
5. **RAVC on four pre-reboot items** (93185): all discharged on this thread, each by commit (@d413196285, @38f60078c4,
   @f2cbab30a1, the live corpus pass on tonight's commits).

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `ssot_validate.py --self-test` / `rectangle <verify>` | the package validator; rectangle.verify.json | 13 of 13; 0 violations, 888 MEASURED | the mechanical limb |
| own instrument `cert_assess.py` (crosstab / invariants / ineq / probes / cell) | 74 x 12 cells | M1 1 violation, M2-M5 0; 22 counts 0 impossible; 2 cells CONTRADICTED | the coherence assessment |
| `sha256sum` verify vs c4 | identity by content | b81a7e9a... vs d3fb85ac... | never a diff |
| `surprise-row-gate.py --self-test`, `proof-of-spec-check.py --self-test` | the gates at a second seat | 6 of 6; 6 of 6 | + live census |
| own census over org/projects/*.json | dep_stage / fabric | 37 of 353 / 4 off-enum; 13 of 353 laptop | matched the author's cells exactly |
| `git show <vintage>:<file> \| grep -c` | audit sink, comp-surprise tree root, three lanes at 2718cffc45 | 0 / 0 / prd ANY_CTO, decompositions TREE_COO, task-orders TREE_COO | vintage-true; since moved |
| `void_terminal_check.py` | the run dir | CLEAN at DRY; the object-verdict VIOLATION at CERTIFIED (CTO's read) -> reshaped -> 0/0 | the checker's contract lives in its docstring |
| `proof-of-spec-check.py <instance>` x3 | T-1, G-5, T-2 instances | VALID rc 0 each; surprises 2/2, 0, 0 | round 2 read on the record |
| `comp-find --corpus aws opal-gateway` (default) | the CE-g-5 remedy | WITHIN BUDGET 14.34 s, 2,100 nodes | the exercised remedy; earlier 3 of 3 expired |
| `Get-CimInstance Win32_Process` | kuzu processes | none alive | |
| `comp-read <annex> --enumerate '<retired tokens>'` | annex v2.1 body | 2 benign hits | form check |
| `jsonschema.validate` | two STEP_LOG instances | VALID | |

**What worked:** refusing to read the dry rectangle, so the attestation could say so; nominating the plant before
re-reading the narrative that would have named it; re-deriving every action-blocking cell with a different instrument.
**What failed:** the certification's `verdict` as an object (the checker wants a string) -- one-field reshape; a step-log
row drafted with guessed message ids -- caught before commit. **Gap found:** F-2 and F-3 (package steward); the checker's
contract has no schema file.

## MCP traffic

Inbound ~20, all READ-acked by id. Outbound of note: 93135 (certifier ready + pre-seal attestation), 93147-93148 (the
verdict), 93168-93170 (the round-2 stamp), 93186 (the reshape), the RAVC answer to 93185. Nothing to any worker after 93093.

## Surprise channel

NFRA_COMPEFFICACY: 9 rows at HEAD; every item dispositioned by its latest carrier; round 2 appended none; the gate's
live census 0 undispositioned. Notifier denominator 20 files / 197 rows.

## Files Modified

`workflows/atom_decomposition/runs/canonical-fabric-workflow-spec/20260903T0305Z/certification.json` @feb8d97fad, @8b61e1409f ·
`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` @450f7ecf2e (v2.1) · `deliverables/CVO_CANONICAL_LOOP_STEPS_1_10_AS_BUILT_20260901.md`
@b1f77d5d4d · `.../surprise-channel/investigations/INVESTIGATION_v1.md` @88c961297b · `.../ledger/STEP_LOG.3.0.0_SA_CVO.round{1,2}.json`
@a8b752df9f, @c2c2127f31 · this log.

## Blockers

None BLOCKED. Everything below is EVENT-GATED.

## Current State

- origin/CLOUD @800b85c1a2 (ls-remote at this seat 06:0xZ); 33 commits ahead locally across the seats; pushes on Andrew's word.
- NFRA_COMPEFFICACY: round 2 stamped (zero graduation); the COO's fork next (more L6 or the close); ROUND_CLOSE is the
  row owner's flip on the stamp.
- Monitors: inbox bec32h3nh; notifier b6cli05zq. Zero crons. The L8 send guard binds by reading this session (its
  server-side path applies at the next launch).

## Next Steps

- [3.0.0_SA_CVO] round 3's rows if the COO dispatches more L6; otherwise nothing at the close beyond the stamp already given.
- [2.0.0_SA_COO] the fork: the next L6 dispatches, or the completion report if the decomposition is spent.
- [1.0.0_SA_CTO] the grades and the CLOSED flip when the report arrives; the package findings F-2/F-3 to the steward.
- [Andrew] the push window, at his word.
