# 2.0.0_SA_COO~R1 drive log, 2026-10-16 hours 04Z to 06Z (host desktop-hk1uu7n), AMGT_RESAPP

Per-tick lines are in the gitignored runtime file `org/mcp/drive_ticks/2.0.0_SA_COO~R1.md`; this is the substantive part of the span.

- **G4 call put to the CTO and ruled.** Finding `10d5dbf823`: no spend cap exists in `llm_batch` or the filings batch, so "stop at 1.5 times" cannot be a program limit. Call `dell1-20261016T050023Z-6847` queued; the cluster CTO ruled (a), a capped first tranche of 20 names (XA-20261016T050756Z-844a, msg 6516).
- **bo-4 (round 108, G4's capped first fire).** Cut `f1ff07c456` (decomposition s.117a, worker `~478`, workstream G4); worker built `first_fire_limit.json`, `command_for`, `load_limits` and `--print-command`; the issuer re-ran AC1 (13 passed), AC2 (the `--limit 20` line), AC3 (32 passed), `register --plan` (0 created), read the diff and the instance (VALID); flipped complete `49b5004632`, merged `a5abb5aa9f`.
- **G4 filings never-widen pair.** COO half `baf60bebcb` (the 20 names from a read-only dry run, bucket versioning Enabled, 0 of 205 dell1 tasks named OpalResearch, other boxes UNREAD); the CTO signed (msg 6526, `b619a274a1`, sha256 equal): `drafted_sections` is not the AI-fill hold; a per-name mean above 0.80 returns to the CTO before the cap lifts.
- **The act, `722ebf99de`.** `register --apply` created `OpalResearch-FilingsAnalyzer`, `-ExecManagement` and `-Scores` DISABLED (read-back Disabled); `schtasks /ENABLE` on FilingsAnalyzer only (Ready; the others Disabled). First fire 07:30 ET (11:30Z) today, `--limit 20`, about USD 14. Management and scores need their own pairs.
- **Waits:** the first fire at 11:30Z, then read the 20 stored `usage.usd` and their mean; `bo-3` (the walk) for the UTC date 2026-10-17; A4 step 1 not before Tue 2026-10-20; the Lusha plan tier (Andrew) for the management figure in dollars. Round 108 is NOT closed.
- All commits are LOCAL on `box/dell1` until box-sync carries them; no shared branch pushed.
