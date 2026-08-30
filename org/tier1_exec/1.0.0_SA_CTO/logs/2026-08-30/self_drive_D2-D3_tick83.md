# /self-drive D2 & D3 — tick 83 (2026-08-30 08:25Z) — state: ARMED

Covers tick 83 and the inter-tick acts since the tick-82 log (`8137c539d7`, on origin @`0ae699e57b` — own
is-ancestor read at the 08:22Z CLOSE). Cron `1c261f82` :07/:37 (fired 08:25Z on idle). Paired
`/drive D2 & D3 @ 2.0.0_SA_COO`.

## Scope (register-read, §0)

`D2 & D3` → 2 of 12 live → 10 projects (1 complete). Open TOs **23 → 24** (register) == **24** (`to-check`):
ADVI_49F 1 → 2 (`c02-MAPVINTAGE`, cell C02-g-8, cut @a33243763d). Claims 342 of 342, lag 0. Ledger **19 / 0
unconsumed**. Delivery state 49 of 50 READ at the tick's open; the 1 SENT row read and acked this tick.

## Calls (§1)

**0 ADJUDICABLE. RESERVED: 5** (R1–R5). R2's card is RE-SIZED on the CVO's P2-1 grade: pass 2 of the census
pull does not batch (one SI range per account), so the ask is pass 1 = 5,309/N + pass 2 ≤ 5,309 — ~4.1 h at
N=1, ~2.1 h at N=50 — not "4.1 h vs 5 min" as this seat's tick-82 recap repeated; the optional 2-account
probe measures pass-1 cardinality only; the ask reaches Andrew on DS~C's re-cut graded hash. No pitch.

## Verdicts since the tick-82 log (§3)

**0 on pitched calls.** Grades read: CVO 86554 P2-1 PASS on substance with R1–R3 (R3 a Rule-24 adoption the
gate ruled, below); CVO 86519 row 38 (a06: DISARMED by ownership, not remediated; the convention item
OBSERVATION/INERT; the 08-20 a00 abort owned at DS~N as one line after M-3).

## Driver's own acts (tick 82 → 83)

1. **The a06 HALT — a live production finding, ruled and cut.** C02-g-7's first send aborted at
   `a06_dim_identity_crosswalk.py:49` on an EMPTY allocation map: the SmartX map is header-only every
   Sat/Sun (13 of 13 empties are weekend dates; 33 of 33 weekdays populated), lands ~13:15Z after the 12:45Z
   fire, and a06 reads the NEWEST partition regardless of chain date (`--map-date` exists at :92, never
   passed). DS~N's owner read (86500) found it has ALREADY fired twice in production — Sun 08-23 and Mon
   08-24 aborted at a06 (3 of 12 floor fires) — masked because the 08-29 P14 backfill wrote the missing
   08-21 partitions; AE~L retracted "masked by the hold" (86516). **Gate ruling** (86478, AMENDED at 86490
   on COO's fact that the 534 P14 crosswalks all carry the 08-28 map, so date-matching the five backfill
   dates would be a vintage island one layer down): a06 resolves the NEWEST POPULATED partition
   (header-only skipped), the :49 guard stays for the genuinely-empty case, the crosswalk STAMPS
   `map_date` + `map_carried`, a validator arm refuses a crosswalk without them; "the map at the chain's
   date" QUEUED as a series-wide item (a 534-crosswalk re-derivation). REC to the issuer: do NOT re-hold the
   floor — the guard is the control, an abort writes six upstream dims and nothing downstream, Friday
   08-28 stands for the weekend (NEVER-4); read at 12:50Z from the S3 chain log. COO cut **C02-g-8 /
   TO ADVI_49F.c02-MAPVINTAGE** at DS~N to the amended spec (86527); M-2+M-3 GO now, before ~12:40Z if the
   DS gate allows, else before Monday's fire (the one that leaves Tuesday's trading-day run without a
   D-1). CVO's caveat adopted (86534): the five re-driven crosswalks' STAMPED map_date printed beside the
   neighbours' INFERRED map vintage (P14 → 08-28; a floor fire → its D-1), labelled. C02-g-7 HALTED at
   date 1 PARTIAL (3 new keys + the 3 declared overwrites, prior VersionIds captured); re-drive after the
   served fix; the three overwrite diffs owed now.
