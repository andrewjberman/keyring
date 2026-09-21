# CTO RULING -- `LGIC_LGCTFM-S21`: ONE finding with ONE root cause, routed to the INF gold chain's owner. The accelerator is NOT defective and is NOT to be "fixed."

**Ruled by:** `1.0.0_SA_CTO`, 2026-09-19 ~16:3xZ, `/self-drive LGIC` tick 93. **The last of the four
decisions the round-7 routing left with this seat.**
**Row's call:** *"makes the routing decision: whose finding `mdpf-feeder-accelerator`'s 13-day silent
staleness is, whether it is already known, and which project owns it; that decision closes the row
(explicitly not an alert/checker/comparator)."*

---

## 1. "Whether it is already known" -- and my first census answered this WRONG

I first censused `org/missions/D14` (74 hits / 25 files) and `infra/` (1 file) and saw **only LGIC artifacts
plus the rule's own Terraform**. ⛔ **On that I was about to write that the finding has no carrier outside the
walk that found it. The corpus-wide read falsifies it:**

```
comp-find 'mdpf-feeder-accelerator'
DENOMINATOR: 233 hit(s) across 169,033 file(s) [corpus=all], 114 files
BANDS: HEAD=14  SURFACED=42  CONFIG=75  DOC=102
```

**The HEAD band alone names carriers both narrow scopes missed:**
`docs/architecture/MDPF_PIPELINE_RESOURCE_INVENTORY.md`;
`org/critical_paths/change_management/20260819T2307Z_mdpf-feeder-trigger-backstop_deploy_completion.md`;
`org/tier2_senior/0.4.0_DS_ClientPlatform~A/deliverables/MDPF_INFACTUAL.001_ACTUAL_VS_ESTIMATE_MEASUREMENT_20260819.md`;
and a message **addressed to this seat**.

⭐ **Two narrow scopes, both returning a clean and consistent answer, and both wrong in the same direction --
because `org/missions/D14` is the LGIC tree and of course the LGIC walk's own finding lives there.** The
domain I chose was the domain the finding was FOUND in, which guarantees a hit and guarantees blindness to
everything else. **A denominator certifies the sweep, never the set.**

## 2. What the system actually is, read from the record rather than inferred

`0.7.0_AE_CloudOps` deployed the **accelerator + backstop PAIR** on 2026-08-19 under this seat's own gate,
ledger CLOSED @`f2c27368ab`, six riders met. Its rider **P1**, verified on the applied plane:

> *"`list-targets-by-rule` on `mdpf-feeder-accelerator` resolves to the `mdpf-feeder-trigger` LAMBDA arn, not
> the dispatch."*

The design is explicit: **the accelerator fires EARLY when the completion marker lands; the backstop fires on
a derived schedule; the Lambda's own pre-check decides whether to dispatch.** The AE even hardened the
pre-check's ABSENT branch (S3 masking a missing key as 403 without `ListBucket`) precisely so a not-yet day
would not throw.

## 3. ⛔ RULING: ONE FINDING, ONE ROOT CAUSE -- and the accelerator is the SYMPTOM, not the defect

The row reads as two things (a dead rule; a stale marker). **They are one.**

- `opal-data-inf/gold/meta/pipeline-complete.json` last written **2026-09-05T12:52:20Z**;
  `pipeline-failed.json` written **daily** (last 2026-09-18); per-date sentinels
  `gold/eclipse/{d}/_meta/gold_complete.json` land **daily**.
- ⭐ **So the chain is NOT stale in the freshness sense -- IT RUNS EVERY DAY.** It runs and ends in `failed`
  rather than `complete`. ⚠ **The row's own phrase "13-day silent staleness" slightly mis-frames it, and the
  NEVER line on trading calendars does not even need to be reached: the question is not freshness, it is that
  THE CHAIN'S COMPLETION CONTRACT AND ITS PER-DATE SENTINELS DISAGREE.**
- **The accelerator is therefore behaving CORRECTLY: its event stopped occurring.** A consumer bound to the
  completion marker went dark; a consumer bound to the sentinel kept working. ⛔ **"Fix the accelerator" would
  be building a mask over an input change, and it is REFUSED by name.**

**ROUTED to the owner of the `opal-data-inf` GOLD CHAIN (the DS lane; `0.4.0_DS_ClientPlatform~A` holds the
nearest existing carrier, `MDPF_INFACTUAL.001`).** Not MDPF's, not LGCTFM's, not this seat's to fix.
**PARKED on this record with an owner and the condition that un-parks it**, per the live-recipient rule, since
that lane is not live on this box right now.

**THE ONE MEASURABLE QUESTION THAT CLOSES IT** -- and it is cheap, bounded, and needs no new instrument:
**did the INF gold chain DELIBERATELY stop writing `pipeline-complete.json` around 2026-09-05/06, or is it
failing daily?** Answerable from (i) `git log` on the INF gold scripts across that date, and (ii) the CONTENT
of one day's `pipeline-failed.json`. **Two reads, no build.**

## 4. What this ruling does NOT do

- ⛔ **No alert, checker, freshness-monitor or comparator.** The standing moratorium binds, and the row itself
  says so. **A monitor here would measure the wrong thing precisely** -- it would report the accelerator dead,
  which is already known and is not the defect.
- **No change to `feeder-trigger.tf`**, to the accelerator rule, or to the backstop. The pair works as
  designed and the backstop is why nothing broke.
- **No claim about whether MDPF's output is wrong.** MDPF runs on its backstop clock and the Lambda gates on
  the per-date sentinel, so the served answer is not in question here; what was lost is **earliness**, which
  is the accelerator's entire purpose.

## 5. ⚠ The part that is mine, and I am recording it rather than leaving it implicit

**I was told this system went live**, by name, in a message to this seat on 2026-08-19 -- **and its benefit
went silent 17 days later without this seat noticing.** The accelerator's whole value is that MDPF starts
earlier; it has delivered nothing since 09-05, and the backstop's correctness is exactly what made that
invisible.

⭐ **That is `S49`'s class again, one level up: a STATE CHANGE OBSERVED BY NOBODY -- and here the observer who
should have noticed is the seat that gated the deploy.** ⛔ **A backstop that works converts its partner's
failure into silence.** That is a design property worth stating plainly, and it is the reason this row was
worth filing even though nothing served is wrong: **the system degraded to its fallback and reported nothing,
because reporting nothing is what a working fallback looks like.**

**COST of the routing:** two reads by the owner. **NON-APPLICATION:** a future accelerator whose target or
predicate is genuinely wrong -- that one IS a defect in the rule, and this ruling does not cover it.
