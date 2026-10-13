# NFRA_DEVPLN -- per-box portal DEV work, approved before it reaches DEV, so PROD carries only approved features

```json
{
 "project": "NFRA_DEVPLN",
 "directive": "D0",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md@5386676d4f",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO` (L2-L4), 2026-10-13. **Owner:** `1.0.0_SA_CTO`. **COO lane:** the third laptop lane, seated by `0.0.0_AB_MSTR`
on this PRD. **Macro:** NFRA (D0). **Registered** @a9280cac15 (tree row `org/missions/D0/NFRA/NFRA_DEVPLN/project.json`).
**Brief:** `docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md` @5386676d4f (`4.0.0_SA_CRO`, measured on the
laptop 2026-10-13 ~14:1xZ-14:2xZ with the portal origin fetched).
**Andrew's words** (records in `org/tier1_exec/`):
- the commission, ~13:5xZ via `2.0.0_SA_COO~C` (`2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_135xZ_PER_BOX_PORTAL_DEV_BRIEF_REQUEST.md`):
  "What should be happening moving forward is that each Box has its own worktree and it must get approval on before merging forward
  to DEV. that way we can do PROD promotes with only approved DEV features."
- the project, ~14:0xZ (`4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md` @90867982ed):
  "get this brief sorted and folded in as a laptop project NFRA_DEVPLN. I want it separated from CTLPLN because CTLPLN is getting too large";
- the five decisions, ~14:3xZ (`4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md` @0ecb2dd97e):
  "yes agreed for all of this";
- the endpoint, ~16:0xZ at the `1.0.0_SA_CTO` terminal (`1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_160xZ_NFRA_DEVPLN_ENDPOINT_CONFIRMED_ALL_AGREED_PROCEED.md`):
  "All agreed, proceed."
**Sign-off:** `3.0.0_SA_CVO~L` signs the ratified-text half (ENDPOINT + CONTRACTS); the brief half is accepted because the CRO wrote the brief.

## ENDPOINT (step 2, /endpoint --forward)

Carried verbatim from `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_DEVPLN_ENDPOINT_FORWARD_20261013.md` @a9280cac15, CONFIRMED by
Andrew ~16:0xZ. FWD-1 is the thread (spine v3.16-3.18); round 1 decomposes over its hops; FWD-2..FWD-7 are enrichment.

```
  FWD-1  One portal feature built on a Dell in that box's own branch is approved by Andrew, then
         reaches DEV, then reaches a client's page through a promote that carries nothing unapproved
         DONE WHEN  EXERCISED -- one real feature followed from the box where it was built to the page
                    a client opens, with its approval read along the way
         ACCEPT     a feature from one box waits as a candidate, is approved by Andrew in one act, only
                    then lands on DEV, and goes out in the next promote; a person can follow that one
                    feature from the box to the client's page and read who approved it and when; a
                    promote that also carried something nobody approved fails it
         SOURCE     brief O1, the candidate thread (the dell2 Investor Reporting pages named as the
                    natural first case)

  FWD-2  Andrew sees every feature waiting for his word in one place and answers each in one act
         DONE WHEN  EXERCISED -- one feature approved and one declined from that list, each answer read
                    back by the box that asked
         ACCEPT     each waiting feature names the box it came from, the pages it changes, whether those
                    pages are client-facing, and how to look at it first; his answer lands where the
                    merge-forward reads it, and a declined feature stays on its branch; the list is the
                    open-calls list he already reads, from whichever box he is at
         SOURCE     brief O2; decision 3 (a)

  FWD-3  Every box builds portal changes in its own worktree and branch, and no box writes DEV
         directly
         DONE WHEN  EXERCISED -- one direct DEV push from a box seat refused, and the same work landing
                    through the approved route
         ACCEPT     a seat on any box can say which branch its feature lives on and that none of it is on
                    DEV until approved; the separate admissions that let a seat push DEV today become the
                    one approved merge-forward; a seat never has to ask whether it may push DEV
         SOURCE     brief O3; Part IV F1 (the four admissions); Part III bar 2

  FWD-4  For every commit on DEV, anyone can tell which approved feature it belongs to and who
         approved it
         DONE WHEN  APPLIED -- the record in place and readable for every commit that lands after it
         ACCEPT     a commit on DEV with no approval behind it is visible as such, never silently mixed in
                    with approved work
         SOURCE     brief O4

  FWD-5  A promote to PROD ships only approved, finished features
         DONE WHEN  EXERCISED -- one promote that carried a chosen set of approved features and left an
                    unapproved change on DEV behind
         ACCEPT     the person running the promote has a list of what goes in front of them, and a
                    half-done or unapproved change on DEV at promote time does not reach clients
         SOURCE     brief O5; Part IV F4 (the promote ships DEV whole today); decision 1 (a)

  FWD-6  The backlog is settled once, and DEV and PROD agree again
         DONE WHEN  EXERCISED -- Andrew's decision recorded per feature group, PROD's own work folded back,
                    and the two trunks read as one line of history from there
         ACCEPT     each group of work now on DEV but not PROD (Investor Reporting, Security Analysis,
                    Ticket Center, Advisor Intelligence, the firm-access change) is approved forward, held
                    on a branch, or dropped, by Andrew's word per group; the work on PROD that never
                    passed DEV is merged back so DEV is again the one source for the next promote; the
                    branches holding work not on DEV are each approved, held or dropped; nothing is
                    rewritten, nothing is lost
         SOURCE     brief O6; Part IV F5-F8; decisions 4 (a) and 5 (yes)

  FWD-7  Before starting, a seat knows whose approval its feature needs
         DONE WHEN  APPLIED -- the line stated where every box reads it, and the gate that admits a DEV
                    merge reads the same line
         ACCEPT     a client-facing feature waits for Andrew; an Opal-internal page waits for the box's
                    CTO; a test-only change waits for nobody; "unsure" is client-facing; the approval
                    step costs Andrew less attention than reviewing PROD after the fact does today
         SOURCE     brief O7; Part IV F3 (the law's three classes); Part III bar 4; decision 2 (b)
```

