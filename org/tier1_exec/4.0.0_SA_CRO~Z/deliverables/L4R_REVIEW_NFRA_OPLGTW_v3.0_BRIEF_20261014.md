# L4-R review -- NFRA_OPLGTW v3.0, BRIEF half (4.0.0_SA_CRO~Z, 2026-10-14 ~13:2xZ)

**archetype:** VALIDATE

- **Reviewed:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` @7878037d98, half `brief`, half_hash 7d8e4e9db877.
- **Delivery:** 1.0.0_SA_CTO~Z msg 34074 (L4-R) and 34076 (the ask to sign against G1).
- **Reviewed against:**
  - (a) the brief_ref `ANDREW_DIRECT_20260914_1511ET_NFRA_OPLGTW_D9_REGISTRATION_AND_PRD.md` @45ce4e5b73, unchanged since the last signed brief half;
  - (b) the v3.0 input, `GATEWAY_DATA_CONTRACTS_20261014/G1_harvest.md` @0d7c29b3c5.
- **Method:** every line cited below was read by printing the bytes at `git show 7878037d98:<path>`; nothing was grepped for its quote.

## Verdict: SIGN, with two corrections for the CTO to carry at the G1 cut

The half went STALE only because the ENDPOINT hash moved when FWD-22 was added.
- BRIEF COVERAGE (lines 473-492) is unchanged and still maps the brief's 10 of 10 level-2 headings at its pin.
- FWD-22 (lines 276-295) and the v3.0 addendum (lines 1091-1122) carry G1's content into the consuming cells.

| G1 content | carried at | verdict |
|---|---|---|
| answer envelope: `as_of`, `source_keys[]`, denominator, `absent_reason` | :279-280 | carried |
| 50 KB default projection (G1 section 3; assessment D6) | :287 | carried |
| freshness in trading days | :288 | carried |
| admission through the Opal-users gate before any read; `harvest_read.admit()` + audit row | :285, :1101-1102 | carried |
| every new S3 / Lambda / DynamoDB read is a never-widen act; the Lambda invoke has its own ask | :285-286, :1108-1110 | carried |
| no Bloomberg call; bronze read from the bucket only | :1111-1112 | carried |
| the 10 typed tools to build; `harvest_describe_dataset` folded into `opal_describe` / `opal_discover` | :1101-1107 | carried (the fold is a CTO ruling; it agrees with one-carrier, no second registry) |
| retirements: publication-links, publications; the hyphen dossier only after the cell reads supersession | :1113-1115 | carried, and it keeps G1's `inferred` claim |
| **newest-part-only read for the snapshot tables (assessment D1)** | **pointer only ("G1 section 3", :1101)** | **correction 1** |
| **`data_status` surfaced; 0 articles never reads as "no chatter" (D9); CUSIP answers `not_held` (D4)** | **absent from the PRD** | **correction 2** |

## Corrections (by pinned line; each is CONTRACTS-side text, so the ENDPOINT hash does not move)

1. **PRD@7878037d98 :1101-1104 (addendum item 1).** Add one clause.
   - The clause: `chatter_daily`, `article_security_mention` and `chatter_window` are read from the NEWEST part file of the newest date partition only.
   - Every part is a full snapshot:
     - newest chatter_daily part 68,002 rows vs 1,338,296 across all parts;
     - newest mention part 52,424 vs 459,334, both with 0 duplicate keys in the newest part.
   - A cell that reads the prefix, which `harvest_list` + `harvest_read` invite, multiplies counts about 9x and 20x with no error.
   - This is the one guard whose absence returns a plausible wrong number. It belongs in the worker face, not behind a link.
2. **PRD@7878037d98 :1101-1104, same item.** Add two clauses:
   - `harvest_get_chatter` returns `data_status` per day and never presents 0 articles as no chatter. On the newest day, 174 of 242 names read DENIED and 68 PARTIAL.
   - `harvest_resolve_security` answers a CUSIP query `not_held`, never `none`. CUSIP is held in 0 of 18 Parquet tables; ISIN only for 65 names.

Neither correction re-opens a half by itself. Both are cheapest at the COO's G1 cut (`2.0.0_SA_COO~O`), where the worker face is written.

-- 4.0.0_SA_CRO~Z
