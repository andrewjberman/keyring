# AMGT_HARVST -- ROUND 11 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~22:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26236, READ-acked, subject *"L10 SLUG AMGT_HARVST round 11
@8ed7e78f16"*, citing `surprise-channel/adjudications/ADJUDICATION_v19.md`. First HARVST round under the re-seated
issuer `2.0.0_SA_COO~H` (record @63854377ef) and the returned CVO route (record @5ac559cb6c).

**Round 11 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE SLUG MEASURED

| limb | reading (re-measured by the CVO, not adopted) |
|---|---|
| L7 | 4 of 4 terminal on the LAST `<status>` tag; 1 judgment criterion (`z-1` AC4) |
| L8 | 75 items, `unknown: []`; the 4 open ids are exactly this round's rows. 2 ARMED (`Z-W31-S1`, `Z-W31-S2`), both CARRIED, disarmed by a condition read on BOTH planes: `scoped-amgt-api.tf` names no timeline route (DESIRED) and `get-routes` on `7k3ed8px20` returns 16 AMGT keys, 0 `timeline`, `/thesis` present as the control (APPLIED) |
| Served act | 1 object ADDED (8 rows), 3 prior ETags unchanged; the CVO read `events served: 8` from that key itself |
| L9 | `z-1` AC4 PASSES Andrew's whose-event standard 8 of 8; the Nvidia 06-01 story now sits on Nvidia, not Lenovo |

**The round-9 addendum rule held on its first served rebuild.** Every article in every span is about the event's own
security.

**One correction the slug makes to the record:** `Z-S34` cites the RANGE route at 5.4 s; the packet's own close run
timed it at **19.9 s**. The 29 s gateway ceiling is closer than the disarm record said. Both routes are timed from the
deployed Lambda in round 12 (s.4 cell 1).

---

## 2. THE DECISION THE SLUG HANDS ME -- THE LEAD HEADLINE

**The finding (measured).** The builder picks the lead as the earliest tier-A article, ties by lowest key
(`lib/research/harvest/tests/test_publication_gold_event.py:181`). That names the FIRST story of the day, not the
dominant one: right on 6 of 8 events (one story each), wrong on both Boeing days (08-26: two unrelated stories;
09-08: the lead is the runway overshoot, the plurality is August deliveries).

**Whose call.** `C-HV-EVENT-SPINE` says only *"Each event carries its lead headline and its articles"*; it does not fix
which headline leads. `FWD-6`'s ACCEPT asks for *"Bursts of real coverage about the company ... as marked events with a
headline"*, so a headline that names the minority story fails the outcome's intent. **The lead rule is an
implementation choice under an unchanged contract, so it is mine.**

**RULING.** The lead is the headline of the story that carries the MOST tier-A articles in the event; ties go to the
earliest. The mechanism (how articles are grouped into stories) is the cell's to choose and state, from the silver
fields already carried; no new vendor field. The rebuild moves served output, so it carries the never-widen pair.

**NOT ruled here -- whether a multi-story day is ONE event.** Boeing 08-26 is two unrelated stories that each clear
the working rule. Splitting events by story would amend `C-HV-EVENT-SPINE`'s working rule (the ratified half). I do
not amend it on 2 of 8: the round-12 judgment grades every multi-story event after the lead fix, and Andrew's
frontend walk tonight (record @c027b4726f) will show the timeline to the person the ACCEPT is written for. An
amendment, if needed, comes from that evidence.

---

## 3. FWD GRADES

- **`FWD-6`: NOT REALIZED.** Its `DONE WHEN` is EXERCISED on the timeline for the validation security, and no user can
  reach a timeline route (0 of 16 mounted). The served events pass the whose-event standard 8 of 8, so the data half is
  ready; the route is the gap.
- **`FWD-5`** (the timeline itself) waits on the same mount, and on the portal DEV push of `92a2576254` that Andrew
  pre-authorised on two measured conditions (ruling 3; `0.0.0_AB_MSTR~Z` measures them after the mount lands).
- **Every other FWD** stands where `ROUND_ANALYSIS.round10.md` left it; 0 of 9 REALIZED.

**Rule 27's close condition is not met, so this analysis ends in an enrichment list.**

---

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 12 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **Mount the two timeline routes on the gateway** | `scoped-amgt-api.tf` both route keys + `scoped_amgt_route_table()` 16 -> 18 in ONE commit, the mount test green both ways, a ledgered deploy (NEVER-2 entry), both routes timed from the deployed Lambda against 29 s. WORLD. Unlocks ruling 3's push and `FWD-5`/`FWD-6`'s walk |
| 2 | **The lead names the plurality story** (s.2 ruling) | rebuild under a never-widen pair; the JUDGMENT criterion re-reads EVERY multi-story event (not only Boeing's two) and asks whether the lead names what the burst was about |
| 3 | **`w-5` (bbg diagnostic)** | one bounded run, Andrew's 18:05Z word; scripted producer, ledgered by the runner |
| 4 | **`w-4` (ft/barrons diagnostic, `Z-S31`)** | one bounded run, same word |
| 5 | **`w-2` capture, capped, `--new-only`** | the word's precondition (after the round-11 rebuild) is met |

**Fan-out** from the chains: 1 is independent and WORLD; 2 shares the gold write surface with nothing else this round;
3, 4 and 5 share the vendor ledger and run in sequence under one runner. Cap 8 not pressed.

## 5. WHAT THIS ANALYSIS DOES NOT DO

It does not close the project, does not amend `C-HV-EVENT-SPINE`, and adds no outcome, so it re-opens no L4-R half.
It makes no vendor ask beyond the three uses Andrew already worded.

## Compiler Tools

The CVO's two-plane read of `Z-W31-S1` (DESIRED terraform + APPLIED `get-routes` with `/thesis` as the positive control)
taken as the measurement; `C-HV-EVENT-SPINE` and `FWD-6` read at `prd/AMGT_HARVST_PRD.md:141-147` and `:694-703` to
decide whether the lead rule is contract text (it is not) before ruling on it.
