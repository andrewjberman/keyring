# ADVI_FIRMBKTS task order -- `FB-g-12` -- THE BUILDER RENDERS THE PER-FIRM OWNERSHIP-KEY BLOCK INTO `firm-config.mjs` (THE CTO'S ADDENDUM 4, AHEAD OF FB-g-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~33</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the builder and one generated file; no cron, rule, schedule or cadence is added or changed and nothing is deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_okeys.py` reads 1 of 5 (O5 in-sync and validate PASS as a control; O1 to O4 FAIL as expected: no block); `r4_flip.py` reads 4 of 4 at base (AC2 is a difference control: the block must not change the value-changing set). Blindness: the check reads the block through `bun`; it cannot see a consumer that parses the file's text.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-12` (round 4, workstream `OWNKEYS`; the CTO's round-3 ADDENDUM 4, msg 3853)

The validator `infra/aws/lambda-edge/auth-validator-edge/index.mjs` reads each firm's authorization map from S3 at the
key `platinum/<firmId>/ownership_map.json` and, once the producers' served platinum moves (the round-4 window), at the key the
producers' seam writes: `advi/49financial/platinum/49financial/ownership_map.json`. The naming gate (ENFORCE) refuses a
hand-typed key template in the validator (rows D1-W24-S3). The CTO ruled: the BUILDER renders a per-firm ownership-key block
into the generated view `infra/aws/lambda-edge/_shared/firm-config.mjs`, and the validator reads it from there (a later cell). You build the block; nothing is
deployed and every other byte of the file stays as it is.

### 1a. Behavior (the whole spec)

1. **The block.** In `lib/opal_naming.py` add a block renderer `_blk_ownership_keys(reg, h16, path)`, register it where
   `_blk_firm_config` is registered (the block dispatcher and the target's block list for `infra/aws/lambda-edge/_shared/firm-config.mjs`), and add the registry
   files it reads to that target's `TARGET_REGISTRY_KEYS` row (the file's mark then names them; a mark line changes and
   nothing else). It renders, after FIRM_CONFIG, one exported object in the file's own style:

   `export const OWNERSHIP_KEYS = Object.freeze({ "<tenant>": Object.freeze({ legacy: "<key>", canonical: "<key>" }), ... });`

   with one entry per firm that OWNS A REGISTERED legacy ownership-map address, and only those. The set is read, never
   typed: the rows of `legacy_addresses.json` whose `key` ends `-ownership-map` and whose `shape` is `object`; a row's
   firm is the `scope` of the destination class (`platinum_destinations.json`) whose `legacy_prefix` starts the row's
   `template`; a row no class owns is a `RegistryError` (a registry row to fix). Today that is one entry, 49financial.
   A firm with no registered address gets NO entry (the validator throws for it and fails closed, as it did on the 404 of
   a key no producer wrote). Each entry's `firmId` must be a tenant `FIRM_CONFIG` lists (`_tenants(reg)`), or
   `RegistryError`.
   - `legacy`: the row's `template`, exactly. No key template is built or typed in the builder (the naming gate refused
     a `platinum/%s/%s` format string at line ~1002: row D1-W33-S3).
   - `canonical`: the producers' seam's destination key for that legacy key, derived from the destination registry the
     builder already reads for `platinum_dest_view.py` (`_platinum_build`; read that function): the class whose legacy
     prefix starts the key, its key template with the tail filled.
2. **Dormant.** Every line of `infra/aws/lambda-edge/_shared/firm-config.mjs` at base stays, in order; the only additions are the block (with its own
   `GENERATED ... [OWNERSHIP_KEYS]` mark and `END GENERATED` lines) and the mark line's changed registry list. Regenerate with
   the builder (`python lib/opal_naming.py generate --out /c/dev/wk-firmbkts-33 --target infra/aws/lambda-edge/_shared/firm-config.mjs`), never by hand.
3. **No consumer change.** The router, guard and validator are not edited (the validator is `FB-g-1`, after this cell).

## 2. BOUNDS

1. Files that change: `lib/opal_naming.py` and `infra/aws/lambda-edge/_shared/firm-config.mjs`. No other file, no deploy, no AWS call.
2. The seam (`lib/platinum_dest.py` and the views), the registry files and `FIRM_CONFIG` are read-only; no firm or bucket
   literal is typed outside the registry-driven code (the naming gate is in ENFORCE mode; a firm token is permitted in
   the builder only inside a `key()`/`address()`/`name()`/`lookup()` call or a registry file).
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
lib/opal_naming.py
infra/aws/lambda-edge/_shared/firm-config.mjs
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~33/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~33/ADVI_FIRMBKTS.TO-FB-g-12.ownership-keys-block.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-12"><invocation>cd /c/dev/wk-firmbkts-33 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_okeys.py --arms block --root /c/dev/wk-firmbkts-33; echo "exit=$?"</invocation><expect>ROUND 4 OWNERSHIP KEYS: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-12"><invocation>cd /c/dev/wk-firmbkts-33 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flip.py --arms flip --root /c/dev/wk-firmbkts-33; echo "exit=$?"</invocation><expect>ROUND 4 FLIP FLIP: 4 of 4 arms</expect></criterion>
  <criterion id="AC3" cell_refs="FB-g-12"><invocation>cd /c/dev/wk-firmbkts-33 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-33 --allow lib/opal_naming.py --allow infra/aws/lambda-edge/_shared/firm-config.mjs --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~33/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require lib/opal_naming.py --require infra/aws/lambda-edge/_shared/firm-config.mjs; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the block through `bun` (one entry per firm, legacy shape, canonical equal to the seam's, the base's lines kept,
the file equal to the builder's output, validate clean). AC2 is a difference control: the flip rehearsal's value-changing
set must stay the four served-tier targets. AC3 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-12.ownership-keys-block.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~33`.
Commit the two files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W33-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3
outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 4 after FB-g-1 and FB-g-2 were refused by the naming gate (rows
D1-W24-S3, D1-W25-S1); workstream `OWNKEYS`; follows FB-g-11 (same builder file). FB-g-1 is re-seated on this cell's merge
and reads `OWNERSHIP_KEYS` from `_shared/firm-config.mjs`, which the validator already imports. The block is an addition: the
deployed router, guard and validator are unchanged until act 4 deploys every regenerated target.

**AMENDMENT 1 (2.0.0_SA_COO~B1, after the worker's report: rows D1-W33-S1 to S3):** the builder's own `platinum/%s/%s`
template was refused by the naming gate as a NEW out-of-pattern S3 key (S3), and no builder path yields a per-tenant
legacy key: the only registered address is 49financial's. Ruled by the issuer inside this decomposition and the CTO's
ADDENDUM 4: render only the firms that own a REGISTERED legacy ownership-map address, and take `legacy` from the row (a
registry fact, not a builder format). No registry row is added (a per-tenant row for a firm with no such object would be a
false statement). `r4_okeys.py` O1 to O3 read this rule (entries are exactly the registered owners). Row S1 (the block's
placement after FIRM_CONFIG in a hand-kept mjs: an `AFTER_BLOCK` anchor in `_render_view`) is accepted as built. Gate limb:
GATE viii read `<placeholders>NONE</placeholders>` at HEAD and no token in the invocations (unchanged).

<status>complete</status>
<round>4</round>
<workstream>OWNKEYS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-12</to_id>
<slot>~33</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
