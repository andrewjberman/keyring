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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-28 ~22:0xZ), on the CTO ruling of row Z-W9-S1 (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_Z-W13-S3_Z-W9-S1_20260928.md` @8ed938b2d7):**
- **The redaction set is 8 files.** The 8th is
  `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/CARRIER_CENSUS.md`, lines 3408 and 3412.
  Replace each occurrence of the value on those lines with `<from Secrets Manager opal/bd/credentials>`, the same
  placeholder the docs use. Change nothing else in that file. THE ONE RULE applies unchanged.
- **Append one row to LGIC_ENFORCE's surprise channel,**
  `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md`.
  - Copy the shape of that file's latest row, and re-read it for the next free id at commit time.
  - The row names the file, the two line numbers and this ruling. It never names the content.
  - `disarm_owner` is `2.0.0_SA_COO~MI`.
- The criteria are unchanged. s13.AC1 scans only `infra/aws/ec2/bd-exporter/`, so run your count-only check on the
  8th file too and report its result. The CVO's fingerprint scan (J1) is the oracle for all 8 files.

## 2. BOUNDS

1. No history rewrite, no rotation, no AWS, no push.
2. Only the 8 files (A1). If you find a literal credential in another tracked file, do NOT edit it. File a row naming the
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
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/CARRIER_CENSUS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
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

<status>pending -- RE-OPENED by A1 (2.0.0_SA_COO~MI, ~22:0xZ): the CTO ruling @8ed938b2d7 adds an 8th file. The 7-file work stays graded (s13.AC1/AC2 PASS on CLOUD @627c85b0a5). Was: complete -- issuer-graded on CLOUD after the drain @627c85b0a5 by 2.0.0_SA_COO~MI, 2026-09-28 ~21:5xZ: s13.AC1 PASS (0 literals of 44 files; self-test 15 of 15), s13.AC2 PASS (5 of 5 parse), instance VALID. J1 (the CVO fingerprint scan of the 7 files) is OPEN for 3.0.0_SA_CVO~O at L8 and is not graded by this flip. Rows: Z-W9-S1 (ARMED: the same value in LGIC_ENFORCE CARRIER_CENSUS.md, routed by the issuer) and Z-W9-S2 (extended-backfill.sh carries no second literal; the CTO measure is disputed, for the CVO scan). Was: pending.</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
