# 0.7.0_AE_CloudOps~A -- OPAL_ASSETS G4 APPLY + R-A/R-B BUILD + two instrument findings

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE

Lane: `0.7.0_AE_CloudOps~A` (post-reboot respawn). Window: 0519Z -> 0625Z.
Self-onboarded from `org/tier1_exec/1.0.0_SA_CTO/PRE_REBOOT_JOINT_NEXT_STEPS_20260713.md`.

---

## Summary

Respawned as the gated applier for 0.8.0's OPAL_ASSETS G4. Applied it, found and closed a gap the
deploy itself created, root-caused TWO silent instrument failures (one of which amended CLAUDE.md
Rule 22a), closed the G-A identity TO, and built R-A/R-B. **I also got a load-bearing analysis WRONG
and retracted it** -- recorded below, because the mechanism is the reusable part.

---

## What landed

| item | evidence |
|---|---|
| **OPAL_ASSETS G4 APPLIED** | `safe-apply` 0 added / 2 changed / 0 destroyed; 0-diff re-plan; commit `94fe0c96c`; tag `opal-assets-v0.2.0`; HEAD==origin/CLOUD verified (not inferred from rc=0) |
| **Deploy ledger** | `20260713T0535Z_opal-assets-g4-ownership-fold` -- OPENED at deploy-start, **5/5 legs proven, CLOSED**, sentinel removed (NEVER#5, nothing stranded) |
| **Ownership backfill** | 19 partitions, **494 rows live**, all uniform at 14 base + 12 ownership, 0 rows missing `value_class` |
| **NFRA_IDENTITY.G-A closed** | TO -> complete @ `5a9543946`; guard landed by CTO @ `786fb085d` |
| **R-A/R-B built** | working tree, gate-clean, 9/9 reachability. **COMMIT HELD** pending 0.8.0's v0.2 guard rewrite (his 2 tests encode the old `partial` schema) -- will not land a red tree |

**IAM verified on all three planes (Rule 22a):** APPLIED (`get-role-policy` shows `ReadEtfsOwnershipDaily`
on `opal-data-etfs/daily/*`, prefix-scoped, additive-only) + SIMULATED (3 SEPARATE single-ARN calls: etfs
target `implicitDeny`->`allowed`; mdpf positive control `allowed`; **sovereign `opal-data-bd` `implicitDeny`
-- 49F/Schwab hold intact**) + EXERCISED (invoke rc=200 -> 26 rows / 14 base / 12 ownership).

---

## FINDING 1 -- CLAUDE.md Rule 22a's mandated instrument has a SECOND false-deny mode (now fabric law)

`simulate-principal-policy` **silently flips a HELD resource to `implicitDeny` when batched in one call with
a NOT-held ARN.** Isolated by exercise (same role, same action, same key -- only the batching differs):

```
1 ARN, held                 -> allowed                      CORRECT
2 ARNs, BOTH held           -> allowed, allowed             CORRECT
2 ARNs, held + NOT-held     -> implicitDeny, implicitDeny   THE HELD ONE FLIPS
```
Ground truth: the Lambda's own CloudWatch log shows it SUCCESSFULLY reading the exact key simulate called
denied. **Rule 22a mandates simulating a NEW (by definition not-held) target WITH a positive control on a
held resource -- batching them IS the poisoned combination.** The rule's method breaks precisely and only in
the configuration the rule mandates, and **the positive control is corrupted by its own presence in the
batch** -- a control must be independent of the fault it detects; here it participates in it.

- **It root-causes base-AE's open gap** (*"simulate false-denied its own positive control"*) -- he batched.
- **It would have false-failed THIS deploy:** the post-apply check includes a sovereign `opal-data-bd` ARN
  that is BY DESIGN not-held; batched, it poisons the etfs verdict -> the landed grant reads `implicitDeny`
  -> roll back a correct change.
- **DISTINCT from base-AE's conditioned-statement mode.** My statement has NO `Condition` at all. Neither
  fix repairs the other. Flagged so they were not deduped into one entry.
- **LANDED BY CTO into CLAUDE.md Rule 22a @ `7f6611ea7`** with both modes + the load-bearing sentence:
  *"A POSITIVE CONTROL IS ONLY A CONTROL IF IT IS RUN IN ISOLATION FROM THE TARGET."*

## FINDING 2 -- the `.tools/aws` shim silently breaks EVERY `powershell.exe ... aws ...` call in the fabric

`build-and-upload.sh` reported SUCCESS while S3 still held the OLD pre-G4 zip (4994B/`AfhKW...` vs expected
7942B/`GfqMY...`). **Caught by base-AE's upload-verify gate (`da5af3c8c`) -- its FIRST PRODUCTION FIRE.**
Without it: source map records the new sha, S3 serves old code, TF deploys G4's IAM grant onto the PRE-G4
Lambda, every record says G4 is live.

ROOT CAUSE (source-grounded): `build-and-upload.sh:294` runs `powershell.exe -NoProfile -Command "aws s3 cp
... --quiet"`. PowerShell's `Get-Command aws` resolves to **`.tools/aws` -- the gitignored BASH shim**
(`19fde37de`, pending CTO~D ratification). PowerShell cannot execute an extensionless shell script, so the
cp **never runs**: `$LASTEXITCODE` returns **UNSET** and `--quiet` hides the void. Probe: TESTPROBE.zip
through that exact path -> **head-object 404**.

**The collision is exquisite: the script routes through PowerShell specifically to ESCAPE MSYS mangling, and
the shim -- whose whole purpose is to FIX MSYS mangling -- intercepts it there and kills it.** Routed to
CTO + CTO~D as decision-grade input for the shim RATIFICATION gate.

## FINDING 3 -- the fabricated-zero class arriving via ABSENCE

Post-apply, only 1 of 19 partitions had ownership rows. **On a table Andrew queries, an absent row is
indistinguishable from "this partner held nothing."** The honest-absence rule protects a partner with no
series; it does not protect a partition the fold never visited. Backfilled the existing range (deeper history
stays Andrew-gated); safety pre-checked, not assumed (`write_rows` = pure `put_item` upsert, no delete/wipe;
base rows rewrite byte-identically; `_latest_partner_key` bounded by run_date so an old-day backfill cannot
read a future partition). Accepted by CTO~B + COO as a genuinely new face of the class.

---

## WHERE I WAS WRONG (the important part)

**I told CTO~B and COO, in writing and with confidence, that their `additive` boolean COULD NOT SHIP** --
that two headline components were missing as rows and a 3-value `contributes: add|subtract|none` was needed.
**FALSE. Retracted in full within ~3 minutes.**

I found mdpf's published identity (`model_aua + sma_aua + non_model_aua - cohort_2b = headline`), matched it
**to the penny on ONE partition**, and called the basis grounded. It IS a true identity -- just not the one
our rows express. **`49f_schwab_custody` IS 49F's complete AUA; the 7 model rows live INSIDE it.**

| set | denominator | result |
|---|---|---|
| `{49f_schwab_custody, inflection_models}` (0.8.0, right) | 427 partitions | MATCH 427 / MISMATCH 0, residual $0.0000 |
| `{7 model rows + inflection}` (mine) | 427 partitions | **MISMATCH 427**, short $197M-$249M |

**Two decompositions agree on the total and disagree about which rows carry it -- one partition cannot
separate them; they agree exactly where I looked.** And I had the tell and explained it away: I SAW
`custody_composite` ($1.62B) exceed the model rows ($1.42B), labelled it "an overlapping lens," and the gap
between them IS the money I then declared "missing from the table." **I fitted the anomaly into my hypothesis
instead of letting it break the hypothesis.**

**COO's HARD GATE caught it** (*"do NOT mark `additive` until the basis is grounded and CTO~B rules"*). Her
reasoning is the durable part: today a naive SUM is wrong and nothing vouches for it; after a mis-specified
flag it is wrong **AND THE SCHEMA SAYS IT IS RIGHT** -- strictly worse, because the plausible wrong number
($1.56B, 11% short) would not be caught by a human, while the absurd one ($5.8B, 3.3x) might. **Ship the
mechanism, gate the semantics.** Banked (canonical entry authored by CTO~B).

---

## R-A/R-B (built, commit HELD)

- **`basis` derived from the cohort spec's `vkind`; `additive` DERIVED from `basis`** -- never hand-set, so
  the flag cannot drift from the axis it describes. Falls out as exactly `{49f_schwab_custody,
  inflection_models}`. 0.8.0's review: *"mine encoded the answer, yours encodes the REASON."*
- **Live dry-run:** 28 rows (14 base + 12 ownership + 2 total); `basis` missing 0; `additive` missing 0;
  **`SUM(value) WHERE additive` = 1,758,111,296.54 == mdpf certified headline, EXACT.**
- **R-B carry-not-compute:** `_total__partner_aua` CARRIED verbatim from `aggregate.opal_aggregate_aua` +
  `headline_formula` + `excludes_audit_only` as provenance. `_total__etf_fund` labelled `provenance=derived`.
  Two strengths of claim, labelled, not blurred. **NO cross-basis total** (bases overlap ~75%).
- **AC7 fail-closed:** an unreconcilable total publishes **NO NUMBER** (`value=None`, `state=incomplete`,
  delta named). 0.8.0 proved it adversarially: rewiring the SMArtX view into the additive axis produced
  `AC7 RECONCILE FAILED ... delta 1,400,957,639.03. NO TOTAL PUBLISHED.` **A miswired additive axis cannot
  put a wrong AUM number in front of Andrew.** Honest residual stated in-code: both sides derive from the
  same body, so it catches OUR transcription, not an error inside mdpf. A transcription check, not an audit.
- **`partial` RETIRED** -> `state=incomplete` DERIVED from declared-vs-observed masters. `source_masters`
  DECLARED (cohort spec / constant), `masters_present` OBSERVED. **Two independently-sourced sides**, because
  deriving expected FROM observed makes them equal by construction and `incomplete` UNREACHABLE -- CTO~B
  ruled this a defect in his own PRD after I flagged it; 0.8.0 confirmed he had the identical bug in his
  in-flight code.
- **Reachability suite 9/9** (`tests/test_incomplete_reachability.py`, NEW file): asserts `incomplete` CAN
  FIRE **and CAN NOT-FIRE** (a flag always-on carries as much information as one always-off), plus a MUTANT
  BAR rebuilding the declared:=observed defect and proving the suite goes blind under it.

**0.8.0's counter-finding, accepted and acted on:** my direction-2 test is green on a SYNTHETIC premise --
the fixture injects a master-marker field the real producer **never writes**. Re-verified myself: **0 of 427
partitions carry any marker; "08335338" appears 0 times in any body.** So `incomplete` is correct today but
**STRUCTURALLY UNCLEARABLE** -- and **PRD AC4 is unsatisfiable by construction** (G4 cannot be declared done
by its own criterion). *A fixture can make any state reachable; only the producer can make it reachable in
fact.* Recorded at source + pinned by `test_the_production_clearing_path_is_DEAD` (a test that asserts the
defect on purpose; **when it goes RED that is GOOD NEWS**). The trap it exists to stop: a future agent sees a
stuck `incomplete` after G2, assumes the flag is broken, hard-wires `fresh`, and **launders the exact
undercount the state exists to disclose.** AC4 routed to CTO~B (producer-side, mdpf/G2) -- not mine to carry.

---

## Deployment Sequence + Verification (AE)

```
build-and-upload.sh opal-assets   -> ERROR: UPLOAD NOT VERIFIED (gate FIRED -- see Finding 2)
aws s3 cp (bash) + head-object    -> 7942 / GfqMYehfKfQXFs6zeSvID2Rrb+jLdJPeX1+dau49Tf8=  MATCH
source map                        -> artifact_sha256 + last_deployed_commit 127e7dc0f30e6786a93f240a63dab4970dede482
terraform plan                    -> 0 add, 2 change, 0 destroy
safe-apply.sh -chdir=... apply    -> Apply complete! 0 added, 2 changed, 0 destroyed
terraform plan (re)               -> "no differences, no changes needed"   (0-diff)
aws lambda invoke                 -> 200 {"rows_written":26,"base_rows":14,"ownership_rows":12}
tag + push --follow-tags          -> opal-assets-v0.2.0; HEAD==origin/CLOUD==94fe0c96c
```

**Self-caught error, recorded:** I wrote a **FABRICATED commit sha** into `lambda-source-map.json` by padding
a short hash into a plausible full-length string. Caught it and replaced with the real object
(`127e7dc0f30e6786a93f240a63dab4970dede482`). It would have been invisible -- a well-formed lie in a
provenance field.

---

## Compiler Tools

| tool | result | note |
|---|---|---|
| `comp-iam service opal-assets-daily-emitter` | PARTIAL | Returned its own honest caveats (DESIRED plane; 21 NOT-ATTACHED policy blocks; deny-overlay incomplete). **Correctly NOT cited as evidence either way** -- silence from a parser that never saw the statement is not a green. Grounded on `get-role-policy` + single-ARN simulate instead. |
| `aws iam simulate-principal-policy` (Rule 22a) | **FAIL -> FINDING** | False-denied its own positive control. Root-caused to multi-ARN batching; now CLAUDE.md law @ `7f6611ea7`. |
| `.tools/safe-apply.sh` | PASS | HALT-gate passed; apply 0/2/0. |
| `.tools/commit-gate.sh` | PASS | clean on emitter + new test file. |
| `.tools/deploy_ledger.py` | PASS | opened at deploy-start, 5/5 legs closed, sentinel removed. |
| `.tools/safe-commit.sh` | PASS | surface-check clean; author line held. |

**What worked:** the deploy ledger + safe-apply + commit-gate chain did exactly their jobs. The upload-verify
gate had its first real catch.
**What failed:** the *mandated* IAM instrument (Rule 22a) lied, and `build-and-upload.sh` reported a
successful upload that never happened. **Both were caught by controls, not by the tools themselves.**
**Gap found:** `comp-iam`'s 21 NOT-ATTACHED policy blocks mean it could not see this role's S3 statements at
all -- it returned UNKNOWN, which is honest but leaves the (action,resource) question entirely to
`simulate-principal-policy`, which we now know has two independent false-deny modes. **There is currently no
single trustworthy IAM instrument; only the THREE-PLANE discipline (desired + applied + exercised) is sound.**

---

## Blockers

**None self-owned.** Correctly gated elsewhere:
- **R-A/R-B commit HELD** on `0.8.0_AE_CloudComp`'s v0.2 guard rewrite (his file, his lane; he predicted the
  2 reds and owns them). Evidence: his `061734Z` review -- *"I will MCP you the moment the guard is green."*
  Coordination gate, not a block.
