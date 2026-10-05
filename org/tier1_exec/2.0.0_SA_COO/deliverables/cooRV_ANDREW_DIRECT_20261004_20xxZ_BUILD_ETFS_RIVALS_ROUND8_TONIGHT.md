# ANDREW-DIRECT 2026-10-04 ~20:5xZ (16:5x ET) -- build ETFS_RIVALS round 8 tonight

**Channel:** Andrew at the `2.0.0_SA_COO~RV` terminal (site Z), in session.
**Verbatim:** "yes, build round 8 tonight. I am smoking the page now"

**The question it answers** (this seat, the turn before, verbatim excerpt): "Say yes or no to building round 8 tonight.
If yes, I start workers now on the five drafted fixes ... Nothing goes live early. Code lands after the 07:00 ET
Bloomberg pull Monday and deploys after the 09:30 ET grades."

**What it changes:** the round-7 analysis (`ledger/ROUND_ANALYSIS.round7.md` @115645c4b4, section 3) deferred the ONE
round-8 issuance until after the 2026-10-05 grades. Andrew's word issues the drafted cells now as round-8 workstream A
(`dt-1`, `an-1 -> rw-1`, `rp-1`, `lg-1`; draft `deliverables/2.0.0_SA_COO~RV/round8/DECOMP_DRAFT.md`). The enrichment list's
item 3 (what the 10-05 grades leave open) follows as workstream B after the grades.

**Bounds stated in the question, carried as conditions:**
1. No merge into CLOUD before the 2026-10-05 07:00 ET (11:00Z) vehicle pull has run (the vehicle runs the CLOUD tree;
   lg-1 touches `collector_bloomberg.py`).
2. No Lambda deploy before `3.0.0_SA_CVO~RV` grades sa-1 J1 and ui-5 on the served 10-05 page (13:30Z), so the first
   unattended scheduled run stays the discriminator.

**Also in the same line:** Andrew is doing the signed-in read of mcp.opalinvest.dev/rivalfunds (FWD-1 / RFW-U19) now.

Recorded by `2.0.0_SA_COO~RV`.
