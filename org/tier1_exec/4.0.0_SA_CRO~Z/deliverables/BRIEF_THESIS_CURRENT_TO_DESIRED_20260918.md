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
   at today's 12 names (~$14 at 24) to re-derive documents it already holds. And the version each analysis carries
   cannot tell stale from current -- it did not move when the output contract did (see build item 2, corrected).
4. **One issuer, two keys.** The 16 Sep universe lists ASML twice (`ASML_NA_Equity` and `ASML_US_Equity`, one CIK
   937966), so the batch on that vintage would analyze the same filing twice (dry run, the batch's own no-call mode:
   13 would-fetch of 250).

And one carried over from the earlier table: **two writers of `drafting/v1/<key>.json`** -- `batch.py:150` and
`analyze.py:1215`. Any sign-off that names what this key holds must read both rules.

---

## 2. Two decisions that are Andrew's -- BOTH ANSWERED ~16:3xZ, see section 8

Kept as first written so the record shows what was asked. His answers: no run until the process is validated end to
end; the last nine are not a sourcing question but a per-security BATTERY, and the process for instantiating a new
security is the priority.

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
   written by the current analyzer. **CORRECTED ~16:5xZ:** this first said an analyzer version was "today absent". **It
   is present and it never moves:** all 12 analyses carry `analyzer_version: opal-filings-analyze/1.0.0` and
   `prompt_version: rj6-two-pass/1`, the ten stale ones included, although rk-19 changed the output contract (read
   12 of 12 from `filings/v1/`; `1.0.0_SA_CTO~Z` caught it on 6, msg 23695). WARN: **So the ORDER is load-bearing:
   FIRST a version that moves whenever the output contract moves (the ten stale analyses then read as out of date),
   THEN the skip rule.** A skip rule built against today's field would skip the ten stale analyses FOREVER and pass
   its own test while doing it. Deduplicate by CIK so ASML is analyzed once and served under both keys.
3. **One writer of `drafting/v1`.** Route the `analyze.py` CLI's pool write through the batch's `run_one`, or retire
   it, so the key has one rule.
4. **Tier 1 -- a second CIK source.** In `filing_identity_for` (`build_universe.py:491`), when the SEC ticker table
   misses, take Bloomberg's `CENTRAL_INDEX_KEY_NUMBER` and put it through the SAME form measurement and name-agreement
   check. Measured today: all six clear the name check (EDGAR entity name matches Bloomberg's NAME). Needs a new
   universe vintage to land. **The newest vintage is 16 Sep, so whether the universe builder runs on a schedule is a
   check for this item, not an assumption.**
5. ~~**Card "May the filings batch run?"**~~ **ANSWERED NOT NOW (section 8):** no fleet run or re-run until the process
   is validated end to end. The stale analyses stay as they are; nothing is surfaced to users.
6. **Tier 2 -- an L4 question for the CTO first**, then a cell. Three parts: an ESEF adapter keyed by LEI; the
   official store where one exists (the FCA's National Storage Mechanism serves the same UK files `filings.xbrl.org`
   mirrors best-effort); and a second section cutter, because `passages.py` cuts by 10-K and 20-F item headings and an
   ESEF management report has no "Item 1A". **Enel's FY2025 report is not in the repository yet** -- the adapter must
   report "newest held is FY2024" rather than serve it as current.
7. ~~**Tier 3** per the second card's answer.~~ **SUPERSEDED (section 8):** the tiers become steps of one battery that
   every security runs, and tier 3 splits into a company-site step and a national-regulator step.

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

---

## 8. UPDATE 1, 2026-09-18 ~16:4xZ -- no re-run yet; filings are a per-security battery; translation is a stage; instantiation is the product

Andrew-direct, recorded verbatim in `ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md`:
*"I dont care about rerunning until the process is completely validated end to end and the product is basically
done. ... for every security, we basically have a battery on how to get its filings: If US 1.) Start with EDGAR, 2.)
Try the BBG resolution, 3.) Try websearch maybe surfaced through an IR page. If International: 1.) I dont know but we
need a plan. The premise behind this is that we will be adding things over time and the more important thing than
establishing a pipeline itself is the process behind full "security analysis" backend instantiation for a new
security."* And, mid-write: *"It is worth considering that a translation functionality will be required in cases like
these and that should be included in the spec/brief you create on Thesis."*

### 8.1 What changes

