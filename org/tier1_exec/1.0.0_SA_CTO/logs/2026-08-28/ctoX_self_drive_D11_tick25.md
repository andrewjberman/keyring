# /self-drive D11 -- tick 25 (2026-08-28 10:24Z-10:3xZ) -- 1.0.0_SA_CTO~X

**state: ARMED** · cadence 30m · cron `e17cfef7` (:11/:41) · paired_with `/drive D11 @ 2.0.0_SA_COO~X` (+15m) ·
carrier `org/XXX.md` Step 1b-F @f6b4fb0c56 · ticks covered: **25** (tick 24 logged @81d761d403; this log is
delta-driven, not floor-driven).

## SCOPE (Step 0, read from the register at 10:24:37Z)

`directives-check.py --json`: D11 "Substrate/Tooling Enhancements", device LAPTOP (this device), **2 members**
[NFRA_SUBSTRATECARDING active/EXECUTING, NFRA_C3MATERIALIZE active/EXECUTING], open TOs 4, flags [], denominator
1 of 12 live. Claims scan: 342 project JSONs scanned (both `prds[]` shapes handled), 1 claim
(NFRA_SUBSTRATECARDING, already a member) -> no lag. Device guard: LAPTOP == LAPTOP.

## OPEN CALLS IN SCOPE (Step 1-2)

**0 adjudicable · 0 RESERVED** -> no pitch (the zero-line; the all-reserved tell cannot fire on an empty
queue). Standing hold at Andrew, not an open call: R1 (L2 release) -- unchanged.

## VERDICTS SINCE LAST TICK (Step 3)

**0 adjudication verdicts.** CVO~X wrote three times this window (R4-DT-5 confirmation 102010Z; R4-DT-6 ruling ask
102650Z and its acceptance 102943Z; both-layers verification 102922Z) -- finding confirmations and a disposition
acceptance on a question CVO~X itself raised, not verdicts on pitched calls. Ledger unchanged: 15 rows, all consumed.

## ACTS TAKEN THIS TICK (the delta since tick 24)

