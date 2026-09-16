# 4.0.0_SA_CRO~Z -- SUCCESSOR LOG: card 4 discharged in full, four identity layers moved, and the traps a successor must not re-learn -- 2026-09-14 00:00Z to 15:20Z

**archetype:** MIXED
**secondary_archetypes:** MEASURE, BUILD, SCRIBE
**Written for:** the winddown ordered by Andrew-direct this hour, relayed as msg 22814. **Prepare, not
stop** -- no deadline was given and none is invented here.

## 0. STATE AT WRITING, MEASURED NOT RECALLED

```
uncommitted under this seat's paths ...... NONE   (control: 483 tracked files)
git stash list .......................... 0
worktrees held by this seat ............. NONE -- this seat created none all session
commits by this seat still LOCAL ........ NONE -- all carried to origin
origin/SITEZ ............................ 00f5e72d9b (ls-remote at writing)
POSN_ASTTAX L4-R gate ................... ADMITTED, both halves SIGNED at current bytes
open task orders naming this seat ....... 0 of 412  (parsed from <issued_to>, per Rule 22a ROSTER)
OPEN CARDS FOR ANDREW ................... ZERO
```
⛔ **NOTHING IS STRANDED AND NOTHING IS OWED BY THIS SEAT TO ANY SEAT.**

## 1. WHAT WAS DELIVERED -- Andrew-direct card 4, DISCHARGED IN FULL

Card 4 (2026-09-13 ~04:0xZ, *"all recs approved"*) granted the **Google Custom Search key for
investor-relations and blog search, SEARCH ONLY, prove-the-shape-first**. Both halves are done.

| layer | at session start | at winddown | artifact |
|---|---|---|---|
| `bloomberg_ticker` | 34 MEASURED | **83 of 89** | `IDENTITY_DIRECTORY_FALLBACK_INFERRED_20260913_Z.json` |
| `ir_domain` | **0 of 89** | **88 of 89** | `IDENTITY_IR_DOMAIN_PASS_20260913_Z.json` |
| `sa_symbol` | 10 INFERRED | 18 answered, 71 NOT ASKED | `IDENTITY_SA_SYMBOL_DENSITY_PASS_20260913_Z.json` |
| `social_account` | **0 of 89** | **61 of 88**, 263 handles | `IDENTITY_SOCIAL_ACCOUNT_PASS_20260914_Z.json` |
| `blog_roots` | did not exist | **52 of 88** | `IDENTITY_BLOG_ROOTS_PASS_20260913_Z.json` |

⛔ **EVERY VALUE IN EVERY LAYER IS `INFERRED`, NEVER `MEASURED`.** No page was fetched to confirm a
company operates a domain, no social account was visited, no ticker was checked against a security
master, no blog root was opened. **They are REJECTABLE values and a consumer refusing one on the
status field is the rule working.** A successor must not promote any of them without a fetch.

**The narrative is `deliverables/HARVEST_BACKFILL_PLAN_20260911_Z.md`, sections 10 through 24.**
Read s.18 and s.19 before planning any round on this: **identity is NOT what gates the SA backfill --
DENSITY is.** Only 9 of 18 resolved names clear `>=3` mentions in 30 days, and the misses cluster on
foreign-ordinary tickers. No harvest fixes coverage that does not exist.

## 2. THE ROUTES, AND WHICH ONE TO USE -- this is the part that saves a successor hours

```
SA article content ....... DIRECT GET to seekingalpha.com/api/v3/symbols/<SYM>/news
                           clean JSON, 50 records, ISO publishOn, NO LOGIN, NO VENDOR
                           >> Bright Data returns a SMALLER, STRUCTURALLY CORRUPTED payload
                              for this same endpoint. TEST THE DIRECT FETCH FIRST.
IR domains / blogs ....... Google Custom Search, free tier 100/day, resets ~07:00Z
social accounts .......... Bright Data scrape_as_markdown of the company's OWN site
                           NOT SERP -- its search_engine returns hostless Google redirect stubs
Bright Data transport .... https://mcp.brightdata.com/mcp   (NOT /sse -- that endpoint is RETIRED)
                           the device config was repointed; the KEY WAS ALWAYS FINE
```

## 3. WHAT IS OUTSTANDING, AND NONE OF IT NEEDS A HUMAN

- **`sa_symbol`, 71 names NOT ASKED.** Behind a Seeking Alpha 403 that **DECAYS over hours and is
  INTERMITTENT**, not a clean budget. Measured: blocked at 06:08Z, both endpoints open at 08:19Z,
  then 1 name resolved of 6 attempted at 20s spacing. **Do not hammer it** -- a burst re-extends the
  block. Resume with `--exclude-done`, which retries vendor-refused names and carries answered ones.
- **`social_account`, 27 of 88 unresolved.** **Not an absence** -- 20 are client-rendered footers a
  markdown scraper cannot see (Nike's 33 KB and Boeing's 25 KB contain no platform word in any form),
  7 are stable empty payloads. **Closing that gap needs a RENDERED-DOM fetch -- a different
  capability, not more calls of the same kind.**
- **`blog_roots`, 36 of 88 refused on evidence.** Genuine refusals.
- ⚠ **HANDED TO OTHERS, NOT MINE:** 24 task-order files whose `<status>` parses differently by
  position (some flip `complete`/`open`) -- they need READING, no rule resolves them; and
  `akpipe_scorer.py`'s U+2010 (see s.5).

## 4. SCRIPTS, AND HOW TO RESUME EACH

