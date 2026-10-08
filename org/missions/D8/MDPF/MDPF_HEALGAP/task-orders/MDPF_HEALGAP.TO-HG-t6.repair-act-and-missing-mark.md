# TO MDPF_HEALGAP.TO-HG-t6 -- round 2 HG-t-6: one repair act that names what it will fetch, and a missing-and-why mark for days that cannot be filled
<to_id>MDPF_HEALGAP.TO-HG-t6</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~5</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-6` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-6`. FWD-3 (PRD v0.2): an operator closes an existing hole with ONE act that says beforehand exactly what it will fetch, and a day
that cannot be truthfully fetched is shown as missing, never filled with another day's data. The vendor serves current state only (row
S2: the runner sends no as-of), so a hole is repairable only on the day it opened.

**The estate, read at the base.** The runner (`infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/lambda_function.py`): event `{"mode":"pull","date":D}`, guard by listing the stamp,
three feeds, `META_PREFIX`. The eleven days 2026-08-31..2026-09-10 lack `rebalancer_model_detail` (round 1 hop 0). Copy the round-1 test
stubbing style (no network).

**Build (two small tools in the runner folder, both DRY-RUN unless `--execute` is given):**
1. NEW `repair.py --date D [--execute]`: (a) if D is not today UTC, print one line `REFUSED date=D reason=the source serves current state
   only; a past date would land today's data under D` and exit 2; (b) list which of the three feeds are missing for D (by listing, as the
   guard does); if none, print `NOTHING-TO-REPAIR date=D` and exit 0; (c) otherwise print one line `MANIFEST date=D feeds=<missing,...>
   keys=<prefixes it will write>` BEFORE anything else happens; (d) only with `--execute`, invoke `cot-rebalancer-runner` for D (async,
   `{"mode":"pull","date":D,"force":true}`) and print `INVOKED ...`. Dry-run never invokes.
2. NEW `mark_missing.py --from D1 --to D2 --feed F --reason TEXT [--execute]`: for each day in the range where feed F has no key, print
   `WOULD-MARK date=<d> feed=F` (dry-run) or write `META_PREFIX + "<d>-missing.json"` = `{"as_of", "feed", "reason", "marked_at"}` and
   print `WROTE ...` (`--execute`). It never writes any key under a feed's prefix. Days where F exists are skipped with `PRESENT ...`.
3. Tests in NEW `test_healgap_repair.py` with these exact names (each must PASS): `test_manifest_printed_before_any_fetch`,
   `test_repair_refuses_a_past_date_with_reason`, `test_repair_names_exactly_the_missing_feeds`,
   `test_missing_mark_payload_names_feed_and_reason`, `test_missing_mark_never_writes_a_feed_key`.

### ACCEPTANCE

<criterion id="HG2-t6-AC1" cell_refs="HG-t-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t6_tests.py</invocation><expect>REPAIR-OK</expect></criterion>
`HG2-t6-AC1` -- the five named tests in `test_healgap_repair.py` pass: manifest before fetch, past date refused with reason, exactly the missing feeds named, mark payload, no feed key written.

<criterion id="HG2-t6-AC2" cell_refs="HG-t-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R2_CHECKS/hg_t6_dryrun.py</invocation><expect>DRYRUN-OK</expect></criterion>
`HG2-t6-AC2` -- dry-run against the real bucket: a past date is REFUSED, today gives a MANIFEST or NOTHING-TO-REPAIR, and the mark dry-run names exactly the eleven days.

<expected_criteria>HG2-t6-AC1 HG2-t6-AC2</expected_criteria>

Run each invocation from the worktree root. Both FAIL at the base: `REPAIR-BAD no file ...` and `DRYRUN-BAD no file ...`. AC2 reads S3 (`s3:ListBucket`) read-only and never writes.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.** Every deploy and apply is the
  issuer's, at the drain. Read-only AWS reads are allowed where a criterion names them.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-W5-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row.
- Do not edit `lambda_function.py` (HG-t-3's write set); stub the runner in tests.

<paths>
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/repair.py
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/mark_missing.py
infra/aws/lambda/cot-pipeline/cot-rebalancer-runner/test_healgap_repair.py
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `HG-t-6`.
<owned_cells>HG-t-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG2-t6-AC1, HG2-t6-AC2. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~5/MDPF_HEALGAP.TO-HG-t6.repair-act-and-missing-mark.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG2-t6-AC1 HG2-t6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule change.
comp-iam: RUN at L5 (decomposition ROUND 2 battery): marks land under blackdiamond/cottonwood/meta/ (existing prefix) by the issuer; --execute needs lambda:InvokeFunction, which dell1 holds on cot-rebalancer-runner (MSTR msg 862: 1 Allow, 0 Deny).
comp-adversary: RUN at L5 (decomposition ROUND 2 battery): both tools default to dry-run; a past date is refused because the vendor has no as-of (S2); the mark never writes a feed key.
risk: WORLD -- tools that write bronze meta and invoke the runner; the marks and the induced-hole repair are the issuer's drain acts.
direct_act: false -- the class is WORLD.
</preflight>

Source: PRD v0.2 ENDPOINT FWD-3; CTO round-1 analysis @475c742f71 section 3; decomposition round 2.
