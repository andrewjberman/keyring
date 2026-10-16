# AMGT_RESAPP task order -- `AMGT-ar-8` -- THE AI-FILL HOLD IS REMOVED FROM `opal-amgt-scoped-api` AND THE STORED DOCUMENTS ARE READ BACK AS SERVED (FWD-41, THE CTO'S LIFT RULING; A WORLD ACT) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_AIFILL_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ar-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~RA1</issued_to>
<issued_by>2.0.0_SA_COO~R2</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ar-8.the-ai-fill-hold-is-removed-and-the-stored-documents-are-served</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one configuration leg; no schedule is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant changes; the function's environment only.
comp-adversary: RUN at the cut -- `check_restore_served.py` reads `AIFILL RESTORE SERVED: NO (8 of 16)` at the base on the live function (the hold is in place, so the four names serve `ai_fill` ABSENT; the eight other arms pass), reads YES (16 of 16) on responses simulated from the stored documents, and NO (12 of 16) with one served block altered (the negative control); its `capture` mode wrote the four live bodies to a local file; you regenerate that file immediately before the apply.
EGRESS CLASS, declared: NONE beyond the function's own Lambda invokes (GET); no Bloomberg, no model call, no S3 write.
</preflight>

**Your worktree:** the shared checkout of the workspace on `box/dell1` (a deploy order, no worker worktree); the order file on that branch is the grant for your `<paths>`.

## 1. THE CELL -- `AMGT-ar-8` (round 109, workstream AIFILLHOLD, decomposition s.18)

The AI-fill blocks were held off the served API on 2026-10-14 by ONE environment entry on `opal-amgt-scoped-api` (`AMGT-ar-7`). The CVO's fresh five-new-name read is MET (`ADJUDICATION_v136`), and the CTO ruled the hold lifted through the pair `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND109_AIFILL_HOLD_RESTORE_{COO,CTO}_HALF.md` (both signed). Leg 1 of the pair is done and read back: the stored document of `SAN_FP_Equity` carries its `mgmt_recent` block as a NONE block. You do leg 2: remove the entry. The handler `_read_ai_fill_document` reads `AMGT_AIFILL_ROOT` at CALL time; with the entry gone it reads the stored documents again, and every name with a valid document serves `ai_fill` SERVED with its five blocks.

SEQUENCE, in this order and no other:
1. read the live function configuration and print it (`LastModified`, `CodeSha256`, `MemorySize`, `Timeout`, `Environment.Variables`, `RevisionId`); open the change-management entry. **At the cut (2026-10-16 ~09:1xZ) the function read: CodeSha256 `UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=`, memory 1769, timeout 29, LastModified 2026-10-14T13:01:34Z, RevisionId `17e28b81-fc4b-4f7b-82c7-36010aa9bb0b`, Environment `{HARVEST_METRICS_TABLE, HARVEST_ARTICLES_TABLE, AMGT_AIFILL_ROOT=/var/empty/aifill-hold}`. If the CodeSha256 you read differs, another seat has moved the function since the cut: STOP and report, do not apply.**
2. capture the four live `/thesis` bodies IMMEDIATELY before the apply: `AIFILL_SERVED_FUNCTION=opal-amgt-scoped-api PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round109_close/restore/check_restore_served.py capture --names ASML_NA_Equity,NESN_SW_Equity,OMAB_MM_Equity,SAN_FP_Equity --out .scratch_restore/thesis_pre.json` (keep it local and uncommitted);
3. in `infra/aws/terraform/harvest/scoped-amgt-api.tf`, in the `environment_variables` map of `module "scoped_amgt_api"`, REMOVE the entry `AMGT_AIFILL_ROOT = "/var/empty/aifill-hold"` together with the comment block above it that names `AMGT-ar-7` (the two HARVEST entries stay exactly as they are); run the `terraform plan` through `safe-apply`'s dry path targeted at `module.scoped_amgt_api`. THE PLAN MUST SHOW ONE IN-PLACE CHANGE, the environment, and nothing else; a plan that shows the code (artifact version or hash), the role, layers, memory or timeout moving is a STOP before the apply: report it, do not apply;
4. the apply: ONE targeted `safe-apply` of `module.scoped_amgt_api`; never a bare `terraform apply`, never `aws lambda update-function-code` or `update-function-configuration`;
5. the verification of the criteria below. **No other reader runs on the function during your capture and verification.**

