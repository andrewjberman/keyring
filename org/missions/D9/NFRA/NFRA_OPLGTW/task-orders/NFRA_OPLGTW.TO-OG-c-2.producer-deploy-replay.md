# TO NFRA_OPLGTW.TO-OG-c-2 -- the producer deploy, then a controlled replay that qualifies one date per master

<to_id>NFRA_OPLGTW.TO-OG-c-2</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~4</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-c-2` | **outcome_ref:** FWD-2, FWD-5, FWD-8 | **depends_on:** `OG-c-1`; **HELD on gate G-B** (both world acts) | **slot:** ~4, queue position 2

---

## WORKER FACE

### THE CELL

`OG-c-2` -- **the producer deploy, then a controlled replay** that writes one qualified completion record per master for
one stated business date. Vendor `OG-c-1`'s merged scripts into the Lambda package directory
`infra/aws/lambda/opal-assets/opal-assets-silver-schwab/`, move the build pin, deploy the `opal-assets-silver-schwab`
Lambda through the estate's path, then run the replay and read it back.

The PRD, verbatim (C3): *"Legacy markers are nonqualifying until a controlled producer replay or metadata backfill
reconciles against original inputs and exact current output versions. Thus no historical date is promised accessible
merely because a silver prefix exists."* And: *"Do not repair source data or rewrite silver values as part of this
extension."* And (C6): *"Source ingesters and source contents remain intact."*

**The deploy path, measured at the cut, not re-decided:** the Lambda is `module "silver_converter"` in
`infra/aws/terraform/opal-assets/silver.tf:640-674` (`../modules/yang-lambda`, `for_each` over six families,
`artifact_key = "opal-assets/opal-assets-silver-${each.key}.zip"`), and the per-family build pin is
`local.silver_build_commit = { schwab = "5c7b2a9a6b" }` at `silver.tf:78-80`, with its own comment explaining why the pin
is sparse and must move with the package. Find the build that writes that artifact from the vendored directory, and use
it. **Rule 13:** code under `data/*/scripts/silver/` deploys through the DS lane's `.tools/safe-deploy.sh` guard; if that
guard, or any lane, refuses your serial, file a BLOCKING row and stop -- the issuer seats a DS lane for this order.

**Gate G-B holds BOTH world acts, the deploy and the replay.** Once the new code runs, every daily conversion (the
schedule `cron(15 12 * * ? *)`, `silver.tf`) writes extended marker objects under `schwab/*/meta/complete/`, and the S3
notification `advi-49f-silver-complete-accelerator` (`silver.tf:756-759`) starts the 49F gold dispatcher on every
`ObjectCreated` under `schwab/08335338/meta/complete/`. That is served output moving, so CLAUDE.md's never-widen rule
binds: before either act, the sign-off record
`org/tier1_exec/2.0.0_SA_COO~O/deliverables/NEVER_WIDEN_SIGNOFF_NFRA_OPLGTW_OG_C2.md` must be at HEAD with two halves,
`1.0.0_SA_CTO`'s and `2.0.0_SA_COO~O`'s, each naming the write set, the number of writers of `meta/complete/` and every
`ObjectCreated` consumer. If it is absent or carries one half, do nothing to AWS: file a BLOCKING row and stop.

The baseline for the bucket settings is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~2/BASELINE.json`
(`OG-p-1`); the record schema is `OG-c-1`'s (its result file in this slot's deliverables).

**The un-staging, before any plan (amended by `2.0.0_SA_COO~O` before re-hand, per `1.0.0_SA_CTO` ruling R-OG-1, msg
97499, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @d6583eab37; row W4-S5).** The
`opal-assets` root carries a staged-and-never-applied change to `opal-assets-daily-emitter` (commit `2740e4de8f`) that
repoints it at `portal/gold/mdpf/_staging/aggregate_aua/`, an empty tree whose producer `mdpf-daily-trigger` has been
destroyed. It is WITHDRAWN from this root, not admitted. As your first act, restore that file to its parent's bytes in
its OWN commit: `git checkout 2740e4de8f^ -- infra/aws/terraform/opal-assets/emitter.tf`. The commit message records that
X-ii-a's AE half is withdrawn from the root because its producer was destroyed and its target tree is empty, and that a
re-home re-lands through its own act under MDPF_CANON. Touch no other file in that commit and nothing in the
`mdpf-pipeline` root. No ledger entry is opened for the un-staging (nothing was ever applied). The discriminator is
`OGC2-AC3`: the plan then reads only the schwab family's rows. Gate G-B stands with no re-read.

