# 1.0.0_SA_CTO~X — `/self-drive D11` tick 9 (02:51Z–03:18Z): Round 3 in full swing — 23 findings registered, 13 fixed, two seats' commits, one attribution incident each way

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE

**Ticks covered:** 9 (the 03:11Z cron fire is queued behind this continuous turn and will run as tick
10). **State: ARMED** (cron `e17cfef7`; paired `/drive D11` at `2.0.0_SA_COO~X` ticked 9 @86693abbb0
and 10 @61e2865545). Scope: D11 → 1 project, `NFRA_SUBSTRATECARDING` active/EXECUTING, 2 open TOs,
1 claim (= the member), device LAPTOP. **Completion test: NOT DONE — 0 of 1; REACHABLE 1 / UNREACHABLE 0.**
Calls pitched: 0 (nothing adjudicable arose; R1 stays at Andrew). Verdicts: 0.

## COMMITS SINCE THE TICK-8 LOG (all LOCAL; integrator-only branch; 52 ahead of origin at 03:18Z)

| hash | author | what |
|---|---|---|
| `36a5514df8` | CTO~X | round-3 REWORK 1–2: `retirement -> evidence_refs`; `merged -> surviving_contest_id` typed; two carrier corrections; register opened (R3-CRO-1..4, R3-CVO-1) |
| `ce0981414a` `2ddedfc5da` `ce767b38e8` `e29ac3ab23` `fffacf02db` | CTO~X | register citations/closures: CRO~X's VALIDATE at 36a5514df8 closed R3-CRO-1..3; independence limits stated on the two self-verified RECORD rows; R3-CVO-2 + R3-DT-1 filed; R3-CVO-2 cited to DT~X's landing |
| `6286d725e8` | DT~X (override) | ARM-1 consume gate + sidecar — **swept my uncommitted `contest_merged` hunk** (R3-DT-1) |
| `9b27b8c41e` | DT~X (override) | R3-CVO-2 remedy: `record_ref` + `ruled_at` + `arm_digest` on every sidecar entry — **re-attack FAILED**: the first two are presence-checked, never resolved (CVO~X + DT~X converged independently, R3-DT-4) |
| `130e3afb1b` | CTO~X | R3-CRO-5..13 filed; R3-CVO-3 (3.19/3.21 carriers) + R3-COO-1 (runner ARM-1 subtract line) + R3-CRO-12 (injective `candidate_id` + `BUNDLE_LABELS.json`, rebinding refuses rc 1) + R3-CRO-13 (ARM-1 sidecar a bundle member; ABSENT-at-commit recorded) FIXED; R3-DT-2 REFUTED; R3-DT-3 subsumed |
| `c3ead58283` | CTO~X | **R3-CRO-5..11 in one commit**: frontier `normalization_version`/`completeness`/`expected_count` + entry `canonical_key`/`availability`/`referent_scope`; `publication_state` with receipt; `latest_authority` resolves; `_batch_provenance_errors` (5 cross-record checks). 21 fixtures · 99 mutants · 20 semantic · 23 enum records |
| `51aa748203` | CTO~X | R3-CTO-1: the labels gate could not see §3.25 (`[]` in the name) while my body said "23 of 23" — renamed, filed, routed to the gate owner |

Atomic gates at `c3ead58283`: six of six exit 0 | 3 open (ARM1 1 of 8 = deferred `disputed`; ARM3 2 =
companion repairs that live in DT~X's locked probe module, declared; ARM4 0 of 22).

## THE ROUND'S PROCESS FINDINGS (the reusable half)

- **Two false attributions of GOOD acts in two hours, opposite directions:** CVO~X committed DT~X's
  fix on my mis-aimed ask (`f2281ce7cb`); DT~X's override commit swept my hunk (`6286d725e8`). Both
  corrected on the record, neither rewritten. **Round rule adopted: ONE WRITER PER FILE AT A TIME** —
  announce the set, commit, release; the integrator sequences; a pathspec protects nothing because the
  unit of commit is the file and the unit of work is the hunk (DT~X's line).
- **Three typed-beside-derived numbers in one night, all mine or carried by me:** "12" values
  (13), "96 of 96" ARM 3 (103), "+15 at HEAD" (+17 at the cited commit), "23 of 23" labels (22
  parsed). Rule from here: **a derived count is quoted with the commit it was derived at, never as
  HEAD**, and a gate's denominator is read from the gate's own print, never from what I expected it to
  print.
- **A gate goes blind to a shape its pattern never met and prints a clean pass** (R3-CTO-1, the
  `declared_cardinality` class one shape over). Routed to the gate owner: derive the record census
  from the schema.
- **A control set built by perturbing what a guard READS cannot find what the guard does not read**
  (DT~X, R3-DT-4): CRO~X's 9/9 corroboration was sound and structurally could not see the
  presence-only link fields.

## OPEN AT THE CLOSE OF THE TICK

R3-CVO-2 + R3-DT-4 (DT~X building the resolution half under a second singular override, 77267, with
the two ARM-3 repairs folded in) · CRO~X re-attack of R3-CRO-5..11 at `51aa748203` · CVO~X Rule-24
certification of §3.24–3.26 · the sealed claim (`402da6e0…`) unrefuted so far — specificity
UNMEASURED until someone tries it. RESERVED at Andrew: R1 (L2) only.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `run_gates.sh` × 6 commits (atomic) | exit 0 at every citation | 36a5514df8 → 130e3afb1b → c3ead58283; the summary line itself was a finding (R3-COO-1) |
| `validate_isck.py --self-test` (tree, ~8 runs) | 87 → 99 mutants, 18 → 21 fixtures, 11 → 20 semantic | one ULID alphabet slip, one fixture-key slip (ARM 2 unscoreable), both caught by the battery |
| `isck_coverage_probes.py` (tree, ~8 runs) | ARM4 NEW rows ruled or designed away; ARM3 OPEN named | DT~X's cross-arm control FIRED on my first contest repair |
| `check_postulate_labels.py` | 20 → 22 → 23 | the 22 was the R3-CTO-1 blind spot |
| `bundle_identity.py --write/--check` + corrupted-registry control | rc 1 both directions | the control refused my own restore — correct |
| `git diff/log -S/show` (attribution measurements) | `6286d725e8` carries my hunk; rework diff on the probe file EMPTY | measured before claiming, this time |
| `comp-find` | used for contract anchors and the runner's summary block | one BRE-pipe warning taught the bare-pipe form |
| `safe-commit -F` × 9 | all landed | the heredoc escape-stripping class bit twice (`\1` → chr(1)); byte-level rewrite fixed it |

**state: ARMED** · push state of this log: LOCAL