2. **TO-S1-AE S1-2 APPLY LEG CLOSED** (86503): 9/1/0 exact; ELEVEN configs, the nine set-identical;
   `suffix=None` read on the primitive; CodeSha256 == the zip; FAMILY env; 0-diff; the eight per-source IAM
   policies intact by name (the design's proof on the applied plane); the plan re-cut fresh after the
   105-minute pause; a third filtered-view disclosure (regex without the colon, 8 of 10) accepted as the
   record. S1e OPEN until the next 04:35Z fire (~20 h); ledger 7b4ebfc470.
3. **The write-set count → the pinned LIST.** 18 → 16 (AE~L 86342) → 15 (DS~N 86415) → 16 by name (DS~N's own
   correction 86450: a two-layer prefix census dropped `reference/`; two errors cancelled on a plausible
   number); the halted run itself wrote `reference/ref_txn_classification` (a05), settling the inclusion
   empirically (86467). The gate read each narrowing as inside the signed shape (no re-sign), wrote
   "corrected to 15" by subtraction across two different lists, and CONCEDED on COO's ruling (86422/86431):
   the denominator is the pinned per-member table (23 prefixes over four layers, 16 IN / 7 OUT with
   reasons), not a count. CVO's strengthening adopted (86452): the OUT-table arm is the VERSION-COUNT delta
   over every prefix (0 on OUT, +5 (+3) on IN), not a five-date presence check.
4. **INF-ONEWRITER manifest: deadlock named and broken** (86545; COO 86544/86577 concur with one
   narrowing): AE's parser reads ONE field (`vendored_modules`; a misspelled key = a silent no-op with rc=0
   → plan (i) asserts denominator == 4 and 0 REFUSES; (iv) gains the misspelled-key arm). DS~V authored the
   manifest @fa0efe270a (4 index-sourced rows at pin 0ae699e57b, verified against the parser's own
   expression with the typo control returning 0) — ACCEPTED (86616-class); AE cuts the re-vendor from
   `git show`, then the (i)–(vi) plan to the gate.
5. **P2-1 graded (CVO 86554); R3 RULED at the gate** (86588): the cell enum is the harness's SIX by name
   (@2762f02f6a :161-166); the two request-side members labelled by emitter; UNAVAILABLE-NOT-RESOLVABLE at
   the ACCOUNT grain (a census-table row, never a cell value); VACUOUS-NO-LINKED-DAYS at the
   differenced-window grain with one sentence separating it from UNAVAILABLE-NO-LINKABLE-DAYS; MECE claimed
   per declared domain. R1/R2 are DS~C's and the issuer's (86584 withdrew the issuer's own carriers). The
   per-feed selector item staffed on the authorship-vs-lane shape; **the gate reads the diff before the
   apply** (default PERFORMANCE only; refuse an unlisted feed).
6. Acks: every row from its Msg-ID line after reading (86494–86615, 22 rows); one crossed-message
   supersession absorbed (86544 vs 86545 → 86577).

## In motion, not mine

DS~N: M-2 + M-3 (the a06 fix, served on the P14 host, read on the running artifact) against the 12:40Z /
Monday clock; the 12:50Z fire read (AE~L); the C02-g-7 re-drive after M-3; AE: the inf-silver-chain
re-vendor → (i)–(vi) plan; DS~C: the P2-1 re-cut on R1–R3 → CVO grade → MSTR carries the ask; DS~C: the
selector patch; the ~12:18Z V-4 check; S1e at the next 04:35Z fire.

## Completion test (§4)

**NOT DONE — 1 of 10.** REACHABLE 9 / UNREACHABLE 1 (`ADVI_49FSRC`, R1 at Andrew).

## Compiler Tools

`directives-check.py --json`, `to-check.py --all`, claims scan (both `prds[]` shapes), `get_delivery_state`
(49/50 READ at open), a timestamp-bounded listing of `inbox/read/`. No comp-find, no comp-state.

state: ARMED · next log at a verdict or tick 89 (floor)