**The replay is RELEASED (issuer, 2026-09-16 ~18:4xZ), on rulings R-OG-4 and R-OG-5** (`1.0.0_SA_CTO` msg 97522, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_NFRA_OPLGTW_20260916.md` @f81896bae3). Both G-B halves are re-signed
(Half 1 s.6, Half 2 s.E). Before the replay, confirm the released terms by reading this order's text at CLOUD HEAD in
the shared tree, `/c/Users/AndrewBerman/Desktop/ajb_workspace`, and that sign-off record there.
- **Write set (W4-S9):** the replay writes FOUR objects: per master, the run manifest
  `schwab/{master}/meta/conversions/{run_id}.json` and the marker `schwab/{master}/meta/complete/date=D_r.json`. Record
  each object's key and VersionId in the result file.
- **Stop precondition:** first run a read-only dry run of `convert_object` for `D_r` on each master. It must print ZERO
  silver writes AND ZERO missing projection dims. Any non-zero count means no replay and one BLOCKING row.
- **The 49F reads (W4-S8)** that sign-off conditions 4, 5 and 7 require are admitted: see the Cross-firm bullet in BOUNDS.
- **Ledger:** the deploy entry is already closed. The replay opens its own entry,
  `nfra-oplgtw-og-c-2-replay` (sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-c-2-replay.json`), and commits
  it before the replay and closes it before `AC7`..`AC11`'s grading reads.

**Read:** the PRD's "C3" and "C6"; `infra/aws/terraform/opal-assets/silver.tf`; `infra/aws/terraform/modules/yang-lambda/`;
`OG-c-1`'s result file; the sign-off record above.

**The probe** for every criterion is `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py`,
taking the short id, printing its measurement with vintage and denominator, then exactly one line
`VERDICT: PASS-OGC2-AC<n>` or `VERDICT: FAIL-OGC2-AC<n> <reason>`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGC2-AC1" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC1</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC1(?![0-9])</expect></criterion>
`OGC2-AC1` -- the vendored files are byte-equal to `data/assets/scripts/silver/` at `OG-c-1`'s merged commit.

<criterion id="OGC2-AC2" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC2</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC2(?![0-9])</expect></criterion>
`OGC2-AC2` -- `silver.tf`'s `silver_build_commit.schwab` names that commit.

<criterion id="OGC2-AC3" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC3</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC3(?![0-9])</expect></criterion>
`OGC2-AC3` -- the plan changes only `opal-assets-silver-schwab` and shows zero rows for the other five families.

<criterion id="OGC2-AC4" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC4</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC4(?![0-9])</expect></criterion>
`OGC2-AC4` -- the deploy runs through this Lambda's estate deploy path under a ledger entry opened and committed before the act.

<criterion id="OGC2-AC5" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC5</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC5(?![0-9])</expect></criterion>
`OGC2-AC5` -- the deployed `CodeSha256` equals the built zip's hash.

