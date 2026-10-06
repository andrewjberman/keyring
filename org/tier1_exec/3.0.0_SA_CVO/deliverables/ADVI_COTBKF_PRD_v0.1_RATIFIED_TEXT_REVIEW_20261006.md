# ADVI_COTBKF PRD v0.1 @3a89d79e77 -- ratified-text half review (half_hash 252056cbee09)

**Reviewer:** 3.0.0_SA_CVO, 2026-10-06 ~17:3xZ. **Asked by:** 1.0.0_SA_CTO msgs 105649 and 105650 ("review now, sign after
his yes"). **Read against:** the brief @902feb3a4f; Andrew's order
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_16xxZ_COTTONWOOD_COMMONWEALTH_10Y_BACKFILL_SPEC.md`);
his three calls (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_172xZ_COTTONWOOD_BACKFILL_THREE_CALLS_SENSITIVE_IN_FIRM_BUCKET.md`);
`lib/opal_naming.py` at HEAD; the ADVI_FIRMBKTS PRD.

## Verdict: NOT SIGNED YET. ENDPOINT is clean; CONTRACTS needs two fixes and one refresh. Andrew's yes is also still owed.

## ENDPOINT -- PASS

- Each outcome traces to the brief: FWD-1 is the candidate thread (which also carries O2, transactions back to 2013),
  then FWD-2 = O1, FWD-3 = O3, FWD-4 = O4, FWD-5 = O5 + F4, FWD-6 = O6 + F5, FWD-7 = O7 + F6 + call 1, and FWD-8 = O8.
- FWD-6's spans match F5 exactly: 13 years of transactions and returns, 10 of activities, 12 months of statements,
  2 tax years, 1 day of positions.
- FWD-7 adds "an unauthorised read refused" to O7. That is stronger than the brief, and an act a seat can take.
- No history, seat serial or annotation inside the block. "Andrew" in FWD-7 names who decides, as the brief's O7 does.
- One phrase dropped: O1's "at addresses the naming canon produces". C-SOURCE carries it, so it is not lost.

## CONTRACTS -- two fixes, one refresh

1. **C-SOURCE contradicts C-SENSITIVE.**
   - C-SOURCE says every address in this project is builder output, none typed by hand.
   - C-SENSITIVE puts the CRM zip in `opal-data-cottonwood`.
   - `address()` (`lib/opal_naming.py:1751`) picks the bucket by the tier's home rule and takes no bucket argument.
     For a bronze key of scope `cottonwood` it returns only `s3://opal-data-assets/...`, measured here as
     `s3://opal-data-assets/commonwealth/cottonwood/bronze/crm/date=2026-06-23`.
   - So the CRM zip's address cannot be builder output. As written, the two contracts cannot both hold.
   - Fix: C-SOURCE names the one exception (the R20 departure's address, typed in the R20 entry), or the PRD names
     the registry row that would let the builder produce it.
2. **No counterpart for the restricted prefix in `opal-data-cottonwood`.**
   - The bucket exists, and its fence and serving grants were adopted and repaired by ADVI_FIRMBKTS. The Terraform is
     `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf`.
   - ADVI_FIRMBKTS's F9 also names `opal-data-cottonwood` as the destination of Cottonwood's cutover.
   - "A prefix readable by a small named group only" is a bucket-policy change on that file.
   - CONTRACTS has no row naming that Terraform's owner, or who the named group is. Fix: one contract row giving the
     owner and the group.
3. **Refresh.** C-SOURCE's "MEASURED at L4: the builder refuses `address('commonwealth', ...)` today" is no longer
   true. The row landed @8e39143feb, and the builder now returns the address above. This is a wording fix. Under
   proportionate sign-off it re-opens nothing.

## What is not this reviewer's call

Both R20 departures in C-SENSITIVE wait on Andrew. His "maybe" on `opal-data-cottonwood` is carried as a proposal, not
treated as decided, which is right. Whether he acknowledges it is his call. If he declines, item 2 disappears and
item 1 becomes a one-line deletion.

## Sign when

The CTO fixes items 1 and 2 (any version), and Andrew gives his yes to the eight outcomes. Then:
`python .tools/prd-signoff.py sign ADVI_COTBKF --half ratified-text --review <this file>@<pin>`.

-- 3.0.0_SA_CVO
