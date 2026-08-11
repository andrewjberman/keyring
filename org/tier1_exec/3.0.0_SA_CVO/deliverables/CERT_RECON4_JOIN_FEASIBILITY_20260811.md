# RULE-14e CERTIFICATION -- CRO RECON-4 (GOAL-3 JOIN FEASIBILITY)

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0552-0600Z** · **archetype:** VALIDATE
**Subject:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/RECON4_GOAL3_JOIN_FEASIBILITY_20260811.md`
@be316d868c · run `workflows/atom_decomposition/runs/advi-model-holdings-account-join/20260811T0530Z/`
@512d7353ed. **Method per @3c8418e34b:** load-bearing cells independently re-derived from the cited
artifacts themselves (downloaded, recomputed) -- not the artifact's citations. Live reads
2026-08-11T05:53-05:59Z. Privacy discipline mirrored: counts, formats, rates only -- no account
values in this record or any output. No vendor egress used (all probes Opal-owned; the @9e1fc54623
session lift was not needed).

---

## VERDICT: **CERTIFIED** -- all three load-bearing cells confirmed by independent recomputation.
## One item REFUSED AS WRITTEN (the run record's own census line). Two grain corrections noted.

## GROUNDING TABLE

| Cell | Rectangle claim | My independent recomputation | Verdict |
|---|---|---|---|
| join.49financial | Feed key = SmartX allocationId (uuid-rate 1.00, 7,230 distinct; custodian 0 non-null; household_id 0 non-null); spine fact_acc 7,239 distinct 10-digit; overlap **0.0%** exact + digits-normalized + last-8 | Recomputed from `mdpf/feeds/model_aua_positions/49financial/2026-08-11.parquet` + `schwab/08335338/silver/fact_acc/date=2026-08-07/data.parquet`: feed 7,230 rows / 7,230 distinct / uuid-rate 1.00 / len-36 rate 1.00 / custodian 0 / household_id 0; spine 7,239 distinct / all-digit 1.00 / len-mode 10; overlap exact **0**, digits-normalized **0**, last-8 **0**. `date=2026-08-07` re-verified as the newest fact_acc partition. SOURCE: `wsb_49f_smartx_model_aua.py:167` `"account_id": r.get("allocationId")` + `:169` `"custodian": None,  # not exposed on the SmartX allocation row` -- verbatim | **CONFIRMED, every number exact.** The STRUCTURALLY-IMPOSSIBLE verdict + identity-acquisition framing are sound; the 7,230-vs-7,239 count-parity trap is real and confirmed live |
| join.inflection | 550/561 = 98.0% exact on native key; spine 869 distinct | Recomputed: feed `inflection/2026-08-06.parquet` 561 distinct (uuid-rate 0.00); spine `accounts_dimension_latest.parquet` 869 distinct; exact overlap **550/561 = 98.0%**. NOTE: the spine object was REWRITTEN 2026-08-11T05:40:35Z (head-object) -- AFTER CRO's cited 08-10T14:08Z vintage read -- and the claim survives on the new object (869 distinct unchanged, 550 overlap unchanged). Different derivation AND different vintage reaching the same numbers is stronger than a same-vintage tie | **CONFIRMED** -- and robust to the artifact moving underneath (CRO~A's live INF repair is rewriting this pointer) |
| join.cottonwood | NO model_aua_positions partition for cottonwood; firms exactly {49financial, inflection}; 116 objects | Live enumeration: prefixes under `mdpf/feeds/model_aua_positions/` = exactly `49financial/` + `inflection/`; recursive object count = **116** exact. Absence claim carries its denominator and both match | **CONFIRMED.** The ~0547Z Andrew amendment (source exists via BD Rebalance endpoint; ingest leg absent) is testimony-graded in-artifact -- correctly not presented as measured |

## REFUSED AS WRITTEN (one item)

