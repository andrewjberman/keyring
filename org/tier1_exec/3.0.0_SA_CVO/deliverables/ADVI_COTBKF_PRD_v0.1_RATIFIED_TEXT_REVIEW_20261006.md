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

## Addendum -- v0.2 @87864d6648 (half_hash 570557faf96a): fixes ACCEPTED; sign on Andrew's yes

- The ENDPOINT is unchanged: the v0.1-to-v0.2 diff does not touch lines 24-86.
- Item 1 is fixed. C-SOURCE now names one declared exception: the CRM zip's key in the firm bucket, written only in
  the R20 entry. Every other address is builder output.
- Item 2 is fixed. C-RESTRICTED names:
  - the owner (`s3-lgic-firm-buckets.tf`, lane CLOUD_OPS_OR_ETL);
  - a policy that refuses everyone by default, with one write by the landing role, live before any write;
  - Andrew as the one who names the readers.
- Item 3 is fixed. The row is recorded as landed, with the builder output printed.
- One note, not blocking. The C-RESTRICTED proof includes "one allowed read by the group". If the group is Andrew
  alone, only he, or the break-glass role on his word, can make that read. FWD-7's DONE WHEN needs only the refused
  read, which a seat can make on demand. So the ENDPOINT itself waits on no one.

The half is ready. Andrew's yes to the eight outcomes is still owed (`"status": "DRAFT"`). This seat signs v0.2 on that yes.

-- 3.0.0_SA_CVO

## Addendum -- v0.3 @5567e751f1 (half_hash e6df4f6ccbbd), RATIFIED: SIGNED

**Andrew's word** (record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_174xZ_COTTONWOOD_BACKFILL_ALL_AGREED_FWD3_DAILY.md`):
"All agreed but we need daily granularity when it comes to FWD 3".

**The diff from v0.2.** In the ENDPOINT only FWD-3 changed. CONTRACTS gained C-DAILY, and C-SENSITIVE and C-RESTRICTED
gained his acknowledgement and the named readers. Nothing else in the half moved.

- **FWD-3 matches his words.** It moves from monthly to daily. Commonwealth's own monthly, yearly and since-inception
  figures and its benchmark stay readable, so brief O3 is still met. The DONE WHEN is an act a seat can take on
  demand: one account's days, chained to months and checked against Commonwealth's months.
- **C-DAILY is honest about the source.** The delivery holds no daily return (brief F2: Month, Year and
  Inception-to-date rows only), so daily returns are derived:
  - an UNKNOWN day is never filled in;
  - each month is graded MATCH or DIFF with its reason;
  - Opal's own price stores are read first, with their coverage printed;
  - any outside price vendor waits for Andrew's per-use word, as the law requires.
- **Readers.** C-RESTRICTED's named group (Andrew alone, plus a break-glass role on his word, no agent seat) is his
  word as recorded.
- **Form.** No history or seat serial inside the ENDPOINT block. FWD-3's SOURCE line quotes Andrew as the source of
  the grain, the same way FWD-7 cites his call.

**Notes for the round, not blocking:**
1. C-DAILY's "stated tolerance" is not stated yet. The issuer states it in the order that builds S10, before the first
   month is graded, so the grade is not set after the result is seen.
2. FWD-3's ACCEPT is satisfied by a day that says UNKNOWN. So the round-1 close should print how many account-days are
   computed against the total. Accounts with holdings before 2013-04, and accounts closed before 2026-06-23, have no
   delivered opening state. A mostly-UNKNOWN result would be honest, but it must be visible as a number.
3. Section 4's lane line (`2.0.0_SA_COO~C`) is the CTO's reading of "All agreed". It sits outside this half and is not
   graded here.

-- 3.0.0_SA_CVO
