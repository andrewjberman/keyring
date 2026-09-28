# AMGT_RESAPP task order -- `AMGT-uu-4` -- THE REDEPLOY: the lambda carries the adjusted Base case

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-uu-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through its existing Terraform resource.
comp-adversary: RUN by the issuer at the cut -- AC3 is a served census over every live-library name that reads 0 of 48 at base; AC2 re-runs FWD-30 on the served plane so the page and the export must move together. The never-widen halves (written after uu-3 lands, against its landed rule) bound the act; BLIND at the cut to the closure diff, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving only `opal-amgt-scoped-api`'s code. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-uu-4` (round 46, decomposition s.54)

**Begin only when all three hold:** `AMGT-uu-3` is `complete` and merged on CLOUD (the issuer's GO names the build commit), and
both never-widen halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/NEVER_WIDEN_HALF_COO_UU4.md`
and `1.0.0_SA_CTO~Z`'s. Act only inside them. **The acts, in order, under ONE NEVER-2 entry opened AND COMMITTED before the
build** (verify the commit reads back): (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>`
and print the closure diff against the deployed build input (baseline by CONTENT: the deployed CodeSha256
`vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew=`, artifact VersionId `0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS`); STOP on any of the
halves' limbs; (2) build and upload the ONE artifact (read and record the prior VersionId at build time), then ONE `safe-apply`;
(3) verify with the three criteria; close the entry. A criterion that fails after the apply is the ROLLBACK trigger named in
the halves. AC2 and AC3 read the LIVE research library on the served plane, fresh; a name that arrives with no identity is
reported, held and routed to the issuer, never counted as a failure. AC2's harness runs from your worktree's `portal/`, which
must be cut from local portal `DEV` at the issuer's GO (it carries uu-2's harness and uu-3's page change).

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
  <criterion id="AC1" cell_refs="AMGT-uu-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-4.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from vBSCqd71wGn1GNOpaWGKr+KdI6t+zo3QVovzEd9Mrew= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-uu-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-4.AC2.sh; echo "exit=$?"</invocation><expect>served: absences missing=0 on N of N names; EXPORT-COMPARE OK on N of N (the LIVE research library, read time printed); sweep rc=0 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-uu-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-4.AC3.py; echo "exit=$?"</invocation><expect>served: reads OK N of N names (failed 0); base SERVED M; ADJUSTED AND BASIS-CARRYING M of M, M at least 1 -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-uu-4.the-redeploy.proof_of_spec.json`. Report once, as a FILE in `org/mcp/inbox/2.0.0_SA_COO/~Z/` if the broker send is down: what you changed and where, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** seat order (a deploy is WORLD). Base: AC1 FAIL (CodeSha256 = vBSCqd71...Mrew=), AC2 PASS (95 of 95 tonight --
the no-regression arm: the page and the export must still agree after BOTH move), AC3 FAIL (0 of 48 served SERVED bases on the
adjusted basis). The COO never-widen half is written AFTER uu-3 merges, against its landed rule (round 45's lesson: a half written
before the producer lands is a prediction). `0.7.0_AE_CloudOps~A` is not live at the cut; the issuer seats it at the GO.

<status>pending</status>
<round>46</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
