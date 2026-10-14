# TO NFRA_DEVPLN.TO-DP-y-1 -- round 8 ENRICHMENT DP-y-1: the client-facing chosen-set promote -- the five dell2 features Andrew approved go to PROD, nothing else, and both trunks measured after

<to_id>NFRA_DEVPLN.TO-DP-y-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.4.0_DT_ClientPlatform</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-y-1` (`decompositions/NFRA_DEVPLN_DECOMP.round8.md`) | **outcome_ref:** FWD-1, FWD-5, FWD-7 |
**depends_on:** act A14a (the integrator pushes the merge-forward of `3635` and `7773` to DEV); your first step checks it with git commands and STOPS if it is not true.

---

## WORKER FACE

### THE CELL

Portal PROD today (`origin/PROD` = `7db035e4`) holds four approved features, each a release merge in the first-parent line since the settlement `63c4f9e3`. A promote ships a CHOSEN LIST of approved features, merged into a release branch cut from PROD, never live DEV whole. This promote ships FIVE client-facing features, all dell2 branches, all approved by Andrew himself (his word of 2026-10-14 ~11:4xZ, rows 1-3 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`; each row reads CLOSED `by=andrew decision=approved`). The push law's client-facing hold is satisfied by that word; your receipt names the five rows.

| branch | row | head |
|---|---|---|
| `cand/dell2/anlreq-90-held-submit` | `dell2-20261013T222707Z-8500` | `794b7df495d2` |
| `cand/dell2/anlreq-88-advisory-fee` | `dell2-20261013T222709Z-7b45` | `9ef6a359b807` |
| `cand/dell2/anlreq-87-model-order` | `dell2-20261013T222710Z-fde0` | `62d455f57525` |
| `cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal` | `dell2-20261013T221411Z-3635` | `030737656431` |
| `cand/dell2/partner-firm-stack` | `dell2-20261013T231910Z-7773` | `1c71bfd8e1a5` (21 commits) |

`origin/DEV` carries commits that PROD lacks and Andrew has NOT approved (the DEV tip is `ab8ecc56`; run `git -C portal log --first-parent --format='%h %an %s' origin/PROD..origin/DEV` and read the lines with no `Approved-By` trailer). They must NOT go to PROD.

### STEPS

1. PRECONDITION. `git -C portal fetch origin`, then both of these must print 1 or more: `git -C portal log origin/DEV --format=%B | grep -c "Feature: cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal"` and `git -C portal log origin/DEV --format=%B | grep -c "Feature: cand/dell2/partner-firm-stack"` (the integrator has pushed those two approved merges to DEV with their trailers). If either prints 0, STOP: do nothing, record `BLOCKED: DEV does not yet carry the approved merge of <branch>` in your report. Do not push DEV yourself. Then, for each of the five branches, `python .tools/open-calls.py approval-status --branch <branch>` must print `state=APPROVED valid=yes` with the head in the table; any other line stops the order.
2. Open the change-management ledger entry (NEVER-2: opened at the start, closed at completion): `deploy_ledger.py open` as `.claude/skills/prod-deploy/SKILL.md` and `org/critical_paths/README.md` direct. Slug `devpln-r8-client-facing-chosen-set-promote-20261014`. Name the portal CI run in the entry once it exists.
3. Run the promote from `.claude/skills/prod-deploy/SKILL.md` in its CHOSEN-SET form: Step 4 runs `bash .tools/portal-release-build.sh --features <the five branches>` in this order: `anlreq-90-held-submit`, `anlreq-88-advisory-fee`, `anlreq-87-model-order`, `irpt-ytd-from-first-day-and-wider-export-modal`, `partner-firm-stack`. It refuses unless every row is APPROVED valid, every head and commit count equals its row's, and the release's first-parent walk shows `unapproved=0`. Keep its `PROMOTE-LIST` and `PROMOTE-CLIENT-FACING` lines for the receipt (expect `count=5`). If the build refuses or a merge conflicts, STOP and report the refusal verbatim: do not edit a branch, do not drop one, do not reorder to get past it. Do NOT merge `origin/DEV` into PROD under any condition. Push, verify the CI conclusion on the pushed sha, and do the rest of the skill's steps as written.
4. MEASURE after the push and record verbatim in your report: `git -C portal rev-list --count origin/PROD..origin/DEV`, `git -C portal rev-list --count origin/DEV..origin/PROD`, `git -C portal log --first-parent --format='%h %s' 7db035e4..origin/PROD`, and `bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e35f259ad76071b1099aeb9dddb150409f`. If the trunks differ by more than DEV's unapproved commits plus each side's own merge of the same feature, say so in a surprise row rather than fixing it.
5. Close the ledger entry. Write a short receipt (what shipped, the `PROMOTE-LIST` and `PROMOTE-CLIENT-FACING` lines, the five rows, the measurements, the CI conclusion) to `org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/NFRA_DEVPLN.TO-DP-y-1.receipt.md`.

### RULES FOR THIS CELL

Five features, one promote. No other branch, no other path. A failed or half-landed promote is rolled back and escalated loud (NEVER-2), never left. The push law, the freeze-window rule and the DT-only check in the skill stand.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-DT-S<k>`, next unused k, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPy1-AC1" cell_refs="DP-y-1"><invocation>bash .tools/portal-release-build.sh --check PROD --repo portal --prod-ref 63c4f9e35f259ad76071b1099aeb9dddb150409f</invocation><expect>unapproved=0 ref=refs/remotes/origin/PROD</expect></criterion>
`DPy1-AC1` -- PROD's first-parent line since the settlement holds no unapproved feature and the check reads `origin/PROD` (run `git -C portal fetch origin` first). AMENDED 2026-10-14 by the issuer: the first version also counted `features=9`, a moving target (another box's approved release landed on PROD after this promote, so the count read 10); the five features are counted by `DPy1-AC2`.

<criterion id="DPy1-AC2" cell_refs="DP-y-1"><invocation>bash -c 'git -C portal log origin/PROD --first-parent --format=%B | grep -c "Approved-By: andrew @dell2-"'</invocation><expect>^5$</expect></criterion>
`DPy1-AC2` -- exactly five release merges on PROD name Andrew as the approver, each with its dell2 row.

<expected_criteria>DPy1-AC1,DPy1-AC2</expected_criteria>

Each invocation runs under `timeout 120` from the workspace root. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/NFRA_DEVPLN.TO-DP-y-1.client-facing-chosen-set-promote.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPy1-AC1,DPy1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round8.md</decomp_doc>
<owned_cells>DP-y-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-y-1.client-facing-chosen-set-promote.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
portal
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the push is a git push to the portal PROD branch by the DT, admitted by the gate's DT carve-out.
comp-adversary: RUN over the order's own steps, BLIND to the filesystem around the cited paths. Findings inlined: `partner-firm-stack` carries 21 commits that may overlap the three ANLREQ branches, so the order is the three first and the stack last, and a conflict stops the order rather than being resolved; the three unapproved ANLREQ direct merges stay on DEV by construction.
lane: the <paths> block IS the grant (worker RULING 1). The seat is Tier 2.
</preflight>

Source: `ledger/ROUND_ANALYSIS.round7.md` section 3 item 2 and 1.0.0_SA_CTO msg 109118 ("cut the integrator's merge-forward of each approved feature and the DT's chosen-set promote naming only those; client-facing, SERVED, L8 packet"); Andrew's word recorded at `ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md`. SERVED: the CVO receives the L8 packet at the drain.
