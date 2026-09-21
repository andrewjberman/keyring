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


---

## R-OG-17 -- 2026-09-17: the dim_asset partial-account restriction is WIRED on the live path; one cell, R-OG-13's bar, and the word is GIVEN

**Call:** `2.0.0_SA_COO~O`, msg 97678 CALL 16, row `NFRA_OPLGTW-W6-S8` (ARMED, disarm owner this seat). The worker's
integrated harness found a SECOND unwired check: PRD C3's `dim_asset` partial-account restriction -- under a
partial-account grant, `dim_asset` returns only CUSIPs the authorized accounts hold on the same master and date -- is
one of OG-q-3's acceptance bullets and is not enforced on the live query path. Same shape as W6-S6, different rule.
A6's failure is this; A8's is OG-q-4's wiring, still on its branch.

**RULING: the REC is adopted verbatim and the cell is CUT -- `2.0.0_SA_COO~O` has the word, issued to `~5` when it
frees.** Graded through the real app under R-OG-13's bar, three criteria and a mutant: a partial-account grant sees
only its accounts' CUSIPs; a CUSIP held ONLY by an unauthorized account is ABSENT; and a mutant that removes the call
site FAILS both -- the third is the one that says the check is wired rather than merely present. R-OG-16's three limbs
bind wherever a name moves inside the cell.

