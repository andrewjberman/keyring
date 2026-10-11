# TO MDPF_HEALGAP.TO-HG-t13 -- round 3 HG-t-13: does the mdpf-daily-runner EC2 still re-publish the slice, and is that a no-op
<to_id>MDPF_HEALGAP.TO-HG-t13</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~10</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-13` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 3) |
**outcome_ref:** row MDPF_HEALGAP-S1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-13`. Row `MDPF_HEALGAP-S1` (`org/surprise_channel/MDPF_HEALGAP/INVESTIGATION_v1.md`, read it): the Cottonwood gold builder has
two callers, the consolidator in the `mdpf-gold-lambda` and the EC2 `mdpf-daily-runner`'s dispatch. The row asked whether the EC2 path
still re-publishes the slice later the same day WITHOUT the catch-up step. It is outside this project's layer boundary, so this cell is
a READ and nothing else: answer it with grounding, and write nothing about a fix.

**What to read (read-only):**
1. `infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh`, the steps around lines 540-560: the condition under which it runs
   `build_cottonwood_mdpf_slice.py` (the builder, the pair and the slice).
2. How the runner stages `assets_gold` (the sync/copy step at the top of the same script and any S3 prefix it names): is
   `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` present in that staged set? A read-only `aws s3 ls` or `head-object` on the
   named code prefix is allowed; a `comp-pipescript deployed` read is the preferred instrument.
3. What the slice step does on a day the Lambda already wrote the partitions: does it rewrite the gold partitions or only re-publish,
   and does its output differ from what is already served (a no-op = the same bytes/keys)?

**Build:** NEW `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~10/MDAILY_RUNNER_SLICE_READ.md` with these lines, each
on its own line, then a short free-text section citing what you read:
```
DENOMINATOR: <n> dispatch entries read
VERDICT: RUNS-SLICE   (or NO-SLICE)
NOOP: YES             (or NO, or UNKNOWN because <reason>)
GROUNDING: infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:<line>, <other path>:<line>
```
`GROUNDING` cites `path:line` for every path, and every path exists in the tree.

### ACCEPTANCE

<criterion id="HG3-t13-AC1" cell_refs="HG-t-13"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R3_CHECKS/hg_t13_read.py</invocation><expect>READ-OK</expect></criterion>
`HG3-t13-AC1` -- the document carries the four lines in their grammar and every grounded path exists.

<expected_criteria>HG3-t13-AC1</expected_criteria>

Run each invocation from the worktree root. AC1 FAILS at the base: `READ-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Lambda invoke, no SSM send, no instance start, no vendor call, no `terraform init`/`plan`/`apply`, no `safe-apply`.**
  Read-only AWS reads are allowed. This is the `mdpf-daily-runner` EC2: **you send it nothing**.
- **Search** only inside the named paths above (rail: `comp-find` over a named path); a recursive repo search is denied.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task. If you ever arm one, name it in your
  report with its state at your close.
- **Refusal clause.** If the question cannot be answered from a read, set `NOOP: UNKNOWN because <reason>` and say what read would answer
  it in your report; file a surprise row (id `MDPF_HEALGAP-D1-W10-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class
  `OBSERVATION`) in the investigation file below. Rows are APPEND-ONLY. Write files with LF line endings and check `git diff --stat`.

<paths>
org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~10/MDAILY_RUNNER_SLICE_READ.md
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 3, the enrichment), cell `HG-t-13`.
<owned_cells>HG-t-13</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG3-t13-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~10/MDPF_HEALGAP.TO-HG-t13.mdaily-runner-slice-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG3-t13-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the file, the check's output, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed or read for change.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls; no grant, no write.
comp-adversary: DECLARED-NOT-APPLICABLE read-only.
risk: LOCAL -- one document; read-only reads.
direct_act: false -- a worker order; worker-light (a single-document read, under the 100-line floor).
</preflight>

Source: row MDPF_HEALGAP-S1; CTO round-2 analysis @1974b85f4e section 2.5 and section 3 item 6; decomposition round 3.
