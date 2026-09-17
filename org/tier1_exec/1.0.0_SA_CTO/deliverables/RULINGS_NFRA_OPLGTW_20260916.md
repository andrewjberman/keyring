# NFRA_OPLGTW -- rulings by 1.0.0_SA_CTO, 2026-09-16 (on 2.0.0_SA_COO~O 97496, /canonical-drive tick 1)

**Authority:** Andrew-direct at the `2.0.0_SA_COO~O` terminal this session ("/canonical-drive NFRA_OPLGTW. Figure out current state and get back in the flow on that project" and the Schwab-to-SharePoint fold-in, verbatim in R-OG-3), and the standing 30m /self-drive word at this terminal ("adjudicate any open calls that arise"). Every value below carries its instrument and vintage.

## R-OG-1 (~18:0xZ) -- OG-c-2 / row W4-S5: the held emitter change is NOT admitted into OG-c-2's apply; it is UN-STAGED from the opal-assets root in its own commit, because its producer no longer exists and its target tree is empty

**Call:** the opal-assets root's plan carries `0.7.0_AE_CloudOps`'s staged-and-held emitter change @2740e4de8f (2026-08-11, "X-ii-a AE half STAGED-NOT-APPLIED": `AGGREGATE_PREFIX` repointed to `portal/gold/mdpf/_staging/aggregate_aua/` plus two IAM pure-adds on the emitter role). With `-target` forbidden, OG-c-2 cannot apply the schwab function alone. COO~O's rec: admit it by name (as ruling 97237 admitted two WAF description backfills) once its owner confirms, or have the owner land or withdraw it.

**Measured before ruling (18:0xZ):**
- `lambda get-function-configuration opal-assets-daily-emitter`: live `AGGREGATE_PREFIX` = `gold/mdpf_revamp/_aggregate_aua/`, LastModified 2026-08-11T01:28Z -- the repoint was never applied.
- `s3api list-objects-v2 opal-data-assets --prefix portal/gold/mdpf/_staging/aggregate_aua/`: **KeyCount 0.** The old tree `gold/mdpf_revamp/_aggregate_aua/` has its newest object at 2026-09-16T13:31Z -- written today.
- `lambda get-function-configuration mdpf-daily-trigger` (the producer the same act repointed in the mdpf-pipeline root): **ResourceNotFoundException.** The producer was destroyed at @120a822241 (OPAL_MDPFCLEANUP TO-3 K3, "producer KILLED -- 10 destroys applied").
- `git log 2740e4de8f..HEAD -- infra/aws/terraform/opal-assets/emitter.tf`: **no commit** touched the file since, so the parent's bytes are the exact pre-change state.
- `0.7.0_AE_CloudOps`: NOT REGISTERED on the broker; its inbox has held unread mail since 2026-09-15.
- Lane on `infra/aws/terraform/opal-assets/**`: CLOUD_OPS_OR_ETL, "any AE agent" -- `1.0.0_SA_CTO` REFUSED, `2.0.0_SA_COO~O` REFUSED; no AE lane is live.

**Ruling.**
1. **Not (a).** Applying the repoint would point a served emitter (it wrote today) at a tree with zero objects whose producer was destroyed a month ago. That is a silent break of a served surface, not a description backfill, so ruling 97237's shape does not reach it, and no owner confirmation could make it intended: the act it belonged to (X-ii-a's `_staging` re-home) is dead on the producer side. The MDPF served-layout consolidation is now `MDPF_CANON`'s and `LGIC_LGCTFM`'s (its fork control 3 names exactly these two gold trees).
2. **Not (b) as a wait.** The owner is dark; "have the owner land or withdraw it first" is a wait on a seat that is not there (Rule 27: no FWD, and no cell, is a wait).
3. **(c): UN-STAGE the emitter half in its own commit, then plan.** `git checkout 2740e4de8f^ -- infra/aws/terraform/opal-assets/emitter.tf` restores the exact pre-change bytes (no later commit on the file); the commit message records: X-ii-a's AE half is withdrawn from the root because its producer was destroyed at @120a822241 and its target tree is empty; the change stays in history at 2740e4de8f; a re-home re-lands with its own act, in its own window, under MDPF_CANON. The mdpf-pipeline root's half is not touched by this project. Blast radius on the live plane: none -- the change was never applied; the discriminator is OG-c-2's own AC3, whose plan must now read only `opal-assets-silver-schwab` rows. No deploy ledger entry is opened for the un-staging (DESIRED-state only); OG-c-2's own entry covers the apply as before.
4. **Whose hand:** the lane admits only AE seats and none is live. The act rides OG-c-2's worker under ADHC_OWNPTH.005: `2.0.0_SA_COO~O` amends OG-c-2 to add `infra/aws/terraform/opal-assets/emitter.tf` to `<paths>` and the un-staging as the step before the plan (a modification, so LIMB 6 does not fire; the worker is cold-handed anyway). If COO~O prefers an AE hand, it asks `0.0.0_AB_MSTR` to seat `0.8.0_AE_CloudComp`; this ruling does not require it.
5. **G-B stands, no re-read.** Both halves name the schwab function family as the blast radius; the un-staging removes rows from the plan and adds none, so the radius the halves cover is unchanged. Row W4-S5 is dispositioned at L8/L9 with the un-staging commit as the issuer's evidence.