**This is the THIRD instance of one root cause and it is now named as such.** R-OG-13 (additivity), R-OG-15 (grouping)
and this row are all criteria written against a MODULE in isolation and proven where nothing calls them. The standing
bar already says call-site grading with a mutant control; what this instance adds is that the population was never
enumerated. **So the same cell carries a CENSUS: every rule PRD C3 states, with the denominator printed, each marked
enforced-on-the-call-path or not, measured through the app.** A fourth instance found one at a time would mean this
seat graded the members and never the set they share (Rule 22's shared-dependency limb).

**Sequencing, as `2.0.0_SA_COO~O` laid it out and this seat confirms:** OG-q-4 re-grades at the repaired harness and
drains; the `dim_asset` cell lands; only THEN does OG-v-2 take its last re-hand to re-grade AC2 whole, or AC2 fails
again on A6 alone. S24's disarm is ACCEPTED on its evidence row `NFRA_OPLGTW-S25` @`c4b78ef2c4` -- R-OG-16 limb 3
exercised end to end, the shared-tree re-run reading 2 failed / 12 passed where it read 5 failed / 2 passed, same
command, one drain between, five ARN-class failures cleared and 0 new. `3.0.0_SA_CVO` writes the clock.


---

## R-OG-18 -- 2026-09-18: ONE cell for all four uncalled C3 rules, and the single MUTANT is what makes that choice falsifiable

**Call:** `2.0.0_SA_COO~O`, msg 97747 CALL 17. R-OG-17's census addition drained @`4db9547d32` (OGQ5-AC5 PASS) and
found that `dim_asset` was not alone: **four more C3 rules are built-but-uncalled** (rows `W5-S14`..`W5-S17`) -- each an
existing `semantics.py` function nothing on the query path invokes. Same shape as R-OG-13, R-OG-15 and W6-S8.

**THE CENSUS IS WHY THEY WERE FOUND, and that is the part to keep.** It was built BY SUBTRACTION exactly as the order
required: C3 split into 6 paragraphs, **34 sentences as the printed denominator**, 3 excluded with their reasons
stated, 2 folded into one row against `qualify_asset_plan()`'s own shape, leaving **29 rules -- 20 ENFORCED-ON-CALL-PATH,
5 NOT-ENFORCED, 4 NOT-A-CALL-PATH-RULE**, every ENFORCED verdict naming its call site and the exercise that reached it.
Seven instances of this class have now been found in one project; the first three were found ONE AT A TIME by whoever
happened to test a call site, and the last four were found TOGETHER by asking what the members shared. **That is Rule
22's shared-dependency limb paying for itself in a single hand-off.**

**RULING: ONE cell for all four, as recommended. The REC is adopted whole.** They share one call site (`query.py`'s
grant check, where OG-q-4 and OG-q-5 already wire), one harness and one mutant control; four cells would buy four cuts,
four spawns and four drains against one edit surface and would not buy one additional discrimination.

**ONE ADDITION, which turns the risk of the one-cell choice into a measurement.** The one-cell case RESTS on the
premise that all four share that call site. So the single mutant control -- removing the shared call site -- **MUST
fail all four live-path criteria, and if it fails fewer than four, the premise is FALSE and that is the finding**: a
rule whose criterion survives the removal of the shared site is not wired to it, and the cell splits on the evidence
rather than on a guess. State that in the order as the mutant's expectation, so the one-cell choice is falsifiable by
the cell itself instead of being an assumption the drain inherits.

**The closing criterion stays the CENSUS RE-READ**, which is the right bar and the reason this ruling is confident: it
proves the POPULATION moved (5 NOT-ENFORCED becomes 1 or 0) rather than proving four tests are green. Four greens
certify four members; the census certifies the set. **And it re-prints its own denominator at re-read time** -- 29 is a
count taken at one vintage of a document this project is actively amending, so a re-read that assumes 29 is the same
inherited-count error one level up.

**On `W5-S13`, the issuer's own `<paths>` defect:** recorded and accepted as reported. `SchwabService.query()` in
`integration.py` is the only place that can hand `qualify_asset_plan()` its inputs, the first cut's grant did not name
that file, and **the worker REFUSED rather than edit outside its grant** -- which is exactly what the order asks and is
the behaviour that makes a grant mean anything. Granted for that call site only @`35377638d7`, re-handed, and the
amendment says plainly the defect was the issuer's. A lane that names its own cut as the cause is a lane whose reports
can be believed.


---

## R-OG-19 -- `2.0.0_SA_COO~O`'s reading of "after OG-q-5 closes" is CORRECT; a sequencing instruction must state its REASON, and mine did not

**The lane did not wait, and it was right not to.** R-OG-18 said to cut the C3 cell "after OG-q-5 closes". `OG-q-5` is
NOT closed -- its `AC6` is a measured FAIL on two failures owned by OTHER cells -- so waiting would have serialised
`q-6` behind two repairs it does not depend on **while slot ~5 idled.** The lane read the ordering's REASON as SLOT
AVAILABILITY, which was satisfied, cut `q-6` @`a96788f138`, and wrote the reading into the order's record face rather
than only into a message.

**RULING: the reading is right and the defect is in my instruction.** I meant "do not double-book slot ~5". I wrote a
CLOSURE condition, which is a different thing, and a closure condition would have imported `q-5`'s unrelated failures
into `q-6`'s start. **A sequencing instruction states its REASON -- dependency, resource, or L10 ordering -- because
the executing seat cannot tell them apart from the word "after", and the three have different remedies.** Where a
sequencing word is ambiguous and a lane's reading keeps work moving without breaking a stated bar, THAT READING
GOVERNS; the lane is closer to the slot than the ruling is.

**And no L10 hazard is in play here, which is worth stating so it is not re-litigated:** LD-0521's deadlock binds a
ROUND N+1 issuance cut before round N's SLUG. `q-6` is a CELL inside the same round, and adding one while a sibling
order is open is ordinary L6 work.

**COST: none -- it is a drafting rule on my own instructions.** **NON-APPLICATION: a genuine dependency, which is
named as one** ("after X drains, because Y reads X's artifact").

---

## R-OG-20 -- CALL 18 adopted whole: a REFUSAL'S ENVELOPE IS PART OF THE REFUSAL, and this is the third instance of a test asserting the right thing about the wrong surface

**Row `NFRA_OPLGTW-W5-S18`, ARMED, disarm owner this seat.** Wiring `OG-q-5` half one UNMASKED a second, unrelated
failure the first assertion had been hiding: a post-revocation `schwab_query` denial reaches the caller with the MCP
`isError` flag **NEVER SET TRUE**. `app/tools.py`'s `_PolicyGuardedMCP.call_tool()` returns `data_entitlement.py`'s raw
guard-denial dict straight through.

⛔ **THE DENIAL'S CONTENT IS CORRECT AND ITS ENVELOPE SAYS THE CALL SUCCEEDED.** That is the whole finding. A refusal
a consumer cannot detect is not a refusal -- it is a success carrying disappointing text, and every test that reads the
BODY passes while every client that reads the FLAG is misled. Nothing is deployed, so nothing served is wrong today.

**RULING: REC adopted whole. ONE small cell to `~6`**, criteria graded live through the real app -- a guard-denied call
returns `isError` true AND its contract error code; a permitted call still returns `isError` false -- plus a mutant
that removes the flag-setting line and must fail the first.

**NOT FOLDED INTO `q-6`, and the lane's reason for that is better than the cell it protects:** `tools.py` is a
DIFFERENT CALL SITE from the query path, and folding it in **would break exactly the one-cell premise R-OG-18's `AC5`
exists to test.** That is this seat's own ruling being applied against a convenience, by the lane that would have
benefited from the shortcut. `app/tools.py` belongs to no open cell, so there is no grant collision.

**THE CLASS, now measured three times this week:** `W4-S19` (a renderer graded by comparing each output to ITSELF),
`OGQ2-AC7/AC15`, and this row. **Each test asserted something TRUE about the wrong surface** -- the artifact's own
bytes, the denial's body -- while the property a consumer depends on went unasserted. **The general bar: a criterion
about a REFUSAL grades the signal the CONSUMER reads, not only the text the producer wrote.**

`OG-v-2` takes its last re-hand ONCE, after both `q-6` and this cell land, so `AC2` is re-graded whole rather than
failing twice on other cells' rows -- the lane's sequencing and it is correct.

## R-OG-21 -- THE LOGIN OUTAGE: `DeleteItem` on `RUNTIME#` is ADMITTED, because THE RATIFIED CONTRACT ALREADY PERMITS IT and the prohibition lives one tier below it

**Andrew approved branch (1) directly (2026-09-18 ~16:1xZ; to this seat, verbatim: *"i already approved it"*).**
`0.7.0_AE_CloudOps` (98003) and `2.0.0_SA_COO~O` (98004) each verified the defect on their own instruments and each
recommended (1); both correctly REFUSED to retire another cell's passing criterion to fix an outage. **That refusal is
why this ruling exists, and both were right to make it.** Login has been impossible through the durable build since
the `OG-r-1` deploy at 05:58:16Z.

**VERIFIED BY THIS SEAT AT THE BYTES BEFORE RULING, not taken from either report:**

| fact | read |
|---|---|
| `schwab_access_state.tf` @HEAD, the whole resource | TWO statements: `AccessStateStrongRead` (`GetItem`) and `AccessStateRuntimeWritesRuntimeKeysOnly` (`PutItem`, `UpdateItem`). **No `DeleteItem`.** |
| `:42` | `access_state_runtime_keys = ["RUNTIME#*"]` |
| `oauth_as.py:649` (`take_pending`), `:772` (code burn) | both call `st.delete_runtime` -- **and BOTH PASS A ConditionExpression** |
| `NFRA_OPLGTW_DECOMP.md:182` | *"...and no DeleteItem or table-admin action"* |
| **`NFRA_OPLGTW_CONTRACT.json` v1.1** | `POLICY`: *"operator writes only; **no TTL or ordinary delete**"*; `RUNTIME`: *"client/pending-auth/code/refresh/ticket/catalog; **runtime conditional writes and expiring records**"* |

⛔ **THE RULING, AND IT TURNS ENTIRELY ON WHICH NAMESPACE THE PROHIBITION SITS IN: the contract forbids ordinary delete
on `POLICY`, AND ONLY ON `POLICY`.** `RUNTIME`'s own clause affirmatively describes *"runtime conditional writes and
expiring records"* -- and both call sites are **CONDITIONAL deletes of EXPIRING records** (a pending authorization, a
one-time code). ⭐ **AND `runtime_policy_access` CONSTRAINS THE SCOPE OF WRITES (`LeadingKeys`), NEVER THE VERB SET** --
*"strong read only; write actions require all LeadingKeys match RUNTIME#*"*. **No ratified clause enumerates verbs at
all.** So branch (1) needs **no contract amendment**: it was already inside the ratified envelope.

**WHAT IT DOES CONTRADICT IS ONE TIER DOWN, AND THAT IS WHAT I AM AMENDING.** `DECOMP:182`'s *"no DeleteItem"* is
**STRUCK AS TO `RUNTIME#`** (it stands for `POLICY#` and for table-admin). `OGI1-AC5`'s requirement that the permission
be ABSENT is **RETIRED PROSPECTIVELY.**

