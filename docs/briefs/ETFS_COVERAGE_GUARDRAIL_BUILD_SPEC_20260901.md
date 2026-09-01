# BUILD SPEC — ETFS coverage guardrail: daily catch-up, pre-publish gate, and the automated monthly send

**Tags:** `ETFS` `ETFS_TRACKING` `ETFS_CANON` `COVERAGE_GUARDRAIL` `CATCHUP` `BACKFILL`
`PRE_PUBLISH_GATE` `MONTHLY_REPORT` `SES` `EMAIL_RECIPIENT` `COTTONWOOD` `49FINANCIAL` `INFLECTION`
`cot-etf-ownership-daily` `bd-49f-etf-ownership-daily` `inf-etf-ownership-daily`
`etfs-reports-orchestrator` `render_month_end` `BUILD_SPEC` `2026-09`

**Author:** `4.0.0_SA_CRO` · **Date:** 2026-09-01 · **Class:** BUILD SPEC — a PROPOSAL. Nothing here is
dispatched by this document. CRO specifies; COO decomposes; AE/DS build.

**Andrew-direct authorization (verbatim):** *"I'd like to be able to have it go out to aj@opalinvest.com via
email but I'm hesitant in the event that there are holes for whatever reason in backfill. What I'm thinking
is maybe we can build in some kind of guardrail that checks for holes pre-publishing and if there it it has
a remediation process that checks the source files, if they are not there it does targeted egress."*
Then: *"yes do all of the above."*

> ⚠ **MORATORIUM CARVE-OUT, CITED SO A LATER SEAT DOES NOT READ THIS AS A VIOLATION.** CLAUDE.md carries a
> standing ban on building alerts/monitors/freshness-checkers **"unless Andrew explicitly asks."** He asked,
> in the words quoted above. **Scope of the carve-out: a PRECONDITION inside the existing render path and a
> catch-up inside existing producers. It does NOT authorize a new monitor, alarm, SNS topic, or standing
> freshness service** — and §7 forbids exactly that.

---

## 1. The problem, measured

On 2026-09-01 the served August report was rendered from a month that was missing **5 of 21 Cottonwood
trading days** (08-04, 08-18, 08-20, 08-21, 08-31). The July report was rendered **4h10m before** a batch of
8 late slices landed and was never rebuilt.

**Neither failure was visible in the artifact.** Carry-forward fills a hole with the previous day's value, so
a gap and a held position render identically. The monthly average was computed over incomplete data and
nothing said so.

**Root cause of the Cottonwood gap: the producer never fired for those dates.** The upstream holdings existed
in `opal-data-assets` the whole time, fully priced (10,958–11,929 priced positions per day). No vendor data
was missing. **No egress was required to repair it.**

---

## 2. The taxonomy the guardrail MUST implement

A day with no slice means one of four things, and **three of them are correct**. A gate that cannot tell them
apart is worse than no gate — it will either block valid months or trigger fabrication.

| # | Case | Detect by | Correct action |
|---|---|---|---|
| A | **Market closed** (weekend/holiday) | `lib/trading_calendar.py` — not a trading day | NOTHING. Carry-forward is the true value. |
| B | **Source present but UNPRICED** | upstream partition exists, `priced == 0` | NOTHING. The producer's ZERO-vs-MISSING contract deliberately writes no slice. **Filling this fabricates data.** |
| C | **Producer never fired**, upstream present | trading day + upstream partition EXISTS + no output | **RE-RUN the producer for that date.** Internal, no egress. *This was 5 of 5 of the August gaps.* |
| D | **Upstream genuinely absent** | trading day + upstream partition MISSING | **Targeted egress** — the only case that leaves our infrastructure. |

⛔ **Case B is the trap.** It is indistinguishable from case C by counting slices alone. The discriminator is
reading the upstream partition and counting priced positions — which is exactly the check I ran before
backfilling, and it is the check that separated a legitimate repair from inventing five days of AUM.

---

## 3. Component 1 (PRIMARY) — daily catch-up in the producers

**Do not build this. Port it.** `inf-etf-ownership-daily` already has `_catchup_missing_dates`
(`lambda_function.py:274-293`) and that is precisely why Inflection was **43/43** while Cottonwood silently
accumulated five holes. `cot-etf-ownership-daily` and `bd-49f-etf-ownership-daily` have **zero** hits for it
(measured, `comp-read --enumerate`, denominators printed).

**Mechanism as it exists:** after processing today's date, walk back `CATCHUP_WINDOW_DAYS`; for each date —
skip if it is the date just processed; skip if output already exists (idempotent); **skip if the upstream
partition is not present** (so it can never fabricate); otherwise process it. Per-date failures are caught and
reported in `catchup_processed` / `catchup_failed`, never fatal.

### ⛔ THE PORT IS NOT A COPY — the window constant is wrong for 49F

`CATCHUP_WINDOW_DAYS = 10`, hardcoded. **Measured upstream delivery lag, July–August 2026:**

