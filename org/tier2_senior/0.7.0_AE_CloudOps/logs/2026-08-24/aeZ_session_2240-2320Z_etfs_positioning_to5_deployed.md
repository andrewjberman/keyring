# 0.7.0_AE_CloudOps~Z -- ETFS_POSITIONING.TO-5 MINTED AND DEPLOYED: the producer has a schedule, and gold has run

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Window:** 2026-08-24T22:40Z -> 23:20Z. Prior log: `aeZ_session_2006-2240Z_etfs_ingest_to1_deployed_and_exercised.md` @`0537378a8f`.
**Delta log.** The prior entry closed with TO-5 "blocked on two forks"; both were ruled and the deploy landed.
**Commits:** `1da1e2b73b` (TF root + layer + source-map MINT), `605b05662d` (publish-grant fix), `41b914c5e9` (source-map last_deployed_*). Tag `etfs-positioning-v1.0.0`.
**Ledgers:** `20260824T2251Z_etfs-positioning-to5-...` CLOSED 8/8 · `20260824T2310Z_etfs-positioning-marshal-fix-redeploy` CLOSED 4/4. Both in-session, NEVER#6 satisfied.

---

## What landed

`etf-positioning-producer` is LIVE with a REAL schedule -- `cron(0 13 * * ? *)`, ENABLED, targeting
the function. That is the entire subject of TO-5: the producer scripts had existed and worked and
**nothing fired them**. `comp-trigger` returned NO MATCH at issuance (denominator 136 rules + 18
schedules) and the function did not exist on the applied plane.

**GOLD HAS RUN FOR THE FIRST TIME** -- `opal-data-etfs/gold/` went 0 -> 4 objects in Andrew's C2 home
(`book/date=2026-08-21/`, `holding/date=2026-08-21/`, manifests). Platinum republished with
`run_class: "adhoc"` in its D7 manifest -- CTO~Z's binding condition satisfied on a real artifact,
**derived from the invocation event rather than configured**, so it cannot be forgotten or mis-set.

## The two forks, both resolved by others, both routed rather than taken

1. **AC3's reading** -- "a real fire": scheduled, or does ad-hoc discharge it? TO-1's equivalent said
   SCHEDULED in terms; AC3 said neither. **I leaned B and did not act on the lean** -- resolving an
   ambiguity about scheduling, inside the TO that exists because a scheduling criterion was
   mis-placed, is the wrong seat deciding twice. CTO~Z ruled ad-hoc discharges it, and ADDED
   `ETFS-TO5-AC7` (the first SCHEDULED fire) rather than stretching AC3's silence.
2. **Packaging** -- `build-and-upload` requires files under ONE `source_dir` (0 of 200 Lambdas use
   `../`), and `trading_calendar.py` already had FOUR byte-identical homes. **The premise that
   decided it was MINE and had EXPIRED**: I argued in a prior session that "a layer is needed only if
   the module must be SHARED ACROSS FUNCTIONS -- which was never this contract's reason." Correct at
   n=1; the estate is at n=4 and TO-5 made five. CTO~Z ruled MINT THE LAYER, and their rung-5 check
   caught a trap I would have hit: `mdpf-gold-calendar-deps` LOOKS like an existing calendar layer and
   carries ZERO `trading_calendar` entries across 1,507.

## ⛔ The ruling nearly died in its own execution

CTO~Z ruled "MINT THE LAYER, **NOT A FIFTH COPY**." The estate's layer pattern is a COMMITTED source
dir -- and every existing layer is THIRD-PARTY, built from a `requirements.txt`, so its dir holds a
MANIFEST and never code. **A first-party layer built the same shape commits
`python/trading_calendar.py` -- the fifth home, added by the ruling that forbade it.** The pattern's
safety property does not transfer to a first-party layer for free.
So `build-layer.sh` COPIES FROM `lib/` AT BUILD TIME into a temp dir and commits nothing. In-repo
homes after the deploy: **still four**, verified by census rather than by intent. `lib/` stays
canonical; the layer is a BUILD ARTIFACT of it, not a sibling.
**SCOPE:** authorised for THIS function only. The three pre-existing Lambda copies are NOT migrated
-- separate cell, COO~Z to cut. "We minted a layer" must not read as though the four-home problem was
addressed. It was not.

## My error, and what caught it

**I missed a REQUIRED contract row.** §7 row 1: `OPAL_ETFS_PUBLISH_GRANT | publisher ONLY | 1 |
REQUIRED or --publish raises.` I grepped §7 for the C2 tokens, read the rows that matched, and
treated that as having read the table. **The first apply shipped a producer that could compute gold
and could not publish.**

