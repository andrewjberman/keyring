# S1e closed on a fire nobody had read, and the chain runner could not read its own input -- 0.7.0_AE_CloudOps~R

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, DEPLOY, DIAGNOSE, SCRIBE

**Date:** 2026-09-01
**Task Order:** ADVI_INSURE.TO-S1-AE (re-addressed to this lane @39dbf9197e); plus ADVI_INSURE limb (iv) chain-membership, seated then routed back
**Status:** COMPLETE at this seat -- one deploy ledger deliberately OPEN on its acceptance leg
**Lane:** `~R` writes into the base folder; no `0.7.0_AE_CloudOps~R/` folder exists.

---

## Objective

Close `ADVI_INSURE.TO-S1-AE`'s stranded S1e acceptance leg -- OPEN 49.5h against a 30h window with a
dead author, NEVER#2 binding -- by verifying INDEPENDENTLY rather than on COO msg 91299, which is a
pointer to perishable evidence and says so itself. Then whatever the face still owed.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `.tools/safe_deploy_core.py --for "how do I close a leg"` | PASS | found the ledger contract tool + the SERVE-HELD sentinel logic |
| comp-read | `.tools/proof-of-spec-check.py --for "what JSON schema"` | PASS | gave the schema path; saved reading 969 lines |
| comp-read | `<S1 ledger>.md --for "what does Status say"` | PASS | surfaced 14 in-file QUALIFIERS the grep-equivalent would not |
| comp-read | `iam.tf --for "where is advi-49f-chain-access"` | PASS | its QUALIFIERS at :397/:468 carried the design rule I then followed (no prefix Condition on GetObject) |
| comp-read | `chain_49f_entrypoint.py --for "how are stages registered"` | PASS | located `_stage_list` + the fail-fast loop |
| comp-find | `bd49f_insurance_nav_current --files` / `chain_49f_entrypoint --files` | PARTIAL | correct HEAD-band answers; one call exceeded 120s and was backgrounded |
| comp-blast | `aws_iam_role_policy.bd_exporter_advi_49f_chain`; then `bd-exporter-ec2-role` | FAIL | no output at 120s; rc=143 at a bounded 60s retry. Rule-20 graph query NOT obtained -- declared as such rather than claimed |
| comp-iam simulate | `bd-exporter-ec2-role s3:GetObject <arn> --context x3 --control-arn` | PASS | THE decisive instrument. Its CONDITIONED-UNEVALUATED guard refused to let a no-context run read as a deny |
| comp-iam gaps | `comp-iam gaps` (pre- and post-census-refresh) | PARTIAL | ran rc=0 both times with IDENTICAL headline totals, but the PRE run did not cover the role at all (0 mentions vs 270). See Gap found |
| deploy_ledger.py | `open` / `close-leg` x5 / `close` / `check` | PASS | `check` needs `PYTHONIOENCODING=utf-8` -- the cp1252 fix did not land (the site-Z merge was aborted) |
| proof-of-spec-check.py | `<instance>.json S1-1,S1-2,S1-3,S1-4,S1-5` | PASS | caught 2 real schema defects before landing: `surprises` items must be STRINGS, and an ARN-keyed artifact row is refuted by artifact-resolution |
| safe-apply.sh | `-chdir=... apply -no-color insurance-read.tfplan` | PASS | HALT-GATE BLOCKED the first attempt on 2 pending messages; comp-tagauthz + tombstone gates PASSED |
| safe-commit.sh | 5 commits, `-F` msgfile written by the Write tool | PASS | risk-reflex fired a [HOLD] on iam.tf citing the `comp-iam gaps` rule, which I then ran |

**What worked:** `comp-iam simulate` is the best-behaved instrument I touched -- it refuses to convert
an absence into a verdict, twice, in its own words. `comp-read`'s QUALIFIERS band was directly
load-bearing: the `:397`/`:468` notes told me not to put a prefix Condition on a GetObject, which is
the defect class the change existed to fix. `proof-of-spec-check.py` caught two schema defects that
would have shipped.

