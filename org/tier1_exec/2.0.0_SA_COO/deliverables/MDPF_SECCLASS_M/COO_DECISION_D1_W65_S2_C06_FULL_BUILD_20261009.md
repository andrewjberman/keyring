# COO decision -- row MDPF_SECCLASS-D1-W65-S2: no C_06 FULL build; the 15-date mix shortfall is accepted on the record

**Decider:** `2.0.0_SA_COO~M1`, 2026-10-09 ~08:5xZ. **Asked by:** `1.0.0_SA_CTO~DELL1`, rounds 13-15 analysis
(`CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUNDS_13_15_20261009.md` section 3: "the COO's decision, recorded").

## The row

SC-e-75's retained-entry reclass heals every holding the BD envelope shows. On 15 of the 105 healed dates, the date's mix stays below 1.0,
by at most 0.047569. The envelope holds only the top 10 holdings per date, so a `multi_asset` position outside the top 10 was never in
that date's mix. Only a C_06 FULL build, which reclassifies every date from the canonical holdings, closes that gap.

## Decision: ACCEPT on the record. No FULL build is run.

1. **A FULL build widens past every signed radius.** It rewrites every BD envelope, client timeseries and (through D_04) every served
   concentration key, not 15 dates. The e75 CTO half ruled it outside its pair (condition 4 of the e67 half states the same for COT). It
   would need its own never-widen pair for a correction worth at most 4.76 pct of a client's mix on 15 historical dates.
2. **The served present is right.** Every date C_06 rebuilds recomputes from the canonical holdings. The 2026-10-09 04:00Z fire served 0
   `multi_asset` over 3,354 concentration keys, and firm unclassified reads 0.05 pct.
3. **The gap is bounded and named.** It sits only on the 15 dates of row D1-W65-S2 and the half request's 'Known limit', and it shrinks as
   those dates age out of any windowed view.

**What would reopen this:** a reader that shows a historical per-date mix to a client and grades it against 1.0, or an Andrew word asking
for a full rebuild. Either one routes a FULL build through its own pair. Neither exists today.
