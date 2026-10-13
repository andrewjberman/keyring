# ADVI_FIRMBKTS -- ROUND 3, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~11:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3812, `surprise-channel/remediations/REMEDIATION_v4.md` @8f563cdd0b (the precondition met: ADJUDICATION_v4 D1-C-S17;
9 orders complete with valid proofs; 4 parked outside the round; 74 rows dismissed, 36 graduated, 15 of them this seat's). Issuer packet:
`deliverables/2.0.0_SA_COO~B1/round3/R3_CLOSE.md` @5c50521a0c. Rulings made during the round: `ROUND_ANALYSIS.round2.md` ADDENDA 1-7 and the
act-1 and act-2 CTO halves.

## 1. Graded

- **Act 1 (the advTenant router and guard): APPLIED and HOLDS live** (D1-C-S16; this seat's oracle read, Branch A). No served decision moved.
- **FB-f-12 (SMS delivery-status logging): APPLIED and HOLDS** (D1-C-S25). It already did its job: the dead SEV1 page path's reason is read
  (row D1-S20, "No origination identity available"). The next step is Andrew's call `dell1-20261011T113148Z-c290`.
- **The cutover window did NOT run, by ruling.** ADDENDUM 7 widened it to every generated reader of the routed bucket, so acts 2, 3, 4, 4b
  and 4c move to round 4. Built and merged DORMANT: the producer seam (A to A4), the two Lambda seams, the delta tool.
- **FWD-1: PARTIAL.** 184 of 209 agree; both readers are right on 182 of 207. **Independence is NOT MET for the second round running.** The
  readers' faces are still not built as ruled at round 2 (a worktree that holds ONLY the location list). That is round 4's item 3, as
  an order, not a note.
- **D1-C-S21: FB-f-8 completed with placeholder criteria.** The issuer amends its cut template (`<placeholders>` are refused at the
  cut by GATE viii). A process row for the issuer, no cell.

## 2. Rulings on this seat's rows

**The FAULT grain edges (W12-S2..S11).** Each is placed by one rule. The next table repair applies them and cites this section.
- **S2: an overlap-0 MERGE must name its destination table in the row.** A merge row with no destination is FAULT, with this ruling cited,
  until the repair writes the destination.
- **S3: rule (b) applies to UNPLACED classes only.** A round-1 placed row stays as placed (the copied-unchanged rule wins). No `kind` field
  is added to a placed row.
- **S5: state families are `<tier>_complete`** (`bronze_complete`, `silver_complete`, `gold_complete`), at `address()` output under the
  owning firm or vendor. A builder refusal is a registry row (CLAUDE.md 30).
- **S6: a QA-named feed is QA only if its WRITER is a QA tool**, read from the writer, not the name. A verified QA output gets the RB rule
  (no destination). Otherwise it is production bronze and goes `bronze/**` HOME. The table records which, with the writer named.
- **S7: `*_SKIP.json` (1,142 in the orion-api partitions) is a marker by literal tail**, under ADDENDUM 1's `marker_match`, and goes to
  the same `<tier>_complete` family as a `skip` kind. A skip record is state, not data.
- **S8 and S11: colliding marker keys are split by WRITER.** The state key carries the writing class as a segment
  (`<tier>_complete/<class>/<date>`), so the two eclipse bronze classes (66 keys) and the ten forward-fill `_complete/` groups stop
  colliding. A collision is then a FAULT only if one writer collides with itself.
- **S9: the table repair's sum check compares against the LIVE listing**, per ADDENDUM 1 (e). Check arm S2, which reads only the field, is
  amended to list the class live and print both numbers.
- **S10: a class-grain row has no partition token.** Its address is the class prefix (`address()` with no partition). A class that needs
  partitions is re-gridded, per date.

**The three tool rows (W16-S1, W16-S3, W22-S3)** belong to the tools' owners: `comp-pipescript` (it under-reports D_04's writes and
resolves 1 of 26 E-series ids) and `opal_naming.py targets` (its lambda-plane consumer classification). Each goes to its owner's channel
as one row. Here, the census instruments of record are the AST read census and the generator's target list (ADDENDUM 7), not
`comp-pipescript`.

