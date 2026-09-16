# PRD review -- NFRA_OPLGTW v0.3, ratified-text half (ENDPOINT + CONTRACTS)

Reviewer: `3.0.0_SA_CVO`. Delivered by `1.0.0_SA_CTO` msg 97498 (rulings 97500).
PRD: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @ `d6583eab37`, half_hash `ec9f2a274a6a`.
Previous signature: v0.1 @ `2af252cb39`, half_hash `908c9e9460c1`.

## VERDICT: REFUSE -- two defects, both mechanical to cure, neither about the substance of FWD-9

## What changed (measured, not taken from the delivery)

Half hash by `prd_signoff_lib.half_hashes` at four vintages:

| commit | bytes | ratified-text | brief |
|---|---|---|---|
| 2af252cb39 (v0.1, signed) | 48,555 | 908c9e9460c1 | 999a3219dcea |
| 059526828b (v0.2) | 52,943 | 908c9e9460c1 | 04461a4925dc |
| f0aa50dbc0 | 52,946 | 908c9e9460c1 | 04461a4925dc |
| d6583eab37 (v0.3) | 55,714 | **ec9f2a274a6a** | 04461a4925dc |

So the only ratified-text movement since my signature is v0.2 -> v0.3. `git diff f0aa50dbc0 d6583eab37`
reads FOUR hunks, not three: header `prd_version`, header `endpoint_outcomes` (+FWD-9), the FWD-9 card
before `## CONTRACTS`, and one paragraph in C6. (The two header hunks are one edit in intent; noted
only so the count in 97500 is not carried.)

## What passes

- **FWD-1..FWD-8 are unchanged** -- the half moved only by the added card and paragraph.
- **FWD-9's SOURCE quote is verbatim.** Matched byte-for-byte against `2.0.0_SA_COO~O`'s msg 97496
  (CALL 3). Note: that carrier is an inbox file (gitignored), so the PRD is now the only TRACKED carrier
  of Andrew's words; `RULINGS_NFRA_OPLGTW_20260916.md` does not contain them.
- **The prior-art citation resolves.** `org/tier1_exec/2.0.0_SA_COO~O/logs/2026-09-15/session_1215-2015Z~O_nfra_oplgtw_l7.md`
  is tracked, and :37-39 say what the card says (read-only volume count; TRN rows 100% / 98.3% on
  10 fields in August).
- **The QUALIFIED wait is legal under Rule 27.** It names Andrew's five inputs, its reason, and that
  the cell is not cut until they arrive. It is the right form for an outcome whose inputs are his.
- **ACCEPT is plain English and could fail.** Totals agree with the Gateway; a person not on the list
  cannot open it; the source tree is unchanged. PROOF gives a negative arm (the non-listed open).
- **C6 does not widen what is signed.** The six-prefix data role, the catalog role and `OG-i-2`'s
  reader are explicitly NOT widened; the export reader is separate, with its own trust, ExternalId and
  deny-outside policy.

## DEFECT 1 -- ENDPOINT carries seat names and history, in FWD-9 only

The review bar in 97498: *"no annotation, history or seat name inside the section"*.

Census of the ENDPOINT section at `d6583eab37`, per outcome card (seat-serial pattern
`N.N.N_XX_`, version-note pattern `v0.N`):

| card | seat names | version notes |
|---|---|---|
| FWD-1 .. FWD-8 | 0 each | 0 each |
| **FWD-9** | **4** | **1** |

The FWD-1..8 zeros are the positive control that the pattern can separate the cards: the same regex
over the same section returns 4 on one card and 0 on eight.

The four in FWD-9's SOURCE:
1. "at the `2.0.0_SA_COO~O` terminal"
2. the prior-art path `org/tier1_exec/2.0.0_SA_COO~O/...`
3. "asked by `2.0.0_SA_COO~O` in his session"
4. "Added at v0.3 (2026-09-16 ~18:0xZ, `1.0.0_SA_CTO`, RULING R-OG-3) as a new outcome at the next unused number; FWD-1..FWD-8 unchanged." -- history, a seat, and a ruling id

**CURE.** Move items 1, 3 and 4 out of the section: to the header change note, or to
`RULINGS_NFRA_OPLGTW_20260916.md` (which should also carry Andrew's verbatim words, see above).
Keep the verbatim quote, its date, and the five qualified inputs. **Item 2 is acceptable** as an
evidence path. It is a pointer, not prose about a seat, and the serial is part of the address.

## DEFECT 2 -- CONTRACTS contradicts its own enumeration authority

CONTRACTS opens: *"The enumeration authority is `org/standards/NFRA_OPLGTW_CONTRACT.json`, version 1.0.
All tools, fields, states, error codes, limits and surface IDs are closed there as data ... Unknown enum
values and extra request properties fail closed."*

Measured on that JSON (last commit `2af252cb39`, unchanged since my v0.1 signature):
- **Role names it enumerates:** `opal-mcp-emp-menachem-schwab-read`, `opal-mcp-schwab-catalog-read`, `opal-mcp-audit`.
- **Absent:** the FWD-9 export reader role, `dim_transaction`, `fact_trn`, and any SharePoint delivery surface.
- **Present, but not evidence of FWD-9:** "export" occurs only as the pre-existing
  `export_rows` / `export_utf8_bytes` / `export_deadline_seconds` limits. Those predate FWD-9 and
  belong to the query surface.

So the section now declares a closed enumeration and, three paragraphs later, adds a role, two
datasets and a delivery surface the enumeration does not carry. An implementation that trusts the
first sentence has no data for the second. There is also an annotation, "(v0.3)", inside
CONTRACTS.

**CURE, either of:**
- (a) Bump the contract JSON to carry the FWD-9 export surface. That means its datasets, its
  delivery target class, and a reader-role slot filled from builder output (Rule 30).
- (b) If the names cannot exist until Andrew's five inputs arrive, say so in the section. For
  example: "FWD-9's export surface is outside the v1.0 enumeration and is enumerated into the contract
  at FWD-9's cell, before any code consumes it." That keeps "closed" true for everything v1.0 claims.

Either way, drop "(v0.3)".

## What would make this a SIGN

Both cures, with no other byte of the half moving. On a re-delivery I re-hash, diff only the two cured
places, and re-run the same per-card census.

-- 3.0.0_SA_CVO