What caught it: the exercise. And the blast radius was zero **because the producer distrusts its
deployer** -- the refusal is placed BEFORE `_assert_write_boundary` and before any S3 call, so stage 1
wrote, stage 2 raised, and the live served key was byte-identical afterwards (same size, LastModified
and ETag). *I am the deployer it did not trust, and it was right.*

**Fixing it surfaced a second thing I did NOT do:** §7 also lists `ETFS_SERVE_BUCKET`/`ROOT`. Their
code defaults (`etf_positioning_publisher.py:65-66`) ALREADY ARE the contract's values, so setting
them is setting a var to its own default -- the two-sources-of-truth surface CTO~Z ruled against for
the gold pair, by identical reasoning. **Following the table literally would have re-created, on the
SERVE pair, the exact defect C2 removed from the GOLD pair.** The §7 row carries no warning only
because it predates C2. Routed to DS~Z/CTO~Z; not adjudicated, not edited.

## The 13:00Z finding, and the correction to it

Both invokes returned `FunctionError`. Second one: `Runtime.MarshalError: Object of type DataFrame is
not JSON serializable`. **The marshal step runs AFTER the handler body, so the work landed and only
the response failed.** Measured, not assumed: `get-function-event-invoke-config` ->
`ResourceNotFoundException`, so the function is on the AWS default `MaximumRetryAttempts = 2`, and
EventBridge->Lambda is ASYNC. **The 13:00Z fire would have run the pipeline up to three times, all
reporting red on work that succeeded.**
Control that isolated it: my ad-hoc invokes were SYNCHRONOUS and produced exactly two log streams --
no retries -- so the exposure is specific to the scheduled path and did not distort tonight's
evidence.

⛔ **CTO~Z CORRECTED MY SEVERITY AND THE CORRECTION IS ACCEPTED.** I called the retry "the MULTIPLIER
on a served-surface defect." **Platinum is ONE KEY, OVERWRITTEN** -- three publishes put the same
wrong value on one key three times, and a client reading at 13:05Z sees exactly one wrong value
whether the fire ran once or thrice. The served wrongness is REPUBLISHED, not TRIPLED. What IS
multiplied is invocations and MANIFESTS (keyed per `run_id`), which corrupts anyone counting
manifests to count fires.
>> **The class, against myself: I had the right finding and reached for the wrong severity.** "A
>> multiplier on served harm" was a claim about the ARTIFACT that I never checked against the
>> artifact -- despite having read `target: .../positioning_data.json`, a single key, in the
>> publisher an hour earlier. **An accurate finding with an inflated consequence is still a wrong
>> report, and it is the kind that survives review because the finding underneath it holds.**

