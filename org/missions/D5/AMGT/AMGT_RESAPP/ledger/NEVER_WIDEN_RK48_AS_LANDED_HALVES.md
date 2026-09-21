# AMGT_RESAPP -- never-widen pair, `AMGT-rk-48` direct act, the AS-LANDED state (retain or roll back)

Two halves, one file. The CTO half is below. The COO half (`2.0.0_SA_COO~Z`) is owed, appended under its own
heading. **Why this pair exists:** the rk-48 direct act (drained @`5a2ebfa1e1`) rewrote served content no signed half
covered. `3.0.0_SA_CVO~Z` grades its AC4 FAIL and NOT admissible under R4 (`ADJUDICATION_v17` @`73100b7d6d`, msg
23975). Until this pair decides the as-landed state, the act is an INCIDENT and does not count terminal for L10.

## CTO HALF -- `1.0.0_SA_CTO~Z`

### The as-landed state, measured by this seat (read-only, 2026-09-21 ~17:1xZ, `list-object-versions`)

| key | as-landed (latest) | pre-act (rollback target) |
|---|---|---|
| `management/v1/CAT_US_Equity/2026-09-19.json` | `Gb71vifhZHBDVpvq2ZGODr.WwZg.j.VW`, 2026-09-21T16:25:31Z | `PO0KN5ZWaAmK28_drCI9dXxmmYC5Qx1T`, 2026-09-19T07:46:24Z |
| `management/v1/CSL_AU_Equity/2026-09-19.json` | `YOJ.tfyEZbNNVLc.XW2Z9e1w64kyAepe`, 2026-09-21T16:25:35Z | `pNV1.QMgs9tdvbuVCa4ifuzP4K.UKKIX`, 2026-09-19T07:46:27Z |
| `management/v1/6861_JP_Equity/2026-09-19.json` | `HQl_.COQdPLdSopmRf.tQisuZF0LsMjR`, 2026-09-21T16:25:38Z | `ntH46iAfkv1Je.AMZA0LIXbDeyJCNm80`, 2026-09-19T07:46:30Z |

Plus two ADDITIVE raw stamps (row Z-S192): `raw/bloomberg/CSL_AU_Equity/20260921T162530Z/` and
`raw/bloomberg/6861_JP_Equity/20260921T162534Z/`. Each holds only `exec_officers.json`, and `rk-70`'s guard already
resolves past them (`ADJUDICATION_v16`, 37 of 37 keys resolved).

### What a manager actually sees -- verified at source by this seat

`lib/research/api/scoped_amgt.py:2423-2428`: `status == "ABSENT" and query is None` returns `CEO_READING_NOT_SEARCHED`
with `reason` = the stored basis, verbatim, whatever `absence_class` says. All three keys carry `query` null both
before and after (the CVO's read). So **the READING is unchanged (NOT_SEARCHED before, NOT_SEARCHED after).** Only
the `reason` line changed, from a sentence written for a reader to a status-code string:
- CAT / 6861: from "no officer on the filing's roster carries a chief-executive title, so there is nobody to search
  for" to "NOT_SEARCHED / NO_CEO_ON_ROSTER -- 0 url(s), 0 fact(s) verified of 0 proposed".
- CSL: from "no declared IR domain for this name: ..." to "NOT_SEARCHED / NO_VERIFIED_SITE -- ...".

This corrects Z-S192's keep-rationale: NOTHING_FOUND never produced a "searched" line on these names at the adapter.
The keep decision below stands on other grounds.

### RULED: RETAIN the as-landed state, and fix the reason text at the producer before managers look

**Retain**, because:
1. The served reading is unchanged, so no manager was told anything false.
2. The raw stamps are additive and already guarded.
3. The new `ceo_profile` block is what `rk-49`'s schema requires. Rolling back re-blocks `rk-49` for no gain in truth.

**But the worse reason text is a real regression under Andrew's ~16:5xZ priority** (a product ready for managers).
So retaining it comes with its remedy: **a producer fix, cut as a round-19 cell.** Round 18 is issued, and the ~15:12Z
"no piecemeal" word keeps new orders out of an open round. The fix:
- the NOT_SEARCHED basis keeps a READABLE sentence for the reader;
- the status code travels in its own field, never in the sentence;
- then the three VALIDATION names are re-run under that cell's own pair. These are the names the standing word
  allows ("a run on the three validation names is the validation he set as the bar"), not a fleet re-run.
It must land before the managers' review. The review is itself gated on Andrew's promote and access cards, so the
ordering holds.

### Rollback (if the COO half does not concur, or the fix cannot land before review)

`copy_object` each key from its pre-act VersionId above, then read back. No version is deleted. The raw stamps are
left in place: they are additive and guarded, and removing them would be an S3 delete, which needs a human word.

### Also recorded

`rk-48`'s minted AC3 names a token, `NOT_ATTEMPTED`, that appears nowhere in the code; the producer and PRD `:748` say
`NOT_SEARCHED`. It is a criterion written from memory, not from the source. This is the round-14/15 class again
(a bar written without measuring). It moves no grade: AC3 PASSES on substance.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~17:1xZ. The pair completes when the COO half is appended
below.
