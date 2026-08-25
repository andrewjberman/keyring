# Session log -- 0.5.0_AE_OpalETL~B -- 2026-08-25 16:41-23:45Z

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

Seat 2 of 2 on MDPF_COTREMEDIATION (AE leg). Two deploys landed and closed; a third prepared and
held. Serial registered 16:41Z, watcher armed (task b1l4muiex), zero crons.

---

## 1. WHAT LANDED

### Deploy 1 -- silver blackdiamond, the 21-column holdings contract
The outage's proximate cause: WE amended the Black Diamond holdings template (@`17c38a26f2`,
0.6.2_AE_PartnerETL, under a CTO pin) and the silver contract was never told. `assert_declared_header`
refused correctly for four trading days. **Not vendor drift.**

DS~M authored the contract edit @`288807f747`; my leg was vendor -> build -> apply -> verify.

### Deploy 2 -- mdpf-gold-lambda, the clause-(vi) membership fix
Global stayed dark after deploy 1 because its GOLD had not rebuilt since 2026-08-20. DS~N's fix
@`1234c8779e`. **The mainline pin also carried D1_CATVIEWS (6 commits, +15,275 B on the
consolidator), which restructures the emission axis of `aggregate-aua-timeseries` -- the artifact
under repair.** COO ruled Path A: a hotfix pin excluding it.

### Prepared, NOT applied -- D1-i-2 (D1_CATVIEWS path-to-live)
Plan @`3c911ed292`, amended to NO-SHIP @`6a257c5b59`.

---

## 2. DEPLOYMENT SEQUENCE + VERIFICATION (AE role section -- actual output)

### Deploy 1: opal-assets-silver-blackdiamond
```
targeted vendor (mirror_schemas.py ONLY -- NOT the full vendor-manifest run)
  two-home md5   85fc671e92ba56491419713c93845b15 -> 8818df2f03bad80601fdefc11f54c3db (both)   COTR-b-3a
import-closure   default OK 9 files | --sources OK 9 files                                     COTR-b-4
build            single-function mode; write VERIFIED size=57707, sha256 metadata match
apply            safe-apply targeted; HALTGT 1 routine msg, HALT_ACK=1
0-diff           "No changes. Your infrastructure matches the configuration."
COTR-c-2, DEPLOYED PACKAGE BYTES (downloaded post-apply, AST-read):
  ("blackdiamond","holdings") declares 21 columns
  'Account Supervised' idx 8 (immediately BEFORE 'AssetID' idx 9); 'Holding Supervised' idx 20
  negative control 'Zzz No Such Column 9999' -> 0
  member diff vs pre-apply: 21 compared, CHANGED 1 (mirror_schemas.py), UNCHANGED 20
```

### Deploy 2: mdpf-gold-lambda
```
hotfix pin       530ba66971  = DS~N's 1234c8779e cherry-picked onto DEPLOYED pin 1daf1913dd
                 minted in an EPHEMERAL DETACHED WORKTREE (shared checkout -- a branch switch on the
                 main tree moves every other seat's tree); torn down after build; mainline untouched
                 risk-free by measurement: spine at the deployed pin is BYTE-IDENTICAL to the fix's
                 parent (both 171,111 B / a7db07bb68f465d5)
scope            21 pairs, 21 comparable, 0 unresolved -> CHANGED 1, UNCHANGED 20
                 consolidator 55,629 B sha256 8da6c0a19480fd98 == DEPLOYED, scopes_for 0
ship gate        0.4.0_DS_ClientPlatform~N PASS through the PRODUCTION entry point (71267)
upload           VersionId r819XZni2appiJCYjDj4ack.BzFrBnJq, 684,807 B,
                 metadata content-sha256=5154f95d...f69887  (verified by live head-object, not cp rc)
plan             s3_object_version + source_code_hash both moving; "0 to add, 1 to change, 0 to destroy"
apply            "Apply complete! Resources: 0 added, 1 changed, 0 destroyed."
0-diff           "No changes. Your infrastructure matches the configuration."  (SCOPED -- see blockers)
live             CodeSha256 UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=  == the value PREDICTED in
                 the ledger BEFORE the upload.  LastModified 2026-08-25T19:38:55Z
DEPLOYED PACKAGE BYTES (downloaded post-apply):
  in-zip manifest pin 530ba66971
  spine        175,795 B  md5 952bbc16ea07ed14cf51a497f1b4cde5  count_membership 14 OCCURRENCES
  consolidator  55,629 B  sha256 8da6c0a19480fd98               scopes_for 0 OCCURRENCES
  member diff vs pre-apply: 21 compared, CHANGED 1 (the spine), UNCHANGED 20
  negative control 'Zzz_no_such_symbol_9999' -> 0
comp-lambdamap reconcile-deployed (scoped): 1 already-in-parity, 0 HELD
```

**Ledgers:** `mdpf-cotremediation-ae-silver-bd-contract-20260825.md` (17:07:45Z -> 17:24Z) and
`mdpf-global-gold-lambda-hotfix-20260825.md` (19:35:11Z -> 19:41:37Z). Both opened at deploy-start,
both closed in-session, nothing stranded.