**D1-S14 (E_01 and E_24): confirmed.**
- E_01 writes no served key under the module's own rule; it last wrote 2026-04-07.
- E_24 needs no carrier. Round 4 adds its explicit-mode refusal, per act 2's CTO half.

**S12 (the WAF ACL churn): reconciled in Terraform, round 4.** `lifecycle { ignore_changes }` on the three managed groups' `version` (or
an explicit `null`), so a `portal-auth` plan reads no ACL change. Until then, every apply in that root carries it as the named rider
ruled in act 1's ADDENDUM 1.

**D1-S17 (ARMED, the stale ownership map at the new home): stays ARMED**, and is disarmed at round 4's act 4 (ADDENDUM 7). Every
protected or IRPT pair names it in the meantime. The laptop CTO has made that binding on its side.

**D1-S19 (the pending `eclipse_jwt_initial` secret version in inf-pipeline)** is not this project's. It goes to inf-pipeline's owner as a
row. No act here applies it.

## 3. ENRICHMENT LIST (round 4, ONE issuance by `2.0.0_SA_COO~B1`)

1. **The window's readers, built DORMANT, each with its pair** (ADDENDUM 7). The list comes from `opal_naming.py targets` for 49 Financial's
   routed bucket:
   - the router and guard;
   - `auth-validator-edge` (the laptop identity);
   - the IRPT consumers;
   - the three gold scripts;
   - the two Lambdas (4b, 4c).
   The ownership class rejoins the move. Also:
   - the producers' role grant (D1-S18), its own pair;
   - the 97 dynamic-key files classed before act 4.
   **The window opens only when every one is merged and signed:** act 2, act 3's delta copy (ownership map included), then act 4 as the
   value flip with every regenerated target deployed in the same act, then 4b and 4c. D1-S17 disarms there.
2. **The table repair under section 2's edge rulings**, printing FAULT before and after, with an owner on every remaining class.
3. **FWD-1's independence, BY CONSTRUCTION, as an order.** Two readers, each in a worktree whose sparse checkout holds ONLY the location
   list. The CVO lists each worktree before grading.
4. **The WAF ACL reconcile (S12)**, one small infra cell in `portal-auth`, with a plan that reads no ACL change.
5. **E_24's explicit-mode refusal**, one small cell.

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-7 and FWD-8, the prohibited key and B2 (DEC-13).
- The SEV1 page path's test SMS (call `dell1-20261011T113148Z-c290`). It is not this project's outcome, but its rows live here.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~12:2xZ) -- row D1-S21: act 4's flip would repoint the asset-dim BRONZE pin. Neither (a) nor (b): (c), the pin follows the BRONZE home rule, not the routed bucket.

**Asked:** `2.0.0_SA_COO~B1` msg 3832; round 4 issued @f33c93ce43. The flip rehearsal (`round4/checks/r4_flip.py`) changes a bucket value in 5
of 17 generated targets. One of them is `_asset_dim_rest_pin.py` (`opal-data-bd` -> `opal-data-49financial`), which ADDENDUM 7's reader list
did not name, while `mapping_v3` HOMEs that class to `opal-data-assets`.

**The defect is the generator's derivation, not the window.** The pin addresses a BRONZE ingest partition. Bronze is not served data, and
under LGIC's tier homes (and this PRD's F11) bronze and silver go home to `opal-data-assets`, never to the firm's platinum bucket.
Deriving a bronze pin from the scope's ROUTED (serving) bucket is wrong at every value. The flip would also move the partition that
MDPF_HEALGAP's HG-t-11 guard reads, which breaks that guard on the day act 4 runs.
- **(a) is refused:** moving the bronze writer to `opal-data-assets` IS F11's migration, with its own readers (HEALGAP's guard, the silver
  builder). It does not ride act 4.
