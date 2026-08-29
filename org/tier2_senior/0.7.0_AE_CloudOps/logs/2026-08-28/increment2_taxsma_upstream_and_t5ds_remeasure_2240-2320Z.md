# 0.7.0_AE_CloudOps~Z -- increment 2 taxsma upstream + T5DS-AC6 re-measure (2240-2320Z)

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, TRACE

## Window

2026-08-28T22:40Z -> 23:20Z, delta since `session_close_2132-2240Z.md` (@`f5ed6338d4`).
ZERO commits by design -- the issuer's standing instruction for this window was **"build nothing,
apply nothing."** ~20 inbound MCP messages handled, 8 substantive dispatches out.

## Scope

Seated on increment 2 (14423) as **the taxsma silver/gold upstream + any deploy it needs -- the long
pole**. Later given one additional re-measure: `ETFS_SATELLITES.TO-5-DS` / `T5DS-AC6` (14616 s1).

## Part 1 -- the taxsma upstream: four blockers found, then three

Andrew's premise (14403): *"we should be able to do now that we've hooked up the Tax SMA pipeline."*

```
  bronze reporting_{performance,costbasis,allocation}   1 pull_date each: 2026-07-17
  silver fact_taxsma_report                             1 object:         2026-07-17
  gold   dim_taxsma_report                              1 object, account=0027265115
  opal-assets-bd49f-reporting-pull  LIVE, LastModified 2026-08-28T18:09:29Z
    TRIGGERS: 0 of 140 EventBridge RULES, 0 of 18 SCHEDULER schedules
              -- inspected BY TARGET ARN, never by rule name
```

**The chain stops at BRONZE.** Not a stalled schedule -- there is no schedule. The premise is true of
the CODE and needs qualifying about the OUTPUT.

**CVO's additive-vs-redistributive fork (14440) RESOLVED on my plane:** 0 of 5 enrolled roster
accounts are in the 0824 base (7,282 accounts, positive-controlled against a known member). So
populating `ALT Strategies` **ADDS** money and `total_aua` must grow -- an AC asserting "total_aua
unchanged" would fail a correct build.

**And two facts that reshaped the ask before it reached Andrew:**
- the attribution key is NOT absent -- `taxsma_roster.json` carries `strategy` 5 of 5,
  human-confirmed at enrollment. Registry DATA, the `SMA_MEMBERS` pattern, not a derivation.
- **all five carry ONE distinct strategy**, so even fully unblocked `Muni SMA` stays null. If the
  mental model is "ALT Strategies complete", the roster does not support it.

## Part 2 -- MY OWN RETRACTION, and it is the important entry

I reported (14473) that item 3 COLLIDED with Andrew's 0824/0833 ruling, because the one resolvable
account carried `in_0833_universe = True`.

**THAT WAS WRONG.** Verified at source at this seat after `3.0.0_SA_CVO~Z` challenged it:
`bd49f_dim_conversion.py:304` sets it from `isin(universe)` where `read_universe()` reads
`schwab/08335338/silver/fact_acc/` -- **a crosswalk COVERAGE flag, the ship-gate denominator.** 0833
is the firm's MASTER scope (49F's own gold dimensions are written under it). `True` meant the account
RESOLVED. Orthogonal to supervised/unsupervised.

⛔ **THE MECHANISM: I read a FIELD NAME containing `0833`, matched it to Andrew's phrase, and treated
a string collision as a semantic one without opening the writer.** That is the exact inference class I
had spent the hour flagging in three other seats' work -- membership from a feed name, from
`issue_type`, from a strategy string. **I named three coats and wore a fourth.**
⛔ **And the qualifier was already mine:** `1.0.0_SA_CTO~Z` had written *"treat the identifier mapping
as UNVERIFIED until someone reads it at the source"* in the very message I built on. **I ACKed it and
dropped the caveat five minutes later.** Banked: `i-policed-an-inference-class-then-committed-it`.

Every OTHER measurement survived -- none of them rested on that limb.

## Part 3 -- built, then stood down

Under 14540's *"proceed at your judgment"* I built the quarter-derivation precondition (handler
defaults for the unguarded `event["q_start"]`/`["q_end"]`, plus a control harness). 14563 then
narrowed to **"build nothing, apply nothing."**
**STOOD DOWN: working tree reverted, test removed, `git status` CLEAN on that lambda.** Design
preserved in scratchpad, validated before standing down (reproduces the one real invocation; ROLL
CONTROL moves across the quarter boundary; rc=0 un-piped).

## Part 4 -- T5DS-AC6 re-measure: FAIL -> PASS

### Verification (ACTUAL output)

```
  RULES     140 total (client-side count), 1 matching, ENABLED cron(0 7 * * ? *)
            TARGET -> arn:...:function:cot-satellites-registry-producer  Input=None
  METRIC    2026-08-28T07:00Z  Invocations 1, Errors 0
  LOG       07:00:16  INVOKE: event_keys=['account','detail','detail-type','id','region',
                              'resources','source','time','version']   <- EventBridge envelope
            07:00:18  OK: derived 9 member(s) of 65 roster row(s)
            07:00:18  OK: wrote s3://opal-data-cot/platinum/satellites/registry.json
            07:00:18  RUN COMPLETE {"rc": 0, "dry_run": false}
  ARTIFACT  LastModified 2026-08-28T07:00:19Z, 2196 bytes, as_of 2026-08-28, books 9
```

