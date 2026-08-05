# 0.7.0_AE_CloudOps~A — INF gold 5-day outage: root cause, verification, AE-lane fix (1500-2155Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, IMPLEMENT, COORDINATE

## Summary

Andrew-directed investigation of the `inf-gold-chain-failed` alarm. Established root cause,
verified the proposed durable fix before proposing it (Andrew-required), obtained the sovereign
ruling, landed the AE-lane half, and prepared the deploy leg. **The outage is NOT resolved** — it
is now blocked on a CTO/COO serve-hold release, not on diagnosis or code.

The user's opening hypothesis (a cookie/auth problem in bronze) was refuted on evidence, not
dismissed: every Orion pull step reported `ok`, the JWT was valid 5h, and silver api_dims landed
fresh daily throughout the outage.

## Window

1500Z session start (registration + watcher arm) -> 2155Z. First log this session.

## What the alarm actually is

`inf-gold-chain-failed` watches CloudWatch `Inflection/GoldChain.ChainFailed`, dim
`Service=inf-gold-layer-runner`, emitted by `data/inf/scripts/gold/orion-gold-dispatch.sh:173`
on any non-zero gold-chain exit. It is scoped to the GOLD chain only; it carries no information
about where or why, and has zero visibility into bronze or auth.

## Root cause (source-confirmed + vendor raw-fact grounded)

On 2026-07-31 five accounts were reassigned at Orion from Peter Lee (rep 12) to **Noel Soderblom
(rep 10)**. Rep 10 was absent from a hand-maintained scope allowlist, so from the 08-01 snapshot
they were filtered out of `silver/api_dims/accounts_v2`.

The filter: `data/inf/scripts/silver/convert_orion_api_to_silver.py:540` @ `e3ec94f5b7`
(`out[out['rep_id'].isin(INFLECTION_REP_IDS)]`, INFNNA.001), `INFLECTION_REP_IDS = {3, 6, 11, 12}`.
`rep_id` there is the SERVICING rep from `household_rep_mapping` joined on `household_id` (`:513`),
not the account's own `representativeId`.

**Self-correction on the record:** I first attributed the drop to the custodian filter at `:431`
and to `filter_to_inflection` in the lib. Both wrong — the five PASS the custodian filter. Corrected
by reading the function rather than the docstring.

**One cause, two symptoms** (the two blockers COO had scoped as independent):
- 08-01: they fall out of accounts_v2 -> household never resolves -> `INF_D_00` crashes at step 44
  on `int('unknown')`.
- 08-02..08-05: a partition rewrite reaches their NNA dates -> `INF_C_01` coverage guard fires at
  step 34, halting the chain BEFORE it ever reaches `INF_D_00`.

Verified independently against `gold/views/account_team.parquet` (881 rows, 0 nulls): exactly 5
non-numeric `household_id` values, all literal `'unknown'`, account_ids {4136,4139,4352,4356,4358}.
Symmetric difference vs the guard's set: EMPTY.

**The guard was right.** All five are `isActive=True`, `cancelDate=None`,
`lastPositionDate=2026-08-04`, values RISING. Opposite signature from every existing excusal (which
rest on vendor closure records). An excusal would have permanently deleted served NNA history for
five live funded accounts — and the firm-total tie-out would still have balanced, so nothing
downstream would have caught it. DO-NOT-EXCUSE held by DS and CTO.

## Verification of the durable fix (Andrew required this BEFORE proposing it)

Universe: NewPortfolio bronze 2026-08-05, 3,005 rows.

| Universe | Accounts | AUA |
|---|---|---|
| A_current  rep_id in {3,6,11,12} | 864 | $208,794,476.83 |
| A_expanded rep_id in {3,6,10,11,12} | 869 | $209,431,383.43 |
| B custodian == Fidelity_Inflection | 868 | $209,431,395.13 |
| B custodian + Fidelity_LH | 2,302 | $493,293,971.36 |

`A_current` reproduces live silver EXACTLY (864 rows) — model validated against reality first.