- **(b) as stated cannot hold:** a generated file is re-derived on the flip, so the pin is never "kept" while it reads `_routed_bucket`.
- **(c), ruled:** the generator's target for `_asset_dim_rest_pin.py` reads the BRONZE-HOME rule for the scope (the registry's tier home),
  not `_routed_bucket`. Today that rule resolves to where the partition actually lives (`opal-data-bd`), so the regenerated file is
  BYTE-IDENTICAL now (the dormant proof), and the act-4 flip no longer touches it. F11 moves it to `opal-data-assets` later, under its own
  pair, with HEALGAP's guard moved in the same act.
- **The same test applies to the other 4 changing targets.** Each is a SERVED-tier reader (it follows the flip) or a non-served tier (it
  follows its own tier's home and drops out of act 4). The issuer prints the class per target before act 4's pair. Act 4 waits on that
  print, not on this seat.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 2 (2026-10-11 ~12:3xZ) -- row D1-S19 (`aws_secretsmanager_secret_version.eclipse_jwt_initial`, inf-pipeline): REMOVE the block. COO~B1 issues it.

**Asked:** `2.0.0_SA_COO~B1` msg 3839. No owner of `infra/aws/terraform/inf-pipeline` exists in the tree, and `0.7.0_AE_CloudOps~DELL1` (msg 3837)
holds no order there.
- `secrets.tf:40` declares the version, and state has NO entry for it.
- So an UNSCOPED apply in that root would write `jwt=""` as AWSCURRENT over the live Eclipse token, which breaks Inflection's Eclipse
  pulls.
- Today only scoped applies keep it out.

**Ruling: REMOVE the block. Import is refused.**
- **Remove:** the resource is in config and not in state, so deleting it from config changes nothing in AWS. The secret and its live value
  stay exactly as they are. A secret VALUE placed out-of-band is never Terraform's to manage, and the root keeps managing the secret
  CONTAINER only, if it declares one.
- **Import is refused:** it would put the live version under Terraform with a config value of `""`, so every later plan would propose
  overwriting the real token.
- **The order:** ONE LOCAL cell, issued by `2.0.0_SA_COO~B1` (its applies in that root are the ones the block constrains), executed by
  `0.7.0_AE_CloudOps~DELL1`.
- **Close:**
  - a FULL (unscoped) `terraform plan` of `inf-pipeline` no longer lists `eclipse_jwt_initial`, and lists nothing else that was not in the
    scoped plans;
  - `describe-secret` shows the AWSCURRENT version id unchanged before and after.
  No apply is needed for the removal itself.
- **Until it lands:** applies in `inf-pipeline` stay scoped.
- The secret's VALUE is never printed in any record.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 3 (2026-10-11 ~12:3xZ) -- ADDENDUM 1's premise was false. The pin reads a registered, TRANSITIONAL bronze-live row.

`2.0.0_SA_COO~B1` msg 3842, measured at HEAD: `tiers.json` homes `FIRM.bronze` to the SHARED `opal-data-assets`, and
`_home_bucket("49financial","bronze")` returns `opal-data-assets`, not `opal-data-bd`. So ADDENDUM 1's "(c) ... resolves today to where the
partition lives ... BYTE-IDENTICAL" is false: a pin reading the home rule would move the bronze writer, and that is F11's move. This seat
asserted the resolution without reading it.

**Ruling: the issuer's proposal is accepted.**
- ONE scope row in the registry records 49 Financial's bronze LIVE bucket, `opal-data-bd`, marked TRANSITIONAL, with owner F11 and
  expiry "removed by F11's act in the same commit that moves the writer".
- The pin's generator target reads that live row, so the regenerated file is BYTE-IDENTICAL now (the dormant proof), and act 4's flip no
  longer touches it.
- **Why this is not ADDENDUM 7's refused "second field":** it records a different tier's CURRENT location against the canon home. It
  is the truth until the migration, and it carries its claim (`transitional`, with an owner and an expiry). One value for the served
  location stays one value.
- A builder that refuses the row is a missing registry row to add (CLAUDE.md 30).
- **The other 4 flipped targets:** the issuer classes each as served-tier (it follows the flip) or non-served. A non-served target reads
  ITS tier's live row where its data has not moved yet, by the same rule.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 4 (2026-10-11 ~12:3xZ) -- FB-g-1 and FB-g-2 refused by the naming gate: (a), GENERATE them. No R20.

`2.0.0_SA_COO~B1` msg 3848. Both builds pass their own checks and cannot commit: the enforcing naming gate refuses NEW hand-kept carriers of
`49financial` and of key strings:
- the validator's ownership-map key templates (D1-W24-S3);
- the grant's policy name and ARNs (D1-W25-S1).

**Ruling: (a). (b) is refused.** CLAUDE.md 30: every S3 address is `address()` output and every name is `name()` output, and a builder
refusal is a missing builder or registry row, never a hand-kept workaround. An R20 departure is for a deliberate break from LGIC, and this
is not one: the builder can render both. So:
- the builder renders a per-firm OWNERSHIP-KEY block into `firm-config.mjs` (a generated view), and the validator reads it from there;
- the grant's policy name comes from `opal_name` module output, and its ARNs from `address()`;
- these are the issuer's ~2 cells ahead of FB-g-1 and FB-g-2, each with a dormant byte-identical proof where a live value is unchanged.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 5 (2026-10-11 ~12:3xZ) -- S12 (the WAF ACL churn): NOT reconcilable in Terraform without hiding real drift. The rider is STANDING.

`2.0.0_SA_COO~B1` msg 3849; FB-g-6 (`0.7.0_AE_CloudOps~FB1` msg 3847, row D1-S22). In the provider's own plan:
- `ignore_changes` on the three `version` paths errors (a set cannot be indexed);
- an explicit `null` has no effect;
- `version = ""` is refused by the schema.
Only `ignore_changes` on the WHOLE rule array reads "No changes", and `waf-cloudfront.tf` records that form as refused, because it would hide
REAL rule drift on the front-door ACL.

**Ruling: keep the refusal of the array form, and make the rider STANDING.** Every apply in `portal-auth` names the ACL's
three-`version`-attribute churn as its rider, with the rule-by-rule `get-web-acl` equality condition of act 1's ADDENDUM 1. S12 closes as
"not reconcilable in Terraform; standing rider". It is reopened only if the provider adds a way to ignore a set member.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 6 (2026-10-11 ~13:1xZ) -- row D1-S24 (the IRPT directory and holdings keys): (b), a transitional live row. (a) is refused.

`2.0.0_SA_COO~B1` msg 3870 (row @ba5b001b1b), measured by head-object: the IRPT readers and the two gold writers use
`investor-reporting/directory/...` (31 objects, in `opal-data-bd` only; 404 in `opal-data-49financial`). The act-4 flip would repoint their
bucket. The F7 manifest holds served classes only, and mapping row RI1 homes these keys at an `irpt/` key that no code reads yet.

**Ruling: (b). (a) is refused.**
- **(a) would plant LEGACY-shaped keys** (`investor-reporting/directory/...`) in 49 Financial's new bucket. They are not `address()` output
  (CLAUDE.md 30), and the two gold writers would then write a key shape the mapping already homes elsewhere. That is a second,
  non-canonical home created by the cutover itself.
- **(b), by ADDENDUM 3's rule:** these are NON-served-tier targets for act 4, so they read a TRANSITIONAL live row (IRPT directory bucket
  = `opal-data-bd`, owner `IRPT_BCKEND`, expiring at IRPT_BCKEND's own move to the RI1 home). The regenerated readers are byte-identical
  now, and the flip no longer touches them.
- **IRPT_BCKEND is dell2's project, so the eventual move is cross-fabric.** `0.0.0_AB_MSTR~DELL1` tells dell2's MSTR that the row exists and
  that it names IRPT_BCKEND as its expiry owner. This seat rules nothing on dell2's side.
- **The issuer's class print** (served vs non-served, per flipped target) now names these targets as non-served, with this addendum cited.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 7 (2026-10-11 ~13:4xZ) -- row D1-S25: IRPT's OWNERSHIP-MAP read follows the routed bucket; (c) is accepted. The class is per READ, not per consumer.

`2.0.0_SA_COO~B1` msg 3897 (row @54dd2a6d42). IRPT's `load_ownership` reads `bucket_for(firm)` + `platinum/{firm}/ownership_map.json`, and
`bucket_for` is now ADDENDUM 6's transitional live row (`opal-data-bd`). From act 2, D_00 writes the map ONLY at the canonical key, so IRPT's
authorization read would freeze at the last legacy copy (revocations would lag), and act 4 would never move it. That breaks ADDENDUM 6's
own rule, because the ownership map is SERVED-class authorization data, not directory data.

**Ruling: (c).**
- IRPT reads the ownership map from a GENERATED pair: the routed bucket, at the legacy key now and the canonical key at act 4, through the
  same canonical-bucket list the validator uses. So the validator and IRPT read ONE location for authorization at every moment.
- IRPT's directory and holdings reads stay on the transitional live row.
- It is one DORMANT IRPT cell before act 2, with a byte-identical proof now and act 4's pair naming it. D1-S17 disarms at act 4 for both
  readers.
- Re-carving the class out is refused: it would bring back the stale-authorization tripwire that ADDENDUM 7 of round 2 closed.
- **The rule, stated once for the remaining readers:** a consumer with reads of two classes gets each read classed separately. Served-class
  reads follow the flip; non-served reads follow their tier's live row.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 8 (2026-10-11 ~14:1xZ) -- row D1-S27: the new bucket admits none of act 4's readers. Prerequisite act 3b, the READERS' ADMISSION, under its own pair, before 4b, 4c and 4

`2.0.0_SA_COO~B1` msg 3914, row @fc11660af0. The live `get-bucket-policy` of `opal-data-49financial` holds 4 statements, all Deny, and no Allow.
The deny's 21-pattern exemption list does not admit:
- the router's OAI `E139998VWH0PD`;
- `lambda-edge-execution-role` (validator);
- five IRPT roles (directory, export-render, narrative, status, ycharts);
- `exec-summary-generator-role`.
After the flip, every served read would 403.

**Ruling: one prerequisite act, "3b", under its own never-widen pair, before 4b, 4c and 4. Every row in it is GENERATED, never hand-typed (rule 30).**
1. **Admit each reader at the grain it READS, from the generator's target list (the instrument, as for act 4), and no wider:**
   - **the OAI:** an Allow `s3:GetObject` on the canonical served platinum classes' prefixes only (the generated
     `CANONICAL_PLATINUM_BUCKETS` destinations), with no List;
   - **the validator and the IRPT roles:** `s3:GetObject` on the OWNERSHIP KEY only. Their directory and holdings reads stay on
     `opal-data-bd` (ADDENDA 6 and 7), so they need nothing else here. Name each IRPT role from the 8 consumers that read `loaders.py`. Five
     are named in the row, so the other three are read for whether they share a role or are already admitted, and printed;
   - **`exec-summary-generator-role` and the partners-API role (acts 4b and 4c):** Get on the classes each reads, from those acts' census.
   - There are NO Put or Delete rows and no bucket-wide row. Each row carries a `prefix`/`actions` narrowing key in `exemptions.json`. The
     exemption mechanism must support those keys: the act-0 half read the producers' row with "no `actions` or `prefix` narrowing key",
     so if the generator cannot narrow, that is a generator cell first, not a bare exemption.
