# MDPF_HEALGAP -- a source that recovers, an ingest that re-runs: Cottonwood Rebalancer bronze heals itself

```json
{
 "project": "MDPF_HEALGAP",
 "directive": "D8",
 "fabric": "laptop",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/mdpf-healgap-midstream-brief-20261007.md@a8c67a424e",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "RATIFIED"
}
```

**Author:** `1.0.0_SA_CTO~DELL1` (L2-L4), 2026-10-07, under laptop `1.0.0_SA_CTO` ruling 106047 (1) and the NFRA_CTLPLN v0.12
addendum ("each Dell's CTO writes L4 and L10 for its projects").
**Brief:** `docs/briefs/mdpf-healgap-midstream-brief-20261007.md` @a8c67a424e (`4.0.0_SA_CRO~DELL1`, `--midstream`).
**Andrew's words:** at the `0.0.0_AB_MSTR~DELL1` terminal ~07:52Z 2026-10-07, VERBATIM: "Explain to me the logic behind
MDPF_HEALGAP. I am intrigued but would need the whole process to go through canonical-flow form. I recommend spawning a
4.0.0_SA_CRO agent to proceed that with CTO." Record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261007_075xZ_MDPF_HEALGAP_THROUGH_CANONICAL_FLOW_CRO_WITH_CTO.md`.
The project's original word (2026-08-31): "We do need to fix this, this needs to be a project underneath D8. Write a brief on it"
(`docs/architecture/MDPF_HEALGAP_BRIEF.md`).
**Placement:** dell1, by laptop `1.0.0_SA_CTO` msg 106053 (`org/projects/MDPF_HEALGAP.json` @5e3b7edf26). COO lane
`2.0.0_SA_COO~G1`, held unseated by `0.0.0_AB_MSTR~DELL1` until this PRD is ADMITTED.
**Sign-off:** `3.0.0_SA_CVO` (dell1) signs the ratified-text half. The brief half is accepted because the CRO wrote the brief.
**Supersedes:** the project's pre-canonical state (an MSTR purpose brief, an uncertified decomposition, and one gold-layer cell
shipped as `data/mdpf/scripts/gold/mdpf_gold_catchup.py`). That cell stays. It is downstream of this project's hole (C-LAYERS).

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  On a day the morning Cottonwood model pull fails because the vendor login has lapsed, a reader
         of the Cottonwood models sees that day's figures by the end of the same day, with nobody acting
         DONE WHEN  EXERCISED -- one morning pull deliberately made to fail, followed to that day's figures
                    on the reader's page; the next naturally failed morning is the negative arm, never the test
         ACCEPT     on a day the morning pull was made to fail, a reader of the Cottonwood models sees that
                    day's figures by the end of the day, and nobody did anything between the failure and the
                    figures appearing; a day left empty, or filled because a person noticed, fails the outcome
         SOURCE     brief PART I, candidate thread; O1

  FWD-2  Anyone reading a run's result can tell whether every part of that day's data arrived
         DONE WHEN  EXERCISED -- one run in which one of the three kinds of data is missing, read from the
                    run's own result
         ACCEPT     an operator reading how the run went can say which kind of data is missing for which day
                    without looking anywhere else; a run missing any part of the day that reads as a success
                    fails the outcome
         SOURCE     brief O2; PART VI.4 (ten days with two of three parts landed)

  FWD-3  An operator closes an existing hole with one act that says beforehand exactly what it will fetch, and a day
         that cannot be truthfully fetched is shown as missing, never filled with another day's data
         DONE WHEN  EXERCISED -- one hole repaired by one act on the day it opened (the source serves current state
                    only), the hole induced on purpose as FWD-1's was; and the eleven days 2026-08-31 to
                    2026-09-10 read as marked-missing, not filled
         ACCEPT     before it fetches anything, the repair says which days and which kinds of data it will
                    fill; afterwards exactly those are present and nothing else changed; a repair that
                    notifies instead of fixing, that fills days it did not name, or that puts today's data
                    under a past date, fails the outcome. A reader of the eleven days sees they are missing
                    and why
         SOURCE     brief O3; PART VI.2; ADDENDUM v0.2 (Andrew-direct 2026-10-07 ~13:58Z, "no refill")

  FWD-4  Someone reading only the runner's settings correctly predicts how it retries
         DONE WHEN  APPLIED -- the settings in place say what the system actually does
         ACCEPT     a reader who sees only the settings can say how many times and over how long a failed
                    morning pull is retried, and is right; settings that promise a window the system cannot
                    deliver fail the outcome
         SOURCE     brief O4; PART IV.4

  FWD-5  The morning pull is scheduled after the login refresh it depends on
         DONE WHEN  APPLIED -- the two schedules in place put the pull after the refresh
         ACCEPT     someone reading the two schedules sees the morning pull set to start after the daily login
                    refresh, with room to spare in both summer and winter time
         SOURCE     brief O5 (a mitigation that makes FWD-1 rarer, never a replacement for it)

  FWD-6  Every other scheduled data pull that leans on a login refreshed elsewhere has an answer
         DONE WHEN  APPLIED -- the written answer, each entry grounded on what was read
         ACCEPT     the owner of the data estate has a list of every scheduled data pull whose success depends
                    on a vendor login kept alive by something else, counted against a fresh count of every
                    scheduled pull, each marked "recovers the same way", "not exposed, because ...", or "exposed,
                    and only a person can renew the login": the last names the person's act and where that act
                    is listed when it is owed; a pull left without an answer fails the outcome
         SOURCE     brief O6 (the 49F login chain first; no claim that it is exposed)
