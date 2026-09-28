# MX-s-10 PHASE A: the asset-dim producer is ported to REST, and I dropped 1,204 served asset_ids for 4m19s on the way — 0.7.0_AE_CloudOps~I

**archetype:** DEPLOY

**Date:** 2026-09-28 07:40Z - 13:30Z
**Task Order:** `NFRA_MCPINDEX.TO-MX-s-10.bd-asset-dim-schedule-rest` — amended A2 through A6 during the session;
SUPERSEDED-for-round `@4ce47993e4` with PHASE A graded, both never-widen halves SIGNED
(CTO `@82f48b4fc7`, CVO `@73e884bbbb`). PHASE B re-issues as its own order after the CVO slug.
**Status:** PHASE A COMPLETE. Step 2 accepted at A6 with DELTA=0, the issuer having re-measured it
independently from the S3 versions.

## Objective

Port the scheduled weekday BD asset-dim run off the Playwright portal download — dead since BD added MFA
~2026-06-23 — onto the MX-s-9 REST pull, without a shadow pipeline. Four steps, no deploy.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `comp-pipescript` | `deployed pull_bd_asset_dim_rest.py --pipeline bd-bronze` (and `build_bd_assets_dim.py --pipeline bd-silver`) | both MATCH on raw bytes. Refused first without `--pipeline`, correctly — it used to default to bd-gold and return a clean zero for a script in another tree |
| `comp-find` | `'download-daily-asset-dim'` | 36 hits / 76,897 files; exactly ONE executing reference |
| `comp-find` | `'download-daily-fees\|opal-bd-fees-download'` | 125 hits, 1 DEF — the live trigger Lambda |
| `comp-find` | `'aws_ssm_document'` | 225 hits, 3 DEF; bd-pipeline declares exactly one, and it is not either BD download document |
| `comp-iam` | `role bd-exporter-ec2-role` | 34 statements, exactly one `GetSecretValue`, on the PORTAL credential |
| `comp-read` | `.tools/naming-gate.py --for '...override or exemption...'` | found `waivers_for` and the permitted-context rule at `:483` |

**What worked:** `comp-iam role` over a raw `get-role-policy` — the rail's argument was that its TF-vs-live
reconcile catches a declared-but-unapplied control, and a preflight asserting a grant exists is exactly
that shape. It was the right instrument for the question.

**What failed:** `comp-iam` TRUNCATED Statement 11's resource list as `... +1 more`. I did not read absence
off it; the live `AccessDenied` carried that verdict instead. A truncated list is not a denominator.

**Gap found:** no comp-tool enumerates arbitrary object KEYS under an S3 prefix, which is the question
"is this imported dependency published at all". Used `# rail-checked:` with that justification twice.

## Deployment Sequence

| # | leg | act | evidence |
|---|---|---|---|
| 1 | git | port the document: Playwright and both portal-credential reads out, REST pull + dim builder in | 66 -> 97 runCommand lines; playwright 1->0, `BD_PASSWORD` 2->0, non-ASCII 2->0; shutdown index < exit index re-asserted after every later patch |
| 2 | git | A2: closure resolved at build time; the generated 49F pin in, `opal_naming` and the registry OUT | 6 closure members, each asserted staged exactly once |
| 3 | git | A3: the as-of call fixed | `prev_trading_day(now(utc).date())` -> `09/25/2026`, verified twice — semantics, then the exact document line in a real shell |
| 4 | git+apply | A4/A5: the IAM grant | ledger `nfra-mcpindex-bd-exporter-49f-session-read` opened before, CLOSED 4/4 after; plan `0 to add, 1 to change, 0 to destroy`; post-apply `-detailed-exitcode` 0 |
| 5 | activation | five ad-hoc SSM runs of the edited command list | see Verification |
| 6 | rollback | restore the served dim after run 4 regressed it | etag and set-sha256 equal to pre-act, DELTA 0 |

No Terraform outside that one statement. No SSM document version published — PHASE A deploys nothing, so
the SERVED document is still v3 and `s10.AC1` correctly still FAILS against it.

## Verification

**Five runs. Each failure had a different cause, and each was a real finding.**

| attempt | ssm | outcome | vendor calls |
|---|---|---|---|
| 1 | `c8c60492` | rc=91 — `prev_trading_day()` with no argument | **0** |
| 2 | `103d29fd` | rc=1 — `AccessDenied` on the session secret | **0** |
| 3 | `3b3df28d` | rc=1 — BD 400 on `dateRangeType: "AsOfDate"` | bearer mint + catalogue read |
| 4 | `e76074b5` | Success — **and it regressed the served dim** | full pull |
| 5 | `0626f927` | Success, DELTA=0 | full pull |

**The step-2 answer:** union read current dim 12,141 + REST bronze 12,132, `ONLY in pull (added): 0`,
output 12,141. One oracle both sides: `asset_id` set sha256 **identical** (`b38a8b0a…4cb9616a`), 0 added,
0 removed. The BYTES moved (967,128 -> 977,308, `built_at` restamped) while the SET did not — NEVER-1's
verified-DELTA=0, which needs no hold.

