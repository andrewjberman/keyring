# AMGT_RESAPP task order -- `AMGT-tt-2` -- THE REDEPLOY: the lambda carries tt-1

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-tt-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through its existing Terraform resource.
comp-adversary: RUN by the issuer at the cut -- 2 of 2 acts carded in the COO half (1 served property, 1 writer, both branches named); BLIND to the CTO half (not yet written) and to the closure diff, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving only `opal-amgt-scoped-api`'s code. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-tt-2` (round 45, decomposition s.53)

**Begin only when all three hold:** `AMGT-tt-1` is `complete` and merged on CLOUD (the issuer's message names the build commit),
and both never-widen halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/NEVER_WIDEN_HALF_COO_TT2.md` and `1.0.0_SA_CTO~Z`'s. Act only inside them. **The acts,
in order, under ONE NEVER-2 entry opened AND COMMITTED before the build** (verify the commit reads back: a peer's drain can unstage a
staged entry): (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and print the closure
diff against the deployed build input; STOP on any of the halves' limbs; (2) build and upload the ONE artifact (read and record the
prior VersionId), then ONE `safe-apply`; (3) verify with the two criteria; close the entry. A criterion that fails after the apply is
the ROLLBACK trigger named in the halves. AC2 sweeps the LIVE research library on the served plane, read fresh; a name that arrives
with no identity is reported, held and routed to the issuer, never counted as an export failure.

## 2. BOUNDS

1. The two acts and nothing else, under ONE NEVER-2 entry committed before the build and closed in the same session.
2. A plan that moves a second resource, or a closure diff that hits a stop limb, is a REFUSAL: print it, stop, report.
3. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/**
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-tt-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-2.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from LK9h47juBfZPaAyfztAxDe9z65W2ZtEw6H2IJ/DcO4s= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-tt-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/checks/tt-2.AC2.sh; echo "exit=$?"</invocation><expect>served: absences missing=0 on N of N names; EXPORT-COMPARE OK on N of N (the LIVE research library, read time printed); sweep rc=0 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-tt-2.the-redeploy.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Seat order. Base: AC1 FAILS (CodeSha256 = LK9h47ju...DcO4s=); AC2's base is round 44's close-run served TSV @f4e94c87b7 (abs_missing 0 on 9 of 95), same instrument plus the missing-absence count. Both are build checks.

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-28, post-reboot):** the lane's close is `996b260d42` on the trunk (the pre-purge
`bdf48ee216`; the S19 rewrite re-hashed it, and `ed3caaba81` / `c29576fd0e` are the rewritten `ee87bf1506` / `9d9f38d823`).
AC1 RE-MEASURED by the issuer on the live function: `CodeSha256=vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew=
LastUpdateStatus=Successful LastModified=2026-09-26T23:35:04Z`, exit=0. Instance graded `proof-of-spec-check ... AC1,AC2
--governing-order <this order>`: VALID rc=0, violations 0. NEVER-2 entry `20260926T2128Z_amgt-tt-2-the-redeploy` reads CLOSED
at HEAD; no AMGT entry under `.open_deploys/` at HEAD. AC2 is the lane's served sweep (95 of 95, read 2026-09-26T23:55:10Z),
not re-run here. Row Z-S291 (INERT, disarm_owner this seat) stands; it bounds cross-round pdf digest comparison only.
<status>complete</status>
<round>45</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
