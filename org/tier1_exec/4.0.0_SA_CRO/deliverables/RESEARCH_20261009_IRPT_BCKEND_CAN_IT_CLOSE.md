# Can IRPT_BCKEND close? Per-FWD disposition (CRO read)

**Author:** 4.0.0_SA_CRO~DELL2, 2026-10-09 ~05:5xZ
**Ask:** Andrew, in-session at 2.0.0_SA_COO~M2 ~05:4xZ, relayed as msg 2619: "Ask CRO if we can close this, what actually
remains on endpoints here that arent finished? i can eyeball it and probably just close it".
**Inputs:**
- ~M2's table `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/IRPT_BCKEND_CLOSE_QUESTION_ENDPOINT_TABLE_20261009.md`
  @60c1fe694e;
- the CTO ruling ca5f74553d (consolidation into IRPT_DASHBD);
- IRPT_ANLREQ v0.3 C-ABSORB @1251f44685;
- ~P2's drain packet d35d2fb851.

## Answer

**Not today as it stands, but it can be shrunk to two outcomes now and closed once those two are driven.** Nine of the
twelve FWDs have a home elsewhere or are obsolete. Two are live platform guarantees that every other IRPT project leans on,
and one of them has an ARMED hazard due 2026-10-12.

| FWD | Disposition | Why |
|---|---|---|
| FWD-1 advisor finds a client | **FOLD -> IRPT_FNTEND** | its grade is FNTEND's; what remains is a PROD route opening and one advisor walk, both frontend |
| FWD-2 restricted advisor sees only their population | **KEEP (platform), open** | security property of the 21 scoped routes; what remains is a replay on current bytes (both principal classes, revoked grant), seat-drivable now |
| FWD-3 Opal performance at INF/COT | **FOLD -> IRPT_DASHBD** | ruled ca5f74553d |
| FWD-4 YCharts sensitivity analysis + export | **SUPERSEDE -> IRPT_ANLREQ** | the Analysis lane is absorbed (C-ABSORB a), and ANLREQ FWD-7 removes YCharts, so "YCharts analysis" as written is obsolete |
| FWD-5 holdings by model | **this share DONE; view -> IRPT_FNTEND** | REALIZED (msg 890) |
| FWD-7 directory cannot go quietly stale | **KEEP (platform), open, ARMED** | row D2-W187-S1: the served directory goes over-age 2026-10-12 (Cottonwood) and 10-13 (Inflection); the seeding run is blocked on a runner-host grant (d35d2fb851); the five-arm controlled-clock drive is seat-drivable |
| FWD-8 branded report with a narrative page | **FOLD -> IRPT_DASHBD** | it is the Performance client statement's export (IRPT_CUSTDY template, ~P2 cell E-P9), now consolidated there |
| FWD-9 forwarded email becomes a request | **FOLD -> IRPT_ANLREQ as a later outcome, or RETIRE on Andrew's word** | a second entry door to the same journey; the intake schedule is DISABLED; ANLREQ's primary door is the form |
| FWD-10 request lands in its own firm's storage | **FOLD with FWD-9** | it follows FWD-9; ANLREQ FWD-5 already holds the firm fence for the form path |
| FWD-11 Opal Global view across firms | **FOLD -> IRPT_DASHBD** | a performance view across firms |
| FWD-12 daily holdings-basis gold | **FOLD -> IRPT_DASHBD** | ruled; it serves as the guard rail |
| FWD-13 Opal vs vendor figure | **FOLD -> IRPT_DASHBD** | the one BD comparison is DASHBD FWD-8 |

## The fastest honest close

1. **Today:** the CTO writes one addendum moving FWD-1, 3, 4, 5 (view), 8, 9, 10, 11, 12 and 13 as above. IRPT_BCKEND then
   holds FWD-2 and FWD-7 only, with ~P2 as its one lane. ~M2 is released (unblock UB-20261009T052107Z-32d8).
2. **Disarm FWD-7's hazard before 2026-10-12:** the runner-host grant for the seeding run, then the five-arm drive on
   served bytes.
3. **Drive FWD-2's replay** (21 routes x 2 principal classes + the revoked arm). This is a test run, with no new build.
4. **Close** when both grade REALIZED. Alternatively, Andrew may close it now and move FWD-2 and FWD-7 to a small
   platform row. But FWD-7's hazard needs an owner either way, so closing outright before the 10-12 date leaves it
   orphaned.

**Limits:** grades since 10-07 are taken from the CTO's records (`held`), not re-run. No release was re-graded here.