---

## 3. COMPILER TOOLS

| Tool | Purpose | Result |
|---|---|---|
| `comp-which` | route "what consumes s3://opal-data-mdpf/code/" | PASS -- near-tie, named `comp-find` as the fallback |
| `comp-find` | mirror_schemas / rebalancer_schemas import sites, `code/scripts/silver`, `opal-data-mdpf` | PASS -- denominators printed throughout |
| `comp-whoread` | who ACTUALLY read the mdpf code prefix | **FAILED CLOSED (correct)** -- zero object-level data events since 2026-05-11 |
| `comp-lambdamap reconcile-deployed` | scoped half-landed detector post-apply | PASS -- 1 already-in-parity, 0 HELD |
| `comp-pipescript deployed` | deploy-currency sweep | PARTIAL -- its silver denominator is `opal-data-bd/code/silver/` (15 objects), OUT OF SCOPE for the mdpf `code/scripts/silver/` question |
| `comp-registry` / project JSON | confirm MDPF_COTREMEDIATION survived the 101-project sweep | PASS -- status=active, directive=D8, correctly excluded |

**What worked:** `comp-find`'s printed denominators caught two of my own bad queries before they
became findings. `comp-whoread` failing closed rather than returning a clean zero is the single best
tool behaviour I saw tonight -- an empty who-read there would have been a false ABSENT.

**What failed:** my `comp-find` pattern `'import mirror_schemas\|from mirror_schemas'` returned
**0 hits** -- `comp-find` does not take `\|` alternation, so the pattern COULD NOT MATCH. The zero was
an instrument artifact. Re-run as plain tokens: 144 and 129 hits. Caught only by disbelieving a zero
I had reason to doubt.

**Gap found:** `opal-data-mdpf` has NO CloudTrail object-level data-event selector, so **no
who-read question about that bucket can ever be answered from the trail.** Routed as a coverage gap
(explicitly NOT as an alarm -- moratorium).

---

## 4. FINDINGS SURFACED (measured, not inferred)

1. **The standard re-vendor would have shipped a 33-day undeployed feature.** `vendor-manifest.sh`
   copy mode has no module filter, so the P0 deploy would have carried the entire 3F-S5 provenance
   sidecar. Refused on measurement, escalated rather than decided. Ruled targeted-vendor.
2. **A dirty TF root on BOTH pipelines.** opal-assets read 4 changes (only 1 mine, incl. a gold-prefix
   repoint on the emitter); mdpf-pipeline reads 1 (`aws_s3_object.mdpf_route_bindings`, not mine, and
   verified NOT D1_CATVIEWS-coupled). Both applies targeted; both 0-diffs consequently SCOPED.
3. **`record-terraform-deploy.sh` would have written 6 FALSE deploy records** -- dry-predicted, not
   run. It scopes by PIPELINE with no notion of a targeted apply; 2 of the 7 were fabricated from
   `None`. Both source-map records were hand-scoped instead.
4. **The source map drifts silently and NOT uniformly**: silver-blackdiamond had the DATE wrong and
   the SHA right; mdpf-gold-lambda had BOTH wrong. Instances closed; class routed to D0/NFRA_DEPLOYLEDGER.
5. **S3 code-prefix trace** (Andrew-direct): `code/scripts/silver/` IS consumed -- EC2 dispatch
   `:125` syncs `--delete`, `:546` puts it on the cottonwood PYTHONPATH, `build_dim_model_portfolio.py:81`
   imports `rebalancer_schemas`. The `mirror_schemas.py` 404 is a TRUE non-member: safe by DEPLOYMENT
   SCOPE (2 of 38 files deployed), not by import absence -- which is more fragile than it sounds and
   is an ARMED latent if anyone deploys that tree.
6. **The scheduled-vs-manual instrument**: `AWS/Scheduler InvocationAttemptCount`, payload-independent,
   both arms exercised on the night's own data (deliveries at 12:50/13:30/13:40/13:50; the 19:00-20:00
   window EMPTY despite two known manual invokes). Refined by peers: no `ScheduleName` dimension
   exists, and 5-minute bins are load-bearing (hour buckets collapse floor+accrual+publisher).
