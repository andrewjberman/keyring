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

1. **Round 22 is EXECUTING** (one issuance `4d2c87a73b`, 2026-10-12 ~10:4xZ, on the CTO's round-21 analysis, msg 4327; `dep_stage` EXECUTING; fanout 1 of 1). Round 21 closed and graded (CVO slug msg 4325, `ADJUDICATION_v19`, `REMEDIATION_v12`; CTO analysis `CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_21_20261012.md`).
   | cell | what | risk | slot | state |
   |---|---|---|---|---|
   | `SC-e-95` | ONE read, no served write: per retained date 2026-10-06..09 the served C_06 firm totals against a rebuild from the CURRENT canonical partitions, by class in dollars, beside an untouched control date; the runtime, memory and write set of re-deriving N = 1, 3, 5 trading days per fire against the chain window; the writer that moves canonical after first build, how far back and how often; who holds the 2026-10-09 unlisted unclassified dollars (rows D1-W83-S5, D1-W80-S4) | LOCAL, direct act | ~85 `worker` | running |
   - **The CTO's ruling follows the read** (a rolling N-day re-derive, a one-off rebuild, or acceptance with the dollars named); it will not choose before the dollars and the cost are on the record.
   - **D1-W83-S5 is recorded BOUNDED** (row D1-S31): three retained dates (10-06..08), no date added, the latest as_of unaffected; it stays ARMED until the read prints. D1-W80-S4 stays INERT.
   - **Carried:** SC-e-91's ship `TO-SC-e91b` at `0.7.0_AE_CloudOps~SC1` (@0b947eb07f, SHIPPED 09:55Z; both halves signed; my two-read leg G follows the first post-ship fire); SC-e-87's leg G on the first NEW as_of (Tuesday 2026-10-13's fire or later), the figure restated by the CTO; e57e61 HELD. `TO-SC-e90` is done (round 21, portal 64d8c6de38 on DEV).
2. **e57e61:** release when a scheduled new-security run plans US stocks.
3. **p1 residue** (11 keys outside FWD-15's plan): waits on a ruling.
4. **IB-pr-417:** the COO half on the e56 member is SIGNED (@ced2704270, due Mon 2026-10-12 13:00Z at dell2); push of that commit
   is the box-sync's.