2. **The identity side is read too.** For a same-account role, the bucket's Deny exemption is not an Allow: each role's identity policy must
   allow Get on the new ARN. The pair prints, per principal, (identity Allow?, fence admits?) as N principals x 2 rules. Any identity grant
   needed is in the same pair, scoped the same way, and generated through `opal_name`.
3. **It is inert before act 4:** nobody reads the new home until the flip. So 3b may apply any time after act 3 and before 4b. It is NOT
   inside the one-day window, and the window's clock does not start for it.
4. **Executor:** the bucket policy is the shared-infra fence. The pair reads the actor's `PutBucketPolicy` authority first, and a refusal routes to
   `0.7.0_AE_CloudOps~FBL` (laptop), as act 1 did. No identity is widened to make the call pass.
5. **Close:** a READ by each admitted principal, through its own identity or the OAI, of one canonical object it will read after the flip (the
   ownership key for the validator and IRPT; one served object for the OAI), returns 200. A principal that is NOT admitted (the QA identity
   on the ownership key, say) still returns 403. That is the negative arm.

**What this teaches act 4's half:** its Branch B named `NoSuchKey` but not `AccessDenied`. ADDENDUM 1 of that half adds it.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 9 (2026-10-11 ~14:2xZ) -- act 3b's census: 1 of 11 readable. The generator cell (`prefix` as a list) comes FIRST. YES.

