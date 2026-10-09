# TO ADVI_COTBKF.TO-CB-z-3.endpoint-read -- round 26 CB-z-3: one endpoint line per FWD, REALIZED / NOT, with its instrument

<to_id>ADVI_COTBKF.TO-CB-z-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~49</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-z-3` (`decompositions/ADVI_COTBKF_DECOMP.round26.md`) |
**outcome_ref:** FWD-1..FWD-9 | **depends_on:** none

---

## WORKER FACE

### THE CELL

ADVI_COTBKF is Cottonwood's 2013-2026 Commonwealth history landed in Opal. Its PRD,
`org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, section ENDPOINT, lists nine outcomes, FWD-1..FWD-9: transaction history,
the delivery kept as received, daily returns graded monthly (FWD-3), CRM records, documents, coverage, sensitive details held where
Andrew decided, the old-to-new account crosswalk, and history following an account renumbering. The CTO's round analyses are in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_*.md` (round 15: "6 of 9 outcomes are REALIZED"; FWD-8
REALIZED at round 7, FWD-6 at round 9). Rounds 16-25 worked FWD-3 only (the latest real run: `method_r25` default, MATCH 3,098 of
82,593 graded months; about 8% of account-days priced).

**Your item (the CTO's analysis, E3).** "Endpoint read: which of the project's FWDs `method_r25` now grades REALIZED -- one line per FWD,
REALIZED / NOT, with its instrument; this seat grades from it at the next analysis."
Write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md`: a table with exactly one row per
FWD (`| FWD-<n> | <REALIZED or NOT> | <instrument> | <evidence> | <what is missing, if NOT> |`), where:
- **instrument** names the act that proves it NOW, run by you: an S3 listing or read-back of the served artifact, a script's output, or
  a page read. Never a status word or an earlier analysis's sentence alone. Earlier analyses are where to look, not proof.
- **evidence** is the measured value and its source (key, row count, commit, line).
Run each instrument read-only (S3 reads only of the buckets the project already uses: `opal-data-assets` commonwealth/cottonwood
prefixes, `opal-data-cottonwood`; never `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection`,
`opal-data-demo`; never the restricted CRM prefix). A FWD whose instrument cannot be run reads NOT with the reason.

### ACCEPTANCE

<criterion id="CB26z3-AC1" cell_refs="CB-z-3"><invocation>python -c "import sys,re;t=open(sys.argv[1],encoding='utf-8').read();r=sorted(set(re.findall(r'^\| FWD-([1-9]) \| (REALIZED|NOT) \|',t,re.M)));print('fwd_rows=%d'%len({a for a,_ in r}))" org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md</invocation><expect>fwd_rows=9</expect></criterion>
`CB26z3-AC1` -- one REALIZED / NOT row for each of the nine outcomes.

<criterion id="CB26z3-AC2" cell_refs="CB-z-3" judgment="true"/>
`CB26z3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each row's instrument was run now and its evidence measured, not copied from a status word or an earlier analysis.

<expected_criteria>CB26z3-AC1,CB26z3-AC2</expected_criteria>

## BOUNDS

- **Grant.** Your deliverables folder and this order's file only. No code change.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun; never the restricted CRM prefix.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W49-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time), and do not weaken the test.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round26.md</decomp_doc> (round 26), cell `CB-z-3`.
<owned_cells>CB-z-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB26z3-AC1, CB26z3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ADVI_COTBKF.TO-CB-z-3.endpoint-read.proof_of_spec.json`, validated with
`python .tools/proof-of-spec-check.py <instance> CB26z3-AC1,CB26z3-AC2` BEFORE the flip. Mechanical: CB26z3-AC1; a judgment criterion is
recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the nine rows, the count REALIZED, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of served artifacts, no schedule involved.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: the restricted CRM prefix (never read; FWD-4/FWD-7 rows say so).
comp-adversary: RUN -- each row's instrument run now, never a copied status; BLIND: served pages behind a login this identity lacks (the row reads NOT with the reason).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` analysis ADDENDUM 1 (msg 2113), E3.
