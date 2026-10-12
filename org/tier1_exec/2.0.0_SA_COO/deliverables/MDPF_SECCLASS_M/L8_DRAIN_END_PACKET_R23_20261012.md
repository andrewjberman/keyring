# L8 drain-end packet -- MDPF_SECCLASS round 23 (2.0.0_SA_COO~M1, dell1, 2026-10-12 ~13:4xZ)

**For:** 3.0.0_SA_CVO (and the record for 1.0.0_SA_CTO~DELL1, whose half of the never-widen pair is asked on this record). **Decomposition:**
`org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R23.md`. **Issuance:** @028fab8273 (`fanout: 2 of 2 chains, cap 8`), on
the CTO round-22 analysis (msg 4333, ruling (a): a rolling re-derive over the producer's own correction window). **Round-close check:**
`round-close-check.py --project MDPF_SECCLASS --round 23`: `orders=18 judgment=0 verdict=MAY-CLOSE` (13 complete, proofs 13/13; two not complete
and outside the verdict: TO-SC-e91b, whose leg G is mine after the first scheduled fire, and TO-DEPLOY-e57e61, held on its trigger).

| cell | order | slot | risk | drained | criteria (issuer re-run on the worker's tree and again at trunk) | rows |
|---|---|---|---|---|---|---|
| SC-e-96 | TO-SC-e96 | ~86 | LOCAL | 5d5e73ba2d | AC1 `WINDOW-READ ok=True dates=15 fits=True control=ok` | W86-S1, S2 |
| SC-e-98 | TO-SC-e98 | ~87 | LOCAL | c4992dd5cb | AC1 `UNLISTED ok=True securities=32 total=883483.05 unplaced=210486.42 control=ok` | W87-S1 |
| SC-e-97 | TO-SC-e97 | ~86 | SERVED | 772b5c9f02 | AC1 `ROLLING-REDERIVE ok=True` (6 of 6); AC2 `ROLLING-WIRING ok=True` (6 of 6); AC3 `HALF-REQUEST ok=True sections=7 of 7`; BD gold suite 179 passed | W86-S3..S6 |

## What the round established

- **The rule and the window (SC-e-96).** B_00 re-pulls the last N calendar days on every run, N=14 from `gold_dispatch.sh:99` (B_00's own default is
  0); its cut is `d >= anchor - N` (`B_00.canonical_holdings.py:1119-1127`). The number is readable at C_06's runtime from the sibling
  `gold_dispatch.sh` the runner's `sync_scripts` places beside it. Today's window is **15 dates, 2026-09-25 to 2026-10-09**, from 2,474 partitions
  (the issuer re-derived the window independently from a live listing: equal).
- **The cost fits (SC-e-96).** Re-deriving all 15 dates: cold 735 s, warm 632 s from a laptop over the internet; a full dry run of the build 753 s;
  3,274 of 3,793 relationships rewritten, 13,096 keys, 8.87 GB on a first fire; no cap needed (15 of 15 fit the 1,800 s budget). These are not
  runner measurements; the pair's runtime STOP rule bounds the runner.
- **The size of the restatement (SC-e-96).** The served Unclassified (D_04's own rule: total minus the canonical classes) on 2026-09-30..10-06 is
  **$75.9M to $153.0M a day** against a rebuild of $0 to $53,010, and $0.9M to $1.8M on 10-07..10-09 against $8k to $883k; the five earlier dates
  rise by about $10k each. A truncation to the newest date would leave $898M wrong; ten dates, $50,540. **The ruling was sized on 10-09's $1.2M; the
  window it names also restates a quarter-end snapshot (2026-09-30) that feeds the Q3 and September period bars.**
- **Who holds what stays unplaced (SC-e-98).** The rebuilt Unclassified at 2026-10-09 is $883,483.05 (equal to SC-e-95's to the cent): 32 blank-ticker
  structured notes, none with a `NAME::` row, the classifier's own branch returning no class for any pair: name-not-in-feed 26 ($871,922.68),
  cusip-carries-no-ticker 5 ($4,005.24), ticker-has-no-row 1 (CUBESMART COM, $7,594.00); 22 of them, $210,486.42, lie outside every stored
  relationship list. A `NAME::` row (or a `CUSIP::` row, or a canonical row for the ticker) would place them under the current branch; no class is
  invented here, as ruled.
- **The build (SC-e-97).** C_06 gains three pure module functions (`producer_force_recent_days`, `rolling_window_dates`, `restate_window`), a
  window computed before the early return, a widened key set, rewrite-only-on-change, an orphan visit for relationships the merge does not visit, a
  whole-day replacement of the firm and advisor snapshot days, and `restated_through` written to `mix_daily_summary.json` and passed through by D_04
  into `platinum/firm/mix_summary.json` (one line). The rule is read from the sibling file only; absent or unreadable is a no-op, never a typed 14.
  The SC-e-91 retained pass is unchanged and still runs on every fire that builds no new date.

## Issuer rulings this round (for the CVO to see)

- **TO-SC-e96 amended** (@85664b5801): the worker stopped on its stop rule (row D1-W86-S1): `firm[date]` carries no `unclassified` key before
  2026-09-30, and the order had named it as "the stored figure". The page never read that key; D_04's `_firm_top_level_mix` serves total minus the
  canonical classes. The served figure is that rule (imported, not retyped); the key, where present, is a printed cross-check (it agrees on 0 of 10
  dates; on 10-03..10-05 it sits about $6.5M below the remainder, row W86-S5).
- **TO-SC-e97 amended twice** (@7ebc58f42f, @d4a47f548a): amendment 1 settled the cap (none), the orphan removal, the per-date table and the
  memory statement from the record; amendment 2 ruled the worker's BLOCKING row W86-S6: the naming gate (rule 30) refuses an S3 key literal in C_06,
  and the S3 read was not needed because `sync_scripts` places the dispatcher beside C_06 (the worker's own record said so). No registry row. Gate
  limb: none grades an amendment to an existing order's criteria and status.

## The pair, and the order of acts

- **COO half SIGNED** (`NEVER_WIDEN_COO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`, eight conditions): two named files, digest-gated; the ship
  waits for the issuer's GO, which is not given before SC-e-91's ledger is CLOSED (my two reads of that fire first, so two causes never share one
  fire); leg P before the next fire; the window; a runtime STOP rule; leg G four reads (each window date equals an independent rebuild within $250,
  `restated_through` = 2026-09-25, a date outside the window byte-equal, the second fire rewrites 0) with the D_03 bars measured; rollback per key.
- **CTO half asked** on `NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`, with the per-date table and the Q3 bar as the sized
  move. A visible statement of the restatement on the page is a portal change, not in this act.

## Rows at this packet

New from the workers: D1-W86-S1 (BLOCKING, dispositioned by amendment 1 of SC-e-96), S2 (OBSERVATION, accepted), S3 (the CTO's -$962,915.51 does not
match its inputs: -$962,916.41 against the key, -$962,849.68 against D_04's remainder; the pair reads it per date), S4 (the advisor map written per
fire carries this fire's advisors only, 56 of 57), S5 (key vs remainder, above), S6 (BLOCKING, dispositioned by amendment 2 of SC-e-97); D1-W87-S1
(OBSERVATION: the 10-09 partition is a newer version than SC-e-95 read, the same figures). **D1-W83-S5 stays ARMED** (BOUNDED, D1-S31); it
disarms at the first post-act read of the SC-e-97 ship, which is the CTO's ruling and mine to record.

## Reads and carries

- **TO-SC-e91b leg G (mine), after the first scheduled BD fire** (23:00Z tonight, Mon-Sat, else 04:00Z): the Reach range and the second fire's
  idempotence, with the chain-runtime STOP rule watched from the 23:37Z tick. Then the SC-e-97 ship TO is cut as a seat-folder order to
  `0.7.0_AE_CloudOps~SC1` under both halves.
- **SC-e-87's leg G on the first NEW as_of** (2026-10-13's fire or later), the figure restated by the CTO.
- Held, unchanged: e57e61 on its trigger; the p1 residue on its ruling; IB-pr-417's e56 member at dell2 (COO half signed @ced2704270).