**The run record's census line.** `run.json` (and the deliverable header) declare
**20 MEASURED / 2 INFERRED / 2 NOT_MEASURABLE**; the shipped `rectangle.final.json` actually
carries **21 MEASURED / 1 INFERRED / 2 NOT_MEASURABLE** (recomputed from the cells; total 24 both
ways). A patch -- most plausibly the ~0547Z cottonwood amendment -- flipped a cell's grade without
the census being rewritten. The mdpf decomp's census summed exactly; this one does not. Nothing
load-bearing rides on it, but a machine record whose self-description disagrees with its own cells
is the declarative-drift class, and the fix is one line: regenerate the census from the cells (and
have the run writer derive it, never hand-state it). **CRO to correct; cert of the three
load-bearing cells is unaffected.**

## GRAIN CORRECTIONS (in-place, not refusals)

1. **`join.inflection.feed_key_identity` says "len 2-4" -- measured len range is 2-14.** 550 ids
   are len 2-4; 11 are len 12-14. The load-bearing overlap number is untouched.
2. **The same measurement SHARPENS the residual CRO left open:** the 11 unmatched accounts are
   EXACTLY the len-12-14 ids, and the 550 matched are EXACTLY the len-2-4 ids -- a perfect format
   partition, zero crossover. The residual is therefore NOT random attrition (closed accounts /
   vintage skew would scatter across short ids): the 11 rows carry keys from a DIFFERENT ID
   NAMESPACE leaking into the feed (candidate: custodian-native account numbers where the Orion
   short id was unavailable). The open question flips from "why did 11 accounts not match" to
   "which upstream emits long-format ids into this feed" -- likely answerable at the inflection
   feeder's source field in one read. Routed to CRO as method input, no action taken here.

## What you should have asked but did not (Doctrine §7) -- asked, then ANSWERED here

Whether the 49F identity-acquisition problem is SYMMETRIC: RECON-4 measures that the feed cannot
reach the spine's Schwab numbers -- nobody asked whether the spine side carries a SmartX id that
could crosswalk the OTHER direction. **I measured it rather than posing it: all 95 columns of the
cited spine table (`fact_acc`, date=2026-08-07) scanned for UUID-format content, 500-row sample per
column -- ZERO UUID-like columns.** The table is pure Schwab CRS ACC content (taxpayer, mailing,
branch, managed-account fields). The crosswalk provably does not exist in `fact_acc`, so the
identity-acquisition framing HARDENS: the missing link must come from a SmartX surface (RECON-2's
endpoint question) or an out-of-band mapping. Honest boundary: other `08335338/silver/*` tables not
swept -- if RECON-2's endpoint probe comes back empty, sweep those before concluding the identity
source must be manual.

-- 3.0.0_SA_CVO

---

## CERT ADDENDUM (0620Z) -- grain-correction 2's MECHANISM hypothesis SUPERSEDED by DS's source
## close; my re-verification confirms; addendum-4 @8f14253ae9 figures DELTA-CERTIFIED

DS measured the residual cause at source (061733Z): the 11 unmatched are the inflection feeder's
DESIGNED portfolio-stub fallback -- `build_mdpf_wsc_inflection_feeder.py:303-309`,
`account_id = f"portfolio_{int(pid)}"` when `eclipse_account_id` is absent. My re-verification
from the artifacts already in hand: **11/11 unmatched carry the `portfolio_` prefix, 0/11
all-digit, model_value sum $0.00 exactly; real-account join = 550/550 = 100.0%, matched
model_value $144,882,401 -- zero AUA unjoined.** Source lines confirmed at HEAD.

So: my FORMAT ISOLATION stands (the tail is structurally distinct, zero crossover -- that is what
made DS's one-read close possible), but my MECHANISM hypothesis ("namespace leak; candidate
custodian-native account numbers") is DEAD -- the tail members are underscore slugs, not ids, and
the mechanism is book-definition-by-design. The hypothesis died the honest way: it named its
discriminating read (the feeder source field) and that exact read killed it. Addendum-4's
grain-labeled figures (98.0% raw-row / 100.0% real-account) are CERTIFIED; a certifier's record
does not leave its own wrong mechanism standing, hence this addendum.

-- 3.0.0_SA_CVO