- **No fleet run and no re-run.** The ten stale analyses stay stale and the chart stays at 1 of 33. That is accepted,
  because nothing is surfaced to users. Build items 1-3 (launch path, pinned universe, re-paying) are still needed
  before the job is ever enabled, but none of them is urgent now.
- **The tiers become steps of ONE battery that every security runs**, new or existing. The question stops being "where
  do these nine come from" and becomes "what does ANY security go through to find its filings".
- **Translation is a stage of the Thesis pipeline**, not an exclusion rule (section 8.4).
- **The plan is judged by one test: can a security not covered today be instantiated end to end, with every step
  explaining itself?** That is also what "validated end to end" means (section 8.5).

### 8.2 The battery -- Andrew's US order, and a proposed international order

Every step runs the SAME acceptance test on what it finds: **(a) right entity** -- the document names the listed
issuer, checked against Bloomberg's legal name and LEI; **(b) current** -- an annual report for a fiscal year ended
within the last 18 months; **(c) known kind** -- a document family the section cutter and the management roster can
parse. **Language is RECORDED, not tested:** a document in any language passes, and a non-English one is routed
through translation (section 8.4). A document that fails (a)-(c) does not stop the battery; it is recorded with its
reason and the next step runs.

| step | route | key it uses | US | international |
|---|---|---|---|---|
| 1 | EDGAR, CIK from the SEC ticker table | ticker | 1 (Andrew) | yes |
| 2 | EDGAR, CIK from Bloomberg (`CENTRAL_INDEX_KEY_NUMBER`) | Bloomberg id | 2 (Andrew) | yes |
| 3 | EU/UK regulated-market repository, ESEF / UKSEF | Bloomberg LEI | -- | EU, EEA, UK |
| 4 | the company's own site, found by web search | Bloomberg name; web address only as a hint | 3 (Andrew) | yes |
| 5 | the national regulator, one adapter per jurisdiction | the jurisdiction's own id | -- | yes |
| 6 | UNRESOLVED-SOURCE, carrying every step's attempt and reason | -- | yes | yes |

**One preference rule:** when the first passing document is not in English, step 4 runs once to look for the issuer's
own English edition of the SAME fiscal year's report. If there is one, it is used and nothing is translated. If not,
the original is used and translated. The English edition wins only because it avoids a transform, never because the
original is worse.

**Why the company site comes BEFORE the national regulator -- measured today.** A company-site annual report surfaced
on the issuer's own domain for **8 of the 9** remaining names (web search under the research word; no document opened
or entity-checked): KDDI (English integrated report 2025, PDF), Hon Hai (English annual-report page), Lenovo (2025/26
annual-report page), Roche (2025 PDF), RWE (2025 online report), SingTel (FY2026 report), Walmex (the official 2025
annual report filed with the Mexican exchange, in English, PDF) and Zurich (2025 PDF, English). **BB Seguridade
surfaced nothing in English on its own domain**, so it is the one name that reaches step 5 today (CVM, Portuguese,
then translation). So step 4 is ONE generic adapter covering 8 of 9, and step 5's per-jurisdiction adapters are built
only when step 4 fails for a name -- one build today instead of seven.

**Measured placement of the 33 keyed names:**

| step | names | how measured |
|---|---|---|
| 1 | 12 | today's served state |
| 2 | 6 | EDGAR submissions read, Boeing control (research note section 3) |
| 3 | 5 current; Enel's newest held report is FY2024, so it fails (b) and falls through | `filings.xbrl.org` index by LEI |
| 4 | 8 surfaced (Enel not yet searched) | web search today; no document opened |
| 5 | 1 (BB Seguridade) | nothing found at step 4 |

Language is not yet measured for the step-3 documents; Hermes (FR), Enel (IT) and KPN (NL) are the candidates for a
non-English original.

### 8.3 Three things the search found that the battery must handle

1. **Bloomberg's web address is a hint, not a key.** It points at a subsidiary or branch site for 3 of 22 names
   (HSBC -> `hsbc.co.uk`; ICICI Bank -> `giftcity.icicibank.com`, a branch site; SSE -> `ssen.co.uk`, its networks
   business), and at a different domain from the one hosting the annual report for Walmex (`walmex.mx`, not
   `walmartmexico.com.mx`) and Lenovo (`investor.lenovo.com`).
2. **The company's own domain serves SUBSIDIARIES' annual reports too.** The same searches returned annual reports for
   Roche Holdings, Inc., RWE Finance Europe B.V., RWE UK's community fund, Zurich Insurance Company Ltd and Zurich
   Life. **Without test (a), step 4 would read the wrong company's report and draft a thesis from it** -- the same
   class as "a CIK is not an annual report".
