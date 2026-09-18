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

## 2. Two decisions that are Andrew's

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
7. **The two cards**, as Andrew answers them.

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
