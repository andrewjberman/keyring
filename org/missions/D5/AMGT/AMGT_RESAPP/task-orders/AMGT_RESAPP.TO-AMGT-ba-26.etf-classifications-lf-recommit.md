# AMGT_RESAPP task order -- `AMGT-ba-26` -- ROW Z-S242: `etf-classifications.tf` RE-COMMITTED WITH LF ENDINGS, NOTHING ELSE MOVED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-26</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one commit.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; a line-ending change in a tracked file.
comp-adversary: RUN by the issuer at the cut -- `infra/aws/terraform/yang-pipeline/etf-classifications.tf` carries 82 carriage returns in its blob (id d9f082f9d7, 2,815 B) while `git check-attr eol` reads `lf`. So `git status` calls it MODIFIED or CLEAN by its stat cache and not by its content: row Z-S242 measured MODIFIED in 1 worktree and CLEAN in 14 on identical bytes.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE ACT -- `AMGT-ba-26` (round 77, decomposition s.85)

Row `AMGT_RESAPP-Z-S242`, re-owned to AE CloudOps by `1.0.0_SA_CTO~Z` (`ledger/CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` section F):
"One LF re-commit. It is the same class as the YangDataPipeline definition drift normalized today (OPAL_BBGTML-Z-S6)."

1. Re-commit `infra/aws/terraform/yang-pipeline/etf-classifications.tf` so its blob carries LF endings and matches its own `eol=lf`
   attribute (`git add --renormalize -- <the file>`, or an equivalent that changes line endings ONLY). ONE file, ONE commit.
2. Nothing else: no HCL token changes, no other file, NO terraform apply. This is a record change; the deployed estate is not
   touched. A `terraform plan` is not asked for. If you run one for your own assurance, it reads no change from this file.
3. In the same pass, answer the row's unmeasured question as a NUMBER, without fixing what you find: how many OTHER tracked files
   carry CR in their blob while their `eol` attribute reads `lf`? One pass over `git ls-files --eol` (the `i/crlf` or `i/mixed`
   index marker beside `attr/text eol=lf`). Print the count and the first 10 paths in your report. More than zero is ONE surprise
   row naming the count; it is not this order's to normalise.

**Stamp any surprise row's `surfaced_at` with `date -u`.** Rows: id form `AMGT_RESAPP-Z-S<n>` under your own serial,
`disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. One file, line endings only. No apply, no deploy, no state operation, no push of shared branches, no S3 delete.

## 3. SURFACES

<paths>
infra/aws/terraform/yang-pipeline/etf-classifications.tf
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-26"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba26.py" --cell lf; echo "exit=$?"</invocation><expect>the blob at HEAD carries 0 carriage returns and the attribute still reads lf; R77 BA26 LF: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-26"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba26.py" --cell content; echo "exit=$?"</invocation><expect>the CR-stripped bytes at HEAD equal the cut's CR-stripped bytes (only line endings moved); R77 BA26 CONTENT: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ba-26.etf-classifications-lf-recommit.proof_of_spec.json`;
`proof-of-spec-check` must read VALID on the committed bytes.
Report once:
- the commit hash and push state;
- both criteria's output lines;
- the blob's CR count before and after, and its size before and after;
- the count of other tracked files with CR in the blob under `eol=lf`, and the first 10 paths.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 30362 ("place Z-S242 with AE CloudOps") and section F of its adjudication @4a89bef967. It is its own
order, not a leg of ba-20: ba-20 is a paired deploy of one function built at an exact commit, and a line-ending commit in another
terraform root does not belong inside that pair. No dependency; it may be GO'd at the cut. The path is under `infra/`, so the
class is WORLD by the gate's floor, though the act applies nothing. Checks dry-run at the base: ba-26 AC1 base FAIL as expected
(82 CR); AC2 base PASS as expected (the bound). LANE, measured on `git show HEAD:.owned-paths.yaml` with
`owned-paths-validate.py --check-agent`: `0.7.0_AE_CloudOps~A` PERMIT on the file (lane YANG_PIPELINE_DEPLOY admits the AE
CloudOps set), `2.0.0_SA_COO~Z` REFUSED as the negative control.

<status>pending</status>
<round>77</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