⛔ **`OG-i-1`'s GRADE STANDS, UNDER R-43** -- the criterion was true at its vintage and was genuinely EXERCISED. A
criterion retired by a later authorized amendment is not a wrong grade. ⭐ **This is the FOURTH instance of that shape
this week** (`W1-S21`, `R38-AC2`, `LGIC_LGCTFM-S25` four hours ago, now `OGI1-AC5`): the cell was right, the record was
right at its vintage, and a later legitimate act made the evidence non-reproducible.

⛔ **BUT `OGI1-AC5` IS THE SHARPEST OF THE FOUR AND DESERVES ITS OWN SENTENCE: IT DID NOT MERELY FAIL TO CATCH THE
DEFECT -- IT CERTIFIED IT.** The criterion's PASS condition *was* the outage condition: a `DeleteItem` on a `RUNTIME#`
key returning `implicitDeny`, recorded PASS. **A criterion that REQUIRES THE ABSENCE OF A PERMISSION THE SHIPPED CODE
NEEDS is a test that passes because the system is broken**, and it will keep passing for exactly as long as the system
stays broken. **The general bar: a criterion asserting that a permission is ABSENT must name the call sites that would
need it, or it is asserting a fact about IAM while claiming one about the system.**

⭐ **AND A SECOND DIVERGENCE NEITHER SEAT NAMED, found only by reading the WHOLE resource rather than the cited
statement: `DECOMP:182` says the grant allows *"Get, Put, Update and TransactWrite"* -- and there is NO `TransactWrite`
anywhere in the file** (every `dynamodb:` action in it, both policies: `GetItem`; `PutItem`/`UpdateItem` on `RUNTIME#*`;
`GetItem`; `PutItem`/`UpdateItem` on `POLICY#*`). **So that one decomp line is wrong in BOTH directions at once --
over-granting on paper where the TF under-grants, and under-granting where the code needs more.** ⛔ **A DECOMPOSITION
SENTENCE THAT MISDESCRIBES THE APPLIED GRANT IN BOTH DIRECTIONS IS NOT A SPECIFICATION OF IT; IT IS A MEMORY OF ONE.**
The constraint belongs in the CONTRACT (where it is ratified and signed) or in the TF (where it is APPLIED) -- never in
a decomp line a later reader will cite as authority, which is exactly what happened here.

**THE CLASS -- Rule 22's shared-dependency blindness, with a live instance and a 10-hour outage as its cost.** Two
COMPLETE cells contradicted each other and **each passed its own criteria**: `OG-a-1`'s 18 tests ran on **moto, which
enforces no IAM**, so the code path was never exercised against the real grant; `OG-i-1`'s `OGI1-AC5` required and
exercised the absence. **Every per-member arm was green. The thing the members SHARE -- the grant the code needs -- was
checked by neither.**

**(2) IS THE BETTER END STATE AND IS CARRIED, NOT DROPPED:** rewriting both deletes as conditional `UpdateItem`s setting
`consumed_at` (the shape `redeem_code` already uses at `:759`), reads treating consumed as absent. It keeps every
ratified criterion green but needs tests, a release through `OG-r-1`'s route and a restart -- **not an outage remedy.**
**Round 2 carries it as the correctness item**, exactly the split `2.0.0_SA_COO~O` proposed and the same one this seat
made for the sentinel.

**AND THE HEALTH-CHECK GAP IS ROUND 2's TOO.** `2.0.0_SA_COO~O` corrected itself to Andrew unprompted: `/health` 200,
`/mcp` 401 and an ALB healthy target were all TRUE and the answer was wrong in substance, because they measure
**LIVENESS** and he asked whether he could **USE** it. ⭐ **A GREEN THAT ANSWERS A DIFFERENT QUESTION THAN THE ONE ASKED
IS WORSE THAN NO ANSWER, because it spends the asker's trust.** **No check on this service covers the login path** --
that is why a 10-hour outage was invisible to every instrument pointed at it, and building that check is round 2's.

## R-OG-21A -- CORRECTION TO R-OG-21, BY `2.0.0_SA_COO~O` (98010): my citation was ONE LINE OFF toward the prohibition my own addendum depends on, and my second finding is RETRACTED, not softened

**The outage is CLOSED.** `0.7.0_AE_CloudOps` applied and EXERCISED the fix @`df9e05cb55` on Andrew's direct word
(*"Go ahead with the fix"*, @`c298ed4b68`): `iam get-role-policy` shows the three actions under the unchanged
`LeadingKeys RUNTIME#*` condition; SSM under `opal-gateway-role` at 16:37:05Z put a `RUNTIME#probe` key, **conditional
`delete_item` SUCCEEDED**, and **`delete_item` on a `POLICY#` key still returned `AccessDeniedException`**. Ledger
`nfra-oplgtw-gw-runtime-deleteitem` opened before the act, three legs proven, CLOSED. `2.0.0_SA_COO~O` cut the decomp
amendment @`86177bf020`. **Both corrections below are `2.0.0_SA_COO~O`'s, and both are right.**

⛔ **CORRECTION 1 -- THE ONE THAT MATTERED. R-OG-21 SAID "`DECOMP:182`'s 'no DeleteItem' is STRUCK AS TO `RUNTIME#`".
THE CLAUSE IS AT `:183`.** Verified by this seat by printing the bytes at each line:

```
:182  - `describe-table` reads SSE enabled, point-in-time recovery enabled, PAY_PER_REQUEST billing, ...
:183  - the runtime grant allows GetItem, PutItem, UpdateItem and DeleteItem on exactly the table ARN, ...
:184  - the operator principal is separate, ... and holds no DeleteItem on `POLICY#` ...
```

⛔ **`:184` CARRIES THE OPERATOR'S `POLICY#` PROHIBITION -- THE ONE PROHIBITION THE CONTRACT DOES STATE EXPLICITLY, AND
THE ONE R-OG-21's WHOLE ARGUMENT RESTS ON.** A seat striking "one line off" in the other direction would have retired
the `POLICY#`-side prohibition **by the act that depends on it surviving.** `2.0.0_SA_COO~O` scoped its edit to `:183`,
asserted `:184`'s survival BEFORE writing and verified it AFTER; `:184` is untouched.

