# BRIEF -- the Exec Management panel, from current to desired

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~17:0xZ, at Andrew's ask: *"This is good, write the brief and bring it to the
CTO~Z"*, after the panel's pipeline drawing and current/gap/desired table. **To** `1.0.0_SA_CTO~Z`, who owns
AMGT_RESAPP from L2 to L4 and keeps the panel-briefs intake
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md`). **Status:** a BRIEF. It
creates no gate, cuts no order, and spends no decision that is Andrew's.

**Andrew's standing direction applies to every item here** (record
`ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md`): *no fleet run or re-run until the process is
validated end to end*, and *the product is the process that instantiates the full security-analysis backend for a NEW
security*. So every gap below is also stated as its instantiation question: **what makes this stage run for a new
security?** No item asks for a run.

**Code vintage for every citation:** HEAD at write time, the cited files unchanged since `@e2d89be7da`.

---

## 0. The denominator

33 keyed names, from `crosswalk/v1/2026-09-15.json` records with resolution MEASURED. Every figure below was read with
the adapter's own `scoped_amgt.read_management` over those 33 at ~16:4xZ, and re-read at ~17:0xZ with no change.

---

## 1. Where the panel stands, measured 2026-09-18

**The headline "management 12 of 33 SERVED" is a STATUS count, and it overstates the panel the same way Trending x
Chatter did on the Lead Panel:** a status reads complete while the content under it is empty.

| what the page shows | measured over 33 |
|---|---|
| management object SERVED | 12 |
| ... of which carry ANY officer | **7** (BA, COST, HD, SAP, BABA, NU, VLO) -- 62 officers |
| ... of which are an UNRESOLVED-SOURCE roster with **0 officers** | **5** (ASML, HAL, INTU, KMB, PBR -- all written by rk-22 at as_of 18 Sep) |
| officers with a role start, so a tenure | 40 of 62 -- BABA, NU and VLO carry none |
| names with officers, tenure AND a pool comparison | **4** (BA, COST, HD, SAP) |
| officers with a profile link (Lusha) | 11 of 62 |
| CEO public profile CONFIRMED | 1 of 12 (SAP) |

**rk-22 moved management by 2 real rosters (NU, VLO), not 7.** Five of its seven new objects are empty rosters that the
adapter serves as SERVED.

### 1.1 Why each empty or thin roster is empty -- read from each object's own `roster_reason`

| name(s) | reason | stage it belongs to |
|---|---|---|
| ASML, PBR | "the persisted 20-F carries an EMPTY officer section (Item 6 ...): the item was not cut from the primary document" | FILINGS -- the officer section is cut in `lib/research/filings/fetch.py` by item heading (`:116` 10-K Item 10, `:147` 20-F Item 6; persisted at `:440-447`) |
| HAL, INTU, KMB | "no declared shape read this section" (20 / 4 / 194 usable lines, 0 candidates) | ROSTER -- `roster.py` knows three layouts: narrative-entry, table-age, table-year |
| BABA, NU, VLO | officers found, no role start | ROSTER -- VLO's role reads "Chairman of the Board, Chief Executive Officer and President 60": the age leaked into the role, a mis-split row |

### 1.2 Four more gaps, found in this read

1. **The CEO profile line gives the wrong reason on 7 of 12.** `ceo_profile_reading` (`scoped_amgt.py:2285-2296`)
   maps any object whose basis "names no url count" to NOT_CONFIRMED_INSTRUMENT_CANNOT_SAY, and the tab
   (`ExecManagementTab.tsx:84-87`) then tells the reader *"the links it returned do not expose a readable host"*.
   **For 7 of the 12 no search ran at all** -- no declared IR domain (NU, VLO), or no CEO to search because the roster
   is empty (the five). Each of those objects carries `absence_class: NOTHING_FOUND`, which the reader ignores. The
   split is 1 CONFIRMED, 4 genuinely searched with unreadable redirect links, and 7 never searched.
2. **An empty roster is shown as a served table.** The tab renders "0 officer(s) from Item 6 ..." over an empty
   table. The object's own `roster_status` and `roster_reason` are carried on the payload and never rendered
   (`ExecManagementTab.tsx:95-137`).
3. **The pool comparison fragments by run.** `compute_pool`'s docstring (`enrich.py:582-588`) promises the average over
   EVERY name with a roster; the code keeps only objects whose file name is exactly that `as_of` (`:594`). So each run
   pools only itself: `_pool/2026-09-15` = 4.08 years over 40 officers of 5 names; `_pool/2026-09-18` = no value, 2
   rosters, 0 officers with a role start. NU and VLO therefore show the pool ABSENT. `names_in_union` is null on the 18
   Sep pool because no 18 Sep universe vintage exists.
4. **The batch has never run, and would do damage if it did.**
   - `OpalResearch-ExecManagement` is DISABLED by design (activation is Andrew's word, `batch.py:9-11`). Its action is
     split at the space in the path (Execute = `C:\Users\Opal`), and its last result is 267011, "has not yet run".
   - `run_batch.cmd` pins `universe/v1/2026-09-15.json`.
   - `persisted_filing_keys` (`batch.py:76-86`) counts `UNRESOLVED-SOURCE` placeholder objects as filings: its census
     reads 188 = 12 real + 176 placeholder-only names. **A run would write ~176 zero-officer rosters, each served as
     SERVED**, and the panel's status count would jump while its content stayed flat.
   - The same census splits S3 keys on `/` (`batch.py:83`), so `BP/_LN_Equity` and `NG/_LN_Equity` are dropped
     silently -- and will stay dropped after the Thesis tier 1 gives both a real 20-F. The batch's own dry run confirms
     both absent from its would-build list.

**Enrichment is a hand list.** Lusha is scoped by company domain, and `domains.json` declares 5 names (the 15 Sep pilot:
BA, BABA, COST, HD, SAP). Every other name is SKIPPED with that reason. BABA was CALLED and matched 0 officers for 2
credits.

---

## 2. Two decisions that are Andrew's -- BOTH ANSWERED YES ~17:1xZ, see section 8

Kept as first written so the record shows what was asked.

| the question | why it is his | this seat's recommendation |
|---|---|---|
| **Should an officer list from Bloomberg fill the table when the filing gives none?** | The contract C-EXEC-MANAGEMENT makes the FILING the roster authority (`roster.py:1-15`); a second source changes ratified text. Bloomberg's `COMPANY_EXEC_OFFICERS` is populated for all 21 keyed names without a filing, but it carries NAME and TITLE ONLY -- no role start -- measured on HSBC, KDDI and Roche. Lusha was rejected as a roster for exactly that gap. | **Yes, as a labelled fallback, and only for the table:** "officers per Bloomberg, no filing available", with tenure and the pool comparison left ABSENT with that reason. It turns 21 blank panels into named executives without pretending to a tenure it does not have. It is still a contract change the CTO writes and the CVO signs. |
| **Should officer profile links (Lusha, 2 credits a name) be part of instantiating a new security?** | Every Lusha call is a billed vendor call and needs his per-use word; today it runs only for 5 hand-listed names and matched 11 of 62 officers. | **Decide after the three-name validation reports**, which exercises everything except Lusha. If it stays in, its company domain should come from the site the filings battery VERIFIED (Thesis brief s.8.2 step 4), never from the hand list or raw from Bloomberg's web address, which points at a subsidiary or branch for 3 of 22 names. |

---

## 3. What makes this stage run for a new security -- today and desired

| step | today, for a new security | desired |
|---|---|---|
| 1. a real filing | only if the filings stage produced one (12 of 33 today) | the Thesis battery (s.8.2): SEC, ESEF, company site, regulator, then translation |
| 2. the officer section cut | automatic inside `fetch.py`, for 10-K and 20-F only; 2 of 12 cut empty | cut for every document family the battery can return, and a cut that comes back empty is a failed cut with its reason, not an empty success |
| 3. the roster | `roster.py`, three layouts | layouts per document family; role start parsed wherever the filing carries it |
| 4. fallback roster | none | Bloomberg names and titles, labelled, if Andrew says yes |
| 5. enrichment | only if a hand-typed domain exists and someone runs the batch with keys | the verified company domain, and only if Andrew keeps Lusha |
| 6. CEO profile | the same | the same domain; four honest states (below) |
| 7. the pool | recomputed only over the same run's objects | recomputed over every current roster whenever any roster lands |
| 8. the trigger | **none** -- every object so far came from a hand run (pilot 15 Sep, rk-22 18 Sep) | the roster builds when the security's filing lands, as a step of instantiation |

---

## 4. The build, in dependency order

All of this is round-14 material, cut by `2.0.0_SA_COO~Z` after round 13's slug and the CTO's round-13 analysis
(LD-0521). **No item includes a fleet run** -- each is proven on the three validation names or on a dry run.

1. **Make the panel honest before making it bigger** -- the cheapest and most important item.
   - CEO line: `ceo_profile_reading` honors the object's own `absence_class`, and the tab prints four states --
     CONFIRMED; NOT SEARCHED (with the reason: no domain, or no CEO); SEARCHED, NOTHING FOUND; SEARCHED, LINKS
     UNREADABLE.
   - Empty roster: the tab renders `roster_status` and `roster_reason` instead of an empty table.
   - A panel status that means content: an object with 0 officers is not counted SERVED by any census.
   **WARN: the first two change what the adapter and page serve, so they move served output and need a CTO+COO
   never-widen pair naming the blast radius** -- every one of the 12 served objects renders differently afterwards.
2. **Fix the census before the batch can ever run.** `persisted_filing_keys` counts only real filings (never an
   `UNRESOLVED-SOURCE` placeholder) and cuts each key between the known prefix and the accession, never by splitting on
   `/`. Prove it with the batch's own `--dry-run`: would-build equals the real-filing names, BP and NG present once they
   have filings.
3. **Make the task launchable and unpinned** -- the same two fixes as the Thesis task (quoted launcher path read back
   with `Get-ScheduledTask`; the newest universe vintage, not a typed date). The task stays DISABLED.
4. **One pool.** `compute_pool` reads the NEWEST object per name across dates, as its own docstring says, and runs
   whenever any roster lands. Its denominator already prints; it becomes true.
5. **Cut the officer section for every filing.** Find why ASML's and PBR's Item 6 came back empty -- INFERRED, not
   measured: a 20-F's directors section can sit in an exhibit or be incorporated by reference from the annual report
   -- and make an empty cut a failed cut with its reason.
6. **Widen the roster.** Layouts for HAL, INTU and KMB's sections; role start where BABA, NU and VLO's filings carry it;
   the VLO age-in-role mis-split. Then one layout per new document family from the Thesis battery (ESEF, company-site
   annual report, translated original). The translation design (Thesis brief s.8.4) applies: names in their original
   script are kept, and matched to English only on an exact rendering.
7. ~~**The two cards**, as Andrew answers them.~~ **BOTH YES (section 8):** 7a, the labelled Bloomberg fallback roster
   (a contract change first); 7b, Lusha as a step of instantiation, keyed on the verified company domain.

---

## 5. Done means measured, not merged

| component | closed when |
|---|---|
| Honest CEO line | over the served names, every NOT SEARCHED object reads NOT SEARCHED with its reason; zero objects read "links returned" without a url count |
| Honest empty roster | every 0-officer object shows its reason on the page, and the served count equals the names with at least one officer |
| Census | the batch's dry run lists exactly the real-filing names, slash-bearing keys by name |
| Pool | one pool object whose `names_with_roster` equals the count of RESOLVED rosters across all dates |
| Coverage | names with officers, N of 33, and every name without officers carrying a stated reason |
| Instantiation | on each validation name, the roster built from its filing with no hand step, or the exact step that stopped it |

---

## 6. Traps named in advance

- **SERVED is a status, not content. Print officers beside every served count.** The 12 contained 5 empty rosters, and
  the round-13 figure "5 -> 12" carried them as coverage.
- **Do not run the batch to "fill" the panel.** As it stands it writes ~176 empty rosters that read as SERVED -- and
  Andrew has ruled out fleet runs until the process is validated.
- **Do not split an S3 key on `/`.** It dropped BP and NG here, as it inflated a count to 34 earlier today.
- **Do not take a company domain from Bloomberg's web address unchecked.** It is a subsidiary or branch site for HSBC,
  ICICI Bank and SSE.
- **Do not call Lusha or Bright Data without Andrew's per-use word.** Both are billed vendors.
- **Item 1 moves served output.** A never-widen pair first, and it names what every served name will render.
- **No monitor or freshness checker** comes out of this brief.

---

## 7. What this brief does not ask for

No seat is re-tasked, no scope is widened, no task is enabled, no run is made and neither card is answered. The only
execution behind it is read-only: the adapter's own reads and the management batch's `--dry-run`, which makes no
vendor call and writes nothing. The three-name instantiation validation (an Opus subagent of this seat, authorized
~16:5xZ) is still running and will report into this brief and the Thesis brief when it lands.

---

## 8. UPDATE 1, 2026-09-18 ~17:1xZ -- both cards YES

Andrew-direct, recorded verbatim in `ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md`: *"1.) Yes. 2.) Yes they
should."*

### 8.1 Card 1 -- a Bloomberg officer list fills the table when the filing gives none

**What it is:** when the filing stage yields no RESOLVED roster, the officer table is filled from Bloomberg's
`COMPANY_EXEC_OFFICERS` (name and title), labelled on the page as Bloomberg's, with role start, tenure and the pool
comparison ABSENT and the reason stated ("Bloomberg carries no role start"). Today that would put named executives on
all 21 keyed names without a filing (measured populated for all 21), and it is the only route to a roster for any new
security whose filing the battery cannot yet reach.

**What it needs, in order -- all for `1.0.0_SA_CTO~Z`'s L4:**
1. **A contract change first.** C-EXEC-MANAGEMENT makes the filing the roster authority (`roster.py:1-15`). The
   amendment adds a second, LOWER source, and it is ratified text, so the CVO signs that half.
2. **The roster object carries its source,** e.g. `roster_source: FILING | BLOOMBERG_FALLBACK`, per "a value must carry
   its claim". The adapter serves it, and the tab labels every Bloomberg row.
3. **The filing's failure travels WITH the fallback.** When a filing exists but its roster failed (today ASML, PBR,
   HAL, INTU, KMB), the object keeps the filing roster's `roster_reason` beside the Bloomberg officers. **Otherwise the
   fallback hides the parser defects that section 4 items 5-6 exist to fix,** and a census would read "covered" where
   the filing path is broken.
4. **The filing wins when it arrives.** A RESOLVED filing roster supersedes the fallback on the next build.
5. **The pull.** `COMPANY_EXEC_OFFICERS` is one more field on an existing Bloomberg reference pull, beside `CIE_DES` /
   `CIE_DES_BULK` for the description (Lead Panel brief 11.3). Adding a field is not a cadence change. Parsing: each
   entry reads `"<name>,  <title>"` (two spaces), with nicknames and honorifics inside the name (`Manveen Kaur "Pam"`,
   `Dr Thomas Schinecker`), kept verbatim.
6. **The count stays honest.** Section 5's "served means at least one officer" applies to both sources, and every
   census prints FILING and BLOOMBERG_FALLBACK separately.

### 8.2 Card 2 -- Lusha profile links are a step of instantiation

**What it is:** every new security's instantiation includes the Lusha step: one prospecting call by company domain,
bounded at 2 credits a name by `enrich.py`'s own `CREDIT_BOUND_PER_NAME`, attaching profile links to officers already on
the roster.

**What it needs:**
1. **The domain comes from the instantiation, not a hand list.** It is taken from the company site the filings battery
   verified at step 4 (Thesis brief s.8.2, the entity test), replacing the 5-name `domains.json`. It is **never taken raw
   from Bloomberg's web address**, which points at a subsidiary or branch for HSBC, ICICI Bank and SSE.
2. **A name with no verified domain** records Lusha as NOT ATTEMPTED with that reason, never a guessed domain -- the
   module's existing rule.
3. **Bloomberg-fallback officers are enrichable.** The contract says Lusha attaches to an officer the FILING confirmed;
   with card 1 it attaches to an officer confirmed by the roster's own source, and the label carries which. That wording
   belongs in the same contract amendment as card 1.
4. **Credits are measured, not estimated,** on the validation names before the step runs at any scale: matched officers
   per credit. Today's measured baseline is weak: 11 of 62 officers linked across the pilot, and BABA matched 0 for 2
   credits.

### 8.3 Not covered by either answer -- put back to Andrew

- **The CEO-profile web search** (Bright Data SERP) is the OTHER billed half of enrichment, and card 2 named Lusha only.
  It stays undecided, and section 4 item 1's honesty fix applies to it either way.
- **Whether the running three-name validation should exercise Lusha** (about 6 credits). Its recorded scope excludes
  Lusha and stays that way until he says otherwise.

---

## 9. UPDATE 2, 2026-09-18 ~17:2xZ -- the CEO search: search the name, then an agent pulls and organizes

Andrew-direct, recorded verbatim in the addendum to `ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md`: *"We should
also do that, search the CEO's name with Bright Data SERP, and have an agent go through it and pull/organize the
relevant results."* This answers s.8.3's first question: the CEO search is IN, and it is redesigned. The second
question (whether the running validation exercises Lusha or Bright Data) stays open.

### 9.1 Today versus the new design

| | today (`enrich.py:404-455`) | Andrew's design |
|---|---|---|
| query | ONE query, `site:<declared IR domain> "<CEO name>"`, one page | the CEO's NAME, not scoped to one site |
| who reads the results | a host test: is any url on the IR domain? | an agent reads the results, keeps the relevant ones, pulls them, organizes them |
| output | one url or ABSENT (`ceo_public_profile`) | an organized set of cited results about the CEO |
| measured outcome | 1 of 12 CONFIRMED; 4 searched and unconfirmed; 7 never searched | -- |

### 9.2 What the new step needs -- for `1.0.0_SA_CTO~Z`'s L4

1. **The search primitive must return what an agent can read.** `serp_brightdata` (`data/find/dualbiz/scripts/serp.py:245-286`)
   returns URLS ONLY -- it drops each result's title and snippet from Bright Data's `organic[]` -- and an agent cannot
   judge relevance from a bare link. It must return the full organic record.
2. **A failed search must not read as an empty one.** The same function `break`s silently on a request error (`:267-268`)
   or an unparseable body (`:271-272`) and returns an empty list, which `enrich.py:438` then records as NOTHING_FOUND.
   Measured in source, not in a run. The new step keeps FAILED distinct from EMPTY -- the same rule as the four honest
   CEO states in s.4 item 1.
3. **The unreadable links.** The 4 searches that ran all returned links the module could not place on the IR host
   (2-10 per name). The module's own label calls them opaque redirect wrappers; **this seat did not verify that.** The
   L4 first measures what the zone returns on one query; if the links are wrapped, they are unwrapped before an agent
   sees them.
4. **Right person first.** The query becomes `"<CEO name>" "<company>"`, and the agent's first test is identity: this
   person, at this company, in this role. CEO names collide across companies, and a result about a namesake is the
   management version of the subsidiary-report trap in the Thesis battery.
5. **"Pull and organize" is verified the way Thesis drafting is.** The agent fetches each relevant page, and **every
   fact it organizes carries its url and a quote that re-locates VERBATIM in the fetched page.** A fact with no quote is
   held, never shown. The agent adds nothing from its own knowledge. This is the panel's trust story, carried over from
   the 389-of-389 verbatim check on Thesis.
6. **A proposed organization, for the L4 to settle:** official biography (company site); professional profile (e.g.
   LinkedIn); prior roles and tenure; board and outside roles; interviews and talks; news profiles. Each item keeps its
   url, host, title, category, why the agent kept it, and its verified quotes.
7. **No contact data, ever.** The module's forbidden set (no email, phone or mobile stored at any level, `enrich.py`
   CONTACT_STEMS / CONTACT_KEYS) carries over to everything the agent pulls.
8. **Where it lands.** A `ceo_profile` block replacing `ceo_public_profile` on the management object; the adapter
   serves it verbatim; the tab shows the organized results with links, and when the step did not run, why.
9. **Cost is measured before any scale:** SERP requests plus fetches plus one model call per CEO, on the validation
   names first.
10. **Contract.** It replaces C-EXEC-MANAGEMENT's "ONE targeted SERP query on the company's own IR domain ... capped at
    one page" (`enrich.py:13-15`), in the same amendment as cards 1 and 2.

### 9.3 What it changes in section 4

Item 1's honest CEO states still land first: they fix what the page says about the 12 objects served today. The new
CEO step is added after item 6 as **item 8**: the structured search primitive with FAILED distinct from EMPTY (9.2 items
1-3), then the agent step (items 4-8) proven on the validation names, all behind the contract amendment. It depends on
card 1's roster (a CEO name to search) and on s.8.2's verified domain only for the official-biography category.

---

## 10. UPDATE 3, 2026-09-18 ~19:4xZ -- the CEO step, explored and prototyped

Andrew asked for a subagent to "go explore how this would be properly implemented" (addendum ~18:4xZ). Its design,
measured on Boeing, SAP and Halliburton (10 of 10 authorized SERP requests; $0.56 of a $5 model cap; no Lusha, no
writes), is `CEO_STEP_IMPLEMENTATION_DESIGN_20260918.md` (committed with this update). It changes section 9 in four
places.

1. **CORRECTION -- the "opaque redirect wrapper" label is stale (s.9.2 item 3).** On 18 Sep, 50 of 50 organic links
   across 6 responses were direct URLs, including a byte-for-byte repeat of the 15 Sep Boeing query. Wrappers remain
   only in non-organic blocks, and one un-followed GET to Google resolves one (1 of 1). So the 4 "searched, links
   unreadable" objects reflect the module never resolving its links, not a property of the zone.
2. **The search primitive errs in BOTH directions, measured (s.9.2 items 1-2).** 3 of 9 requests failed on captcha,
   arriving as HTTP 200 with a 0-byte body (the failure shows only in `x-brd-*` headers), and each came back from
   `serp_brightdata` as an empty list, recorded as NOTHING_FOUND. The one genuinely empty search returned 9 URLs,
   because Google rewrote the query (`spelling.original_empty: true`). The design adds `serp_brightdata_records`
   beside the old function (whose two other callers are FIND_DUALBIZ's -- a lane note for the L4) with OK / EMPTY /
   FAILED from the measured shapes, and retries only on captcha or 5xx (2 of 2 retries succeeded).
3. **The role term makes identity work for a common name.** `"Jeff Miller" "Halliburton"` returned 0 of 9 results
   about him (obituaries of people surnamed Halliburton, a foundation, another employee); `"Jeff Miller" Halliburton
   CEO` returned 9 of 9. Identity is three layers: model triage over titles and snippets, a deterministic anchor
   (surname within 500 characters of the company token: 18 of 18 positives pass, 4 of 4 readable negatives fail),
   and a verified identity quote. Untested: a same-name person in the same industry.
4. **Two axes, not one list (s.9.2 item 6).** The category list mixed a SOURCE axis (official bio, professional
   profile, interview, news) with a FACT axis (prior roles, board roles). The design puts `source_kind` on each page
   and `topic` on each fact. "Official bio" is settled from the verified company domain, not by the model, which
   mislabelled 2 of 3 third-party hosts.

**The verbatim rule held:** 101 of 101 recorded facts re-located on their pages, and 163 of 163 one-word mutants of
kept quotes were rejected. **Cost, measured: about $0.14 per CEO in model spend** (about $4.7 for 33). The SERP
unit price is not in any header or estate record, so the account's billing console has to supply it.

**Open, several of them Andrew's:** whether "found but not read" links are shown (recommend yes, labelled, links
never facts); whether LinkedIn pages are fetched (recommend link-only); whether an unlocker may read the 403/429
pages (his cost ruling in `FIND_DUALBIZ_PRD.md:47` says `serp_opal` only); whether residence lines are ever shown;
and the query's name form.

---

## 11. UPDATE 4, 2026-09-18 ~20:4xZ -- the CEO step's four open questions, all answered YES

Andrew-direct, verbatim in the record's ~20:4xZ addendum: *"1.) yes to all on ceo search. Posture we will get to
later."* The four, as put to him, and what each now binds:

| question | ruling |
|---|---|
| Show links the step found but could not read? | **YES**, labelled, listed as links and never as facts -- the `found_not_read[]` block of the design's schema |
| LinkedIn: link-only, never fetched? | **YES.** The step never fetches a LinkedIn page. Lusha already supplies the profile URL for a matched officer |
| An unlocker for pages answering 403 or 429? | **YES, for the CEO step only.** It is a paid per-page read, so the cut states its bound. It supersedes his FIND_DUALBIZ cost ruling (`FIND_DUALBIZ_PRD.md:47`) **for this path alone**; no other AMGT path is widened |
| Show a residence or home-location line? | **YES.** Contact data (email, phone, mobile) stays forbidden at every level |

**What this changes in the design** (`CEO_STEP_IMPLEMENTATION_DESIGN_20260918.md`): its risks 4 and 5 are settled, and
its open items (a), (b), (c) and (e) are closed. The `other` fact topic it proposed dropping comes back only for a
location line, which is labelled as such. Still open there: the query's name form (its s.3.4), and whether the running
validation exercises the step.

**Posture is deferred** by the same word; its brief stays committed and unissued, with its comparable decision open.
