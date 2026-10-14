# ANDREW_DIRECT 2026-10-14 ~19:xxZ -- check whether the Black Diamond report is parsed page by page with an Opal replacement; if not, do it and fold it into IRPT_DASHBD

**Channel:** Claude Code terminal, dell2, to `4.0.0_SA_CRO~DELL2A`. **Recorded by:** `4.0.0_SA_CRO~DELL2A`, same turn.

**Andrew, verbatim:**

> "Something I want you to do is check to see if we have already parsed this document page by page end to end and figured out
> how to replace it with our own data/calculations: C:\Users\Test\Downloads\17752262.pdf. Being able to generate an export version
> of this and a visual represenation in the performance tab is of peak importance, arguably the number one most important thing on
> this box. I want to establish first if this has already been done, and if so, if that is already approved and folded in to
> IRPT_DSHBRD workstream. If not, you need to do it now and make sure that gets folded in."

**Reading:** "IRPT_DSHBRD" is read as `IRPT_DASHBD` (the Performance tab project on dell2, which absorbed IRPT_CUSTDY on
2026-10-09). The PDF is the Black Diamond 49F report taildropped on 2026-10-08
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_221xZ_BD_REPORT_AND_TEMPLATE_SCREENSHOT_TAILDROP_TO_DELL2.md`).
It is client data: it stays outside the repo, and only names, structure and counts are committed.

**Finding (read by `4.0.0_SA_CRO~DELL2A`, same turn):**

- **Same file.** `17752262.pdf` has the same SHA-256 (`ae08e100...43ffb`) as the CTO's private baseline copy
  `C:/dev/_irpt_private_evidence_20261009/bd_baseline/BD_49F_FINANCIAL_PERFORMANCE_REPORT_20261007.pdf`.
- **Parsed.** The CTO read the text of all 32 pages into a section/table/column schema:
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`.
  IRPT_CUSTDY's earlier field map (`BD_FIELD_MAP_CU-g-3`) covers the same 32 pages.
- **Replaced with Opal sources.** `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` 0.4.3 has 117 members, one per
  baseline cell. 104 name an Opal gold source and 13 are ABSENT:
  - 10 household-grain returns: the Portfolio Value Summary "Return (Cumulative)" over 4 windows, and the Holdings Overview
    returns over 5 windows plus MTD net gain;
  - 2 cover fields (household name, account list);
  - 1 disclosure page (waits on Andrew's call a252).
- **Approved and folded.** This is IRPT_DASHBD FWD-21 in PRD v0.14 (RATIFIED; both L4-R halves signed). 34 FWD-21 orders ran
  in rounds 94-109, all complete. Round 110 is open: DB-b-217 is pending; DB-b-222 and DB-b-223 are staged.
- **Not done yet:** FWD-21 is not graded REALIZED. The renders are private and local only, and no FWD-21 portal commit is on DEV.
  The first Inflection render was graded J1 FAIL on 4 counts. Cottonwood waits on a scheduled performance producer.
- **The gap no cell covers:** the 49 Financial (and Cottonwood) HOUSEHOLD return. Round 110 sources it for Inflection only,
  from Orion's client grain. The contract's own remedy is "a household daily return series built the way the account series
  is built, as a new contract", and no order cuts it.

**Priority:** Andrew calls this "arguably the number one most important thing on this box". That is his word to this seat; it is
relayed to `1.0.0_SA_CTO~DELL2` by this record's path, not adjudicated here against the 14:73xZ four-priority record.
