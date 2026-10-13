# ENDPOINT (step 2, /endpoint --forward) -- NFRA_DEVPLN: per-box portal DEV work, approved before it reaches DEV, so PROD carries only approved features

Author `1.0.0_SA_CTO`, 2026-10-13 ~14:3xZ. **STATUS: EMITTED; the brief's five decisions APPROVED by Andrew ~14:3xZ at the CRO
terminal** (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_143xZ_DEVPLN_RECS_APPROVED_AND_COMM_ASSIST_THROUGH_MUSE.md`
@0ecb2dd97e, "DEVPLN decisions a-e approved"); **the seven DONE WHEN lines are CONFIRMED by Andrew ~16:0xZ at this terminal, VERBATIM "All agreed,
proceed."** (record `ANDREW_DIRECT_20261013_160xZ_NFRA_DEVPLN_ENDPOINT_CONFIRMED_ALL_AGREED_PROCEED.md`; the one L2 touch that is his:
"i will confirm CTO's 'DONE WHEN' from their /endpoint --forward", Andrew-direct 2026-09-03). The PRD carries this section verbatim. Registered at L3 in the same
commit as a laptop project under D0 on his word of ~14:0xZ ("get this brief sorted and folded in as a laptop project NFRA_DEVPLN.
I want it separated from CTLPLN because CTLPLN is getting too large", record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md`
@90867982ed). His commissioning words, relayed by `2.0.0_SA_COO~C` (`ANDREW_DIRECT_20261013_135xZ_PER_BOX_PORTAL_DEV_BRIEF_REQUEST.md`):
"What should be happening moving forward is that each Box has its own worktree and it must get approval on before merging forward
to DEV. that way we can do PROD promotes with only approved DEV features."

**Brief read:** `docs/briefs/nfra-devpln-per-box-portal-dev-approval-brief-20261013.md` @5386676d4f (`4.0.0_SA_CRO`, 192 lines, read in
full; substrate measured 14:1xZ-14:2xZ on the laptop with portal origin fetched).

**The brief's five open decisions, ruled on the CRO's recommendations** (self-drive Step 1: the driver rules on the REC; each is a
design choice inside the scope his words set, not a widening). They are written into the outcomes below, so his confirmation of the
DONE WHEN lines confirms them; any he changes re-words the outcome in place.

| decision | ruling |
|---|---|
| 1. what one approval covers | (a) one feature: one branch with a stated purpose and its pages |
| 2. who approves which class | (b) Andrew approves a client-facing feature; the box's CTO approves an Opal-internal page; a test-only change needs no approval (the push law's three classes, unchanged) |
| 3. where he approves | (a) the open-calls list he already reads, from any box; (b) a Teams or phone reply through COMM_ASSIST once that channel carries it, a dependency on site Z, not owned here |
| 4. the DEV backlog | (a) DEV becomes the baseline after he reviews it by feature group; no rebuild of a shared branch |
| 5. the PROD-only commits | yes: PROD merged back into DEV once, and every later PROD-direct fix follows the same back-merge |

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

**Provenance.** READ: the brief in full @5386676d4f; Andrew's two records (@90867982ed and COO~C's 135xZ relay); CLAUDE.md Portal and
Agent Autonomy sections (the three-class line). NOT READ: the register, any task order, any project JSON, `never-rules-gate.sh`'s
bytes, `/prod-deploy`'s skill text, the portal branches themselves (the brief measured them; the L4 PRD re-reads what it builds on).

**Boundary carried from the brief, PART II:** NFRA_CTLPLN keeps box roles and the gate's general rules; NFRA_DEVPLN changes only the
portal DEV/PROD limbs of `.tools/hooks/never-rules-gate.sh`, one writer per change ruled by `1.0.0_SA_CTO`; COMM_ASSIST (site Z) is
a dependency for FWD-2's second channel; the portal producers' own outcomes are untouched; opal_ai and mcportal are out of scope.

**What waits on Andrew (L2):** confirm the seven DONE WHEN lines, or re-word any. Then L4 (the PRD) is this seat's, and
`0.0.0_AB_MSTR` seats a COO lane on the laptop for L5/L6 (the laptop holds one live COO, `2.0.0_SA_COO~C`, on NFRA_CTLPLN).