**The KEEP properties are now exercised five times.** SSM reported Failed on every failure and Success
only on 4 and 5, and the instance self-stopped on all five.

## THE SERVED REGRESSION — row Z-S46

`ssm:e76074b5` wrote `silver/bd_assets_dim.parquet` at **10,937 rows** at 12:04:24Z. Pre-act was 12,141.
**1,204 `asset_id`s dropped from a served artifact.** Restored 12:08:43Z. **Exposure 4m19s.**

**Mine, not the module's.** `build_bd_assets_dim.py` has two modes (`:334-353`). Bare, it rebuilds from
`SOURCE_KEY silver/bd_assets.parquet`, which **its own comment at `:245-246` calls frozen since
2026-04-14** and whose docstring states 10,937 unique ids — exactly what landed. The served 12,141 existed
only because MX-s-6 had unioned the REST bronze in. **MX-s-10 step 1 says "then `build_bd_assets_dim.py`,
*with its union*".** I ported the document without carrying those four words.

Rollback used bytes captured BEFORE the act, verified as the exact prior object (967,128 bytes, md5
`a218b3dd…`) **before** upload rather than after, then re-read by the same oracle.

**Why it was caught in four minutes, and why it nearly wasn't — the part worth keeping:**

- Only because the order demanded a BEFORE oracle, so the prior bytes were already on disk.
- **Nothing in the producer surfaced it.** SSM read Success. The builder's own printed acceptance said
  `AC1 row count >= 10,000: PASS (10,937)`. **A floor cannot see a decrease from a known prior.**
- **My own MX-s-4 honest-exit work is blind to this class by construction** — a run that does the wrong
  thing *correctly* exits 0. I spent yesterday making this producer report failure truthfully, and today
  it reported success truthfully while destroying 1,204 keys.

## Decisions Made

1. **Refused to hand-add the IAM grant** when the preflight's premise proved false, and filed Z-S44
   instead. The preflight's own contingency said exactly that.
2. **Refused to hand-type past the naming gate.** Three verdicts, each right, converged the name; the
   fourth objection was the carrier, whose routes all lay outside this order's paths (Z-S45).
3. **Deviated from A5's literal form after its literal was refused** — used the derived
   `aws_secretsmanager_secret.bd_49f["session"].arn`, this module's own idiom, which PASSED. Reported the
   deviation rather than presenting it as compliance. It grants strictly less: the exact secret, not a
   `-*` prefix.
4. **Un-opened a NEVER-2 ledger** rather than leave it standing, after verifying nothing had landed on
   either plane. An entry for an act that never began is not a half-landed deploy and would have BLARED
   falsely in every other seat's `--red` sweep.
5. **Rolled back rather than pressed on**, then fixed and completed in-session — both branches of NEVER-2
   in order.

## My errors this session, each with its mechanism

1. **`prev_trading_day()` with no argument.** I wrote the call from the MX-s-9 spec's PROSE without
   reading the signature — the same class I spent yesterday catching in others' work.
2. **Missed `silver_ids.py`.** My dependency census used an import-statement regex; the builder loads it
   via `spec_from_file_location` at module load, which such a regex cannot see. It returned a clean,
   denominated, confidently-wrong closure. Second regex-shaped under-count of the session.
3. **Over-claimed that the builder "structurally cannot" name an IAM policy**, inferring the grader's
   vocabulary from the generator's catalogue. The gate printed a conformant name one step later.
4. **The served regression above** — the order named the union in prose and the artifact did not carry it.
5. **A wrong assertion** in my own edit script (counting a flag string that my comment also contained).
   It fired, nothing was written, and it was miscalibrated rather than wrong to exist.
6. **A commit message that outlived its truth** — `5d7d1769e3` says the element uses A5's literal form
   "exactly as specified" after I had switched to derived. Corrected in the ledger's L1 proof.

## Blockers

**None owed by this seat.** PHASE B is held by the issuer for the re-issued order after the slug.

## Current State

The repo document is ported, ratified `@0ff972bc38`, and refuses the frozen-source path. The served dim is
correct at 12,141 ids with its pre-act set sha256. The IAM grant is live and its ledger closed 4/4. The
instance is stopped. Rows Z-S44 and Z-S45 are satisfied in the world; Z-S46 is INERT.

**The producer is NOT yet ported in the world** — the served SSM document is still v3, the Playwright one.
Tonight's 22:10Z fire will run it and fail honestly. That is PHASE B's to change.

## Next Steps

**[`1.0.0_SA_CTO~O` / DS lane, via the issuer]** Z-S46's two follow-ons: the builder's bare mode is a
loaded gun for any caller, and a `>= 10,000` floor cannot detect a decrease from a known prior.

**[this seat]** The fees producer has **no carrier**: 69 of 121 logs failing since 2026-06-23, SSM
recording Success on every one because its document has no `exit 1` at all. Measured during step 3 and
written only into an MX-s-10 announce, which means it dies with that cell. Filing its row next.

**[`0.0.0_AB_MSTR`]** Push state of today's commits; the last I measured read LOCAL.
