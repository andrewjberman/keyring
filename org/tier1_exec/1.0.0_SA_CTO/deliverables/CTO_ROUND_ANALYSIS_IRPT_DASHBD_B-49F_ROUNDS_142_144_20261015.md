# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): rounds 142 and 144 (2026-10-15 ~23:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v113 (r142) and v114 (r144). Round 143 (DB-b-276) is pending, so no packet is owed for it.
**No PRD addendum.**

## Round 142: contract 0.4.2 passes L9
- **Both of my orders are MET:**
  - round 124 item 2: `market_value_eod_claim`;
  - rounds 138-141 rulings 1-4: `VENDOR_REPORTED` out, Orion TWR, provenance as a text map in `source` with its test.
- v108's (iii) FAIL is cured. The rule-24 record and token census are present.
- **The B-IN adapter's "done" gate is met.**
- The one-drain rule binds from its issue time (22:40Z) onwards. Not a FAIL here, as the CVO reads it.

## Round 144: the disclosure placeholder (Andrew's 90ef word, "placeholder for now")
- The code authors exactly one text, "Disclosure page pending", with the sheet title "Disclosures". There is no invented disclosure
  language, and that is correct.
- **The criteria FAIL on the landed tree, because the code lives only in the portal candidate.** The CVO passed them on a scratch worktree
  of the candidate. So:
  1. `~D2` re-points the criteria to run against the candidate's tree, named by commit, until it merges. A criterion that reads the
     wrong tree is not a grade.
  2. **A render check is owed before this candidate merges:** print the 49F report from the candidate (its own dev port, or the render
     host under its pair) and read the last sheet for the exact placeholder text. Its criterion is owned by `~D2`, alongside the
     default-report work (`~F2`, FWD-21).
  3. **The candidate stays unregistered until that check passes.** The default report is CLIENT-FACING, so its PROD promote waits on
     Andrew's word, as the client-facing approval the CRO's brief lists.
- **The guard narrowing is refused as built.** Dropping "advisory fee" from the scan narrows a guard for everyone. Restore the term and
  add a one-label exemption for the single existing label, named by its file and line (CVO v114). A tighter guard, not a looser one.

**Next for `~D2`:** round 143 (in flight), then the re-pointed round-144 criteria, the render check and the guard repair as ONE issuance.

-- 1.0.0_SA_CTO~DELL2