⭐ **AND THE FAILURE IS THE EXACT ONE RULE 27 NAMES AND R-73 RECORDED, COMMITTED BY THE SEAT THAT RECORDED IT: I PRINTED
THE BYTES OF A RANGE (`sed -n '178,190p'`) AND THEN TYPED A SINGLE LINE NUMBER OFF MY MEMORY OF THAT RANGE.** The quoted
TEXT was correct, so every check I ran on the quote passed. **A range read does not verify a point citation** --
"print the bytes at the cited line" means at THE LINE, singular, after the number is written.

⛔ **CORRECTION 2 -- MY SECOND "FINDING" IS WITHDRAWN IN FULL.** R-OG-21 said *"there is NO TransactWrite anywhere in
that file"* and inferred a decomp that *"over-grants on paper where the TF under-grants."* **Both halves are wrong.**

- **The token IS in the file.** My census was `grep 'dynamodb:'` -- scoped to `dynamodb:`-PREFIXED tokens -- and I then
  wrote a sentence about *"anywhere in that file."* ⛔ **THAT IS RULE 24's SCOPE-TELL: A DENOMINATOR WHOSE SCOPE IS
  NARROWER THAN THE SENTENCE BESIDE IT** -- the identical defect I spent the `LGIC_ENFORCE` round-8 analysis
  correcting, committed roughly three hours later, in a ruling, by me.
- **And the substance is a CATEGORY ERROR, which is a better reading than mine.** There is **no
  `dynamodb:TransactWriteItems` IAM action at all**; a transaction is authorized PER ITEM against `PutItem`/`UpdateItem`.
  `probes/og_i1.py:33` states it and **MEASURED it**, grading "TransactWrite" on those constituents under the
  `LeadingKeys` condition as row `NFRA_OPLGTW-W1-S3`. ⭐ **So the cell had already handled it correctly, `DECOMP:183`
  names a CAPABILITY rather than an action, and there was never a two-directional error to find.** My warning that
  *"if a later cell relies on TransactWrite being granted, it is not"* is withdrawn as misleading: such a cell would not
  be under-granted, it would be naming something no IAM policy can grant.

⚠ **ONE FIGURE IN THE CORRECTION ITSELF DOES NOT RECONCILE, AND IT CHANGES NOTHING.** 98010 reports `TransactWrite`
*"four times, all in COMMENTS, at `:19-21` and `:27-28`."* Measured by this seat at BOTH vintages -- `86177bf020^` and
HEAD -- **the literal token occurs exactly ONCE**, at `:21`, inside the sentence stating the IAM action does not exist.
**The substance of 98010 is right and mine was wrong; its count is the same class of error as the one it is correcting.**
Recorded because a later seat re-deriving "four" will not find it.

**WHAT STANDS FROM R-OG-21, UNCHANGED:** the ratified contract permits a conditional delete on `RUNTIME#` and forbids
ordinary delete on `POLICY#` only; `OGI1-AC5` is retired prospectively and `OG-i-1`'s grade stands under R-43; the
`LeadingKeys` confinement; the standing bar that **a criterion asserting a permission is ABSENT must name the call sites
that would need it**; and that `OGI1-AC5` did not merely miss the defect but CERTIFIED it. `2.0.0_SA_COO~O` accepts that
bar and the health-check finding without reservation.

⛔ **ONE CLOCK REMAINS OPEN AND IT IS NOT THE IAM ACTION: NO REAL END-TO-END LOGIN HAS BEEN OBSERVED SINCE THE FIX.**
The IAM action is exercised; the `/callback` path is not. Disarm condition, readable via SSM with no identity read: the
journal shows one `GET /callback` answering 30x then one `POST /token` 200 after 16:37Z. Andrew is the expected producer
(reconnect from Claude). `NFRA_OPLGTW-S46` @`5efdc94d2f` carries it, disarm owner `2.0.0_SA_COO~O`. **The act is proven
at the permission and UNPROVEN at the outcome, and those are different claims.**

---

## R-OG-22 -- CALL 1 (AC4): the REC is adopted AGAINST raising the cap, but the call offers a FALSE BINARY and the third branch is the one the measurements actually point at

**The call:** the contract asks 250,000 rows / 50 MiB per export; the job cap is `job_memory_bytes = 268435456`. The measured export peaked at **270,581,760** and ended `LIMIT_EXCEEDED`. The largest export that COMPLETED was **62,500 rows / 9,468,970 bytes at 214,065,152 peak RSS**. `2.0.0_SA_COO~O`'s REC: a PRD revision lowering `export_rows`/`export_utf8_bytes` to a measured-achievable pair, rather than raising `job_memory_bytes`.

### The half of the rec I adopt outright

⛔ **`job_memory_bytes` DOES NOT MOVE.** The rec's reason is correct and it is the blast-radius reason: the cap is a **multi-tenant ADMISSION parameter** on a 1,936,322,560-byte host where two jobs already reserve 912,624,640, while the export size is a **single-feature contract term**. Widening a shared admission parameter to fit one feature re-prices every other tenant's admission -- the wider radius, chosen to fix the narrower problem. That is settled and no revision may quietly take the other route.

### ⛔ THE BRANCH NEITHER THE CALL NOR THE REC NAMES, AND RULE 24 IS WHY I LOOKED FOR IT

The call is framed as a two-member set -- *lower the contract* or *raise the cap*. Rule 24 (i): **hunt the uncovered member, and hunt it by SUBTRACTION.** The domain is not "which of the two numbers do we edit"; it is **every way peak RSS can be brought under the cap at contract scale.** Subtracting the two named members leaves one:

⭐ **CHANGE NEITHER NUMBER -- MAKE PEAK RSS STOP BEING A FUNCTION OF EXPORT SIZE.** And the cell's own measurements are what point there: **9,468,970 bytes of output cost 214,065,152 bytes of peak RSS -- a ratio of about 22.6 to 1.** A writer that streamed rows would not carry that ratio; a resident result set does. **The measured evidence is more consistent with "the whole result set is materialised in memory" than with "the contract is too big."** I have NOT confirmed that read -- it is an inference from a ratio, and I am labelling it as one -- but it is a cheap thing to falsify and it is not in the record at all.

### THE RULING

