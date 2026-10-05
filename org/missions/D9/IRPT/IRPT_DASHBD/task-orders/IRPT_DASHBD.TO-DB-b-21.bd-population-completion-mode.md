# TO IRPT_DASHBD.TO-DB-b-21 -- the ONE Black Diamond pull's completion mode: the complement only, the bearer re-minted before it expires (E3, batch 248)

<to_id>IRPT_DASHBD.TO-DB-b-21</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~7</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 248 (msg 105044): the completion run over the accounts
not yet answered IS the same pull; on a bearer expiry it re-mints and refreshes before the measured expiry, requests only the
complement, and prints both denominators. The issuer's cause read (msg to the CTO 00:21Z) found the class (a) bearer expiry: the
first bearer died after 18 calls (~9 s), and a fresh bearer answered 200 for the same account. | **Decomp cell:** `DB-b-21`
(decomposition section 13) | **outcome_ref:** P-5 (FWD-8's population tie-out) | **depends_on:** DB-b-20 (merged @5a671b2aba).

THIS CELL MAKES NO VENDOR CALL. The issuer runs the completion.

---

## WORKER FACE

**What exists.** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/bd_population_pull_e3.py` (DB-b-20) and its plan
`BD_POPULATION_PLAN_E3.json` (5,252 requests) are the pull. Its live run aborted at call 19 on HTTP 401: the ClientView bearer
expired. The pull record is `BD_POPULATION_PULL_E3.json` in that folder. Landed responses are under
`s3://opal-data-assets/blackdiamond/49financial/bronze/reporting_performance/pull=20261004/acct=<bd_internal_id>.json`, 19 at the cut.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-dashbd-7`. Run everything from its root.

**What you build**, under `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~7/`:
1. **`bd_population_complete_e3.py`.** It imports the DB-b-20 script's functions by path; do not copy them. Two modes:
   - **`plan`** stays OFFLINE under DRY_RUN=1, with S3 list reads only. It reads the DB-b-20 plan, lists the landed keys under
     `pull=20261004`, and writes `BD_POPULATION_COMPLETION_PLAN_E3.json` with:
     - `requests_planned` (5252), `landed` and `landed_accounts` (the bd ids read from the keys);
     - `complement` and `complement_accounts` (the plan's requests minus the landed set);
     - `vendor_calls: 0` and `dry_run`.

     It prints both denominators.
   - **`run --go`** (LIVE; the issuer runs it, never you). It refuses unless `--go` is given, the completion plan exists and is
     re-derived identically, and the DB-b-20 folder's `E3_SHAPE_RULING.json` exists. Then:
     - it requests ONLY the complement accounts, each once;
     - pace is the ruling's (2 req/s);
     - it re-mints the bearer through the same 49F sign-in path every 10 calls, before the measured ~18-call expiry;
     - one transient retry per run;
     - it aborts the whole run on the first non-transient error;
     - a 401 directly after a fresh mint is a stop, not a retry;
     - each response lands at the builder's address under `pull=20261004`;
     - it writes `BD_POPULATION_COMPLETION_E3.json`;
     - it never logs a credential.
2. **`tests/test_bd_population_complete_e3.py`**, at least 5 pytest tests, all offline (stub boto3 and the helpers):
   - the complement excludes every landed account;
   - a landed account is never requested;
   - the bearer is re-minted every 10 calls (count the stub's mints);
   - both denominators are printed;
   - `run` refuses without `--go`.

   The words `complement`, `landed`, `re-mint`, `denominators` and `--go` appear in the file.
3. **Run `plan` once**, then commit the script, the tests and the completion plan.

<criterion id="DB13-1-AC1" cell_refs="DB-b-21"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r13/p13_completion_mode.py" . DB13-1-AC1</invocation><expect>DB13-1-AC1 PASS</expect></criterion>
`DB13-1-AC1` -- the completion tests pass, at least 5, naming the five words. Base: FAIL.

<criterion id="DB13-1-AC2" cell_refs="DB-b-21"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r13/p13_completion_mode.py" . DB13-1-AC2</invocation><expect>DB13-1-AC2 PASS</expect></criterion>
`DB13-1-AC2` -- the offline completion plan reconciles: planned 5252 = landed + complement, landed of at least 19, and no overlap.
Base: FAIL.

<criterion id="DB13-1-AC3" cell_refs="DB-b-21"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r13/p13_completion_mode.py" . DB13-1-AC3</invocation><expect>DB13-1-AC3 PASS</expect></criterion>
`DB13-1-AC3` -- a GUARD: your commits touch only IRPT_DASHBD paths. Base: PASS.

<expected_criteria>DB13-1-AC1,DB13-1-AC2,DB13-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** S3 reads and lists only. NO Black Diamond call, no token mint, no `run`.
- **Refusal clause.** Any vendor call, a `run`, or a credential written anywhere is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~7/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-21.bd-population-completion-mode.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 13 (round 13, workstream B), cell `DB-b-21`.
<owned_cells>DB-b-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB13-1-AC1, DB13-1-AC2, DB13-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~7/IRPT_DASHBD.TO-DB-b-21.bd-population-completion-mode.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB13-1-AC1,DB13-1-AC2,DB13-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, the completion plan's denominators, each criterion's last line, and any
surprise row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script, tests and an offline plan under a deliverables folder; 0 served bytes move; no vendor call in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB13-1-AC1 base FAIL (no tests), DB13-1-AC2 base FAIL (no completion plan), DB13-1-AC3 base PASS (guard), dry-run at base 0dc80bec30 2026-10-05 ~00:2xZ.
lane: the <paths> block IS the grant.
</preflight>