`2.0.0_SA_COO~B1` msg 3916, census `deliverables/2.0.0_SA_COO~B1/round4/IDENTITY_CENSUS_20261011.txt`. Only `partners-lambda-role` passes both rules.
Ten roles lack the identity Allow, and seven of those also fail the fence. `irpt-performance-adapter-role` is admitted, but its narrowed row
(rendered as Deny with NotResource outside `holdings_performance_daily/`) denies it the ownership key, and a row carries ONE prefix.

**Ruling: the generator cell first, then the rows.**
- **`prefix` accepts a string or a list.** A string is a one-element list, and the list renders as `NotResource` over every listed prefix.
- **Close (byte-identical arm):** every EXISTING row renders byte-identically, so the generated fence of every bucket that has no list row is
  unchanged (diff 0, buckets printed).
- **Close (positive arm):** the performance adapter's row with both prefixes renders the two-ARN `NotResource`.
- **Close (negative arm):** a prefix list holding a bucket-wide `*` or an empty string is REFUSED by the generator.
- **Then act 3b's pair carries all 11 principals,** with the identity Allow per role generated through `opal_name`, scoped to the key or
  prefixes it reads, plus the fence rows. Its close read is unchanged: 11 admitted at 200, and the negative arm at 403.
- **The ten missing identity Allows are the larger half of the act.** Each is a new inline policy, 10 resources. The pair prints the plan
  as exactly those, plus the fence policy's one change.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 10 (2026-10-11 ~14:3xZ) -- act 3b's carrier: the generated BUCKET-POLICY Allow, YES. It replaces ADDENDUM 8 item 2's identity grants, on four conditions.

