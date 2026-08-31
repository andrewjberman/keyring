# Relaunch, then the ADVI_INSURE determination: nothing failed on 08-29 — a converter was extended to a feed the scheduled producer never produces — 0.7.0_AE_CloudOps~K

**Date:** 2026-08-30
**Task Order:** ad-hoc relaunch load (MSTR hint 00:20Z) → `2.0.0_SA_COO` 84023 [DRIVE] ADVI_INSURE determination
**Status:** COMPLETE — RAVC2 returned (84094/84095/84096/84097); nothing owed at this seat

---

## Objective

Post-reboot relaunch: re-establish reachability, run the `org/XXX.md` startup protocol, ACK the
issuer, and resolve whether the `_broker_health()` probe fix belonged here. Then execute the work
`2.0.0_SA_COO` routed on the back of that ACK: **determine why `insurance_relationshipdetail` has
no 2026-08-29 partition after the 04:35Z fire** — (i) fan-out never invoked, or (ii) invoked and
received nothing. Read-only forensics, hard scope cap.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | A.3 EXERCISE limb — scored on OUTPUT (its banner), not rc. |
| (forwarder census) | `command -v` over `.tools/comp-*` | PASS | `105 of 105 resolve bare` — denominator printed. |
| comp-find | `comp-find "insurance_relationshipdetail" --all` | PASS | 59 hits / 130,918 scanned, bands DEF=1 SURFACED=3 CONFIG=3 DOC=52. The single `[DEF]` row put me straight on `bd49f_insurance_conversion.py:123` — the converter side of the finding. |
| comp-find | `comp-find "bd49f_reporting_pull" --all --files` / `"insurance_leg" --all --files` | PASS | `[HEAD]` band resolved the TF and the Lambda module in one hop each. |

**What worked:** The banded output did real work here. `[DEF]` vs `[DOC]` separated *the converter
defines this feed* from *52 messages talking about it* — that separation IS the finding, and a flat
grep would have buried the one definition line under the discussion.
**What failed:** Nothing.
**Gap found:** none.

---

## Work Completed

### 1. Reachability (no orphan, no kill)

Registered PID 27064; Monitor `bb6xd80pk` persistent, `TaskOutput` → `running`, arm banner
`parent-tied: pid 118503` (**ARMED, not orphan-capable**). No pre-existing watcher for this lane
existed at load, so no kill was warranted and none was performed. `CronList` → zero jobs.
Stream confirmed **end-to-end**, not merely armed: its first event delivered 83915. READ-clock acks
recorded for 83915, 84010, 84023, 84030.

### 2. `org/XXX.md` A / A.1 / A.2 / A.3 / B / B.1

A.2 returned exactly the two findings `org/XXX.md` names as KNOWN and OWNED-UNTIL-`rv0057-f001`
(`to-pos-override-audit.log` uncovered; baseline 2026-08-20T042433Z, 236.6h). **Not re-filed** — no
third finding, no shrink row, no absence row, which is the only condition under which that note
licenses silence.
B.1 `to-check --all --assignee 0.7.0_AE_CloudOps~K` → `total=0 scanned=2191`, **reported as
uninformative, not as idleness** (the documented `SEATED:`-notation blindness). Corroborated by the
dispatch-message read and `2.0.0_SA_COO` 83846.

### 3. `ADVI_INSURE.TO-A4-AEC` — re-derived, not inherited

`:12` reads `<status>complete</status>`; the 05:4xZ `issuer_record` records AC4 ACCEPTED, all five
PASS, proof VALID bare rc=0 @`fe060aa6cf`. **AC4 not re-graded** — the 04:35Z fire is the single
shared discriminator both TOs spend; a re-read cannot strengthen it and a divergent re-read would
be a false alarm. World-done closes SUPERSEDED.

### 4. Broker thread — routing closed, not built

83915 named the defect at `org/mcp/server.py:512-520` (`_broker_health()` bare `except` over a 2s
`urlopen` → a busy broker reads ABSENT → `_ensure_broker` spawns a second). Measured at 01:1xZ:
`127.0.0.1:7800 LISTENING pid 4856` — **one** listener. ⛔ Reported as the **pre-duplicate state,
not an all-clear**: the reboot cleared the process table and the mechanism predicts birth at a seat
launch under load, not at rest. 84010 adopted that framing and **ruled the fix stays with
`1.0.0_SA_CTO`** as `org/mcp` lane owner. Asking cost one message; guessing would have put an AE
edit into the CTO lane's comms substrate on a second-person pronoun in a six-recipient message.

### 5. LD-0477 corroborated on a second instrument

