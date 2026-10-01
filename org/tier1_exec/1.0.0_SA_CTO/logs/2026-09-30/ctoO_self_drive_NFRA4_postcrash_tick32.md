# /self-drive NFRA four -- ticks 30-32 + MX-t-13 naming call (1.0.0_SA_CTO~O, site Z, 2026-09-30 10:2xZ-11:2xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Previous log:** tick 29 @bad886ea37.

## Carried tick lines (drive_ticks)

- tick 30 10:21Z: 16 of 187 open. MX-q-3 is complete @e3c47f2cc9: `query_v0` is now the MCP tool
  `gateway_query_catalog`. 0 calls.
- tick 31 10:51Z: 16 of 187 open. MCPINDEX 6 of 80 open (r-6, r-7, s-14, t-10, t-12, t-13). 0 calls.

## Tick 32: the MX-t-13 naming call

1. **msg 27110 (2.0.0_SA_COO~MI, 10:57Z):** MX-t-13 (`blackdiamond_list_fees`) is built with AC1 and AC2 PASS, but the
   naming limb refuses its commit. COO~MI asked for a LEGACY-READ ruling. Evidence: row Z-W21-S9, @07c669e722.
2. **Governance fork pitched** to 3.0.0_SA_CVO~O at 11:01Z. The question was who issues the ruling: this seat or laptop
   1.0.0_SA_CTO. REC: this seat.
3. **Verdict, msg 27113, 11:12Z:** "1.0.0_SA_CTO~O issues it. The laptop CTO gets a copy as remediation owner, not a
   hold." Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/GOVERNANCE_VERDICT_MX-t-13_LEGACY_READ_ISSUER_20260930_O.md`
   @9c9fa60bc8.
   - Grounding: `.owned-paths.yaml:60-63` (CTO role with suffix inheritance), `naming-gate.py authority_ok()` (it grades
     the pinned record, not the seat), and this seat's MX-t-8 authority.
   - It is landed in `drive_pairs/O_fabric/VERDICTS.jsonl`.
4. **The driver's measurement, taken before acting:** the waiver cannot reach these literals.
   - `.tools/naming-gate.py:1413`: `new = pre_text is None or not _in_pre(lit, pre_text)`. A literal absent from the
     file's HEAD pre-image is NEW.
   - `:1444-1445`: NEW OUT-OF-PATTERN/ALIAS returns REFUSE BEFORE the waiver lookup at `:1446`. The code's own comment
     says a NEW literal "can never reach it".
   - Row Z-W21-S9 grades all 5 MX-t-13 literals NEW: `integration.py:51/52/56` and `blackdiamond_reader_iam.tf:30/41`.
   - Row Z-W15-S5 graded the ETF literals NEW too. So the verdict's suggested second use (clearing B3 in the same sitting)
     does not apply.
5. **Ruling:** MX-t-13 joins B3. Both go to Andrew as one R20 acknowledgement (CLAUDE.md rule 30). COO~MI holds MX-t-13
   and MX-r-7 built and stops the waiver-syntax restructure.
   - Sent to COO~MI and CVO~O (msgs 27114 and 27115).
   - The CVO verdict on the issuer stands. Only its mechanism does not reach these literals, so there is no disagreement
     on the ruling it made.

## Measured (11:2xZ)

- **Inbox:** 0 unread.
- **Open TOs:** 16 of 187.
  - NFRA_OPLGTW 4 of 54.
  - NFRA_OPALAI 4 of 35.
  - NFRA_MCPORTAL 2 of 18.
  - NFRA_MCPINDEX 6 of 80.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE (acts per the tick-11 log).

## Acts only Andrew can do (each cited)

- **One R20 acknowledgement covering two served legacy keys** (CLAUDE.md rule 30: "a deliberate departure is an R20
  register entry Andrew acknowledges"):
  - (a) `opal-data-portal-v2` `platinum/etfs/positioning_data.json` at MX-t-10's new sites (B3);
  - (b) `opal-data-bd` `silver/fees/` for MX-t-13 and its release MX-r-7.
  - Both keys are where the data lives today, and each has an open migration (ADVI_FIRMBKTS for bd; none yet for etfs).
- **Widen one existing Schwab grant to `dim_transaction`** (his admission, FWD-9, per ruling B2).
- **MX-t-12:** lifting his NOT YET on platinum/advi, a hold he set by name.
- **Unchanged:**
  - G-ACCT step 5;
  - MCPORTAL G-2ND and G-CLOSE;
  - OPLGTW G-D and Part D;
  - NFRA_MCPMSP G-USER, G-IT-INF, G-ADVISOR, G-FIRM and G-KEY.
- G-C is external, at Opal IT.

## Compiler Tools

- `.tools/naming-gate.py` read at `:1413`, `:1440-1470` and `:1479-1483` (the NEW test, the waiver consumption point,
  `_in_pre`).
- `git show 07c669e722` (row Z-W21-S9, with the gate's verdict lines).
- Last-tag `<status>` census over the four projects' task-order files.
