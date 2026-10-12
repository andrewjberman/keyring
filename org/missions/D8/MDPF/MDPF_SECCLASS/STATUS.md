# MDPF_SECCLASS -- one canonical security classification -- status

Seat `2.0.0_SA_COO~M1` (dell1), successor to `2.0.0_SA_COO~M`. Contract `org/standards/MDPF_SECCLASS_CONTRACT.json`. Lease **FULL**
(`drive-mode.py read`); `/canonical-drive` armed at 60m (Andrew-direct 2026-10-10 ~23:3xZ). As of **2026-10-12 ~10:4xZ** (each table row carries its own measure time).
History is in git and the drive logs (`org/tier1_exec/2.0.0_SA_COO~M1/drive_log_*Z_*.md`).

Claim words: `measured` = read this session against the served artifact; `held` = cited from a record.

## Live thread (FWD-1)

| Surface | State | Claim |
|---|---|---|
| Investor Reporting Holdings | live since 2026-09-30 | held |
| Black Diamond firm Mix (Advisor Intelligence) | six classes + one `Unclassified` line; Unclassified 972,621.40 (0.048 pct) at data_as_of 2026-10-08; the 23 ticker-no-row securities ($966,285) still sit in it (row D1-S26) | measured 02:4xZ |
| Cottonwood firm / clients | four clients' latest point sums to 1; no multi_asset class served; firm_composition gap $0.01 | measured 02:5xZ |
| Cottonwood NAME:: placement (e84) | 1,061 positions ($17.32M) placed, none outside the six; firm unclassified 65.2M vs the 84.3M baseline | measured 02:4xZ |

## Deploy ledgers

All MDPF_SECCLASS ledgers are CLOSED except two (one ordered, one held):

| Ledger | State |
|---|---|
| e91b C_06 retained-unclassified ship (SC1) | SHIPPED 2026-10-12 09:55:03Z (leg D closed; V and P closed; `E91-SHIPPED ok=True` by SC1 and re-read by me: served ETag `2e35d043163cc18b135d7698cf11dc56`, VersionId `zjQmOYVVYTSGOWLFQ0P33vVeWkwp4_eT`, D_04 / D_03 / lib unmoved, watch set 190 of 190 keys, one moved). Leg P: 29,547 keys, 0 without a VersionId, `E91_PREFIRE_VERSIONS_20261012.json`. Ledger `secclass-e91-c06-retained-unclassified-sc1-20261012` HELD on MY leg G: the first scheduled fire (23:00Z tonight, else 04:00Z), two reads (the Reach range at 10-09 and 10-08; the second fire rewrites 0 relationship keys) plus the chain-runtime STOP rule (30 minutes over the 04:00:46Z fire's launch-to-stop of about 2h19m) |
| e87b BD three-file ship (SC1) | CLOSED 2026-10-12 06:4xZ, leg G NOT MET: shipped as signed (06:20Z, `E87-SHIPPED ok=True`, ETags = signed digests) but D_04's served `mix_summary.json` Unclassified is unchanged at the same as-of (2026-10-09, identical firm total): $1,846,332.73 before the ship, after the 00:18Z `bd-gold-trigger` run and after the 04:00:46Z nightly fire, equal to the cent. D_03's `firm_composition.json` did move (92 / $3,325,002.64 -> 66 / $2,760,199.32). Cause (code at HEAD): C_06 is incremental and `reclassify_retained` (:274-311) skips retained `unclassified` holdings; D_04 reads C_06's snapshot (:486). Row D1-S30 |
| e57e61 FWD-10 apply (~S) | HELD on the first scheduled new-security run that plans US stocks |
| e60 D_04 Unclassified line | CLOSED (SC1): AC1 ok, arm 2 closed as non-e60 drift by the CTO (ADDENDUM 1 @4cac828d3c) |
| e79 BD lib ship | CLOSED, leg G NOT MET: the lib is inert on the served path (row D1-S26) |
| e84 COT NAME:: port | CLOSED, leg G PASS |
| remap-b (33 multi_asset rows) | CLOSED, leg G PASS |

## Open findings

- **D1-S26:** the three BD classify sites (D_04, C_06, D_03) called `classify_with_identity` with an empty ticker only, so e79's
  ticker-no-row branch never ran. FIXED IN CODE by round 20's SC-e-87 (23 of 23 placed, $966,285.46 on the live table, CVO's own
  run, ADJUDICATION_v16 D1-C-S2); SHIPPED 06:20Z by `TO-SC-e87b`; leg G NOT MET at D_04 (row D1-S30): the fix reaches D_04 only on a date C_06 builds new.
- **D1-S27:** C_06's firm-daily `total` differs from its class sum by about $128 with a flipping sign; e60's `Unclassified` carries
  it. EXPLAINED by SC-e-88 as 6-decimal share rounding (2026-10-08 reproduces to the cent). Only the owner's acceptability ruling
  is open (remediation owner `1.0.0_SA_CTO~DELL1`).
- **D1-W78-S1** (INERT): the served firm totals for 2026-10-06 and 2026-10-07 do not reproduce from the current partitions
  (partitions rewritten 2026-10-10 23:15Z, after the 05:26Z snapshot); cause not traced.

## Next, in order