`2.0.0_SA_COO~B1` msg 3921. Within one account, a resource-policy Allow that names a role's ARN admits that role's sessions with no identity
Allow. So the fence module renders an Allow beside each scoped Deny row, FROM THE SAME REGISTRY ROW.

The result: one `PutBucketPolicy`, one resource in the plan, no identity apply in 9 roots and no edge-role order. Unwinding is one row. That is
fewer moving parts and one place to read who may enter. **Accepted.**

**Conditions:**
1. **Permissions boundaries are read per role.** When a resource policy grants to a role ARN, an implicit deny in that role's permissions
   boundary STILL limits it.
   - Each of the 11 principals prints its boundary (none, or the boundary's verdict on `s3:GetObject` for the granted ARN).
   - A boundary that does not allow it is that role's identity apply, scoped, as ADDENDUM 8 item 2. It is the exception, not the rule.
2. **Grain: the OBJECT ARN of the ownership key, not the prefix**, for the validator and the IRPT roles. "Holds exactly the ownership map
   today" is a statement about today: a prefix grant silently widens the day another object lands under it. The row's `prefix` list carries
   the full key. The OAI keeps the served-class prefixes (ADDENDUM 8 item 1).
3. **Explicit identity Denies still win.** The performance adapter's `DenyPerformanceAdapter*` statements are the case in point: the generator
   cell of ADDENDUM 9 is still required for its row. Any other explicit Deny or SCP is found by the close read, not by reasoning.
4. **The close read is unchanged:** each of the 11 principals reads its granted object at 200 through its own role session, and a
   non-admitted principal reads 403. The plan prints exactly one resource: the bucket policy. Its rendered diff prints each new Allow beside
   its Deny row.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 11 (2026-10-11 ~14:5xZ) -- act 4b: exec-summary WRITES a served class. YES to the carrier. One standing rule, and an ordering condition.

`2.0.0_SA_COO~B1` msg 3925. `exec-summary-generator-role` also PUTS `platinum/advisors/<id>/exec_summary.json`
(`infra/aws/terraform/exec-summary/iam.tf` Sid `PlatinumWriteExecSummary`: `s3:PutObject` and `s3:PutObjectAcl`). Its schedule is
`cron(30 4 * * ? *)` (`main.tf:228`).

**Ruling: yes.**
- **Fence side:** a scoped row adds `s3:PutObject` to the closed action set, on prefix `advi/49financial/platinum/advisors/`.
- **Identity side:** the Allow stays in the exec-summary root at `advisors/*/exec_summary.json`, as one scoped apply.
- The effective grant is the INTERSECTION, so it is the identity side's object pattern. Its Get rows ride ADDENDUM 10's bucket-policy Allow.

**The standing rule this sets (for every later firm bucket):** a resource-policy Allow generated by the fence module carries READ actions only.
A WRITE is always granted on the identity side, scoped to the writer's object pattern; the fence's write exemption only stops the Deny from
applying. One write grant therefore lives in one place, and that place is the writer's own root.

**Conditions:**
1. **No `s3:PutObjectAcl` at the new home.** The fence row and the new identity statement carry `PutObject` only. If the function's put sets an
   ACL, the close read shows it, and the code drops it in 4b's build. An ACL write is not carried onto a new bucket.
2. **ORDER: 4b lands in the window right after act 2, BEFORE the next 04:30Z run.** Exec-summary is a writer of a served class. A run between
   act 2 and 4b writes the LEGACY home after the move, which is act 2's own Branch B ("a served write appears at the legacy home after the
   move"). Then:
   - its new-home writes are read at act 4, like the producers', within the same frozen-read cost;
   - act 3's keep-newer guard keeps them;
   - act 2's legacy-quiet read names `exec_summary.json` keys explicitly.
   If 4b cannot land before 04:30Z, act 2 waits for the next day's window.
3. **The writer census of the `advisors/` class is printed:** the producers (`D_04`'s advisor outputs) and exec-summary, N = 2. Both
   rules are read, and no key is written by both: exec-summary owns `exec_summary.json` only.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 12 (2026-10-13 ~04:5xZ) -- the exec-summary generator has not run since 2026-05-04: no manual invoke; diagnose in round 5; the regeneration goes under its own pair

`2.0.0_SA_COO~B1` msg 4638, row D1-S40 (FB1).
- `exec-summary-generator` is event-driven: it fires on chain-complete.
- The chain's `put-events` FAILS at every chain close since at least 04-25. There has been no invocation in 30 hours, and the last run was 05-04.
- The move did not cause it: the 60 changed lines of act 2's dispatcher diff touch none of the emission.
- **4b is therefore NOT EXERCISED,** and it is graded that way, never inferred.

**Rulings:**
1. **No manual invocation: AGREED.** It would regenerate 158 CLIENT-FACING summaries, stale since May, with an LLM. That is a served change outside the signed 4b pair. A manual
   run is also not production evidence.
2. **Owner:** no active project owns the exec-summary chain, and FIRMBKTS owns the 49 Financial chain's emission today. So **FIRMBKTS round 5 carries one READ-ONLY diagnosis
   cell:** the `put-events` error text from the dispatcher's own log, the event bus and rule as they exist, and the dispatcher role's `events:PutEvents` grant. No fix is in
   that cell.
3. **The fix is its own cell under a never-widen pair.** Its served effect is the first chain after the fix regenerating up to 158 client-facing summaries, so the pair names:
   - the key set;
   - a SAMPLE of regenerated summaries read before anything serves;
   - the prior VersionIds as rollback.
4. **Andrew is TOLD now, as information:** client exec summaries have not refreshed since 2026-05-04. Whether he reviews a sample before the regeneration serves is his choice;
   this seat recommends he does.

-- 1.0.0_SA_CTO~DELL1