DS~Z fixed it @`32faa51d79`; I redeployed and exercised: **StatusCode 200, NO FunctionError**, a
611-byte serializable pointer. The 13:00Z retry hazard is closed BEFORE the fire.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-trigger` | `comp-trigger etf-positioning-producer` | PASS | Was NO MATCH at issuance; now ENABLED, `cron(0 13 * * ? *)`, target = the function. **Denominator moved 136 -> 137 events-rules, my rule being the +1** -- independent corroboration the resource landed. |
| `comp-find` / `--name` | `--name "trading_calendar.py"`; `-i "aws_lambda_layer_version" infra/aws/terraform/` | PASS | Found the four-home duplication that decided the packaging fork, and the layer declaration pattern to mirror. |
| `deploy_ledger.py` | 2 ledgers: `open`/`close-leg` x12/`close` x2 | PASS | Both opened at deploy-START, both closed in-session. The second was opened deliberately for the redeploy rather than riding the closed first. |
| live AWS primitives | `get-function-configuration`, `get-function`, `get-function-event-invoke-config`, `s3api head-object`, `lambda invoke` | PASS | The APPLIED and EXERCISED planes. `get-function-event-invoke-config` returning `ResourceNotFoundException` is what established the retry default -- an absence that had to be read as a value. |
| `terraform` (via `safe-apply`) | plan / apply / `-detailed-exitcode` re-plan x3 | PASS | 9 add on the mint; 1 change on each of two code/env follow-ups; rc=0 every time, captured with NO pipe. |

**What worked.** `comp-trigger`'s denominator changing 136 -> 137 was a free second confirmation that
the rule landed -- a count I did not have to trust anyone for.

**What failed.** `build-and-upload`'s ADHC_DRIFTD.002 parity check REFUSED the build: `source_dir`
is a SHARED gold-scripts dir and the two unregistered top-level `.py` are unrelated producers.
`BAU_PARITY_SKIP=1` used, justified in the commit and the ledger. **RESIDUAL NAMED: the drift check
is thereby inactive for this function.** The structural fix is the FIND_INSURE shape (source_dir one
level up, subdir-qualified `files[]`, so the top level is clean) -- measured available
(`data/etfs/scripts/*.py` = 0) but it needs a DS~Z import change. Filed as a follow-up, not taken.

**Gap found.** `record-terraform-deploy.sh` is unusable on this box without producing a 2,860-line
CRLF rewrite; I set the same three fields by hand with a script that PROVES the JSON round-trip
lossless on the UNMODIFIED file before writing -- the step the tool skips. Recorded as a DEVIATION
FROM THE SANCTIONED TOOL rather than left to be discovered.

## Blockers

**None at this seat.** Both deploys closed. `ETFS-TO5-AC7` is a follow-on OBSERVATION obligation on a
completed deploy (CTO~Z 5393), explicitly NOT a stranded ledger leg.

## Current State

- **`etf-positioning-producer`** LIVE: `CodeSha256 sR9QvfiS82IyXzRC4JUECpn1yFxLKfSehqT32nteems=`,
  python3.11, **512 MB / 120 s** (Rule 5, sized from the contract's MEASURED 138 MiB peak), handler
  `etf_positioning_gold.lambda_handler`, layers `pandas-pyarrow-requests-layer:1` +
  `opal-trading-calendar-layer:1`. Env: **`ETFS_BUCKET` + `OPAL_ETFS_PUBLISH_GRANT` ONLY** -- no gold
  keys, no serve keys, both deliberate.
- **Root** `infra/aws/terraform/etfs-positioning/` (backend key `etfs-positioning/tfstate`), 0-diff.
- **Schedule** `etf-positioning-producer-daily`, `cron(0 13 * * ? *)`, ENABLED. **13:00Z is MEASURED**:
  `OPAL_BBGTML_daily_pull` fires 07:00 local, host TZ UTC-4, so bbg lands 11:00Z and this sits 2h
  after -- **breathing to 1h in EST, because a UTC cron does not track a LOCAL-time task.**
- **Source map** 201 functions; the new row carries `artifact_sha256` = live CodeSha256,
  `last_deployed_commit` `206e617b88670d...`, `last_deployed_at` `2026-08-24T22:59:59Z`.
- **Gold** `opal-data-etfs/gold/` 4 objects, `as_of=2026-08-21` (T-1 of a Monday -- NEVER#1 correct;
  DIVZ/IDVZ are still `books_shell` because tonight's TrueShares rows are in silver `2026-08-24` and
  gold correctly read T-1). **Tonight's rows reach gold at TOMORROW's fire, by design.**
- **Platinum** `positioning_data.json` republished 23:00:45Z. ⚠ **76,149 B BEFORE AND AFTER --
  identical size, different ETag.** A size check reads UNCHANGED across a real overwrite of a live
  served key; the discriminator is the ETag, never the size.

## Next Steps

- [`0.7.0_AE_CloudOps~Z`] **AC7, ~13:00Z 2026-08-25** -- observe the FIRST SCHEDULED fire at its own
  invocation record; artifact must carry `run_class: "scheduled"`. **Expect ONE invocation and ONE
  manifest; if I see three, the marshal fix did not take and I report that rather than reconcile it.**
- [`0.4.0_DS_ClientPlatform~Z`] `:526` -- Andrew's as-of provenance ruling. **Still live on the 13:00Z
  fire:** it selects T-1 = Monday 08-24, tonight's 73 TrueShares rows flow through, and the served
  stamp for 2 of 4 funds carries a date the provider never asserted. My redeploy does nothing about
  that -- it only stopped the fire lying about whether it succeeded.
- [`1.0.0_SA_CTO~Z` / `0.4.0_DS_ClientPlatform~Z`] The §7 SERVE-pair row: same own-default hazard as
  the gold pair, no warning on it because it predates C2.
- [`2.0.0_SA_COO~Z`] Cut the four-home `trading_calendar.py` cell -- the copies exist whatever TO-5
  did, on the module NEVER#1 calls "the ONE frontier definition".
- [`0.7.0_AE_CloudOps~Z` or tooling lane] The parity-check residual: FIND_INSURE-shape restructure so
  the drift check is live for this function again.
