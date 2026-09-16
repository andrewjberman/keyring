# RESEARCH BRIEF -- AMGT_RESAPP tab-score data: five points, Andrew's input, what the CTO needs

**Issued by:** `1.0.0_SA_CTO~W`, 2026-09-15 ~19:1xZ. **Issued to:** `4.0.0_SA_CRO~W` (research, then a findings brief back).
**Companion ask:** `4.0.0_SA_CRO~Z` runs the Seeking Alpha authenticated crawl (point 3), by Andrew's name.
**Authority:** Andrew-direct ~19:0xZ, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_190xZ_FIVE_TAB_SCORE_CALLS_ANSWERED_BRIEF_TO_CRO_W_SEEKING_ALPHA_TO_CRO_Z.md`:
*"make a structured brief on all 5 of these points covering my input and what you need, and issue that brief to CRO~W to go do the
research and come back with a brief of their findings."*
**Project:** AMGT_RESAPP. This is research feeding the round-11 L10 addendum (candidates 13-16). It cuts nothing, issues no task order,
and moves nothing served; the round-11 specification stays frozen.

## 0. What to read first (all at HEAD)

| what | where |
|---|---|
| the four score models, verbatim | `ANDREW_DIRECT_20260915_174xZ_...` (per-tab principle), `..._181xZ_...ROBUSTNESS...` (+ follow-on), `..._182xZ_...PEERS...`, `..._183xZ_...DIVERGENCE...` in `org/tier1_exec/1.0.0_SA_CTO/deliverables/` |
| what the CTO already measured | card `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/TAB_SCORE_SOURCING_BLOOMBERG_LUSHA_MEASURED.md` |
| the instruments behind that card, re-runnable | the same folder, `instruments/` (Bloomberg field search, field documentation, reference data with overrides, peer identity grain, the V computation, the Robustness coverage, the consensus probe, the Lusha shape census) |
| the addendum candidates | `org/missions/D5/AMGT/AMGT_RESAPP/ledger/L10_PREREAD.round11.md` s.4, candidates 12-16 |

**Populations used so far.** POOL = the 33 names with a `peers/v1` object in `s3://opal-data-harvest`. ANALYZED FIVE = BA US, COST US,
HD US, SAP GY, BABA US. PEER-COMPLETE = the 10 pool names whose served peer set is non-empty. Name the population on every number.

## 1. The frame for every point: discovery before absence (Andrew's point 4)

Andrew, verbatim: *"Make sure that in any of these cases that you have robust discovery mechanisms, want to make sure we aren't missing
things because of how the data is pulled versus lack of coverage itself. In any case, we will have to reorient around data availability."*

So every input the findings call missing carries ONE of these classes, with the instrument that discriminates it:

| class | meaning | the discriminating evidence |
|---|---|---|
| `NOT_CARRIED` | the source does not hold it | the source's own dictionary or documentation searched under several terms, AND a positive-control name where a sibling field IS served |
| `NOT_REACHED` | the source holds it and our pull did not get it | name the pull defect: wrong mnemonic, missing override, wrong period, wrong security form, reference versus history request, unauthenticated or unpaginated fetch, a route never called |
| `NOT_ENTITLED` | the source refuses us | the refusal text as returned (Bloomberg BAD_FLD can mean a wrong name, a wrong security type or no entitlement -- separate them) |
| `NOT_APPLICABLE` | the input has no meaning for this name | the rule that makes it so (for example EV multiples for a bank) |
| `UNRESOLVED_IDENTITY` | we asked about the wrong security or none | the requested identifier against the name the source returned |

Measured examples of the pull-versus-coverage trap, already found today: Bloomberg `BEST_*` estimates without
`BEST_FPERIOD_OVERRIDE` silently return next QUARTER; `<raw identifier> Equity` resolved 3 of 120 peer members to a different company
with no error; FIND_INSURE's 661 Lusha records carry no job history because every one is the prospecting shape (the reveal step was
deferred), not because Lusha lacks it; the pool's model block lacked Robustness inputs that Bloomberg itself serves for 22 of 33 names.
**A zero is a finding only after its class is named.**

Andrew's second sentence is a direction for the findings: for each score, say what the data actually supports, and propose how the score
reorients around it (a lower frequency, fewer constraints, a different input, a different population), with numbers. Proposals, not
rulings -- the models are Andrew's.

---

## 2. Point 1 -- Lusha: one bounded enrich for executive job history

**Andrew's input:** "Yes" to: *one enrich over the 11 matched officers, requesting no emails or phones, with the reveal flag turned on
for that call.*

