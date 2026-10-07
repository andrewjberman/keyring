# CTO ASSESSMENT 2026-10-07 -- IRPT_BCKEND's Y workstream against IRPT_YCDGEN: layered, not duplicate; three items to stop

**Author:** `1.0.0_SA_CTO` (laptop, the control plane). Both projects target dell2.

## Andrew's words, VERBATIM (typed at the `1.0.0_SA_CTO` terminal ~07:3xZ)

"Also I want you to check out the IRPT_BCKEND (Y Workstream) and the IRPT_YCDGEN projects, and assess if they are
complementary/synergistic, or if the Y Workstream is deprecated. Initially we had been working on a solution whereby we ported YCharts
analysis service via the backend of the opalinvest.dev webapp through the "Analysis" tab on the Investor Reporting page. Because that
connection was tenuous and it takes so long on complicated reports, it made more sense to build out a local solution in our AWS
Cloud, and thereby YCDGEN was born. Accordingly I want you to make sure that these two workstreams do not overlap."

"I have already alerted the workers on the Dell box of this matter as well, but it is worth you looking over as the CTO on the control
plane."

## Verdict

**Complementary, with a deprecation date.** The Y workstream is two things in one lane. One half is the Analysis tab's chassis, which
IRPT_YCDGEN runs on and cannot replace. The other half is the YCharts producer, which IRPT_YCDGEN replaces at its outcome FWD-11.
The Y workstream is NOT deprecated today: IRPT_YCDGEN's first version has no prices, returns or risk (its contract C-V1), and its
producer serves one sign-in (Andrew's), so every other user's full report still comes from YCharts.

## What I read

`org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` v0.8 (sections 1, 2, 4, 5, 6 and the contracts table);
`org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md` (vintage 2026-10-05 16:2xZ); the code layout under
`infra/aws/lambda/investor-reporting/ycharts/`; `resident_worker.py:115-142` and `:407-433`. Not read: the IRPT_BCKEND PRD's own Y
section, and the dell2 seats' current state.

## The split

| Part | Owner | Fate when IRPT_YCDGEN reaches FWD-11 |
|---|---|---|
| Intake, acceptance and the job row | IRPT_BCKEND Y | KEPT: IRPT_YCDGEN's thread says they are "unchanged" (PRD section 2, hop 1) |
| The generation worker and queue `irpt-generation`, the resident host | IRPT_BCKEND Y | KEPT: the Opal producer runs inside this worker (`resident_worker.py:407`) |
| Status route, report history, publish | IRPT_BCKEND Y | KEPT |
| Brand assets on the export path | IRPT_BCKEND | KEPT, read only |
| The Opal producer (`ycharts/research/`: `opal_producer.py`, `layout_overview.py`, `held_data.py`, the runner) | IRPT_YCDGEN | becomes the only producer |
| The reference and look-through refresh, a new daily job | IRPT_YCDGEN | new |
| The YCharts sign-in, session capture and probe, the lease | IRPT_BCKEND Y | REMOVED ("the YCharts calls have stopped", PRD section 1) |
| The YCharts recipe: upload, the 900-second hold, the read-back, the firewall handling | IRPT_BCKEND Y | REMOVED |
| Re-reading the YCharts PDF figure by figure (`ycharts/extract/`) | IRPT_BCKEND Y | REMOVED |

## Where the two actually touch (the overlap risk, four places)

1. **One file, two projects.** `ycharts/generate/resident_worker.py` carries the switch between producers (`:115-133`) and is the
   Y workstream's own worker. It took 31 commits in 21 days. IRPT_YCDGEN's PRD already says the switch is "written through another
   owner's release, as a named cell with its half" (section 5).
2. **The check gate.** IRPT_YCDGEN FWD-16 moves the typo and swap verification from YCharts' data to Opal's, in files the Y workstream
   owns (`upload_suggestions.py`, `security_resolution.py`; PRD surface S31).
3. **The report contract.** One `AnalysisReport` contract with a YCharts form and an Opal form; the contract file is the CTO's.
4. **The allow list.** `resident_worker.py:121` still holds a placeholder on CLOUD; the real value is on branch `rel-ycdgen-r6-b2`
   (commit 409e3066d1) and lands after Andrew's report retry.

## Recommendation

**A. One lane holds both on dell2.** On the laptop both were issued by `2.0.0_SA_COO~Y`, which is why the shared file never
collided. dell2 seated `~Y2` on IRPT_BCKEND and, at this writing, no lane on IRPT_YCDGEN. `~Y2` should hold both; two lanes on
`resident_worker.py` is the collision.

**B. Stop three Y items that only improve the YCharts producer.**

| Item | State | Recommendation | Why |
|---|---|---|---|
| Y-5 packet 2, the Kimi swap | HELD (CTO batch 218) | STOP for good | It adds capability to a producer that is being removed; FWD-16 builds the swap on Opal's data instead. |
| Y-6 runs 8 to 10 | open, the page lane's | STOP | They measure the YCharts path's behaviour; seven runs already recorded it, including the eviction. |
| New work on the session, the lease or the firewall | none open | Do not start | Repair only what breaks for users still on YCharts. |

**C. Finish one Y item, because it is already built.** The 390-second release (branch `y-release-390` @f1e101d19c) cuts each YCharts
report's fixed wait from 900 to 390 seconds. Everyone but Andrew stays on YCharts until FWD-11, and the first Opal version has no
prices, so that wait is paid for some time yet. It needs its never-widen pair and a resident build.

**D. Keep the Y workstream open until FWD-11, then close it with the removal.** The chassis half moves to whichever project owns the
Analysis tab after that; today that is IRPT_BCKEND.

## What would change this verdict

If Andrew wants no further user on YCharts before the Opal report has prices, item C stops too and the Y workstream becomes
maintenance only. That is his call: it trades a faster report now for less work on a path with an end date.

## For the dell2 CTO

`1.0.0_SA_CTO~DELL2` self-drives these projects and rules them. This is the control plane's read, sent as a finding with
recommendations A to D, not as an order to a dell2 seat.

-- 1.0.0_SA_CTO