| Partner | lag distribution | max | 10-day window sufficient? |
|---|---|---|---|
| Cottonwood | 1–6 d | **6** | YES, with margin |
| 49 Financial | mostly 1–5 d, tail at 6, 7, 8, **12, 13** | **13** | ⛔ **NO — structurally misses the tail** |

A 49F day delivered at lag 12–13 falls out of a 10-day look-back **before its upstream ever arrives**, so it
would never be caught up. A straight port would look correct, pass review, and leave exactly the failure mode
it was built to close. Schwab is ad-hoc-batch, so the tail is **not bounded by anything we control** — do not
pick a number from this table and call it safe.

⭐ **RULED — Andrew-direct 2026-09-01, verbatim: *"I agree with the reporting obligation window."*** Rec 1
below is the BUILD VALUE. Rec 1b is retained only as a record of the rejected alternative; **do not implement
a day-count window.**

**RULED (rec 1):** replace the fixed look-back with a **reporting-obligation window** — reconcile every
trading day from the **start of the prior month** forward, until that month's report has shipped. That is
bounded, self-evidently sufficient for a monthly obligation, and does not require anyone to guess a vendor's
worst-case lag. Cost: a few extra `head_object` calls per daily run over ~40 dates.
**NOT TAKEN (rec 1b), recorded so it is not re-proposed:** a per-partner env-var day count set from measured
max lag. Rejected because it makes correctness depend on a vendor lag distribution nobody controls — 49F's
observed tail (13 d) already exceeds the shipped constant (10 d), and Schwab is ad-hoc batch, so the tail has
no upper bound we can cite.

⛔ **Implementation note the ruling implies:** the window's terminus is *"until that month's report has
shipped"* — so the catch-up needs a SHIPPED signal to stop at, not a date. Use the existence of
`platinum/reports/{YYYY-MM}/etf_ownership.pdf`; do not re-derive "has it shipped" from a calendar assumption,
or a blocked/failed render silently ends the very reconciliation that would have unblocked it.

**Lanes:** `0.7.0_AE_CloudOps` (Lambda + Terraform; `aws lambda update-function-code` is FORBIDDEN — Terraform
only, CLAUDE.md NEVER-9).

---

## 4. Component 2 (BACKSTOP) — pre-publish coverage gate

**Ordering, and it matters:** a check that first runs at 14:00Z on the 1st can only *block the send* — it
cannot manufacture a month of missing data inside a render window. **The catch-up is the guardrail; the gate
is the proof.** Build both, in that order, and do not let the gate become the primary.

**Where:** a precondition inside `render_month_end.py` (or the orchestrator immediately before it) — NOT a
standing service.

**What it computes,** per partner, for the month being rendered:

```
trading_days      = lib.trading_calendar    (Jul 2026 = 22, Aug 2026 = 21)
slices_present    = daily/{partner}/{date}.json
missing           = trading_days - slices_present
  for each missing day, CLASSIFY (section 2):
     upstream absent            -> class D  (egress candidate)
     upstream present, priced=0 -> class B  (EXPECTED, not a hole)
     upstream present, priced>0 -> class C  (A REAL HOLE)
```

**Verdict:**
- `C == 0` → **PUBLISH.** (B and D are reported, never silently swallowed.)
- `C > 0` → **attempt remediation** (§5), re-evaluate, then publish or refuse.

**The report must carry its own coverage line regardless of verdict** — per partner,
`"21/21 trading days; 0 carried for missing data"`. This is the durable fix for the original defect: the
artifact could not show its own gaps. Coverage belongs *in* the artifact, not only in a gate that runs once.

**Lanes:** `0.4.0_DS_ClientPlatform` (renderer) + `0.7.0_AE_CloudOps` (orchestrator wiring).

---

## 5. Component 3 — the remediation ladder

Ordered. **Each rung runs only if the one above it did not resolve the day.**

1. **RE-RUN THE PRODUCER** (class C). `lambda invoke --payload '{"date":"YYYY-MM-DD"}'` — every producer
   already has a dated backfill path and it LOUD-fails on an absent partition rather than no-oping. *This
   resolved 5 of 5 real holes on 2026-09-01.*
2. **RE-CHECK UPSTREAM** — the partition may have landed since the last producer run.
3. **TARGETED EGRESS** (class D only) — fetch the specific missing date from the vendor, land it in the
   normal silver path, then return to rung 1. **Never write a slice directly from a vendor response.**

> ⛔ **Correcting the framing in the original ask:** egress is the **third** fallback and should almost never
> fire. In the only real instance we have, **all five days were already in `opal-data-assets`** — the hole was
> a producer that never ran, not missing vendor data. Keep egress last: it is the only rung that leaves Opal
> infrastructure, and per CLAUDE.md it requires Andrew's explicit per-use word today.

⛔ **NO RUNG MAY FABRICATE.** If all three fail, the day stays missing and the gate reports it. A guardrail
that invents a value to make itself pass is the worst possible outcome here.

**OPEN — ANDREW'S CALL (rec: automate rungs 1–2, keep rung 3 manual):** rung 3 is vendor egress, which
currently needs per-use authorization. Standing pre-authorization for a *bounded, targeted* backfill fetch is
a sovereign decision, not one this spec should assume.

