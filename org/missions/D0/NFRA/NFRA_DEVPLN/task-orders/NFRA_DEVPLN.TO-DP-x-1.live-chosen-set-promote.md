# TO NFRA_DEVPLN.TO-DP-x-1 -- round 2 ENRICHMENT DP-x-1: the first chosen-set promote -- one approved feature to PROD, nothing else, and both trunks measured after

<to_id>NFRA_DEVPLN.TO-DP-x-1</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.4.0_DT_ClientPlatform</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>ENRICHMENT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-x-1` (`decompositions/NFRA_DEVPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-1, FWD-5 |
**depends_on:** act A1 (the integrator pushes the approved merge to DEV); your first step checks it with a git command and STOPS if it is not true.

---

## WORKER FACE

### THE CELL

Portal PROD today (`origin/PROD` = `63c4f9e3`) is the whole-DEV promote of earlier today. From now on a promote ships a CHOSEN LIST of approved features, merged into a release branch cut from PROD, never live DEV whole. This is the first one.
The list has ONE feature: the branch `cand/laptop/contributing-boxes` (one commit `07f065e6`, a docs file `CONTRIBUTING-BOXES.md` in the portal repo root; no page a user opens, class opal-internal). Its approval row `laptop-20261013T200117Z-9e8a` reads `APPROVED valid=yes by=1.0.0_SA_CTO`.
`origin/DEV` carries 7 commits that PROD lacks (three IRPT_ANLREQ merges by a dell2 manager, no `Approved-By` trailer). They are NOT approved and must NOT go to PROD; leaving them behind is part of what this order proves.

### STEPS

1. PRECONDITION. `git -C portal fetch origin`, then `git -C portal log origin/DEV --format=%B | grep -c "Feature: cand/laptop/contributing-boxes"` must print 1 or more (the integrator has pushed the approved merge to DEV with its trailers). If it prints 0, STOP: do nothing, record `BLOCKED: DEV does not yet carry the approved merge` in your report. Do not push DEV yourself.
2. Open the change-management ledger entry (NEVER-2: opened at the start, closed at completion): `deploy_ledger.py open` as `.claude/skills/prod-deploy/SKILL.md` and `org/critical_paths/README.md` direct. Name the slug `devpln-r2-chosen-set-promote-20261013`.
3. Run the promote from `.claude/skills/prod-deploy/SKILL.md` in its CHOSEN-SET form: Step 4 runs `bash .tools/portal-release-build.sh --features cand/laptop/contributing-boxes` (it refuses unless the row is APPROVED valid, the head and commit count equal the row's, and the release's first-parent walk shows `unapproved=0`), keep its `PROMOTE-LIST` and `PROMOTE-CLIENT-FACING` lines for the receipt. Expect `PROMOTE-CLIENT-FACING count=0`: the push law (a PROD promote changing a client-facing page waits on Andrew) does not apply, and the receipt says so with the page class. Do NOT merge `origin/DEV` into PROD under any condition. Push, verify CI conclusion, and do the rest of the skill's steps as written.
4. MEASURE after the push and record verbatim in your report: `git -C portal rev-list --count origin/PROD..origin/DEV`, `git -C portal rev-list --count origin/DEV..origin/PROD`, and `git -C portal log -1 --first-parent --format=%B origin/PROD`. The first number should still include the 7 unapproved commits (plus the integrator's merge of the feature on DEV); if the two trunks differ by more than that, say so in a surprise row rather than fixing it.
5. Close the ledger entry. Write a short receipt (what shipped, the `PROMOTE-LIST` lines, the three measurements, the CI conclusion) to `org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/NFRA_DEVPLN.TO-DP-x-1.receipt.md`.

### RULES FOR THIS CELL

One feature, one promote. No other branch, no other path. A failed or half-landed promote is rolled back and escalated loud (NEVER-2), never left. The push law, the freeze-window rule and the DT-only check in the skill stand.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-DT-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPx1-AC1" cell_refs="DP-x-1"><invocation>git -C portal show origin/PROD:CONTRIBUTING-BOXES.md</invocation><expect># Contributing a portal feature from a box</expect></criterion>
`DPx1-AC1` -- the approved feature's file is on PROD (run `git -C portal fetch origin` first).

<criterion id="DPx1-AC2" cell_refs="DP-x-1"><invocation>git -C portal log -1 --first-parent --format=%B origin/PROD</invocation><expect>Approved-By: 1.0.0_SA_CTO @laptop-20261013T200117Z-9e8a</expect></criterion>
`DPx1-AC2` -- the PROD tip is the release merge, and it names who approved the feature and the row.
</proof_of_spec>

<expected_criteria>DPx1-AC1,DPx1-AC2</expected_criteria>

Each invocation runs under `timeout 120` from the workspace root. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/NFRA_DEVPLN.TO-DP-x-1.live-chosen-set-promote.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPx1-AC1,DPx1-AC2`, and flip `<status>` to `complete` only when both pass and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round2.md</decomp_doc>
<owned_cells>DP-x-1</owned_cells>
</decomp_ref>

<paths>
org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.4.0_DT_ClientPlatform/
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_DEVPLN/task-orders/NFRA_DEVPLN.TO-DP-x-1.live-chosen-set-promote.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
portal
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no IAM; the push is a git push to the portal PROD branch by the DT, admitted by the gate's DT carve-out.
comp-adversary: RUN over the order's own steps, BLIND to the filesystem around the cited paths. Findings inlined: DEV and PROD will each hold their own merge commit of the same feature afterwards (measured in step 4, not resolved); the 7 unapproved DEV commits stay behind by construction.
lane: the <paths> block IS the grant (worker RULING 1). The seat is Tier 2.
</preflight>

Source: L10 round analysis `ledger/ROUND_ANALYSIS.round1.md` @14a0501ee5 item 1; PRD `prd/NFRA_DEVPLN_PRD.md` v0.3 C-PROMOTE, C-CLASS; row `laptop-20261013T200117Z-9e8a` closed approved by 1.0.0_SA_CTO. SERVED: the CVO receives the L8 packet at the drain.