## CONTRACTS

Each contract names what must hold, who holds it, and the measured state behind it. "Measured" cites the brief's Part IV finding;
"held" is a design this PRD sets and L5 cuts.

| contract | holder | text |
|---|---|---|
| C-FEATURE: the unit of approval (FWD-1, FWD-2, FWD-5) | this project | A FEATURE is one branch of the portal repo with a stated purpose and the pages it changes. Its name carries its box: `cand/<box>/<slug>` (the brief's F7 prior art `cand-*` and `q/<box>/...`, unified). One feature, one branch, one approval. A branch with no stated purpose is not a feature and cannot be approved. Decision 1 (a). |
| C-APPROVAL: where the word lives (FWD-2, FWD-4) | this project; the open-calls tools (read, not changed) | A feature waiting for approval is ONE row of kind `approval` on the building box's open-calls list (`org/devices/state/<box>/open_calls.json`, with its S3 cluster copy), carrying: box, branch, purpose, pages changed, class (client-facing / Opal-internal / test-only), how to look at it (the DEV site, a preview build, or a screenshot walk). Andrew's answer closes the row with `approved` or `declined` and his words; the row is the record the merge-forward and the promote read. A declined feature stays on its branch. The open-calls kind enum gains `approval` by a four-postulate record (rule 24) before the first row is written. Decision 3 (a); (b) through COMM_ASSIST is a later consumer of the same row (COMM_ASSIST FWD-8), never a second record. |
| C-BRANCH: every box builds in its own worktree and branch (FWD-3) | this project; each box's portal checkout | A portal change on any box is made in a linked worktree on a `cand/<box>/<slug>` branch and pushed to origin as that branch. Measured (F7): branches exist per worker (`wk-*` 27, `cand-*` 5, `q/<box>/` 4), none named as approved. The convention is stated in `portal/CONTRIBUTING-BOXES.md` (one page, every box reads it) and the worker skill's portal step names it. |
| C-MERGE-FORWARD: the one approved route onto DEV (FWD-3, FWD-4) | this project; `1.0.0_SA_CTO` the one writer of `.tools/hooks/never-rules-gate.sh` | DEV is written by one script, `.tools/portal-merge-forward.sh <branch>`, which refuses unless the branch's approval row reads `approved` (or the class needs no approval, C-CLASS) and then merges, never rebases, into DEV with a merge commit carrying `Feature: <branch>` and `Approved-By: <who> @<row id>` trailers. The gate's four DEV admissions (F1: integrator; DT seat; FAST-lease seat; test-only fast-forward) collapse to: the merge-forward script's commit, and the integrator for the settlement (C-SETTLE). The gate edit is one change by `1.0.0_SA_CTO` under NFRA_CTLPLN's shared-file rule (the brief's Part II). A DEV commit with no trailers is visible as unapproved by one read (`git log DEV --format=%b | grep -c Approved-By` against the commit count). |
| C-PROMOTE: a chosen set, never live DEV whole (FWD-5) | this project; `/prod-deploy` (changed, not replaced) | The promote takes a LIST of approved feature branches, merges them (and only them) into a release branch cut from PROD, and ships that branch; live DEV is never merged whole again. Measured (F4): today `/prod-deploy` merges live `origin/DEV` at GO time. Prior art (F8): `wk-dsgn-irptv1-r25-61-prodcut`. A promote whose list names an unapproved branch is refused by the script. The push law stands: a promote changing a client-facing page waits on Andrew's word; the list is what he reads. |
| C-CLASS: whose approval, stated once (FWD-7) | this project; CLAUDE.md's three-class line (read, not changed) | Client-facing feature: Andrew. Opal-internal page: the building box's CTO lane. Test-only change: nobody. "Unsure" is client-facing. The class is declared on the approval row by the builder and may be raised, never lowered, by the box CTO. The same line is read by `portal-merge-forward.sh` and by the promote. Decision 2 (b). |
| C-SETTLE: the backlog, once (FWD-6) | this project; `0.0.0_AB_MSTR` for the back-merge | Measured (F5, F6): DEV 201 ahead of PROD (InvestorReporting 143 files, SecurityAnalysis 51, TicketCenter 19, AdvisorIntelligence 4, api 3, firmAccess 1), PROD 32 ahead of DEV (merge base 2d42e9b733), 9 branches with work not on DEV. Settlement: (1) PROD is merged back into DEV once by the integrator (no rebase, CLAUDE.md hard stop); (2) Andrew rules each remaining DEV group forward / held / dropped from one list (the firm-access carrier 53506d49 already leaves by his word of ~14:3xZ, cherry-picked to PROD alone); (3) each of the 9 branches is approved, held or dropped by its owner's name; (4) from the settlement commit forward, C-MERGE-FORWARD binds. Decisions 4 (a) and 5 (yes). |

## 1. The arc

Round 1 builds the thread (FWD-1): one real feature on dell2's Investor Reporting pages (the brief's named first case) goes
branch -> approval row -> Andrew's word -> merge-forward -> chosen-set promote -> the client's page, with every hop a real call. The
settlement (FWD-6) is round 1's precondition for the promote hop: the first chosen-set promote can only be read as "nothing
unapproved" after PROD is folded back and the backlog ruled. Rounds 2+ enrich: the refused direct push (FWD-3's negative arm), the
per-commit read (FWD-4), the class line in the gate (FWD-7), the declined-feature arm (FWD-2).

## 2. Rounds

- **Round 1 (the thread + the settlement):** C-APPROVAL's enum record and first row; `portal-merge-forward.sh`; the gate's DEV limbs
  collapsed; `/prod-deploy --features <list>`; the back-merge and Andrew's group list; one real feature end to end.
- **Round 2:** FWD-3's refusal arm on every box; FWD-4's read; FWD-7's line in `CONTRIBUTING-BOXES.md` and the gate; FWD-2's declined
  arm.
- **Later:** the COMM_ASSIST consumer of approval rows (its FWD-8), a dependency on site Z's gateway, never owned here.

## 3. ENRICHMENT BACKLOG (ordered)

1. FWD-6 settlement first (the promote hop depends on it). 2. FWD-1 thread. 3. FWD-3 refusal arm. 4. FWD-4 per-commit read.
5. FWD-7 line. 6. FWD-2 declined arm. 7. FWD-5's second promote with an unapproved change left behind (the negative arm).

## 4. Engines

| engine | what it does | state |
|---|---|---|
| `.tools/open-calls.py` | the approval row (kind `approval`), its S3 copy, Andrew's close | measured, in use cluster-wide; enum widening owed |
| `.tools/portal-merge-forward.sh` | the one DEV writer; refuses without an approved row; merge with trailers | held (new, round 1) |
| `.tools/hooks/never-rules-gate.sh` DEV/PROD limbs | admits DEV only from the merge-forward commit and the integrator's settlement | measured (F1: four admissions); one edit by `1.0.0_SA_CTO` |
| `/prod-deploy` | chosen-set promote from a release branch cut from PROD | measured (F4: ships live DEV whole); changed in round 1 |
| portal CI (VALGATE) | runs on every push, unchanged | measured, not owned |

## 5. WORKSTREAMS AND OWNERS

One workstream, one issuer (the third laptop COO lane). Executors: workers in their own worktrees for the scripts and the
page; the integrator `0.0.0_AB_MSTR` for the PROD-into-DEV back-merge (the shared-branch act); a DT seat for the promote under the
push law; `1.0.0_SA_CTO` for the gate edit. The Dells build the first feature on their own portal checkouts under C-BRANCH; no Dell
pushes DEV.

## 6. Rulings closed at L4 (no decide-first question enters L5)

- DEC-1 feature = branch `cand/<box>/<slug>` with a stated purpose (decision 1 (a)).
- DEC-2 the approval record = an open-calls row of kind `approval` on the building box's list; its enum widening lands by a
  rule-24 record before the first row.
- DEC-3 DEV's one writer = `portal-merge-forward.sh`; merge, never rebase; trailers `Feature:` and `Approved-By:`.
- DEC-4 the promote = a list of approved branches merged into a release branch cut from PROD; live DEV is never merged whole.
- DEC-5 the settlement = PROD merged back into DEV once by the integrator; the DEV groups ruled by Andrew from one list; the 9
  branches dispositioned by name; 53506d49 already out by his word.
- DEC-6 the class line = CLAUDE.md's three classes, declared by the builder, raised only by the box CTO.
- DEC-7 scope = portal only (opal_ai and mcportal out, the brief's Part II); the workspace repo's `box/*` -> `CLOUD` flow is
  NFRA_CTLPLN's and untouched.
- DEC-8 no preview infrastructure is built in round 1: "how to look at it" is the DEV site or a screenshot walk; a per-branch
  preview build is a later enrichment on its own merit.

## 7. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-2, FWD-4 | `.tools/open-calls.py` kind enum + row fields for `approval`; `org/devices/state/<box>/open_calls.json` and its S3 copy | measured (in use; enum lacks `approval`) | C-APPROVAL | build | -- | one row per feature; the row is the record |
| S02 | FWD-3, FWD-4 | `.tools/portal-merge-forward.sh` (new) | held | C-MERGE-FORWARD | build | S01 | merge, never rebase; refuses without an approved row |
| S03 | FWD-3, FWD-7 | `.tools/hooks/never-rules-gate.sh` portal DEV/PROD limbs (lines ~643-760 today) | measured (F1) | C-MERGE-FORWARD, C-CLASS | build | S02 | one edit, one writer (`1.0.0_SA_CTO`); the other limbs untouched |
| S04 | FWD-5 | `.claude/skills/prod-deploy/SKILL.md` and its script: `--features <list>` mode, release branch from PROD | measured (F4) | C-PROMOTE | build | S02 | a promote naming an unapproved branch is refused |
| S05 | FWD-6 | portal `DEV` and `PROD` trunks: the back-merge commit; Andrew's group list; the 9 branches | measured (F5-F8) | C-SETTLE | wire | -- | integrator's act; no rebase; nothing deleted |
| S06 | FWD-3, FWD-7 | `portal/CONTRIBUTING-BOXES.md` (new, one page) and the worker skill's portal step | held | C-BRANCH, C-CLASS | build | -- | every box reads the same page |
| S07 | FWD-1 | one real feature on dell2's Investor Reporting pages, branch `cand/dell2/<slug>` | held | C-FEATURE | wire | S01-S06 | the thread's live trace |

## 8. BRIEF COVERAGE

O1-O7 -> FWD-1..FWD-7 one to one. Part II boundary -> DEC-7 and the holders column. Part III bar -> FWD-3 ACCEPT ("never has to
ask"), FWD-5 ACCEPT ("a list in front of them"), FWD-7 ACCEPT ("costs less attention"). Part IV F1-F8 -> the contracts' measured
cells. Part V -> S01-S07. Part VII (not claimed) -> the L5 battery reads what the brief did not: each `wk-*` branch's owner and
whether its work is already on DEV; the 8 lease files' expiry; portal CI state; how the Dells hold their checkouts. Open decisions
1-5 -> DEC-1..DEC-6, approved by Andrew ~14:3xZ.
