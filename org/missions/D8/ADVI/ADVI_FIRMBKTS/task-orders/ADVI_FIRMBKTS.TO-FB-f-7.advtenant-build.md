# ADVI_FIRMBKTS task order -- `FB-f-7` -- THE advTenant REMEDY: THE RULE-24 RECORD AND THE DORMANT BUILD (router, guard, generated config)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R3.md</decomp_doc>
<owned_cells>FB-f-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~17</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change and no AWS act: the cell edits repository files and runs local tests.
comp-adversary: RUN by the issuer -- router run-gate.sh reads 39 pass (the cell's arms expect 42 or more) and the guard's `bun test` reads 35 pass after `bun install --frozen-lockfile` (the arms expect 36 or more) at base; r2_f6.mjs diff reads 193 of 193 identical at base (the difference control: PASS by construction); r3_advt_record.py 0 of 3 at base, 3 of 3 on a fixture. Blindness: the lens cannot see a request shape the corpus of 193 events does not carry; the controls below name the shapes the remedy exists for.
EGRESS CLASS, declared: NONE (`bun install` fetches the guard's pinned dependencies; no other request leaves the machine).
</preflight>

## 1. THE CELL -- `FB-f-7` (round 3, enrichment item 1, step 1; PRD F6; LD-0442's carried row)

The edge router asserts the tenant of a `platinum/advi/{firm}/` request by comparing the BUCKET the path's firm resolves to
with the bucket the caller resolves to (`infra/aws/lambda-edge/shared-advisor-router/index.mjs` lines 410-436), and the
response guard re-derives the same comparison on its own (`shared-advisor-router-response/index.mjs` lines 89-122). A
bucket comparison separates tenants only while one bucket is one firm. At the cutover `49financial` resolves to its own
bucket while its declared alias `mockadv` stays on `opal-data-bd`: the buckets differ, so BOTH layers would refuse an
alias that works today by sharing a bucket. The remedy the header of `_shared/firm-config.mjs` names is
**tenant-grain entitlement**: compare the tenant DIRECTORY the path selects with the SET of tenant directories the caller
may read, with alias pairs DECLARED rather than inferred. You build it DORMANT: for today's registry every decision is
byte-identical to today's, and nothing is deployed.

### 1a. Behavior (the whole spec)

1. **The generated field.** `FIRM_CONFIG` gains, per firmId, `advTenant`: the frozen array of tenant directory names that
   firmId may read under `platinum/advi/{tenant}/`. It is generated, never typed: extend the registry generator
   `lib/opal_naming.py` (`_blk_firm_config`, line 871, using `_tenants(reg)`, which already yields each tenant with its
   scope and whether it is the scope's own tenant) so that the set of a tenant is EVERY tenant of its scope: the scope's own tenant and each
   alias tenant of that scope (so `49financial` and `mockadv` each list both directories, AMENDED twice, see ISSUER NOTES). One
   scope is one equivalence class: the PRD's tenant-assertion contract says the path's firm segment resolves "aliases
   included, to one firm", so the alias resolves to its firm on the path side as on the caller side. Regenerate `infra/aws/lambda-edge/_shared/
   firm-config.mjs` with the generator command its header prints; never hand-edit a generated block.
2. **The router.** For a request on the `platinum/advi/{tenant}/` path class: the caller's entitlement set is
   `FIRM_CONFIG[firmId].advTenant`; for `opal-capital` staff with `?firm=<slug>` it is the union of the `advTenant` sets
   of every firmId whose configured bucket equals `opal-data-<slug>` (the proxy keeps working exactly as today: it is
   today's boundary, no wider and no narrower). The request is served only when `{tenant}` is a member; otherwise the
   same 401 `Firm scope mismatch` the router returns today, with the same log rule name. The origin bucket is set exactly as at
   base (the canonical tier constant, after the assertion): this change moves the assertion only (AMENDED).
3. **The guard.** `shared-advisor-router-response` derives the same membership INDEPENDENTLY from the same generated
   `FIRM_CONFIG` (never by importing the router's decision) and trips its existing 502 only where the same request is
   outside the set.
4. **Dormant.** For the registry as it stands, every (firmId, tenant directory, path, query) decision of both functions
   equals the decision at base. `r2_f6.mjs diff` (the issuer's corpus, 193 events) must still read identical, and so
   must your own full grid (`evidence/dormancy_grid.mjs`, 88 router decisions and 396 guard cases at the cut): it builds
   its base copies itself with `git show 576e574de4:<path>` into `.scratch/base`, and its last line reads
   `DORMANCY: router differing 0, guard differing 0`.
5. **The controls the change exists for** (each is a test you write, in a NEW spec file per package; a test that cannot
   fail is not a control, so state in the record which mutation of the build makes each one fail):
   - SHARED BUCKET: a test double of `FIRM_CONFIG` in which two distinct non-alias firmIds share one bucket. The base
     comparison admits a cross-tenant request there; the new rule REFUSES it.
   - ALIAS: the declared alias is admitted on its own directory and on the tenant directory its declaration names, and the
     scope's own tenant is admitted on the alias's directory (one equivalence class), although their buckets differ in the
     cutover state (build that state as a test double: the registry carries no such difference today); both are refused on
     any directory outside the class.
   - STAFF PROXY: `opal-capital` with `?firm=<slug>` is admitted on exactly the tenants of that bucket and refused on
     another bucket's tenant.
   - NO FIRM LITERALS: your tests and code type no firm name and no key-shaped string; they read names from
     `FIRM_CONFIG` and the router's exports. The commit-time naming gate refuses a typed one (the same refusal that
     stopped `FB-e-6` once); run it first, section 1c.

### 1b. The record (the cell's second deliverable)

`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/ADVTENANT_RULE24_RECORD.md`: the four-postulate
record (CLAUDE.md section 4, TAXONOMY LAW) for the entitlement schema. Four headings, in this order, each a heading line
containing the label and each followed by more than 200 characters: `(i) MECE over a declared domain`, `(ii) SAME GRAIN`,
`(iii) INTENT COHERENCE`, `(iv) STATE COHERENCE`. The declared domain is the generated `FIRM_CONFIG`'s firmIds, printed
as a table with a denominator, each with its `advTenant` set and its bucket. Name the three standing cases and the set
each resolves to: the `mockadv` alias, the `opal-capital` staff proxy (`?firm=`), and a firm that shares a bucket with
another. Say, per postulate, which values one remedy does NOT move.

### 1c. The steps

0. Work in `/c/dev/wk-firmbkts-17`. Begin every shell call with `cd /c/dev/wk-firmbkts-17 &&`. Put
   `export PATH="$PATH:$HOME/.bun/bin"` first in any call that runs `bun`.
1. Baseline, before any edit: run the router's gate and the guard's suite (section 4's commands, minus the new arms) and
   keep the counts (39 pass, 35 pass expected).
2. Extend the generator, regenerate the config, then edit the router and the guard.
3. Write the two new spec files: `shared-advisor-router/test/tenant-grain.spec.mjs` and
   `shared-advisor-router-response/test/tenant-grain.spec.mjs`.
4. Before committing: `git diff HEAD > .scratch/f7.diff` then `python .tools/naming-gate.py --diff .scratch/f7.diff
   --enforce`; it must print `NAMING-GATE: PASS`. A REFUSE names the literal: replace it by a read from `FIRM_CONFIG`.
5. Mutation, for each control: break the build in one named way, run the new spec, see it FAIL, restore. Report each.
6. Write the record. Run AC1-AC4 (section 4).

## 2. BOUNDS

1. No deploy, no `terraform`, no `aws` call, no change to a Lambda, CloudFront or IAM object. Repository files only.
2. Behavior for today's registry is unchanged: if any existing test in either package changes its expectation, STOP: a
   BLOCKING row. You add tests; you do not edit an existing one.
3. A generated block is regenerated by the generator, never by hand. The generator's change is the minimum that emits
   `advTenant`; touch no other emitter in `lib/opal_naming.py`.
4. Only the files in section 3 change. No non-ASCII (the router has 5 pre-existing non-ASCII comment lines: leave them,
   a later cell owns them). LF line endings.

## 3. SURFACES

<paths>
lib/opal_naming.py
infra/aws/lambda-edge/_shared/firm-config.mjs
infra/aws/lambda-edge/shared-advisor-router/index.mjs
infra/aws/lambda-edge/shared-advisor-router/test/tenant-grain.spec.mjs
infra/aws/lambda-edge/shared-advisor-router-response/index.mjs
infra/aws/lambda-edge/shared-advisor-router-response/test/tenant-grain.spec.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of both packages and their tests, `infra/logic/registry/`, the issuer's checks under
`deliverables/2.0.0_SA_COO~B1/round2/checks/` and `round3/checks/`, `org/tier0/ledger/LD-0442.md`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/ADVI_FIRMBKTS.TO-FB-f-7.advtenant-build.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-7"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 110 bash infra/aws/lambda-edge/shared-advisor-router/run-gate.sh; echo "exit=$?"</invocation><expect>\b(4[2-9]|[5-9][0-9]) pass</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-7"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17/infra/aws/lambda-edge/shared-advisor-router-response &amp;&amp; timeout 115 bash -c 'bun install --frozen-lockfile >/dev/null 2>&amp;1; bun test test/ 2>&amp;1 | tail -6'; echo "exit=$?"</invocation><expect>\b(3[6-9]|[4-9][0-9]) pass</expect></criterion>
  <criterion id="AC3" cell_refs="FB-f-7"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 110 bun "org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round2/checks/r2_f6.mjs" diff; echo "exit=$?"</invocation><expect>F6 DIFF: identical 193 of 193 events through handleWithMap; 193 of 193 through handler</expect></criterion>
  <criterion id="AC5" cell_refs="FB-f-7"><invocation>export PATH="$PATH:$HOME/.bun/bin" &amp;&amp; cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 110 bun org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/evidence/dormancy_grid.mjs /c/dev/wk-firmbkts-17 2>&amp;1 | tail -3; echo "exit=$?"</invocation><expect>DORMANCY: router differing 0, guard differing 0</expect></criterion>
  <criterion id="AC4" cell_refs="FB-f-7"><invocation>cd /c/dev/wk-firmbkts-17 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round3/checks/r3_advt_record.py --record org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17/ADVTENANT_RULE24_RECORD.md --root /c/dev/wk-firmbkts-17; echo "exit=$?"</invocation><expect>ROUND 3 ADVTENANT RECORD: 3 of 3 arms</expect></criterion>
</proof_of_spec>

A fourth criterion is carried because the Rule-24 record is the CTO-ruled deliverable of this remedy and nothing else
reads it; a fifth (AC5) because the first build measured the dormancy claim over the full grid and found three decisions
changed (row D1-W17-S1), which the corpus of 193 events does not carry. AC1 and AC2 are the built behavior (the new arms add 3 or more to the router's 39 and 1 or more to the guard's
35, each package's own suite). AC3 is the difference control for the whole change: today's registry, same decisions.
Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-f-7.advtenant-build.proof_of_spec.json`, `D` =
`org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~17`. **Flip this order's `<status>` to `complete` in
the SAME commit as your proof instance and the deliverables**, only when AC1-AC4 pass. A row id on this project carries
the dell1 infix and your slot: `ADVI_FIRMBKTS-D1-W17-S<k>`, `surfaced_at` from `date -u +%FT%TZ`. Report once: the
baseline counts and the final counts, each control's mutation and its failing arm count, the naming-gate verdict line,
the output of AC1-AC4, the `advTenant` set per firmId as generated, and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the first report, rows D1-W17-S1..S4):** (1) D1-W17-S1: the cut's own spec
was wrong. An alias's set listed only the scope's tenant, so the alias's OWN directory fell outside it and 3 router and
9 guard cases narrowed (all on `platinum/advi/mockadv/`). Dormancy outranks the ALIAS wording: an alias lists itself and
the scope's tenant (today's boundary, no wider and no narrower). (2) D1-W17-S2: the origin-bucket sentence of 1a.2 is
replaced by what the base does. (3) D1-W17-S3: accepted; the ALIAS arms run on a cutover double. (4) D1-W17-S4: the
status flip is the issuer's. Gate limb: none grades an amendment to an order already complete-pending; `<placeholders>NONE`
at HEAD, so GATE viii graded it and the invocation added carries no token.

**AMENDMENT 2 (2.0.0_SA_COO~B1, after the second report, row D1-W17-S5):** the grid still read router differing 1 and
guard differing 3: `49financial` reading `platinum/advi/mockadv/` is admitted at base. The first amendment made the alias's
set directional. The PRD's CONTRACTS row ("tenant assertion") resolves the path's firm segment "through the registry,
aliases included, to one firm", so both directions are one boundary: a scope's own tenant and its alias tenants form ONE
equivalence class and every member lists every member. That is today's boundary exactly (no wider: no other firm's
directory; no narrower: no decision moves) and needs no CTO ruling; the shared bucket stops being the accident that
admits it and becomes a declaration. D1-W17-S5 closes on AC5 reading 0 and 0.

**ISSUER NOTES:** class WORLD by the infra floor (the paths are `infra/`), built dormant exactly like `FB-e-6`, which was
spawned the same turn it was cut. The deploy is `FB-f-8`, staged. The same log that records the 2026-08-21 deploy
(`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-21/session_1531-1712Z_p4r3_route_act.md`) records that the build of
this remedy was an open sovereign call at Andrew ("mockadv has ZERO users, measured; recommendation PARK"); the CTO's
round-2 analysis orders it built and names it step 1 of the window. The shared file `lib/opal_naming.py` is
LGIC_ENFORCE's; the edit is one emitter. A worker that finds the generator needs more than `_blk_firm_config` files a row.

<status>pending</status>
<round>3</round>
<to_id>ADVI_FIRMBKTS.TO-FB-f-7</to_id>
<slot>~17</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
