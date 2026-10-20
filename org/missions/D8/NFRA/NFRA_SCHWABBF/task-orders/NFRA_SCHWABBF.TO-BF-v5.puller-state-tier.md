# TO NFRA_SCHWABBF.TO-BF-v5 -- the puller writes 0840's run records and last_run to the state tier in the firm bucket

<to_id>NFRA_SCHWABBF.TO-BF-v5</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~2</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>keyform</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-v-5` (`decompositions/NFRA_SCHWABBF_DECOMP_R5.md`) |
**outcome_ref:** FWD-6 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`BF-v-5`, PRD v1.0 C-TIERS and C-DAILY. Andrew-direct ~17:0xZ: "a, yes. this needs to go through the same full bronze/silver process that the other masters go through." The puller's run records (`_ops/` and `meta/pulls/`) become the builder's `state` tier in the FIRM bucket for 08403355; 08242234 and 08335338 keep today's writes byte for byte. WORLD floor only because the file sits under `infra/`; nothing is deployed or run against Schwab or AWS.

**The contract (fixed in `decompositions/NFRA_SCHWABBF_DECOMP_R5.md`).** For firm-form master M = 08403355 (firm `49financial`, state bucket `opal-data-49financial`; builder output `address('schwab','49financial','state','daily_pull','date=2026-10-20')` is `s3://opal-data-49financial/schwab/49financial/state/daily_pull/date=2026-10-20`). The same run manifest file (`$mp`, the `$WORK\last_run.json`) is written to three places today (about lines 705-721 of `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`):
- `s3://$BUCKET/$OPSROOT/daily_pull/last_run.json` (ROLLING) -> `s3://opal-data-49financial/schwab/49financial/state/daily_pull/date={UTC date of the write}/08403355.last_run.json`;
- `s3://$BUCKET/$OPSROOT/daily_pull/runs/$RUNID.json` -> `s3://opal-data-49financial/schwab/49financial/state/daily_pull/date={UTC date of $RUNID}/08403355.$RUNID.json`;
- `s3://$BUCKET/schwab/$Master/meta/pulls/$RUNID.json` -> `s3://opal-data-49financial/schwab/49financial/state/pulls/date={UTC date of $RUNID}/08403355.$RUNID.json`.
`$RUNID` is `yyyyMMddTHHmmssZ` (line ~67 `(Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')`). Rolling objects: readers take the newest partition at or before today (CTO msg 109970). The write keeps `--sse AES256 --only-show-errors` and its existing WARN-on-failure behavior (the run record is diagnostic; a failure does not fail the pull). For 08242234 and 08335338 and for the staging target: unchanged.

**What exists (read first).** The script as merged by round 3 (`24eb435138`): `Test-FirmForm`, `Get-FirmOf`, `Get-BronzeKeyDir`, `$KEYROOT`, `$OPSROOT = "schwab/$Master/_ops"`, `$BUCKET = 'opal-data-assets'`, the pre-loop index and the post-run guard filtered by master, `-OnlyAsOf`. The 0840 box role currently has `_ops` and `meta/pulls` grants in `opal-data-assets` only (cell `BF-g-5` adds the firm-bucket grant).

**Build (edit `sdd-daily-pull.ps1` and one new test).**
1. Pure functions in the script (extractable by the PowerShell AST, as the existing tests do): `Get-StateBucket([string]$Master)` (the firm bucket for firm-form masters, `$null` otherwise) and `Get-StateKey([string]$Master,[string]$Table,[string]$DateIso,[string]$Name)` returning `schwab/{firm}/state/{table}/date={DateIso}/{Master}.{Name}`; a literal firm-to-bucket map for the five firm-form masters (`49financial` -> `opal-data-49financial`, `cottonwood` -> `opal-data-cottonwood`).
2. The three `aws s3 cp` calls use them when `Test-FirmForm $Master`; otherwise exactly today's calls. Dates come from `$RUNID` (first eight digits as `yyyy-MM-dd`) and from the UTC write time.
3. Tests `data/canonical/schwab/tests/test_sdd_daily_pull_state.py` (AST extraction harness like `test_sdd_daily_pull_key_form.py`; do NOT run the script, do NOT call AWS or Schwab): (a) KEY/BUCKET parity: for 08403355 and the four Cottonwood masters, the three destinations equal `address('schwab', F, 'state', table, 'date=D')` plus `/M.name`, with F and the bucket read from `infra/logic/registry/scopes.json` (the row whose `masters` lists M and its `bucket`), and the script's literal map equals the registry; (b) OLD: for 08242234 and 08335338 the three destinations equal the pre-change strings (compare with `git show 0429204ae7:<path>`); (c) the rolling `last_run` of two different UTC days lands in two different partitions; (d) an unknown master throws.

### ACCEPTANCE

<criterion id="BF5-v5-AC1" cell_refs="BF-v-5"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_state.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-v5-AC1` -- the three run-record destinations for the five firm-form masters against the builder and the registry, the unchanged destinations for 0824 and 0833, and the rolling-date rule.

<criterion id="BF5-v5-AC2" cell_refs="BF-v-5"><invocation>python -m pytest data/canonical/schwab/tests/test_sdd_daily_pull_key_form.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF5-v5-AC2` -- the control: the bronze key tests of the same script still pass (13 passed at the base).

<expected_criteria>BF5-v5-AC1,BF5-v5-AC2</expected_criteria>

Dry-run at the base: AC1 "file or directory not found" (rc 4) -- FAIL as expected; AC2 `13 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** You do not deploy, upload or run the puller, you do not contact Schwab, and you do not touch AWS. Fire times (do not change): 09:45, 10:15, 10:45, 21:45, 22:15, 22:45Z. The session lock, the vendor-master guard and the quarantines stay as they are.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W2-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W2-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]` and keep the file's own line endings; verify `git diff --numstat` shows only added lines). Do not weaken the test to pass.

<paths>
infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1
data/canonical/schwab/tests/test_sdd_daily_pull_state.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R5.md</decomp_doc> (round 5), cell `BF-v-5`.
<owned_cells>BF-v-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF5-v5-AC1, BF5-v5-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~2/NFRA_SCHWABBF.TO-BF-v5.puller-state-tier.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF5-v5-AC1,BF5-v5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the functions you added and the three call sites you changed (line numbers), the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- fire times inlined above; no schedule edit.
comp-iam: RUN -- decomposition battery scanned monolith-iam.tf and silver.tf (2 Terraform files); the box role has no write on the firm bucket today (cell BF-g-5 adds it) and the firm bucket's own policy (SSE or KMS requirement) was NOT read; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (a different bucket) and 3 (rolling objects take the write date) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v1.0 C-TIERS, C-DAILY; CTO msgs 109966 and 109970; decomposition round 5 cell BF-v-5; round-3 merge `24eb435138`.