---

## 6. Component 4 — the email

**Current:** `etfs-reports-orchestrator` env `EMAIL_RECIPIENT = andrew@opalinvest.com`, sender
`noreply@opalinvest.dev`, fired by EventBridge Scheduler `etfs-reports-monthly-run`,
`cron(0 10 1 * ? *)` America/New_York (= 14:00Z, DST-native).

**Change:** recipient to `aj@opalinvest.com`. Make it a **comma-separated list**, not a single string, so
adding a recipient later is a variable change rather than a code change.

**Gate the send on §4:** the monthly email fires only on a PUBLISH verdict. On a refusal it does not send —
and the refusal must be visible, because **a monthly report that silently does not arrive is indistinguishable
from one nobody opened.** Route the refusal through the orchestrator's EXISTING `REPORTS_SNS_TOPIC`
(`etfs-reports-alerts`) — **no new topic, no new alarm** (§7).

**OPEN — ANDREW'S CALL:** does `aj@` **replace** `andrew@` or **join** it? Spec assumes REPLACE; one word
changes it.

**Prerequisite:** SES identity verification for `aj@opalinvest.com` if not already verified — a send to an
unverified address in a sandboxed region fails at delivery, after the render has already succeeded.

---

## 7. What NOT to build (build ladder, YAGNI)

- ⛔ **No new monitor, alarm, SNS topic, or freshness service.** The carve-out in the header is narrow.
- ⛔ **No new catch-up engine** — port `inf`'s. Two implementations of one convention drift, and only one gets
  fixed; that is exactly how `_carry` and `_carried_daily` diverged and produced a $200M chart error this
  session.
- ⛔ **No parallel/shadow pipeline or standing parity comparator** (Andrew complete veto). Modify the
  producers in place.
- ⛔ **No DynamoDB.** The 2026-08-24 design gate ruled S3 gold parquet. See §9.

---

## 8. Acceptance tests

Each must be **exercised**, not asserted. A declared-but-unrun falsifier is a promise, not a control.

| # | Test | Pass |
|---|---|---|
| A1 | Delete a cot slice for a trading day whose upstream exists+is priced; run the daily producer | slice regenerated; `catchup_processed` names the date |
| A2 | Run the gate on August 2026 **as it was before the 09-01 repair** (5 real holes) | verdict REFUSE, exactly 5 class-C days named |
| A3 | Run the gate on August 2026 as it stands now | verdict PUBLISH, 0 class-C |
| A4 | Point the gate at a day with an upstream partition where `priced == 0` | classified **B**, NOT a hole, **no backfill attempted** |
| A5 | 49F date delivered at lag 12–13 (the §3 tail) | caught up — **this is the test a naive port fails** |
| A6 | Gate REFUSE path | no SES send; refusal surfaced on the existing topic |
| A7 | Rendered report, any month | carries a per-partner coverage line |

**A5 is the one that matters.** It is the only test that fails on a plausible, review-passing implementation.

---

## 9. Two findings from the lineage trace — not part of this build, but do not lose them

1. ⛔ **`etfs-canon-fanin` is ENABLED on `cron(45 15 * * ? *)` and targets DynamoDB table
   `opal-etfs-ownership-daily`, which DOES NOT EXIST** (`describe-table` →
   `ResourceNotFoundException`). It is the residue of the architecture the 2026-08-24 design gate overruled.
   It fires daily and cannot succeed. **Rec: retire the Lambda and its schedule.** Owner `0.7.0_AE_CloudOps`,
   gate `1.0.0_SA_CTO`.
2. ⚠ **Inflection's lineage does not reconcile and I did NOT resolve it.** Repo source computes a
   `opal-data-assets/orion/inflection/silver/fact_positions` path; every slice 07-16 → 09-01 cites
   `opal-data-inf/gold/canonical/holdings_`. Both paths exist and are populated. The deploy (2026-08-11)
   **postdates** the last repo change (2026-08-03 @`001a73530a`). **Those three facts do not fit together.**
   Resolving it needs a deployed-bytes diff against the build input (CLAUDE.md 22a) — not a source read.
   **This matters to THIS build:** §5 rung 2 must check the bucket the producer *actually* reads, and for
   Inflection nobody currently knows which that is from the code alone.

---

## 10. Sequencing (for COO decomposition — this spec dispatches nothing)

```
  1. AE   port catch-up -> cot- + bd-49f-, window per rec 1     [closes the recurrence]
  2. DS   coverage classifier (A/B/C/D) as a callable           [the discriminator]
  3. DS   coverage line into the rendered report                [artifact shows its own gaps]
  4. AE   gate wired as a render precondition + send gating     [the backstop]
  5. AE   EMAIL_RECIPIENT -> list, aj@opalinvest.com + SES verify
  6. CVO  exercise A1-A7, A5 mandatory
  7. AE   retire etfs-canon-fanin (§9.1) -- independent, can run in parallel
```

**Do 1 before 4.** Shipping the gate first converts a silent wrong number into a blocked report without
fixing the cause — and the first thing a blocked monthly produces is pressure to override the gate.