**Known:** prospecting matched 11 of 48 filing officers on the analyzed five (rj-8, M-1), title equal to the filing role for 4 of 11, no
dates. The repo client (`data/find/imo/scripts/_util/lusha_client.py`, `contacts_enrich`) is gated by `LUSHA_CONTACT_REVEAL_ENABLED`; its
`reveal` list is optional. Position history (`currentPosition.startDate`, `previousPositions[].startDate/endDate`) appears only in a
hand-built fixture; the FIND_INSURE parsers already read that shape (`silver/parse_linkedin_silver.py`,
`gold/score_linkedin_gold.py:443 parse_tenure_years`).

**The bounds of the authorization (do not widen):**
- ONE enrich request, at most the 11 matched officers. If their Lusha contact ids are not persisted, one prospecting call per analyzed
  company domain to recover them is inside the bound (prospecting is not a reveal).
- BEFORE the call, establish from Lusha's v3 documentation how to request NO emails and NO phones (whether omitting `reveal` reveals a
  default set and charges for it). If the request cannot exclude them, stop and report that instead of calling.
- `LUSHA_CONTACT_REVEAL_ENABLED` set in that one process's environment for that call; never persisted to a profile, a config or a
  Scheduled Task.
- Contact data is NEVER stored: any email, phone or address in the response is dropped in memory before anything is written. What is
  kept: per officer, the job-history STRUCTURE and dates, title, company, and the response's `billing.creditsCharged`.
- Secrets via `comp-secrets get <name> --reveal` only.

**What the CTO needs back:**
1. Per officer (11): did `currentPosition.startDate` come back; did `previousPositions` come back, with dates; is there more than one
   position AT THE SAME COMPANY (the as-a-manager versus in-general split); does the current title match the filing role.
2. The two scoped measures Andrew asked about, for the officers that support them: average time at the company AS A MANAGER, and
   average time at the company IN GENERAL -- each beside Bloomberg's `EXECUTIVE_AVERAGE_TENURE` for the same company and the filing
   join years where the filing states them (BA 6 of 12, HD 6 of 10).
3. Credits charged, and the per-officer cost this implies across a pool of analyzed companies.
4. A verdict on reliability (coverage, date agreement with the filings) and parseability, with the denominator printed.

## 3. Point 2 -- the dispersion behind Divergence: cash flow per share or EPS

**Andrew's input:** *"CFPS or EPS is fine."*

**Known:** Bloomberg carries no FCF estimate spread or count (every `_STDDEV`, `_NUMEST`, `_HI`, `_LO`, `_MEDIAN` variant of
`BEST_ESTIMATE_FCF` and `BEST_CALCULATED_FCF` is INVALID on 33 of 33). It carries `BEST_CPS_STDDEV` (29 of 33) with `BEST_CPS_NUMEST`
(1FY: BA 4, COST 5, HD 5, SAP 10, BABA 8) and `BEST_EPS_STDDEV` (33 of 33) with 26-38 estimates. At `BF` the counts are fractional
blends.

**What the CTO needs back:**
1. Discovery first (s.1): confirm the FCF spread is `NOT_CARRIED` rather than `NOT_REACHED` -- other mnemonics, BEst detail fields,
   broker-level estimate data if entitled, and a positive-control name.
2. Coverage and estimate counts for CFPS and EPS dispersion over the POOL and over the peer-complete names' members, at `1FY` and `2FY`,
   with how many names clear Andrew's `N_est >= 4` guard under each.
3. How to carry the chosen spread into FCF units, with the arithmetic shown on the analyzed five: the relative spread (sd / |mean|)
   applied to |F_cons|, or the per-share sd times diluted shares -- and the currency of each piece (BABA's estimates are CNY against a
   USD listing).
4. A recommendation between CFPS and EPS, with the numbers that decide it.

## 4. Point 3 -- consensus from Seeking Alpha, and the house forecast Divergence needs

**Andrew's input:** *"Ask CRO~Z to explore Seeking Alpha with an authenticated crawl, they should have consensus figures."*

**Routing:** `4.0.0_SA_CRO~Z` runs the authenticated crawl (asked in its own message, same turn). `4.0.0_SA_CRO~W` does not repeat it;
the findings brief cites `4.0.0_SA_CRO~Z`'s result, and if that result has not landed when the other points are ready, this point
reports its state and the findings brief goes out without waiting.

**Known:** the CRO's Seeking Alpha REST path (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py`, session from
`sa_harvest_session.py`) calls symbols, the virtual-analyst report, news and articles. The stored `symbol.json` objects advertise routes
no fetch has called: `/earnings/estimates`, `/earnings/revisions`, `/valuation/metrics`, `/cash-flow-statement`, `/peers/comparison`,
`/growth`, `/profitability`, and `meta.contentCounters.annual_earnings_estimates`. Both scripts read secrets through Secrets Manager
directly, which Andrew's rule replaces with `comp-secrets get <name> --reveal`.

