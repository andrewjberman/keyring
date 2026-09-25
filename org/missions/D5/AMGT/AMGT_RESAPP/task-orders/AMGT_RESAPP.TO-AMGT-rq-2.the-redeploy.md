# AMGT_RESAPP task order -- `AMGT-rq-2` -- THE REDEPLOY: the lambda carries rq-1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rq-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through its existing Terraform resource.
comp-adversary: RUN by the issuer at the cut -- 2 of 2 acts carded in the COO half (1 served property, 1 writer, 1 rule read); BLIND to the CTO half (not yet written) and to the closure diff, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving only `opal-amgt-scoped-api`'s code. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-rq-2` (round 42, decomposition s.50)

**Begin only when all three hold:** `AMGT-rq-1` is `complete` and merged on CLOUD (the issuer's message names the build
commit), AND both never-widen halves are committed:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/NEVER_WIDEN_HALF_COO_RQ2.md` and `1.0.0_SA_CTO~Z`'s.
The halves name what each act may touch and its rollback; act only inside them. **The acts, in order, under ONE NEVER-2 entry
opened before the build:** (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and
print the closure diff against the deployed build input (`git diff --stat <deployed build commit> <build commit> --
lib/research`); a file outside the halves' list, a change to `build_pack`, or a change to `scoped_amgt.py`'s pdf branch (the `if fmt == "rich":` gate or the `build_pack(display_form, block)` call in `_print_pack`) is a STOP and a report; (2) build and upload the
ONE artifact (record the prior VersionId), then ONE `safe-apply`; (3) verify with the two criteria; close the entry. A criterion
that fails after the apply is the ROLLBACK trigger named in the halves. AC2 sweeps the 89-name snapshot (`0.9.0_WK_AMGT_RESAPP~4/universe.json`, read 2026-09-10T23:18Z); the ABSENCE axis on all 89, the FIGURE axis on every name whose page carries figures on the served plane.

## 2. BOUNDS

1. The two acts and nothing else, under ONE NEVER-2 entry opened before the build and closed in the same session.
2. A plan that moves a second resource, or a closure diff outside the halves, is a REFUSAL: print it, stop, report.
3. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/**
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-2.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from pmH20bb+L1Kcejf4MKS4tVt+tCIPgeHwSZAsTe+nXZo= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-2.AC2.sh; echo "exit=$?"</invocation><expect>served over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-rq-2.the-redeploy.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Amended at the cut's CTO half (msg 25872): the pdf-branch stop limb added to step (1); no criterion changed, so no gate limb grades this modification. Seat order; the issuer restamps lib/research/api/_harvest_prefixes.py immediately before naming the build commit if gen_harvest_prefixes.py --check reads rc 1. The lane is live at the cut (process read).

<status>pending</status>
<round>42</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