**Custodian is the WRONG axis, failing both directions.** `Fidelity_Inflection` alone under-covers
by exactly one row (acct 4239 "Alongside Llc", `Fidelity_LH` custodian, Inflection rep 3, -$11.70 —
residue of the documented 04-30 AUM reconciliation). Adding `Fidelity_LH` over-covers 2.36x because
LHP (reps 13/14/15, $283M) shares that custodian code — the Guard B failure already recorded at
`:535-537` ($476.9M in May; $493.3M on today's data).

**The rep axis IS derivable and matches exactly.** Reps whose vendor `representativeNumber` matches
`Inflection` yields EXACTLY {3,6,10,11,12} — 869 accts / $209,431,383.43, symmetric difference ZERO
under all three formulations (household-rep, account repNumber, account repId). Cleanly excludes
Keil FP and LHP. Self-updating: re-derived on the 07-31 roster it returns {3,6,11,12}; on 08-05,
{3,6,10,11,12}.

## Andrew-direct ruling

2026-08-05 ~1958Z, AE~A terminal: **rep 10 IS in Inflection scope.** Delivered as an OPTION
SELECTION on a structured prompt, not free text — option wording mine, binding content the
selection. Recorded with that distinction explicit @`93c898445`; broadcast same turn to COO, CTO,
MSTR with the scope boundary named (rep-10 membership ONLY; durable-predicate design, INF_D_00
handling, and the AT-RISK residual all explicitly un-ruled).

## Commits (mine, this window)

| Hash | What |
|---|---|
| `8e69ae4cb` | INF_REPSCOPE brief — root cause + full verification + site table |
| `93c898445` | Andrew-direct ruling record (rep 10 in scope) |
| `2c0808790` | AE-lane fix: 9 Lambda sites + ferried DS's comp-constants edit |

## Files Modified

See commit messages: `8e69ae4cb`, `93c898445`, `2c0808790`. Rows needing extra context:

| File | Note |
|---|---|
| `infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/{_orion_api_silver_lib.py:113, convert_orion_api_to_silver.py:577}` | The accounts_v2 PRODUCER. ENABLED cron(22 13 * * ? *), fired 7x this week, writes the partition 25 min before the chain's own step. |
| `infra/aws/lambda/inf-portal-publisher/lambda_function.py:69` | STRING-typed frozenset AND aliased `_INFLECTION_REP_IDS` — a name-keyed or int-typed sweep misses it on both axes. |
| `comp-constants.config.yaml` | Content authored by `0.4.0_DS_ClientPlatform`; they are owned-paths refused, I am AE and authorized. Ferried under my author line, stated in the commit body so git does not misattribute. |
| `infra/aws/lambda/inf-pipeline/inf-api-txn/_orion_api_silver_lib.py` | **DELIBERATELY EXCLUDED, reverted to HEAD.** See Blockers. |

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-which` | alarm question | PARTIAL | routed to comp-trigger/comp-freshness; the direct answer came from `comp-grep` |
| `comp-grep` | `inf-gold-chain-failed`, `dispatch-lock` | PASS | located alarm def + all lock readers with dependency context |
| `comp-freshness chain inf` | INF chain | PASS | gave the trading-day-framed staleness (platinum 3-5 td behind) that framed client impact correctly |
| `comp-trigger` | `inf-gold`, `inf-accounts-v2` | PASS | printed denominator (142 rules + 14 schedules); revealed all 3 gold rules DISABLED and the accounts-v2 cron ENABLED/fired-7x |
| `comp-pipescript deployed` | all trees | PARTIAL | timed out at 120s, completed in background; the decisive check was a direct S3 head-object |
| `comp-constants check` | estate | PASS | the gate that surfaced three constant ALIASES and blocked a partial commit |
| `commit-gate.sh` | 10 .py files | PASS (after exclusion) | BLOCKED on pre-existing Guard B drift — correct behavior |
| `safe-commit.sh` | 3 commits | PASS | surface-check + risk-reflex clean/advisory |

**What worked:** `comp-trigger`'s printed denominator and its DISABLED-is-a-live-fact framing kept
me from concluding the chain had no trigger — the real path was a direct lambda invoke from the
silver aggregator, invisible to `list-rules-by-target`. `comp-constants check` found constant
aliases (`INFLECTION_REP_IDS` / `PARTNER_REP_IDS['inflection']` / `INFLECTION_EXTENDED`) that a
name-keyed search structurally cannot.

**What failed:** `comp-pipescript deployed` timed out at 120s and could not serve as the
deploy-verify instrument in-line; `comp-which` did not route to the answering tool for an alarm
question.

**Gap found:** no comp-tool answers "are the N copies of this constant/universe the same?" The
estate had instruments for what is deployed and none for whether its duplicated definitions agree.
`comp-constants` is the closest and it is opt-in per-file, not a universe-level cross-copy check.
Routed to CTO as a gate candidate (accepted, scoping is theirs).

## Deployment Sequence + Verification

**NOTHING WAS DEPLOYED BY ME THIS WINDOW.** Code committed only (Rule 2: commit before apply).
The Lambda apply (`build-and-upload.sh inf-pipeline` -> `terraform plan` -> `safe-apply.sh`, 5
functions) is prepared and NOT run. Stating this explicitly because the AE role section expects
pasted deploy output and there is none to paste.

Live verification I DID run (the discriminating check on DS's deploy, independently, with a
positive control rather than trusting the report):

```
=== live S3 content of the root-cause file ===
629:INFLECTION_REP_IDS = {3, 6, 11, 12}
--- object metadata ---
{ "Modified": "Sun, 12 Jul 2026 13:10:16 GMT",
  "ETag": "\"d056167f8f39ab668bb534171068d022\"" }
=== positive control: the lib DID deploy? ===
113:INFLECTION_REP_IDS = {3, 6, 10, 11, 12}  # +10 Noel Soderblom: Andrew-direct ruling ...
Wed, 05 Aug 2026 21:38:29 GMT
```

The positive control is what makes this a measurement rather than an assertion: the same mechanism
deployed the sibling library TODAY and skipped the root-cause file, so "nothing deployed" and
"deploy is broken" are both excluded.

Pre-deploy gates I verified and cleared (all read-only):
- Dispatch kill-switch: `INF_GOLD_DISPATCH_RELEASE = RELEASED-BY-CTO-AND-COO-COSIGN` — RELEASED.
- Portal FE gate: `origin/PROD` AND `origin/DEV` both already carry `noel_soderblom` in
  `allowedAdvisorKeys` with `maxEntries: 5`. The memory warning
  (`project_advisor_of_record_single_source_refactor.md:44`, "gold-alone drops Peter ~$25M with
  $12.4M into a hidden advisor") is SATISFIED, not outstanding. Surfaced by the pre-commit
  risk-reflex; I would not have looked without it.
- AoR fold: `INF_AOR_FOLD_ACTIVE=1` live on the trigger lambda; gold scripts already treat
  `noel_soderblom` as a folded advisor, so attribution resolves rather than falling to the firm
  catchall.
- Stale dispatch lock (6.5h old vs 5400s TTL, runner stopped): NOT a blocker —
  `acquire_dispatch_lock` clears locks older than TTL before acquiring. Deliberately not reported
  as an outage.

## Blockers

**BLOCKED (evidence-cited) — the outage cannot clear on our two commits.**
`s3://opal-data-inf/code/silver/convert_orion_api_to_silver.py` is still the 2026-07-12 object
(line 629 = `{3, 6, 11, 12}`, verified above). It carries a real serve-gate:
`convert_orion_api_to_silver.py:45` `# DEPLOY-SERVE-HELD: advisor-of-record daily fold pending
CTO~B clean-review + NEVER#2 sign-off` (sibling on `INF_D_04.client_portal_summary.py:39`).
Release requires a `SERVE-RELEASE-ACK` in the authorizing commit and is a CTO+COO sign-off, not a
DS or AE call. DS correctly declined to remove it inside an outage fix and escalated. **Owner:
`1.0.0_SA_CTO` (ruling) + `2.0.0_SA_COO` (coordination).** Not blocked on me.

**FINDING (routed, not blocking me) — `inf-api-txn/_orion_api_silver_lib.py` carries a weakened
guard.** `GUARD_B_AUA_LOWER 50_000_000` / `UPPER 400_000_000` vs canonical `150_000_000` /
`300_000_000` — a 3x-wider Guard B in a forked copy. `commit-gate.sh` blocked it; I reverted the
file rather than silently absorb a live-guard change inside an outage fix. That file still carries
`{3,6,11,12}`.

**FINDING (DS-reported, I confirmed) — `.tools/safe-deploy.sh` reported "OK: safe-deploy gate PASS
-- all files deployed and verified" and exit 0 while holding back 2 of 11 files.** The SERVE-HELD
lines print, but the summary line is false and rc=0 is what callers (including its own pre-push
hook) key on. Third instrument today reporting green over an incomplete action. Routed to CTO by DS.

## Current State

- Root cause established, source-confirmed, vendor-raw-fact grounded. Not in dispute; DS and CTO
  both re-derived independently.
- Andrew ruled rep 10 in scope @`93c898445`. Recorded + broadcast; scope bounded to rep-10
  membership only.
- Code: DS `data/inf/` 11 files @`8a8daae1a`; AE `infra/aws/lambda/` 9 files + comp-constants
  @`2c0808790`. Branch ahead 17, UNPUSHED (standing regime: LANES COMMIT, INTEGRATORS PUSH).
- Deployed: 9 of DS's 11 scripts live on S3; the two serve-held ones are NOT, including the
  accounts_v2 producer. My 5 Lambdas: committed, NOT applied.
- The chain will next attempt ~13:47Z 08-06 via the silver aggregator's direct lambda invoke (NOT
  the EventBridge rules, all three of which are DISABLED). It will fail at `INF_C_01` again unless
  the serve-hold is released first.
