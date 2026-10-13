# NFRA_DEVPLN -- per-box portal DEV work, approved before it reaches DEV, so PROD carries only approved features (L1 brief)

**Author:** `4.0.0_SA_CRO` (laptop), 2026-10-13 ~14:3xZ. **Mode:** NEW.

**Commissioned by Andrew**, relayed by `2.0.0_SA_COO~C`
(`org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_135xZ_PER_BOX_PORTAL_DEV_BRIEF_REQUEST.md`), VERBATIM:

> *"What should be happening moving forward is that each Box has its own worktree and it must get approval on before merging
> forward to DEV. that way we can do PROD promotes with only approved DEV features."*

**Made a project** by Andrew at ~14:0xZ
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md`),
VERBATIM:

> *"get this brief sorted and folded in as a laptop project NFRA_DEVPLN. I want it separated from CTLPLN because CTLPLN is
> getting too large."*

**Consumer:** `1.0.0_SA_CTO` at L2 (`/endpoint --forward`) and L3 (registration, placement laptop). Nothing here is built; no gate
is implemented by this brief.

---

## PART I -- THE OUTCOME TERRITORY

### O1 -- THE CANDIDATE THREAD: Andrew approves one feature built on one box, and only then does it reach DEV and then PROD
One portal feature is built on a Dell in that box's own worktree and branch. Coarse grain: one feature, one box, one page; the
dell2 Investor Reporting pages are the natural first case. It waits as a candidate. Andrew approves it. Only then does it merge
forward to DEV. The next PROD promote carries it, and carries nothing on DEV that was not approved. A person can follow this
one feature from the box where it was built to the page a client opens, and read who approved it and when. This is FWD-1 at L2.

### O2 -- Andrew sees every feature waiting for his approval in one place, and approves or declines one in one act
A pending feature names the box it came from, the pages it changes, whether those pages are client-facing, and how to look at
it before saying yes (a preview build or the DEV site). His answer is recorded where the merge-forward reads it.

### O3 -- Each box builds portal changes in its own worktree and branch, and no box writes DEV directly
A seat on any box can say which branch its feature lives on and that nothing of it is on DEV until approved. The "who may push
DEV" exceptions in Part IV all become the one approved merge-forward.

### O4 -- Anyone can tell, for every commit on DEV, which approved feature it belongs to and who approved it
DEV holds only approved work. A commit on DEV with no approval behind it is visible as such, not silently mixed in.

### O5 -- A PROD promote ships only approved, finished features
The promote can no longer carry a half-done or unapproved change to clients because it happened to be on DEV at promote time.
Today the promote merges live DEV whole (Part IV, F4).

### O6 -- The backlog is settled once, by Andrew's decision per feature group, and DEV and PROD agree again
The current backlog:
- 201 commits on DEV that PROD lacks;
- 32 commits on PROD that DEV lacks;
- 9 branches with work not on DEV.

Each group is approved forward, held on its branch, or dropped. PROD-only work is folded back so DEV is again the one source
for the next promote.

### O7 -- The approval line is stated: what needs Andrew's word, what a box's lead approves, and what needs none
A seat building a test-only change, an Opal-internal page or a client-facing page knows before it starts whose approval its
feature needs. It is the same three classes the push law already uses (Part IV, F3).

## PART II -- WHERE THE BOUNDARY SITS

- **NFRA_DEVPLN owns:** the per-box portal branch rule, what a "feature" and an "approval" are, the record of approvals, the
  approved merge-forward to DEV, the approved-only PROD promote, and the one-time settlement of the current DEV/PROD backlog.
- **NFRA_CTLPLN (laptop) keeps** box roles, the push gate's general shared-branch rules and the integrator. NFRA_DEVPLN changes
  only the portal DEV/PROD limbs of `.tools/hooks/never-rules-gate.sh`. That shared file needs one writer per change, ruled by
  `1.0.0_SA_CTO`. Andrew split this from CTLPLN on purpose: no CTLPLN outcome is re-opened here.
- **COMM_ASSIST (site Z)** may be where Andrew's approval arrives (Teams/phone). If so, it is a dependency, not owned here.
  Andrew already approves ad hoc work "at my discretion over that COMMS_ASSIST channel" (same record, item 4).
- **`/prod-deploy` (the DT promote skill)** is changed by O5, not replaced.
- **The product projects that write portal pages** are the feature producers this governs; their own outcomes are untouched:
  DSGN_IRPTV1, IRPT_ANLREQ, IRPT_DASHBD, AMGT_RESAPP, TCKT_VNEXT, MDPF_SECCLASS, ADVI_FIRMBKTS.
- **Portal CI (VALGATE)** keeps running on every push; NFRA_DEVPLN does not own it.
- **Not in scope:** opal_ai and mcportal (Andrew named portal DEV only); the workspace repo's own `box/*` -> `CLOUD` flow.

## PART III -- THE QUALITATIVE BAR

- Andrew can say, of any page a client sees on PROD, "I approved that", and point to where he did.
- A Dell seat building a feature never has to ask whether it may push DEV: the answer is always "not until approved", and the
  route to approval is one step it can take on its own.
- A promote is a decision Andrew can make with a list in front of him, not a merge whose contents nobody chose.
- The approval step costs Andrew less attention than reviewing PROD after the fact does today. If it costs more, the line in O7
  is drawn in the wrong place.

## PART IV -- THE SUBSTRATE (findings, measured 2026-10-13 ~14:1xZ-14:2xZ)

- **F1 -- Who may push portal DEV today is four separate admissions, not one rule** (`.tools/hooks/never-rules-gate.sh`):
  - the integrator MSTR (the base rule);
  - a DT seat, for DEV and PROD (the "DT PORTAL-PROD CARVE-OUT", widened to DEV 2026-09-02);
  - the seat of a live FAST lease, for DEV ("FAST-LEASE PORTAL-DEV CARVE-OUT", Andrew-approved 2026-09-24);
  - any author of a test-only fast-forward ("TEST-ONLY PORTAL-DEV CARVE-OUT", 2026-09-24 cut 2).

  `org/mcp/drive_mode/` holds 8 lease files; their expiry was not read.
- **F2 -- DEV is written by many seats on several boxes.**
  - Committers of the 201 DEV-not-PROD commits: `2.0.0_SA_COO~D2` 30, `2.0.0_SA_COO~D1` 19, `0.9.0_WK_IRPT_ANLREQ~51` 14,
    `0.0.0_AB_MSTR~DELL1` 14, `2.0.0_SA_COO~Y2` 12, DSGN_IRPTV1 workers 22+, `2.0.0_SA_COO~P2` 8.
  - Workers merge `DEV` into their own `wk-*` branches and back.
  - Nothing on DEV records an approval.
- **F3 -- The law already has a three-class approval line** (CLAUDE.md, Portal and Agent Autonomy sections):
  - a candidate touching no product file lands on DEV by its author;
  - a product candidate is CTO-reviewed;
  - only a PROD push changing a client-facing page waits on Andrew ("unsure = client-facing").

  O7 can re-use this line rather than invent one.
- **F4 -- The promote ships DEV whole.** `.claude/skills/prod-deploy/SKILL.md`: "The promote merges LIVE `origin/DEV` at GO time
  -- it is NOT a frozen snapshot." No step selects features.
- **F5 -- DEV and PROD have diverged both ways.** DEV is 201 commits ahead of PROD; PROD is 32 ahead of DEV (the `AV-zzs-1` /
  `AV-zzr-1` Security Analysis work by `0.9.0_WK_DSGN_AMGTV1~141/~142`, PROD tip 37aa1247, 2026-10-09). The merge base is
  2d42e9b733, so PROD took work that never passed DEV. DEV tip is f6ef1d25 (2026-10-13 09:39 ET).
- **F6 -- What the 201 touch**, by file count from the PROD...DEV diff:
  - `pages/InvestorReporting` 143;
  - `pages/SecurityAnalysis` 51;
  - `pages/TicketCenter` 19;
  - `pages/AdvisorIntelligence` 4;
  - `api/endpoints` 3;
  - `lib/firmAccess.ts` 1, NFRA_CTLPLN's carrier 53506d49, held from PROD by Andrew's call today.

  InvestorReporting and TicketCenter may open to partner logins, so they are client-facing by the unsure rule.
- **F7 -- Branches already exist per worker, not per box, and nothing names an approved one.**
  - The 50 remote branches: `wk-*` 27, `cand-*` 5, `q/<box>/...` 4, `irpt-*` 3, plus `feature/`, `sitez/`, `demo`, `backup`,
    `experiment`, `testing`, `main`.
  - 9 have commits not on DEV:
    - `cand-dell1-secclass-e53-r9` +4;
    - `cand-dell1-secclass-e59-r10` +2;
    - `irpt-dev-candidate-3-20260924` +3;
    - `irpt-dev-candidate-7-20260924` +1;
    - `irpt-opal-scope-p-portal-20260923` +1;
    - `q/dell2/wk-IRPT_BCKEND-167-portal/r1` +2;
    - `sitez/merge-trial-20260915` +2;
    - `wk-IRPT_ANLREQ-51-portal-r4` +1;
    - `wk-dsgn-irptv1-r25-61-prodcut` +34.
  - The `cand-` and `q/<box>/` prefixes are the closest prior art to "a box's candidate waiting for approval".
- **F8 -- A selective PROD cut has already been tried once:** `wk-dsgn-irptv1-r25-61-prodcut` (+34 over DEV, 2026-10-11). It is
  prior art for O5; how it was cut and whether it shipped was not read.

## PART V -- WHAT MUST BE TRUE (named, not sequenced)

- A definition of "feature": the unit Andrew approves, most naturally one branch with a stated purpose and its pages.
- A place approvals are recorded that the merge-forward and the promote can both read.
- A way for Andrew to look at a feature before approving it: DEV preview, a per-branch preview build, or a screenshot walk.
- The gate's four DEV admissions (F1) reconciled into the approved route, through `1.0.0_SA_CTO` as the one writer of that file.
- `/prod-deploy` able to promote a chosen set rather than live DEV whole.
- The PROD-only 32 folded back into DEV. No rebase on a shared branch is permitted (CLAUDE.md hard stop); a merge is the route.
- Each box's portal worktree convention, so every box answers O3 the same way.
- The owner of each DEV commit's feature identified for the backlog settlement (O6).

## PART VI -- STATUS (NOT OUTCOME-BEARING; measured 2026-10-13 ~14:1xZ-14:2xZ, portal origin fetched)

- DEV 201 ahead of PROD, PROD 32 ahead of DEV; 50 remote branches, 9 with work not on DEV.
- The laptop portal checkout has 4 worktrees.
- A whole-DEV promote is on hold on Andrew's ~14:0xZ answer: the REC "hold until this brief lands" was not refused.
- dell1's open call `dell1-20261011T033643Z-e7f2` (AMGT_RESAPP empty-state card, Opal-internal) waits on the same promote.

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- Ownership of each `wk-*` branch was not checked, nor whether its work is already on DEV under another commit.
- The 8 FAST lease files' expiry, and so whether any seat may push DEV right now, were not read.
- Portal CI state on DEV and PROD was not read.
- How the Dells hold their portal checkouts (nested checkout, separate clone, worktrees) was not inspected on those boxes; only
  their branch names are seen.
- Whether Andrew wants approval per feature or per promote is not settled. O2 assumes per feature because his words say
  "approval on before merging forward to DEV". It is the first open decision below.
- No number is set for how long a feature may wait for approval.

## OPEN DECISIONS FOR ANDREW (each with the CRO's recommendation)

1. **What one approval covers.** (a) one feature (a branch and its pages); (b) one commit; (c) one promote.
   **REC (a)** -- his words name features, and a promote of approved features follows from it.
2. **Who approves which class.** (a) Andrew approves every feature; (b) Andrew approves client-facing features, the box's CTO
   approves Opal-internal pages, test-only changes need no approval (the line in F3).
   **REC (b)** -- it keeps his attention on what clients see and matches the law already in force.
3. **Where he approves.** (a) the open-calls list he already reads; (b) a Teams/phone reply through COMM_ASSIST; (c) a portal
   page.
   **REC (a)** first, (b) once COMM_ASSIST carries it -- (a) exists today and every box already writes to it.
4. **The 201 DEV commits already there.** (a) accept DEV as the baseline after Andrew reviews it by feature group (Investor
   Reporting, Security Analysis, Ticket Center, Advisor Intelligence, firm access list); (b) rebuild DEV from PROD plus approved
   groups only.
   **REC (a)** -- (b) re-writes a shared branch the law forbids rebasing and risks losing work; the approval rule applies from
   the settlement forward.
5. **The 32 PROD-only commits.** Merge PROD back into DEV once, so DEV is again the single source.
   **REC yes**, and any future PROD-direct fix follows the same back-merge.

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md
  PROJECT           NFRA_DEVPLN (named by Andrew; not yet registered -- L3, 1.0.0_SA_CTO), placement laptop
  EXISTING PRD      NONE
  SIBLING PROJECTS  NFRA_CTLPLN (gate file, push law), COMM_ASSIST (approval channel), the portal producers in Part II
  PRIOR ART         never-rules-gate.sh DEV/PROD carve-outs (F1); CLAUDE.md three-class line (F3); /prod-deploy (F4);
                    cand-*/q/<box>/ branch naming (F7); wk-dsgn-irptv1-r25-61-prodcut (F8)
  MEASURED AT       2026-10-13 ~14:1xZ-14:2xZ UTC, portal origin fetched by 4.0.0_SA_CRO on the laptop
```