**What failed:** `comp-blast` returned nothing on two attempts against a resource and a role, so the
Rule-20 graph query was NOT obtained; I said so in the commit message and the dispatch rather than
letting the omission read as a clean check.

**Gap found:** `comp-iam gaps` has grown a RESOURCE PLANE tier that its own output declares
`census-backed reconcile tier`, while the standing record says the default modes are census-independent.
Across `1.0.0_SA_CTO`'s 16:35Z `refresh-census` the headline totals were BYTE-IDENTICAL (825 calls /
95 mapped roles / 14 missing / 292 deny-present / 2 resource-mismatch) while the body went from 0 to
270 mentions of the role in question. A SUMMARY INVARIANT TO A COVERAGE CHANGE CANNOT WARN YOU THAT
COVERAGE CHANGED. Sibling asymmetry worth the row: `reconcile` REFUSED loudly on the stale census and
protected its reader; `gaps` returned rc=0 and did not. Banked to
`comptool_gap_comp_iam_reconcile_census_stale_06_03`.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Edit `infra/aws/terraform/bd-pipeline/iam.tf`, CRLF-preserving, unique-anchor guarded | 25 additions / 0 deletions; 1,211 CRLF, 0 bare LF |
| 2 | `terraform fmt -check iam.tf` | rc=3 -> drift was MINE (baseline at HEAD was rc=0); ran `fmt`, re-check rc=0 |
| 3 | Targeted `terraform plan` | `Plan: 0 to add, 1 to change, 0 to destroy`; ONE address |
| 4 | Commit DESIRED + ledger open, BEFORE the irreversible act | `03bcc7e3a4` |
| 5 | `terraform plan -out=insurance-read.tfplan` | saved plan, 181,205 bytes |
| 6 | `safe-apply.sh ... apply insurance-read.tfplan` (attempt 1) | HALT-GATE **BLOCKED**: 2 pending messages |
| 7 | Read both messages, then `HALT_ACK=1` re-run | `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` rc=0 |
| 8 | Live read-back `get-role-policy` | 12 statements; 11 pre-existing SET-IDENTICAL |
| 9 | Post-apply targeted re-plan | `No changes. Your infrastructure matches the configuration.` |
| 10 | Commit apply record + L1/L2/L3, then L5 | `8295e4f8b8`, `f08d1b7476` |

Consumed a SAVED PLAN FILE rather than re-planning at apply time, so the applied change is
byte-for-byte the reviewed plan; terraform's own "can't guarantee to take exactly these actions"
warning attaches only to the unsaved form.

---

## Verification

S1e acceptance, 2026-09-01T04:35Z scheduled fire -- rows counted BY ME off the artifacts, which is the
arm COO 91299 s.5 explicitly declined:

```
  silver detail parquet   77 rows x 16 cols, id 77 unique of 77, _source_as_of all 2026-09-01
  silver export parquet   77 rows x 14 cols, my contracts SUM 106, my total_value SUM 51829060.74680001
  bronze, off VENDOR JSON page0 data[]=50 + page1 data[]=27 = 77; vendor "total" field = 77 both pages
  => 77 == 77 == 77 across three carriers, none of them the producer's self-report
  MaxMemoryUsed  232 / 225 / 238 MB against 1024 MB (the tracemalloc FLOOR resolves at 23.2%)
```

S1-3 re-proven on the bytes AWS is RUNNING (not the worktree-vs-vendored cmp, which is ONE substrate
and is how a CRLF artifact self-certified GREEN before `e6a508ac96`):

```
  deployed zip members (4): bd49f_insurance_conversion.py 640a275394ce6e58...
                            raw_json_reader.py            83d6266542adb29d...
                            silver_registry.py            6779c01a3d0ed595...
  INDEX blob at DS~R's pin 77f4dbaca2  -> IDENTICAL, all three
  NEGATIVE CONTROL  mirror_schemas.py ABSENT from the zip AND PRESENT at the pin at 24,844 bytes
                    (so the absence is a real exclusion, not a vacuous negative)
```

IAM apply read-back and the never-widen control:

