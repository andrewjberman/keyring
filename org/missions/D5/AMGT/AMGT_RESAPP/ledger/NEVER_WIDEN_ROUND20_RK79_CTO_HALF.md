# AMGT_RESAPP round 20 -- never-widen pair, R20-A (+ R20-B folded) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-21 ~20:4xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND20_RK79_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`22a1fc5d0e`).
**Sources:** `ROUND_ANALYSIS.round19.md` @`e25b2bee60` s.2-s.4; the COO's issuance note (msg 24061); PRD v0.16
@`2d0da569e7` `C-EXEC-MANAGEMENT`; Andrew-direct ~19:5xZ @`4bcfed0e0d` (one Keyence search).

## `AMGT-rk-79` -- one CEO web search for Keyence, readable roster reasons, CAT marked incomplete: THREE writes

### 1. WHAT THIS HALF COVERS -- the blast radius, whichever branch the producer takes

The act MAY write exactly three S3 objects, one NEW version each, and nothing else:

| key | may change | pre-act latest (live read, this seat) | rollback |
|---|---|---|---|
| `management/v1/6861_JP_Equity/2026-09-19.json` | `roster_reason`, `absence_reason_evidence`, `ceo_profile`, `ceo_public_profile` | `1Hm1g.MqxkFnnyRqLgQlwSiB925mRG9G`, 3827 B, 19:03:39Z | `copy_object` from the worker's AC3 pre-act VersionId, then sha256 read-back |
| `management/v1/CSL_AU_Equity/2026-09-19.json` | `roster_reason`, `absence_reason_evidence` | `u_iDxPeXTBMyIMZtwYwJYVU53iwMdgiS`, 9494 B, 19:03:38Z | same |
| `management/v1/CAT_US_Equity/2026-09-19.json` | `roster_status`, `roster_reason`, `section_refers_to`, `absence_reason_class`, `absence_reason_evidence` | `tJMJuD2oIO1ONv6dngrilLVgX4tOS3qU`, 3256 B, 19:03:37Z | same |

- Bucket `opal-data-harvest`, all in `s3://`. Each key held 3 versions and 0 delete markers at this seat's read, and the
  latest VersionIds equal the COO half's cut values.
- Instrument: `s3api list-object-versions`, one call per key. That is the same plane as the COO's cut, not an
  independent instrument. **The worker's AC3 value is the rollback target where it differs.**
- **Vendor egress (6861 only):** ONE `serp_brightdata_records(max_pages=1)` call, at most 3 SERP requests, at most 3
  result-page GETs, at most 4 model calls, **cap USD 1.00**. The mode checks the cap BEFORE the write; if it is exceeded,
  the run is BLOCKED and nothing is written. The spend is not reversible, and Andrew's word covers it.
- **Both branches are covered for every key.** For 6861, the searched branch (CURATED, NOTHING_FOUND, UNREADABLE or
  SEARCH_FAILED) or the not-searched branch. For CAT, branch B (Item 1D not held, measured at the cut) or branch A
  (held at spawn: parsed from it, with officers changing, which is a REFUSAL branch under this pair, not a covered
  write). **So under this pair CAT is only ever re-classed. A parse that moves its officers stops and comes back.**

### 2. WRITER CENSUS -- read, not repeated

The COO half counts N = 3 writes through `write_document`, one per key, with every other writer patched to RAISE in the
order's tests. This seat accepts that count and does not re-derive it; it carries the Z-S192 lesson (count one call
deeper). The one rule this seat read itself is the served class for CAT:
- `scoped_amgt.py` `read_management`, the `roster_status != "RESOLVED"` branch (repo lines ~2615-2634 at HEAD, printed by
  this seat): ABSENT / `ROSTER_UNRESOLVED_NO_FALLBACK`, `officers []`, with `reason` = the stored `roster_reason`, and
  `roster_status` verbatim.
- The COO measured the DEPLOYED bytes equal to the repo (sha256 `9832f57a...`). This seat did not re-download the
  artifact; that identity is the COO's measurement.

### 3. WHAT A MANAGER WILL SEE -- ACCEPTED

- **CAT changes from SERVED (1 officer, no CEO) to ABSENT, and its officer table is withheld.** The line shown is "The
  10-K lists its executive officers in Item 1D, which was not read, so this roster is incomplete."
- This is accepted as the truthful class under the deployed adapter. A one-officer table labelled complete is the
  defect S202 names. An explained absence is not.
- **Named follow-on (not covered here):** CAT gets a real roster by either Andrew's EDGAR word (the card) or, failing
  that, a Bloomberg fallback built from the STORED `raw/bloomberg/` objects. That would be an act with a write path this
  pair excludes (`apply_bloomberg_fallback` writes raw), so it needs a new pair in a later round.

### 4. THE FOUR WORDING ITEMS (msg 24061) -- APPROVED

1. The UNRESOLVED-filing sentence rule and its route table, including CSL's sentence as quoted in the COO half. The
   COO's measurement over 180 unresolved filings objects, 0 printing None, is the evidence I rely on.
2. `INCOMPLETE-NO-CEO`, one new enum value, and its two sentences.
3. Rule 1b retires the "no reason recorded" sentence. That is sound only because (1) always yields a reason, so the
   retirement rides on (1)'s None census.
4. rk-80's subtitle, "Officers from the Bloomberg fallback list -- the filing roster did not resolve".

Also accepted: rk-80's one-check amendment to rk-78's `resolved_unchanged`, which sets aside CAT's CEO line on both
sides. Without it the check turns permanently red (the Z-S193 class).

### 5. NOT COVERED

Everything the COO half's NOT COVERED lists, plus:
- any write if CAT's re-derivation would change its officers;
- any served RESOLVED roster with no CEO after the act. The census must read 0 of 15, or the run rolls back.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-21 ~20:4xZ. The vintage is this file's commit.