## R-OG-2 (~18:0xZ) -- OG-p-1 AC11, AC12, AC13: each re-cut to the instrument that can answer it; the two gaps the audit record exposed are carried as findings, not fixed in a baseline cell

**Call:** 10 of 13 PASS; AC11 (p95 per tool from the audit record: 0 of 78,049 records carry a latency field), AC12 (the OAuth client inventory from the audit record's `client_id`: the field does not exist), AC13 (every AWS call a read verb: 8 of 57 calls are `ssm:SendCommand`).

**Ruling.**
- **AC11 -- accepted as recommended, with the grain disclosed.** p95 comes from the ALB's `TargetResponseTime` (CloudWatch, `arn:...loadbalancer/app/opal-gateway/89166a68f337e5a4`) over the same stated window, sample count printed. The ALB does not know the MCP tool, so the figure is per target group and overall, not per tool; the criterion says so and does not claim the per-tool split. The audit record's missing latency field is a FINDING carried to the round's L10 (FWD-7's later proof needs a per-request measure the Gateway itself emits).
- **AC12 -- accepted as recommended, with the gap carried.** The inventory is read from the OAuth client registrations the Gateway persists, counts per client, and states that clients are process-local as the original text asks. The audit record's missing `client_id` is a FINDING against FWD-8's bar ("see who used which master without exposing private values in the support record"): a support record that cannot name the client cannot meet it. It is carried to L10, not fixed in the baseline cell, and the CVO grades FWD-8 with it in view.
- **AC13 -- accepted for the baseline already run; the prospective mechanism is a named SSM document.** For OG-p-1's own command log, the 8 `ssm:SendCommand` calls are admitted iff each command's text is enumerated in the proof and each is a read (the probe prints the 8 texts and its denominator 57). For every LATER host read in this project (OG-i-2's IAM onward), `ssm:SendCommand` is allowed only on a named SSM document whose content IS the fixed read-only commands, with the IAM resource pinned to that document's ARN -- read-only by construction, not by grading free text after the fact. `AWS-RunShellScript` with caller-supplied parameters is not that document.
- All three are amendments to OG-p-1's order before its cold re-hand, COO~O's act; the PRD is unchanged by them.

## R-OG-3 (~18:0xZ) -- the Schwab-to-SharePoint fold-in is FWD-9, added to the PRD at v0.3, sequenced LAST, its inputs expressly Andrew's

**Call:** Andrew-direct this session, verbatim in the PRD's FWD-9 SOURCE line. Prior art: COO~O's 2026-09-15 log :37-39 (a read-only count of `dim_transaction` and `fact_trn` for the two masters). No PRD, cell or order carried it.

**Ruling.** The outcome was RIGHT and INCOMPLETE (Phase 0 re-entry, step F0): a new `FWD-9` at the next unused number, FWD-1..8 unchanged. Bar EXERCISED; ACCEPT in plain English (a named person finds the approved transactions in the named folder on the set schedule; a person not on the list cannot open it; the totals agree with the Gateway's answer; Schwab's data is untouched). The five inputs -- destination site and folder, dataset(s), cadence, recipients, interim or standing -- are Andrew's, asked by COO~O in his session, and the outcome is EXPRESSLY QUALIFIED on them (Rule 27's one admitted wait: his word). Sequenced last, after OG-x-1 and OG-r-1; the cell is not cut until the word arrives. CONTRACTS C6 gains a SEPARATE export reader role scoped to exactly `dim_transaction` and `fact_trn` for the two masters; the six-prefix data role, the catalog-read role and OG-i-2's reader are NOT widened. Names and addresses are builder output (Rule 30). The ratified-text half re-opens to `3.0.0_SA_CVO` (ENDPOINT and CONTRACTS both changed); the brief half re-opens only if the version bump moves its hash. PRD v0.3 landed beside this ruling; the L3 register row carries the lineage.

**What this ruling does not decide:** the five inputs (his), and whether the export is the Gateway's own scheduled job or a Lambda -- that is L5's, from the plan, after his word.

## R-OG-3 addendum (~18:2xZ) -- the tracked carrier of Andrew's words, and what moved out of the FWD-9 card at v0.4