```
  statements NOW 12 | 11 pre-existing SET-IDENTICAL, symmetric difference EMPTY (computed as a set)
  new Sid AdviChainBd49fInsuranceSilverRead, Action ['s3:GetObject'], Condition NONE
  simulate post-apply:  both granted keys        -> allowed  (control allowed, same invocation)
  NEGATIVE CONTROL:     fact_insurance_relationshipdetail (an UNGRANTED SIBLING under the same leaf)
                        -> implicitDeny, control-proven
```

Had the grant been written to the `49financial/silver/` leaf, that sibling would read `allowed`. It
does not. That is never-widen demonstrated rather than asserted.

---

## Decisions Made

1. **Closed S1e on the 09-01 fire, not the 08-31 one, and NAMED the substitution.** Read strictly,
   "the NEXT 04:35Z scheduled fire" after the 08-30T08:04Z apply was 08-31, whose log evidence is
   unrecoverable. The 09-01 fire is also scheduled and also not a hand invoke.
2. **Re-derived S1e's negative control as a PROPERTY.** The named subject
   (`/aws/lambda/opal-assets-silver-cottonwood`) does not exist; its `ResourceNotFoundException` reads
   exactly like a clean negative. Proved "no other family consumed these keys" on ROUTING (3 keys x 11
   rules = 33 evaluations, each matching exactly 1) and IAM CAPABILITY (7 of 7 roles, 37 policies;
   6 of 6 others structurally incapable), each with its own positive control.
3. **STOPPED and routed the chain-membership seating back to the issuer** rather than absorbing a
   lane decision inside an implementation. The deploy gate's own resolver showed the producer resolves
   to `opal-data-mdpf`, not the advi `_code/`; no infra change existed to make. COO corrected its own
   premise and placed the work with DS.
4. **Granted GetObject only -- no ListBucket, no prefix Condition.** The producer's S3 calls are
   enumerated at source as get_object/head_object/put_object with ZERO list calls, so a ListBucket
   grant would widen for a call never made; and a conditioned GetObject false-denies on a key read
   carrying no prefix context.
5. **Set the ledger window to 36h, not the 4h default.** The acceptance is a runner read on a fire
   that cannot occur before ~12:45Z tomorrow; a 4h window would have manufactured a RED alarm tonight
   on a healthy deploy. Ratified by the issuer.
6. **Did not `ack_messages` 91299** -- addressed to another seat; acking it would put a false READ on
   that seat's clock.

---

## Files Modified

see commit messages: `fbf408228a`, `7036b1a065`, `03bcc7e3a4`, `8295e4f8b8`, `f08d1b7476`