3. **Not every annual document is the statutory report.** KDDI's English document is an integrated report, not the
   statutory annual securities report, and its officer section may not carry what the management roster needs. The
   battery records the document FAMILY because the cutter and the roster parse by family. The families after this
   battery are 10-K and 20-F (parsed today), ESEF, and company-site annual reports. Whether one heading-based cutter
   can serve the last two is a design question for `1.0.0_SA_CTO~Z`'s L4, so that each new country does not become a
   new parser.

### 8.4 Translation -- a stage, designed so the verbatim guarantee survives it

Today every drafted sentence is checked VERBATIM against its filing (389 of 389 PASS). That check is the panel's trust
story, and a translation step can quietly break it: a sentence "verified" against a translation is verified against
the model's own output, not the filing. So the design has to keep the ORIGINAL as the object of every check.

**Where it sits.** After `passages.py` cuts the original-language document, and before analysis. Two designs are
possible, and they differ in what the check proves:

| design | what is verified | trade-off |
|---|---|---|
| **A. analyze the original; translate the output** (recommended) | every cited span re-locates VERBATIM in the ORIGINAL filing; the English shown beside it is labelled a translation | the guarantee is unchanged; the analyzer must read non-English text |
| B. translate the passages; analyze the English | spans re-locate in the TRANSLATION only | simpler analyzer, but the check no longer touches the filing -- a mistranslation is invisible to it |

**Contract for any translated text, per "a value must carry its claim":** the original passage and its language travel
with every translated passage and sentence; the translation carries `translated: true`, the source language, the
translator (model and version) and the time; and the page shows it labelled as a translation, never as the filing's
words.

**What translation touches downstream -- each a line in the L4:**
- **Chart points.** Numbers in the original use local formats (`1.234,5` in Europe; million-yen units in a Japanese
  report). A point's span is verified in the original; the value is parsed with the document's locale and unit, and
  the parse is part of the verified record.
- **Management roster.** Officer names may be in the original script (kanji, for example). The roster keeps the
  original, adds the issuer's own English rendering where the English edition gives one, and matches to Bloomberg's
  English names only on an exact rendering, never a guess.
- **Cost.** Translation adds model tokens on documents that can run to hundreds of pages. Translating only the cut
  passages the analyzer reads, not the whole document, bounds it. The cost per name is measured on the validation
  exemplar, not estimated here.
- **Language detection** is recorded by the battery on every document, so the translation stage runs exactly when it
  is needed and a mis-detected language is visible.

### 8.5 The frame: instantiating a new security is the product; filings is one stage of it

Andrew's premise puts the PROCESS ahead of any pipeline. From the two panels walked so far, a security needs at least
these stages. Each should take the battery's shape: ordered attempts, one acceptance test, an explicit terminal state
(SERVED, or UNRESOLVED with its reason), and the route recorded.

| stage | what must exist for the security | known today |
|---|---|---|
| identity | a MEASURED crosswalk record | everything keys on it; NVIDIA shows that data without identity is invisible to every panel |
| universe row | a `universe/v1` row with its filing identity | newest vintage is 16 Sep; what triggers a new one is not yet measured |
| model block | a Bloomberg model block | the trigger for a new name is not yet measured |
| filings | a source object from the battery | section 8.2 |
| translation | translated passages, when the source is not English | section 8.4; not built |
| analysis and drafting | an analysis and a drafted document | batch task disabled by Andrew's word; no run until validated |
| management | a roster from the filing, enriched | follows filings exactly (Lead Panel brief 11.2) |
| posture | a posture object | produced for 33 by a one-off run (rk-22) |
| description | a drafted section, or Bloomberg's `CIE_DES` | Lead Panel brief 11.3 |
| chatter and news | article links for the name | the source covers 3 names (Lead Panel F1) |
| price | a daily price pull | approved to go daily (Lead Panel card A) |
| movement lists | computed from chatter and price | automatic once both inputs exist |

**Every row asks the same open question: when a new security is added, what makes this stage run for it?** The answers
are the instantiation process. Most are not measured yet, and the remaining panels will add rows.

