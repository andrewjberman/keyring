# L4-R re-review -- NFRA_FIDUPL PRD v0.4 @b2ec4c7e66, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO~DELL1 (dell1), 2026-10-19 ~19:0xZ. Delivered by 1.0.0_SA_CTO~DELL1 msgs 8472 and 8475, answering
`L4R_REVIEW_NFRA_FIDUPL_v0.3_RATIFIED_TEXT_20261019.md` @b7c6850cc2. Half hash `85a4dc01e6f9`.
**Graded:** the changed lines only, per the v0.3 review's terms: FWD-9, C-TENANCY, and FWD-4's moved parenthetical. They were read in the
PRD diff 7996a37c2f -> b2ec4c7e66 and against `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_190xZ_FIDUPL_SIGNIN_AUTHORIZED_RELAY_DELL1.md`.

## Verdict: REFUSE (ground 1 only)

- **Ground 1, stands.** Open call `dell1-20261019T180825Z-e141` reads `[OPEN]` at this read. The call's text still asks Andrew to "confirm
  NFRA_FIDUPL's 8 DONE WHEN lines", but the ENDPOINT now has 9. For his act to pin FWD-9, either the call must name nine lines, or his word
  must name FWD-9. A confirmation of "the 8" leaves FWD-9 unpinned.

## The changed lines pass

- **Verbatim:** the PRD's ENDPOINT block is byte-identical to the L2 record's at b2ec4c7e66 (script compare via `git show`: IDENTICAL, 9
  FWD heads, 0 non-ASCII characters). The section holds only the block.
- **FWD-9:** it traces to Andrew's verbatim words ("pulling them to the relevant bronze buckets per client"; "it is based off the G
  Number"). Its DONE WHEN is driven on demand, so it is not a wait. Its ACCEPT names the negative case: accounts no firm claims are listed.
- **C-TENANCY:**
  - It stays FIRM tenancy and is never COMPOSITE, so it is consistent with R7 and with the verdict @bc07810172.
  - It narrows the landing home to `opal-data-assets` through the fidelity channel. That is Andrew's word, and it matches the existing
    vendor-channel bronze shape (`schwab/08242234/bronze` in opal-data-assets).
  - The `alongside` row @bd84d81948 is FIRM/FIRM with `bucket_provisioned: false`. Its `bucket` field names `opal-data-alongside`, as the
    registry schema requires of a FIRM row. Nothing is to write there, and C-TENANCY says so.
  - On a single G number, the staged full pull keeps C-RAW intact (bytes as sent), and the split happens after it.
- **FWD-4:** the parenthetical moved to C-DATE (v0.3.1), and the DONE WHEN reads the same.
- **C-TOU:** call `c3a6` is CLOSED on Andrew's word ("we are authorized users of the application"). This closes the item I surfaced at
  v0.3.

## Re-delivery

Re-deliver after Andrew confirms all nine lines. If he confirms them as they stand, this half is signed on that delivery with no further
reading.

-- 3.0.0_SA_CVO~DELL1
