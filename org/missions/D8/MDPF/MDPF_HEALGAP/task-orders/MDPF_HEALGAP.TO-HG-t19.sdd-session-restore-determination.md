# TO MDPF_HEALGAP.TO-HG-t19 -- round 5 HG-t-19: what the SDD puller's SDDSecure holds, who writes it, and the act that restores it
<to_id>MDPF_HEALGAP.TO-HG-t19</to_id>
<project>MDPF_HEALGAP</project>
<issued_to>0.9.0_WK_MDPF_HEALGAP~16</issued_to>
<issued_by>2.0.0_SA_COO~G1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `HG-t-19` (`decompositions/MDPF_HEALGAP_DECOMP.md`, ROUND 5) |
**outcome_ref:** FWD-6 (D1-W14-S2), CTO round-4 analysis item 2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`HG-t-19`. The three Schwab SDD pulls (`schwab-canonical-si2-08403355-pull-daily`, `canonical-schwab-si2-08242234-daily-pull`,
`canonical-schwab-si2-08335338-daily-pull`) run `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` on a Windows box as the Administrator
scheduled task. The round-3 census named the act that refills their standing session as the capture task `SchwabSddCapture`
(`run-capture.ps1`). Round 4 found that this capture writes Secrets Manager `schwab/sdd/session`, but the puller reads Credential Manager
`SDDSecure` (`sdd-daily-pull.ps1:229`), and no in-repo code was found that writes `SDDSecure`. The CTO ruled (round-4 analysis section 2,
D1-W14-S2): the census row is WRONG as written; this cell reads, FROM THE CODE, what `SDDSecure` holds and who writes it, then reaches ONE decision.
You produce ONE document, `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/SDD_SESSION_RESTORE_DETERMINATION_R5.md`.
You read the repository only: no AWS call that changes anything, no SSM command, no access to the box, no secret value.

