# AMGT_RESAPP task order -- `AMGT-rr-3` -- THE REDEPLOY: the lambda carries rr-2

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rr-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through its existing Terraform resource.
comp-adversary: RUN by the issuer at the cut -- 2 of 2 acts carded in the COO half (1 served property, 1 writer); BLIND to the CTO half (not yet written) and to the closure diff, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving only `opal-amgt-scoped-api`'s code. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-rr-3` (round 43, decomposition s.51)

**Begin only when all four hold:** `AMGT-rr-2` is `complete` and merged on CLOUD (the issuer's message names the build commit);
`AMGT-rr-1` is `complete`; and both never-widen halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/NEVER_WIDEN_HALF_COO_RR3.md` and `1.0.0_SA_CTO~Z`'s.
Act only inside them. **The acts, in order, under ONE NEVER-2 entry opened AND COMMITTED before the build:** (1) run
`bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and print the closure diff against the
deployed build input (`9b7b146d9a`); STOP on any of the half's three limbs; (2) build and upload the ONE artifact (record the
prior VersionId), then ONE `safe-apply`; (3) verify with the two criteria; close the entry. A criterion that fails after the apply
is the ROLLBACK trigger named in the halves. AC2 sweeps the LIVE research library on the served plane with the CASES axis
graded.

## 2. BOUNDS

1. The two acts and nothing else, under ONE NEVER-2 entry committed before the build and closed in the same session.
2. A plan that moves a second resource, or a closure diff that hits a stop limb, is a REFUSAL: print it, stop, report.
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
  <criterion id="AC1" cell_refs="AMGT-rr-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-3.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from FOF+dRXoW1KFFzD0moLigsMB2LMmIjwhwURq7FkCzbw= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rr-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round43/checks/rr-3.AC2.sh; echo "exit=$?"</invocation><expect>served over 94 of 94 folders (the live research library at the cut, pinned): OK 94, NOT_OK 0, CAPTURE_FAILED 0, with cases over 94 of 94 compared names at missing=0 extra=0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-rr-3.the-redeploy.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Amendment 1 (issuer, ~23:5xZ, on the lane's HELD entry): AC2's population is pinned to the 94 folders the live library held at the cut; 'AIA Group', added after the cut with no identity, is new scope (row filed). Gate limbs: a MODIFIED order without <placeholders> is graded by none. Seat order; the issuer restamps lib/research/api/_harvest_prefixes.py immediately before naming the build commit if gen_harvest_prefixes.py --check reads rc 1. N is the live library's count at the run, printed with its read time (94 at the cut).

<status>pending</status>
<round>43</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
