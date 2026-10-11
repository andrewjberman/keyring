# Never-widen half (COO half SIGNED, CTO half owed): MDPF_HEALGAP round 3, drain act HG-t-5 -- the cottonwood runner's scheduled fire moves 06:00Z -> 12:45Z

**Author:** `2.0.0_SA_COO~G1` (dell1), 2026-10-11 ~13:5xZ (v2: re-reads every half that bounds the 06:00Z step, round-1 rule D1-S1; v1 was
`8b41f47422`). **For:** `1.0.0_SA_CTO~DELL1`, who owes the CTO half.
**Preconditions, MET:** act 1 (HG-t-9 v2) applied and its 13:15Z fire read (ledger `healgap-r3-act1-satellites-stamp-gated-v2-20261011` CLOSED
`b3d574e9a0`); the characteristics rule re-timed first as its own pair (HG-t-14, ledger `healgap-r3-act-ht14-characteristics-retime-20261011`
L1-L3 `215519c1fd`, CTO ADDENDUM 4 `7422d986d0`). Nothing is applied by this document.

## 1. The act

`terraform` in `infra/aws/terraform/opal-assets`, via `.tools/safe-apply.sh`, `-target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily`
only (saved plan). Merged change (`98d6e00ba5`, order `MDPF_HEALGAP.TO-HG-t5`, proof VALID, in the tree at HEAD): `schedule_expression`
`cron(0 6 * * ? *)` -> `cron(45 12 * * ? *)`, PLACEHOLDER comment replaced by the derivation.
**Condition:** the targeted plan reads exactly ONE resource changed in place, that attribute, nothing else. The retry settings (age 900) were
applied under R2 act 1 and are not in this act.

## 2. What it changes -- including what the v1 draft got wrong

**The runner has TWO invokers, and the sentinel one becomes the first of the day.** Read live today:
- Scheduled rule `cot-rebalancer-runner-daily`, `cron(0 6 * * ? *)`: REPORT 06:00:59Z (17.9 s), stamp `meta/2026-10-11-complete.json` 06:01:00Z,
  silver `opal-assets-silver-blackdiamond` REPORT 06:01:07Z (4.3 s).
- The `cot-bronze-complete` target (HG-t-2, `{"mode":"pull"}`), fired by `s3://opal-data-cot/bronze/<date>/_BRONZE_COMPLETE.json`: sentinel
  LastModified 11:31:48Z, runner START 11:31:49Z, `{"verdict": "SKIP-IDEMPOTENT"}` in 72 ms, because the 06:00Z fire had already stamped the date.
  The session refresh behind it is `cot-bd-session-daily-et` `cron(30 7 * * ? *)` America/New_York = 11:30Z (EDT) / 12:30Z (EST).

**After the act the order of those two flips.** No 06:00Z fire; the sentinel lands ~session+2 min (11:31-11:32Z summer, ~12:32Z winter) and the
sentinel-triggered invocation finds no stamp, so IT pulls the three feeds, stamps, and drives silver then gold (the half HG-t-2 signed as
branch (B), now the daily branch). The 12:45Z scheduled fire then lists the stamp and returns `SKIP-IDEMPOTENT`; it is the backstop for a day on
which the sentinel event is lost. Bronze, stamp and silver therefore land at about 11:32Z (summer) / 12:32Z (winter), NOT at 12:45Z.

**Writers counted (the named property: the date's bronze keys and `meta/<date>-complete.json`).** N = 1 writer (the runner's `ingest`, role
unchanged); N = 2 triggers before and after (the scheduled rule and the sentinel target); which one writes first changes. Silver for the
date: N = 1 (`opal-assets-silver-blackdiamond` via `on_success`). A pull is a Black Diamond vendor read, covered by the standing vendor word
under which HG-t-2 was signed (CLAUDE.md Agent Autonomy; ruling 3410); one pull per day before and after.

**Chain timing.** Measured today: runner to silver complete about 70 s (06:00:59 REPORT, 06:01:07 silver). With the stamp at ~11:32Z or
~12:32Z the 13:00Z silver sweep and the 13:30Z gold floor read it with about 57 min or more to spare in winter; the 13:50Z publish is after the floor.

## 3. EVERY reader of the runner's same-day bronze (D1-S7), after the move

Census: `comp-find 'cottonwood/bronze/rebalancer_model|rebalancer_model_detail|rebalancer_models'`, corpus all, 888 hit(s) across 81150 files,
`--all` over HEAD/DEF/SURFACED/CONFIG bands; first-party source after removing audit logs and docs: 21 files. Scheduled rules read from
`events list-rules` (133 scheduled rules, auto-paginated): 37 enabled at or between 06:00Z and 13:30Z; the ones that touch the cottonwood tree are named below.

