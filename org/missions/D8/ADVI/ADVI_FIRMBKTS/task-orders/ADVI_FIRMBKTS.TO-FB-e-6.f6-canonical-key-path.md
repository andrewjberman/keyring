# ADVI_FIRMBKTS task order -- `FB-e-6` -- F6: THE ROUTER'S CANONICAL PLATINUM KEY PATH, BUILT DORMANT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R2.md</decomp_doc>
<owned_cells>FB-e-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~9</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the router's role and policies are untouched and the build is not deployed.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~B1) on dell1 -- the router's own gate reads 31 pass / 0 fail across 2 files at base; r2_f6.mjs diff and seam read NOT RUN at base (handleWithMap absent) and 193 of 193, 20 of 20 + 9 of 9 on the issuer's reference build; mutants: no registry gate 183 of 193 (fails), views class mis-pointed 18 of 20 (fails). The patch applies clean at HEAD and the gate reads 39 pass / 0 fail across 3 files with it. Blindness: the lens runs the handler on synthetic CloudFront events, not on a live distribution, and it cannot see the five behaviors' real traffic.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-e-6` (round 2, enrichment item 5; PRD F6)

`infra/aws/lambda-edge/shared-advisor-router/index.mjs` is the origin-request function on five CloudFront behaviors. It
resolves a firm's bucket from the registry's generated map (`FIRM_BUCKET_MAP`) and rewrites an advisor-intelligence request
to a LEGACY key (`/platinum/...`, `/gold/entities/...`, `/gold/views/...`, `/gold/artifacts/...`). Round 1's table places
the served keys of 49 Financial at `advi/49financial/platinum/...` in `opal-data-49financial`. This cell BUILDS the router's
ability to address those keys, DORMANT:
- with the registry's map as it is TODAY, every request resolves byte for byte as before (the difference control);
- only when the bucket a request resolves to is NAMED in the router's canonical-bucket list does the canonical path
  engage, through ONE table of served classes. The list ships EMPTY: nothing engages until a firm's cutover adds its
  bucket (and the registry's map names it), so no request changes today by construction;
- a served class the table does not place is refused with the router's own 404 (`unplaced_canonical_resource`).

**You do not design this; the issuer built and proved the edit.** It is the patch
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/F6_ROUTER_EDIT.patch` (one edit of `index.mjs`: the firm
map becomes a parameter of `handleWithMap(event, firmBucketMap)` and `handler` calls it with the registry's map; the
canonical table and its branch behind the empty list; plus one new spec file `test/canonical-platinum.spec.mjs` of
eight arms, which types no firm name and reads the registry's generated view instead). You apply it,
unchanged, and prove it three ways.

### 1a. The steps

1. Start from a clean router: `git checkout -- infra/aws/lambda-edge/shared-advisor-router/index.mjs` and delete
   `infra/aws/lambda-edge/shared-advisor-router/test/canonical-platinum.spec.mjs` if an earlier attempt left them. Then
   `git apply --check <the patch>` and `git apply <the patch>` from your worktree's repository root. If it does not apply,
   that is a BLOCKING row with the error text; never hand-edit to make it apply.
   The naming gate runs at the commit and grades `infra/` files: the patch passes it (`NAMING-GATE: PASS`, issuer's run on
   this exact patch), so a refusal there is a BLOCKING row with its text and never a reason to edit the patch.
2. Run the three invocations of section 4, in order. Change directory into your worktree with one command FIRST, then run
   each invocation EXACTLY as written in a later command, so the recorded invocation text equals the order's (the
   checker compares them). Each must read as its `<expect>` says (the pattern is matched against the output; also read the `exit=` line: it must be 0). A different reading is your
   final report; you do not change the patch or the checks to move a number.
3. Commit `index.mjs` and the new spec together with the proof instance and the status flip.

## 2. BOUNDS

