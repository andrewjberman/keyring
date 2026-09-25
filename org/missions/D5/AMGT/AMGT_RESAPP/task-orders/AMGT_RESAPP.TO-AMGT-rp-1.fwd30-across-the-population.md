# AMGT_RESAPP task order -- `AMGT-rp-1` -- FWD-30 ACROSS THE POPULATION: THE SERVED EXPORT MEASURED ON ALL 89 COVERAGE-LIST NAMES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~158</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the cell READS one deployed function through the box's own credentials (lambda:InvokeFunction on opal-amgt-scoped-api, the same reads rn-5's and ro-7's checks made); it grants nothing.
comp-adversary: RUN by the issuer over the round-40 analysis at the cut; declaration in the issuance commit message.
EGRESS CLASS, declared: ONE AWS READ SURFACE -- `lambda invoke` of Opal's own `opal-amgt-scoped-api` (account 313476888478), GET routes only, for the 89 coverage-list keys; no S3 write, no vendor, no server.
</preflight>

## 1. THE CELL -- `AMGT-rp-1` (round 41, decomposition s.49)

`FWD-30` is REALIZED for `BA_US_Equity` only (round-40 analysis s.1b); the goal names every security in the coverage list.
**Measure the served export across the WHOLE coverage list** -- the 89 folders of
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~4/universe.json` (`names[].folder`).

Per folder, in order:
1. **Key:** `scoped_amgt.resolve_identity(crosswalk.harvester_key(folder, crosswalk.load_pilots())[0])["security_key"]`
   (`lib.research.api.scoped_amgt`, `lib.research.identity.crosswalk`). At the cut this read 89 of 89 MEASURED, 89 distinct.
2. **Capture** the deployed function's served routes for that key exactly as
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~150/served_capture.py` does for BA -- overlay, thesis,
   peers, rankings trending/chatter, and `print?format=rich` -- generalised to take the key, into a temp directory.
3. **Compare** from `portal/`: `node src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs --fixture
   <served_fixture.json> --rich <rich body>`. Record its FIGURES, CITES and ABSENCES `page/rich/same/missing/extra` and its
   `PAGE ABSENCE LINES COVERED` count.

**Write ONE table** at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/fwd30_population.tsv`,
tab-separated, one row per folder, with exactly this header:

`folder security_key fig_page fig_rich fig_same fig_missing fig_extra cit_page cit_rich cit_same cit_missing cit_extra abs_page abs_rich abs_same abs_missing abs_extra abs_covered verdict reason`

- `verdict` is `OK` when the harness prints `EXPORT-COMPARE OK`, and `NOT_OK` otherwise.
- `verdict` is `CAPTURE_FAILED` when a route errors. Its counts are blank, and `reason` names the route and its status.
- `reason` is empty on an OK row; on a NOT_OK row it names the first failing set.

Commit the sweep script, the table and a per-name log beside them.

## 2. BOUNDS

1. **No server; no write to AWS.** Read routes only; the harness is plain node. Standing: no install, no push, no promote, no
   vendor call. REFUSE, do not rescue.
2. **No fix.** You change no code outside your deliverables folder. A NOT_OK row is the measurement; record it and continue.
3. **Captures stay out of the repository.** Write every capture to a temp directory outside the worktree (about 0.5 MB per name);
   commit only the sweep script, the table and a per-name log.
4. **Portal is a nested repository** at `<worktree>/portal`, branch `wk-AMGT_RESAPP-158-portal` at DEV `fe618e50`; you do not
   commit inside it. Python from the repo root with `PYTHONPATH="$(pwd)"`; AWS through boto3 as `served_capture.py` does.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for AC1-AC2's sweep inputs, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round41/checks/rp-1.AC1.py; echo "exit=$?"</invocation><expect>rows 89 of 89 folders; missing 0; extra 0; duplicated 0; TABLE SHAPE OK -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round41/checks/rp-1.AC2.sh; echo "exit=$?"</invocation><expect>BA_US_Equity row EQUALS a fresh served read: 15 of 15 counts -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rp-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round41/checks/rp-1.AC3.sh; echo "exit=$?"</invocation><expect>THE HARNESS CAN FAIL: harness on the stale body: rc=1 (the control needs 1) -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rp-1" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round41/checks/rp-1.AC4.sh; echo "exit=$?"</invocation><expect>every row that is not OK, printed whole, for a person to judge whether it names an export defect, a page defect or a data gap; RECORDED, no verdict</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/AMGT_RESAPP.TO-AMGT-rp-1.fwd30-across-the-population.proof_of_spec.json`. Report once: the verdict counts, every NOT_OK or CAPTURE_FAILED folder, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** s.5 item 1, the analysis's largest unmeasured thing. SERVED declared above the LOCAL floor as rn-5 was: the cell writes nothing served but its claim is about served output. AC4 is a judgment criterion although the cell touches no served figure: a NOT_OK row needs a person to say which side is wrong. The checks were dry-run at the base (round41/base-runs/): AC1 and AC2 FAIL (no table), AC3 PASSES (a control). AC1 was also run on a synthetic 89-row table (OK) and on two broken ones (NOT OK), and AC2 on a temporary BA row (15 of 15, then 14 of 15 on one changed count).

**WORKER CLOSE, 0.9.0_WK_AMGT_RESAPP~158.** proof-of-spec-check VALID rc=0 (AC1-AC3 PASS-by-output; AC4 RECORDED for L9/L10).
AC1: rows 89 of 89, missing/extra/duplicated 0, distinct keys 89, TABLE SHAPE OK. verdicts OK 5 (BA_US_Equity, COST_US_Equity,
HD_US_Equity, NU_US_Equity, SAP_GY_Equity), NOT_OK 84, CAPTURE_FAILED 0 -- every one of the 89 x 5 = 445 route invokes returned
200. AC2: BA_US_Equity row equals a fresh served read, 15 of 15 counts. AC3: the difference control fires as expected, rc=1 on
round 38's stale body. AC4: all 84 NOT_OK rows printed whole for a person's judgment. Row AMGT_RESAPP-Z-W158-S1 (OBSERVATION,
ARMED, disarm_owner 2.0.0_SA_COO~Z): 2 of 89 resolved security_keys (BP/_LN_Equity, NG/_LN_Equity) carry a literal '/' from an
unescaped landed-model-block display value; lambda:Invoke tolerated it but the real API Gateway HTTP route is unmeasured.
Commits: cc181e5be849f899c212f8d1b31d5e67e67bf325 (sweep.py, capture_lib.py, fwd30_population.tsv, 89 logs, the surprise row),
6c1f20eabb (the proof-of-spec instance). Both LOCAL on wk-AMGT_RESAPP-158, never pushed. Portal untouched (read-only).

<status>complete</status>
<round>41</round>
<slot>~158</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
