# SESSION CLOSE -- 0.4.0_DS_ClientPlatform~H -- OPAL_GLDRNS twr D-1 mirror

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Window:** 2026-08-25T02:00Z -> 05:33Z (whole session)
**Serial:** `0.4.0_DS_ClientPlatform~H` (lane; logged under the base folder, no lane folder exists)
**Project:** OPAL_GLDRNS -- the twr_daily D-1 mirror remedy. ONE project, per spawn brief.

> **THIS IS A CONSOLIDATION, NOT A THIRD RECORD.** The work is already logged in full at
> `gldrns_twr_d1_mirror_surfaces_abcd_0200-0303Z.md` @`52f9098e6d` and
> `gldrns_mint_and_deploy_critical_path_0303-0525Z.md` @`82bab46091`. **Measured before
> writing: ZERO commits and ZERO new inbox items since `82bab46091`** -- the 05:25Z->05:33Z
> tail holds one ack of a broker re-surface and one heartbeat. Nothing here is new work; this
> exists to be the handoff surface a successor reads first.

---

## What this session did, in one paragraph

The 49 Financial advisor product's daily performance returns were emitting EMPTY -- 7,335 of
7,335 rows refusing, every scheduled day, silently. The cause was source-confirmed and then
MEASURED: every stage in the chain addresses exactly one date, so the local mirror never held
D-1, so c02's BMV lookup could never resolve, so every row took the refusal branch and the
partition structurally lacked four columns. **They were never derivable, not dropped.** I
delivered surfaces (a)(b)(c)(d) of the 26-cell decomp -- 21 owned cells -- plus two defects
that only became visible because the remedy worked. All of it is committed, pushed and
deployed. The pipeline now computes real returns.

## Delivered, all ON `origin/CLOUD` and all DEPLOYED

| commit | what | deployed (UTC) |
|---|---|---|
| `b9a665364f` | surfaces (a)(b)(c)(d), 21 cells | 03:01:42Z |
| `77ecd4f0de` | c04 check-7 disarm (`NOT-EVALUATED`) | 03:23:48Z |
| `2ee5f8ca43` | minted `NO-PRIOR-BALANCE-ACCOUNT-ABSENT` | 05:06:45Z |
| `52f9098e6d`, `82bab46091` | session logs | ride integration |

**APPLIED layer verified for every file**, by reading deployed CONTENT and hashing it
CRLF-normalized against the ref that BUILT it (not by filename, not by ETag):
`deployed f8b761f3d05acee12d2f7f8af8f44b7b == repo @2ee5f8ca43`, mint marker x2,
`dates_loaded` x2, positive control 5, negative control 0. MSTR adopted this form over their
own marker-count check and is folding it into the `comp-closure` repair.

## Current State (for a reader with ZERO prior context)

**The producer.** `data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` gained
`_pull_prev_valuation_into_mirror()`, invoked immediately before the `c02_twr_daily` stage and
keyed on that stage's NAME so a future reorder cannot silently detach it. It S3-pulls the
prior TRADING day's `canonical_valuation` into the local mirror, reusing the shape
`_pull_canonical_for_c04` already established. The prior trading day comes from a04's
`dim_calendar` via the same `prev_map` c02 itself builds -- no second calendar source, no
wall-clock arithmetic (NEVER#1 lives in this exact file; c02 once carried a hardcoded
`date=2026-08-07`).

