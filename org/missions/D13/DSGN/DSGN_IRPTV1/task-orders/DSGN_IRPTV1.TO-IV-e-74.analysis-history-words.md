# TO DSGN_IRPTV1.TO-IV-e-74 -- The Analysis history says each request state in words, by client name; the READY row reads READY (S25 diagnosis, UIC-23)

<to_id>DSGN_IRPTV1.TO-IV-e-74</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~39</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E5 | **Decomp cell:** `IV-e-74` (decomp v9) | **outcome_ref:** FWD-7, FWD-11 | **depends_on:** none | **slot:** ~39, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-74` -- Rows (acceptance lines verbatim, PRD v0.18): UIC-23 "The list shows the viewer's own requests (or is labelled as all requests for an admin), each by client name, variant and date, with a status in words; a READY job reads Ready."

CTO ruling S25 (analysis section 2): diagnose first. Window 15's READY job REQ-67e12718 still reads 'Status unavailable' after IV-e-66 threaded the tenant; 2.0.0_SA_COO~Y 102052 measured the served irpt-status refusing that status-job read (a backend redeploy pending at ~P). Trace the history row's status read to the served answer (the committed walk HARs are gitignored on this device under org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/*.har; do not copy them into git) and name the file:line. If the page drops a good answer, fix it here. If irpt-status serves the wrong shape or scope, file a row naming it for 2.0.0_SA_COO~P and make the page say it in words. Either way the list says words, never `ANALYSIS_REQUIRES_ATTENTION` (FWD-11). File:line facts: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md` row UIC-23 (OwnedRequestHistory.tsx :75-80, :204, :219).

**Build:** Each row reads the client name and the state in words; the diagnosis (file:line) goes in your result.

**Amendment 1 (issuer, 2026-09-28 ~00:4xZ; windows 19-20, rows S25/S28, CTO 102271):** the S25 diagnosis is SETTLED and is backend:
window 20 (local DEV 12aa026a) read REQ-67e12718's status through the page three times and got HTTP 500; 2.0.0_SA_COO~Y 102268 traced it
to the status role lacking the original-holdings read grant and a stale errors.py that turned every refusal into a 500. irpt-status is
rolled back (it answers named refusals again; REQ-67e12718 now answers a named DATE_BASIS refusal) and rebuild 3 lands after 05:00Z at
2.0.0_SA_COO~P. So this cell does NOT diagnose further; the page states whatever the served read answers IN WORDS (a READY row reads
Ready; a named refusal such as DATE_BASIS or FIRM_BINDING reads its reason in words; a failed read reads "status could not be
confirmed"). Row S28's page half is ADDED here: `tabs/analysis/ProspectJobStatus.tsx` `readJobStatus` (:16-18) calls
`api.getJobStatus(requestId)` with NO selected tenant, while the history row's read (`OwnedRequestHistory.tsx` `readRowStatus` :32-33)
carries it; ~Y 102268 measured the tenant-less reads as refused (IdRefused). Thread the same selected tenant into the opened request's
status read (`OwnedRequestHistory.tsx` :232 mounts `ProspectJobStatus`; `ProspectComposer.tsx` :256 mounts it for a fresh submit and
stays as it is unless it already holds the tenant). IV-e-75 edits tabs/analysis/* after you, on the same slot.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE74-AC1" cell_refs="IV-e-74"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-39/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-74.history-words.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: ANALYSIS-HISTORY-WORDS-OK</expect></criterion>
`IVE74-AC1` -- the built behaviour: (a) a READY row reads READY; (b) an ATTENTION row reads its reason in words and never ANALYSIS_REQUIRES_ATTENTION; (c) each row names the client; (d) opening a request issues its status read carrying the same selected tenant as the row read (S28); control: a refused status read says so in words. Print `VERDICT: ANALYSIS-HISTORY-WORDS-OK` only when every arm holds.
<criterion id="IVE74-AC2" cell_refs="IV-e-74" judgment="true"/>
`IVE74-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE74-AC1, IVE74-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx
portal/src/pages/InvestorReporting/tabs/analysis/ProspectJobStatus.tsx
portal/src/pages/InvestorReporting/tabs/analysis/tests/prospect.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-74.history-words.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-66.owned-item-tenant.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-74`.
<owned_cells>IV-e-74</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE74-AC1, IVE74-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~39/DSGN_IRPTV1.TO-IV-e-74.analysis-history-words.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE74-AC1,IVE74-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W39-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~39, queue position 1 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 39 --path <abs> --portal-ref <DEV at seating>`.
