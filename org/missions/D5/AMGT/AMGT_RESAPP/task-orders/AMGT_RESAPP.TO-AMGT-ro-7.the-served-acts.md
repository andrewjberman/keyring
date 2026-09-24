# AMGT_RESAPP task order -- `AMGT-ro-7` -- THE SERVED ACTS: the lambda carries ro-1 and ro-3, and the peers pool carries the units

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ro-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant moves; the function's code moves through its existing Terraform resource.
comp-adversary: RUN by the issuer at the cut -- 3 of 3 acts carded in the COO half (3 served properties, 1 writer each, 3 rules read); BLIND to the CTO half (not yet written) and to the closure diff past 19a22f2f51, which the lane prints at build.
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving only `opal-amgt-scoped-api`'s code; (C) ONE peers batch writing ONE NEW partition per name under `peers/v1/` in Opal's harvest bucket (no overwrite); the build's own pinned `pip download` from PyPI inside `build-and-upload-scoped-amgt.sh`; reads of the deployed function. No vendor call, no S3 delete.
</preflight>

## 1. THE CELL -- `AMGT-ro-7` (round 40, decomposition s.48)

**Begin only when all three hold:** ro-1 and ro-3 are `complete` and merged on CLOUD (the issuer's message names the build
commit), AND both never-widen halves are committed:
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/NEVER_WIDEN_HALF_COO_RO7.md` and `1.0.0_SA_CTO~Z`'s. The
halves name what each act may touch and its rollback; act only inside them. **The acts, in order, under ONE NEVER-2 entry opened
before the build:** (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` first and print
the closure diff against the deployed build input `19a22f2f51` (`git diff --stat 19a22f2f51 <build commit> -- lib/research`);
a file outside the halves' list is a STOP and a report; (2) build and upload the ONE artifact (record the prior VersionId),
then ONE `safe-apply`; (3) the peers batch: `python lib/research/peers/engine.py --as-of <today> --write-as-of <today>T<HHMM>Z
--write-pool`, after a `--dry-run` census of the names it will write, printed; (4) verify with the three criteria; close the
entry. A criterion that fails after the apply is the ROLLBACK trigger for its act, named in the halves.

## 2. BOUNDS

1. The three acts and nothing else, under ONE NEVER-2 entry opened before the build and closed in the same session.
2. A plan that moves a second resource, a closure diff outside the halves, or a batch count different from the dry-run census
   is a REFUSAL: print it, stop, report.
3. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/**
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/tier2_senior/0.7.0_AE_CloudOps~A/deliverables/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ro-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-7.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from the prior y5bJBQsP8Q7Lfudb5nwc5wEr72IcH53uS5cz2T8bn/w= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ro-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-7.AC2.sh; echo "exit=$?"</invocation><expect>FWD-30 ON THE SERVED PLANE: served-plane export compare rc=0 (figures extra=0, page absences covered N of N, EXPORT-COMPARE OK) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ro-7"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round40/checks/ro-7.AC3.sh; echo "exit=$?"</invocation><expect>THE SERVED P/E: P/E x percent yield == 100 (+/-1): 24 of 24; off-relation 0; null 0 on the deployed peers response -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ro-7.the-served-acts.proof_of_spec.json`. Report once: what you changed and where, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Seat order; the issuer restamps `lib/research/api/_harvest_prefixes.py` immediately before naming the build commit if `gen_harvest_prefixes.py --check` reads rc 1. The lane is re-seated at its turn (not registered at the cut).

<status>pending</status>
<round>40</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