1. **`job_memory_bytes` stays at 268435456.** Not a revision candidate.
2. ⛔ **BEFORE any contract number is lowered, the revision ANSWERS ONE QUESTION: is 250,000 rows / 50 MiB a CONSUMER REQUIREMENT or an aspiration?** The two answers have different remedies and the record currently supports neither, because nobody has asked. **If a real consumer needs 250k rows, lowering the contract does not solve that consumer's problem -- it relabels it**, and the streaming branch is the only member of the set that serves it.
3. **If it is an aspiration**, the rec lands exactly as written -- and the achievable pair is stated **with margin, never at the observed maximum**: the largest completed run sat at 214,065,152 against a 268,435,456 cap, and a pair pinned to an observed peak has no headroom for the next input that is 5% larger.
4. **The pair is MEASURED, never interpolated.** 62,500 rows completing does not license "125,000 rows probably completes"; the ratio above is the reason that interpolation is unsafe.

**I own the revision (L4) and I am not cutting it this tick** -- it is blocked on question 2, which is a question about a consumer, not about this cell. `2.0.0_SA_COO~O` is not blocked by that: nothing in OG-r-2 waits on the revision.

---

## R-OG-23 -- CALL 2 (AC6): the REVISED rec is adopted, the criterion is NOT weakened, and `2.0.0_SA_COO~O`'s correction of its own call is the finding of this round

**Superseded first:** call 2 as written at 22:11Z argued from "an ambient background rate" to weakening the bar. `2.0.0_SA_COO~O` corrected itself at 22:47Z (msg 98070, row `S49` @`6acc95cba2`) before I ruled, and the correction reverses its own recommendation. ⭐ **I am ruling on the CORRECTED call, and the correction is right.**

### WHY THE ORIGINAL REC WAS WRONG IN A WAY THIS ESTATE HAS A NAME FOR

The first rec rested on a **14-day SUM**. The correction read the same metric **per day-bucket (denominator 15)** and found the events are **EPISODIC**: non-zero on FOUR days (09-04 = 3, 09-09 = 3, 09-10 = 13, 09-18 = 2), **true zeros on ELEVEN** while `RequestCount` is non-zero on all fifteen; at period 3600 they are bursts inside single hours, never a rate.

⛔ **THIS IS RULE 24'S SCOPE-TELL EXACTLY: A REAL DENOMINATOR SUPPORTING A SENTENCE ABOUT A DIFFERENT POPULATION.** A sum over 14 days is a true number that cannot distinguish "irreducible ambient rate" from "four bad days and eleven clean ones" -- and **those two have opposite remedies.** "Ambient" means irreducible, which argues for replacing the bar with a rate comparison. **Episodic means a zero-failure window is CONSTRUCTIBLE**, which is the opposite conclusion from the same instrument at a finer grain.

### THE RULING

1. ⛔ **AC6's literal "zero failures" STANDS. It is not amended, not weakened to a rate, and not given a delta bar.** Eleven clean days of fifteen are the proof that the bar is satisfiable, and **a bar is not unsatisfiable because one cell could not build a window that met it.**
2. **It is graded on a window free of NAMED incidents, each named IN THE RECORD with its cause.** That is the corrected rec and I adopt it verbatim.
3. ⛔ **THE 19 ERRORS OF 09-04 / 09-09 / 09-10 ARE NOT NAMED.** `2.0.0_SA_COO~O` says so itself and declines to claim a cause it did not read. **So those three days are NOT eligible window material until named** -- a window is "free of named incidents" only when the incidents in it have actually been named, and an unexamined burst is not a clean day.
4. **Today's two ARE named and ARE ours:** the 14:00Z and 15:00Z buckets correspond to `GET /callback` 503s at 14:55:37Z and 15:16:07Z during the `DeleteItem` outage (row `S46`, a different plane, same two events). ⭐ **Two instruments, independently derived, agreeing on the same two events is CORROBORATION rather than repetition** -- the CloudWatch metric and the journal read share no method. 09-18 is therefore an eligible day for a window that EXCLUDES the outage interval, and a named incident of our own making is precisely what the clause is for.
5. **Row `W2-S10` stays ARMED and its disposition remains the CVO's at L9.** Its core claim -- *the criterion is unsatisfiable in the windows THAT CELL could build* -- is TRUE and is not disturbed by this ruling. ⚠ **It is a claim about the cell's windows, not about the criterion**, and the two must not be collapsed when the row is dispositioned.

⭐ **RECORDED AS CREDIT, NOT COURTESY:** a seat that re-measures its own recommendation at a finer grain and publishes the reversal before the ruling lands is doing the thing the correcting-seat trap says is hardest. The correction cost one metric call and changed the remedy.

---

## R-OG-24 -- CALL 3 (AC2): the rec is adopted -- the bar IS "never exceeds", so the PASS is VACUOUS -- and the defect is in a SHARED LIMB, which makes it bigger than AC2

**The call:** `onhost_bench.py:418-421` grades `cap_respected` by comparing RSS **only when the job succeeded**; a job ending `LIMIT_EXCEEDED` is graded `True` with its RSS unread. The maximal job peaked at **282,021,888** against the **268,435,456** cap -- 5.06% over -- and PASSES, while AC4's export job FAILS at a SMALLER 270,581,760 only because AC4's text also demands the CSV be generated.

### THE RULING

1. ⛔ **AC2's BAR IS "NEVER EXCEEDS." The PASS IS A DISCLOSED FAIL.** Adopted as recommended.
2. ⛔ **AND IT IS WORSE THAN AMBIGUOUS -- IT IS VACUOUS.** A limb that reads the guarded property **only on the success path cannot return non-zero on the positive case it exists to catch**: the jobs most likely to breach a memory cap are exactly the jobs that die of it. This is the catalogued *detector that cannot fire* shape, and the verdict it produces is not evidence of compliance in either direction.
3. ⭐ **THE DEFECT IS IN A SHARED LIMB, SO THE SCOPE IS NOT AC2.** Rule 22: *a check scoped to the members cannot see a defect in what the members share.* **Every criterion whose verdict reads `cap_respected` inherits this, and each one currently reads PASS or FAIL on a limb that is blind on the failure path.** ⛔ **CENSUS `cap_respected`'s CONSUMERS BEFORE ANY OF THEM IS QUOTED AGAIN, AND PRINT THE DENOMINATOR.** I am not naming a count, because I have not run it and a number I did not measure is exactly what this ruling convicts.
4. **The instrument is repaired, not worked around:** `cap_respected` reads peak RSS on **every** terminal path, `LIMIT_EXCEEDED` included. A grader that must be read together with a caveat is a grader that will be quoted without one.
5. **Admission arithmetic is priced against transient overshoot**, as recommended -- a child that transiently reaches about 1.05x the cap.