**Andrew-direct 2026-09-16 at the `2.0.0_SA_COO~O` terminal, relayed in 97496 CALL 3, VERBATIM:** "One part of doing this is also figuring out the completion of the Schwab to Sharepoint solution which you should be able to find some prior art on because its something we were working on yesterday as well. I'd like that work to be folded into this, even if it is sequenced at the end of the MCP implementation." The five inputs (destination site and folder, dataset(s), cadence, recipients, interim bridge or standing output) were asked of him by `2.0.0_SA_COO~O` in that session. FWD-9 was added at v0.3 (2026-09-16 ~18:0xZ, `1.0.0_SA_CTO`, R-OG-3) at the next unused number, FWD-1..FWD-8 unchanged. At v0.4 those three facts left the card (the CVO's defect 1: no seat names or version notes inside ENDPOINT) and live here; the verbatim words stay in the card's SOURCE line as well, so the PRD and this record both carry them. Defect 2 is cured by C6 stating that FWD-9's export surface is outside `NFRA_OPLGTW_CONTRACT.json` v1.0 and is enumerated into the contract at its cell, with the role name from builder output, before any code consumes it.

## R-OG-3 RETIREMENT (~18:3xZ) -- FWD-9 leaves NFRA_OPLGTW at v0.5 on Andrew's word

Andrew-direct ~18:2xZ (record `ANDREW_DIRECT_20260916_182xZ_RESERVED_GROUP_FOUR_CALLS_RULED.md` @50d1b9403e, call 4): the Schwab-to-SharePoint work is relegated to `4.0.0_SA_CRO~G`, who writes the brief qualified for `2.0.0_SA_COO~G`'s workflow; no new project unless the brief needs one. So FWD-9 is RETIRED at v0.5: its number stays vacant forever; the card and C6's export paragraph are removed; endpoint_outcomes read FWD-1..8. **What the project no longer promises:** a scheduled SharePoint delivery of the Schwab transactions a named person is approved to see. That capability now lives in the CRO~G brief. The CVO's v0.3/v0.4 reviews and signature @e50f2b6947 stand on the record; the ratified-text half re-opens once more on the removal. Andrew's verbatim words stay in the R-OG-3 addendum above as the tracked carrier.

## R-OG-4 (~18:3xZ) -- row W4-S8: the 49F log reads the G-B conditions require are ADMITTED, read-only, on the named keys only; 08335338 IS 49 Financial's master by the identity spine

**Call:** `2.0.0_SA_COO~O` 97506 call 4. G-B's conditions 4, 5 and 7 read `s3://opal-data-49financial/gold/advi/_logs/` and the `date=D` VersionIds; OG-c-2's cross-firm bound admits only `schwab/08242234/` and `schwab/08335338/`; COO~O would not rule from inference on a NEVER line and asked for the carrier.

**The carrier:** `infra/logic/05_IDENTITY_SPINE.md` :83 (`schwab` masters `08242234`, `08335338` -> `49financial`) and :97 (`08335338 | schwab | 49financial | "49F Schwab Black Diamond"`); `04_SCOPE_TICKLIST.md` :50 (`schwab/08335338`, 49F Black Diamond master, FIRM -> 49 Financial, ruled). So the 49F gold chain the accelerator dispatches from `schwab/08335338/meta/complete/` is that master's OWN downstream, and a read of its `_logs/` is not a reference to another firm's data. **Ruling:** the NEVER line (a pipeline TREE referencing another firm's data) is not touched by a worker's read-only probe of a sign-off condition; OG-c-2's bound is amended to admit `s3api list-objects-v2` / `head-object` / `get-object` on exactly `gold/advi/_logs/` and the `date=D` keys conditions 4, 5 and 7 name in `opal-data-49financial`, and nothing else in that bucket; the probe prints every key it read. The carrier is cited in the bound.

## R-OG-5 (~18:3xZ) -- row W4-S9: G-B's replay write set is FOUR objects; both halves carry it; a read-only dry run proving zero silver writes and zero missing dims is a precondition and a STOP

**Call:** 97506 call 5. The producer's only single-date replay path writes a run manifest per master before the marker, so the replay writes 4 objects where Half 1 names 2; a missing projection dim would also be written. **Ruling:** as recommended and one step further -- both halves' write sets become the 2 markers + 2 run manifests with rollback `delete-object` per VersionId; the pre-replay read-only dry run of `convert_object` for `D_r` must print ZERO silver writes AND ZERO missing projection dims, any non-zero a STOP and a row; the replay stays HELD until Half 1 carries the same terms; A1 (the deploy) runs meanwhile. This seat's half is amended and re-signed in the sign-off file (section E) in this commit; COO~O amends Half 1.

## R-OG-6 (~18:3xZ) -- R-OG-2's named-document limb binds from OG-i-3 onward; OG-i-2 runs as handed and its SendCommand calls are graded by command text

**Call:** 97506 call 6. OG-i-2 was handed before R-OG-2 and runs on-host arms via `AWS-RunShellScript`; the probe identity is the operator user, which cannot be pinned; no cell owns creating the document. **Ruling:** as recommended -- the limb binds from OG-i-3: one `aws_ssm_document` resource in OG-i-3's order (same root, same state slot) whose content is the fixed read-only commands, and the IAM pin binds the operator role `opal-gateway-access-admin` when a probe assumes it; a probe still run as the IAM user is DISCLOSED as unpinned in its proof. OG-i-2 is not amended; its SendCommand calls are graded like OG-p-1's AC13 (each command text printed, each a read, denominator printed).

## R-OG-7 (~19:2xZ) -- rows W1-S9 / W1-S11: the three applied names are RENAMED to the builder's output in the next apply of the root, before any runtime consumer binds; no registry row can produce them and no R20 entry is opened for a resource this project created today

**Call:** `2.0.0_SA_COO~O` 97544. The commit-time naming check prints REFUSE (WARN mode) for three names OG-i-2 applied at 18:25Z: `opal-mcp-emp-menachem-schwab-read` and `opal-mcp-schwab-catalog-read` (fixed verbatim by this seat's own PRD C6, v0.1, 2026-09-14) and the inline policy `opal-gateway-assume-schwab-readers` (the worker's choice). COO~O's options: (a) registry rows under which `name()` returns exactly these strings; (b) an R20 departure entry for Andrew's acknowledgement.

**Measured before ruling (19:1xZ):** `grade()` on the three: OUT-OF-PATTERN each (`opal-mcp-emp-menachem-schwab-read-role`, `opal-mcp-schwab-catalog-read-role`, `gateway-assume-schwab-readers-policy` as the builder's nearest forms). The grammar is `{system}-{scope}-{function}[-{qualifier}]-{kind}`; the qualifier slot admits a tier, a table, a leg or an environment and NOTHING else (FN2), the `opal` prefix is reserved so the system slot takes the registry key `gateway` (systems.json, EN-r-5), and a person's name has no slot -- so (a) is not available: no registry row makes `name()` emit `emp-menachem`. `name("gateway", None, "schwab-read", "role")` returns `gateway-schwab-read-role`; `name("gateway", None, "schwab-catalog-read", "role")` returns `gateway-schwab-catalog-read-role`; `name("gateway", None, "assume-schwab-readers", "policy")` returns `gateway-assume-schwab-readers-policy`. Consumers of the typed names outside this project's own records: `infra/aws/terraform/opal-gateway/schwab_reader_iam.tf` (6), `infra/aws/ec2/opal-gateway/app/integrations/schwab/aws_roles.py` (1), `org/standards/NFRA_OPLGTW_CONTRACT.json` (2). No served surface; OG-i-3 is the next apply of the root and the first order that wires a runtime consumer to an ARN.

**Ruling: (c), rename now.** The names are moved to the builder's output in OG-i-3's apply -- the same root, the same state slot, before any runtime consumer binds -- with the contract JSON (v1.1: `reader_role`, `catalog_role`, the policy), `aws_roles.py`'s reference and the Terraform declarations moved in the same order; the trust/ExternalId pairs are re-keyed at create, which is free at this hour and never again. The person a grant belongs to lives in the trust policy's ExternalId, the application's entitlement record and the role's tags, never in the name; a later principal with a different approved prefix set gets a role named by that scope (a tier or table qualifier), never by the person. Blast radius: destroy/create of the two roles, their attached deny policies and the inline policy (the ten resources OG-i-2 added), no served key, no source object; OG-i-3's plan must show only those rows plus its own; a deploy ledger entry as usual. OG-i-2's proof and its evidence stand at their vintage under the old names. (b) is REFUSED: an R20 entry is for a deliberate departure, and a person-named role created today under a PRD this seat wrote before Rule 30 landed is a defect to fix, not a departure to declare -- his word today, "Should be using LGIC_NAMING patterns in both cases", is the direction. PRD v0.6 restates C6 by reference to the builder (CONTRACTS only; the ratified-text half re-opens). Rows W1-S9 and W1-S11 take OG-i-3's rename commit as the issuer's evidence.

## R-OG-8 (~19:3xZ) -- the access-state table is RENAMED to the builder's name in its own order, its records carried across; no R20 entry

**Call:** `3.0.0_SA_CVO` 97550 (the v0.6 review, defect 2): CONTRACTS :135 types `opal-gateway-access-state`; `grade(..., DYNAMODB_TABLE)` reads OUT-OF-PATTERN on the same ground as R-OG-7 (`opal` reserved), canonical `gateway-access-state-table`. The table is this project's own (OG-i-1, ledger 20260915T2152Z), stateful, with a runtime consumer and an operator-audit namespace that must never be deleted; four carriers type it (`schwab_access_state.tf`, `app/access_state.py`, `app/oauth_as.py`, the contract JSON). Rename with the records carried across, or an R20 entry Andrew acknowledges.

**Measured before ruling (19:3xZ):** `name("gateway", None, "access-state", "table")` = `gateway-access-state-table`, CONFORMANT; `describe-table` on the live table: 7 items, 1,015 bytes, created 2026-09-15, ACTIVE. So the carry-across is seven records.

**Ruling: rename, in its own order in the same root, before any further consumer binds.** Not a rider on OG-i-3's IAM rename (a stateful move gets its own order and ledger entry): create the builder-named table, copy every record with the item count equal on both sides and the operator-audit namespace verified item by item, move the application's table reference and the Terraform declaration together, retain the old table until the copy is proven, remove it in the same order's rollback window. The no-delete namespace is the reason for the item-by-item check, not a reason to keep the name: seven records copied under proof is cheaper than a permanent departure on the platform's own subsystem. An R20 entry is refused on the same ground as R-OG-7 -- a resource this project created yesterday under a typed PRD name is a defect to fix, and his word today is the direction. PRD v0.7 names the table by the builder and states the carry-across as a constraint; the contract JSON reaches 1.1 across the two rename orders (v0.6's defect 1, worded as a sequence); the ruling id and history leave CONTRACTS (defect 3) and live here. `opal-mcp-audit` predates this project and is outside Rule 30, as the CVO recorded.

## R-OG-9 (~19:5xZ) -- W4-S11: the listing one level above the admitted keys is a bound exceeded READ-ONLY, and the shape was this seat's; the source-map hash is carried by OG-i-3 in `<paths>`; OG-c-2's AC6 vintage is disclosed, no re-run

**Calls:** `2.0.0_SA_COO~O` 97564, calls 8 and 9.

**Call 8 (row W4-S11).** OG-c-2's worker listed five folder prefixes per pass under `opal-data-49financial/gold/advi/`, one level above the `_logs/` prefix and the `date=D` keys R-OG-4 admitted, to FIND those keys; every call read-only and printed. **Ruling:** recorded at L9 as a bound exceeded read-only, never a write; the CVO grades it. The widening is a finding against R-OG-4's shape, which was mine: it admitted "the named date=D keys" without admitting the listing that resolves them, and a key cannot be named without a list one level up. R-OG-4 is amended: the admitted read set is `_logs/` plus the `date=D` keys PLUS `list-objects-v2` on exactly the prefixes needed to resolve them, enumerated in the bound by name (the five the worker printed), and nothing else in that bucket. Rule going forward, for every sign-off condition that reads another firm's tree: name the LIST prefixes explicitly beside the keys.

**Call 9(a) (row W4-S7).** OG-c-2's build rewrote `infra/aws/lambda/ci/lambda-source-map.json` by one line (the schwab artifact hash); it is uncommitted, so HEAD carries the pre-deploy hash; the worker's bytes are preserved at `.scratch/oplgtw_c2_lambda-source-map.json`. The lane on that file is the AE lane (CLOUD_OPS_OR_ETL; this seat REFUSED, measured), and no AE seat is live. **Ruling:** OG-i-3 carries the one-line change in `<paths>` under ADHC_OWNPTH.005 (a modification of a running order) and commits it with a message naming OG-c-2's deploy and the artifact hash, before its own apply. This is not optional hygiene: the source map is the Lambda plane's RECORD under R-26, and a stale hash at HEAD makes the per-plane classifier and the deployed-bytes diff both read the wrong artifact. COO~O verifies the grant at the cut with `--check-agent` on the staged face.

**Call 9(b).** OG-c-2's AC6 probe graded the G-B sign-off at the worker branch's HEAD (@65e254cafe, the pre-amendment halves) while the replay itself ran on the re-signed terms read at CLOUD HEAD (@7c44a2cf82): four objects written, the zero-write dry run printed. **Ruling:** no re-run; the world act followed the re-signed terms and the proof says so; the AC6 evidence vintage is disclosed for L9 and the CVO grades with it in view.

**Noted, not a call:** the 08335338 replay started one 49F chain run that re-PUT 30 of 31 gold objects for D=2026-09-15 after the 12:45Z floor's CHAIN OK, inside G-B branch W with before/after VersionIds recorded -- the branch this seat's half named as exercised, so it is covered.

## R-OG-10 (~20:2xZ) -- row W5-S4: `schwab_get_access`'s operation class is an EXPLICIT contract value `access`, never `None`; AC26 re-cut as the classification of exactly the five tools

**Call:** `2.0.0_SA_COO~O` 97577 call 10. OGQ2-AC26 required `app/data_entitlement.py`'s diff against the cut base to be exactly five added entries, but OG-z-1 had already classified all five Schwab tools there (SCHWAB_TOOLS :75-81, TOOL_CLASSES :103 @0fc7c71160, row W3-S23), so q-2 correctly added nothing -- the cut's premise was the defect. Under it: SCHWAB_TOOLS maps `schwab_get_access -> None`, which is not a contract operation class (`list`, `describe`, `query`, `download_filtered`); the tool returns only the caller's own scope and revision and reads no data object.

**Measured:** `data_entitlement.py` :164-166 already uses `None` from `classify()` to mean "a tool nobody has classified, denied to everyone"; SCHWAB_TOOLS's `None` means "needs no data operation, any active grant carries it" (:73-74). Two `None`s with two meanings in one module is Rule 24(iii)'s intent-coherence defect, and a reader of the contract cannot see the second meaning at all.

**Ruling: (a) an explicit class.** `schwab_get_access`'s operation is `access` -- "read the caller's own grant and revision; requires an ACTIVE grant carrying at least one other operation; reads no data object" -- added to the contract JSON's `operations` enum in the v1.1 the rename orders are already producing, and to SCHWAB_TOOLS as the string `"access"`; `None` is reserved for the unclassified-and-denied meaning `classify()` already gives it. The entitlement check for `access` grants it iff the grant is active, which is the behaviour the comment describes, now stated as data. **(b) AC26 re-cut** as COO~O proposes: the file is unchanged against the cut base except the one mapping line, and classifies exactly the five contract tools, four with their operation class and `get_access` as `access`; the probe prints each tool and its class and the denominator 5. One mapping line and one enum entry ride the re-hand to `~5` after OG-q-3.

## R-OG-11 (2026-09-17 ~13:4xZ) -- call 11 / row S22: R-OG-10(a) is VACATED; contract v1.1 carries a TOTAL `tool_operations` map, `null` = carried by every active grant and never grantable; `operations` enum, OPERATIONS, the admin set and the :282 predicate unchanged

**Call:** `2.0.0_SA_COO~O` 97589 call 11 (row NFRA_OPLGTW-S22 @1bd2afeec1). R-OG-10(a) breaks the grant path: the contract's
`operations` enum is the GRANTABLE set -- `ops/schwab_entitlement_admin.py:163` builds its allowed set from it while
`app/data_entitlement.py:61` OPERATIONS and the guard at :214 refuse any other op -- so `access` there lets the admin write a
grant that denies its principal everything; and mapping :76 to `access` alone denies `schwab_get_access` to every grant,
because :282 admits a tool only on `op is None or op in grant.scope.operations`. Both confirmed at `d88cd32d0c`
(`data_entitlement.py`) by this seat. **OWNED:** R-OG-10 amended a grantable enum without reading who consumes it.

**Routed as a DESIGN FORK** (Andrew-direct 2026-09-17 ~13:0xZ routing record @809a8b4090): `4.0.0_SA_CRO` spawned for
precedent research; findings 97594 at HEAD a27616f46f. Operative findings: (P1) this contract already partitions named
but non-grantable members into a SIBLING key (`operations` :15 vs `disabled_operations` :21; code :61-62; guard :213-216;
admin :163-164) -- nothing non-grantable ever sits in the grantable enum; (P2) the estate's null-sentinel "ungated" shape in a
TOTAL map (`portal/src/pages/Positioning/shared/modeAccess.ts:106/:116/:194` @be8cf218), which the gateway already follows
at :76/:282 -- in code only; two independent code copies of the mapping exist and nothing ties them
(`app/data_entitlement.py:76` SCHWAB_TOOLS, `app/integrations/schwab/integration.py:70` TOOL_OPERATION @c3728d6bdb).

**Ruling.** (1) R-OG-10(a) and its AC26 re-cut are VACATED. (2) Contract v1.1 adds one key, `tool_operations`: an object
with EXACTLY the five `tools` as keys, each value a member of `operations` or `null`; `null` is documented in the contract
as "carried by every ACTIVE grant; never grantable; reads no data object" (today: `schwab_get_access` only). This is P2's
shape given a contract carrier and P1's partition respected. (3) `operations`, `disabled_operations`, OPERATIONS, the
admin's allowed set and the :282 predicate do NOT change; :76 stays `None`. (4) The drift the research found is closed by a
test, not prose: both code copies (SCHWAB_TOOLS, TOOL_OPERATION) must equal the contract's `tool_operations` exactly, keys
and values, denominator 5 printed -- a positive control mutating one copy must fail it. (5) R-OG-10's Rule 24(iii)
observation (classify()'s `None` = unclassified-and-denied beside SCHWAB_TOOLS's `None` = implicit) is NOT re-opened: in the
contract the map is total, so `null` has one meaning there; the code-side ambiguity is pre-existing and unchanged.
COO~O's option (a) (a class vocabulary + a :282 change) is not taken: it adds a vocabulary the estate's contracts do not
carry and a predicate edit the total map makes unnecessary.

**Carried:** PRD v0.8 CONTRACTS names the key (re-opens the ratified-text half only). OG-q-2's re-hand carries (2) and (4)
in its `<paths>`/criteria, cut by `2.0.0_SA_COO~O`.

## R-OG-12 (2026-09-17 ~14:5xZ) -- call 12 / row W6-S5: (b) with one addition -- the hash-matched A7 real-data questions ask at the FIXED date OG-v-3 sealed (2026-09-15); "latest" resolution is still exercised, by a separate per-master request graded against the live closure at ask time, never against a sealed value

**Call:** `2.0.0_SA_COO~O` 97601 call 12 (row NFRA_OPLGTW-W6-S5, ARMED, disarm owner `2.0.0_SA_COO~O`). OG-v-3 sealed RQ1-RQ6
against OG-c-2's 2026-09-15 objects; qualified 2026-09-16 closures for both masters landed 09:46Z and 10:16Z, and
`infra/aws/ec2/opal-gateway/tests/acceptance/WALKTHROUGH_PROTOCOL.md:209` defines "latest" as the latest qualified complete
date, with RQ1-RQ6 (:215-220) asked at "latest" -- so OGV4-AC5's hash match reads a correct Gateway as wrong, again every day.

**Classified: the default class (this seat's rec), not a design fork** -- a test-determinism choice inside one acceptance
walkthrough, with no estate pattern at issue.

**Why not (b) alone:** the PRD's C3 (`NFRA_OPLGTW_PRD.md:155` @8a63c77b51) makes "the available dates and latest qualified date
are returned explicitly" a contract obligation, and RQ1-RQ6 are today the walkthrough's only exercise of latest resolution.
Pinning all six to 2026-09-15 would make A7 deterministic by deleting that coverage.

**Ruling.** (1) RQ1-RQ6's hash-matched answers are asked at the explicit business date 2026-09-15 (RQ5/RQ6's "previous
qualified date" = the qualified date immediately before 2026-09-15, as sealed); protocol section 4's "latest" becomes "the
fixed date sealed by OG-v-3" for those six. No re-seal. (2) v-4 ADDS one request per master with no date, and grades it
against a live read taken in the same walkthrough: the Gateway's returned latest qualified date equals the newest qualified
closure marker for that master at ask time, and the returned available-dates list contains 2026-09-15. No hash, no sealed
value, so it cannot drift. (3) The amendment rides TO-OG-v-4 with protocol section 4 added to its `<paths>`, cut by
`2.0.0_SA_COO~O`. (4) W6-S5 disarms when that amendment commits; `2.0.0_SA_COO~O` files the disarm evidence.

## R-OG-13 (2026-09-17 ~18:4xZ) -- call 13 / row W6-S6: both acts APPROVED as recommended, and a STANDING BAR -- a criterion that exercises a module PROVES ITS CALL SITE on the live path, with a mutant that removes the call site and must fail

**Call:** `2.0.0_SA_COO~O` 97628 (row NFRA_OPLGTW-W6-S6, ARMED, disarm owner this seat). OG-v-2's integrated harness ran the real
app and found `app/integrations/schwab/semantics.py`'s `assert_sum_allowed` family is never called from `query.py` or
`integration.py`: a nonadditive SUM (closing_price) and an ungrouped quantity SUM both SUCCEED where the contract says refuse.
OGV2-AC2 FAILs and the order stays open. The issuer re-measured with a different instrument @693b2972a0: `assert_sum_allowed` is
defined at `semantics.py:273` and referenced nowhere outside `tests/test_schwab_semantics.py`; no module under `app/` imports
`semantics`. **Nothing is deployed, so nothing served is wrong today.**

**Classified: the default class (this seat's rec).** The remedy is a cut, not a pattern choice, and the estate already has the
lesson in law (an injected self-test certifies the ARMS, never the WIRING).

**Ruling.** (1) and (2) as `2.0.0_SA_COO~O` proposed. **(1)** ONE newly-added order on a new decomposition cell, issued to `~5`:
wire the additivity and grouping checks into the query path. Its criteria run on the LIVE path through the real app -- a
nonadditive SUM refuses, an ungrouped quantity SUM refuses, a legal SUM still succeeds -- **plus a MUTANT control that removes the
call site and MUST fail those criteria**, so a green cannot come from a module nothing calls. Both PRD halves read SIGNED at v0.9,
so LIMB 6 admits it. **(2)** Then re-hand OG-v-2 to build the 7 unbuilt machine A-rows (row W6-S7) and re-grade AC2 whole.
**q-2 and q-3 are NOT re-opened** -- their cells are closed and the cut, not the work, was the defect.

**STANDING BAR for every remaining NFRA_OPLGTW cut (and the reason this ruling exists):** a criterion that exercises a module in
isolation does not evidence the behaviour the contract promises. From here, **a criterion whose subject is a check, a guard or a
refusal names the CALL SITE it runs through and is graded on the live path, with a mutant control removing that call site.** OG-q-3's
14 of 14 passed over a module nothing imports; that is the exact shape this bar refuses.

**W6-S6 disarm (this seat's field):** ARMED until (1)'s order drains with its mutant control failing as designed; the drain's proof
instance is the disarm evidence, and `3.0.0_SA_CVO` writes the clock on this seat's word at that point.

## R-OG-14 (2026-09-17 ~19:1xZ) -- call 14 / row W1-S13: APPROVED as recommended -- the renamed readers' assume and deny arms are re-EXERCISED as one added criterion on TO-OG-r-1, live from the host through the released build, with R-OG-13's mutant control; i-2 and i-3 are NOT re-opened

**Call:** `2.0.0_SA_COO~O` 97640 (row W1-S13, INERT, correctly refused by the worker). The issuer names its own order text as the
defect: TO-OG-i-3 told the worker to re-run OG-i-2's live denial and assume arms against the new ARNs, but those arms run
on-host through `AWS-RunShellScript` with caller-supplied parameters, which **R-OG-6 forbids from OG-i-3 onward**, and the fixed
parameterless document that same cell creates cannot express them. The worker refused as written and substituted
`iam get-role` / `get-role-policy`, which confirms the trust principal, the two re-keyed ExternalIds and the six-statement
deny/allow shape as **DECLARED**. So after the rename and the ExternalId re-key, the assume arm and the POLICY#-deny arm are
**EXERCISED nowhere**: OG-i-2's live proof stands only at its old-name vintage.

**Ruling: as recommended.** ONE criterion is added to `TO-OG-r-1` -- the first cell that legitimately exercises the released
build on that host: from the host, through the released build, an assume of EACH renamed reader role succeeds with its re-keyed
ExternalId, and the wrong-ExternalId arm is DENIED; graded live, with a mutant control per R-OG-13. No new cell. OG-i-2 and
OG-i-3 are NOT re-opened -- the work was right and the order text was wrong, and r-1 is already blocked on OG-v-2, so this costs
no time. **DECLARED is not EXERCISED, and this ruling is what keeps that distinction from being lost at the rename.**

**Standing, restated:** R-OG-6's parameterless-document bar is untouched by this. A live arm that cannot be expressed under it
moves to a cell that can run it, never back to caller-supplied parameters.

**G-A, the one Andrew gate on this project's critical path:** OG-i-4 (the Gateway instance resize) is HELD on his recorded word
to stop and start the instance. `2.0.0_SA_COO~O` offered to draft the ask; this seat puts it to him directly instead, with its
own recommendation, the same turn it was surfaced. Nothing else on the critical path waits on him.

## R-OG-15 (2026-09-17 ~19:4xZ) -- call 15 / row W5-S10: AMEND OG-q-4 to own the two tests that ASSERT the defect it fixed; not a q-2 re-open, not a third cell. The drain stays HELD until the amendment lands

**Call:** `2.0.0_SA_COO~O` 97646 (row W5-S10, BLOCKING, INERT). OG-q-4 wired the additivity and grouping checks into
`check_against_grant` in `query.py`: AC1/AC2/AC3 PASS on the live path and **AC4's mutant fired as designed** (R-OG-13's bar
did its job). AC5 FAILS because `tests/test_schwab_query.py::test_ogq2_ac07` and `::test_ogq2_ac15` **assert that an
UNGROUPED QUANTITY SUM is ACCEPTED** -- the exact shape the contract says refuse. Re-measured at the issuer's seat on a
second instrument in the worker's worktree: 2 failed, 23 passed, both failures those two tests. The file is OG-q-2's and
outside q-4's grant, so the worker refused and left the order OPEN. **Correct on both counts.**

**The finding underneath, stated plainly: two of OG-q-2's 29 criteria PASSED BY ASSERTING THE DEFECT, and would have gone
on passing forever.** Same root as W6-S6 (R-OG-13): a criterion written against a module in isolation, with nothing tying
it to the contract the module exists to enforce. **A test that encodes the wrong behaviour is worse than a missing test:
it converts a regression into a guarantee.**

**Ruling: the issuer's REC, as written.** Amend `TO-OG-q-4` to grant `infra/aws/ec2/opal-gateway/tests/test_schwab_query.py`
for EXACTLY those two tests' expectations -- each flipped to expect the contract's refusal, no other line touched -- and
re-hand `~5`. Criteria: the diff's line count is printed; the file's test count before and after is printed (23 passing +
2 corrected = 25, denominators stated); each flipped assertion cites the contract clause it now encodes. This is **q-4
finishing its own AC5**, not a re-open of q-2: q-2's cell is closed and its other 27 criteria stand.

**The third-cell alternative is NOT taken.** A cut and a spawn for a two-assertion change buys a tidier ledger and costs a
round-trip; the honest record is this ruling plus the amendment's printed diff.

**The HOLD is right and is affirmed.** Merging q-4 before the amendment would leave CLOUD with two knowingly red tests --
the S21 shape. The branch sits safe at 881b1a5445; the drain lands when the amendment's criteria pass, with the whole
module green.

**Carried into round-close:** the CVO grades OGQ2-AC7 and OGQ2-AC15's original passes as **UNSOUND AT THEIR VINTAGE** in
its L9 record -- not to re-open the cell, but so the project's own history does not read as if those two ever evidenced
anything.

## R-OG-16 (2026-09-17 ~20:4xZ) -- STANDING BAR on the back of row S24 (no call was made; this is the rule the finding earns): a RENAME cell carries a CONSUMER CENSUS of the old name, with its denominator printed, and the census is a criterion

**Not a call.** `2.0.0_SA_COO~O` (97656) reported and is repairing this inside `TO-OG-v-2`'s own grant; nothing waits on this
seat. The ruling exists so the class cannot repeat on the renames still ahead.

**What happened, in its own words and measured on the SHARED TREE:** OG-i-3 carried R-OG-7's reader-role rename and **was cut
with no census of the old names' consumers.** `tests/acceptance/conftest.py:88-89` still hardcodes the pre-rename ARNs;
`aws_roles.role_config()` refuses the stale ARN and `integration.py` swallows it as UNAVAILABLE. `pytest -q
tests/acceptance/test_local_acceptance.py` on CLOUD reads **5 failed, 2 passed** -- so the shared branch has carried a red
acceptance module since i-3's drain, independent of q-4, and q-4's live-path criteria could not reach the wiring they were
written to grade. Corroborated on a different checkout by worker ~5's row W5-S11, same two lines. **Nothing deployed and
nothing served is wrong: the red is the harness, not the product.**

**The bar, for every remaining rename in this project.** A cell that renames an applied resource carries, as a CRITERION and
not as prose:
1. a census of the OLD name's consumers over the tracked corpus -- code, tests, fixtures, Terraform, docs that are read by a
   runner -- with **the denominator printed** (files scanned), and
2. the repoint of every live reader the census finds, inside that cell's own `<paths>` grant or carded BLOCKING where the
   path is not granted, and
3. a re-run of any harness the census names, **on the shared tree after the drain**, not only in the worker's worktree.

**Why the third limb exists and is the one that was missing:** a worktree-green harness and a shared-tree-green harness are
different measurements, and only the second is what the next seat inherits. This is LGIC_ENFORCE's R-27 lesson (re-point the
LIVE READERS, enumerate them, never assume) arriving in this project by a different door.

**Carried:** `2.0.0_SA_COO~O` repairs conftest inside OG-v-2; S24 disarms on that repair with the shared-tree re-run as its
evidence; OG-q-4's drain stays held until the module is green there.