**What the CTO needs back (from the crawl's result, read by `4.0.0_SA_CRO~W`):**
1. For the analyzed five, whether Seeking Alpha serves consensus for FCF, cash flow per share, EPS and revenue, per fiscal year: the
   mean or median, the high and low, the number of analysts, and the revision history -- each field classified per s.1.
2. Whether its figures are independent of Bloomberg's BEst consensus or a relay of the same contributors, as far as the source says.
3. **The question Andrew's answer leaves open, carried as research:** Divergence needs `F_model`, the house model's NTM FCF, with
   drivers seeded at least partly independently of consensus. The pool's model blocks hold only reported history. Report what the
   estate holds toward a forecast (any driver or projection producer, in the repo or the pool), and what Seeking Alpha offers that could
   seed drivers independently (quant or author estimates, revisions). Options with their data, no ruling.

## 5. Point 4 -- discovery for every score, and the percentile basis

**Andrew's input:** the discovery requirement and the reorientation, s.1. The percentile basis question (all three models rank within
sector; Andrew ~17:5xZ set the pool of analyzed companies; 33 names put one to four in a sector) was not ruled.

**What the CTO needs back:**
1. **Re-run the three coverage reads with discovery,** classifying every ABSENT:
   - Robustness over the POOL: x1 14, x2 22, x3 3, x4 3, x5 22, x6 0 names at full history; 3 of 33 rankable. Is x6 (largest customer
     share) truly `NOT_CARRIED` on Bloomberg -- supply-chain bulk fields with revenue percentages, segment data, other mnemonics? Are
     x3/x4 thin because the maturity ladder is annual (`NOT_CARRIED` at quarterly frequency) or because of the request?
   - Peers over the peer-complete members: the 7 identity failures resolved properly, the measure coverage re-read, and why 23 of 33
     pool names carry an EMPTY peer set (the similarity function, the universe, or the identifiers).
   - Mgmt over the POOL: whether any Bloomberg field or bulk field carries per-officer start or join dates (`NOT_CARRIED` versus a field
     not yet found).
2. **The reorientation, per score:** what each model can compute on the data that exists, and the smallest change that makes it
   rankable on the pool (for example annual frequency for x3/x4, n >= 4 while x6 has no source), each with the resulting count of names.
3. **The percentile population:** sector sizes in the analyzed pool today; what a sector percentile means at those sizes; the options
   (rank within the analyzed pool with a minimum sector size and a fall-back to all analyzed names; calibrate sector statistics on a
   broad universe such as the scanner's 2,851 names while ranking within the pool), each with its counts.

## 6. Point 5 -- the Peers cap

**Andrew's input:** *"Yeah sure"* to capping the company's own values at the peer bounds. RULED.

**What the CTO needs back:** V recomputed with each subject measure clamped to its peers' p5/p95 bounds (instrument
`peers_v_feasibility_grain.py`, the clamp added), per name beside the uncapped V (BABA +3.45 today, driven by an inverse-PEG z of
+19.17), and whether any name still has a single measure carrying more than half of its V.

---

## 7. What comes back

**Carrier:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_TAB_SCORE_DATA_FINDINGS_20260915_W.md`, committed, with one message to
`1.0.0_SA_CTO~W` naming the commit.

**Shape:** one section per point (1-5), each with: Andrew's input quoted; what was read (instrument, population, denominator, vintage);
every missing input with its s.1 class and evidence; the recommendation; what stays open. A closing table: per score, the inputs
available, the names computable today, and the proposed reorientation with its count.

## 8. Bounds that hold throughout

- Research and QA reads only: no task order, no deploy, no served output moved; the round-11 specification frozen.
- Harvest collection mechanism and cadence are Andrew's: a bounded crawl or pull for this research is not a recurring job, and nothing
  is scheduled.
- `s3://opal-data-harvest` writes, if any, only under an existing key shape (for example `raw/seekingalpha/{key}/{stamp}/`) and never
  over an existing key; findings and samples otherwise live in the seat's deliverables.
- The ETF plane is read-only for AMGT. Posture is never read by the trade pipeline.
- Secrets through `comp-secrets get <name> --reveal` only, never printed or logged. Lusha contact data never stored. Bloomberg sign-in
  only through the credential wrapper, two-phase.
- Site-Z push hold: commit, never push; `0.0.0_AB_MSTR~Z` carries.
