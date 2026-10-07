# /self-drive dell2 projects -- tick 3 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since the tick 2 addendum (@aca051cad6), plus tick 3 (08:45Z). **state: ARMED**

## Scope state (08:45Z)

| project | status | dep_stage | sequence flags |
|---|---|---|---|
| IRPT_CUSTDY | active | EXECUTING (was PRD at tick 2; round 1 issued and drained by `~K2`) | NEEDS-SLOT (tracker gap; `~K2` live) |
| IRPT_BCKEND | active | EXECUTING | none |
| ADVI_COTBKF | active | EXECUTING | NEEDS-SLOT (tracker gap; `~C2` live) |
| IRPT_YCDGEN | active | EXECUTING; PRD v0.9 WITHHELD pending the CVO re-sign | none |
| IRPT_DASHBD | active | EXECUTING | none |

Inbox (0.8): 0 unread at 08:45Z. Messages read and acked since tick 2: 95, 97, 101, 107, 108, 111, 113, 115, 117, 119, 123, 135,
136, 140, 144 and 159.

## Andrew-direct received (recorded same turn)

- ~08:0xZ at this terminal: 4.0.0_SA_CRO is the research arm for AI swap suggestions and the check/swap UI. Record @1ea0796be2.
- ~08:0xZ at the laptop CTO, relayed (msg 113, laptop record @c3e1caead4): "any new project concept has to go through full
  /canonical-flow."

## Calls closed

| call | ruling | carrier |
|---|---|---|
| `~G2` msg 95: propose /closer for IRPT_YCDGEN? | No. One break remains on FWD-1's path (t-6). Re-open if F1 fails after t-6 lands on DEV | msg to `~G2` 07:58Z |
| `~P2` msg 97: who measures S338 | (a) a laptop seat reads it. Laptop decision 106062 put it with laptop `3.0.0_SA_CVO`; the fence fix is NFRA_CTLPLN round 4 | relay 08:00Z; msg 108 |
| `~K2` msg 101: which 49F advisor for FWD-1 | Picked by census: the fewest households of those with 10 or more and full Schwab coverage at 2026-09-30. Handing the reports to the advisor is Andrew's act | msg to `~K2` 08:02Z |
| Y-5 packet 2 | STOP withdrawn (msg 104), then SUPERSEDED by IRPT_YCDGEN S32 (msg 120), on the CRO brief section 4.1 | msgs 104, 120 |
| Leg A1 of `irpt-inf-performance-serving-20261002` | Amended @9204974f23 on the laptop CVO's measurement and the laptop's REC (msg 115). Three disclosed no-close days pass; a fourth fails. Part (2) is routed to a laptop read (msg 136) | relay 08:21Z |
| IRPT_BCKEND rows 47-60 (slug 111) | L10 analysis @e363a194ed. 0 of 12 REALIZED. Enrichment: P 7, Y 3, M 1 | msgs 154-156 |
| IRPT_DASHBD W12-S1 (slug 117) | One gross basis; BD's fee is added back per segment; no FEES reason. L10 @e363a194ed | msg to `~D2` |
| ADVI_COTBKF S9 (slug 140) | Cause NAMED: dell2's calendar fallback covers 2024-2027 only, reproduced on 1,450 of 1,450 rows. No links apply from dell2. L10 @e363a194ed | msg to `~C2` |
| `~M2` msg 159: is the E-M1 condition met? | MET. Laptop `~M` is FINAL on IRPT_BCKEND (handoff @1640a0e86e, lines 1-4). Issue E-M1 | msg to `~M2` 08:40Z |
| S348 row-id collision (dell2 and laptop) | dell2's S348 keeps the id. The laptop row is renumbered at the next merge | msg to MSTR 08:17Z |
| The check/swap brief (CRO, @3d0ecacb0b plus Part VIII @c16f0f8ddd) | Accepted. L2 run; IRPT_YCDGEN PRD v0.9 @8499df49ce adds FWD-17 to FWD-23 | msgs to the CVO and `~G2` 08:44Z |

## Escalated across boxes

- **The Dell trading-calendar hazard** (relay 08:38Z, URGENT): `lib/trading_calendar.py` falls back to holidays for 2024-2027
  only when `pandas_market_calendars` is absent. 103 Python files import it. REC to laptop `1.0.0_SA_CTO`: generate the full
  closure list on the laptop, and make the calendar fail closed outside its years. Dell2 installs nothing from PyPI.

## Verdicts since last tick

None from `3.0.0_SA_CVO` on this loop's pitches. Owed: the IRPT_YCDGEN v0.9 ratified-text half (asked 08:44Z).

## Acts only Andrew can do

1. IRPT_YCDGEN F1 retry, his own sign-in, after t-6 lands on DEV (his login).
2. IRPT_BCKEND: ONE export that exercises S340-S342, S345 and S346 (his per-use vendor word, CLAUDE.md), and opening
   `/investor-reporting` on PROD to an advisor, or naming an advisor test principal (lifting a gate he set by name,
   2026-09-22).
3. IRPT_CUSTDY: putting the FWD-1 reports in front of the chosen advisor (egress off Opal infrastructure, CLAUDE.md Agent
   Autonomy). Listed when the run is ready.
4. Optional: the CRO's external-products research (web egress, CLAUDE.md).
Not an act, but offered: his confirmation of IRPT_YCDGEN FWD-17 to FWD-23. The PRD marks them as emitted and not yet confirmed.

## Addendum 08:51Z (same tick, events after the first draft)

- `~Y2` msg 171 GRANTED: `.owned-paths.yaml` @4f3505fb84. `~Y2`, `~P2` and `~M2` are added beside their predecessors in the IRPT
  lanes (22 lines; `~M`'s MDPF lanes left to dell1). New lane IRPT_RESIDENT_ONE_WRITER_G2 holds the three resident host files,
  with `~G2` as its only COO lane (executes msgs 90/91). Broadcast as msgs 186-189.
- Laptop CTO 08:5xZ rulings (msg 172): HOLD on pre-2024 dates through `lib/trading_calendar.py` on dell2; only the Dell mints
  row ids for a Dell project, and a laptop result arrives as a FILE. Relayed to all 7 dell2 COO lanes (msgs 192-198).
- `~M2` msg 185 (S352, 403 on the firms' Holdings manifests): RULED (a), a laptop read delivered as a FILE. Relayed with the
  IRPT_CUSTDY ownership-map read and its naming-registry row (08:50Z).
- `~K2` msg 184 (IRPT_CUSTDY round 1 drained, 4 of 4 VALID, thread NOT LIVE): W4-S1 (render contract) is a DESIGN FORK, sent to
  `4.0.0_SA_CRO~DELL2` for research (08:50Z). The S01/hop-1 wording lands in the L10 addendum after the CVO's compile. S3 is
  round 2's first item.

## Completion test

NOT DONE: 0 of 5 complete. 5 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `prd-signoff.py status`: IRPT_YCDGEN reads WITHHELD after v0.9 (the ratified-text half is STALE, as expected after an ENDPOINT
  change).
- `prd-manifest` commit gate: OK on IRPT_YCDGEN v0.9. Trap seen today: an editor that writes CRLF on Windows (Python text mode)
  rewrote all 346 lines of an LF file. The fix was a byte-level LF restore before commit. On a shared file, always diff `--stat`
  before committing.
- `to-pipeline-gate._top_section` probe: used to check the manifest and ENDPOINT parse without staging.
- Forks: 3 analysis drafts and 1 portal review; each draft was read and amended by this seat before landing.
