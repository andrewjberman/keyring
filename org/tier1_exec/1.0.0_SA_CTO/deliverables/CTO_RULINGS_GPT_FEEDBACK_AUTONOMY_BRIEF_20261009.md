# CTO rulings on the GPT-feedback / no-cross-box-dependency brief

**By:** 1.0.0_SA_CTO (laptop), 2026-10-09 ~19:4xZ. **Brief:** `docs/briefs/gpt-feedback-autonomy-solutions-brief-20261009.md` @e104bb0ddd
(4.0.0_SA_CRO, msg 108096). **Andrew's words:** `ANDREW_DIRECT_20261009_190xZ_GPT_FEEDBACK_TO_CRO_FOR_SOLUTION_ANALYSIS.md` and
`ANDREW_DIRECT_20261009_191xZ_NO_CROSS_BOX_DEPENDENCIES_AFTER_MIGRATION_AND_DELL_PACKAGES.md`. Constraint held: no new approval gate,
monitor or shadow pipeline.

**Correction accepted:** the deploy backlog is 24 tracked open entries on every branch, not 95-131 per box (the scan counted disk). The
process report is corrected in its next update.

| # | Ruling | Owner | Route |
|---|---|---|---|
| 1 | **YES.** The five append-only logs (`org/git-author-override-audit.log`, `org/mcp/agent-spawn-audit.log`, `org/mcp/drive-mode.log`, `org/law-edit-audit.log`, `org/safe-deploy-bypass-audit.log`) get `merge=union` in TRACKED `.gitattributes`; the laptop-local lines in `.git/info/attributes` are removed after. The box-sync pre-land commit of a seat's uncommitted appends covers all five. Per-box split logs: NOT now (union gives the same result for one setting). | `0.0.0_AB_MSTR` (`.gitattributes`); `4.0.0_SA_CRO~A` (box-sync step) | MSTR |
| 2 | **YES.** One rule in `/integrate` and in box-sync's HELD message: a break in a trunk-shared file is repaired only by the seat owning the file's lane, on its own box; every other box takes `CLOUD` at its next pass. Unowned (ANY) paths: the integrator's box repairs. | `0.0.0_AB_MSTR` | MSTR |
| 3 | **YES, both steps:** per-phase seconds in the BOX-SYNC row (`t_fetch`, `t_merge_<box>`, `t_push`), and an in-pass retry of a refused integrate push (re-fetch, rebuild, push, at most twice), as `box` mode already does. Confirm the win by comparing phase times before and after. | `4.0.0_SA_CRO~A` (box-sync owner) | CRO~A |
| 4 | **YES:** `unblock.py tick --result nothing --wait-until <UTC> --owner <serial>` BEFORE a case is opened; it reads WAITING UNTIL and holds the count at 0. Plus one line in `/unblock` and `/next-calls --drive`: a dependency with a live owner and a time is a wait -- record it, do not count it. | `4.0.0_SA_CRO` | CRO |
| 5 | **YES:** (a) the CRO fixes its `open_deploys` scan to read each worktree's HEAD and name untracked sentinel files apart, now; (b) each of the 24 tracked entries is reconciled by its author with `deploy_ledger.py check` -- measure the artifact, close with proof or SUPERSEDED (CLAUDE.md NEVER-2); (c) merged worker worktrees are force-removed at every drain (Andrew's standing word); an unmerged one goes to its owner. Deleting untracked files on a box's disk in bulk is a recursive delete and waits on Andrew. | CRO (a); entry authors (b); each box's COO and MSTR (c) | CRO; MSTR broadcast |
| 6 | **YES:** `placement` in the mission `project.json` is the one placement field; readers already prefer it (@4934c4b98b). This seat aligns the 16 disagreeing mission rows now (fabric := placement), and every transfer from now on edits placement and fabric in one commit AND names, in the move's record, the rights and lanes the project needs on the new box (the checklist line the brief proposes). Legacy flat rows with no box are a spring-clean question, not a placement one. | `1.0.0_SA_CTO` | this seat |
| 7 | Covered by 1-6 and section D. | -- | -- |

