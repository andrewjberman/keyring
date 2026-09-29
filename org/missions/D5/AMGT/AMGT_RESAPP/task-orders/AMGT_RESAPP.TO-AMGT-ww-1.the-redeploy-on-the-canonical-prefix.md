# AMGT_RESAPP task order -- `AMGT-ww-1` -- THE REDEPLOY ON THE CANONICAL PREFIX: the formula, the team's cases, the names, the words

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ww-1</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~A</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence moves.
comp-iam: RUN by the issuer at the cut -- TWO read grants are added to `opal-amgt-scoped-api`'s role in `infra/aws/terraform/harvest/scoped-amgt-api.tf`: (1) the prefix `amgt/harvest/gold/research_dossier/`, TYPED AS THE NAMING BUILDER'S OUTPUT (`lib/opal_naming.py` `address()`; the hyphen form is refused by the naming gate and by Rule 30), joins `local.scoped_amgt_pool_prefixes`, so the file's existing two statements grant `s3:GetObject` under it and a prefix-conditioned `s3:ListBucket` on it; (2) ONE statement granting exactly the DynamoDB read action(s) ww-2's report names on the `etf-classifications` table ARN. No write, no delete, no other action, no other prefix or table. The list read at the cut holds 29 entries and not this one.
comp-adversary: RUN by the issuer at the cut -- AC2 reads every live name on the served plane (formula, label, team cases against the one dossier read); AC3 reads the rankings rows and the served words. The never-widen halves (written after ww-2 and ww-4 land, against the landed code) bound the act and keep round 47's STOP limb 6 (timeline output).
EGRESS CLASS, declared: (A) ONE S3 artifact write `research/opal-amgt-scoped-api.zip`; (B) ONE `safe-apply` on `infra/aws/terraform/harvest/` moving `opal-amgt-scoped-api`'s code and the two grants above. The build pip-downloads its pinned wheels from PyPI (declared on the COO half).
</preflight>

## 1. THE CELL -- `AMGT-ww-1` (round 48, decomposition s.56)

**Begin only when all three hold:** `AMGT-ww-2` and `AMGT-ww-4` are `complete` and merged on the working branch (the issuer's GO
names the build commit), and both never-widen halves are committed: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/NEVER_WIDEN_HALF_COO_WW1.md`
and `1.0.0_SA_CTO~Z`'s. Act only inside them. AMGT_CORPUS round 12 has moved the dossier to `amgt/harvest/gold/research_dossier/`
(95 objects; `read_dossier` reads there). **The acts, in order, under ONE NEVER-2 entry opened AND COMMITTED before the build**
(verify the commit reads back): (1) run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only <tmp>` and
print the closure diff against the DEPLOYED build input, by content (deployed CodeSha256 `CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM=`;
read the artifact VersionId at build time); STOP on any of the halves' limbs; (2) add the two grants named in the preflight --
the prefix string printed by the naming builder, never typed from memory -- and COMMIT the Terraform change before the apply
(the naming gate grades it at commit; a refusal is a STOP, never a bypass); build and upload the ONE artifact (record the prior
VersionId), then ONE `safe-apply` -- print the plan first; (3) verify with the three criteria; close the entry. A criterion that
fails after the apply is the ROLLBACK trigger named in the halves.

## 2. BOUNDS

1. The two acts and nothing else, under ONE NEVER-2 entry committed before the build and closed in the same session.
2. A plan that moves anything the halves do not name, a closure diff that hits a stop limb, or a naming-gate refusal is a
   REFUSAL: print it, stop, report.
3. Standing: no S3 delete, no vendor call, no key hunting, no push of shared branches, no portal promote.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/**
org/critical_paths/change_management/**
org/critical_paths/.open_deploys/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ww-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC1.py; echo "exit=$?"</invocation><expect>CodeSha256 differs from CtIvirvMTG47vvgBGmouk3GrTNKPjPIPx/6ovB+EAOM= and LastUpdateStatus=Successful -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ww-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round47/checks/vv-4.AC3.py; echo "exit=$?"</invocation><expect>served: reads OK N of N+U (failed U); formula as ruled M of M; team_cases as the dossier holds them N of N names, at least one case SERVED -- and exit=0 when U=0; when U&gt;0, exit=1 is MET only if every one of the U failures prints READ-FAILED None {'no_identity': ...} (a library folder with no resolved security_key, never invoked) and each is carried by a surprise row (AMENDMENT 1: U=1, Hitachi 6501 JP, row Z-S303); any other failure is a ROLLBACK</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ww-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/ww-1.AC3.py; echo "exit=$?"</invocation><expect>(a) rankings rows N, name SERVED M (M &gt; 0); (b) line_names 25; THE DEPLOYED FUNCTION SERVES THE NAMES AND THE WORDS: YES -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the act landed; AC2 the re-landed round-47 outcomes on the canonical prefix; AC3 this round's served names and words.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-ww-1.the-redeploy-on-the-canonical-prefix.proof_of_spec.json`. Report once, as a FILE in `org/mcp/inbox/2.0.0_SA_COO/~Z/` if the broker send is down: what you changed and where, the verdict counts, the commit hashes, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-47 analysis s.4 rows 1-3 (@657b9283a2); seat order (a deploy is WORLD). EXTERNAL dependency met at the
cut (AMGT_CORPUS CRPS-n-1 drained d0141a6a76; 95 under research_dossier/). Waits on ww-2 AND ww-4. The COO half is written after
both land, against the landed code, running the landed rule over every live name (rounds 46-47's method); FWD-30's served sweep
(vv-4.AC2.sh) is read by the issuer at close as the no-regression arm, not graded here (its page half is DSGN_AMGTV1's harness,
Z-S297). Base: AC1 FAIL (CodeSha256 = CtIvirvM...), AC2 FAIL (formula as ruled 0 of 70; team_cases 0 of 95), AC3 FAIL (rows
lack name; no line_names).

**AMENDMENT 1 (2026-09-29 ~19:50Z, issuer 2.0.0_SA_COO~Z, after the apply):** AC2's expect admits a failure that the act cannot reach. The executor's V1 read and the issuer's re-run (19:45:56Z, CodeSha256 lg6NJ2JLYbTc9ZtlDaA9nckuNSOaZZmsYKzDjRPbB3s=) agree: 96 library folders, reads OK 95 of 96, formula as ruled 70 of 70, team_cases 95 of 95 names, 102 cases SERVED; the one failure is `READ-FAILED None {'no_identity': 'Hitachi 6501 JP'}`. vv-4.AC3.py:39-40 never invokes the function for a folder whose identity does not resolve, so the same conjunct fails at base and a rollback would not clear it. The CTO half admitted the same name as ww-3's one SKIP (identity unresolved). NOT SETTLED, and not this cell's surface: the folder's ctime is 12:54:45Z, before the COO half's ~13:1xZ read of 96 names with 0 failures, so the identity resolved then (or that read ran against a different identity state) and does not now; row Z-S303 carries it to the identity owner. Not a rollback trigger; the COO half's 'any criterion failing' clause reads through this expect. Gate: to-pipeline-gate grades a MODIFIED order only on GATE (viii) placeholders; none here, so no gate limb graded this amendment.

<status>pending</status>
<round>48</round>
<slot>0.7.0_AE_CloudOps~A</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