### ⚠ ONE NUMBER IN THE CALL DOES NOT RECONCILE, AND IT IS CHEAP TO FIX

The call says two such children reach **562,036,736** against a reserve computed at 375,753,728. But **2 x 282,021,888 = 564,043,776**, not 562,036,736 -- a difference of **2,007,040**, which means the two figures rest on DIFFERENT child values (562,036,736 is the double of 281,018,368, not of 282,021,888). **Neither is necessarily wrong** -- one may be the measured maximum and the other a different run's peak -- **but the doubling must print its own input.** ⛔ **The conclusion is unaffected: on either figure two children exceed the 375,753,728 reserve by more than 185 MB**, so the admission finding stands and this is a provenance repair, not a reversal.

**Nothing here re-grades a criterion or moves a cap.** AC2 becomes a disclosed FAIL and joins AC4 as the second input to R-OG-22's revision; the `cap_respected` repair and its consumer census are `2.0.0_SA_COO~O`'s to place in a cell.

---

## R-OG-25 -- THE LOST SALT (row `S42`): the RE-SEAL IS ORDERED NOW and **`G-C` IS NOT SCHEDULED UNTIL IT LANDS** -- plus the falsifiable ordering test, because a late re-seal and an honest one look identical in the record

**The finding (`2.0.0_SA_COO~O`, row `NFRA_OPLGTW-S42` @`28f12de3b0`, ARMED and BLOCKING):** `SEALED_EXPECTED.json` is committed at HEAD and names its own missing input -- `sha256(salt || canonical_json(answer))`, salt at `C:/tmp/nfra-oplgtw-sealed/expected/SALT.txt`, **outside the repository. The tree does not exist.** Measured on two independent path planes (bash `test -d` ABSENT, PowerShell `Test-Path` False) while `C:\tmp` itself holds 36 children, none matching `nfra*`. `OG-v-3` put the values and the salt there and nowhere else, with retention *"until OG-v-4 has graded"*; `OG-v-4` has not graded, **so the tree went EARLY -- before the clause governing it allowed.**

Blast radius **ONE criterion** -- `OGV4-AC5` -- after `2.0.0_SA_COO~O` corrected its own sweep from 2 to 1 (the `OGV4-J2` hit was its own regex catching a trailing `<expected_criteria>` list). ⭐ **The correction is in the right direction: it made the finding SMALLER, which is the direction a seat has no incentive to move its own number.**

### 1. THE RULING ON THE PART THAT IS MINE -- `G-C`'s TIMING

⛔ **THE RE-SEAL IS ORDERED, AND `G-C` IS NOT SCHEDULED UNTIL THE RE-SEAL COMMIT HAS LANDED.**

The reasoning is entirely `2.0.0_SA_COO~O`'s and I adopt it without dilution: the seal exists so the grader cannot tune expectations to the result. **A re-seal TODAY preserves that property exactly, because the walkthrough has not happened** -- `G-C`, `G-D`, `G-E` and `G-F` are all absent at HEAD, verified this tick, all four owning deliverables directories at 0 files. **The same re-seal AFTER the walkthrough would be worthless.**

⚠ **THIS IS A SEQUENCING ORDER ON TWO ACTS THIS SEAT ALREADY OWNS, NOT A NEW APPROVAL GATE.** CLAUDE.md forbids implementing an approval gate Andrew did not ask for. Nothing here adds a permission step: `G-C`'s timing was already mine, the re-seal was already owed, and I am stating which comes first. No seat needs anyone's sign-off that it did not need yesterday.

⛔ **AND IF THE ROUND'S ARITHMETIC CANNOT DRAIN IN TIME, `G-C` IS WHAT MOVES, NOT THE RE-SEAL.** `2.0.0_SA_COO~O` declined to cut the cell in-round on LD-0521's arithmetic -- *"I am not going to argue the exception into existence for my own finding"* -- and that restraint is correct and is not to be undone by me. **The window is protected from the other end: I hold `G-C`, so I delay `G-C`.**

### 2. ⛔ IT IS A RE-SEAL, NOT A RECOVERY, AND THE RECORD MUST NEVER READ OTHERWISE

`SEALED_EXPECTED.json` records key AND `version_id` for every source object plus the exact instrument, so **the ANSWERS recompute from identical versioned objects.** ⛔ **THE COMMITTED HASHES CAN NEVER BE MATCHED** -- a new salt yields different digests. Any repair produces **NEW hashes**.

So: the new artifact **supersedes** the old and says so in its own bytes, naming the old digests as **RETIRED, never as "verified"**. ⚠ **A future reader who finds two sets of digests and no supersession note will assume the first set was checked.** The retirement line is the only thing standing between this incident and that misreading.

### 3. ⭐ THE ORDERING TEST -- because "we re-sealed before the walkthrough" is a CLAIM, and the whole point is that it cannot be taken on trust

An honest early re-seal and a worthless late one **look identical in the record**, which is exactly the property the seal was built to deny. So the re-seal carries a discriminator a later reader can run without trusting anyone:

**The re-seal commit MUST be a git ANCESTOR of the first commit in `G-C`'s deliverables directory, and the row cites BOTH hashes.** Falsifiable in one command (`git merge-base --is-ancestor <reseal> <first G-C artifact>`), by any seat, at any later date, on an ordering **no party to the grading can back-date.** ⛔ **A DATE TYPED INTO THE ARTIFACT IS NOT THIS TEST** -- the artifact is written by the party that benefits; the ancestry is not.

### 4. THE STANDING BAR THIS EARNS -- `2.0.0_SA_COO~O`'s carry, sharpened

Its generalisation is right and is the durable part: ⭐ ***"AN OUT-OF-REPO INPUT SITS OUTSIDE EVERY GUARD THIS ESTATE HAS."*** No gate, no freeze, no worktree and no commit protects `C:/tmp`, **and a held cell depending on one is trusting a path nothing defends for exactly as long as it stays held** -- which is longest precisely when a cell is blocked, i.e. when nobody is looking.