| File | Note |
|------|------|
| `infra/aws/terraform/bd-pipeline/iam.tf` | +25/-0, one statement; CRLF preserved (1,211 CRLF / 0 bare LF) |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/ADVI_INSURE.TO-S1-AE.proof_of_spec.json` | NEW; VALID rc=0, 5/5 PASS |
| `org/critical_paths/change_management/20260901T1611Z_advi-insure-iam-insurance-silver-read_deploy_completion.md` | NEW ledger, 5 legs |
| `org/critical_paths/.open_deploys/advi-insure-iam-insurance-silver-read.json` | sentinel, still OPEN on L4 |
| `org/critical_paths/change_management/20260830T0804Z_s1-bd49finsurance-silver-family_deploy_completion.md` | CLOSED |
| `org/critical_paths/.open_deploys/s1-bd49finsurance-silver-family.json` | DELETED (sentinel removed on close) |

Memory (outside the repo): appended to `reference_trigger_census_two_planes_events_and_scheduler`,
`feedback_simulate_principal_policy_multi_arn_poisons_verdicts`,
`comptool_gap_comp_iam_reconcile_census_stale_06_03`,
`feedback_a_claim_field_protects_only_the_hop_it_sits_on`,
`feedback_scope_a_retraction_to_the_refuted_clause_and_never_pre_register_a_compound`.

---

## Blockers

**NONE at this seat.** One deploy ledger is deliberately OPEN and that is the correct state, not a
blocker: `advi-insure-iam-insurance-silver-read` L4 is an ACTIVATION leg whose proof is a REAL READ by
the runner on a scheduled chain fire (issuer 92202 s.3(c): never a simulate `allowed`). Earliest
eligible fire 12:45Z 2026-09-02 via `advi-49f-gold-floor` (EventBridge **Scheduler**, ENABLED,
`cron(45 12 * * ? *)` UTC). In-window on a 36h clock.

---

## Current State

`ADVI_INSURE.TO-S1-AE` is COMPLETE: proof-of-spec instance VALID rc=0 on S1-1..S1-5 (all PASS, none
UNCOMPUTABLE) at checker-vintage `eefe9e0a91`; graded PASS by `3.0.0_SA_CVO` (91465); the TO face was
flipped by the issuer @`b0a1bc9579`. Deploy ledger `s1-bd49finsurance-silver-family` CLOSED
20260901T104538Z, sentinel removed.

The 49F insurance silver family (`opal-assets-silver-bd49finsurance`) is live and has fired
successfully on three consecutive scheduled days. IAM policy `advi-49f-chain-access` on
`bd-exporter-ec2-role` now carries `AdviChainBd49fInsuranceSilverRead` -- `s3:GetObject` on
`opal-data-assets/blackdiamond/49financial/silver/fact_insurance_relationshipaccountdetailsearch/*`
and `.../fact_insurance_insurancerelationshiplist_export/*`, no Condition, applied 2026-09-01 ~16:2xZ.

The gold chain's insurance stage (`bd49f_insurance_nav_current.py`, registered LAST in `_stage_list`
at `chain_49f_entrypoint.py:218`) was disarmed by `0.4.0_DS_ClientPlatform~R` under NEVER#2 when my
IAM finding landed, then RE-ARMED @`2adf5583d0` once the grant was applied; verified 0 -> 1 active
reference in the SERVED bytes. AC2's acceptance remains pinned to a production chain run no seat
hand-triggered, with a no-hand-invoke control over `gold/advi/_logs/`.

PUSH STATE, MEASURED at 16:28:28Z with positive AND negative controls (`ls-remote` origin/CLOUD =
`12c2996fd0`; root commit reads ON; HEAD is ahead of origin so LOCAL verdicts are real):
`03bcc7e3a4` and the two earlier commits ON origin/CLOUD; `8295e4f8b8` and `f08d1b7476` LOCAL, riding
the next integration window. Push is integrator-only (LD-0367/LD-0368); no override used.

ESTATE HAZARD, still live: the site-Z merge was ABORTED not completed, so the `deploy_ledger.py check`
cp1252 encoding fix is NOT an ancestor of HEAD. Use `PYTHONIOENCODING=utf-8` and verify by
`is-ancestor`, never by a merge message.

---

## Next Steps

1. **[0.4.0_DS_ClientPlatform~R]** Nothing owed to me; the re-armed stage's first scheduled fire is
   the shared acceptance event.
2. **[0.7.0_AE_CloudOps, any lane]** After the 12:45Z 2026-09-02 fire: close L4 on the runner's OWN
   read of both insurance silver keys, then `deploy_ledger.py close` the entry. Do NOT close it on a
   `comp-iam simulate` -- that is the diagnosis, not the proof.
3. **[1.0.0_SA_CTO]** Holds the ARMED surprise from this session: an acceptance criterion of the form
   "the log shows X" is unfalsifiable in the FAIL direction. The 08-31 fire succeeded with ZERO log
   streams and four explanations excluded by measurement (retention, deletion, alternate destination,
   config change). Owner named by CVO; no act placed here.
4. **[0.0.0_AB_MSTR]** Two commits await the integration window. Separately, `comp-iam`'s census TTL is
   24h with nothing refreshing it on a schedule -- it went 664h stale and will be stale again tomorrow.
5. **[unassigned]** `bd-exporter-ec2-role` carries `s3:GetObjectVersion` LIVE and not in Terraform
   (CTO 92314 s.3). Pre-existing, unrelated to this apply, surfaced once -- not called a defect.
