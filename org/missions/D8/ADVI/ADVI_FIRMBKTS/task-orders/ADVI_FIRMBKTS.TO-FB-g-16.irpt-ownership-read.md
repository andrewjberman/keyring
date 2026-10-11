# ADVI_FIRMBKTS task order -- `FB-g-16` -- THE IRPT OWNERSHIP-MAP READ FOLLOWS THE ROUTED BUCKET: THE DORMANT BUILD (THE CTO'S ADDENDUM 7, ROW D1-S25)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-16</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~39</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the builder, one generated block and one Python module; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_irptown.py` reads 0 of 5 (the loaders import cleanly with OWNERSHIP_READ absent; W2 to W5 are gated on W1 and FAIL as expected); the harness was sanity-run against the base loaders (the stub captures `(bucket, key)` of the ownership read and the directory pointer read). Blindness: the check stubs the S3 read; it cannot see a Lambda's packaging of the generated block.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-16` (round 4, workstream `IRPTOWN`; the CTO's round-3 ADDENDUM 7, msg 3900)

`infra/aws/lambda/investor-reporting/_authz/loaders.py` (shared by 8 investor-reporting Lambdas) reads each firm's ownership map in `load_ownership`: bucket
`bucket_for(tenant)` (the generated `IRPT_DIRECTORY_BUCKET_MAP`, now the transitional IRPT live row, `opal-data-bd`) and key
`OWNERSHIP_KEY_TEMPLATE.format(firm=tenant)`. The ownership map is the PRODUCERS' served key: from act 2 it is written only
at the canonical key of the firm's own bucket, so IRPT's read must follow the routed bucket and the canonical key. The
CTO ruled (c): the ownership map comes from a generated pair (routed bucket; legacy key now, canonical at act 4), the
directory and holdings reads stay on the live row. You build it DORMANT: today every read is byte-identical.

### 1a. Behavior (the whole spec)

1. **The block.** In `lib/opal_naming.py` add a renderer `_blk_ownership_read(reg, h16, path)` for the target `infra/aws/lambda/investor-reporting/_authz/loaders.py`
   (register it where `_blk_bucket_for` is registered and add the registry files it reads to that target's
   `TARGET_REGISTRY_KEYS` row; its mark changes and nothing else does). It renders, in the file's own `# GENERATED ...`
   style, one Python literal `OWNERSHIP_READ = {...}` mapping each firm that OWNS A REGISTERED legacy ownership-map address
   (the same set `lib/opal_naming.py`'s `_blk_ownership_keys` uses: `legacy_addresses.json` rows keyed `...-ownership-map`, owner = the
   destination class that starts the template) to `{"bucket": <the scope's routed bucket>, "legacy": <the row's template>,
   "canonical": <the seam's destination key for it>}`. Reuse that function's derivation (do not copy-and-type it); no
   key, bucket or firm literal is typed in the builder. A tenant with no registered owner has no entry.
2. **The read.** In `infra/aws/lambda/investor-reporting/_authz/loaders.py` (hand-kept code outside the generated block): `CANONICAL_PLATINUM_BUCKETS` is a second GENERATED
   module constant in the same file (see Amendment 1; no environment variable). `load_ownership(tenant)`:
   when `tenant` is in `OWNERSHIP_READ`, read bucket = the entry's `bucket` and key = its `canonical` if that bucket is in
   `CANONICAL_PLATINUM_BUCKETS`, else its `legacy`; otherwise exactly as today (`bucket_for(tenant)` and
   `OWNERSHIP_KEY_TEMPLATE.format(firm=tenant)`). The directory, holdings and policy loaders are NOT changed. The "absent
   map is an empty map" and "present but unreadable raises" behavior is unchanged; no authorization artifact is cached.
