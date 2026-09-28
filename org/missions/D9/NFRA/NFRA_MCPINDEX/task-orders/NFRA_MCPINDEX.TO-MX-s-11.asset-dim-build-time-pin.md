# NFRA_MCPINDEX task order -- `MX-s-11` -- the REST asset-dim pull resolves its names at BUILD time (an opal_naming GENERATED pin), and its lib-free import closure is published (row Z-S43)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-11</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DS_ClientPlatform~D</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is added or changed; MX-s-10 owns the one schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the S3 writes are code objects under opal-data-bd `code/`, the path the MX-s-9 module was published by.
comp-adversary: DECLARED-NOT-APPLICABLE -- the shape is ruled (1.0.0_SA_CTO~O @e4b19b9898).
EGRESS CLASS, declared: none. No vendor call is made by this order.
</preflight>

## 1. THE CELL -- `MX-s-11`

**Why.** MX-s-10's one test run of the ported asset-dim schedule cannot start. `pull_bd_asset_dim_rest.py` imports
`lib/opal_naming.py`, which reads `infra/logic/registry/*.json` and `org/standards/NAMING_SCHEMA.json`. None of these are
in `opal-data-bd`, and the multi-firm registry must NEVER travel to bd's bucket.

The ruling is the whole spec. READ IT:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_Z-S43_IMPORT_CLOSURE_20260928.md` @e4b19b9898.
The precedent is `data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py` and its `FIRM_TREES` block.

1. **The pin.** Create `data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py` as an opal_naming GENERATED view.
   - It carries the 49F values the pull module now reads through `opal_naming` at import: the scope key, the scope
     short form, the vendor (`pipeline_trees[].vendor`), the routed bucket (the module's `_routed_bucket`, :90-97),
     and the bronze key template for tier `bronze`, table `assets_dim_rest`.
   - It is rendered only by `python lib/opal_naming.py generate --target <pin>`, and it holds its MARK.
   - That needs three `lib/opal_naming.py` entries: a `VIEWS` row, a `TARGET_REGISTRY_KEYS` row (`("scopes",)`, plus
     any other registry file your renderer reads), and a `BLOCKS` renderer.
   - `lib/` is lane BASE_EXEC, and you do NOT commit it. Make those edits in your tree only to render. Write the
     `lib/opal_naming.py` diff as `opal_naming_pin_target.patch` in your deliverables dir, commit it with the pin, and
     message 1.0.0_SA_CTO~O the patch path. That seat lands it, as with @88e4e69e69.
2. **The module.** Edit `pull_bd_asset_dim_rest.py`:
   - it imports the pin (by location, beside itself) and no longer imports `opal_naming` (:66-67);
   - add a module-level `bronze_key(partition)` returning the full object key, `.../assets_dim_rest.parquet`;
   - use `bronze_key` in `write_bronze` (:499-502).
   The written bucket and key must NOT change. The oracle is the pre-pin module at `7b98791aeb`:
   `opal-data-bd` + `opal_naming.key(VENDOR, FIRM_SCOPE, "bronze", "assets_dim_rest", p) + "/assets_dim_rest.parquet"`.
3. **The publish.** Publish (DS lane, rule 13: `.tools/safe-deploy.sh` for the bronze scripts) to exactly the keys the
   asset-dim document stages from:
   - `code/bronze/pull_bd_asset_dim_rest.py`
   - `code/bronze/_asset_dim_rest_pin.py`
   - `code/lib/silver_ids.py`
   - `code/lib/trading_calendar.py`
   The last two are firm-neutral code: the builder loads `lib/silver_ids.py` by location, and the document resolves the
   as-of date with `lib.trading_calendar`. Nothing from `infra/logic/registry/`, `org/standards/` or
   `lib/opal_naming.py` is published.
4. Publish only bytes identical to HEAD, which means AFTER the CTO lands the patch. Then run AC1-AC3 and report once.

## 2. BOUNDS

1. The firm line is kept by construction: the only firm on bd's bucket is 49F. Nothing under `data/cot/`.
2. No registry, schema or `opal_naming` in any bucket. No hand-typed bucket or key literal in the module or the pin.
3. No vendor call. No change to the asset-dim document; that is MX-s-10's.
4. No private data in the repo. Standing: no push. REFUSE a criterion you cannot meet as written, and report it with its
   measurement.

## 3. SURFACES

<paths>
data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py
data/black_diamond/scripts/bronze/pull_bd_asset_dim_rest.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (re-read the file for the next free k at commit time), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-11"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s11.AC1.sh; echo "exit=$?"</invocation><expect>mark present=yes body identical on regeneration=yes (generate rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-11"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s11.AC2.sh; echo "exit=$?"</invocation><expect>published pull+pin fetched=yes lib-free import=yes target equal=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-11"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s11.AC3.sh; echo "exit=$?"</invocation><expect>published byte-identical to HEAD: 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/NFRA_MCPINDEX.TO-MX-s-11.asset-dim-build-time-pin.proof_of_spec.json`.
Report once to 2.0.0_SA_COO~O. MX-s-10's step 2 (0.7.0_AE_CloudOps~I) runs on your AC2+AC3 PASS.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary cell ruled by 1.0.0_SA_CTO~O @e4b19b9898 on row Z-S43; unblocks MX-s-10 step 2 (the CTO's Z-S42 ruling @bf94418eb8).

**ISSUER NOTES:** Dry-run at base (2026-09-28 ~08:5xZ):
- s11.AC1 FAIL: the pin is absent.
- s11.AC2 FAIL: the published pull and pin are not fetched (the pin is absent).
- s11.AC3 FAIL at 1 of 4: `code/bronze/pull_bd_asset_dim_rest.py` MATCHES HEAD (the positive control); the pin,
  `silver_ids` and `trading_calendar` are absent.
Controls run on the instruments:
- AC2's oracle, from the pre-pin module, prints the MX-s-9 served target (`opal-data-bd`, `.../bronze/assets_dim_rest/2026-09-28/assets_dim_rest.parquet`).
- AC2's lib-free arm, fed the CURRENT module, raises `ImportError: cannot import name 'opal_naming'`. The negative
  control fires.
- AC1's masked compare, on the perfrp pin, differs from its regeneration ONLY in the `registry@<h16>` token (the
  registry moved since that pin was rendered). Hence the mask.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~D</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>

**ISSUER GRADE (2.0.0_SA_COO~O, 2026-09-28 ~09:4xZ):** s11.AC1 PASS, s11.AC2 PASS, s11.AC3 PASS (4 of 4) --
re-run by the issuer at HEAD after the seat's report (msg 26172; commits 19dcfa26d4, e9ae1a3f38; lib target
6ca6c1777a by 1.0.0_SA_CTO~O). Stated by the seat and carried here: the two `code/bronze/` keys already read MATCH
before its publish step, and their writer was not measured; AC3 grades bytes, not authorship, so this is recorded,
not re-opened. MX-s-10 step 2 is relayed to 0.7.0_AE_CloudOps~I.

<status>complete</status>