**The status vocabulary.** `c02_twr_engine.py` now distinguishes two states `piv.get()` could
not: `REFUSED-NO-BMV` (the D-1 partition is not loaded -- a WIRING state the remedy moves, and
the population Andrew's acceptance requires to reach ZERO) from
`NO-PRIOR-BALANCE-ACCOUNT-ABSENT` (the partition IS loaded and this account is not in it -- a
POPULATION state nothing ever moves). Discriminator: `dates_loaded`, already in the frame.

**Execution.** The chain runs from `s3://opal-data-49financial/_code/` via
`aws s3 sync --delete` fresh on EVERY run (AE~G read the actual SSM `get-document`
`runCommand`, not the Terraform comment describing it), so the code channel IS the executing
surface -- no Lambda package is involved (CVO withdrew that caveat after finding no
`lambda-source-map.json` entry for this chain). **Schedule `cron(45 12 * * ? *)` UTC, ENABLED,
target `advi-49f-gold-dispatch`.**

**Last measured behaviour** (ad-hoc QA, explicitly NOT production evidence):
`{'OK': 6393, 'UNCOMPUTABLE-ZERO-BMV': 922, 'NO-PRIOR-BALANCE-ACCOUNT-ABSENT': 17}`,
`REFUSED-NO-BMV` = 0, manifest `bmv_source "canonical_valuation date=2026-08-18"`, cols 9 -> 13.

## Blockers

**None.** Nothing is held on this seat and nothing is owed by it.

## Compiler Tools

Cited from context, not re-run for this table (speed contract).

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `-i 'REFUSED-NO-BMV'` | PASS | consumer census before the mint -- no consumer branches on the refusal status STRINGS |
| `comp-find` | `-i 'twr_daily' <runners_49f>` | PASS | found c04 as the only in-tree consumer; produced the check-7 finding |
| `comp-find` | `-i 'stages='` | PASS | proved no machine consumer of the stage-count line before changing it |
| `comp-pipescript` | `deployed c02_twr_engine.py` | **REFUSED rc=2** | gap, below |
| `comp-which` | A.3 startup exercise | PASS | forwarder RAN, not merely resolved |

**What worked:** `comp-find`'s BAND separation distinguished a comment mention in
`perfrp_rollup` from real branching in one call -- that is what made the mint's
consumer-safety claim cheap and defensible instead of a guess.

**What failed / GAP:** `comp-pipescript deployed c02_twr_engine.py` REFUSES at this seat
(`--pipeline` required) and offers only `inf-runners_inf` / `cot-runners_cot` -- **neither is
the 49f tree under test** -- while `0.0.0_AB_MSTR` cited `[advi:gold] MATCH` (1 of 57) and
`3.0.0_SA_CVO` cited `STALE` (1 of 69) from what reads as the same command. Three seats,
three behaviours, two differing denominators. **Raised as an OBSERVATION, not routed** -- both
their verdicts were corroborated independently and the STALE one matched my byte read exactly.
It matters only because this instrument established both a MATCH and a STALE on a publish
path, and a same-name script in three trees is the shape that yields a confident answer about
the wrong file. A flagless full sweep exceeded 120s here and was left running.

## Findings raised this session

1. **ARMED (filed `ADVI_PERFRP-S12`)** -- raised against my OWN remedy before building it: it
   creates MIXED partitions, where refused rows read `bmv=NaN` -- PRESENT-AS-NaN, not ABSENT.
   Produced a ratified-contract retraction (CVO), a new sequencing invariant `GLD-inv-7` (COO),
   and DS~G finding a LIVE bug: `link_returns` tested `v is not None`, and a NaN is not None,
   so it returned `(nan, "COMPUTED", coverage 1.0)`.
2. **BLOCKING** -- the ratified acceptance `REFUSED-NO-BMV -> ZERO` was unachievable without
   manufacturing a BMV, which `GLD-inv-1`/`GLD-a-4` forbid. Resolved by CTO's option-B mint.
3. **ARMED** -- c04 check 7 had never evaluated a return and could not (`twr_daily=None`
   hardcoded while every sibling loaded via `_try`). Disclosure disarm mine; remediation CTO's.
4. **Decomp oracle correction** -- `GLD-b-2` said "a Monday must pull FRIDAY"; true 98/103.
   Five Mondays pull a THURSDAY (holiday Fridays). Landed by COO @`d3e653dbf6`.
5. **Cert-bar improvement** -- CVO's check 9 gained two passing forms on my amendment
   @`eb4ccf34f8`: an unmapped requirement is a finding ONLY when it is also UNDECLARED.

## Errors of mine, recorded rather than smoothed

- **Asserted a deploy state from context instead of measuring it**, on a sovereign critical
  path. CTO carried it into a push request to MSTR. Retracted same-turn; CVO falsified it
  independently; MSTR closed it before acting. **Nothing was spent because both corrections
  arrived before the integrator moved.** Every push-state claim afterwards carried both
  controls.
- **Resolved a source by FILENAME at a ref that predated the change** (c04 at `b9a665364f`)
  and briefly reported GENUINELY DIFFERS. The file was right; the REF was wrong.
- **A regex stage census returned a confident "4 of 4"** (nested brackets); AST gave 15. The
  conclusion it supported happened to be right, which is what made it dangerous.
- **A `tail -20` truncated the line I was checking for** and I briefly read that as the code
  not printing it.
  *All four were caught by controls, not by care, and none reached a conclusion I shipped.*

## Next Steps

1. **[the artifact, not a seat]** `GLD-f-1` closes ONLY on the **12:45Z SCHEDULED** run's own
   artifact: `REFUSED-NO-BMV` = 0, real returns present with count and denominator printed,
   the three legitimate refusal classes reported in their own words. **NO AD-HOC RUN** --
   Andrew's own rule makes one a QA instrument and never production evidence; COO has backed
   that refusal. `3.0.0_SA_CVO` pre-declared their s.14(c) read so it cannot be shaped after
   the fact.
2. **[2.0.0_SA_COO]** the three unimplemented-constant c04 checks (msg 68380). My
   `checks_ran: 8` still counts them as "ran" -- better than "9 checks" and not yet true. I did
   not regrade them: that is a Rule 24 classification act on checks I do not own, and one of
   the four constants is legitimately final.
3. **[1.0.0_SA_CTO]** `GLD-f-3` deploy-completion ledger entry. The deploy already completed,
   so the honest form is a CLOSED retrospective entry. Named rather than opened because I am
   not the pusher; I will write it if asked.
4. **[whoever owns comp-pipescript]** the tree-resolution discrepancy above. One run settles
   it; nothing gates on it.
5. **[unassigned]** Surface (e) remains HELD OUT under Rule 24(iv). Its 6 partitions are still
   UNCLASSIFIED by status -- the contract's `refused_dates` names the dates but not which of
   the three statuses each carries, and I have not quoted them as classified.
