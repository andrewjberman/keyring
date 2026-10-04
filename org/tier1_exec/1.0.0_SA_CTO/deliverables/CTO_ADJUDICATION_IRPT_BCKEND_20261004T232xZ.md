# CTO ADJUDICATION -- IRPT_BCKEND, 2026-10-04 ~23:2xZ (`/open-calls --adjudicate` mode, Andrew-direct 2026-09-03)

On `3.0.0_SA_CVO`'s outcome grade at portal PROD c69b4747 (msg 105019,
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_OUTCOME_GRADE_PROD_c69b4747_20261004.md` @c860c50818): **0 of 12 REALIZED.**
The grade puts one ENDPOINT question to this seat. Two of its blockers are acts only Andrew can do; they are listed for him at
the end, not ruled here.

+-- CALL 1 of 3 ---------------------------------------------------+
  **Does FWD-3 still promise a no-flow holdings figure on 49 Financial's page and PDF? (a) amend FWD-3 to Inflection and Cottonwood, with 49F's figure held by IRPT_DASHBD; (b) keep it**
  49F now serves IRPT_DASHBD's flow-adjusted total return (PATH B, on Andrew's P-2 promote word). Batch 178 already says IRPT_DASHBD
  FWD-1, FWD-2 and FWD-8 hold the Performance outcomes.
  --------------------------------------------------------------------
  **REC --** (a). Two outcomes cannot both own 49F's served figure, and Andrew's own promote moved it.
  --------------------------------------------------------------------
  **RULING -- (a), because:**
  - his 2026-09-30 word narrowed the 09-28 holdings-only ruling for IRPT_DASHBD;
  - his "1 yes today" promote put that figure on 49F's page;
  - FWD-3 as written can never be realized at 49F again.
  FWD-3 is AMENDED IN PLACE (id unchanged, PRD v0.26). It now reads per firm whose page serves the holdings basis: Inflection and
  Cottonwood.
  - **Capability no longer promised:** IRPT_BCKEND does not put a holdings-basis figure on 49F's rendered view or PDF.
  - **Kept:** IRPT_BCKEND still produces 49F's holdings-basis gold every trading day (FWD-12) as IRPT_DASHBD's guard rail
    (C-GUARD), and the 09-28 no-flow constraint still binds Inflection and Cottonwood.
+---------------------------------------------------------------------+

+-- CALL 2 of 3 ---------------------------------------------------+
  **`~P`'s orders tag export and Analysis-export hops `FWD-9`, which the ratified ENDPOINT gives to email intake. Re-key?**
  The grade's finding 5. An outcome-driven analysis cannot read work tagged to the wrong outcome.
  --------------------------------------------------------------------
  **REC --** Yes. Every new order's `outcome_ref` cites the ratified FWD.
  --------------------------------------------------------------------
  **RULING -- yes, from the next issuance.**
  - The map: export of a branded report is FWD-8; a report and export at a second firm from the global view is FWD-11; the
    Analysis export is FWD-4; email intake is FWD-9.
  - Past orders are not rewritten: their records stand, and this record is the key that reads them.
+---------------------------------------------------------------------+

+-- CALL 3 of 3 ---------------------------------------------------+
  **Where do the grade's two new rows go: S324 (the READY PATH B export carries neither ref ADDENDUM v0.24 requires) and S238 (directory foreign-firm read, disarm owner this seat)?**
  --------------------------------------------------------------------
  **REC --** Both go into `~P`'s round-47 E2 list.
  --------------------------------------------------------------------
  **RULING -- both into `~P`'s E2.**
  - **S324:** a performance export's bundle carries its narrative packet reference (FWD-8 needs it). If PATH B exports
    legitimately carry no narrative yet, the v0.24 contract row is amended to admit that by name; the code is never left
    disagreeing with the contract.
  - **S238:** this seat holds no principal to read with. `~P` runs one foreign-firm request against the DIRECTORY route on
    deployed bytes, and this seat clocks the disarm on that read.
+---------------------------------------------------------------------+

## Acts only Andrew can do (listed, with citations; not ruled here)

- **The PROD gate.** `/investor-reporting` is admin, internal and Dev only on PROD (App.tsx :105, :460, his 2026-09-22 word "marked
  in tsx for admin and isDev only"). FWD-1, FWD-2's advisor arm and FWD-5's page walk need a firm advisor on PROD. Lifting a hold he
  set by name is his.
- **The directory refresh (row S323).** It has failed at 49F and INF since 09-29 (HAND_OVER_RUNNER_OFFLINE). The runner
  i-02448edb624a7a7cf was stopped "User initiated (2026-10-04 16:41:18 GMT)". Restarting or re-routing a data-engineering runner is
  his directive (his 2026-10-03 ~17:3xZ word: "inappropriate for agents to adjust our data engineering operations without my
  explicit directive").

Recorded by `1.0.0_SA_CTO` and broadcast the same turn to `2.0.0_SA_COO~P`, `3.0.0_SA_CVO` and `0.0.0_AB_MSTR`.

-- 1.0.0_SA_CTO
