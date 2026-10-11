# TO IRPT_DASHBD.TO-DB-b-118 -- the thresholds a method row states carry their claim: the producer's thresholds input and the dim_return_method row gain a per-value claim (measured / inferred / held / absent), rule-24 record first, then the change with tests; no S3 write

<to_id>IRPT_DASHBD.TO-DB-b-118</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~93</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>62</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 4060 (thresholds are the run's own values with their claim; the producer's file is this lane's) | **Decomp cell:** `DB-b-118` (decomposition section 64) | **outcome_ref:** FWD-11 | **depends_on:** DB-b-116 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-93`; run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/`.

**THE CLIENT-DATA RULE (binding):** never print an account number or a client figure in a commit message, a record, a row or a report. Test fixtures
are synthetic. The pinned 49F thresholds file in git history carries per-account keys: do not print it; read only the key names you need.

**The cell (`DB-b-118`).** ADVI_COTBKF will write `dim_return_method` `method_version=3` for Cottonwood. The CTO ruled (msg 4060) that its thresholds are
the values the 107,316-row run USED, never 49F's, each stated with its claim. DB-b-116 measured that the Cottonwood run passed `thresholds=None` (every
row `GUARD_NOT_REACHED`), so for that row the truthful statement is that the thresholds were not measured and not applied.
`emit_method_row` in `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` (~line 1881) cannot say that today: it reads
`thresholds["tolerance"]` and four more values as bare numbers, and the row has no field a consumer can reject on. CLAUDE.md: a value must carry its
claim in a field a consumer can reject on (`measured/inferred/held/absent`); no such field means it may not be treated as measured.

Read in `C:/dev/wk-irpt-dashbd-93` first: `emit_method_row`, its CLI path (`--thresholds-in`, `--method-row-only`, ~lines 1996-2034), `comparability`
and every other reader of `thresholds` in the producer; `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/ROW3_VS_COTTONWOOD.json`
(the guard-threshold fields); `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`; any contract under `org/standards/` that declares `dim_return_method`.

1. **Rule-24 record first** (`THRESHOLD_CLAIM_RULE24.json` and a one-page `.md`), before any code:
   - `postulates` {mece, same_grain, intent_coherence, state_coherence}, each {finding, evidence: [{file, line}]}. The claim set is the law's four;
     show it is MECE over the declared domain "how the row's writer knows this threshold value", by subtraction, and name which values one remedy
     does not move.
   - `token_census` {files_scanned, scope, tokens}: word-boundary, `comp-find -i`, for `measured`, `inferred`, `held`, `absent` and your chosen field
     name. Print the denominator.
   - `decision` {field_name, where_written, file_without_claims, reasoning}: the grain is PER THRESHOLD VALUE (five values: tolerance,
     large_flow_share, the two plausibility band ends, comparability_max_excluded_weight). Say where the claims are written (row columns, manifest,
     or both) and why, and what the writer does for a thresholds file that carries NO claims. Constraints on that last choice: it never treats an
     unclaimed value as measured; and the 49F row 2 partition already served must not need a rewrite for this cell to land.
2. **Then the change, in the producer only:**
   - a module constant `THRESHOLD_CLAIMS = ("measured", "inferred", "held", "absent")`;
   - the thresholds input may carry the per-value claims; a claim outside the set is REFUSED; a value may be null ONLY when its claim is `absent`;
   - `emit_method_row` writes the claims as your record decided, and with `upload=False` returns them in its `row`;
   - `comparability()` and the grading paths are NOT changed: a run with `thresholds=None` behaves exactly as before.
3. **Tests** in `data/assets/scripts/gold/irpt_reporting/tests/`: a row written from thresholds whose five claims are `absent` with null values states
   that; a claim outside the set refuses; a null value under any claim but `absent` refuses; your `file_without_claims` rule; and the returns
   tables' bytes are untouched (the five output tables do not read this path -- show it from the code with file and line, or by an existing test).
   Keep every existing test in that folder and in `infra/aws/lambda/investor-reporting/reporting-gold/tests/` passing.
4. Record in the same JSON: `row_example` (the `row` returned for the all-absent case on a synthetic firm), `readers` (every reader of
   `dim_return_method` or its manifest you can find, with the denominator, and whether the new field breaks it), `tests` {passed, failed, new_test}.

**No S3 write, no AWS call, no deploy.** The Cottonwood row itself is written later by ADVI_COTBKF under its own pair.

<criterion id="DB62-1-AC1" cell_refs="DB-b-118"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r62/p62_round62.py" . DB62-1-AC1</invocation><expect>DB62-1-AC1 PASS</expect></criterion>
`DB62-1-AC1` -- the rule-24 record answers the four postulates with file-and-line evidence, carries the token census, and states the field, where it is written and the no-claims rule. Base: FAIL.

<criterion id="DB62-1-AC2" cell_refs="DB-b-118"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r62/p62_round62.py" . DB62-1-AC2</invocation><expect>DB62-1-AC2 PASS</expect></criterion>
`DB62-1-AC2` -- the producer declares the four-member claim set and the new test file passes at HEAD. Base: FAIL.

<expected_criteria>DB62-1-AC1,DB62-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Served output does not move.** No edit under `infra/` or `portal/`, and under `data/` only the path in the grant.
- **This order's exception:** you edit `account_return_daily.py` and tests under `data/assets/scripts/gold/irpt_reporting/`. No other producer file.
- **AWS:** none. NO Black Diamond or vendor call, no secret read, no S3 read or write, no deploy, no bun, no download of any package, script or program.
- **Refusal clause.** A vendor call, a secret read, an S3 write, a deploy, an edit outside the grant, a filled figure, or an account
  number, name or balance in a committed `.md` is a defect: stop and file a row.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/
data/assets/scripts/gold/irpt_reporting/account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-118.threshold-claim.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 64 (round 62), cell `DB-b-118`.
<owned_cells>DB-b-118</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB62-1-AC1, DB62-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~93/IRPT_DASHBD.TO-DB-b-118.threshold-claim.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB62-1-AC1,DB62-1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the decision (field, where written, the no-claims rule), each postulate's finding in one line, the census denominator, the all-absent row example's claim fields, the readers found, test counts and the new test's name, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the dim_return_method row writer in the returns producer; the returns tables and the gold Lambda's run do not read this path.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call, no new key.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- DB62-1-AC1 and DB62-1-AC2 FAIL at base (no record). CTO ruling msg 4060.
lane: the <paths> block IS the grant.
</preflight>
