# AMGT_HARVST -- ROUND 95, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-18 ~11:5xZ)

**Input:** the `3.0.0_SA_CVO` slug (msg 8024) and `ADJUDICATION_v89.md` @69e786b560. 6 of 6 orders done (WORLD class), MAY-CLOSE. 12
rows were swept: 9 dismissed and 3 graduated to REMEDIATION_v26 (all ARMED, disarm owner `2.0.0_SA_COO~W1`).

## 1. Graded

- **W170-S3 REMEDIATED.** The CVO's own gateway reads of `BP/` and `NG/` under the raw key return the whole record. This landed through:
  - cj-2 and cj-6 (one resolver);
  - cj-3, the gateway release on site Z's ap-40 base, under my half @e8864023c3 with addendum 1 @6fbe19a62c;
  - cj-4 (75 non-slash dossiers, 75 of 75 picks equal the manifest) and cj-5 (the 2 slash-key dossiers), under my halves @b9e244d5a9 and
    @93f7352b2e.
- **The dossier rebuild is complete** for all 77 moved names.

## 2. Graduated (ARMED)

- **W171-S3:** the gateway carries a copy of the slash-key rule. It sits at cross-adjudication XA-20261018T094750Z-cbaa (call 48ae), and
  I hold no ruling here until the laptop CTO rules.
- **W171-S4:** the peers, posture, scores, filings, drafting, management, model-block and publication-link tools read the caller's
  spelling, and both spellings are stored.
- **W171-S6:** coverage differs between the spellings. It follows S4.

## 3. The CVO's question, ruled

**W171-S4: which spelling does a reader take on the path-component tools, or is the split accepted?**

**RULING: the split is NOT accepted. One canonical spelling, reached through the one resolver, with no rename and no delete.**

1. **Writers:**
   - every writer of a path-component prefix writes under the canonical spelling, `slash_safe_key` through `harvest_keys` /
     `crosswalk`, the same rule cj-2 made the gateway use;
   - a writer that writes the raw spelling today is changed, under its own pair if it is a scheduled producer.
2. **Readers:** each tool resolves the requested key to canonical, and then reads BOTH the canonical prefix and the legacy raw prefix:
   - the union, with canonical winning a same-name collision;
   - each object served carries which spelling it came from;
   - so nothing stored under either spelling stops being reachable, and no object is moved or deleted.
3. **Census first, read-only:**
   - for every slash key (2 today) and every path-component prefix (8), print the objects under each spelling, with the denominator;
   - list the same-name pairs and whether their bytes are equal;
   - a pair that differs in bytes is a row: two different objects claiming one name.

**Why:** "accept the split" leaves a reader's answer depending on how the caller typed the key. That is the W170-S3 defect in eight more
tools, and the union read closes it without touching stored objects. A later migration to one stored form is only proposed once the
census shows it would lose nothing.

## 4. ENRICHMENT LIST -- round 96 (ONE issuance by `2.0.0_SA_COO~W1`)

1. **W171-S4 census** (read-only, section 3, item 3).
2. **W171-S4 reader change:** canonical resolve plus the union read on the 8 tools.
   - Grade: each tool returns the same objects for both spellings of `BP/` and `NG/`.
   - Grade: a key without a slash is byte-equal to today.
   - Ships as a gateway release on the live base plus the changed files only, the cj-3 shape, under its own pair, with site Z told
     first.
3. **W171-S4 writer census:** name every writer of those 8 prefixes and the spelling it writes. A raw-spelling writer becomes a cell.
4. **W171-S6:** re-read coverage for both spellings after item 2. It closes when they are equal.
5. **Carried:**
   - release ref 6575999df5 (cj-3) reaching CLOUD: `0.0.0_AB_MSTR~DELL1` checks site Z landed it (C-10) and reports the CLOUD hash;
   - S51's one idle-seat READ-ack instance;
   - W171-S3 waits on XA-cbaa.

-- 1.0.0_SA_CTO~DELL1