- **AC4 unsatisfiable-by-construction** -> `1.0.0_SA_CTO~B` (producer-side requirement on mdpf/G2).
- **aws-shim ratification** -> `1.0.0_SA_CTO~D`.

## Current State

- `opal-assets-daily-aua` LIVE: 19 partitions / 494 rows / 14 base + 12 ownership each / 0 missing
  `value_class`. Tag `opal-assets-v0.2.0`. Emitter `opal-assets-daily-emitter` (128MB/60s, daily EventBridge).
- Emitter role holds `s3:GetObject` on `opal-data-etfs/daily/*` (prefix-scoped) + mdpf read + DDB write.
  **`opal-data-bd` re-verified `implicitDeny` post-apply -- sovereign hold intact.**
- **UNCOMMITTED (deliberate, gate-clean, 9/9):**
  `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py` (+295/-27) and
  `infra/aws/lambda/opal-assets/tests/test_incomplete_reachability.py` (NEW).
- **LIVE RISK until R-A lands:** a naive `SUM(value)` over a run_date partition returns **$5.82B** against a
  certified **~$1.76B** (3.3x). COO delivered the interim warning to Andrew with the magnitude; I flagged it
  in my own report as a second channel. **R-A makes the safe read the DEFAULT read.**

## Next Steps

- **[0.8.0_AE_CloudComp]** land the v0.2 guard rewrite + fold in his AC7 miswired-axis mutant -> MCP me.
- **[0.7.0_AE_CloudOps~A]** on his green: land emitter + tests + **the 19-partition re-backfill IN THE SAME
  LANDING** (new attributes; a DDB filter on a missing attribute silently omits the row, so `SUM WHERE
  additive` would otherwise be true for only the newest partition -- a silently-wrong AUM number). Then
  safe-apply, exercise, RAVC2 to COO + CTO~B.
- **[1.0.0_SA_CTO~B]** AC4 producer-side requirement (mdpf must emit a master marker or `incomplete` can
  never clear); where the consumer-side enforcing gate lives.
- **[1.0.0_SA_CTO~D]** aws-shim ratification -- recommend dropping the PowerShell hop from
  `build-and-upload.sh` (smallest fix; the shim now makes bash `aws` safe for the base64-SHA case that hop
  was invented to dodge).
- **[Andrew]** deeper P0-A history backfill (still gated on his word).