Win32 `CreationDate` via CIM: every python sidecar born ≥ 23:16Z 08-29; the liveness-retry fix
landed ~20:15Z; reboot 23:17Z. All sidecars are post-fix. Offset read from the clock, not assumed:
`UTC 2026-08-30T01:12:12Z == LOCAL 2026-08-29 21:12:12 EDT`. Named as a **second instrument on one
claim**, not a second seat agreeing. Not re-sent (84010 said no reply needed).

### 6. ⭐ THE DETERMINATION (84023) — verdict (i), and wider than (i) as written

**The leg never invokes `relationshipdetail` on ANY fire.** The surface is *defined* in the
deployed module and is *not in the production driver's call path at all*. (ii) is excluded.

**6a. Deployed code, at EXERCISED state.** Package pulled via `lambda get-function` Code.Location
and opened:

```
deployed insurance_leg.py sha256  5ba2562a512ee1aaf673e8d8e449541cf8f78df31ca8cb5bffd510b1c422760e
pin 52ffb6c8a3        sha256      5ba2562a512ee1aaf673e8d8e449541cf8f78df31ca8cb5bffd510b1c422760e
BYTE-IDENTICAL: True
NEG CONTROL  prior vintage d0f9a8f7e4 vs deployed -> NOT equal   (the check discriminates)
live CodeSha256 0XJf+G2pBpIIuxTUUOYWBsJVVm4trytwCGCpfqkzNE0=, LastModified 2026-08-28T18:09:29Z
```

So reasoning from `52ffb6c8a3` **is** reasoning about running bytes — the
running-bytes-older-than-built trap is closed by measurement, not assumed away.

`run_insurance_leg()` @ `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/insurance_leg.py:588`
@`52ffb6c8a3` has exactly two limbs: `:612 fetch_detailsearch_all_pages(...)` and
`:617 receipt.update(run_and_download_export(...))`. Measured on the deployed bytes:
`relationshipdetail` occurs **2× in the whole module** — both registry entries (`:122`
`SURFACE_EGRESS`, `:143` `SURFACES` → `("GET", "/relationship/request/relationship/%s", "clientview")`)
— and **0× inside `run_insurance_leg`'s body**.

⛔ **A competing explanation ruled out affirmatively:** `SURFACE_EGRESS["relationshipdetail"] =
(True, "")`. The feed is egress-**sanctioned**, so this is not the fail-closed guard refusing it —
that guard raises its reason string verbatim at the call site, and no such refusal is in the log.

**6b. Runtime — the 04:35Z fire.** Stream `2026/08/29/[$LATEST]66655a500c034920b6a3d66ee7f8ace0`,
RequestId `325f3836-0292-418e-96f5-4cbb58a26501`. Complete stream = 5 events:
`BD49F-INSURANCE: pull_date=2026-08-29 pages=2 rows=77 attested_total=77
completeness=measured-complete receipt=LANDED (DRY_RUN=False)` at 04:35:19Z; END/REPORT
Duration 12741.01 ms. **No error, no exception, no retry.** A clean 12.7s success is independently
inconsistent with a 77-id per-relationship fan-out having been attempted and failed.

**6c. The negative control 84023 required.**

| feed | in `run_insurance_leg` body? | per-feed token in the 04:35Z log? |
|---|---|---|
| `relationshipaccountdetailsearch` | YES (`:612`) | YES — `pages=2 rows=77 attested_total=77` |
| `insurancerelationshiplist_export` | YES (`:617`) | YES — `receipt=LANDED` |
| `relationshipdetail` | **NO** (0 occurrences) | **NO** (no token at all) |

✅ Positive for 2 of 3, negative for 1 of 3 — the instrument is **not blind to feeds generally**, so
this is a real negative rather than an instrument that cannot see invocation. That is precisely the
distinction pre-committed to in the ACK (84036).

**6d. ⛔ The reframe — the part that changes what anyone should do.** **Nothing failed on 08-29.**
My own `s3api` read, fully paginated with the denominator printed: **14 keys**, and
`insurance_relationshipdetail/` has **one partition in the entire estate — `2026-08-27/`**. The
08-28 17:43Z fire (stream `2026/08/28/[$LATEST]44b6d3e6978f47e8864b7611309d740b`) also landed
detailsearch + export and no relationshipdetail. **The 08-27 partition is the anomaly; the 08-29
absence is the norm** — 08-27T18:31:25Z predates the leg becoming schedule-reachable and is cited
as a manual capture in `0.6.0_AE_PartnerETL`'s `ADVI_INSURE.TO-A2-AE_PROOF_OF_SPEC.json:19`.

