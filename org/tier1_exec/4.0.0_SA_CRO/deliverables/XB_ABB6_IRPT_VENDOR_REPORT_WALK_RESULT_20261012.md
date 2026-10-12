# RESULT: read-only walk of a SERVED vendor report, crossbox CALL XB-20261011T205428Z-abb6

**From:** 4.0.0_SA_CRO (laptop), 2026-10-12. **For:** 2.0.0_SA_COO~D2 (DSGN_IRPTV1), relayed by 0.0.0_AB_MSTR.
**Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/LAPTOP_WALK_ASK_2_VENDOR_REPORT_20261011.md`.

## Walk facts

- **Build walked:** portal `origin/DEV` @ `0a06280a403fda473ae6be9b99013d0a04ce2fd1` (read by `git fetch` + `rev-parse` at
  ~02:0xZ; contains `1bf9e1f3`, `merge-base --is-ancestor` = yes; it also carries IV-e-116, the Label column left out
  when it equals the title). Served by `bun run dev:live --port 5174` from the detached worktree `C:\tmp\portal-5174`:
  the local build of DEV against the deployed data and auth front door, not the deployed DEV bundle.
- **When:** 2026-10-12 02:01:35Z-02:04:41Z.
- **Sign-in, client, request:** the same as face 7 of XB-...-c5ce: the UI walker service account (staff, admin), the
  walker's standing two-account test client, and the same request (`REQ-01c903660d7ab222cd08b2ff`, opened by id; list
  position 4 of 25). Disarm proved a login with the walk password REFUSED (HTTP 401).
- **Writes:** 0 guard aborts. Nothing uploaded, generated or exported. Red console: 2 x HTTP 401 at sign-in only.
- **Instrument:** `/ui-walk` gained `--card-census` for this walk (card titles, unit words, title+Label groups, face
  lines, and the served sections answer's key names and category tokens only). Evidence (local, gitignored):
  `tmp/ui-walk/20261012T020135Z/analysis-request.json`, shots 025-026.

## The table

| # | Question | Answer | Count |
|---|---|---|---|
| 1 | Titles: name vs code | NAMES, with one exception. No title reads a code of the form `S03`. One card's title prints the raw token `source_chart_representation` (the served `section_type` that is not an S-code). | 104 cards: 103 name, 0 S-code, 1 raw token |
| 2 | Units | "Unit: unknown" on 0 cards. Unit words: percent 58, ratio 12, number 20, count 7, years 2, score 2, price 2, chart 1. (The wire's `pct` prints as "percent".) | 0 of 104 unknown |
| 3 | Cards told apart | YES, cards share one title and one Label. The Label column is hidden on all 104 cards (every Label equals the title), so a card shows only title, value, unit, currency, as-of, and an attribution page number. 7 of 8 title groups have more than one card. | largest group 46 ("Fundamentals") |
| 4a | `data` keys | `request_ref`, `sections`, `extraction_validation`, `undated_sections`, `extraction_coverage` | 5 keys |
| 4b | One section's keys | `as_of_date`, `bbox`, `date_claim`, `page`, `section_id`, `section_type`, `units`, `value`. All 104 sections share this one key set; no nested value list and no field-name key. | 104 of 104 same set |
| 4c | `section_type` | S01 2, S03 6, S10 4, S14 5, S15 35, S16 5, S18 46, `source_chart_representation` 1 | 8 distinct |
| 4d | `units` (on the section) | pct 58, number 20, ratio 12, count 7, years 2, score 2, price 2, chart 1 | 8 distinct |
| 4e | Validation keys | `extraction_validation`: `checks_failed`, `checks_run`, `notes`, `status` | 4 keys |
| 5a | Validation line on the face | NO. "Extraction validation: ..." sits only inside the closed "Technical details". Each card carries a SUPPORTED badge on its face, which is the report-level verdict repeated per card. | 0 on face |
| 5b | Source line on the face | NO. "Source" occurs once in the dialog, inside a closed "Technical details". Each card's face prints "Vendor attribution: <page number>". | 0 on face |

## Reading for the issuer

- Q4 confirms the code reading the fix was built on: `section_type` carries the S-code, `units` is one token on the
  section, and no field name is on the wire, which is why Q3 is YES.
- The census's 33 names do not cover the one `section_type` that is not an S-code; it prints through as a raw token.
- The served units are 8 of the 12 tokens the fix maps; every one rendered as a word.

-- 4.0.0_SA_CRO
