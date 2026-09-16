# CTO ADJUDICATION -- AMGT_RESAPP, /self-drive tick 2 (2026-09-15 ~20:2xZ)

**Adjudicator:** `1.0.0_SA_CTO~W`, on Andrew-direct ~19:3xZ (@`2ac5611057`, "you adjudicate"). **Scope:** AMGT_RESAPP.
**New input since tick 1:** `4.0.0_SA_CRO~W`'s Lusha v3 reference review @`ecfe46465e` (delivered 20:03:03Z after its heartbeat was
restored), which answers tick 1's card 2.

```
OPEN CALLS -- AMGT_RESAPP -- 1.0.0_SA_CTO~W, /self-drive tick 2 (1 new call, ADJUDICABLE; the 2 RESERVED cards of tick 1 stand at Andrew)

+-- CALL 15 ---------------------------------------------------------+
  **Is Lusha a source for executive tenure at all?**
  Lusha's Enrich Contacts reference (docs.lusha.com/apis/openapi/enrich/enrichcontacts): "Omit reveal to get both by default" (emails and
  phones); no documented position-only request; `previousEmployment` carries company and title with NO documented start or end dates.
  --------------------------------------------------------------------
  **REC --** No. Close the Lusha route for tenure under the documented contract; the companion tenure metrics come from filings only.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) The one Lusha enrich authorized ~19:0xZ is NOT run: the documented request cannot exclude emails and
  phones, and the documented response carries no employment dates, so it could return neither the safe shape nor the needed field.
  `exec_company_tenure_avg_years` and `exec_role_tenure_avg_years` come from filings -- the proxy statement's executive biographies and
  the annual report's officer section (10-K, 20-F) -- and are ABSENT with reason where the filing does not state the date. The headline
  (`exec_mgmt_tenure_avg_years`, Bloomberg) is unaffected. No message to Lusha is sent from this ruling. Answer to Andrew's ~18:2xZ
  question ("how reliable lusha is in getting exec manager info and if the information is parseable"): prospecting matched 11 of 48
  filing officers with 4 titles right and no dates; the enrich contract documents no dates; so Lusha is not a tenure source.
+---------------------------------------------------------------------+
```

Ledger row appended to `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/ctoW_AMGT_RESAPP/VERDICTS.jsonl` (tick 2). Push state: LOCAL.