The effect: for every name with a stored document the `/thesis` body keeps the key `ai_fill`, which now reads `SERVED` with the five stored blocks; every other key is unchanged; the Opal-internal page `/security-analysis` renders the blocks; `SAN_FP_Equity` `mgmt_recent` prints the page's fixed not-prepared sentence.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-S<k>`, `disarm_owner` `2.0.0_SA_COO~R2`.

## 2. BOUNDS

1. The act and nothing else: REMOVE ONE environment entry on `opal-amgt-scoped-api`. No role, route, schedule, layer, other function or other variable; no addition of any variable.
2. No S3 write or delete, no Bloomberg, SEC or model call. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The captures stay local and uncommitted (they carry served research content).
5. A change the plan or the pair does not name is a STOP and, inside the same hour, a rollback unless the CTO names KEEP on the evidence.

## 3. SURFACES

<paths>
infra/aws/terraform/harvest/scoped-amgt-api.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ar-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; AIFILL_SERVED_FUNCTION=opal-amgt-scoped-api PYTHONPATH="$(pwd)" timeout 900 python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round109_close/restore/check_restore_served.py" verify --pre ".scratch_restore/thesis_pre.json" --docs "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R2/round109_close/restore/docs"; echo "exit=$?"</invocation><expect>no `FAIL` arm line and the line `AIFILL RESTORE SERVED: YES (16 of 16)`; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ar-8"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round97_prep/checks/r97_sector_serve_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round95_prep/checks/r95_classification_census.py" --where deployed &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round94_prep/checks/r94_name_census.py" --where deployed; echo "exit=$?"</invocation><expect>the earlier serves are KEPT: R97 SECTOR SERVE CENSUS: YES, R95 CLASSIFICATION CENSUS: YES, R94 NAME CENSUS: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ar-8"><invocation>.tools/aws lambda get-function-configuration --function-name opal-amgt-scoped-api --region us-east-1 --query "{Env:Environment.Variables,Sha:CodeSha256,Mem:MemorySize,Timeout:Timeout}" --output json</invocation><expect>one JSON object: `Env` holds `HARVEST_METRICS_TABLE` and `HARVEST_ARTICLES_TABLE` unchanged and does NOT hold `AMGT_AIFILL_ROOT`; `Sha` equals `UIkRgr9gbz2RbsaOJq2uRe3aZPOgNE/YoCAG6j7HyO4=`; `Mem` 1769; `Timeout` 29</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

The instance is genre DEPLOY, with a NAMED rollback (re-add the one entry `AMGT_AIFILL_ROOT = "/var/empty/aifill-hold"`, ONE targeted `safe-apply`, `get-function-configuration` shows the variable present and `CodeSha256` equal to the pre value) as the discriminating control, at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/AMGT_RESAPP.TO-AMGT-ar-8.the-ai-fill-hold-is-removed-and-the-stored-documents-are-served.proof_of_spec.json`.
`proof-of-spec-check` must read VALID on the committed bytes. Close the change-management entry. Report once:
- the step-1 configuration print and the plan's lines (the resource addresses it changes);
- the change-management entry's slug and state;
- every criterion's output lines;
- the first request after the apply (request id, handler time, Init Duration) as information;
- any row.
Flip `<status>` to `complete` only if every criterion PASSES.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED until the seat is live and the GO goes out; both halves of the pair are signed (COO @247b2f6a4f, sha256 `d4281bce...0e05`; CTO half msg 6624) and leg 1 (the SAN FP re-store) read back at @c7c8c8b7be, so nothing stands before this leg. The GO is the broker message with this path. This is the undoing of `AMGT-ar-7` and takes the same shape reversed. ROLLBACK: re-add the entry, one targeted `safe-apply`. Round 110 (the generic described-source rule, the pack-restatement and pronoun rules, the SAN naming sentence) is NOT in this order.

<status>staged</status>
<round>109</round>
<workstream>AIFILLHOLD</workstream>
<slot>0.7.0_AE_CloudOps~RA1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<proof_genre>DEPLOY</proof_genre>