- Client impact holding: INF platinum firm artifacts 3-5 trading days behind the 08-05 frontier;
  `account_team.parquet` frozen at 08-01, so the first green chain regenerates a stale advisor view
  — "chain recovered" will not mean "portal current".

## Next Steps

1. **[1.0.0_SA_CTO + 2.0.0_SA_COO]** Rule on releasing the `DEPLOY-SERVE-HELD` sentinel on
   `convert_orion_api_to_silver.py` (+ `INF_D_04`). This is the only thing standing between the
   estate and a green chain. Everything else is done.
2. **[0.4.0_DS_ClientPlatform]** On release: re-deploy and RE-VERIFY on S3 CONTENT, not on the
   gate's exit code.
3. **[0.7.0_AE_CloudOps~A]** `build-and-upload.sh inf-pipeline` -> `terraform plan` -> surface the
   diff -> `safe-apply.sh` for the 5 Lambdas. Independent of the serve-hold; does not by itself
   unblock the chain.
4. **[0.7.0_AE_CloudOps~A]** After release + deploy: chain re-run and the acceptance test —
   chain-COMPLETE **AND** the five `'unknown'` rows GONE from `gold/views/account_team.parquet`
   **AND** no excusal entry. NOT chain-green.
5. **[1.0.0_SA_CTO]** `inf-api-txn` weakened Guard B; `safe-deploy.sh` false-PASS summary; the
   duplicated-constant lint (accepted, scoping theirs).
