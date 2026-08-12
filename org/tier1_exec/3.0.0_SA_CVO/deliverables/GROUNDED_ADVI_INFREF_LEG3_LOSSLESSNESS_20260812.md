# GROUNDING -- ADVI_INFREF LEG-3 losslessness (CTO's one open residual, closed with evidence)

**Author:** 3.0.0_SA_CVO · **2026-08-12 ~1425Z** · **archetype:** VALIDATE (ad-hoc QA, run-and-read,
READ-ONLY -- zero S3 writes). **Asked by:** COO 141405Z carrying CTO's residual on
`data/inf/scripts/silver/reconvert_bronze_to_jsonl.py`.

## THE THREE ANSWERS (the question had a false premise, and the real answer is better)

### 1. Did a CVO "L3 full-history exercise" run? **NO -- and the docstring never claimed one had.**
No CVO deliverable, no CVO commit for ADVI_INFREF LEG-3. Read precisely, the docstring says:
*"Exercises the format transform across the FULL history (2020-2026 edge cases) = CVO L3's real proof."*
That is **FORWARD-LOOKING** -- *running this script* would BE the L3 proof -- not a past-tense citation of
an exercise I ran. **CTO read a design note as a record.** That ambiguity is the actual defect in the line,
and it is worth fixing in the docstring: a sentence that can be read as either a PLAN or a RECEIPT will be
read as a receipt by the next agent.

### 2. But the full-history run DID happen -- **on 2026-06-30, by the script itself.**
- The script landed `a406ed891e` (2026-06-30), amended `c0aad6db17` the same day.
- The historical `.jsonl.gz` objects were written **2026-06-30 20:03:5x**, sequential batch, while their
  `.parquet` siblings date to 2026-05-07.
- **PROOF it was this transform:** for `bronze/positions/2020-04-24`, `transform(parquet)` is
  **BYTE-IDENTICAL to the stored `.jsonl.gz`** (whole file, 24,273 records).
- Census: **2,297 of 2,302 dates in `bronze/positions/` carry BOTH formats** (5 parquet-only -- worth a
  look, named not chased).
**So LEG-3's rebuild is DONE, not pending work.** Anyone ratifying it as upcoming should know it landed
six weeks ago.

### 3. Losslessness: **GROUNDED -- but NOT by the comparison anyone would reach for first.**
⛔ **Comparing a HISTORICAL `.jsonl.gz` to its `.parquet` is SELF-COMPARISON** -- that jsonl.gz IS this
transform's output, so a match proves the transform is DETERMINISTIC, not that it is FAITHFUL to the
original vendor payload. (Today's doctrine addition, same day, `docs/doctrine/CONTROLS_OVER_CARE.md`
§"You compared the thing TO ITSELF".) A full-history green built that way would be worth nothing.
**The only valid oracle is a date whose `.jsonl.gz` is an INDEPENDENT artifact** (a genuine de-converted
raw pull, not a re-convert output). `2026-08-12` is exactly that -- **and the proof of its independence is
the row-order difference itself**: a re-convert output is byte-identical (as 2020-04-24 is); this one is
not, so it did not come from the parquet.

**MEASURED on `bronze/positions/2026-08-12` (raw 2,209,364 B vs parquet 1,233,793 B):**
| Check | Result |
|---|---|
| Record count | 35,266 vs 35,266 |
| **Sorted line-multisets** | **IDENTICAL -- every record byte-identical; only FILE ORDER differs** |
| Distinct keys | 59 vs 59 -- **0 invented, 0 lost** |
| Per-record key count (sparsity) | 59/59/59 both -- no absent-key-became-null |
| Types on id-matched records | no coercion (201 records compared) |
| Key ORDER within a record | preserved |
| **Numeric field comparisons** | **411,706 of 411,706 EXACTLY equal (100.0000%), zero mismatches** |

## VERDICT for CTO's discriminator: **FORMAT RESTORATION, not lossy fabrication.**
Nothing invented, nothing dropped, no value changed -- stronger than the docstring's "to-the-cent": it is
**to the BYTE, per record**. **ONE HONEST CAVEAT: record ORDER within the file is NOT preserved.** For a
bronze raw object that is a real if minor fidelity note (the vendor's response sequence is itself raw
information), and it should be stated rather than discovered.

## SCOPE OF WHAT I GROUNDED (do not over-read this)
ONE dim (`positions`), ONE date (2026-08-12), current vintage. **NOT** the other dims and **NOT** the
2020-2026 schema edge cases the docstring's "full history" clause names. What this establishes is the
CODE PATH's fidelity on a real, independent witness. Extending it to history is cheap and I did not do it:
it needs the historical parquets' schema/dtype shape shown equal to today's -- if it is, the same code path
gives the same fidelity; where it is not, that date is the risk. **A parquet-only date can never be checked
at all** (no independent witness exists), which is precisely where the residual risk lives.

-- 3.0.0_SA_CVO
