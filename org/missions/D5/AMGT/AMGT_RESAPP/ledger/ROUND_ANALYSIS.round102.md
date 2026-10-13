# AMGT_RESAPP -- ROUND 102, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~17:0xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4954, `surprise-channel/adjudications/ADJUDICATION_v124.md` @4a8f8b49eb. MAY-CLOSE.

## 1. Graded

- **bi-1 and bi-2, the per-phase timing log lines: APPLIED** (this seat's half and ADDENDUM 1, with `exemptions.json` admitted as the 12th member, replay 0 differ).
  - **The phase is named:** the first overlay a container serves costs about 20 s, and **18.8 s of it is the FEED phase reading the whole `article_security_mention`
    table** (C-S112).
  - That cost is paid whether or not the container is cold: run 1 q2 took 20.08 s with no Init, and the cold first request 4737aa2a took 20.57 s on bKCGUhXp.
  - Round 100 ADDENDUM 2(b)'s condition is met (no remedy until the phase is named), so the remedy is cut below.
- **bi-3 AC3: MET, with a binding limit** (C-S113). "Steady state" rests on 3 warm overlays with no window; the CVO's log window holds 737 warm overlays (median 0.49 s) under a
  different condition. The Saturday close must state a window and a denominator, not three requests.
- **bi-4 AC4: MET** (C-S114). The suite at `0a06280a` reads 1,419 / 1,386 / 27 / 6, which are the table's six failures. `c26e0c68` is not on DEV by ancestry or by patch: it was
  withdrawn by `2.0.0_SA_COO~R1` (msg 4923), and this seat's approval of it is void.
  - The three still-red tests (IRPT_ANLREQ, IRPT_BCKEND and DSGN_IRPTV1) are routed to dell2 through MSTR. D1-S18 is disposed ROUTED, and it closes when DEV CI is green.
- **Rows:**
  - W402-S1 is GRADUATED ARMED to REMEDIATION_v39 (the cold-overlay hazard is still served), with disarm owner `2.0.0_SA_COO~R1`; it is item 1 below.
  - W402-S3 is inert, S27 is disarmed, and round 97's W393-S1 is dismissed (C-S119).

## 2. ENRICHMENT LIST (round 103, ONE issuance by `2.0.0_SA_COO~R1`)

1. **THE FEED CELL (disarms W402-S1).** The overlay's feed phase reads ONLY the requested security's rows of `article_security_mention`, never the whole table: a key-scoped
   read the store already supports, or a per-security slice written by the existing producer (build ladder first; no new pipeline, no shadow copy).
   - Under its own pair. Served overlay bytes are BYTE-EQUAL to the current recompute for a named sample (ASML_NA plus 4 drawn keys), with a negative control: a key with no
     mentions returns its empty answer equal too.
   - **Close:** ONE driven first overlay on a fresh container after 15 quiet minutes, with the feed phase read from the bi-1 log lines. The negative arm is the current build's
     18.8 s.
     - The PRD addendum this analysis writes sets the target: **feed phase at most 2 s, first overlay at most 4 s**.
2. **bi-3's steady state, with a window:** the warm-overlay figure is restated over a declared window (start, end, trading-calendar basis), with its denominator and its median
   and 95th percentile, read from the logs. The Saturday read is the organic negative arm; it is not waited on.
3. **The admission-table tool** (this seat's bi-2 half, ADDENDUM 1): `r94_admission_table.py` diffs EVERY registry file the build packages, not a fixed two. Its arms are a
   build that packages `exemptions.json` (must list it) and a build that packages none (must list none).
4. **Andrew's rule, TWR pricing on every surface** (`org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`, census row A4):
   - `integrations/bloomberg/research/price_axis_pull.py` adds a total-return field to its daily pull at the 5-trading-day window (site Z item Z5);
   - the rankings stay on price until a PRD addendum says otherwise;
   - it is a site Z cell, and its draw goes through the queue.
5. **Staged and carried:**
   - ss-7 / pp-4 on MDPF_DEMQUE's CRNCY answer;
   - the reader-side EXPIRED criterion for the first `packs/<key>/status.json` reader (from AMGT_HARVST).

## 3. ACTS ONLY ANDREW CAN DO (cited)

None.

-- 1.0.0_SA_CTO~DELL1
