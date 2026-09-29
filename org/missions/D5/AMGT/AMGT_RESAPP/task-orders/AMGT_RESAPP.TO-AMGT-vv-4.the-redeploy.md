# AMGT_RESAPP task order -- `AMGT-vv-4` -- THE REDEPLOY: the lambda carries the basis-true formula and the team's cases

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-vv-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: RUN by the issuer at the cut -- ONE read grant is added: the prefix `amgt/harvest/gold/research-dossier/` joins `local.scoped_amgt_pool_prefixes` in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, so the file's existing two statements grant `s3:GetObject` under it and a prefix-conditioned `s3:ListBucket` on it; no write, no delete, no other action, no other prefix. The list read at the cut holds 29 entries and not this one.
comp-adversary: RUN by the issuer at the cut -- AC3 reads every live name on the served plane, formula AND team cases, against the one dossier read; AC2 re-runs FWD-30 so the page/export parity must hold after the deploy. The never-widen halves (written after vv-1 and vv-2 land, against their landed code) bound the act; BLIND at the cut to the closure diff, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving `opal-amgt-scoped-api`'s code and the ONE pool-prefix entry above. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-vv-4` (round 47, decomposition s.55)

**Begin only when all three hold:** `AMGT-vv-1` and `AMGT-vv-2` are `complete` and merged on CLOUD (the issuer's GO names the build
commit), and both never-widen halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/NEVER_WIDEN_HALF_COO_VV4.md`
and `1.0.0_SA_CTO~Z`'s. Act only inside them. **The acts, in order, under ONE NEVER-2 entry opened AND COMMITTED before the build**
(verify the commit reads back): (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and print
the closure diff against the DEPLOYED build input, by content (deployed CodeSha256 `CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`;
read the artifact VersionId at build time); STOP on any of the halves' limbs; (2) add the ONE pool-prefix entry named in the
preflight, build and upload the ONE artifact (record the prior VersionId), then ONE `safe-apply` -- print the plan first; (3) verify
with the three criteria; close the entry. A criterion that fails after the apply is the ROLLBACK trigger named in the halves. AC2 and
AC3 read the LIVE research library on the served plane, fresh; a name that arrives with no identity is reported, held and routed to
the issuer, never counted as a failure. AC2's harness runs from your worktree's `portal/`, cut from local portal `DEV` at the GO.

## 2. BOUNDS

1. The two acts and nothing else, under ONE NEVER-2 entry committed before the build and closed in the same session.
2. A plan that moves anything the halves do not name, or a closure diff that hits a stop limb, is a REFUSAL: print it, stop, report.
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
  <criterion id="AC1" cell_refs="AMGT-vv-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-vv-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC2.sh; echo "exit=$?"</invocation><expect>served: absences missing=0 on N of N names; EXPORT-COMPARE OK on N of N (the LIVE research library, read time printed); sweep rc=0 -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-vv-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC3.py; echo "exit=$?"</invocation><expect>served: reads OK N of N (failed 0); formula as ruled M of M; team_cases as the dossier holds them N of N names, at least one case SERVED -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-vv-4.the-redeploy.proof_of_spec.json`. Report once, as a FILE in `org/mcp/inbox/2.0.0_SA_COO/~Z/` if the broker send is down: what you changed and where, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** seat order (a deploy is WORLD). Waits on vv-1 AND vv-2 (vv-2 waits on AMGT_CORPUS). The COO half is written AFTER
both land, against the landed code, by running the landed rule over every live name (round 46's method). Base: AC1 FAIL (CodeSha256 =
CtIvirvM...), AC2 PASS (95 of 95 at round 46's close -- the no-regression arm), AC3 FAIL (formula as ruled 0; no team_cases).

<status>pending</status>
<round>47</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
