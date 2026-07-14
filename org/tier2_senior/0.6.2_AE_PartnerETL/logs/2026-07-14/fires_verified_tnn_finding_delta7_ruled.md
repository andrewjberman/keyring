# 0.6.2_AE_PartnerETL -- both evening fires verified (S2 15/15 TIE), the tnn hole-seam finding -> DELTA-7 ruled + contract-closed same hour; ratchet 74% on 0824

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Date:** 2026-07-14 | **Window:** ~21:4xZ -> ~22:2xZ | **Serial:** 0.6.2_AE_PartnerETL

## Summary

**The fires:** 0833 21:45Z = enumerated 254 / downloaded 1 / ok=true; 0824 22:15Z = enumerated 220 /
downloaded 0 / skipped 220 / ok=true (the S6 healthy-skip branch EXACTLY as priced). The one 0833
download was a late-posted tnn 20260713 straggler -- which exercised a seam the expectation report did
NOT price: **the event path hard-fails NAMED-HOLE types** (feed_from_key's unrecognised-type raise; tnn
is deliberately outside RAW_TYPES) -> action=failed -> 3 retry manifests (214602Z/214714Z/214916Z, all
ok=false, nothing landed) -> DLQ. Loud + safe, but tcf lands DAILY -> recurring morning noise both lanes.

**Surfaced -> ruled -> contract-closed inside 25 minutes:** finding to CTO/DS 215259Z with the
recommendation (hole-class events -> action='skipped-hole', manifest-visible, no raise/retry/DLQ);
CTO APPROVED 215400Z as **DELTA-7** (renumbered: delta-6 = the commissioned streaming-parse fix) with
the design guard -- the branch derives from conversion_manifest.NAMED_HOLES (ONE vocabulary), skipped-hole
structurally cannot match outside it, unknown-type refusal stays byte-identical WITH a mutant, hole->
converted promotion only via the contract path; timing = tomorrow, standard path. DS landed contract
**v1.2.4 @ de54d79a3** same hour (all four guards written into the cell-4 text). Code side = my queue
head tomorrow after the box upload.

**FIRST LIVE S2-TABLE VERIFICATION** (parquet-footer metadata on the ratchet's landed 0824 silver):
**15/15 landed pinned partitions TIE EXACTLY, zero mismatches** (acc 7,073 / rps 92,103 + s2 7,074 /
trn 890 / sec 2,056 / rld 453 / rlu 287,566 / rlw 250,201 / rly 234,639 / rtu 114,209 / rty 77,675 /
4 dims parity; uln/ult 07-13 not yet reached). **Both delta-5 laws exercised IN PRODUCTION:** the
2025-01-09 SHELL landed 0 rows / 86 cols; pre-boundary rlu 2025-03-07 landed 226,525 rows with
schwab_order_id null_count == 226,525 (the landed artifact's own column statistics). ZERO rl* refusals
all day. **Event-trigger confirmation leg of Andrew's condition: CONFIRMED** (~10s landing-to-manifest,
3x consistent). Consolidated fire report to CTO 221805Z; board note to COO 221811Z.

**Ratchet:** walls and all -- OOM wall at invoke #3 (pre-sizing), sizing proposal measured/ruled/applied
(10240 @ v0.13.0), relaunch, now 5,561/7,468 on 0824 (~74%); rate profile matched the belt structure
(heavy periodics ~15-27/invoke, rps+dims burst +496, uln/ult heavies ~100-260, light tail +1,366).
0833 drains overnight; per-lane RAVC on completing manifests.

## Compiler Tools

| Tool | Purpose | Result |
|---|---|---|
| aws s3 cp (manifest reads) | both fire run-manifests + 3 event manifests | grounded the finding |
| aws logs filter-log-events | the failing key + error class (CW tracebacks) | tnn + feed_from_key raise, 3x |
| pyarrow.parquet footer reads (S3 filesystem, metadata-only) | S2 verification on landed silver + shell + null-count | 15/15 TIE; 0-row shell; 226,525/226,525 nulls |
| ratchet driver (Monitor) | the drain | 5,561/7,468 and running |

**What worked:** the fire watch caught the seam within seconds; footer-only metadata reads made a
17-partition verification cost ~nothing; the manifest's own column statistics proved the null-fill law
without downloading a row. **What failed/caught:** my expectation report priced the pipe types and the
sweep but NOT hole-type EVENT landings -- the gap class: I enumerated conversion outcomes per type but
not trigger-path x type; banked for future expectation reports. **Gap found:** delta-7 (ruled).

## Blockers

None. Overnight: ratchet ticks (Monitor-driven). Tomorrow queue: box-script upload + guarded first fire
-> V2-2 RAVC-4; delta-7 authoring -> DS diff -> CTO review -> swap; per-lane parity RAVCs as they land.