1. **Round 23 is at ROUND_CLOSE again (SC-e-97 was reopened ~13:1xZ at dce3041fb8 for the CVO's ARMED row C-S17 and the CTO's SUSPENSION of his half, msgs 4348 and 4349; re-measured and drained @2e8d5c96ef; packet ADDENDUM 1 `L8_DRAIN_END_PACKET_R23_ADDENDUM_1_20261012.md`; C-S17 disarmed by evidence row D1-S32)** (one issuance 028fab8273, 2026-10-12 ~11:5xZ; `round-close-check` r23 `verdict=MAY-CLOSE`, orders=18, 13 complete, proofs 13/13; L8 packet `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R23_20261012.md`; on the CTO's round-22 analysis, msg 4333; `dep_stage` EXECUTING; fanout 2 of 2 chains, cap 8). Round 22 closed and graded (CVO slug msg 4332, `ADJUDICATION_v20` @d24cc0d6ad; CTO analysis `CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_22_20261012.md`). **The CTO's ruling (a): a ROLLING re-derive over the window the producer itself corrects** (B_00 `--force-recent-days`, the number read from its rule at build time, dates older than the window stay as built, `restated_through` on the served object, the dollars no classifier places stay Unclassified and are listed by security, its own never-widen pair; D1-W83-S5 disarms at the ship's first post-act read).
   | cell | what | risk | slot | state |
   |---|---|---|---|---|
   | `SC-e-96` | READ: where B_00's window number lives and whether C_06 can read it at build time, the dates inside it, the cost of re-deriving all of it against the 30-minute budget, per date served vs rebuilt Unclassified and the orphan counts, the gap if truncated | LOCAL, direct act | ~86 `worker` | DRAINED @5d5e73ba2d, complete (amended 85664b5801: served = D_04's rule); AC1 `WINDOW-READ ok=True dates=15 fits=True control=ok`. Rule N=14 from `gold_dispatch.sh:99`, readable at runtime (`sync_scripts` places it beside C_06); window 2026-09-25..10-09 (15 dates); cold 735 s / warm 632 s from this seat (fits 1,800 s, largest N 15, no cap); 3,274 of 3,793 relationships differ, 13,096 keys, 8.87 GB; served Unclassified 09-30..10-06 $75.9M-$153.0M vs rebuilt $0-$53k (restated into other classes); gap 0 at 15, $50,540 at 10 |
   | `SC-e-97` | BUILD: C_06 re-derives the producer's window on every fire (three pure functions, `build()` wiring, `restated_through` through D_04), tests, the never-widen half request | SERVED | ~86 (after SC-e-96) | DRAINED AGAIN @2e8d5c96ef, complete (amendment 3 @dce3041fb8 + clause @a57c9d1c94): radius amended from the build's own dry run, the issuer's recompute from its raw capture reconciles every date to $0.00. **Firm total moves on 14 of 15 dates (up 10: $32M-$247M on 09-25..10-02 and $5k-$49k on 10-03/04; down 4: $1.3M-$1.9M on 10-05..08; holds 10-09); AUA (client_performance) holds and the rebuilt total equals it on all 15**; 876 added / 151 dropped rows, 0 new to the store; advisors 56 and 56 (no drop), 502 of 840 advisor-days move, about $55M of attribution between two advisors (current rel_architect lookup); the bars' totals hold, classes move (Q3/Sept Unclassified -$82.39M, structured +$87.55M). COO half RE-SIGNED (addendum 1, conditions 9-12); CTO half SUSPENDED, re-signs or refuses first; the ship waits on both and on SC-e-91's leg G |
   | `SC-e-98` | READ: the rebuilt 2026-10-09 Unclassified by security with a reason, the unplaced dollars marked | LOCAL, direct act | ~87 `worker` | DRAINED @c4992dd5cb, complete; AC1 `UNLISTED ok=True securities=32 total=883483.05 unplaced=210486.42` (worker, issuer on its tree, issuer at trunk). 32 blank-ticker structured notes, no class came back for any pair: name-not-in-feed 26 ($871,922.68), cusip-carries-no-ticker 5 ($4,005.24), ticker-has-no-row 1 ($7,594.00); 22 of them ($210,486.42) outside every stored list |
   - **The ship of SC-e-97** is a later pair-gated act by a CloudOps lane (both halves SIGNED: COO `NEVER_WIDEN_COO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`, CTO `NEVER_WIDEN_CTO_HALF_SECCLASS_C06_ROLLING_REDERIVE_20261012.md`; leg P, window, STOP rule; CTO conditions: post-act equality per date INCLUDING the 10-03..05 key-vs-remainder gap reading 0, direction printed per date (a date outside its prediction is STOP), the Q3/Q4/September/October bars printed before and after by class, the ship after SC-e-91's leg G, the page sentence a PROD portal change on Andrew's word that the data correction does not wait for), cut as a seat-folder order to `0.7.0_AE_CloudOps~SC1` only after SC-e-91's ledger is CLOSED (so two causes never share a fire). **The move is large:** served Unclassified on 09-30..10-06 $75.9M-$153.0M against a rebuild of $0-$53k (Q3 and September bars end 09-30).
   - **Carried:** SC-e-91's ship `TO-SC-e91b` (SHIPPED 09:55Z; my two-read leg G follows the first post-ship fire); SC-e-87's leg G on the first NEW as_of; `TO-SC-e90` is done (portal 64d8c6de38 on DEV); e57e61 HELD.
   - **Open question, recorded not sent:** the CTO says the restated history "must be stated on the page"; the served field is in the list, a visible sentence on a client-facing page is a portal change that waits on Andrew at PROD. One question to the CTO with the build's record.
2. **e57e61:** release when a scheduled new-security run plans US stocks.
3. **p1 residue** (11 keys outside FWD-15's plan): waits on a ruling.
4. **IB-pr-417:** the COO half on the e56 member is SIGNED (@ced2704270, due Mon 2026-10-12 13:00Z at dell2); push of that commit
   is the box-sync's.
