# /self-drive dell2-box -- tick 155 (2026-10-20 ~04:57Z-05:29Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** tick 155, since the tick 154 log (@434a07f6c6). state: ARMED.

## Andrew's fresh-report verify: PASS

- **Run 5D** (IB2 msgs 11210 and 11215; receipt `irpt_anlreq_commentary_e2e5d/A_E2E5D.txt`) is RUN-DONE PASS at 05:02Z.
  - Read here: R0 root `0485393f3a-r34l` active.
  - The allow-listed principal took the Opal producer; READY 25 s after submit.
  - R2: `n_sections=3 value=1 not_available=2 builder_only_without_value=0 not_in_this_version=0`.
- **The report to Andrew** is `REPORT_TO_ANDREW_425_CARDS_FIX_LIVE_AND_VERIFIED_20261020.md` @ad01c07f93; its path went to MSTR for ms.

## Rulings and acts

| item | ruling / act |
|---|---|
| ADDENDUM 8 (run 6, the unseeded staff filing that grades FWD-1) | CTO half SIGNED @95404e7e5a; the binding was corrected @bb3d307f29 to blob 09f6fa2997, sha256 1f43ae0c (the diff from fbb1c8398a was read: r37 v2 CodeSha256, and the staff user off the allow list). It starts only after r37 v2 and r34m v2 close green. Vendor producer at P1 means STOP. |
| r34m v2 sequencing (`~Y2` msg 11212) | Proceed. The confirm fix gates the PORTAL's PROD promotion, not the r34m install. Not started at 05:29Z; it waits for 07:00Z (the freeze is 05:45Z-07:00Z). |
| The 4 ARMED TCKT rows owned by this seat (CVO msg 11220; `comp-surprise --armed` reads 4) | W6-S2: a BUILD cell (data-refresh routes refuse a missing userType). S50: a BUILD cell (a DISABLED users row is refused). S46: a READ cell first (count the lambda:InvokeFunction principals). Both builds go under one pair. S53 goes to Andrew (an entitlement): open-calls row a331. |

## Acts only Andrew can do

- **Row a331** (an entitlement; CLAUDE.md, the self-drive act list: "entitlements beyond his grants"): whether the outside-domain users
  row in TCKT_VNEXT-D2-S53, which carries the internal firm id, keeps all-firm access. REC: limit it to its firm, or disable it.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"):
  - `C:\dev\wk-irpt-dashbd-503`;
  - row 544d;
  - row 65a1;
  - row a392.
- **S3 deletes:**
  - row 6e7c;
  - row 128f;
  - the synthetic leftovers of runs 5 to 5D (rows S218-S222 and 5D's).

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
