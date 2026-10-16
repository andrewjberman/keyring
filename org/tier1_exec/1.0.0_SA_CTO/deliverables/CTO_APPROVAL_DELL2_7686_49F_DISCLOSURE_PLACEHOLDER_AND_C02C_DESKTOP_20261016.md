# CTO APPROVAL 7686 and the c02c desktop list (2026-10-16 ~01:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**On:** Andrew's words at the laptop CTO terminal ~01:36Z, relayed by `0.0.0_AB_MSTR~DELL2` (record
`ANDREW_DIRECT_20261016_013xZ_F086_DELL1_7686_INTERNAL_CRM_MATCH_KEY_C02C_DESKTOP.md` @e27ec8628b on box/laptop). Verbatim:
- "7686 it doesnt matter if its in production because it isnt visible for anybody outside opal."
- "c02c we will get to this later i just need that list/message file on dell2 desktop."

## 7686: APPROVED
- **The row:** `dell2-20261016T001759Z-7686`, `cand/dell2/irpt-49f-report-render-disclosure-placeholder` @42a1539b, re-cut on PROD e0e69da7.
- **The class is Opal-internal on his word** (no one outside Opal can see it), so the building box's CTO approves (CLAUDE.md Portal).
- **What was read:**
  - `~D2`'s render shows 21 sheets, the last titled Disclosures, with "Disclosure page pending" exactly once
    (`RD_DISCLOSURE_RENDER_R145.json`);
  - the round-144 criteria pass on the candidate by commit (CVO v114);
  - the "advisory fee" guard is restored with a one-label exemption.
- **The promote's two-dot diff against PROD must read exactly the candidate's own files.** The DT's receipt prints it, and any other file is
  a STOP (the a00f lesson).

## c02c: the list and message are on the dell2 desktop (the call stays OPEN; no send)
- **The message:** `C:\Users\Test\Desktop\DRAFT_Inflection_Orion_account_start_dates.txt` (written 10-15).
- **The list:** `C:\Users\Test\Desktop\Inflection_accounts_missing_Orion_start_date_20261016.csv`.
  - 40 rows: every account in the reported roster (`opal-data-inf/silver/api_dims/accounts_v2/snapshot_date=2026-10-15`, 863 rows) with a
    null `account_start_date`.
  - All 40 also lack a start value and a model, which matches the round-120 erratum's measured 40 of 863.
  - Columns: account number, name, household id, custodian, status, active flag, representative, start date, start value, current value,
    model.
- **The roster-wide 96 of 3,040 are NOT in the file.** The silver snapshot holds only the 863 reported accounts. The full roster would need
  the bronze NewPortfolio pull; it is produced on request.
- **No client data is in the repo.** The downloaded roster and dimension files were deleted from the scratch folder after the build. This
  record carries counts only.
