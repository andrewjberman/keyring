# Deploy-completion ledger: mdpf-pipeline /mdpf/custody_source (CLOSED -- finding was FALSE POSITIVE, deploy net-no-op)

**Status:** CLOSED (2026-07-07T15:56Z)
**Opened:** 2026-07-07T15:45Z
**Agent:** 0.5.0_AE_OpalETL
**Authorization:** COO GO 20260707T153523Z; correction filed 20260707T155624Z

## Corrected root cause (supersedes the OPEN-state narrative below-the-line)
The originating "drift landmine" finding was a FALSE POSITIVE. /mdpf/custody_source existed
CONTINUOUSLY since 2026-07-01 21:14Z: it was already TF-managed by
`aws_ssm_parameter.mdpf_custody_source` (lambdas.tf:55; deliberate `ignore_changes=[value]` +
operational-flip design), created v1=bd dormant, flipped v2=schwab 07-02 14:06Z in the cutover
window. Every "ParameterNotFound" that grounded the finding came from Git Bash aws calls whose
leading-slash `--name /mdpf/custody_source` was MSYS path-mangled -- the documented CLAUDE.md
footgun (leading-/ aws args need PowerShell). PowerShell get-parameter-history is the definitive
correction record (v1 bd 07-01 / v2 schwab 07-02 / v3-v4 schwab today, this deploy's writes).

## What was actually deployed (net-no-op on substance)
1. Commit 338f754b5 lineage: duplicate `aws_ssm_parameter.custody_source` (ssm.tf) applied with
   overwrite=true -> wrote v3=schwab (value unchanged).
2. Duplicate discovered via the resulting tag/description perma-diff against the canonical
   resource -> `terraform state rm aws_ssm_parameter.custody_source`, ssm.tf deleted (committed).
3. Canonical resource reconciled its description/tags (v4=schwab, value unchanged, apply
   0-add/1-change/0-destroy).
4. **Final plan: "No changes." (0-diff CONFIRMED).** Live param (PowerShell): value=schwab, v4,
   no policies. State clean, single canonical resource, design exactly as authored 07-01.

## Checklist
- [x] Ledger opened at deploy-start
- [x] Commits: ssm.tf add (2x) + retraction (safe-commit, agent author line)
- [x] plan -> safe-apply (HALTGT) -> reconcile apply -> **0-diff**
- [x] Live verify (PowerShell, non-mangled path): value=schwab
- [x] CHANGELOG + tag mdpf-pipeline-v1.2.1 + push --follow-tags (same session)
- [x] COO corrected-record RAVC (20260707T155624Z)
- [x] Exercised leg: NOT required post-correction -- the 15:01Z nightly bootstrap
      (export CUSTODY_SOURCE=schwab, SSM cmd b0e86ed2) already exercised the healthy path today.

## Lessons (banked to memory + session log)
- A Git Bash `aws` NotFound on a leading-slash identifier is NOT existence evidence; SSM
  parameter ops go through PowerShell. A surprising-absence claim needs a second independent
  probe path BEFORE it grounds a finding, a dispatch, or a GO request.
- Grep the TF module for the RESOURCE TYPE (`aws_ssm_parameter`) before authoring a "new" one --
  the canonical resource was one comp-grep away the whole time.
