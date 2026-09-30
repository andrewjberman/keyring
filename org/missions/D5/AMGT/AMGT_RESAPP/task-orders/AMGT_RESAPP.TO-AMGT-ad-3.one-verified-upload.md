# AMGT_RESAPP task order -- `AMGT-ad-3` -- ONE VERIFIED UPLOAD FOR EVERY HARVEST BUILD SCRIPT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ad-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~194</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- shell code only; the check uses a local stub for aws and makes no AWS call.
comp-adversary: RUN by the issuer at the cut -- AC1's harness reproduces the MSYS mangle without the guard (C:/Program Files/Git/...) and passes with chatter-axis's function as the helper; at the base the helper is absent.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AMGT-ad-3` (round 54, decomposition s.62)

Under Git Bash, an argument that starts with `/` is rewritten to a Windows path when it crosses into a native program. The artifact
upload passes `--metadata "content-sha256=$SHA_B64"`, and a base64 sha256 starts with `/` about 1 time in 64: the stored metadata then
reads `C:/Program Files/Git/...` with rc=0 and the right size, and `modules/yang-lambda` reads that metadata as `source_code_hash`.
`infra/aws/terraform/harvest/build-and-upload-chatter-axis.sh` (its `upload_verified` function, ~:36-55) already does it right:
`MSYS_NO_PATHCONV=1` on the cp segment, then a head-object read-back that exits non-zero unless the stored `content-sha256` AND
`ContentLength` match. `build-and-upload-scoped-amgt.sh` (~:742), `build-and-upload-print-deps-layer.sh` (~:79) and `build-and-upload.sh`
(~:29, on bare `aws`) pass the metadata bare and only print the read-back.

**Build:** move chatter-axis's `sha_b64`, `sha_hex` and `upload_verified` into ONE new file,
`infra/aws/terraform/harvest/upload_verified.sh`, that callers `source`; `upload_verified <zip>` reads `BUCKET`, `KEY` and `AWS` from the
caller, as today. All FOUR `build-and-upload*.sh` source it and upload through it; none keeps its own `--metadata` line.
`build-and-upload.sh` resolves `AWS` the way the others do (the `.tools/aws` shim), never bare `aws`. Each script's build steps, zip
contents, bucket and key are unchanged. You never run an upload.

## 2. BOUNDS

1. The five files above. No S3 write, no build run against AWS, no terraform. Standing: no install, no push, no promote, no deploy, no
   vendor call. REFUSE, do not rescue.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/upload_verified.sh
infra/aws/terraform/harvest/build-and-upload-chatter-axis.sh
infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh
infra/aws/terraform/harvest/build-and-upload-print-deps-layer.sh
infra/aws/terraform/harvest/build-and-upload.sh
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~194/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ad-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round54/checks/ad_3_readback.sh; echo "exit=$?"</invocation><expect>honest arm exit 0 with the leading-slash sha received intact; plant arm exit non-zero; each of the four scripts sources upload_verified.sh with 0 other --metadata lines; UPLOAD KEEPS A LEADING-SLASH SHA AND REFUSES A MANGLED READ-BACK: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ad-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; for f in infra/aws/terraform/harvest/upload_verified.sh infra/aws/terraform/harvest/build-and-upload*.sh; do bash -n "$f" &amp;&amp; echo "syntax OK $f" || echo "syntax BAD $f"; done; echo "exit=$?"</invocation><expect>syntax OK for all five files, no "syntax BAD" -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~194/AMGT_RESAPP.TO-AMGT-ad-3.one-verified-upload.proof_of_spec.json`. Report once: what you changed per script, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-53 analysis item 3 (Z-S319 / Z-S321; ruling 2 keeps the head-object limb on every build pair until this lands).
Base: AC1 FAIL (helper absent), AC2 FAIL (the helper file does not exist: 'syntax BAD'; the four scripts parse). Positive arm (ruling 1): AC1 PASS with
chatter-axis's function as the helper and simulated sourcing scripts; FAIL with the same helper minus MSYS_NO_PATHCONV (the native stub
received `C:/Program Files/Git/HmoIi0wOY...`); FAIL on the real scripts (0 sources, 1 bare --metadata each). `<risk>` is WORLD by the
L6 gate's floor for an infrastructure path (the act itself writes no AWS state; the next build that runs these scripts is under a pair).

<status>complete</status>
<round>54</round>
<slot>~194</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