```

## ACTS ONLY ANDREW CAN DO (each with its citation)

1. **Standing vendor word for the same-day re-pull (FWD-1).** The mechanism calls Black Diamond's Rebalancer a second
   time on a day the first call failed. Citation: CLAUDE.md, "NEVER call an external vendor API without Andrew's explicit
   per-use word", and brief PART V.4. The exercise of FWD-1 is held until he words it, as a standing grant for this one
   runner or per use.
2. **Per-use vendor word for the repair of the eleven days (FWD-3).** Same citation. **Disclosed before he spends it (the
   2026-09-01 lesson, `/endpoint` 9b):** the 2026-09-01 one-shot re-run filled two of the three feeds for 2026-08-31 and NOT
   the model detail (brief PART VI.3). From 2026-09-01 the runner landed two feeds daily without the third (PART VI.4), and
   that cause is unread. A repair fired before that cause is read may return the same empty result. Round 1 reads the
   cause first, with no vendor call (section 2, hop 0), and the word is asked for only when the read predicts that the
   repair will fill the days.

## CONTRACTS

| Contract | Direction / owner | Binding agreement |
|---|---|---|
| C-LAYERS: which layer each outcome grades at | this project | FWD-1 to FWD-5 grade at the INGEST layer (the three Rebalancer bronze feeds per date), and FWD-1 is also read on the reader's page. The shipped gold catch-up re-values holdings dates at gold and never covers a date with no assignment partition. It is downstream and is not an ingest repair. |
| C-ONE-PIPELINE: recovery is a step of the existing pipeline | law (no shadow pipeline) | Any same-day re-attempt is a step of the existing runner and its existing chains: the runner's `on_success` destination and the session chain. It is never a second schedule, output path or comparator. Build ladder rung 2. |
| C-FIX-NOT-NOTIFY | law (moratorium; GLOBALALARM D10 hold) | No outcome here becomes an alarm, alert, notification, monitor or freshness checker. FWD-2 is the run's own result, read on demand. |
| C-COMPLETE: what "landed" means | this project | A date is landed only when all three feeds are present for it (`rebalancer_models`, `rebalancer_accounts`, `rebalancer_model_detail`). The completeness read is per feed. |
| C-IDEMPOTENT: a second attempt never doubles a day | this project | The runner's guard against re-landing a complete date is proven to work before any second attempt exists. It read as dead on 2026-08-31 (missing read on the complete stamp; 2026-08-31 brief section 6.1), and its state today is unread. |
| C-SESSION: the login chain is relied on, not owned | `0.6.2_AE_PartnerETL` (`cot-bd-session-trigger`, `cot-pipeline/schedule-et.tf`) | This project reads the session chain's success and may hang a destination off it. It does not change the session's mint time. Any fire-time move (FWD-5) re-derives the 13:30Z floor margin first, because the mint time is an Andrew-direct placement. |
| C-VENDOR | law (CLAUDE.md vendor rule) | Every vendor call a repair or re-attempt makes sits under Andrew's word (ACTS 1 and 2). No exercise runs on availability. |
| C-BOUNDARY-COTBKF | ruled here at L2 | ADVI_COTBKF is the Commonwealth custodian delivery of Cottonwood's 10-year history: a different source, store and consumer. MDPF_HEALGAP is the daily Black Diamond Rebalancer ingest. They share no write surface. A future join of the two is ADVI_COTBKF's. |
| C-NAMES | law (rule 30) | Every new address and name is `lib/opal_naming.py` output, printed in the order that writes it. A builder refusal is a registry row, never a hand-typed name. |

## 1. The arc

**Start.** A vendor login lapses before the morning pull; the pull fails; the login heals hours later; nothing re-runs, and the day
is a permanent hole that every instrument reads as healthy. One feed went missing for eleven consecutive days while its two siblings
landed, and the run called that success. The settings promise a six-hour tolerance the system cannot deliver.
**End.** A morning failure heals the same day with nobody acting; a run reports which feed is missing; an existing hole closes with
one named repair; the settings tell the truth; the pull runs after the login it needs; and every other pull of the same shape has an
answer.

## 2. THREAD -- FWD-1, round 1 (hop by hop)

0. **Read before building (no vendor call):** why `rebalancer_model_detail` stopped from 2026-09-01 to 2026-09-10 while its siblings
   landed. Also, the state of the idempotency guard today (C-IDEMPOTENT). Both are reads that change the build, so round 1 opens with
   them.
1. The morning runner fails on a lapsed login. In the exercise this is deliberate; the mechanism to induce it is the issuer's to
   decompose, and it must not touch the production login.
2. The session chain mints a fresh login (its existing daily fire).
3. The re-attempt hangs off that success (C-ONE-PIPELINE). If the date is incomplete (C-COMPLETE), the runner re-runs for that date
   only. If complete, the guard skips (C-IDEMPOTENT).
4. All three feeds land for the date; the existing `on_success` chain takes them to silver, then gold.
5. The reader's page shows that day's Cottonwood figures.

The exercise of hops 1-5 waits on ACT 1 only. Hop 0 and the build do not.

## 3. ENRICHMENT BACKLOG (ordered)

1. FWD-2, the per-feed result on every run (it is also hop 3's completeness read, so it may land in round 1).
2. FWD-3, the repair of the eleven days, after hop 0's read and ACT 2.
3. FWD-4, the settings made true.
4. FWD-5, the fire-time move, after the floor margin is re-derived.
5. FWD-6, the class answer (49F first).

## 4. WORKSTREAMS AND OWNERS

One workstream on dell1, issuer `2.0.0_SA_COO~G1`. The session chain is `0.6.2_AE_PartnerETL`'s (relied on). Terraform edits apply
through `safe-apply` from a box whose grant covers them. Dell create grants are BUILT, NOT APPLIED (NFRA_CTLPLN brief section 2), and
IAM writes are the laptop's by write-in.

## 5. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | verb | bound |
|---|---|---|---|---|---|
| S01 | FWD-1 | the runner's same-day re-attempt, keyed on the session chain's success | held (brief IV.1, IV.2) | wire | C-ONE-PIPELINE; C-IDEMPOTENT first |
| S02 | FWD-1 | the runner's guard against re-landing a complete date | held (2026-08-31 brief 6.1; unread today) | repair | C-IDEMPOTENT |
| S03 | FWD-2 | the per-feed completeness in the run's own result | measured (brief VI.4) | build | C-COMPLETE; C-FIX-NOT-NOTIFY |
| S04 | FWD-3 | one repair act naming its dates and feeds before it fetches | held | build | C-VENDOR; after hop 0 |
| S05 | FWD-4 | `cot_rebalancer_runner.tf` retry and age settings | measured (brief IV.4) | amend | true to the AWS async cap |
| S06 | FWD-5 | the runner's schedule against `cot_bd_session_daily_et` | measured (brief IV.2) | amend | C-SESSION; floor margin re-derived |
| S07 | FWD-6 | the census of session-dependent scheduled ingests | held | read | each answered |
| S08 | hop 0 | why model_detail stopped 2026-09-01..09-10 | held (brief VII.1) | read | no vendor call |

## 6. BRIEF COVERAGE

| Brief heading | Carried | Consuming sections |
|---|---|---|
| PART 0, blind constraint | the bend is disclosed; no outcome cut from leaked fields | ENDPOINT SOURCE lines |
| PART I, thread and O1-O6 | the thread; six outcomes | ENDPOINT; section 2 |
| PART II, boundary | owns ingest recovery; relies on session chain, `on_success`, gold catch-up; ADVI_COTBKF settled | C-LAYERS, C-SESSION, C-BOUNDARY-COTBKF |
| PART III, bar | nobody acts; no false success; config truth; repair once | FWD-1, FWD-2, FWD-4, FWD-3 |
| PART IV, substrate | `on_success`, session schedule, gold catch-up, unreachable tolerance, prior art | S01, S05, S06, C-ONE-PIPELINE, C-LAYERS |
| PART V, must be true | guard first; per-feed completeness; floor margin; vendor word; fix not notify | C-IDEMPOTENT, C-COMPLETE, C-SESSION, C-VENDOR, C-FIX-NOT-NOTIFY |
| PART VI, status | eleven-day model_detail hole; two-of-three landings | FWD-2, FWD-3, ACT 2 |
| PART VII, not claimed | cause of the eleven days; served effect; guard state; 49F; COTBKF | hop 0, S02, FWD-6, C-BOUNDARY-COTBKF |

## Provenance

GROUNDED ON: the brief @a8c67a424e (12,346 bytes), read whole; `org/projects/ADVI_COTBKF.json` title (boundary); the SECHIST PRD
for house shape. NOT READ: this project's earlier decomposition and task orders (deliberately: Phase 0 reads the brief only); the
served Cottonwood series; the runner's guard code today.

## ADDENDUM v0.2 (2026-10-08 ~14:5xZ, `1.0.0_SA_CTO~DELL1`, L10 of round 1) -- FWD-3 amended in place, id unchanged

Round 1 found, in row S2 (graduated, REMEDIATION_v1), that the runner's Black Diamond calls carry no as-of date: the Rebalancer
endpoints serve CURRENT state only. So the only "repair" of the eleven days 2026-08-31..09-10 would put October compositions under
September dates, which is fabricated history. Andrew declined that refill (Andrew-direct 2026-10-07 ~13:58Z, "ACT 2 rec (no refill)
approved", @e5fb41862f).

**What FWD-3 no longer promises:** that those eleven days hold their true model compositions. No source Opal reads serves them.
**What it still promises:** the one-act, named-in-advance repair, exercised on a real hole whose source can still serve the day.
It also now promises that a day which cannot be truthfully filled reads as missing, with its reason. FWD-3 is AMENDED (the outcome
was wrong about what is recoverable), not retired: the capability stands. This is an ENDPOINT change, so the ratified-text half
re-opens for `3.0.0_SA_CVO`'s signature. No other outcome moves.

**v0.2 wording note (~14:5xZ, CVO review @e0ed8e415a):** "a hole whose source can still serve that day" can only be a same-day
hole, so the DONE WHEN says so and admits an induced hole, as FWD-1's was. Wording only: the promise is unchanged, and the notifier
does not wait on a re-sign of wording (CLAUDE.md rule 27, proportionate sign-off).

## ADDENDUM v0.3 (2026-10-11 ~03:0xZ, `1.0.0_SA_CTO~DELL1`, L10 of round 2) -- FWD-6 amended in place, id unchanged

Round 2's census (graded NOT REALIZED by `3.0.0_SA_CVO`, ADJUDICATION_v2) found pulls whose login no machine renews: the two
`canonical-schwab-si2` daily pulls, the third Schwab SDD master `schwab-canonical-si2-08403355-pull-daily`, and
`astn-wsjft-3am-run`. The SI2 session and the FT cookie are re-established by a person (CTO batch @6c538a0bfd sections E and K).
For those pulls neither "recovers the same way" nor "not exposed" is true. As written, FWD-6 could only be met by a false answer
or by building an automated vendor login, which is a separate scope.

**What changes.** FWD-6 admits a third, honest answer: "exposed, and only a person can renew the login". It must name the
person's act and where that act is listed when owed (the open-calls list). The grade still shows the exposure; nothing is
hidden. The list must also be counted against a fresh count of every scheduled pull, because round 2's 162 was stale against
a live 164 (row D1-C-S15).
**What does not change.** A pull whose login IS renewed by a machine must still recover or be shown not exposed. This is an
ENDPOINT change, so the ratified-text half re-opens for `3.0.0_SA_CVO`. No other outcome moves.
