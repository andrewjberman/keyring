# TO NFRA_TRNSPT.TO-TR-l4 -- each scheduled mail fire prints one counts-only line to its own log

<to_id>NFRA_TRNSPT.TO-TR-l4</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by path floor (the Lambda handler); nothing is applied | **Decomp cell:** `TR-l-4` (`decompositions/NFRA_TRNSPT_DECOMP_R4.md`) |
**outcome_ref:** FWD-7 | **depends_on:** TR-w-4 (same slot, same file; handed to you after TR-w4 is complete on your branch)

---

## WORKER FACE

### THE CELL

`TR-l-4` (CTO round-3 analysis @c2b5eb89a4, section 4, C2): "The fire states what it did, in its own log. The handler prints ONE
line per fire: `MAIL-PULL-FIRE run=<id> window_days=<n> listed=<n> admitted=<n> landed=<n> skipped_known=<n> list_refusals=<n>
silver_rows=<n> held_out=<n>`. No sender, address, subject, name or id beyond `run=`."

Why: the machine that grades the fire cannot read the transcripts store (its principal is refused the bucket's key, by ruling), so a
fire must be gradeable from its CloudWatch log line alone.

**Measured at the cut:** `infra/aws/lambda/transcripts-pull/mail_handler.py` `lambda_handler` gets `rec` from
`pull.run(...)` (`data/transcripts/scripts/outlook/pull.py:134`) and builds `results` (one dict per silver date with `rows` and
`held_out`). It prints nothing today. The fields map from what already exists:

| field | value |
|---|---|
| `run` | `run_id` |
| `window_days` | `days` |
| `listed` | `rec["listed"]` (None -> 0) |
| `admitted` | `rec["ingest"]` |
| `landed` | `rec["landed"]` (bronze objects newly landed) |
| `skipped_known` | `rec["skipped_known"]` (None -> 0) |
| `list_refusals` | `len(rec["list_refusals"])` |
| `silver_rows` | sum of `rows` over `results` |
| `held_out` | sum of `held_out` over `results` |

**Build:**
1. `mail_handler.py`: after the silver loop and the `silver.json` write, `print(...)` exactly ONE line in that field order, each value
   an integer except `run`. On a raised error (e.g. `GatewayToolsAbsent`) behaviour is unchanged (it raises; no line is required).
2. New file `data/transcripts/scripts/tests/test_mail_fire_line.py` (reuse the fakes in `test_mail_pull_handler.py` by import or
   copy): invoke the handler on a fake route listing at least one admitted message and one near miss, capture stdout (`capsys`),
   assert exactly one line starts `MAIL-PULL-FIRE `, its `key=value` set equals the nine fields above and nothing else, and the values
   match the run. CONTROL in the same test: the fake's sender address, subject and recipient addresses appear NOWHERE in captured
   stdout.

### ACCEPTANCE

<criterion id="TR4-l4-AC1" cell_refs="TR-l-4"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R4_CHECKS/r4_checks.py l4-line</invocation><expect>R4-L4-LINE-OK</expect></criterion>
`TR4-l4-AC1` -- one `MAIL-PULL-FIRE` line per fire with exactly the nine fields, values matching the run; the planted sender, subject
and recipients never in stdout (the control is part of this criterion).

<expected_criteria>TR4-l4-AC1</expected_criteria>

Dry-run at the base (CLOUD b6a856bfb9): AC1 `R4-L4-LINE-FAIL absent` -- FAIL as expected. The suite and the bundle import are the
issuer's drain checks, not yours; do not break them.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **WORLD by path (the Lambda handler); NOTHING is applied.** Never `terraform apply` / `safe-apply`, never deploy, never invoke the Lambda, never call the gateway, never read the
  `opal-data-transcripts` bucket. `dist/` is never committed.
- Do not log anything else from the handler; no sender, address, subject, name or message id.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_TRNSPT-W1-S<k>`, next unused), and do not weaken a test to pass.

<paths>
infra/aws/lambda/transcripts-pull/mail_handler.py
data/transcripts/scripts/tests/test_mail_fire_line.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R4.md</decomp_doc> (round 4), cell `TR-l-4`.
<owned_cells>TR-l-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR4-l4-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-l4.mail-fire-line.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR4-l4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the line as the test captured it (from the fake run), the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule touched.
comp-iam: DECLARED-NOT-APPLICABLE the cell writes no bucket and applies nothing.
comp-adversary: RUN -- the only exposure is PII in a log line; the planted-address control is inside AC1.
lane: the <paths> block IS the grant; infra/aws/** is the AE lane at APPLY, which this order never reaches.
</preflight>

Source: CTO round-3 analysis @c2b5eb89a4 section 4 C2; decomposition round 4 cell TR-l-4. The analysis's criterion (2) "the suite
passes" moves to the issuer's drain (verification diet, spine v3.16).
