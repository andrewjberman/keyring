# COT_RUNNER_REFACTOR.P1 — Groups A/B/C (scoped) + parquet writer-format — build session
**agent:** 0.4.0_DS_ClientPlatform~B · **date:** 2026-08-11 ~1450Z–1640Z · **archetype:** IMPLEMENT

## What happened
Fresh lane boot (Andrew-instantiated per the ~1450Z GO @162965ed1c). /watcher armed (Monitor
bb42cpx5l), registered, XXX.md protocol run. COO's staged dispatch read; TO
COT_RUNNER_REFACTOR.P1.scripts-groups-a-c-scoped executed end to end: the full P1-SCRIPTS scope
LANDED AND VALIDATED in one session — 15 scripts, 4 proof-of-spec instances (44 acceptance rows
total, all VALID rc=0 unpiped), TO id-sets appended, every group reported to COO same-window.

## Commits (all under this lane's author line, safe-commit, gate-passed)
- @b9e6b154e4 — harness + Group A (runner_common + a00–a05; 7 files, 1,274 insertions)
- @f19b796e0c — Group A instance + TO amendment (13 ids)
- @05d35274de — Group B (b00–b03)
- @f0fad0116e — Group B instance + TO amendment (13 ids)
- @3fbbf91e19 — Group C (c00–c03)
- (this commit) — Group C + writer-format instances + TO amendments + this log

## The load-bearing results
1. **The relationship-grain collapse is VENDOR-CORROBORATED, not merely ruled.** The collapse
   removes EXACTLY $205,070.77 (the DC1-measured double-count, to the cent, account z0927448821,
   stable on every value-carrying day probed), and BD's own account-level MV
   (fact_allocations `Account Market Value`) ties the COLLAPSED sum on 888/925 accounts at 1bp
   with ZERO unexplained variances — on the dual specimen it equals the collapsed value exactly
   while the naive sum would read $410,141.54.
2. **The COT spec's OPEN cell #2 is partially closed by measurement:** an account-level BD total
   EXISTS at rest (roster surface, 889/925, same-vintage). Consumed as B_03's tie only; the B_00
   swap stays RECON-5a's ruled event.
3. **F-4 segregation is LARGE at cot:** all 1,914 journals are one-sided (never pair, never
   vendor-marked) → $121.2M segregated beside the $404.9M headline NNA. Ruling eye needed at
   RECON-5a (genuinely-external one-leg vs out-of-export counterparts).
4. **Vendor-vs-GIPS divergence quantified for ruling:** BD's External Flow enum marks all 618
   Management Fee rows (+86 Expense, +57 Tax Withholding, +9 Sale) external-Withdrawal and 202
   Buy rows Contribution; GIPS excludes fees from external flow. Vendor-alignment delta carried
   as data (−$1.11M / 704 rows). Corroboration on authored-externals: 100.00% (14,208/14,208).
5. **UNRESOLVED = Corporate Action family + Return of Capital** (65 rows, 0.309% $) — the INF
   five-code-amendment class; characterized as ruling evidence, never guessed.
6. **Found-and-fixed in-wave (declared in the C instance):** the zero-BMV refusal initially
   leaked NaN into COMPUTED-stamped rows on 2 TRUE-ZERO accounts (4 account-days) — the fixture
   proved the function, the population exposed the status path. Post-fix 0 NaN-on-COMPUTED;
   UNCOMPUTABLE discriminates 72 null-status + 4 ZERO-BMV.
7. **fact_allocations true grain = Account × REP-ASSIGNMENT** (rep_code the only varying column,
   641 accounts, fee-split class) — per-membership rep sets carried on dim_relationship;
   ADVI/D-lane projection declared.

## Transposability (two frames per CTO ruling, per group)
A: verbatim ~62% / diverged 46% (9 calls) · B: ~78% / 31% (5 calls) · C: ~84% / 29% (6 calls).
Curve 62→78→84 vs ~A's 64→79→86 — the front-loading prediction held within 2 points per step.

## Declared waits (per TO, blockers named)
A_06 (RECON-5a first deliverable) · C_04/C_05 (the P2 probe). D is HOLD-FOR-RULING — the ruling
event fires with this session's C-completion report (deciders Andrew + CTO + COO; inputs: base's
B-4 emitter outcome + ~A's D outcome + this C-completion).

## Discipline notes
No cot S3 pushes at any point (P1 scripts-only; base's 15:06Z window respected and now spent).
No gates manufactured; findings banked same-turn to COO, one line each, work never held.
LANES COMMIT, INTEGRATORS PUSH — nothing pushed from this lane.

## Compiler Tools
| Tool | Invocation | Result |
|---|---|---|
| comp-to | COT_RUNNER_REFACTOR.P1.scripts-groups-a-c-scoped | session TO context set (race-free per-session file) |
| comp-find | --name COT_ABCD* / --name ADVREVIEW* / --name PROOF_OF_SPEC.schema.json | located spec, form doc, schema (1 hit each, denominators printed) |
| comp-find | collapse_relationship_grain | 2 DEF hits: the canonical build_dim_model_portfolio.py:149 + the Lambda vendoring precedent — vendored per that precedent (Build Ladder rung 2) |
| comp-which | "how do I grep the repo" (A.3 exercise) | forwarder RAN (PATH 96/97 + exercise PASS) |
| comp-validate | deferred | runners_cot unregistered — NO_CONFIG = UNVALIDATED, declared, never signaled safe; consolidated at CTO as ONE act (COO 160305Z) |
| comp-pipescript | deferred | same act; no deploy leg exists in P1 |

Gap noted for the record: the proof-of-spec-check id set is ONE comma-joined positional arg —
13 separate argv ids rc=2s exactly like the flagged form. Fold into the protocol template note.