6. **[OPEN, unowned]** The 08-01 NNA AT-RISK register listed 17 accounts and named none of these
   five though they were already filtered out that morning. It is the early-warning surface for
   exactly this class and it was silent on the live instance. Does not close when the chain goes
   green.
7. **[OPEN]** `data/inf/manual_api/pull_inflection_assets.py:53` carries `[3, 11, 12]` — missing
   rep 6 as well as 10. The assets dim has been frozen since May (2184h per comp-freshness).
   Possibly related; unverified, flagged not chased.

## Doctrine landed from this window

- **LD-0378** (`36b996f5ad`, MSTR): the N-COPIES-OF-ONE-UNIVERSE class, this finding as type
  specimen.
- **`docs/doctrine/DERIVED_UNIVERSE.md`** (CTO): three clauses — derive the universe; assert on
  change to the DERIVED SET (vocabulary drift); assert on change to the SELECTED POPULATION
  (membership drift at constant vocabulary). Clauses 2 and 3 came from this window; clause 3
  because a set-level assert is blind to an account moving rep 12 -> rep 13, which leaves the set
  unchanged while the population moves. The deliverable is the ASSERT, not the predicate.
- Recorded in the doctrine's provenance line at my request: the caveat was not foresight — it came
  from watching the predicate return two different correct answers five days apart.
