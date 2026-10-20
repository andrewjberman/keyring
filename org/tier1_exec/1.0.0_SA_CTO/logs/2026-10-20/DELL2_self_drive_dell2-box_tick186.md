# /self-drive dell2-box -- ticks 185-186 (2026-10-20 ~19:26Z-20:27Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 185 and 186, since the tick 184 log (@8c04d53a9b). state: ARMED.

## The two PDF routes

- **AR-y-470**, drained @d8497f8adc: the commentary PDF route binds by logical id and signs the PDF's own sha (the run 7c R
  cause).
- **AR-y-471**, drained @ee2c94f553: an offline trace through the real Opal writers. RESULT FAIL: `opal_producer.py:600`
  never writes `release.protected_pdf_ref`, so `/pdf` refuses `ANALYSIS_PDF_NOT_RETAINED` for every Opal report
  (`owned_report.py:321-322`).
- **Ruled** (msg 19:57Z): fix the route side in the same irpt-status release if the artifact resolves; otherwise fix the writer
  in r34o.
- **AR-y-472**, drained @06cb0e999d: "the Overview PDF route resolves the retained Opal PDF". This is the route-side option.
- **Next:** `~Y2`'s code-only irpt-status release packet carrying AR-y-470 and AR-y-472. The CTO half signs it, then run 7d reads
  both routes and saves Andrew's FWD-9 sample.

## Cross-box: the OPAL_ASSETS inf mirror (laptop CTO msg 110004, relayed by MSTR)

- **Finding** (laptop's measurement): since 2026-10-18 the mirror raises MirrorRaise ALIEN SURPLUS on
  `opal-data-assets/orion/inflection/bronze/scope_account_returns/date=2026-10-16/scope.json.gz`. The writer is IRPT_BCKEND's
  Scope feed, which takes its bucket from INF_B_00's `S3_BUCKET`.
- **Ruled** (reply via MSTR 20:18Z):
  - no mirror carve-out;
  - the feed is re-pointed to the source `opal-data-inf` at a builder address (rule 30);
  - the feed is FROZEN (no `--upload`) until then;
  - the stray key is real Orion data, so its delete stays with Andrew (the laptop CTO is asking him).
  - The re-point goes into IRPT_BCKEND's next round, behind Andrew's no-performance-until-Fidelity hold.

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.
- **The stray Scope key in `opal-data-assets`** (real data; S3 delete, CLAUDE.md Agent Autonomy). The laptop CTO carries it.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