1. The edit is the patch and nothing else. No change to `infra/aws/lambda-edge/_shared/firm-config.mjs` (a generated view,
   and its header forbids editing a bucket value without the `advTenant` remedy), to the response guard, to Terraform, to
   any registry file.
2. **NO DEPLOY OF ANY KIND.** Do not run `build-nodejs-lambda.sh`, `safe-apply`, `terraform`, `aws lambda`, `aws s3 cp`
   or any publish. This cell's output is a committed file change on your worktree branch; its deploy is not a cell of this
   round (decomposition v2, "Not in round 2").
3. The harness `r2_f6.mjs` writes one scratch file beside the router (`.r2_base_index.mjs`) and deletes it; if it is
   left behind, delete it before the commit and never commit it.
4. `bun` is the runner. If `bun` is not found, `export PATH="$PATH:$HOME/.bun/bin"` first.
5. No non-ASCII; LF line endings. If an item cannot be met within your paths, file a surprise row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~9/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the patch, the issuer's checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/`
(`r2_f6.mjs`; never edit it), `infra/aws/lambda-edge/_shared/firm-config.mjs`,
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/mapping.json` and `census.json`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~9/ADVI_FIRMBKTS.TO-FB-e-6.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-e-6"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 bash infra/aws/lambda-edge/shared-advisor-router/run-gate.sh; echo "exit=$?"</invocation><expect>\b39 pass</expect></criterion>
  <criterion id="AC2" cell_refs="FB-e-6"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 bun "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f6.mjs" diff; echo "exit=$?"</invocation><expect>F6 DIFF: identical 193 of 193 events through handleWithMap; 193 of 193 through handler</expect></criterion>
  <criterion id="AC3" cell_refs="FB-e-6"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 110 bun "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f6.mjs" seam; echo "exit=$?"</invocation><expect>F6 SEAM CONTROLS: 10 of 10</expect></criterion>
</proof_of_spec>

AC1 is the built behavior (the router's own deploy-chain gate, `31 pass` at base, with the eight new arms counted). AC2 is
the difference control: the new router's `handleWithMap` and its `handler` equal the pre-change router (git blob at
`fda1c4f0cc`) on a 193-event corpus covering every branch, every firm and the staff proxy. AC3 is the seam probe against
the real neighbour, the round-1 table: every router-reachable served class rewrites to the key the table gives it
(its first line, `F6 SEAM: 20 of 20 ...`, must read the same), and the ten controls hold, the first of which is that
the shipped EMPTY list changes nothing even under a map that names the firm's own bucket.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~9/ADVI_FIRMBKTS.TO-FB-e-6.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1-AC3 pass. A row id
on this project carries the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W9-S<k>`, with `surfaced_at` from
`date -u +%FT%TZ`. Report once: the apply result, the gate's pass/fail counts and file count, the DIFF and SEAM lines
verbatim (both SEAM lines), the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** class WORLD by the gate's infrastructure floor (`<paths>` names `infra/`), although nothing is
deployed. The edit is the issuer's, proved by the issuer before the cut (the harness also caught itself once: its first
"193 of 193" compared two THROWs; fixed and re-run). Why dormant: (a) the registry's map names `opal-data-bd` for
49financial and mockadv, so nothing changes today; (b) `firm-config.mjs` forbids a shared-bucket value change before the
`advTenant` remedy; (c) the producers still write `opal-data-bd` (row D1-S4). The seam probe uses the round-1 table, so
FB-e-1's repair does not move it; if the repair places more served classes, they enter the router's table by a later
cell. The CTO's exercised read at close is AC2 and AC3 run again.

# pipeline-override: the one refusal is LIMB PRD_HEADER.fabric='laptop' vs the register's 'dell1'. The register row is the authority since 1.0.0_SA_CTO's L3 re-placement @8afcb0f851; the PRD header repair is the CTO's. Every other limb passed in the issuer's dry run.
<status>complete</status>
<round>2</round>
<to_id>ADVI_FIRMBKTS.TO-FB-e-6</to_id>
<slot>~9</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
