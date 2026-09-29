# L4-R review -- MDPF_SECCLASS PRD v0.1, ratified-text half (`3.0.0_SA_CVO`)

**Delivery:** `1.0.0_SA_CTO` message 103032, 2026-09-29T20:54:59Z. **PRD:**
`org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` @`b9680cfe86`, half_hash `db182bcd984d`.
**Verdict: SIGN.** Two wording notes (W1, W2) and two items for L5 (Q1, Q2). None re-opens the half.

## The review limbs

| limb | result | evidence |
|---|---|---|
| ENDPOINT verbatim against the ratified pin | PASS | the FWD-1..FWD-8 block of the PRD @b9680cfe86 against the endpoint `CANONICAL_SECURITY_TABLE_ENDPOINT_FORWARD_20260929.md` @8639932f66, both read by `git show`: 79 lines each, 0 diff lines |
| Andrew's confirmation of the DONE WHEN lines | PASS | `ANDREW_DIRECT_20260929_195xZ_CANONICAL_SECURITY_TABLE_DONE_WHEN_CONFIRMED.md` quotes "yes this is all correct" against the same endpoint pin |
| every operative constraint present | PASS | the server-side word is C-SERVER; the per-use vendor word is C-VENDOR; the destructive delete is C-DELETE; never-widen is C-SERVED; cross-firm is C-FIRM; rule 30 is C-NAMES |
| no annotation, history or seat name inside the section | PASS with W1, W2 | the only seat and message references are inside SOURCE lines that are the endpoint's own bytes |
| CONTRACTS agrees with the counterpart PRD | PASS | `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md` defines C-FIVE-CLASSES (:415) and C-ONE-SOURCE (:417); C-TABLE consumes both and changes neither |

## Checks this seat ran

- **Names (C-NAMES).** `lib/opal_naming.py name('mdpf', None, 'secclass', k)` for `lambda`, `role`, `daily` returns
  `mdpf-secclass-lambda`, `mdpf-secclass-role`, `mdpf-secclass-daily`. The PRD's three names are builder output.
- **Contract file.** `org/standards/MDPF_SECCLASS_CONTRACT.json` exists (4,074 bytes) and carries a four-postulate
  record and a token census for both `instrument_kind` and `classified_by`.
- **C-WRITER against the seed script.** `seed-etf-classifications.py` (306 lines) writes with `put_item` inside a
  batch writer after a paginated pre-read, and has no delete call. A seed run therefore does not remove a row the
  scheduled writer added. The "seed always wins" rule and the "scheduled writes only absent rows" rule can both hold.

## Wording notes (not blocking; they are the endpoint's bytes, so a change is an endpoint edit)

- **W1.** FWD-6's SOURCE line says "section 2 below (the CTO's decision)". In the PRD, section 2 is the THREAD. The
  reference points into the endpoint document. ENDPOINT PROVENANCE already states the decision, so a reader is not
  misled if they read both.
- **W2.** FWD-7 and FWD-8 SOURCE lines say "brief addendum pending". The addendum is committed at @87ad6973f3. ENDPOINT
  PROVENANCE says so.

## What you should have asked but did not

- **Q1. The seed script has two overwrite flags.** `--force-overwrite` skips the pre-read and writes every item.
  C-WRITER says seed always wins, which is correct for a ticker in the seed source. The L5 cell for FWD-7 should state
  that a forced seed run still touches only tickers the seed source names, and prove it on a table holding one
  `scheduled` row.
- **Q2. The seating lint does not evaluate tree orders.** Section 5 records that `.tools/to-decomp-ref-lint.py` tests
  `task_orders/` while the tree folder is `task-orders/`. Andrew's word seats FWD-7 and FWD-8 on `2.0.0_SA_COO~M`, who
  already holds IRPT_BCKEND. No instrument has graded that fit. It needs an owner before L6, or the first ~M issuance
  under this project passes a gate that never looked.

## Not verified by this seat

The file:line addresses marked `held` in the SURFACE MANIFEST, the live `bd-securities` table, and the brief's
98-file token census. They are outside the ratified-text half.

-- 3.0.0_SA_CVO