EXERCISED, on the scheduled envelope, artifact read independently rather than trusting `rc: 0`.

⛔ **AND MY FIRST READ SAID THE OPPOSITE.** boto3 returns CloudWatch `Timestamp` as `tzlocal()`; I
formatted it with a hardcoded `Z`, shifting every value 4 hours, so the real 07:00Z fire printed as
`03:00Z` and read as ABSENT. **One step from filing a confident FAIL on a criterion that had passed 16
hours earlier.** Caught ONLY because a second instrument (log streams) disagreed by exactly four
hours -- **the disagreement was the signal.** Banked: `boto3-returns-timestamps-in-tzlocal`.

## Part 5 -- the Monday frontier

`3.0.0_SA_CVO~Z` found a counter-example (Mon 08-10 computed Thursday) and attributed it to upstream
availability. **Falsified:** both weekday-only feeds had landed the Friday data on SATURDAY
(`fact_rps_s2` 08-08 10:16Z, `fact_holdings` 08-08 22:31Z). Cause UNIDENTIFIED; I proposed none.

Then, answering 14600's "one-off or recurs" -- **and catching a second false alarm on myself:** my
first pass counted CALENDAR days and made all three Mondays look like stalls. On the TRADING-DAY axis
CLAUDE.md requires:
```
  WEEKDAY runs ON FRONTIER (T-1): 16 of 17.  OFF: 1 -- Mon 2026-08-10 only.
  WEEKEND runs all sit one trading day back, 3 of 3 weekends, CONSISTENT (not a stall).
  MONDAY DENOMINATOR = 3:  08-10 T-2 | 08-17 T-1 | 08-24 T-1
```
Monday is structurally the catch-up run every week. The question is not "can the frontier stall for
days" but "does Monday's catch-up fire" -- 1 failure in 3.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-which` | (not run this window) | -- | no code search performed; every question was answered on live AWS/S3 planes, not the repo |

**What worked:** nothing repo-shaped arose. All eight findings came from live-plane reads (S3 listings
with client-side counts, both EventBridge APIs by target ARN, CloudWatch metrics + logs, parquet
schemas) plus `git show`-free source reads of three files.
**What failed:** no compiler tool failed because none was applicable.
**Gap found:** none in the comp-rail. The two failures this window were BOTH mine and BOTH in
timestamp/axis handling (`tzlocal()` + hardcoded `Z`; calendar days where the trading calendar
governs) -- neither is a surface any comp-tool covers.

## Files Modified

**NONE COMMITTED -- deliberately.** One working-tree edit was made and reverted (Part 3); the tree is
clean. Two memories written outside the repo:
`i-policed-an-inference-class-then-committed-it`, `boto3-returns-timestamps-in-tzlocal`.

## Blockers

**NONE at this seat.**

**Owned elsewhere:**
- [`1.0.0_SA_CTO~Z`] tax/muni attribution mapping + the recurring-vendor-egress word (one trip).
- [`2.0.0_SA_COO~Z`] sequencing of the schedule leg; my rec (behind the ruling) is adopted.
- [unassigned] an unexplained ERROR on `cot-satellites-registry-producer` at 2026-08-28T01:00Z --
  OBSERVATION, INERT, surfaced not chased.

## Current State

Item 3's blockers are THREE, all independent: bronze never scheduled (AE, mine, unblocked in basis but
HELD on egress); gold `dim_taxsma_report` has no member/strategy axis (86 columns, read at the
artifact); coverage ceiling is ONE account (Chiles-only builder + 2 of 5 roster accounts
`pending_resolution`). Lifting any one leaves the other two.

⚠ **The egress ask is narrower than first stated:** the module's own `DRY_RUN` hard gate is ALREADY
OPEN (`DRY_RUN="0"` live) and was exercised -- the 2026-07-17 objects prove a live BD call happened.
So the question is whether a PER-USE sanction extends to a CADENCE, not whether we may call BD.
**I have found that sanction's EFFECTS, not its record** -- the gate cites `WS-1 TO gate @8bf441b1c`
and someone should read it before quoting me on "the word was given."

`T5DS-AC6` is PASS. Nothing at this seat is pending.

## Next Steps

- [`0.7.0_AE_CloudOps` next session] The schedule leg, on the COO's word: quarter derivation
  (patch preserved in scratchpad, validated) + scheduler role/schedule/permission mirroring
  `mdpf_portal_publisher.tf`. **Do NOT attach an alarm or freshness check** -- standing moratorium.
- [`0.7.0_AE_CloudOps` Monday] If asked whether increment 2 landed: the regularity says yes, the
  single counter-example is unexplained, and no availability argument is evidence.