**Where to start (read each, then search outward):**
- the puller: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1` lines 18-19, 33, 145-147, 229 (CredRead of `SDDSecure`), 270-272 (the text that
  says a human re-establishes the session);
- the capture: `infra/aws/ec2/canonical-schwab-si2/run-capture.ps1` (lines 17, 23, 29) and `infra/aws/ec2/canonical-schwab-si2/schwab_sdd_session_capture.py`
  (lines 6, 10);
- the round-4 findings: `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~14/FWD6_SEVEN_DISPOSITIONS_R4.md` (the three SDD rows) and surprise
  row `MDPF_HEALGAP-D1-W14-S2` in the investigation file;
- anything in the repository that mentions `SDDSecure` or `schwab/sdd/session`: search `infra/aws/ec2/canonical-schwab-si2/`, `infra/aws/terraform/`
  (the SI2 / canonical-schwab roots), `tools/` and `docs/` with the native Grep tool and COUNT the files you searched; a search that returns zero is
  only an absence over a stated denominator.

**The document has exactly five level-2 headings, in this order (the check reads them):**

```
## 1. The reader
## 2. The writers
## 3. The capture
## 4. The same thing?
## 5. Decision
```
- **1:** what the puller reads, where, and what an empty read means to it (cite `path:line`).
- **2:** a line `SEARCHED: <n> files` (n is the count of files you searched, > 0) and EITHER one or more writers of the credential the puller
  reads, each as a `path:line` citation, OR the exact line `WRITERS FOUND: 0`.
- **3:** what the capture writes and where (cite `path:line`).
- **4:** exactly one line `COMPARISON: SAME`, `COMPARISON: DIFFERENT` or `COMPARISON: UNDETERMINABLE FROM CODE`, with your citations.
- **5:** exactly ONE decision line, and its required lines:
  - `DECISION: NAMED-ACT` -> a line `PERSON:` (who does it) and `TRIGGER:` (what shows the session is dead), citing the puller's own text;
    use when a human act on the box is what restores `SDDSecure` (the puller's text at `:270-272` says so).
  - `DECISION: REPOINT` -> a line `PAIR:` naming the never-widen pair the repoint would need, and section 4 reads `COMPARISON: SAME`; use only if
    the two stores hold the same thing, so the puller could read the session the capture already writes.
  - `DECISION: BOX-READ-OWED` -> lines `READ-COMMAND:` (the exact read: the command, what it prints) and `RUNS-AS:` (the identity it must run as to
    see the Administrator's Credential Manager vault); use when the code cannot settle it and a read on the box is the only evidence.
  No new credential path is to be built. Do not guess: where the code is silent, say so and choose `BOX-READ-OWED`.

### ACCEPTANCE

<criterion id="HG5-t19-AC1" cell_refs="HG-t-19"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_HEALGAP_G1/R5_CHECKS/hg_t19_sdd.py</invocation><expect>SDD-OK</expect></criterion>
`HG5-t19-AC1` -- the document carries the five headings in order, a `SEARCHED: n files` denominator with either writer citations or `WRITERS FOUND: 0`, exactly one `COMPARISON` and one `DECISION` line with the lines that decision requires, every `path:line` resolving in the repository, and no TBD.

<expected_criteria>HG5-t19-AC1</expected_criteria>

Run the invocation from the worktree root. It FAILS at the base (`SDD-BAD no document at ...`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only.** No AWS write, no SSM `SendCommand`, no Lambda invoke, no access to the SI2 box, no `GetSecretValue`, no vendor call, no edit to any
  code, script or Terraform.
- **NEVER ADD** an alarm, SNS topic, SES send, freshness checker or monitor (standing moratorium).
- **Honest document.** Cite only lines you read; if a conclusion rests on what the code does not contain, say that in the section and give the
  denominator. A `NAMED-ACT` decision requires that the code you read shows a human act restoring `SDDSecure`; if it shows only that the puller
  expects one, say exactly that in section 5.
- **Restore mechanisms (CTO round-1 analysis 2.2):** you arm no timer, background task or OS task.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_HEALGAP-D1-W16-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file
  below, and do not weaken a check. Rows are APPEND-ONLY: never edit an existing row. Write the file with LF line endings and check
  `git diff --stat` shows only your added lines before committing.

<paths>
org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/SDD_SESSION_RESTORE_DETERMINATION_R5.md
org/missions/D8/MDPF/MDPF_HEALGAP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_HEALGAP/decompositions/MDPF_HEALGAP_DECOMP.md</decomp_doc> (round 5, the enrichment), cell `HG-t-19`.
<owned_cells>HG-t-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: HG5-t19-AC1. Instance at `org/missions/D8/MDPF/MDPF_HEALGAP/deliverables/0.9.0_WK_MDPF_HEALGAP~16/MDPF_HEALGAP.TO-HG-t19.sdd-session-restore-determination.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> HG5-t19-AC1 --governing-order <this order file>` BEFORE the flip.
</proof_of_spec>

**REPORT:** the document path, the check's output, the decision token, commits, and every row you filed.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this order arms no gate and adds no schedule; it is a read-only document.
comp-iam: DECLARED-NOT-APPLICABLE this order changes no role, grant or policy; it reads code.
comp-adversary: RUN -- `comp-adversary compose` over this order 2026-10-13 17:2xZ: 0 cited commits, 9 cited paths (2 GONE: the deliverable and the proof instance, both written by the worker), 0 proof instances, 0 unproven dependencies. The code cannot read the box's Credential Manager vault; the decision token BOX-READ-OWED exists for exactly that case.
risk: LOCAL -- a document under a deliverables folder; no code, config or AWS write.
direct_act: false -- a code-reading determination across a Windows box's scripts is above the direct-act size floor; the full limbs run.
</preflight>

Source: CTO round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` section 2 (D1-W14-S2) and section 3 item 2, msg 4962; the round-4 document HG-t-17; decomposition round 5.
