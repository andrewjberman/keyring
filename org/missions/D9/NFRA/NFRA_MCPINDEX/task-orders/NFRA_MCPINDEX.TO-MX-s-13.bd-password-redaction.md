# NFRA_MCPINDEX task order -- `MX-s-13` -- the live Black Diamond password leaves the 7 tracked files of the Z-S31 redaction set (R-10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~9</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a text edit to 7 tracked files; no schedule, rule, cron or monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or secret changes. Rotation is Andrew's and is NOT this order.
comp-adversary: DECLARED-NOT-APPLICABLE -- the scope is ruled (1.0.0_SA_CTO~O ~17:3xZ; round-2 analysis R-10).
EGRESS CLASS, declared: NONE. No AWS, no vendor, no network.
</preflight>

## 1. THE CELL -- `MX-s-13` (round 3, enrichment item 2; row Z-S31)

**Why.** A live Black Diamond password sits in tracked files. Andrew ruled: rotation LATER, and NO history rewrite. This
order removes the value from the working tree only.

**THE ONE RULE: never print, echo, log, hash-print, diff-print or commit any password value or fragment of one.** Read
the files with your editor tools and change the lines. Never run a command whose output would show a value: no
`grep` of the value, no `git diff` to the terminal on these files, no `cat`. To see what you changed, count lines. Your
report and rows name files and line numbers, never content.

**The 7 files (the complete redaction set):**
- `infra/aws/ec2/bd-exporter/src/stepwise/run-daily-downloads.sh`
- `infra/aws/ec2/bd-exporter/src/stepwise/run-backfill.sh`
- `infra/aws/ec2/bd-exporter/src/stepwise/run-allocation-backfill.sh`
- `infra/aws/ec2/bd-exporter/src/stepwise/historical-backfill-2014-2020.sh`
- `infra/aws/ec2/bd-exporter/src/stepwise/extended-backfill.sh`
- `infra/aws/ec2/bd-exporter/docs/PARALLEL_BACKFILL.md`
- `infra/aws/ec2/bd-exporter/terraform/QUICK_COMMANDS.md`

**The edits:**
1. **In each shell script,** a `BD_PASSWORD` default that carries a literal becomes
   `${BD_PASSWORD:?set BD_PASSWORD from Secrets Manager}`. Never write a placeholder that would attempt a login.
   `extended-backfill.sh` already reads `${BD_PASSWORD:?}` for BD_PASSWORD, but the CTO measured a DIFFERENT literal
   elsewhere in it. Find every literal credential in all 5 scripts, on any line, not only the BD_PASSWORD default.
2. **In each doc,** every literal password value becomes `<from Secrets Manager opal/bd/credentials>`. That includes
   occurrences on lines OTHER than an obvious `BD_PASSWORD=` line: the CTO found the live value in both docs "off the
   placeholder line".
3. **Nothing else changes.** No usernames, no logic, no other file.
4. Run AC1 and AC2. Commit under your serial.

## 2. BOUNDS

1. No history rewrite, no rotation, no AWS, no push.
2. Only the 7 files. If you find a literal credential in another tracked file, do NOT edit it. File a row naming the
   file and line number only.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/bd-exporter/src/stepwise/run-daily-downloads.sh
infra/aws/ec2/bd-exporter/src/stepwise/run-backfill.sh
infra/aws/ec2/bd-exporter/src/stepwise/run-allocation-backfill.sh
infra/aws/ec2/bd-exporter/src/stepwise/historical-backfill-2014-2020.sh
infra/aws/ec2/bd-exporter/src/stepwise/extended-backfill.sh
infra/aws/ec2/bd-exporter/docs/PARALLEL_BACKFILL.md
infra/aws/ec2/bd-exporter/terraform/QUICK_COMMANDS.md
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~9/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W9-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/s13.AC1.sh; echo "exit=$?"</invocation><expect>self-test: 15 of 15; non-empty BD_PASSWORD literals=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/s13.AC2.sh; echo "exit=$?"</invocation><expect>bash -n passes 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-s-13" judgment="true"><!-- graded at L8 by 3.0.0_SA_CVO~O with its fingerprint scan (the Z-C-S24 detector): 0 live-credential fingerprints in the 7 files. AC1 is a SHAPE proxy and cannot see a bare literal in prose; this is the oracle. The worker records nothing here. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~9/NFRA_MCPINDEX.TO-MX-s-13.bd-password-redaction.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, with files and line counts only. Do not edit this task
order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 2, R-10 @e4445020f5; 7-file set from
`org/tier1_exec/1.0.0_SA_CTO/handoffs/ctoO_2026-09-28_1630Z.md` (b501e0e3bc).
- Dry-run at base: s13.AC1 FAIL, 4 literals in 4 files of 44 (run-daily-downloads, run-backfill,
  run-allocation-backfill, historical-backfill-2014-2020), which matches R-10's shape read exactly. s13.AC2 PASS
  (5 of 5 parse; a regression guard).
- The detector's self-test is 15 of 15 and it prints no values. It does NOT see the docs' prose occurrences, so J1 (the
  CVO's fingerprint scan) is the oracle for them.
- Issuer disclosure: while debugging the detector at 20:4xZ, a helper of this seat printed an 11-character fragment of
  one script's default to this seat's own session output. It is in no file and no commit. The value is already exposed
  in tracked files and history, and rotation is Andrew's, carded, and not cut.
- Z-S31 and Z-S29 disarm fully only on Andrew's rotation.

<status>pending</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
