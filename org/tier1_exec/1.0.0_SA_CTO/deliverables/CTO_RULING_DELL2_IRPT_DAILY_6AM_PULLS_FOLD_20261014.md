# CTO ruling -- folding the IRPT daily 6 AM ET pulls scope (S1-S7) into IRPT_BCKEND and IRPT_DASHBD (2026-10-14 ~19:3xZ)

From `1.0.0_SA_CTO~DELL2`, on `4.0.0_SA_CRO~DELL2` msg 7833 (`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_DAILY_PULLS_SCOPE_20261014.md`
@712e2eb0e3). It answers crossbox ORDER `XB-20261014T185521Z-75d6` (Andrew-direct ~19:0xZ,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_190xZ_IRPT_DAILY_6AM_ET_PULLS.md`). Frame: P1 Investor Reporting, Nov 15.

## The cause, in one line

The runs fire and succeed. The holdings publish gate REFUSES on `account_lost`, so Cottonwood serves 10-08 and 49 Financial 10-12. And no
6 AM ET schedule exists anywhere.

## Rulings

| item | owner | ruling |
|---|---|---|
| **S1: `account_lost`** | IRPT_BCKEND `~P2` | It is the signed holdings-producer release, IB-pr-532: the cash rule plus the exemption repair. Its packet already has Cottonwood "publish with 1 lost account listed". **It stays the critical path:** round 196's closure fix, the built-bundle differential, Cottonwood's attribution, packet v3, the apply. No second route is built beside it. After it applies, the after-read confirms each firm publishes T-1 with any lost account listed by reason. |
| **S2: one naming and timing pattern per firm** | IRPT_BCKEND | Every upstream pull fires at **06:00 America/New_York** (Andrew's word) on an EventBridge Scheduler entry. Each IRPT producer runs on its own New York schedule after its input lands, with a `trading-day-frontier` freshness basis. **Names are `lib/opal_naming.py name()` output (CLAUDE.md rule 30), never the hand-typed `irpt-<firm>-<source>-pull-daily`.** A builder refusal is a registry row. |
| **S3: a Cottonwood performance schedule; Inflection performance to New York time** | IRPT_BCKEND | Cut with S2. Row IRPT_DASHBD-D2-S37 (Cottonwood's performance gold ends 2026-09-25, 12 trading days behind) closes on it. |
| **S4: the reporting chain for Cottonwood and Inflection** | IRPT_DASHBD `~D2` | **Not 49F-only.** P1 is "all clients at all firms". It is already on the IRPT_DASHBD thread (rounds 108-111). |
| **S5: success-only triggers become schedules** | IRPT_BCKEND, with the firm producers | Production pipelines MUST be scheduled (CLAUDE.md). A success-only trigger becomes a schedule plus an input-frontier check. It is ported directly, in the same window, never alongside the old trigger. |
| **S6: one copy each of Inflection Orion bronze and Eclipse silver** | IRPT_BCKEND | The duplicate copies are retired after their readers move to the canonical silver. It is a consolidation, under its own pair. |
| **S7: the six disabled 49F Black Diamond triggers** | this seat | **Retire them, not re-enable them**, the window after the S2 schedule for 49F reads one good scheduled fire. Re-enabling them would keep the forks Andrew wants gone. Each is read first: what it fired, and whether S2 covers it. |

**Order:** S1 (in flight), then S2 with S3 and S5 as one schedule release per firm, 49 Financial first; then S6; then S7. S4 runs alongside
on IRPT_DASHBD.

-- 1.0.0_SA_CTO~DELL2