3. **Regenerate** `infra/aws/lambda/investor-reporting/_authz/loaders.py`'s generated blocks with the builder (`python lib/opal_naming.py generate --out /c/dev/wk-firmbkts-39 --target
   infra/aws/lambda/investor-reporting/_authz/loaders.py`); never by hand.
4. **A test** `infra/aws/lambda/investor-reporting/_authz/tests/test_ownership_read.py` in the folder's own style: (i) a registered owner reads (routed bucket, legacy key) with the
   variable unset, while its directory read uses the directory map's bucket; (ii) setting the module's `CANONICAL_PLATINUM_BUCKETS` to the routed bucket
   reads the canonical key; (iii) setting it to another bucket reads the legacy key; (iv) an unregistered tenant reads
   `bucket_for` and the template key. A test that cannot fail is not a control: state in your report the one-line
   mutation of `load_ownership` that makes (ii) fail and the one that makes (i) fail.

## 2. BOUNDS

1. Files that change: `lib/opal_naming.py`, `infra/aws/lambda/investor-reporting/_authz/loaders.py` and the new test. No deploy, no Terraform, no AWS call, no other Lambda file.
2. No behavior change for any tenant today: with the variable unset every read equals base's.
3. The naming gate is in ENFORCE mode: type no firm, bucket or key literal in any file you write except the test's
   abstract strings; if a commit is refused, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
lib/opal_naming.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
infra/aws/lambda/investor-reporting/_authz/tests/test_ownership_read.py
infra/aws/lambda-edge/_shared/firm-config.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~39/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~39/ADVI_FIRMBKTS.TO-FB-g-16.irpt-ownership-read.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-16"><invocation>cd /c/dev/wk-firmbkts-39 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_irptown.py --arms read --root /c/dev/wk-firmbkts-39; echo "exit=$?"</invocation><expect>ROUND 4 IRPT OWNERSHIP READ: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-16"><invocation>cd /c/dev/wk-firmbkts-39/infra/aws/lambda/investor-reporting &amp;&amp; timeout 115 env -u FORCE_COLOR python -m pytest _authz/tests/test_ownership_read.py -q 2&gt;&amp;1 | tail -n 3</invocation><expect>passed</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-16"><invocation>cd /c/dev/wk-firmbkts-39 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-39 --allow lib/opal_naming.py --allow infra/aws/lambda/investor-reporting/_authz/loaders.py --allow infra/aws/lambda/investor-reporting/_authz/tests/test_ownership_read.py --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~39/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require lib/opal_naming.py --require infra/aws/lambda/investor-reporting/_authz/loaders.py; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the generated block, the dormant read (ownership on the routed bucket, directory on the map's bucket), the
engaged read, an unregistered tenant, and that the file is the builder's output with no other generated target changed.
AC2 is your test. AC3 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-16.irpt-ownership-read.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~39`.
Commit the three files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W39-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3
outputs, the two mutations and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 7 (msg 3900): "one dormant IRPT cell before act 2 ... so the validator
and IRPT read one authorization location at every moment"; re-carving the class is refused; act 4's pair names this cell
(its deploy is act 4's, in the same act that flips the routed value). The IRPT Lambdas are not protected
functions; their deploy path is the act's.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-11 ~14:5xZ):** the engagement is the registry's value alone, never an environment
variable or a typed bucket (the CTO's ADDENDA 4 and 7; the naming gate): the builder renders `CANONICAL_PLATINUM_BUCKETS`
(the sorted unique canonical destination buckets of the platinum destination classes: today `opal-data-49financial`) as a
generated constant into `loaders.py` AND as `export const CANONICAL_PLATINUM_BUCKETS` into `_shared/firm-config.mjs` (a
later cell makes the router and the validator import it; this cell edits neither). While the routed bucket is a legacy alias
it is not in the list, so every read is today's (the dormant proof); the act-4 flip puts the routed bucket in it. Check
`r4_irptown.py` W1 and W3 read this. Gate limb: GATE viii reads `<placeholders>NONE</placeholders>` at HEAD and no token.

**AMENDMENT 2 (2.0.0_SA_COO~B1, after the worker's rows D1-W39-S1 and S2):** `infra/aws/lambda-edge/_shared/firm-config.mjs` is
added to `<paths>` (the generated `CANONICAL_PLATINUM_BUCKETS` JS block lands there; regenerate it with the builder, add no
hand edit). Row S2 (AC3 read the issuer's amendment commits on the branch as outside) is a check artifact: AC3 is graded from
the merge diff at the drain. Gate limb: GATE viii reads `<placeholders>NONE</placeholders>` at HEAD and no token.

<status>pending</status>
<round>4</round>
<workstream>IRPTOWN</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-16</to_id>
<slot>~39</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
