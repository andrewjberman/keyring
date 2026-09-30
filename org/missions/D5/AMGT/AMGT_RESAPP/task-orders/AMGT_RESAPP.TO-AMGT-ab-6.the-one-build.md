# AMGT_RESAPP task order -- `AMGT-ab-6` -- THE ONE BUILD, AND ASML'S D-1 DRIVER SPLICE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ab-6</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN by the issuer at the cut -- round 51's 3 simulate calls on opal-amgt-scoped-api-role stand for the reads this build keeps (crosswalk GetObject ALLOWED; ListBucket and the ranking Query NOT-DECIDABLE, exercised live); the dossier read is already served. BLIND: the D-1 object write runs under the executor's credentials, not simulated; the plan must show NO IAM change.
comp-adversary: RUN by the issuer at the cut -- AC1-AC4 each read the deployed function or the served route, each FAILING at the base.
EGRESS CLASS, declared: NONE for the acts; the build pip-downloads its pinned wheels.
</preflight>

## 1. THE ACT -- `AMGT-ab-6` (round 52, decomposition s.60)

ONE act, under ONE NEVER-2 entry and ONE never-widen pair: (1) redeploy `opal-amgt-scoped-api` carrying AMGT-ab-2 (every name's
`dossier_fields` block; `pack_shape` pass-through), AMGT-ab-4 (comments) and the closure the build's content diff names (including
`lib/research/corpus/dossier.py`'s METHOD_VERSION `/5`, which moves the dossier read to the `/5` objects); AND (2) write ONE object,
`s3://opal-data-harvest/drafting/v1/ASML_NA_Equity.json`, with AMGT-ab-1's committed splice:
`python -m lib.research.filings.drafting_build --splice-driver --only-keys ASML_NA_Equity --pre-act-dir <your deliverables>/ab6-pre-act`
(run it with `--dry-run` first; the dry run must name ONLY `thesis_driver` as moving).

**Begin only when all four hold:** ab-1, ab-2, ab-4 and ab-5 are `complete` and merged (the issuer's GO names the build commit, a PIN);
both halves are committed -- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/NEVER_WIDEN_HALF_COO_AB6.md` and
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND52_AB6_CTO_HALF.md`; and **the base CodeSha256 the halves name
(`zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`) is still the live one, re-read immediately before the build -- a moved base is a STOP
and a re-sign.** **The acts, in order, under the entry opened AND COMMITTED before the build** (sentinel + entry): (1) the pre-apply
captures the halves name; (2) build from a checkout AT THE PIN (never HEAD) + upload the ONE artifact (record the prior VersionId); the
build prints `CONTENT-DIFF` lines and a `CONTENT-DIFF SUMMARY` -- save them and STOP on any CHANGED/ADDED/REMOVED file outside the halves'
list; then ONE `safe-apply` -- print the plan first; code only; (3) the D-1 splice for ASML (record the object's prior VersionId; the
rollback is a copy of it); (4) verify with the four criteria; close the entry. A criterion failing after the act is the ROLLBACK trigger
named in the halves.

## 2. BOUNDS

1. The act and nothing else. A plan beyond the function's code, a packaged file beyond the halves' list, a D-1 write to any key but
   ASML's, or a gate refusal is a REFUSAL.
2. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

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
  <criterion id="AC1" cell_refs="AMGT-ab-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_2_dossier.py --plane served --what absent; echo "exit=$?"</invocation><expect>plane served: A NAME WITH NO DOSSIER SERVES EVERY FIELD ABSENT WITH ITS REASON: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ab-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_2_dossier.py --plane served --what shape; echo "exit=$?"</invocation><expect>plane served: PACK_SHAPE PASSES THROUGH FROM THE DOSSIER: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ab-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round51/checks/zz_8_served.py --what chart; echo "exit=$?"</invocation><expect>ASML chart SERVED source 'filing' points 3; THE SERVED DRIVER CHART READS THE FILING'S VERIFIED POINTS: YES -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-ab-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round52/checks/ab_6_code.py; echo "exit=$?"</invocation><expect>deployed CodeSha256 differs from zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ= and LastUpdateStatus Successful; THE ONE BUILD LANDED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

A fourth criterion, reason: the one act carries a build and an object write, and each served move keeps its own served read; AC4 is the
landing itself.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ab-6.the-one-build.proof_of_spec.json`. Report once: the content-diff summary, the prior and new VersionIds and CodeSha, the D-1 splice's prior VersionId and receipt, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-51 analysis items 1 and 6, combined into ONE act under ONE pair (one entry, one executor); every criterion reads the
SERVED route (ruling 5). Base: AC1 FAIL (6501 READ_FAILED), AC2 FAIL (no pack_shape), AC3 FAIL (ASML ABSENT), AC4 FAIL (zHpr7FhS). The
COO half is written after ab-1/2/4/5 land, against the landed code, the build-only content diff at the pin, and the then-live base.

<status>pending</status>
<round>52</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