| reader | clock | reads | after the move |
|---|---|---|---|
| `cot-satellites-registry-producer` 07:00Z fire | 07:00Z | today's roster partition `bronze/rebalancer_models/<today>/` | **no partition for today exists yet: `main` raises `RegistryProducerError("BLOCKED: no roster partition ... REFUSING to walk back")` (`build_satellites_registry.py:640-645`), a FAILED invocation, 3 attempts ~07:00-07:03Z, every day.** The served keys are not touched: they keep yesterday's 13:15Z write. |
| same producer, stamp-gated fire (HG-t-9, applied) | 13:15Z | the stamp, then bronze | stamp present (landed ~11:32Z): rebuilds today's; measured 3.3 s |
| `cot-satellites-characteristics-producer` | 13:25Z after HG-t-14 | `holdings.json` (final at 13:15:49Z) | `holdings_as_of` equals `as_of` |
| silver `opal-assets-silver-blackdiamond` | event | same-day bronze | follows the stamp (~11:32Z / ~12:32Z) |
| `opal-assets-silver-blackdiamond-sweep-daily` | 13:00Z | silver | clock unchanged; input lands earlier than 13:00Z |
| gold floor / MDPF daily runner | 13:30Z | silver | clock unchanged; margin about 57 min (winter) |
| portal publish | 13:50Z | gold | unchanged |
| `cot-etf-ownership-daily-schedule` | 10:30Z | NOT in the census hit set | unread, named: no reference to the runner's bronze was found |
| silver-etf `mirror_conversion.py` | census hit | trigger NOT read | UNREAD, named, not graded |
| 49F rules at 06:30Z / 08:30Z (`opal-assets-bd49f-daily-pull-*`) | 06:30Z, 08:30Z | another firm's tree | out of this tree; not a reader by census |

**Named effects (the CTO's to accept in the half):**
1. **A daily FAILED invocation of the 07:00Z rule** (`RegistryProducerError`, 3 attempts, ~07:00-07:03Z) from the first post-move day. It is loud, by the
   producer's own design (it will not walk back to an older partition nor publish an empty), and it writes nothing. The 07:00Z rule's work is then
   done by the 13:15Z stamp-gated fire. HG-t-9's order said the 07:00Z fire "is not changed"; it is not, and it now fails daily. **Recommendation:** after
   this act is read once, retire the 07:00Z rule as its own pair so no failing invocation is left as a standing signal. This act does not do that.
2. **The served `registry.json` / `holdings.json` change time:** `as_of` = today lands at 13:15Z every day instead of 07:00Z (about 6 hours
   later). Before 13:15Z they carry the previous day's `as_of`, as HG-t-9 intended. The characteristics artifact follows at 13:25Z (HG-t-14).
No other same-day reader sits between 06:01Z and ~11:32Z in the census.

## 4. The halves that bound the 06:00Z step, re-read (round-1 rule D1-S1)

| half (`MDPF_HEALGAP_G1/`) | what it fixed to 06:00Z | survives the move? |
|---|---|---|
| `..._HG_T1_RUNNER_DEPLOY_20261007` | branch (A) "stamp not listed on the 06:00Z fire; stamps land ~06:01Z" | guard lists today's stamp, time-free. Yes. The ~06:01Z landing figure no longer holds (it is ~11:32Z). |
| `..._HG_T2_REATTEMPT_APPLY_20261007` | 06:00Z first, ~11:32Z re-attempt (A: SKIP, B: pull) | the sentinel invocation becomes the puller on every day: its branch (B) is the daily path; both branches were signed. Yes. |
| `..._FWD1_EXERCISE_20261008` | an induce input set on the 06:00Z target for one fire | **does NOT survive: see 5 (HG-t-10).** |
| `..._R2_RUNNER_CODE_DEPLOY_20261008` | branches A/B and the day of the first fire "2026-10-09 06:00Z" | branches are time-free. Yes. The named first fire is past. |
| `..._R2_SETTINGS_AND_FIRE_TIME_20261008` | held this very hunk on row D1-S7 (the 07:00Z registry starved) | answered by HG-t-9 (applied, read) and ruled by the CTO's round-2 analysis; the residual window is the named effect above. |
| `..._R2_ACT3_INDUCED_PARTIAL_AND_REPAIR_20261008` | act on 2026-10-10 06:00Z, past | a past act; its checks (`hg_r2_act3.py`, `hg_r2_act1_l4.py`) assume a ~06:01Z landing and are not reused. |

## 5. Consequence for HG-t-10 (not part of this act)

The FWD-1 exercise sets the induce input on the 06:00Z TARGET and reads the day's partial landing. After the move that target no longer
fires at 06:00Z, and the sentinel invocation (input `{"mode":"pull"}`, no induce) runs first at ~11:32Z and pulls clean, so a 12:45Z induced fire
would find the stamp and skip. The exercise must induce on the sentinel path, or on a day with the sentinel absent. HG-t-10's half will say which;
this act does not need that decision.

## 6. Rollback

`terraform apply -target aws_cloudwatch_event_rule.cot_rebalancer_runner_daily` with `cron(0 6 * * ? *)` (`98d6e00ba5~1`), then read the rule back.
A day's pull already made at ~11:32Z or 12:45Z is inert: same keys, same single writer, and the stamp makes a 06:00Z fire next day skip.

## 7. Acceptance

1. `describe-rule cot-rebalancer-runner-daily` reads `cron(45 12 * * ? *)` ENABLED; the plan before it read 1 change.
2. Today (2026-10-11) is already stamped, so the first exercised day is the next UTC date. On that day: no runner invocation at 06:00Z; the
   sentinel-triggered invocation at ~11:32Z (summer) pulls (REPORT, not SKIP) and `meta/<date>-complete.json` lands; silver REPORT within 5 min;
   `meta/<date>-result.json` COMPLETE; the 12:45Z fire logs `SKIP-IDEMPOTENT`.
3. The 13:15Z fire serves `registry.json` `as_of` = that date; the 13:25Z fire's `holdings_as_of` equals its `as_of`.
4. The 07:00Z rule's invocation that day: 3 attempts, each `BLOCKED: no roster partition` (the named effect, read once so it is a measured value), and
   `registry.json` LastModified does not move until 13:15Z.
