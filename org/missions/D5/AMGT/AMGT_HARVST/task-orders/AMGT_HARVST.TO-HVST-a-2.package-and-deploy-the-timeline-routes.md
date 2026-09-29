# AMGT_HARVST task order -- `HVST-a-2` -- ROUND 12 chain 1 of 3, cell 2 of 2: PACKAGE AND DEPLOY -- the scoped API answers both timeline routes with real data, timed in-region

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-a-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no cron, alarm, monitor or cadence moves; 0 AMGT entries open under org/critical_paths/.open_deploys/ at the cut.
comp-iam: RUN at L5 on the APPLIED plane (corrected by AMENDMENT 1, row AMGT_HARVST-Z-S36) -- opal-amgt-scoped-api-role's inline policy opal-amgt-scoped-api-grants reads 25 harvest resources, including every publisher's harvest/silver/* and the bucket itself, and NO amgt/harvest/gold/*; the two timeline loaders GET chatter_daily / chatter_event / article_security_mention under amgt/harvest/gold/, so this cell ADDS ONE read-only grant (s3:GetObject on arn:aws:s3:::opal-data-harvest/amgt/harvest/gold/*) in infra/aws/terraform/harvest/, carded on the halves. No write, no other grant.
comp-adversary: RUN at L5 -- the adversary is a deploy that MOUNTS both routes and ships code that cannot import pyarrow, so the gateway answers an import failure where a 404 used to be (row AMGT_HARVST-Z-S35). AC1 invokes the deployed function and requires HTTP 200 WITH DATA.
EGRESS CLASS, declared: (A) ONE S3 artifact write research/opal-amgt-scoped-api.zip (versioned; the prior VersionId is the rollback target); (B) at most ONE layer publish if the halves choose a layer; (C) ONE safe-apply on infra/aws/terraform/harvest/ moving the scoped API's code, its two new routes (and a layer attachment only if the halves name one); (D) any wheel download is sha256-pinned and named on the halves -- none is admitted otherwise. (E) ONE read-only IAM grant on the function's role, s3:GetObject on arn:aws:s3:::opal-data-harvest/amgt/harvest/gold/* (AMENDMENT 1).
</preflight>

## 0. BEGIN ONLY WHEN ALL THREE HOLD

1. `HVST-a-1` is `complete` and merged on CLOUD. The spawn message names its merge commit.
2. BOTH never-widen halves for this act are COMMITTED, and the spawn message names both paths:
   the COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round12/NEVER_WIDEN_HALF_COO_A2.md`
   and `1.0.0_SA_CTO~Z`'s half. **Act only inside them.** The halves fix the pyarrow wheel source and version, the
   unzipped budget against 250 MiB, and the rollback. If they conflict with this face, the halves win.
3. ONE NEVER-2 entry under `org/critical_paths/change_management/` is opened AND COMMITTED before the build, with its
   `.open_deploys/` sentinel, and reads back from HEAD.

## 1. THE CELL

Round 11 wired both timeline routes into `lib/research/api/scoped_amgt.py` (`HVST-z-0`) and `HVST-a-1` declares them
in `infra/aws/terraform/harvest/scoped-amgt-api.tf`. **Neither answers a user today, for two reasons, and this cell
removes both:**

1. **UNMOUNTED.** API `7k3ed8px20` carries 16 `/api/scoped/amgt/` routes and 0 timeline routes (the issuer's
   `get-routes` read at the cut, every page counted client-side: 106 routes over 5 pages).
2. **UNIMPORTABLE (row `AMGT_HARVST-Z-S35`).** The loaders import `lib.research.harvest.publication_gold` at
   FUNCTION scope, and it imports `pyarrow` at module scope (`publication_gold.py:37-38`); `store` reaches
   `lib.opal_naming` and its registry data. **The deployed package carries pyarrow 0, `lib/opal_naming` 0; its only
   layer `opal-amgt-print-deps:1` carries numpy 2.2.6 and pyarrow 0, at 121.7 MB unzipped.** Runtime `python3.11`,
   `x86_64`. The estate's working pattern for the same reader is the chatter-axis build
   (`infra/aws/terraform/harvest/lambda_src/build_zip.py:40-53`): pyarrow vendored, `lib.opal_naming` and its registry
   JSONs added to the closure roots, the unzipped total printed against 250 MiB and refused past it -- but that
   build is cp312, so its wheels do not carry across.

**The acts, in order, under the ONE entry:**
1. Make `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh` package what the two loaders import, by the
   mechanism the halves name. Run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only
   <tmp>` and print: the closure diff against the deployed artifact (VersionId `0XDw5hJWOYgx3P8CSA42oAlkLuTlupkS`),
   and the UNZIPPED total of package plus every layer against 250 MiB. STOP on any limb the halves name.
2. Build and upload ONE artifact (record the prior VersionId), then ONE `safe-apply` on
   `infra/aws/terraform/harvest/`. Print the plan first. A plan that moves anything the halves do not name is a
   REFUSAL: print it, stop, report.
3. Run AC1 and AC2. A FAIL after the apply is the ROLLBACK trigger named in the halves: re-point to the prior
   VersionId and `safe-apply` again, forward, then close the entry as ROLLED BACK.
4. Close the NEVER-2 entry in the same session.

## 2. BOUNDS

1. The acts above and nothing else. No runtime change, no memory or timeout change, no authorizer, no other route,
   and no IAM change beyond the ONE read-only gold grant named in the preflight (AMENDMENT 1).
2. **No S3 delete of any kind**, including a noncurrent artifact version -- the prior version IS the rollback.
3. No vendor call, no portal promote, no push of a shared branch, no key hunting.
4. `lib/research/api/` and this API serve AMGT_RESAPP's page. AC2 sweeps three of its routes as controls.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-a-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round12/checks/a-2.AC1.py</invocation><expect>AC1 RESULT: PASS (0 failure(s))</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-a-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round12/checks/a-2.AC2.py</invocation><expect>AC2 RESULT: PASS (0 failure(s))</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~A/AMGT_HARVST.TO-HVST-a-2.package-and-deploy-the-timeline-routes.proof_of_spec.json`
with `to_id` `AMGT_HARVST.TO-HVST-a-2.package-and-deploy-the-timeline-routes`. Report once: the closure diff and the
unzipped total, the plan's resource list, both criteria's output, the NEVER-2 entry's open and close commits, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **A SEAT ORDER, not a worker's.** Rule 13 puts infra deploys with AE; AMGT_RESAPP's redeploy `AMGT-tt-2` set the
   pattern (issued to `0.7.0_AE_CloudOps~A`, halves on both sides, NEVER-2 entry committed before the build). No AE
   seat was live at the cut; `~R` has no prior log and is seated for this project only. The spawn is this seat's act
   (`/mstr-spawn`) once the precondition in section 0 holds.
2. **Base dry-runs, by this seat at the cut:** AC1 FAIL as expected (6 failures; its first draft passed the ceiling
   arm vacuously on a 404 and was fixed to require a 200 first). AC2 FAIL as expected on its two build arms; its
   rollback-target arm and its three RESAPP controls PASS at the base.
3. **Why the packaging sits here and not in a worker cell:** the wheel source is either egress to PyPI (declared on
   `AMGT-tt-2`'s half as precedent) or an owned layer, and the 250 MiB budget is an infra call. Both belong on halves
   the CTO signs, which this seat writes only after `a-1` lands and a `--build-only` closure diff exists.
4. **The deploy moves RESAPP's served routes too** (one function, one artifact). The COO half cards that, and AC2's
   three controls are its exercised check.

**AMENDMENT 1 (issuer, 2026-09-28 ~23:3xZ, before any spawn) -- row `AMGT_HARVST-Z-S36`, filed by `4.0.0_SA_CRO~Z`
@f9acd618b1 (msg 26281).** The cut's comp-iam line said the role "already reads opal-data-harvest gold (the RESAPP
chatter routes)". **That was an inference, never a read, and it was false.** Re-measured by this seat on the APPLIED
plane (iam list/get role policies, both pages): 2 policies, 25 harvest resources, 0 under `amgt/harvest/gold/`. So the
deploy as cut would mount two routes that answer AccessDenied -- the third reason the timeline cannot answer, beside
`Z-S35`'s missing pyarrow. **Remedy, in this order's own scope:** the preflight line is corrected in place, the egress
class adds (E) one read-only grant, and bound 1 admits that one IAM change and no other. AC1 already refuses an
AccessDenied (it requires HTTP 200 with data). The issuer amends its own criteria without a CTO ruling (CLAUDE.md
rule 27, L6); **the gate limb that graded this modification: GATE (viii)** -- measured at the amendment commit `a60bd1bae5`
("1 of 1 staged-MODIFIED tree order(s) already declare <placeholders> at HEAD and were graded"). That commit's message
says "none"; the gate's own line is the record, and `<placeholders>NONE</placeholders>` counts as declaring. The CTO sees the grant on
the halves it signs.

**AMENDMENT 2 (issuer, 2026-09-29 ~00:5xZ) -- ONE COMBINED ACT, and the seat that runs it.** `1.0.0_SA_CTO~Z` ruled
(msg 26318) that HVST-a-2 and AMGT_RESAPP `AMGT-uu-4` run as ONE act -- one HEAD build, one apply, one change-management
entry naming both orders, one CloudOps seat -- under BOTH pairs, because a HEAD build ships each project's change and
neither may ship alone (uu-4 was refused on exactly that, @`c524129644`). **Re-addressed from `~R` (never seated) to
`0.7.0_AE_CloudOps~A`**, the live seat that measured this function's closure for uu-4 (recommended by
`2.0.0_SA_COO~Z`, msg 26321). `<issued_to>`, the deliverables path and `<slot>` move with it. Section 0's precondition
now reads: BOTH pairs' four halves committed (this order's two, `NEVER_WIDEN_HALF_COO_A2.md` and the CTO's; uu-4's
two); the ONE entry names both orders. Criteria unchanged; each project's graded separately at its own L9.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
