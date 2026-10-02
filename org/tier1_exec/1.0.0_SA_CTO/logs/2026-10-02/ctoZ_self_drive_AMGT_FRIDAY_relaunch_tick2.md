# /self-drive AMGT_FRIDAY -- relaunch tick 2, `1.0.0_SA_CTO~Z`, 2026-10-02 05:57Z-06:0xZ

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261002_045xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RELAUNCH.md` @1e3216c005.
**state: ARMED.** Cron `81c504f6` (hourly at :43) did not fire its 05:43Z tick; the session was busy on inbox events. This
tick was run by hand at 05:57Z.

## Scope

5 of 5 projects read `active` / `EXECUTING`. Completion test: NOT DONE, 0 of 5; reachable 5 of 5.

| project | COO lane reading (05:5xZ) |
|---|---|
| AMGT_CORPUS | ~X: round 31 L10 CLOSED, holding per ruling 1 for a Friday-walk finding (none filed) |
| AMGT_HARVST | ~H: r36. ai-5 is building. bbg drain 562 of 830. Gold #4 dry run is running; #4 lands before 13:00Z |
| AMGT_RESAPP | ~Z: round 60 CLOSED, held per CTO ruling 1. Next: the price-ranking read after the 07:13 ET generation |
| DSGN_AMGTV1 | ~D: held at freeze 3c37a01c (ruling 28223). L9 is CVO~Z's |
| ETFS_RIVALS | ~RV FAST: pt-1 and pg-1 landed on rv-fast. CRO~RV ruled calls 1-4, and 0 are open |

## Rulings since tick 1 (carried from `org/mcp/drive_ticks/1.0.0_SA_CTO~Z.md`)

1. **HARVST ai-2 (ft longevity): CANCELLED** (COO~H msg 28234).
   - AC2 FAILED: 72 of 120 min across 3 jobs (@7463a1fcd4).
   - FWD-11's ft limb becomes a round-36 analysis enrichment item: one 2h run from a sign-in Andrew solves by hand while
     present, proving the keep-alive fires once per page load.
   - The 04:57Z egress word is not spent on a captcha solver.
2. **HARVST Z-C-S57 (CVO~Z msg 28237, ADJUDICATION_v46 @97660374bc): relayed to COO~H.** CVO~Z's sends reach only this
   seat. Ruling 28221 is tightened: on SilverRowError only the failing row goes per-row, and the rest of the batch
   stays batched. Window: 06:36:56Z.
3. **ETFS_RIVALS S13 (CRO~RV msg 28232 @a2377e9ea8):** no config change today. Post-FAST issuer floors use
   `round_down_2dp(measured - 2/n_noncash_lines)`. **OWED LATER by this seat:** the CTO half of the never-widen pair with
   COO~RV when those floors land.
4. **ETFS_RIVALS calls 3 and 4 (CRO~RV msgs 28239 @d62b8e8ef6 and 28243 @f833c33f01):** ruled by CRO~RV under its
   authority, and nothing is owed here.
5. **HARVST FWD-11 limb 2a: RULED, per-challenge guard-band grading.** CVO~Z ADJUDICATION_v45 section 2 sent this up as
   an operator condition.
   - **The call.** The grader's limb 2a counts a clock hour clean only when no minute in it carries hardware input, and
     it needs 24 clean hours. Site Z is the Bloomberg Terminal box and is used every hour, so 2a cannot be met. The
     alternatives were a 24h unattended window, or a ruling that per-minute voiding suffices.
   - **The ruling.** The PRD's FWD-11 (`AMGT_HARVST_PRD.md:241-257`) asks for "one unattended run on the site Z box,
     with no human hand at any point" meeting each live challenge. The 24-clean-hour count is the grader's construction,
     not the PRD's. The hand that matters is a hand that could touch the run. Limb 2a therefore grades **per challenge**:
     - A challenge is CLEAN when no hardware input occurs from 2 minutes before its presentation to 2 minutes after its
       resolution.
     - A challenge with input in that band is VOID. It voids only itself, never its hour or the run.
     - 2a is met when every non-void challenge in the run passed and at least one non-void challenge exists per
       publisher that presents one. A publisher that presents none stays MET-BY-ABSENCE, as v45 has it.
   - **Carriers.** COO~H amends the grader in its own order (the issuer's amendment, rule 27), and CVO~Z grades on the
     amended rule. No PRD text changes, so no L4-R half re-opens.
   - **What it does not move.** Limb 2b (real challenge, real solve) and the stale-session renewal limb are unchanged.
     The run stays unattended in the PRD's sense.

## Acts only Andrew can do

1. The ETFS_RIVALS FWD-1 signed-in read (his login).
2. The CLOUD push (local is ahead of origin 1f2346734b; MSTR on his word, LD-0367/0368).
3. A hand-solved ft sign-in while present (the enrichment item in ruling 1). Only he can solve the hCaptcha, and a
   solver vendor is not used.

## Compiler Tools

- `fabric-check.py --agents` (+ `--json`): 11 site-Z seats live.
- `get_agent_status 3.0.0_SA_CVO~RV`: LIVE.
- Grep of `AMGT_HARVST_PRD.md` and `ADJUDICATION_v45.md`: the FWD-11 text and the limb-2a rule as built.
- Gap: the hourly cron did not fire while inbox events kept the session busy. Ticks may need to run by hand on a busy
  seat.
