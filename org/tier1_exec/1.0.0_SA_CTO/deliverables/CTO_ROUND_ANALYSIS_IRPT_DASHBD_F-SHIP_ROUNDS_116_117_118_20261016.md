# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): rounds 116, 117 and 118, graded after an unseen close (2026-10-16 ~01:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v118 (r116), v119 (r117) and v120 (r118). All are MAY-CLOSE: the criteria pass on their candidate heads
(e23ddb8e34, 0d58fe2c43 and 65f2e5430b).
**No PRD addendum.**

- **Nothing was promoted while unseen.** None of the three heads is on `origin/DEV` or `origin/PROD`, so no client-facing change escaped
  Andrew's word.
- **The criteria FAIL on the landed tree,** because the code lives in portal candidates. As for `~D2`'s round 144, `~F2`'s criteria read
  the candidate by COMMIT until it merges. A criterion that reads the wrong tree is not a grade.
- **W505-S1 (the server demanded version_id, sha256 and size)** is resolved in repo code: `freeze_filled_report` calls
  `server_pinned_body` (`retained_export.py:450-452`; `~P2`'s IB-pr-563/566).
  - **That server is not deployed yet,** so a client-only export would be refused live.
  - The deploy is `~S2`'s, under the handover of the export serve path.
  - `~F2`'s export candidate does not promote before that deploy reads live.
- **Rows D2-S102 and D2-S103 lack "disarms when" lines (CVO v120).** These are the conditions, adopting the CVO's suggestions:
  - **S102 (FWD-3)** disarms when a SERVED series carries the class keys through the route.
    - The producer is the existing one (my F-SHIP r119 ERRATUM @135366f9f7 settles v120's "premise conflict": `account_class_daily`
      contract 0.1.0, its producer and its applied release are the ones in use).
    - `~D2` adds the class keys and publishes them; `~F2` reads them on the tab.
  - **S103 (FWD-5)** disarms when the transaction contract and its per-firm producer land with their L9 (after the search my erratum
    requires shows none exists).

  `~F2` appends a row for each that carries its "disarms when" line. Rows are append-only.
- **The three closed-without-packet rounds are now graded.** From here on, `~F2` writes a packet at every drain: L8 cannot grade a round it
  cannot see.

-- 1.0.0_SA_CTO~DELL2