All under `org/tier1_exec/4.0.0_SA_CRO/scripts/`, all gate-clean, all with a `--dry-run` that costs
zero calls and a `--exclude-done` that never re-spends an answered name.
```
ir_domain_bulk_pass.py        --mode ir | --mode blog   (blog needs --held-domains)
sa_symbol_resolve_pass.py     resolves the symbol AND measures density in one sweep
social_account_pass.py        reads each company's own site via the held ir_domain
social_account_shape_probe.py the 2-call shape probe
```
⛔ **EVERY ONE STOPS AFTER 3 CONSECUTIVE VENDOR REFUSALS AND PARTITIONS "NOT ASKED" FROM "REFUSED ON
EVIDENCE".** A successor must preserve both. **A vendor refusal recorded as a finding is the single
most expensive mistake available here** -- it books "Costco has no SA symbol" as a fact.

## 5. THE TRAPS THIS SESSION PAID FOR -- do not re-learn these

1. **A name is not a unique key. Neither is a ticker root.** Three wrong-entity catches, every one
   arriving as a clean success: `investor.kyntrabio.com` for AstraZeneca; **`ROG` returning 50
   immaculate records about ROGERS CORP, not Roche**; `LILA` (Liberty Latin America) for America
   Movil with 48 of 50 titles "confirming" it. **A Bloomberg root IS a unique key** -- it closed nine
   `ir_domain` refusals at zero call cost.
2. **Two tests that share a dependency are one test.** The `LILA` acceptance passed both my tests
   because both read the same weak token `america`. Fix: a SYMMETRIC measure derived from the two
   names, never a longer stopword list from recall.
3. **A success flag constant across every outcome carries no information.** Bright Data returned
   `isError=false` for a transient failure, a dead host, a client-rendered shell, a vendor validation
   ERROR, and real content. **Size inverts too** -- 12,791 bytes of navbar outranks 438 of error.
   **Assert on the FIELD you came for; retry once before recording an absence.**
4. **Store the INPUT to a rule you may have to fix, not just its answer.** The IR branch stored its
   result domains and a later repair replayed offline over 88 records at ZERO call cost with a
   control. The blog branch stored only its output and the identical repair cost 7 calls.
5. **A guard does not travel to its sibling.** SIX instances in one session of a control living in
   one script and absent from its neighbour -- twice in ONE FUNCTION twenty lines apart. **Diff an
   older script against a new one for GUARDS, not for logic.**
6. **A negated-character-class regex cannot span a nested construct.** THREE wrong counts from this
   one mechanism: over nested JSON, over an inline `<status>` mention, and over `open(os.path.join(...))`
   -- that last said 27 of 77 where a balanced-paren scan says 2 of 70.
7. **A citation has THREE layers on THREE clocks:** the POINTER (Rule 22 tests it -- mine was missing
   a vintage for a day), the BYTES (can go stale while the pointer stays right), and the CLAIM the
   citing document wraps around them (**nothing tests this**; mine widened authority into capability).
8. **The harness heredoc unescapes backslashes. I hit this FOUR TIMES in one session** despite it
   being banked, once breaking two working files. **The remedy is to stop putting backslashes in
   heredocs, not to remember harder.**
9. **A staged path alone cannot tell a peer's edit from an in-flight merge's own content.** Check
   `git rev-parse -q --verify MERGE_HEAD` before raising an alarm.
10. **Non-ASCII has TWO independent axes and a cleanup needs both:** RAISING vs MOJIBAKE under cp1252,
    and FUNCTIONAL vs COSMETIC. `akpipe_scorer.py` is raising, and its sole carrier `U+2010` sits
    inside a live regex -- **the minimal "stop it raising" edit is the worst available one**
    (CLAUDE.md s.4 @`7a0ffb5ffa`). **Escape sequences satisfy both constraints; deletion satisfies
    neither.** NOT applied -- handed over.

## 6. WHAT A SUCCESSOR SHOULD NOT DO

- ⛔ **Do not promote any identity value to `MEASURED`** without fetching the page. Card 4 is
  search-only.
- ⛔ **Do not write a local `SEQUENCE.yaml` or a second `sequence-check`** (msg 22480). A second copy
  of a single-source-of-truth document is the worst response to not being able to read the first.
- ⛔ **Do not push a shared branch.** `0.0.0_AB_MSTR~Z` carries. This seat pushed nothing all session.
- ⛔ **The PORTAL FREEZE STANDS.** COMMIT YES / PROMOTE NO. This seat holds **0 commits under
  `portal/`** (control: 147 commits elsewhere, so the author filter works).
- ⛔ **No vendor call without Andrew's per-use word.** Card 4 covers Google CSE for IR and blogs;
  his Bright Data word covers that vendor. **The two never merge.**

## 7. RELATIONSHIPS AND OPEN THREADS WITH OTHER SEATS

- `1.0.0_SA_CTO~Z` -- carries Rule 22a ROSTER, Rule 27's LIMB 6 and s.4's non-ASCII do-not-do. I owe
  it nothing; it has an outstanding **question from me**: whether msg 22655 is mine, which I do not
  recognise. **If a successor is told it authored a byte-count finding about `to-pipeline-gate.py`,
  that is probably not this seat's.**
- `0.0.0_AB_MSTR~Z` -- integrator, carries every commit. Withdrew its silence-as-consent fallback for
  merge windows after four seats answered explicitly; **answer its windows, do not stay silent.**
- `3.0.0_SA_CVO~Z` -- **STOP stands. No respawn, no re-attach, no keystroke.**

**Push state at writing:** origin/SITEZ `00f5e72d9b` (ls-remote). This log is committed, not pushed --
the integrator carries it.
