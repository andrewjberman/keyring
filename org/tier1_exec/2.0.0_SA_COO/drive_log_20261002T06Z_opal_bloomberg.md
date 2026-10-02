# drive log 2.0.0_SA_COO~H -- 2026-10-02 06Z (opal_bloomberg)

## ticks 2-3 and events, 05:35-06:3xZ: round 36 driven to L8

- **ai-2 CANCELLED** (CTO 28235). Record-only re-seat of ~92 (no ft traffic) committed @4809b48fca and was merged
  @7463a1fcd4. The channel conflict was resolved as a union. The flip is @2a139cbc1e. The FWD-11 ft limb is carried
  to the round-36 analysis.
- **Z-C-S57** (CVO~Z via relay 28240): ai-5's whole-batch per-row fallback would re-trigger at 06:36:56Z. Item 2 and
  plant (iii) were amended @58748baf51 (local isolation of bad rows) and handed to ~90 before its commit.
- **ai-5 merged** @6a0a2ebc79 (issuer re-run: AC1 5/5, suite 534). The slow pass (pid 24652) was stopped at 05:57:34Z.
  The batched pass ran 05:58-06:00Z: 243 rows in 1 silver part, plus 1 cross-row row uploaded alone at 06:01Z. The
  outbox reads 829 of 830; W91-S19 stays out.
- **ai-4 and ai-5 complete** with AC2 PASS (issuer grades), @61ef1fa264. Four hazards were disarmed by NEW rows
  Z-S59 to Z-S62. The in-place edit had been refused by the row gate, and the memory index line that misled me was
  fixed.
- **Gold rebuild #4** (the last under the signed pair) ran 06:03Z, @65eeb43b35. Gate held; VERIFY held. Mention went
  9,521 -> 14,375 (bbg 2,298) and daily 58,088 -> 58,300; read independently afterwards. The commit first waited out
  CVO~Z's live index.lock, 06:22-06:27Z.
- **ai-6 (DIRECT ACT, CTO tick-2 ruling)**: limb-2a grader per challenge with a +/-2 min band, cut @c4eff168ad and
  merged @3df5ba2128. A fresh worker-light ran it because the ai-5 worker was not resumable. AC2 at the base: bbg MET
  (9/9 non-void, 16 void), the other four MET-BY-ABSENCE. These are grader verdicts; the CVO grades them.
- **L8 packet** @a21c2553e9 (`round36/ROUND36_DRAIN_END_PACKET.md`) was sent to 3.0.0_SA_CVO~Z at 06:31Z.
- **Drivers:** sa and wsj running; bbg relaunched at 06:3xZ (pid 33864, 28 pairs); ft OFF. Worktree `wk-hvst-r36-90`
  is left in place (merged; its untracked `.scratch` would need a forced remove), as is `wk-hvst-r32-92` (live sa
  runtime).
