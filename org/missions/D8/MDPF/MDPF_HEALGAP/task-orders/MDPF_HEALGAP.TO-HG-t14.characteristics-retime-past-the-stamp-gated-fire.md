# TO MDPF_HEALGAP.TO-HG-t14 -- round 3 HG-t-14: the characteristics producer's daily rule fires after the stamp-gated registry fire
<to_id>MDPF_HEALGAP.TO-HG-t14</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~11</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>CHARRETIME</workstream>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-14` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3, AMENDMENT 1) |
**outcome_ref:** FWD-5 (a consequence of the runner's move; CTO ruling ADDENDUM 3 `c3cc34f2d0`, msg 3655) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-14`. The satellites weighted-characteristics producer (`cot-satellites-characteristics-producer`) fires once a day at
`cron(30 12 * * ? *)` and reads `platinum/satellites/holdings.json`, which the registry producer writes. After the cottonwood runner moves
from 06:00Z to 12:45Z (a later act, not yours), `holdings.json` is final only at the registry producer's stamp-gated 13:15Z fire, so a 12:30Z
characteristics run would publish one calendar day behind its input, silently. This cell moves ONLY the characteristics rule's time to
`cron(25 13 * * ? *)`. Nothing else changes. The new time is a wall-clock schedule, never a trigger on any upstream's success.

**The estate, read at the base.**
- `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf`: resource `aws_cloudwatch_event_rule.cot_satellites_characteristics_producer_daily`,
  `schedule_expression = "cron(30 12 * * ? *)"`, a `description` that states "Fires 12:30Z", and a comment block above it (the heading
  `THE SCHEDULE -- ITS OWN CLOCK, CHAINED OFF NOTHING`) that derives 12:30Z.
- `infra/aws/terraform/cot-pipeline/satellites-registry-producer.tf`: rule `cot_satellites_registry_producer_stamp_gated`,
  `cron(15 13 * * ? *)`, applied and read live 2026-10-11 (the registry producer function has `timeout = 90`).
- **Measured on the first 13:15Z fire (2026-10-11), CloudWatch `/aws/lambda/cot-satellites-registry-producer`:** INIT_START 13:15:44Z,
  `END` 13:15:48Z, `REPORT Duration: 3281.22 ms`, `Init Duration: 323.41 ms`; `holdings.json` LastModified 13:15:49Z.

**Why 13:25Z, derived (put this derivation in the comment):** the fire's measured wall is about 4 s. The DECLARED worst case is two
async retries (about 180 s, the AWS engine's own schedule: roughly 1 minute then 2 minutes after a failure) plus the 90 s timeout = 270 s,
so no run of the 13:15Z fire can still be writing `holdings.json` after 13:19:30Z. 13:25Z leaves 600 s, more than twice the declared
worst case. It is still after the 07:00 America/New_York Bloomberg pull in both DST states (the file's own derivation, 12:30Z is the floor)
and before the 13:30Z gold floor. Both rules are UTC crons, so the margin is constant; if either is re-anchored to ET, this cron must move.

**Build:**
1. In the tf file change ONLY: the rule's `schedule_expression` to `"cron(25 13 * * ? *)"`; the rule's `description` string so it states
   `Fires 13:25Z on its own clock, AFTER the stamp-gated 13:15Z registry fire has finished and after the 07:00 America/New_York Bloomberg
   pull in both DST states.` (keep the rest of the description's wording); and the comment block above the rule: replace the 12:30Z derivation
   with the derivation in the paragraph above (cron, measured wall, declared worst case, margin, the UTC-cron "moving part" note). Keep the
   `ALL DAYS, not MON-FRI` paragraph and the `STILL NOT success-of-upstream` paragraph's meaning.
2. Touch nothing else in the file: no grant, no role, no target, no permission, no module call, no other comment block.
3. Do NOT edit `data/assets/scripts/gold/build_satellites_characteristics.py` (DS's producer) or the Lambda wrapper.

### ACCEPTANCE

<criterion id="HG3-t14-AC1" cell_refs="HG-t-14"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t14_schedule.py</invocation><expect>T14-OK</expect></criterion>
`HG3-t14-AC1` -- the characteristics rule is an every-day wall-clock cron at least 270 s after the stamp-gated registry fire (read from its own tf), not earlier than 12:30Z, with only `schedule_expression` and `description` changed against the base pin.

<expected_criteria>HG3-t14-AC1</expected_criteria>

Run the invocation from the worktree root. AC1 FAILS at the base (`T14-BAD TIME: characteristics fires 12:30Z ...`).
No `terraform fmt` criterion: the file already carries unrelated alignment drift at the base (`hg_tf_fmt.py` reads FMT-BAD rc=3 on it before any edit),
so such a criterion would force edits outside this cell. Your edits are a string, a description and comments; they cannot change alignment.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** The apply is the issuer's, under its own
  never-widen pair. Read-only AWS reads are allowed where a criterion names them.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium).
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your report.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W11-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below,
  and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Keep LF line endings; check `git diff --stat` shows only your lines
  before committing (the Edit tool has rewritten LF files to CRLF on this box).

<paths>
infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, AMENDMENT 1), cell `HG-t-14`.
<owned_cells>HG-t-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: HG3-t14-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~11/MDPF_HEALGAP.TO-HG-t14.characteristics-retime-past-the-stamp-gated-fire.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t14-AC1 --governing-order org/missions/D8/MDPF/MDPF_HEALGAP/task-orders/MDPF_HEALGAP.TO-HG-t14.characteristics-retime-past-the-stamp-gated-fire.md` BEFORE the flip (several ids would be comma-separated; space-separated ids print a usage error, rc 2).
</proof_of_spec>

**REPORT:** the files, every check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE comp-schedule is the gate ledger and this order arms no gate; the new fire `cron(25 13 * * ? *)` is placed 10 minutes after the stamp-gated registry fire (measured wall 4 s, declared worst case 270 s) and 5 minutes before the 13:30Z floor, which does not read this key.
comp-iam: DECLARED-NOT-APPLICABLE the order changes a schedule string and a description and no grant; the role `cot-satellites-characteristics-producer-role` and its four read surfaces and one write key are untouched (the never-widen pair reads the writer count live).
comp-adversary: RUN -- the check's TIME arm reads the registry rule's cron from its own tf rather than typing it, and its scope arm refuses any other non-comment line; mutants (16 min, weekday cron, 12:00Z, event_pattern) each print T14-BAD, a good copy prints T14-OK.
risk: WORLD -- a served-output schedule (`platinum/satellites/characteristics.json`); the apply is the issuer's under its own never-widen pair, BEFORE HG-t-5.
direct_act: false -- the class is WORLD.
</preflight>

Source: CTO ruling ADDENDUM 3 (`1.0.0_SA_CTO~DELL1`, msg 3655, `NEVER_WIDEN_ROUND3_HG_T9_T11_CTO_HALF.md`); reader census `CHARACTERISTICS_JSON_CENSUS_20261011.md` @61d007d22c
(3 runtime readers); the HG-t-5 half draft `NEVER_WIDEN_HALF_REQUEST_HEALGAP_R3_ACT_HG_T5_20261011.md` @8b41f47422.
