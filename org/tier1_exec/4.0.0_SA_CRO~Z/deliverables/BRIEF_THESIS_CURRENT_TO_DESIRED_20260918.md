# BRIEF -- the Thesis panel, from current to desired

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~16:1xZ, at Andrew's ask: *"update the thesis brief"*, under his standing word
of the same morning: *"Please update your brief with your updated findings as the gaps are discovered."*
**To** `1.0.0_SA_CTO~Z`, who owns AMGT_RESAPP from L2 to L4. **Status:** a BRIEF. It creates no gate, cuts no order,
and spends no decision that is Andrew's. It is the FIRST Thesis brief: until now the panel had a pipeline drawing, a
current/gap/desired table, and the source research
`THESIS_FOREIGN_FILINGS_CHANNELS_20260918.md` (@`70361878b6`). This brief folds all three into one plan, and adds
four gaps found while writing it (section 1.2).

**Code vintage for every citation below:** `@e2d89be7da` (the newest commit touching any cited file; HEAD
`6366933721`).

---

## 0. The denominator is 33, and NVIDIA is outside it

The population of record is `crosswalk/v1/2026-09-15.json`, `denominators.MEASURED = 33`. This seat's earlier Thesis
figures said "of 34". Diffed today against the crosswalk's MEASURED records' `model_key` (a different instrument from
`1.0.0_SA_CTO~Z`'s, which was a model-store listing, msg 23693): **mine minus the crosswalk = {`NVDA_US_Equity`};
the crosswalk minus mine = {}.** So the 34 was the 33 keyed names plus NVIDIA, which has model blocks and a
union-universe row but no measured identity. Every figure below is over the 33. NVIDIA is named once where it matters
(section 3, tier 1) and counted nowhere. The research note is corrected in place to match.

---

## 1. Where the panel stands, measured 2026-09-18

Read with the adapter's own `read_thesis_bundle` per key, at 15:27Z and again at 16:0xZ: **zero fields changed
between the two reads.**

| stage | measured over 33 | note |
|---|---|---|
| filing identity on the union universe (CIK + form) | **12** (7 10-K, 5 20-F) | 21 carry `filing_identity.source = none` |
| source object in `filings/v1/<key>/` | 33 | 12 real filings; 21 explicit UNRESOLVED-SOURCE objects -- never a silent skip, as designed |
| stored analysis (the model call) | **12** | `claude-opus-5`, $0.45-$0.73 each, $6.90 for all 12 |
| drafted thesis prose, SERVED | **12** | 389 of 389 sentences PASS the verbatim check |
| "big thing" driver chart, SERVED | **1** (Boeing, 3 of 3 verified points) | 32 ABSENT |

**The drafting half is correct wherever it runs.** Every served sentence re-locates verbatim in its filing, and the
chart refuses to show a point it cannot verify (`scoped_amgt.py:2020-2118`: an exact series match, or at least 2
filing points each carrying a verified span). The gaps are all in COVERAGE and RUNNING, not in the method.

### 1.1 Why the chart shows one name, not twelve -- a stale-analysis gap, not a chart gap

| analyses | written | `thesis_driver.points` |
|---|---|---|
| BABA, COST, HAL, HD, INTU, KMB, NU, PBR, SAP, VLO (10) | 17 Sep, 02:15-02:34Z | **the field does not exist** |
| ASML | 17 Sep 15:35Z | 3 points, **none carrying a verified span** |
| BA | 17 Sep 16:02Z | 3 points, 3 verified -> chart SERVED |

The ten were written by the analyzer BEFORE it emitted chart points (the points branch arrived with AMGT-rk-19). No
chart fix helps them; **a re-run on the current analyzer does**, at about $6 for the ten. ASML is the honest case: its
points exist and did not verify, so its chart may stay ABSENT after a re-run, and that is a correct outcome.

### 1.2 Four gaps found while writing this brief (new, not in the earlier table)

1. **The scheduled task cannot launch as defined.** `Get-ScheduledTask OpalResearch-FilingsAnalyzer` reads
   `Execute = C:\Users\Opal` and `Arguments = Bloomberg\Desktop\ajb_workspace\lib\research\filings\run_batch.cmd`.
   The launcher path was split at the space in "Opal Bloomberg". **Enabling the task as it stands runs nothing, and a
   run that never starts writes no pool object -- it reads exactly like "no new filings".** The task is DISABLED by
   design (activation is Andrew's word, `batch.py:9-11`), so nothing has failed yet; it would on the first fire.
2. **The launcher is pinned to one day.** `run_batch.cmd:9` passes `--universe universe/v1/2026-09-15.json`, so every
   weekly run would re-read 15 September forever. A newer vintage (16 Sep, 250 names) already exists.
3. **Every run pays for every name again.** `batch.py:210-213` analyzes every fetchable name on every run, with no skip
   when the filing's accession is unchanged. Annual reports change once a year, so a weekly batch would spend ~$7 a week
   at today's 12 names (~$14 at 24) to re-derive documents it already holds.
4. **One issuer, two keys.** The 16 Sep universe lists ASML twice (`ASML_NA_Equity` and `ASML_US_Equity`, one CIK
   937966), so the batch on that vintage would analyze the same filing twice (dry run, the batch's own no-call mode:
   13 would-fetch of 250).

And one carried over from the earlier table: **two writers of `drafting/v1/<key>.json`** -- `batch.py:150` and
`analyze.py:1215`. Any sign-off that names what this key holds must read both rules.

---

## 2. Two decisions that are Andrew's

| card | the question | what it unblocks | this seat's recommendation |
|---|---|---|---|
| **May the filings batch run?** | Once now (re-run the 11 stale analyses, add the new names), then weekly on the existing disabled task. Each name is one paid model call, ~$0.58 on average. | Charts for the drafted names; every name the tiers below add | YES, after build items 1-2 land, so the first weekly fire is also the last full-price one |
| **Where do the last nine come from?** | Nine names have no free source that works across countries: build nine jurisdiction adapters (several not in English), buy a global filings feed (LSEG Filings API, S&P Capital IQ), or ask the Bloomberg rep whether filings are available through Data License or the BQL entitlement | 33 of 33 | Ask the Bloomberg rep FIRST -- it is the route Andrew called cleaner, and it needs no build. Hold the nine until that answer. **Terminal traffic interception stays off the table** (licence risk to the terminal itself) |

---

## 3. Coverage: the three tiers, over 33

| tier | source | names | reaches | cost |
|---|---|---|---|---|
| today | SEC EDGAR, CIK from the SEC ticker table | 12 | **12 of 33** | -- |
| 1 | SEC EDGAR, CIK from Bloomberg's `CENTRAL_INDEX_KEY_NUMBER` | +6: National Grid, Novartis, BP, HSBC, ICICI Bank, Unilever | **18 of 33** | no new source |
| 2 | ESEF / UKSEF annual reports, `filings.xbrl.org` by Bloomberg's LEI | +6: Enel, Imperial Brands, KPN, Reckitt, Hermes, SSE | **24 of 33** | one adapter + one section cutter |
| 3 | per-jurisdiction channel, or a feed (card above) | 9: KDDI, BB Seguridade, Lenovo, Hon Hai, SingTel, Walmex, RWE, Roche, Zurich | **33 of 33** | the card |

(NVIDIA also files a current 10-K and would join through tier 1, but it is outside the 33 until its identity is
measured.)

**Why tier 1 is small:** the universe builder takes a CIK only from the SEC's ticker-to-CIK table
(`build_universe.py:491-531`), and "NG/", "HSBA" or "ULVR" are not SEC tickers. **The step that MEASURES the form from
the issuer's own EDGAR history already exists** in the same function, as does the refusal of a cross-listing name
collision. Only a second CIK source is missing.

---

## 4. The build, in dependency order

All of this is round-14 material, cut by `2.0.0_SA_COO~Z` after round 13's slug and the CTO's round-13 analysis. Items
1-3 need no card.

1. **Make the task launchable.** Re-register the action with the launcher path quoted, and read it back with
   `Get-ScheduledTask` until `Execute` names the whole `run_batch.cmd` path. The task stays DISABLED. **WARN: site-Z
   tasks run the working tree**, so any edit to `run_batch.cmd` is live the moment the task is enabled; open a
   change-management entry before the edit.
2. **Stop re-paying, and read the newest universe.** The launcher resolves the newest `universe/v1/` vintage instead of
   a typed date. `run_one` skips a name whose `filings/v1/<key>/<accession>.analysis.json` already exists AND was
   written by the current analyzer. That needs an analyzer version stamped on each analysis, which is today absent, and
   is also what makes the ten stale analyses re-run automatically. Deduplicate by CIK so ASML is analyzed once and
   served under both keys.
3. **One writer of `drafting/v1`.** Route the `analyze.py` CLI's pool write through the batch's `run_one`, or retire
   it, so the key has one rule.
4. **Tier 1 -- a second CIK source.** In `filing_identity_for` (`build_universe.py:491`), when the SEC ticker table
   misses, take Bloomberg's `CENTRAL_INDEX_KEY_NUMBER` and put it through the SAME form measurement and name-agreement
   check. Measured today: all six clear the name check (EDGAR entity name matches Bloomberg's NAME). Needs a new
   universe vintage to land. **The newest vintage is 16 Sep, so whether the universe builder runs on a schedule is a
   check for this item, not an assumption.**
5. **Card "May the filings batch run?"** One run -> expected 18 drafted of 33, and a chart for every name whose driver
   clears the bar.
6. **Tier 2 -- an L4 question for the CTO first**, then a cell. Three parts: an ESEF adapter keyed by LEI; the
   official store where one exists (the FCA's National Storage Mechanism serves the same UK files `filings.xbrl.org`
   mirrors best-effort); and a second section cutter, because `passages.py` cuts by 10-K and 20-F item headings and an
   ESEF management report has no "Item 1A". **Enel's FY2025 report is not in the repository yet** -- the adapter must
   report "newest held is FY2024" rather than serve it as current.
7. **Tier 3** per the second card's answer.

**What the tiers also move on the Lead Panel header -- and one correction to this seat's research note.**

- **Management follows Thesis coverage exactly.** Its roster is read from the FILING's officer section (Item 10 of a
  10-K, the senior-management item of a 20-F), by contract C-EXEC-MANAGEMENT (`management/roster.py:1-15`,
  `enrich.py:8`). That is why management is 12 of 33: the same 12. **Tier 1 adds six 20-F rosters with no new
  work, provided each clears one of the roster's three declared shapes; tier 2 needs a roster shape for ESEF reports.**
- **CORRECTION:** the research note (@`70361878b6`, sections 2 and 6.4) said Bloomberg's `COMPANY_EXEC_OFFICERS`
  "closes most of the management gap". **It does not, as a field add.** Using it would make Bloomberg a second roster
  authority, which is a change to C-EXEC-MANAGEMENT's ratified text and so an L4 question for the CTO (card 2 already
  rejected a vendor roster, Lusha, for carrying no tenure). It is populated for all 21 names; whether it carries tenure
  was not measured.
- **Description is a genuine field add.** `CIE_DES_BULK` (Bloomberg's long description) is populated for all 21 keyed
  names without a filing identity (the 12 with one were not measured). Added to the existing Bloomberg pull, it serves
  the description line for the names Thesis cannot reach. It is routed through the Lead Panel brief, section 11.

---

## 5. Done means measured, not merged

| component | closed when |
|---|---|
| Task | `Get-ScheduledTask` shows the whole launcher path; after the card, a real Sunday fire with `LastRunResult` 0 and a pool write |
| Cost discipline | a second run with no new filing makes zero model calls and says so in its own summary line |
| Tier 1 | 18 of 33 carry a filing identity on the newest universe vintage |
| Drafting | N of 33 SERVED at a named read time, every sentence PASS verbatim |
| Chart | every drafted name either SERVED, or ABSENT with the bar-miss reason -- never "no points field" |
| Tier 2 | 24 of 33, with each ESEF name's fiscal year stated on the page |

---

## 6. Traps named in advance

- **Print 33, not 34.** Do not take the model store's listing as the population (it holds NVIDIA), and do not split a
  key at its own slash (`BP/_LN_Equity`, `NG/_LN_Equity`). A wrong-object census that keeps the count is invisible to
  the count (`1.0.0_SA_CTO~Z`, msg 23693).
- **A CIK is not an annual report.** Fifteen names have a CIK and no current annual report (Enel's last 20-F is 2007).
  Tier 1 takes the form from EDGAR history, never from the CIK's existence.
- **Do not enable the task before item 1.** It would fail silently in a way that reads as a quiet week.
- **Do not fill the chart with unverified points.** The adapter refuses them today; keep that refusal.
- **Do not cut round 14 before round 13's slug** (LD-0521).
- **No monitor or freshness checker** comes out of this brief; the task's own run result is the signal.

---

## 7. What this brief does not ask for

No seat is re-tasked, no scope is widened, no task is enabled, no model call is made, and neither card is answered.
The EDGAR and `filings.xbrl.org` reads behind section 3 ran under Andrew's per-use word for research only (record
`ANDREW_DIRECT_20260918_16xxZ_EDGAR_CHECK_AND_WEB_SEARCH_EGRESS.md`). Building tier 1 or tier 2 as a producer is a new
act, and needs its own word where it calls outside Opal.
