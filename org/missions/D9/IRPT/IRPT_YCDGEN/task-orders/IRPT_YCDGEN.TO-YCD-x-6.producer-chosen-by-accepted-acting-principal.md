# IRPT_YCDGEN task order -- `YCD-x-6` -- ROUND 6 (THREAD): THE PRODUCER IS CHOSEN BY THE ACCEPTED ACTING PRINCIPAL

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6N.md</decomp_doc>
<owned_cells>YCD-x-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-x-6.producer-chosen-by-accepted-acting-principal</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~8</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a producer-selection code change; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the gap was measured in code (served.py:1022-1050, prospect.py:41, resident_worker.py:126-133) and ruled by the CTO (msg 2067)
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT) -- the Analysis report made in house, Opal-branded, with no YCharts call. Work ONLY in the worktree your
spawn line names; every path below is relative to that root. No vendor call, no AWS call, no deploy.

**RULES THAT BIND THIS ORDER (verbatim, from the dell2 CTO and Andrew):**
- "research browsing only when necessary; no packages, no installs, no file fetched onto the box."
- Never `bun install`; no package fetch of any kind.

## 1. YOUR CELL (inlined from the round-6 addendum-N decomposition)

### `YCD-x-6` -- the resident chooses the producer by the accepted acting principal (C-SWITCH; FWD-1)
Under IRPT_BCKEND's E5 (`infra/aws/lambda/investor-reporting/_authz/served.py` ~1005-1050) a filer whose `allowedFirmIds` lists the tenant must
name the firm advisor, and the request is then OWNED by that advisor (`_scope/prospect.py` `resolve_prospect_owner`, `principal_id` = the
advisor's email). `ycharts/generate/resident_worker.py` `producer_for` (~126-133) reads `record["owner"]["principal_id"]`, so a request a
listed principal files on behalf of an advisor routes to YCHARTS.
- FIRST, a census (print it with its denominator): every place the server records the acting principal of an UPLOAD and of an ANALYSIS
  SUBMIT, and every field of the ACCEPTED request record the resident receives (`resident_worker` `execute` / the queue message / the job row).
  Known: `intake/uploads.py:267` writes `acting_principal_id` on an on-behalf UPLOAD record. Say whether the accepted ANALYSIS request the
  resident reads carries a server-recorded actor, and where.
- IF it does: change `producer_for` to read that server-recorded actor when present, else the owner as today. Edit nothing else.
- IF it does not: STOP the code arm, file a row naming the acceptance path that would have to record it (file + function), and finish the
  census and the test arm only. Do not edit any file outside `<paths>`.
- Tests in `ycharts/generate/tests/test_producer_actor.py` (new): owner = an invented advisor, actor = a listed principal -> OPAL; owner =
  advisor, actor = an unlisted principal -> YCHARTS; owner = listed, no actor -> OPAL; owner = unlisted, no actor -> YCHARTS. Use
  monkeypatched allow lists with invented principals only.

## 2. THE CONTRACT YOU BUILD AGAINST

**R22 The Opal producer is chosen by the accepted acting principal.** `producer_for` reads the actor the SERVER recorded at acceptance, never a
client-sent value and never the owner when an actor is recorded; with no recorded actor it reads the owner as today.

## 3. WHAT YOU NEED TO KNOW

- The existing pin test in `ycharts/generate/tests/test_resident_worker.py` asserts the shipped allow list; leave it as it is at your HEAD.
- Python: `python -m pytest -q -p no:cacheprovider <test>` from `infra/aws/lambda/investor-reporting/ycharts/generate`. ASCII only. No real
  email, client figure or secret in any committed file.

## 4. SURFACES AND BOUNDS

NEVER: a vendor call, any AWS call, a deploy, an install. A check you cannot satisfy inside your `<paths>` is a surprise row appended to
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `IRPT_YCDGEN-D2-W8-S<k>`, next unused k;
`fabric` "dell2"; `surfaced_at` the real UTC time).

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_producer_actor.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/x6_checks.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/IRPT_YCDGEN.TO-YCD-x-6.producer-chosen-by-accepted-acting-principal.proof_of_spec.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the census names every server-recorded actor field on the upload, the submit and the accepted request, with its denominator
- **AC2** -- the four producer cases pass
- **AC3** -- the existing resident_worker and opal-thread tests still pass

`x6_checks.py` (new): one argument (`census`, `cases` or `regress`), one RESULT line each.

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-x-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/x6_checks.py census</invocation><expect>^RESULT: census PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-x-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/x6_checks.py cases</invocation><expect>^RESULT: cases PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-x-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/x6_checks.py regress</invocation><expect>^RESULT: regress PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit, then write the instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~8/IRPT_YCDGEN.TO-YCD-x-6.producer-chosen-by-accepted-acting-principal.proof_of_spec.json`
with `to_id` `IRPT_YCDGEN.TO-YCD-x-6.producer-chosen-by-accepted-acting-principal`, check it with `python .tools/proof-of-spec-check.py
<instance>`, and commit it. Report once: the census, each criterion's verdict line with its output, files written, rows filed. Leave the
`<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** addendum N (IRPT_YCDGEN_DECOMP_R6N.md), cut on 1.0.0_SA_CTO~DELL2 ruling msg 2067 after the st26 F1
upload was refused by E5 and an advisor_email retry was measured to route to YCHARTS (msg 2065). Chain `~8`, fresh slot; worktree cut from
box/dell2. resident_worker.py sits in lane IRPT_Y_ACCESS_INTEGRATION_P: the worker's write surface is this order's <paths>; if owned-paths
refuses the worker, the issuer rules (audited override per CTO 1374). Risk WORLD (infra path floor): code only, no deploy -- st27 is its own pair.

<round>6</round>
<workstream>R6N_PRODUCER_ACTOR</workstream>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
**ISSUER CLOSE 2026-10-09 (2.0.0_SA_COO~G2) on 1.0.0_SA_CTO~DELL2 ruling msg 2111:** closed on its census. AC1 PASS, AC3 PASS; AC2
3 of 4 with case 1 a strict xfail: the case (an advisor-owned ANALYSIS request accepted from a listed actor) cannot arise, because the
analysis owner is forced to the submitter (submission_service.py:115 ACTUAL_SUBMITTER_REQUIRED; prospect_submission.py:72-73,111) and E5's
advisor ownership is the UPLOAD input's. Read in code, not run; the st27 F1 asserts the producer from the served report and the resident log.
Row D2-W8-S1 stands as the record of the missing actor field; no code arm is owed.

<status>complete</status>