**Proposed sequence:**
1. Finish the panel walk; each panel's brief adds its stages to this table.
2. This seat writes the L1 brief "instantiate a new security" (the CRO's limb), with the filings battery and translation
   as its first fully worked stages.
3. **Validation = instantiate securities not covered today end to end, through every stage:** one US name, one
   international name whose report is in English, and one whose report is not, so translation is exercised. That is the
   "validated end to end" Andrew set as the bar. It costs a handful of model calls on three names, not a fleet re-run.
   Whether those validation runs sit inside his "no re-run" line is his call, and is put to him, not assumed.

**Sources for 8.2-8.3 (web search, 2026-09-18):**
[KDDI integrated report 2025](https://www.kddi.com/extlib/files/english/corporate/ir/ir-library/sustainability-integrated-report/pdf/kddi_sir2025_e_yme7th.pdf);
[Hon Hai annual reports](https://www.foxconn.com/en-us/investor-relations/financial-information/reports?category=annual);
[Lenovo annual and interim reports](https://investor.lenovo.com//en/publications/reports.php);
[Roche annual report 2025](https://assets.roche.com/f/170920/x/fba4184df7/roche-annual-report-2025.pdf);
[Roche Holdings, Inc. annual report 2025](https://assets.roche.com/f/176343/x/1b6314b627/ar25-roche-holdings-inc.pdf);
[RWE annual report 2025](https://www.rwe.com/en/rwe-annual-report-2025/);
[RWE Finance Europe B.V. annual report 2025](https://www.rwe.com/-/media/RWE/documents/05-investor-relations/anleihen-und-rating/annual-report-2025-of-rwe-finance-europe-bv.pdf);
[SingTel annual report FY2026](https://www.singtel.com/about-us/investor-relations/annual-report-fy2026);
[Walmex annual report 2025, MSE, English](https://files.walmex.mx/upload/files/2025/EN/Annual/Walmex_Annual_Report_MSE_2025.pdf);
[Zurich annual report 2025](https://www.zurich.com/-/media-assets/project/zurich/dotcom/investor-relations/docs/financial-reports/2025/annual-report-2025-en.pdf);
[Zurich Life Insurance Company Ltd annual report 2025](https://www.zurich.com/-/media-assets/project/zurich/dotcom/investor-relations/docs/financial-reports/2025/annual-report-2025-zurich-life-insurance-company-ltd.pdf).

---

## 9. UPDATE 2, 2026-09-18 ~18:5xZ -- the three-name validation, and two corrections it makes to this brief

The validation Andrew authorized (~16:5xZ) ran Caterpillar, CSL and Keyence through every stage as it exists. Report:
`INSTANTIATION_VALIDATION_REPORT_20260918.md` @b527b93214. Its section 2 is section 8.5's table MEASURED, with a
"trigger for a new name" column; its section 5 lists 27 defects with file:line.

**Correction 1 -- battery step 1 is not "the SEC ticker table" (s.3, s.8.2).** `build_universe.py:503-508` reads a
33-ticker cache in a worker's deliverables folder (`0.9.0_WK_AMGT_RESAPP~19/sec_ticker_cik_cache.json`) and reports a
miss as absence from the full 10,422-row table. It misses Caterpillar. The live table with the existing name guard
resolves CAT and correctly refuses CSL (Carlisle). Step 1 needs the live table, or a cache rebuilt per name, before any
new US name is added (report D1).

**Correction 2 -- "389 of 389 sentences PASS verbatim" includes vacuous passes (s.1).** `drafting_build.py:85-128`
passes a sentence with no quoted span. On the validation names that was 17 of 39 (CAT) and 16 of 40 (CSL). The figure
is true as stated and weaker than it reads: the count of sentences that carry a quote which re-locates is the one to
print (report D18).

**Confirmed -- translation design A (s.8.4) holds.** On Keyence's Japanese Yuho, 70 of 71 findings carried a verbatim run
inside their one cited passage. The neighbour-passage and mutation controls refused 70 of 70 and 68 of 68, and 0 of 71
translations relocate in the original. Cost: $0.32 a name. It needs Unicode passages (`passages.py:67-79` keeps 6.8% of
Japanese text), citation blocks pre-cut to the passage map, and a character-level verbatim rule.

**Confirmed -- battery step 4 works, and the document layer is the gap.** Step 4 found the right, current report for both
international names; nothing in the estate can cut either. PDF reflow lifts passage coverage from 9.3% and 1.8% to 91.6%
and 92.4%. The 20-F "riskfactors" fallback cut a 70,000-character wrong-object excerpt from CSL's report (D9), so test
(c) must be a real gate.