⛔ **BAR: AN INPUT A HELD OR SEALED CELL WILL NEED AT GRADING TIME LIVES IN A DEFENDED STORE WITH A NAMED RETENTION OWNER -- NEVER A TEMP PATH.**

⚠ **AND THE OBVIOUS REMEDY IS WRONG HERE, WHICH IS WHY THE BAR NAMES A STORE RATHER THAN "COMMIT IT":** committing the salt in clear would destroy what the salt buys. The hashes' integrity comes from the COMMIT (they were fixed before the answers were known), but **the SALT's secrecy is what stops a low-entropy answer being brute-forced out of its own digest** -- and this seal's answers are business-date-shaped, i.e. low entropy. A published salt would let a party recover the expected answer from the committed hash and then build to return it, which inverts the threat rather than closing it. **So: an Opal-owned defended store (SSM SecureString / Secrets Manager), never the repo in clear and never `/tmp`.** COST: one parameter write per seal. NON-APPLICATION: an input a cell consumes and grades in the same act, which is never held.

### 5. WHAT IS NOT CLAIMED

**Nothing about WHAT removed the tree.** A temp sweep, a reboot, a cleanup -- unmeasured, and `2.0.0_SA_COO~O` declines to claim it. ⭐ **The remedy does not depend on the cause, which is why the ruling does not wait for it.** And per Rule 22's negative mirror: this is an **EXPOSURE that FIRED** -- the guard was missing AND the loss occurred -- so it is an INCIDENT, and the re-opening it requires is exactly `OGV4-AC5`'s re-seal. Nothing else was admitted by the gap, because `OG-v-4` never graded.

---

## R-OG-25A -- CORRECTION TO R-OG-25, BY THIS SEAT: **I ORDERED AN ACT THAT HAD ALREADY LANDED, AND HELD `G-C` ON A PRECONDITION ALREADY MET.** `G-C` IS RELEASED

**`G-C` IS SCHEDULABLE NOW.** The hold R-OG-25 placed on it is LIFTED, and it was never correctly placed.

### 1. WHAT I GOT WRONG

R-OG-25 (23:24:57Z) ordered a re-seal and held `G-C` until the re-seal commit landed. **The re-seal landed at 13:53:17Z the same day -- nine and a half hours BEFORE the ruling was written.**

Verified on this seat's own instrument, not on the report that told me:
- `git log -1 d5af54a90a` -> `2026-09-18T09:53:17-04:00` (= **13:53:17Z**), author `2.0.0_SA_COO~O`, *"drain: merge wk-oplgtw-6-reseal (row gate clean on the merged index)"*
- `git show --stat d5af54a90a` -> carries `.../0.9.0_WK_NFRA_OPLGTW~6/SEALED_EXPECTED.json` (+36/-6) and `probes/og_v4.py` (+177)
- `git merge-base --is-ancestor d5af54a90a HEAD` -> **true**

⛔ **THE DEFECT IS MINE AND IT IS NOT "THE ROW WAS STALE."** `2.0.0_SA_COO~O` offers me that exit -- *"the ruling reasons from row S42 as filed at 12:22Z and could not see a remediation that landed after it"* -- and **I decline it, because it is not what happened.** The row was filed at 12:22Z; the remediation landed at 13:53Z; **the message carrying the row to me quoted a push state read at 17:57Z**, and I ruled at 23:24Z. The information needed to catch this was available for nine hours and the check costs one `git log`.

⛔ **I RULED ON A BLOCKING CLAIM ABOUT THE WORLD WITHOUT MEASURING THE WORLD.** Rule 22 sizes verification by who eats the error: an ORDER to another seat is the world axis, which requires DISCRIMINATION -- *could the evidence differ if the claim were false?* I ran no check that could have come back "already done." **This is the same shape as the open-deploy-entry rule I cite in my own rulings:** *an entry a device left OPEN proves only that THIS device saw no completion -- before acting on any open entry, MEASURE THE ARTIFACT.* An ARMED row is exactly such an entry. ⚠ **A row's ARMED state is the FILER'S claim at FILING TIME, and it does not age with the world.**

### 2. THE COST, STATED PLAINLY

`G-C` is, in `2.0.0_SA_COO~O`'s words, *"the last non-spec gate between round 1 and its close."* **I held it from 23:24Z on a condition that was already satisfied.** Nothing else was damaged: the re-seal was not re-run (the lane read the ruling correctly and reported rather than re-executed), and no act was taken twice.

⭐ **AND THE HOLD WAS THE ONLY WRONG LIMB.** The ancestry test and the standing bar were not wasted, and I am not retracting them:
- **The ancestry test is SATISFIED BY CONSTRUCTION, which is stronger than satisfied by promise.** `d5af54a90a` is already in `CLOUD`'s history, so **every future commit in `G-C`'s deliverables directory necessarily descends from it.** Nobody can back-date around that -- the test needs no further act by anyone, ever.
- **The standing bar was being violated AS I WROTE IT, and worse than I knew.** `C:/tmp/nfra-oplgtw-sealed/expected/` held `SALT.txt` **and `RQ1..RQ6.txt` -- the six REAL ANSWERS in clear.** ⛔ **That is the worse half and my ruling did not see it: the salt only protects the DIGESTS; the answer files were the answers themselves, undefended.** All seven now sit in SSM SecureString under `/opal/nfra_oplgtw/ogv4/reseal_20260918/`, read back with `--with-decryption` and compared by sha256 against the local bytes, **7 of 7 MATCH**, with no value reaching a transcript, log or commit -- only names, byte lengths and hash-equality booleans. Retention owner: that lane, until `OGV4-AC9` commits them as drain evidence. **Temp copies deliberately NOT deleted, and that judgment is correct**: the probe still reads that path, and deleting the working copy before the cell is re-handed would repeat `S42` from the other direction.

### 3. WHAT BINDS NOW

1. ⛔ **`G-C` IS RELEASED AND SCHEDULABLE ON THE EXISTING EVIDENCE, NOT ON A NEW ACT.** No further re-seal, no further verification, no new gate.
2. **R-OG-25's standing bar STANDS** (an input a HELD or SEALED cell needs at grading time lives in a DEFENDED store with a named retention owner, never a temp path) -- now with the sharper statement that **the bar covers the ANSWERS, not merely the salt.**
3. ⭐ **THE CHECK THIS EARNS, AND IT COSTS ONE COMMAND: BEFORE ORDERING AN ACT ON THE STRENGTH OF AN ARMED ROW OR AN OPEN ENTRY, MEASURE WHETHER THE ACT IS ALREADY DONE.** COST: one `git log` / one artifact read. NON-APPLICATION: an order whose act is inherently unrepeatable-by-others, or a row filed and ruled inside the same tick.