| when | what | hash / id |
|---|---|---|
| 10:14Z-10:16Z | WP-3 decomp c0 **CERTIFIED PASS**, attempt 2 (CVO~X; planted spec_citation found pre-reveal; 168 cells UNMEASURED; consumable `rectangle.final.certified.json` sha256 2776f110...) -- recorded, ack 77632 | @7cbefad614 (CVO~X) |
| 10:19Z | DT~X wave-1 **AC6-AC8 evidenced** (runner with three non-collapsible exit codes; 0 of 190 -> exit 3 NOT_EXERCISABLE by design; AC7 unreachable by construction; AC8 on the member-list intersection 14/6/0) -- ack 77636 | 77636 |
| 10:2xZ | **R4-DT-5 filed** DISCLOSED-NO-CHANGE: the TO's AC8 extension globs cannot show "no +27 member changed" -- git pathspec `*` crosses `/`; no glob reaches `run_gates.sh`. Reproduced here with a third instrument (`git ls-files 'org/standards/isck/*.py'` = 4 files under `ledger/`); members 14 read by importing `bundle_identity` | @2935876c06 (77 rows); msg 77641/77642 |
| 10:24Z | remedy had already landed at the issuer @e6344dbe6c (+ face drift @f079bebb47); both checked to exist and touch the TO; row's `fix_commit` resolved | @1180650690 |
| 10:25Z | **R4-DT-6 BLOCKING** (77646): TO cites DECOMP.md in parentheses; `.tools/proof-of-spec-check.py:317` `\S+DECOMP\.md` captures the paren (read at source; 5 of 5 commits on the file are 3.0.0_SA_CVO's) -> ARMED hazard disarmed by naming two owners in one body | msg 77650/77651/77652 |
| 10:26Z-10:29Z | layer 1 fixed @17678336ed exposed **layer 2**: DECOMP.md held 6 of the rectangle's 168 cell ids -> 50 violations, unfixable from the instance. Issuer fixed @3ff89ea821 (CELL INDEX generated from the certified rectangle; rectangle bytes untouched; `<owned_cells>` delimiter). CVO~X independent re-run: 168/168 diff 0/0, 53/53, VALID rc0, **HOLD LIFTED** | @17678336ed, @3ff89ea821 (COO~X) |
| 10:29Z | **CTO ruling REC on CVO~X's ask**: certification ADDENDUM, not re-cert (the certified subject is byte-identical); CONDITION = a regeneration gate beside the generator (rebuild index from rectangle, fail on any set difference, dropped-id mutant must FAIL) -- a derived copy beside its source is a typed-beside-derived carrier. **Accepted by CVO~X 102943Z** as the addendum's condition; gate mechanism being checked at @3ff89ea821, else routed to COO~X before signing | msg 77656/77657 |
| 10:3xZ | **R4-DT-6 filed FIXED** (both layers; follow-ons: addendum + gate at CVO~X/COO~X; checker :317 + `<decomp_doc>` at CVO base) | @23956dca9a (78 rows) |
| 10:31Z | **ADDENDUM CONDITION MET** at the issuer: `check_cell_index.py` beside the run (derives the id set from the certified rectangle; `--check` exact equality both directions, ABSENT = FAIL; `--mutants` drop / extra / dup-swap **3 of 3 FIRED**; clean 168/168 missing 0 extra 0 MATCH; index REGENERATED through it; rectangle sha unchanged; DT~X instance still VALID). Ready for CVO~X's addendum run -- ack 77659 | @af69d18511 (COO~X; 2 files, +155/-1) |

Fix (b) on the checker stays in the checker author's lane and is not a gate on the wave (COO~X 77655 and CVO~X
102922Z agree). DT~X may land the one wave-1 commit + report (CVO~X's lift). Wave 2 (ledger code) cuts at COO~X on
wave 1's measured completion, from the same certified cells.

## SCOPE STATE (denominators printed)

| project | status | dep_stage | open TOs | note |
|---|---|---|---|---|
| NFRA_SUBSTRATECARDING | active | EXECUTING | -- | round 4 CLOSED @abcb491373; +27 FROZEN @7a44b65f50; register **78 rows** (60 round 3, 18 round 4) |
| NFRA_C3MATERIALIZE | active | EXECUTING | 4 on D11 (register count) | decomp c0 CERTIFIED @7cbefad614; TO-WP3-1-DTX: AC1-AC8 evidenced, instance VALID rc0, commit pending at DT~X |

## COMPLETION TEST (Step 4)

**NOT DONE -- 0 of 2 projects `complete`**; both REACHABLE (active seats, live TOs, no scope question open). D11 not in
`DIRECTIVES_RETIRED.yaml`.

## RESERVED AT ANDREW

R1 (L2 release hold) -- standing; production population + L3 cells HELD. No new card this tick.

## PUSH STATE

LOCAL. origin/CLOUD @540503df0a (09:58:49Z window); `rev-list --count 540503df0a..HEAD` = **22** before this log
(8 CTO~X, 12 COO~X, 2 CVO~X) -- the next MSTR window's tail. Integrator-only branch.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `directives-check.py --json` | D11 LAPTOP, 2 members, 4 open TOs, 1 of 12 live | scope |
| claims scan (`prds[].path`, both shapes) | 342 scanned, 1 claim, 0 lag | denominator printed |
| `git ls-files 'org/standards/isck/*.py'` | 4 files under `ledger/` from a top-level pathspec | third instrument on R4-DT-5's crossing limb |
| `import bundle_identity` (GATES 8 + VOCAB 3 + DOCTRINE/SCHEMA/VALIDATOR) | 14 members incl. `run_gates.sh` | denominator derived, not copied |
| `proof-of-spec-check.py:317` read at HEAD | `re.search(r"(\S+DECOMP\.md)", blob)` | R4-DT-6 grain |
| `git log --format=%an -- .tools/proof-of-spec-check.py` | 5 of 5 = 3.0.0_SA_CVO | owner for fix (b) |
| `git show --stat` on e6344dbe6c / f079bebb47 / 17678336ed / 3ff89ea821 | each exists, each touches the named artifact | before any citation |
| `render_round2_register.py --round 3 --check` | OK 77 -> 78 rows | three commits |
| `ack_messages` | 77632, 77636, 77643, 77646, 77649, 77655 | READ clock; CVO~X's four notes were file-transport, no broker id |
