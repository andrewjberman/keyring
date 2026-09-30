# AMGT_RESAPP task order -- `AMGT-yy-5` -- THE ONE BUILD: THE DEPLOY AND THE NEO PERSIST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-yy-5</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- the dossier read (research_dossier/) and the management read (management/v1) are already granted; the plan must show NO IAM change. The two M-1 writes use the roster pool writer's existing write path.
comp-adversary: RUN by the issuer at the cut -- AC2-AC4 read the deployed function for each served move, each FAILING at the base.
EGRESS CLASS, declared: EDGAR through lib/research/filings/fetch.py for the two persist runs (R-21, scripted); the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-yy-5` (round 50, decomposition s.58)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair (CTO round-49 ruling 2): redeploy `opal-amgt-scoped-api` carrying
`AMGT-yy-2` (/thesis `dossier_fields`), `AMGT-yy-3` (the management pass-through of the NEO label) and `AMGT-yy-4` (the base case's
owner label), AND run the scripted persist for the two pointer names so their served management is the NEO set.

**Begin only when all four hold:** yy-2, yy-3 and yy-4 are `complete` and merged (the issuer's GO names the build commit); both halves
are committed -- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/NEVER_WIDEN_HALF_COO_YY5.md` and
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND50_YY5_CTO_HALF.md`; and **the base CodeSha256 the halves name is still the
live one, re-read immediately before the build -- a moved base is a STOP and a re-sign.** **The acts, in order, under the entry opened
AND COMMITTED before the build** (sentinel + entry): (1) pre-apply captures the halves name; (2) build + upload the ONE artifact
(record the prior VersionId), content-diff it against the deployed object, then ONE `safe-apply` -- print the plan first; code only;
(3) `python -m lib.research.management.proxy_officers --persist --security-key INTU_US_Equity` and the same for `HAL_US_Equity`
(committed code; EDGAR only through fetch.py); (4) verify with the four criteria; close the entry. A criterion failing after the act
is the ROLLBACK trigger named in the halves.

## 2. BOUNDS

1. The act and nothing else. A plan beyond the function's code, a closure beyond the halves' list, or a gate refusal is a REFUSAL.
2. Standing: no S3 delete, no vendor call outside fetch.py, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-yy-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy-5.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from Um3BOJ+jcVc3B79VuFCn4RyD5VYu+IzCpe3BQOP/p7A= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-yy-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_thesis.py --plane served --what fields; echo "exit=$?"</invocation><expect>plane served: pillars P of P over 4 names, /THESIS PASSES THE DOSSIER'S FIELDS: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-yy-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_thesis.py --plane served --what label; echo "exit=$?"</invocation><expect>THE BASE CASE NAMES ITS OWNER: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-yy-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round50/checks/yy_neo.py --plane served; echo "exit=$?"</invocation><expect>THE PROXY'S OFFICERS ARE SERVED AS NAMED EXECUTIVE OFFICERS (served): YES -- and exit=0</expect></criterion>
</proof_of_spec>

A fourth criterion, reason: ruling 2 puts three served moves in ONE act, so each move keeps its own served read.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-yy-5.the-one-build.proof_of_spec.json`. Report once: what changed and where, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-49 analysis s.4 rows 2-4, ruling 2. Base: AC1 FAIL (Um3BOJ+j...), AC2 FAIL (pillars 0 of 15), AC3 FAIL
(ADBE 'Historical-multiple reference'), AC4 FAIL (HAL source None). The COO half is written after yy-2/3/4 land, against the landed
code and the then-live base.

<status>pending</status>
**ISSUER CLOSE (`2.0.0_SA_COO~Z`, 2026-09-30 ~02:3xZ):** landed; entry `amgt-resapp-yy5-one-build-20260930` CLOSED 3 of 3 02:04:25Z (committed @67becd1b9f). The issuer re-measured all four on the served plane at `pVa+sgzj8XNZ9uvJqCOwRNCJn0IZhUklnWZh6JbO7B0=` (01:46:54Z): AC1 PASS; AC2 pillars 13 of 13 YES; AC3 owner label YES; AC4 INTU + HAL 5 NEOs each, DEF 14A 000089687825000057 / 000004501226000033, YES. Two M-1 first mints validate against management.schema.json; the 09-18 objects untouched. Instance graded VALID rc=0. Built at 50cc86edd6 (a HEAD build REFUSED at the REGISTRY_HASH guard, row Z-S306), so only the signed nine files shipped. **CORRECTION, the issuer's (row Z-S307):** the COO half's 'lib/opal_naming.py is not packaged' was read from code comments, not the build manifest; it IS packaged (with six registry JSONs and NAMING_SCHEMA.json). No wrong file shipped only because the build commit predated it. Row Z-S308: the issuer's 'no AMGT sentinel open' reads were shared-tree only; four sit on undrained worker branches.
<status>complete</status>
<round>50</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