⚠ **AND THE ROUTE MATTERS MORE THAN THE ANSWER HERE:** R-OG-25 reached a defensible bar by a method that could equally have ordered a second re-seal on top of a good one. **A right answer reached without the discriminating check is a lucky one**, and it is the route that gets graded.

---

## R-OG-23A -- CLARIFYING MY OWN CLAUSE BEFORE IT IS GRADED ON: **NAMING AN INCIDENT DOES NOT MAKE ITS DAY COUNTABLE AS CLEAN.** The window is CONTIGUOUS and a named incident DISQUALIFIES it

`2.0.0_SA_COO~O` discharged R-OG-23 s.3's naming obligation completely (`S52` @`5f57597894`), and the row is better
than the obligation required: retention checked FIRST so a zero would have meant zero; **19 of 19 on one endpoint,
zero exceptions**, enumerated to the second; corroborated across two instruments sharing no mechanism (journal vs
the ALB metric in `S49`); the cause pinned at the minute (`/graph/health` 200 beside `POST /graph/cypher` 502, retry
200 six seconds later -- a swap window on the graph store); and an explicit statement of what it does NOT claim.
**The naming obligation is CLOSED.**

⚠ **BUT THE ROW READS MY CLAUSE ONE WAY AND I MEANT THE OTHER, AND THE DIFFERENCE DECIDES A GRADE.** It writes
*"the three days become eligible window material."* My clause was *"graded on a window free of NAMED incidents."*

⛔ **"FREE OF NAMED INCIDENTS" MEANS THE WINDOW CONTAINS NONE -- NOT THAT THE ONES IT CONTAINS HAVE BEEN LABELLED.**
Naming was never a way to make a dirty day usable. It was the check that a day called clean is clean *because
somebody looked*, not because nobody did -- an unexamined burst is not a clean day, and a named burst is not one
either. **A named incident DISQUALIFIES any window containing it.**

### ⛔ AND THE READING I AM REFUSING IS THE ONE THAT DESTROYS THE BAR

If naming let us excise an incident's minutes from inside a window, **"zero failures" would be satisfiable over ANY
data by excising every failure** -- the bar would measure nothing but our willingness to name things. That is
exactly the shape the skill's own stop-condition clause forbids: *a condition satisfiable by shrinking its own
denominator is not a condition, and the party doing the shrinking is the party that benefits.* **I kept the literal
bar in R-OG-23 against a rate; I am not now reintroducing the weakening through the window's edges.**

### ⭐ AND NOTHING IS LOST BY THE STRICT READING -- A QUALIFYING WINDOW ALREADY EXISTS

From `S49`'s own day-buckets, non-zero on **09-04, 09-09, 09-10, 09-18**; the other eleven of fifteen are true
zeros. The contiguous clean runs are **09-05..09-08 (4 days)** and **09-11..09-17 (SEVEN days)**.
⭐ **So `OGR2-AC6` can be graded on a seven-day contiguous window with the literal "zero failures" bar intact, no
excision, no attribution argument and no judgment call.** The strict reading costs the round nothing.

**So `S52`'s operative sentence is right and its label is loose:** the round-2 cell grades AC6 on a window that
**EXCLUDES** the graph-swap days and the 09-18 outage -- which is what the row actually describes doing. I am
correcting the phrase *"eligible window material"* only so the next reader does not take it as licence to include
those days with a footnote.

**Unchanged:** the AC6 re-grade is round-2 work and is not performed here; `W2-S10` stays ARMED with its disposition
the CVO's at L9; and its core claim -- unsatisfiable in the windows THAT CELL could build -- remains true and
remains a statement about that cell's windows, not about the criterion.

---

## R-OG-23B -- `2.0.0_SA_COO~O` RAN THE CHECK MY RULING DID NOT: **a clean window with no TRAFFIC passes vacuously, and R-OG-23A asserted its span from the failure series alone**

R-OG-23A claimed a seven-day contiguous clean window (09-11..09-17) exists, **derived entirely from `S49`'s
failure-count day-buckets.** ⛔ **A FAILURE SERIES CANNOT DISTINGUISH "NO FAILURES" FROM "NO TRAFFIC."** I asserted
a window was usable without ever asking whether anything happened in it.

**`2.0.0_SA_COO~O` measured the missing half** (CloudWatch, the same dimensions as `S49`, period 86400, seven
buckets): **RequestCount 3323, 1123, 1142, 4309, 2778, 5017, 1781 -- every bucket NON-ZERO, total 19,473
requests** -- against **HTTPCode_Target_5XX_Count: NO DATAPOINTS** over the identical span.

⭐ **So the span is clean AND loaded, and the ruling stands -- but it stood on evidence it did not have until now.**
`OGR2-AC6` is gradeable on 09-11..09-17 with the literal bar intact over 19,473 real requests.

### THE DEFECT WAS MINE AND IT IS CATALOGUED

This is *a gate called with an EMPTY input set returns a vacuous pass that reads as clean*, moved up one level from
a gate's input to a **measurement window**. ⚠ **I have cited that trap at other seats; I did not apply it to my own
window claim**, and the tell was available the whole time -- **a denominator I never printed.**

### THE BAR, WHICH IS `2.0.0_SA_COO~O`'s AND IS BETTER THAN A CORRECTION

⛔ **A CLEAN-WINDOW CLAIM PRINTS TWO NUMBERS: THE FAILURE COUNT AND THE TRAFFIC DENOMINATOR.** One extra query.
⭐ **And the symmetry is the point, in that lane's own framing: a bar can be weakened at its WINDOW'S EDGES without
ever touching the bar, and the strict reading that closes that hole opens its mirror** -- excision makes any window
clean, and emptiness makes any window clean. **Both are answered by printing the denominator beside the zero.**
**NON-APPLICATION:** a claim whose subject IS the traffic (there the denominator is the measurement).

**Unchanged:** the AC6 re-grade is round-2 work; `W2-S10` stays ARMED, disposition the CVO's at L9.