## Section D -- cross-box dependencies

| Row | Ruling |
|---|---|
| Bloomberg (dell1 MDPF/ETFS projects) | **Kept as a served interface:** the DEMQUE queue is the route (CLAUDE.md: Bloomberg pulls go only through their queue); dell1 files requests and reads the stored series and never needs a site Z lane for it. |
| Harvest/induction runners (AMGT_HARVST, AMGT_CORPUS) | **Measure first:** dell1's COO for each project (`~W1`, `~C1`) names which runners are site-Z-only; then either move the runner host or give the Dell group a box-local deploy lane to it, as an NFRA_CTLPLN grant. |
| Gateway releases (NFRA_TRNSPT FWD-6, ADVI_BILLING) | **YES: a dell2 release lane to the gateway host** (scoped SSM route grant); the gateway's own release gate unchanged. NFRA_CTLPLN round-7 enrichment. |
| svc-irpt password windows (dell2) | **YES: dell2 opens and closes its own window** on that one ARN under a scoped NFRA_CTLPLN grant (the amendments 20-24 shape); the window stays audited and time-boxed. NFRA_CTLPLN round-7 enrichment. Until it lands, the laptop keeps opening them. |
| AMGT_RESAPP republish rights | **YES: one scoped grant to the Dell group** for that republish target. NFRA_CTLPLN round-7 enrichment. |
| MDPF_STRATID / MDPF_GLOBAL sign-off | **RULED NOW:** the never-widen CTO half for served output a placed project moves is signed by the CTO of the box the project is placed on. A dell1 project moving MDPF_GLOBAL's served output: `1.0.0_SA_CTO~DELL1` signs. This seat (MDPF_GLOBAL's owner) is no longer a required half. |
| Dell IAM grants (TO-APPLY-29 class) | **Kept, by design:** the control plane granting the Dells their rights is the one legitimate standing dependency. Batch each round's grant needs into one amendment. |
| NFRA_CTLPLN exercises on dell1 | **Kept:** migration-class work; ends with the project. |

## Addendum ~19:5xZ -- section D (b) runner census (0.0.0_AB_MSTR 108107; dell1 CTO msgs 3098/3099) and progress

- **Runners: dell1's REC ACCEPTED.** Site-Z-only are AMGT_HARVST's FWD-18 cycle runner and backfill driver legs (bound to site Z's publisher
  sessions and Chrome profiles) and AMGT_CORPUS's `amgt-induction-daily` (bound to the Bloomberg Terminal). Their hosts cannot move, so they stay
  on site Z as a SERVED capability owned by a site Z lane; dell1 files requests by crossbox file and gets no new deploy lane. Everything else
  (gold builds, dossier, continuation, census) already runs on dell1. This is the second hardware-bound exception beside the Terminal itself.
- **Box gap (packages):** `fitz` (PyMuPDF) does not load on dell1 (Python 3.14 or the 3.12 kit), so dell1 stubs the PDF extract. Owner: dell1's
  manager, as box infra -- install a PyMuPDF build that loads on dell1, or switch `extract.py` to `pypdf` (already installed). Census otherwise:
  dell1 hard_missing 0 (849cd33fa3).
- **Landed:** items 1-2 (@1e775f68b6, @9f5386270c, MSTR); item 3 + the five-log append (@e68f2921cc, CRO~A, with a before-baseline of 211 integrate
  rows, median 44.5 s); items 4 and 5a (@69759661d3, @dbee5062c9, CRO); item 6 register alignment (@228e8598cd, this seat: 9 rows + 6 sequence
  DRIFT rows; sequence-check DRIFT 6 -> 0).
- **ADVI_FIRMBKTS** re-placed LAPTOP -> DELL1 @8afcb0f851 for dell1's free COO slot (it gates LGIC_CANON and MDPF_CANON there).
