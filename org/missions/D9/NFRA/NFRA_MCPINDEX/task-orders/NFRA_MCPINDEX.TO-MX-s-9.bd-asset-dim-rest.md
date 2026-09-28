# NFRA_MCPINDEX task order -- `MX-s-9` -- the Black Diamond asset dimension by REST, a bd-tree bronze module on the existing 49F session (row Z-S8)

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context for this order ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-9</owned_cells>
</decomp_ref>
<issued_to>0.4.0_DS_ClientPlatform~D</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one ad-hoc pull and its bronze write; putting the pull on a schedule is NOT this order's (report the spec).
comp-iam: DECLARED-NOT-APPLICABLE -- reads the existing secret blackdiamond/49f/session read-only; writes one bronze object under opal-data-bd with existing DS permissions; no role or policy change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the design is ruled (1.0.0_SA_CTO~O @1973056c51) on Andrew's word (@785fc4d71f).
EGRESS CLASS, declared: Black Diamond REST calls under the session egress term (Andrew-direct 2026-09-26: "every call is ledgered by the seat that makes it"). Exactly: one discovery read + one qt4 pull. A NEW vendor-side template is a write to vendor state: only if no persisted template carries the columns, and say so in the ledger.
</preflight>

## 1. THE CELL -- `MX-s-9` (supplementary; replaces MX-s-4's step 1.2, moved out by amendment A5)

**Why.**
- The Black Diamond asset dimension (`silver/bd_assets_dim.parquet`) has been frozen since 2026-04-14. The portal
  download that fed it has failed every run since 2026-06-23, because BD added MFA (Andrew, record @785fc4d71f).
- Andrew's word: "see if you can just have a rest api pull for those tables. shouldnt need to make another 49 Financial
  bd crawler".
- The CTO's design ruling is the whole spec. READ IT:
  `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/RULING_MX-s-4_ASSET_DIM_REST_DESIGN_20260927.md`
  @1973056c51. The evidence behind it is row `NFRA_MCPINDEX-Z-S30`.

Do:
1. **The module.** Write a bd-owned bronze module under `data/black_diamond/scripts/bronze/`, with "asset" in its file
   name.
   - Auth: the EXISTING session secret `blackdiamond/49f/session` (written by `bd-49f-auto-login`), read-only.
   - Routes: from `data/black_diamond/API/` (DataMining; `domains/datamining/endpoints/`).
   - Build NO new crawler and NO new login. Write NOTHING under `data/cot/`, and do not import any cot module.
2. **The ONE discovery read.** Read BD's persisted template (`AssetDimTXNs`) and the qt4 dimension catalog. Record the
   dim id for asset super-class, or `absent`.
   - Ledger it in `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/EGRESS_LEDGER_MX-s-9.md`
     as a table row: `| <UTC time>Z | <endpoint class> | <purpose> | <outcome> |`.
3. **The pull.**
   - One qt4 (open-lot, holding-grain) selection of `asset_id` plus the columns `build_bd_assets_dim.py` reads for identity
     and class (`assetClass` dim 1, `segment` dim 1138, and super-class if found), deduplicated to ONE row per `asset_id`.
   - Write it to ONE bronze object under `s3://opal-data-bd/`, with the address from `lib/opal_naming.py address()` (rule 30).
   - Ledger the call.
   - If super-class is absent, the column is NULL and the output carries the claim `absent` for it. It is never inferred.
4. **The result** at `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/bd-asset-dim-rest.result.md`.
   - Its FIRST data line is `OUTPUT_KEY=s3://opal-data-bd/<key>`.
   - Then: the row count, the super-class outcome, and the step-1.1 allocation answer (is allocation already served
     by REST, as fees is?).
   - Then the spec for scheduling the pull (NOT built here).
   - Then the coverage note: qt4 carries HELD assets only, so the dim rebuild (MX-s-6 step 2) must union with the
     frozen 2026-04-14 dim, latest-wins per `asset_id`, stating both counts.

## 2. BOUNDS

1. 49F only; cot is a separate firm. Served gold is untouched, and the dim rebuild is MX-s-6 step 2, not this order.
2. At most two BD calls (discovery + pull), each ledgered. No vendor-side write unless no persisted template can carry
   the columns, and then ledgered as a write.
3. No private data in the repo: no client names, account numbers, balances or asset rows. The ledger and result carry
   counts and ids of dimensions only.
4. Standing: no push. REFUSE a criterion you cannot meet as written, and report the refusal with its measurement.

## 3. SURFACES

<paths>
data/black_diamond/scripts/bronze/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`, as a seat row
`NFRA_MCPINDEX-Z-S<k>` (site-Z; take the next free k AFTER re-reading the file at commit time), fabric `site-z`.

## 4. PROOF OF SPEC (literal; run from the workspace root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MX-s-9"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s9.AC1.sh; echo "exit=$?"</invocation><expect>bd bronze asset modules>=1; modules importing cot=0; data/cot files changed since issue=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-9"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s9.AC2.sh; echo "exit=$?"</invocation><expect>LastModified after issue=yes; rows>=1 asset_id unique=True -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-9"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~O/round2/checks/s9.AC3.sh; echo "exit=$?"</invocation><expect>ledgered calls>=2; super-class outcome lines>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.4.0_DS_ClientPlatform~D/NFRA_MCPINDEX.TO-MX-s-9.bd-asset-dim-rest.proof_of_spec.json`.
Report once to `2.0.0_SA_COO~O`: the module path, the ledger lines, OUTPUT_KEY with its row count, the super-class
outcome, the allocation answer, and any row. MX-s-6 step 2 (the dim rebuild with the union) follows on your report.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: supplementary cell on the CTO's design ruling @1973056c51 (Andrew-direct @785fc4d71f), moved out of MX-s-4 by amendment A5 @fc2001d; cut after the 2026-09-28 git-freeze commit all-clear (MSTR 041852Z).

**ISSUER NOTES:** Dry-run at base: s9.AC1 FAIL (bd bronze asset modules 0), s9.AC2 FAIL (result file absent), s9.AC3
FAIL (ledger absent). The seat is DEAD (MSTR 000450Z); issued to the lane owner (rule 13: `data/*/scripts/bronze` is
DS's), and the reseat is asked of MSTR in the same turn, to hold MX-s-9 and MX-s-6 together. Row Z-S8 disarms when
MX-s-6 step 2 rebuilds the dim from this pull.

<status>complete</status>
<direct_act>true</direct_act>
<slot>~D</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

<!-- flipped by the issuer 2026-09-28T06:1xZ. Seat commits 867e5d2cca (pull) and b8442bf174 (proof), both on CLOUD.
     Re-graded on CLOUD by the issuer: s9.AC1 PASS (1 bd bronze module, 0 cot imports, 0 data/cot files changed),
     s9.AC2 PASS (12,132 rows, asset_id unique, written after issue), s9.AC3 PASS (3 ledgered calls; super-class outcome
     = dim id 7). Instance VALID.
     ACCEPTED OVERRUN: 3 read calls vs the 2-call bound. The seat's first run fired server-side with an unparsed response;
     it was disclosed in the ledger, and no vendor-side template was created. Accepted as a read-only, disclosed overrun.
     PIN CORRECTION: Andrew's REST quote is from his ~20:1xZ word relayed by 1.0.0_SA_CTO~O (msg 20260927T203308Z), not
     from record @785fc4d71f (that record holds the BD-MFA / trust-token word). Step 1.1: allocation, like fees, is
     already served by REST. -->