7. **D1_CATVIEWS BRICKS the lambda** (DS~N's find, re-derived here): `mdpf_category_registry.py` is
   imported top-level and is not in `build_package.py`'s PACKAGE list. **`import-closure-check.py`
   catches it (true rc=1) and the GOLD builder does not run it, while the SILVER builder does
   (`build-and-upload.sh:257`).** Remedy is build-ladder rung 2 -- wire the existing check -- but NOT
   as-is: the gold manifest says `layers_expected` where the checker reads `layer_dependencies`, so
   unchanged it fails every correct build on 4 false positives, and a gate that screams gets switched off.

---

## 5. CORRECTIONS I MADE AGAINST MYSELF

Recorded because the pattern is the useful part, not the individual errors.

- **Amplified DS~N's "doubly-owned edge" as the real finding.** It was two authorization chains ~40s
  apart, both legitimate. Withdrawn, not softened. I also called the no-op luck; it was
  `conditional_put`, a designed control.
- **Declined a credit COO gave my member-diff.** It provably CANNOT catch a missing module -- a module
  absent from both packages never surfaces in a pre-vs-post diff. Accepting it would have put a false
  guarantee under the next deploy, and it would have been believed because it was flattering.
- **Corrected COO's credit for my "voluntary" corroboration downgrade** -- the rider had landed 20
  minutes earlier; that was compliance, not supererogation.
- **Overstated the S7 hazard as general.** `spawn-agent.ps1` performs ZERO git operations and all live
  watchers resolve to 1 root, so a seat spawned on this box sees local commits. The gap is exactly
  one device wide.
- **Repeated "10 commits local, nobody pushing" three times after it went stale.** Measured: 5 of 10
  were on origin. A self-subject claim restated from memory.
- **Read `rc=0` off a pipe** on `import-closure-check.py` when the checker returned 1 -- 40 minutes
  after writing about that exact trap. The lesson does not transfer by knowing it; only the
  capture-then-read habit does.

---

## 6. BLOCKERS

**None held by me.** One declared consequence, not a blocker:

- **Both post-apply 0-diffs are SCOPED, not root-clean**, because both TF roots carry other agents'
  unapplied changes. Evidence: opal-assets plan `0 to add, 4 to change, 0 to destroy` (3 not mine);
  mdpf-pipeline `0 to add, 1 to change, 0 to destroy` (not mine, and the identical rider was excluded
  from the 2026-08-19 rebuild of the same Lambda). A residual root row is not this work's leftover.

---

## 7. CURRENT STATE (written for zero prior context)

- **`opal-assets-silver-blackdiamond`** runs the 21-column BD holdings contract. CodeSha256
  `XiJ6ZADpVAwtJcRR4U0l/IhO4+eFfzost0Mz9fnTIJA=`. Source of truth
  `data/assets/scripts/silver/mirror_schemas.py`; vendored copy in
  `infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/`.
- **`mdpf-gold-lambda`** runs the clause-(vi) membership fix at pin `530ba66971`, D1_CATVIEWS
  deliberately ABSENT (`scopes_for` = 0 in the shipped bytes). CodeSha256
  `UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=`. Artifact
  `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip`, VersionId
  `r819XZni2appiJCYjDj4ack.BzFrBnJq`. Pin anchored by LOCAL tag `mdpf-gold-hotfix-pin-20260825`
  -- **peel with `^{commit}`; the tag OBJECT sha `9165a40d0e` is NOT a valid pin.**
- **Global is RESTORED**, served `as_of_last=2026-08-24`, `source_keys` advanced. **The restore act
  was `1.0.0_SA_CTO`'s ad-hoc invoke at 19:42:5xZ on Andrew's direct word -- NOT mine and NOT DS~N's.**
- **`BUILD_MANIFEST.json`** (silver-blackdiamond) carries two disarm keys I landed:
  `vendor_parity_expected_red` (@`a3fb502194`, the 2-of-8 red parity gate) and
  `deploy_precondition_S7` (@`24d7c5a465`, the S5/S7 armed coupling).
- **11 commits at this seat**, all verified by HASH lookup with a firing negative control.
  a3fb502194 a7777bc84d d3f760136b 8c6e1c5af1 5472f32bbc 445aac9002 c032c26f73 24d7c5a465
  3c911ed292 6a257c5b59 + this log. **5 of the first 10 were on origin/CLOUD at last measure; the
  rest ride integration.** Integrator is gate-enforced MSTR-only and MSTR has no live session.

---

## 8. NEXT STEPS

- **[`1.0.0_SA_CTO`]** Holds the 2026-08-26 13:30Z scheduled acceptance. Three legs, none relying on
  the forgeable `trigger.kind`: Scheduler datapoint in the **13:30 5-minute bin** (`sum = 0` is the
  conclusive direction); the gold object's own result (an ATTEMPT count is not a success); the served
  payload on **data-bearing leaves only** -- a raw-byte sha256 compare FALSE-FAILS because
  `_provenance.written_at` moves daily.
- **[`1.0.0_SA_CTO`]** Rule the source-map `last_deployed_commit` convention: I set it to the BUILD
  PIN `530ba66971`, which is NOT CLOUD-reachable, deliberately -- it is the only commit whose tree
  matches the deployed package. `verify-local` will read deployed != HEAD, and that is TRUE.
- **[`0.7.0_AE_CloudOps`]** S5 twin remediation (seated by COO). **Read
  `deploy_precondition_S7` in BUILD_MANIFEST.json BEFORE shipping -- shipping S5 is what arms S7.**
- **[`0.4.0_DS_ClientPlatform~N`]** D1_CATVIEWS correctness read continues; deploy-readiness is
  already answered NO on packaging.
- **[`2.0.0_SA_COO`]** D1-i-2 release decision. Two holds now, and they do not expire together: the
  acceptance confound lifts after 13:30Z; **the packaging defect does not expire on a clock.**
- **[unowned]** Wire `import-closure-check.py` into `build_package.py` -- align the manifest key first.