<criterion id="OGC2-AC6" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC6</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC6(?![0-9])</expect></criterion>
`OGC2-AC6` -- the never-widen sign-off of gate G-B is at HEAD before the replay, cited by path@commit, with both halves (the probe also shows its commit precedes the deploy's).

<criterion id="OGC2-AC7" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC7</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC7(?![0-9])</expect></criterion>
`OGC2-AC7` -- the controlled replay writes one qualified closure record per master for one stated business date.

<criterion id="OGC2-AC8" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC8</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC8(?![0-9])</expect></criterion>
`OGC2-AC8` -- each replayed record validates against `OG-c-1`'s schema.

<criterion id="OGC2-AC9" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC9</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC9(?![0-9])</expect></criterion>
`OGC2-AC9` -- every VersionId a replayed record lists HEAD-matches the live object.

<criterion id="OGC2-AC10" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC10</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC10(?![0-9])</expect></criterion>
`OGC2-AC10` -- (difference) the VersionIds of every silver object for the replayed dates are identical before and after the replay.

<criterion id="OGC2-AC11" cell_refs="OG-c-2"><invocation>cd <WS> && timeout 120 py -3.12 org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/probes/og_c2.py AC11</invocation><expect>(?m)^VERDICT: PASS-OGC2-AC11(?![0-9])</expect></criterion>
`OGC2-AC11` -- the bucket settings read back equal to `OG-p-1`'s baseline.

<expected_criteria>OGC2-AC1, OGC2-AC2, OGC2-AC3, OGC2-AC4, OGC2-AC5, OGC2-AC6, OGC2-AC7, OGC2-AC8, OGC2-AC9, OGC2-AC10, OGC2-AC11</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **G-B.** No deploy and no replay without the two-half sign-off record at HEAD. Its absence is a BLOCKING row and a stop; vendoring and the pin edit may be committed before it.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-c-1` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** `py -3.12`; no package install in this cell.
- **Deploy discipline (spine L7).** Open the entry with `py -3.12 .tools/deploy_ledger.py open --slug nfra-oplgtw-og-c-2-producer ...` and COMMIT its sentinel `org/critical_paths/.open_deploys/nfra-oplgtw-og-c-2-producer.json` and entry BEFORE the deploy; the replay is a second leg of the same entry; close the legs and the entry and COMMIT BEFORE the grading reads. NEVER leave it half-landed: finish in-session, or roll the Lambda back to the previous artifact and file an ARMED row naming yourself as disarm owner.
- **Terraform** only through `.tools/safe-apply.sh`, never bare `terraform apply`, never `-target`, never `aws lambda update-function-code`. `.tools/terraform.exe` is provisioned into your worktree by the issuer; if absent, a BLOCKING row.
- **Blast radius.** One function family. A plan row for any other family, any IAM change, or any change to the bucket, its notifications or its policy is a BLOCKING row and no apply.
- **No source mutation.** No write, delete or overwrite of any bronze or silver object; the replay writes completion records only. AC10 is the proof.
- **Cross-firm law.** Only `schwab/08242234/` and `schwab/08335338/`; no other firm's bucket or prefix. One exception, by ruling R-OG-4 (msg 97522 @f81896bae3, row W4-S8): the reads that G-B conditions 4, 5 and 7 require are admitted read-only (list, head, get) on exactly `s3://opal-data-49financial/gold/advi/_logs/` and the `date=D` keys those conditions name, with every key read printed and nothing else in that bucket. Carrier: `infra/logic/05_IDENTITY_SPINE.md:83,:97` and `04_SCOPE_TICKLIST.md:50` map master `08335338` to `49financial`, so this is the master's own downstream chain. It is a probe of a sign-off condition, not a pipeline tree referencing another firm's data.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No new monitor, alarm, SNS or notification path.**
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W4-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/conversion_manifest.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_runtime.py
infra/aws/lambda/opal-assets/opal-assets-silver-schwab/BUILD_MANIFEST.json
infra/aws/terraform/opal-assets/silver.tf
infra/aws/terraform/opal-assets/emitter.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-og-c-2-producer.json
org/critical_paths/.open_deploys/nfra-oplgtw-og-c-2-replay.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-c-2`, round 1 (section 3, S4; section 6 G-B; section 8 bound 5).
<owned_cells>OG-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGC2-AC1` .. `OGC2-AC11` (11). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~4/NFRA_OPLGTW.TO-OG-c-2.producer-deploy-replay.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGC2-AC1,OGC2-AC2,OGC2-AC3,OGC2-AC4,OGC2-AC5,OGC2-AC6,OGC2-AC7,OGC2-AC8,OGC2-AC9,OGC2-AC10,OGC2-AC11`
BEFORE the `complete` flip. Result file `producer-deploy-replay.result.md` beside it, naming the replayed date per
master and each record's key and VersionId. **Flip `complete` only when every MECHANICAL criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. This cell is HELD on project gate G-B for both of its world acts: the decomposition's s.6 names the replay, and its bound 5 (no served output moves without G-B) reaches the deploy too, because the daily run then writes extended markers that the 49F accelerator consumes. The never-widen, no-half-landed-deploy and safe-apply-only moratoria bind it.
comp-iam: RUN at L5 -- comp-iam service opal-gateway covers the Gateway, not this Lambda; the lens is re-run on opal-assets-silver-schwab by this cell (473 .tf files at the cut) and recorded in its instance. The deploy adds no IAM change; any plan row that does is a BLOCKING row.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood. The unscoped marker census at the cut (361 hits over 172,084 files) found the live consumer at silver.tf:756-759 that makes G-B bind here.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant); rule 13's DS guard on data/*/scripts/silver/ deploys is measured by this cell, and a refusal seats a DS lane.
</preflight>

Seating: slot ~4, queue position 2, handed after `OG-c-1` merges; its world acts wait on the G-B record. Round 1 of
NFRA_OPLGTW, issued by `2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770. The issuer copies
`.tools/terraform.exe` into the slot's worktree at hand-off.