**The real gap:** the SILVER CONSUMER was extended to a feed the SCHEDULED BRONZE PRODUCER does not
produce. `data/assets/scripts/silver/bd49f_insurance_conversion.py:123` defines `FEED_DETAILREL`
and converts it at `:458`/`:495` per COO's 08-28 four-table ruling; `run_insurance_leg` was never
extended to match. **Two carriers of one contract, and only one moved.**

**Owner:** `0.6.0_AE_PartnerETL` — sole author of all three `insurance_leg.py` commits
(`52ffb6c8a3`, `d0f9a8f7e4`, `d7583e51b2`) and holder of `ADVI_INSURE.TO-A3-AE`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Verdict (i), stated WIDER than the dispatch framed it | The dispatch asked about the 04:35Z fire; the evidence shows the call path has never contained the feed. Answering only the narrower question would have left the reproduction unseen. |
| Refused to adjudicate whether the producer SHOULD carry the feed | Two readings survive the evidence — (a) producer missing a feed, (b) converter extended ahead of a deliberately-sequenced producer act. Code and logs cannot separate a missing act from a sequenced one. Issuer's call. |
| Did NOT recommend extending the producer | It is a vendor-egress increase (77 ids → 77 calls). Availability is not authorization; that needs the issuer's word and Andrew's per-use word for widened BD egress. |
| Ran the deployed-bytes identity check with a negative control | The claim feeds an ownership determination routed to another seat. Source-only reasoning would have been one rung short of EXERCISED. |
| Did NOT re-grade AC4; did NOT patch `server.py` | Closed row / other seat's lane. See §3, §4. |
| Re-derived the S3 state rather than inheriting 83966 | Same discipline `2.0.0_SA_COO` applied in 83811. My read matched — which is what makes it corroboration rather than repetition. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/mcp/sessions/e3f9e420-...serial` | A.1 serial file written at load | untracked runtime artifact |
| this log | new | see commit |

**No code, no Terraform, no AWS mutation. No apply, no deploy, no S3 write, no vendor call.**

---

## Blockers

**NONE at this seat.** Nothing here waits on anyone.

**Owned elsewhere, listed so it is not read as dropped:**
- [`0.6.0_AE_PartnerETL`] the producer-side scope call on `relationshipdetail`. Message 84096 is
  **QUEUED, not delivered** — that seat was not live at 01:3xZ.
- [`2.0.0_SA_COO`] the (a)/(b) scope ruling. [`3.0.0_SA_CVO`] grades.
- [`1.0.0_SA_CTO`] the `_broker_health()` probe fix, at that seat's priority.

---

## Current State

`0.7.0_AE_CloudOps~K` is LIVE (PID 27064), reachable (Monitor `bb6xd80pk`, `parent-tied: pid
118503`), zero crons. `ADVI_INSURE.TO-A4-AEC` is `complete` with AC4 accepted @`fe060aa6cf`. The
84023 determination is **returned and closed at this seat**: verdict **(i)** — `insurance_leg.py`'s
`run_insurance_leg` (deployed bytes byte-identical to `52ffb6c8a3`, negative control passed) never
calls `relationshipdetail`; the 04:35Z fire logged a clean 12.7s success landing 2 of 3 convertible
feeds with no error; the absence reproduces on the 08-28 fire and the only partition estate-wide is
a manual 08-27 capture. **The finding is a producer/consumer contract split, not a failed fire**,
and the open question left for the issuer is scope, not fact.

⛔ **RECORD GAP, disclosed rather than papered over: there is NO 2026-08-29 log for this lane.**
`logs/` holds `2026-08-26/` and `2026-08-28/` only. The 08-29 `~K` session graded AC4 at ~05:3xZ and
made the broker-duplicate catch 83915 credits — and left no session log. **This entry does not
reconstruct it**: everything above about 08-29 is sourced from the committed face, `fe060aa6cf`, and
the message record (83811 / 83846 / 83875 / 83915 / 84010), never from recollection this session
does not have.

---

## Next Steps

1. **[`2.0.0_SA_COO`] Rule (a) vs (b)** on whether the scheduled producer should carry
   `relationshipdetail` — the determination is fact-complete and waits only on that call.
2. **[`0.6.0_AE_PartnerETL`] On return, read 84096** — the producer-side lane owner.
3. **[`0.7.0_AE_CloudOps~K`] Idle-available** for the next `2.0.0_SA_COO` allocation.
4. **[`1.0.0_SA_CTO`] The `_broker_health()` probe fix** — listed for traceability, not chased.

---

**Push state:** stated as a MEASURED value in the commit report, never a default.
