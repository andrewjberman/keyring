# Session close 16:33-19:30Z -- 0.4.0_DS_ClientPlatform~C (LANE ~C; no ~C folder exists, so this sits in the base seat's log tree) -- ADVI_BDPARITY P1-PROBE seated, our leg built, probe gated at Andrew

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~C` | **Session:** seated 2026-08-29T16:33Z by `2.0.0_SA_COO` (msg 83245) | **Window:** whole session, first log of this seating (no `logs/2026-08-29/` existed) | **Project:** ADVI_BDPARITY, ONE project per Rule 27 | **Cap:** BUILD-only, serve behind the shared arm-(a) sovereign gate.

---

## What this session was

Seated onto three staged TOs cut 2026-08-19 and never worked (`P1-PROBE` -> `P2-CENSUS` -> `P3-EXACT`). COO asked for one thing before any building: a read-back on whether P1-PROBE's acceptance criteria are executable as written, **including if they are not**, because the faces are ten days old and were written for a seat that never existed.

They are executable. Five findings say where the world moved under them. The probe itself is now gated on two things and neither is mine.

---

## Commits (2, both LOCAL ONLY)

| hash | what |
|---|---|
| `8ae7a3ab82` | `build(ADVI_BDPARITY.P1-PROBE)` -- `data/assets/scripts/gold/runners_49f/parity_period_returns.py`, 501 lines, our-side period linker |
| `9368be5bc4` | `measure(ADVI_BDPARITY.P1-PROBE)` -- `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPARITY_P1_COHORT_CANDIDATES_20260829.md`, 154 lines |

**PUSH STATE, MEASURED TWICE.** At 18:5xZ both were LOCAL ONLY (`origin/CLOUD` = `1896be6985`, is-ancestor negative for both, bogus-hash control fatals). **After MSTR's window 53 CLOSE at 20:08Z both are ON ORIGIN** -- `origin/CLOUD` = `bfaa0a6e6e` by own `git ls-remote` at 20:2xZ, is-ancestor positive for both. **The first reading was true when taken and is not true now; a push state is perishable and this log carries both readings with their clocks rather than the one that flatters the record.**

⚠ **A `--since` TRAP HIT AND CORRECTED IN THIS SESSION, worth carrying:** `git log --author=... --since="2026-08-29 16:00"` returned **ZERO** for my own two commits. Commit dates render LOCAL (-0400), so 18:20Z/18:46Z read as 14:20/14:46 and fell outside a UTC-shaped window. **A self-report built on that filter would have said "no commits" and looked complete.** Both were confirmed by direct hash read instead. Per-file detail: see the commit messages, which carry it.

---

## Files modified

See commit messages `8ae7a3ab82`, `9368be5bc4`. Two files, both new; no existing file was edited this session. Memory index compacted separately (outside the repo, under `~/.claude/.../memory/`): 167 -> 134 lines, one duplicate entry retired.

---

## The read-back -- five findings (full text in msg 83558)

1. **BP1-1's verb is wrong.** `opal-assets-bd49f-reporting-pull` has carried `performance -> POST /portfolioreporting/api/performance/performancePeriod` since 2026-07-17, BEFORE the TO was cut, and `lambda_handler` already accepts an explicit account list (`accounts = event.get("accounts") or discover_accounts()`). BP1-1 is a payload + resolution act, not a code build. Applied env measured (not read off the .tf): `DRY_RUN="0"`, LastModified 2026-08-28T18:09:29Z.
2. **The ruled period set is not what the builder asks for.** `body_performance_period` (`lambda_function.py:168-176`) emits `Custom` + two trailing CALENDAR YEARS + `SinceInception`. **CORRECTED by `1.0.0_SA_CTO` 83442 and I am carrying CTO's framing, not my own:** this describes the BUILDER AS BUILT, not the ruled set; trailing-1Y is a `Custom` with computed dates like QTD, so **only YTD is genuinely open**. CTO then upgraded YTD from guess to attested (83445) -- `"YearToDate"` appears in Andrew's own HAR, but on `/advisor/api/v1/Dashboard/data` with a SINGULAR `dateRange`, not the plural array `performancePeriod` needs. Evidence about the vocabulary, not proof about the endpoint.
3. **SinceInception fails silently for a non-roster account.** `run()` passes `inception=acct.get("inception", q_start)`, so the SI range collapses to the window and BD returns a figure labelled SI that is arithmetically QTD. Nothing raises.
4. **The cohort is reachable.** `discover_accounts()` defaults to the TaxSMA roster (5 entries, 3 active, 2 of those 3 with trade_start 2026-08-05), but the tier-1 xref fast-path resolves ANY account with zero egress. `dim_account_xref` `date=2026-08-28`: 6,201 rows, 5,375 resolved 1:1, 826 unresolved, `account_is_open` True = 6,145 (the PRD's own figure, still true).
5. **P2-5's premise moved.** `c00_flow_ledger.py` SCHEMA_VERSION 1.3, `in_kind_unvalued` defaults TRUE by construction; flow_ledger sampled at earliest (2024-07-08), midpoint (2025-08-28) and latest (2026-08-28) reads 1.3 on 3 of 3. **STATED AS A SAMPLE: 3 of 535, not a census.**

**Census denominators measured for BP1-4:** our twr_daily 7,370 accounts | BD-resolvable 5,375 | INTERSECTION 5,309 | ours-only (out-of-oracle) 2,061 | BD-only 66 | plus 826 BD rows with no Schwab key as a SECOND out-of-oracle subclass on BD's side. 5,309 independently equals the xref's own `in_0833_universe` count, derived without using it.

---

## Briefs written (DS role addition)

| brief | path | for | state |
|---|---|---|---|
| Rider-4 cohort candidates | `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPARITY_P1_COHORT_CANDIDATES_20260829.md` | `4.0.0_SA_CRO` (selection is CRO's per rider 4) | committed `9368be5bc4`, LOCAL ONLY |

Headline: **only 38 of 6,185 accounts hold any rate-bearing position** (rb_share>0.20: 8; >0.50: 7), so **the C5 class denominator is 38, not the book**. The pre-named C5 specimen ...2917 is corroborated from a second instrument (CRO~A picked it on largest accrual $22.47K; position composition gives rb_share 0.8982 on $790,249.11 -- no shared input) and resolves to `bd_internal_id 13477111`.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 exercise, "how do I grep the repo" | PASS | forwarder RAN (own banner); PATH 105 of 105 resolve bare |
| `comp-find` | `D2_ADVI_49F_E2E_PRD`, `bd49f`, `c00-FIX`, `D2_ADVI`, `parity` (+ `--band HEAD`, `--files`, `--all`) | PASS | denominators printed each run; located the reporting-pull vehicle and the c00 fix at source |
| `comp-find` | `0.4.0_DS_ClientPlatform~C` (tilde serial, corpus=all, `--band HEAD --all`) | **FAIL (timeout)** | exceeded the 120s tool timeout, backgrounded. See Gap below. |
| `.tools/to-check.py` | `--all --assignee 0.4.0_DS_ClientPlatform~C` | PASS | 3 ACTIVE TOs, 1 project, scanned 2101/2181 -- the known tilde-lane zero did NOT bite this lane |
| `.tools/audit-archive-invoker.py` | A.2 startup | rc=1, 2 findings | both are the KNOWN pair (`UNCOVERED-AUDIT-LOG org/to-pos-override-audit.log`, `STALE-BASELINE`) owned until `rv0057-f001`; NOT re-filed per org/XXX.md |
| `.tools/commit-gate.sh` | on `parity_period_returns.py` | PASS | py_compile + ds-precommit + ruff clean, 1 of 1 checked |
| `.tools/safe-commit.sh` | x2, `-F` msgfile written by the Write tool | PASS | risk-reflex CLEAN (1 file vs 1,910 danger nodes) both times; msg-verify MATCH len=5089 / 3738 |
| `.tools/aws` shim | s3 ls/cp/sync, lambda get-function-configuration | PASS | applied-plane read for DRY_RUN; 37-partition sync in 6.9s |

**What worked:** `comp-find --band HEAD` put the bd49f reporting vehicle in front of me in one call out of 3,771 hits -- the band split is what made a 3,771-hit token usable. The `safe-commit` msg-verify (`MATCH len=`) is the control that makes a `-F` commit message auditable rather than assumed.

**What failed:** `comp-find` on a tilde-suffixed SERIAL over `corpus=all` did not return inside 120s. Every other pattern this session returned in seconds; the distinguishing feature is a high-frequency token that appears in ~1,000+ inbox files.

**Gap found:** a serial is the single most likely thing an agent greps for at session start (to find its own prior work), and it is exactly the shape that is slowest -- serials saturate `org/mcp/inbox/`. Worth a `--band HEAD` default or an inbox-excluding corpus for serial-shaped patterns. **NOT filed as a TO from this seat** (out of lane, and it cost me one call, not the session); recorded here so the next seat that hits it has the mechanism rather than the surprise.

---

## MCP traffic

**20 messages addressed to this lane; 20 ACKed on the READ clock. 5 send CALLS = 11 recipient-rows (10 DELIVERED, 1 QUEUED to the dark CRO seat).**

⛔ **THIS COUNT WAS WRONG IN THE FIRST DRAFT OF THIS LOG AND I MEASURED IT RATHER THAN SHIPPING IT.** I wrote "11 received" from recollection; `get_delivery_state` returned **20 addressed, 16 READ, 4 OFFER-EXHAUSTED** -- and the four were not noise. THREE were messages I had never opened at all (`83429` CTO, `83432` COO, `83435` CVO), each seen only as a Monitor filename and never read. One of them (`83432`) contained the fact that **my "record item" about P1-PROBE's `project=` tag was NOT cosmetic: as it stood I held TWO projects, a live Rule-27 violation created at seating.** A self-report from recollection would have buried that and read as complete. All four are now read and ACKed; the count above is measured.

Significant only:

- IN 83245 `2.0.0_SA_COO` -- the seating; three TOs re-addressed base -> ~C, BUILD-only cap stated.
- OUT 83558-60 -- the read-back (COO/CVO delivered; CRO QUEUED, seat dark).
- OUT 83549-51 -- the r_gross surprise item, OBSERVATION/ARMED.
- IN 83418 `3.0.0_SA_CVO` -- grading bar stated BEFORE the build: P2-1 needs the PERIOD denominator beside the account one, and SI-COMPUTED vs SI-UNAVAILABLE must be separate counted outcomes. **Both are built into `coverage_report()`, not promised.**
- IN 83426 / 83442 / 83445 `1.0.0_SA_CTO` -- the convention/vendor split ruling; the correction to my "2 of 4" framing; the YTD attestation.
- IN 83553 / 83565 / 83570 -- the r_gross item disarmed, arms censused (2 of 18, both EQUALITY-keyed, so a wrong sign FAILS LOUD), CTO retracting its own "silently certifies" class.
- IN 83576 -- COO's card at Andrew for both gates. IN 83581 -- the fix cell seated at `0.4.0_DS_ClientPlatform~N`; this seat EXCLUDED BY NAME ("assigning the finder is how a surprise channel turns into a tax on reporting").
- IN 83499 / 83522 -- MSTR windows 51/52 open+close; commits held and made after the CLOSE.

---

## Blockers

**BLOCKED -- and both blockers are evidence-cited, sovereign, and not mine to open.**

1. **Vendor egress for the live BD pull.** `DRY_RUN=0` is applied (measured), so the machine will not stop it. `1.0.0_SA_CTO` 83426 ruled: editing the builder is in-lane and needs no word; EXERCISING it against BD is a vendor call and needs Andrew's explicit per-use word. Carried to Andrew by `2.0.0_SA_COO` 83576.
2. **Methodology routing.** The SI anchor definition and cumulative-vs-annualised both change what we ask BD for. `4.0.0_SA_CRO` base is DARK (`3.0.0_SA_CVO` 83424; my 83415/83560 both returned QUEUED), and per `ADVI_BDPARITY.json`'s recorded seam a BDPARITY-vs-PERFRP subject collision routes to Andrew only, never adjudicated locally. Also on COO's card.

**NOT blocked, deliberately not started:** BP1-4's census design. Its measurable half is in hand (population denominators above; runtime -- 37 partitions load in 0.2s, so a 535-partition full-history load is seconds, not a risk). Its classification-threshold half needs BOTH CRO's N-bp word and the probe's own delta distributions, and writing it before the probe fires would be inventing the thing the TO says the probe produces.

---

## Current State (for a reader with zero prior context)

**`data/assets/scripts/gold/runners_49f/parity_period_returns.py` @`8ae7a3ab82` is OUR half of the BD parity comparison and it works.** Our chain emits no period returns at all: `twr_daily` (at `s3://opal-data-49financial/gold/advi/canonical/twr_daily/date=YYYY-MM-DD/`, 535 partitions 2024-07-08..2026-08-28) carries per-account DAILY `r_net`/`r_gross`, and `c01_account_performance`'s `cumulative_investment_return` is keyed to FIRST-LINKED-DATE, which is where our chain started carrying the account and **is not an inception**. All four ruled periods (QTD/YTD/1Y/SI) are therefore DERIVED by geometric linking in `link()` / `link_account_period()`.

Every `(account, period)` cell returns one of six MECE outcomes and **an unavailable cell carries no value** -- `COMPUTED`, `UNAVAILABLE-NO-ANCHOR`, `-NO-COVERAGE`, `-WINDOW-NOT-LOADED`, `-NO-OBSERVATIONS`, `-NO-LINKABLE-DAYS`. `coverage_report()` derives both denominators from the cell table itself. Run `python data/assets/scripts/gold/runners_49f/parity_period_returns.py --self-test` -> 18 of 18, rc=0.

⛔ **THE THING A SUCCESSOR MUST NOT UNLEARN: the first REAL-DATA run refuted this module twice, and its fixture had passed both times.** (a) YTD/1Y returned `COMPUTED` with values identical to QTD because the coverage guard compared the window against GOLD's floor while the caller had loaded a 59-day slice. (b) A cell returned `COMPUTED` carrying a null because neutrality was decided by a status list built from ONE partition's `value_counts` -- across 37 partitions the vocabulary is FOUR (`REFUSED-NO-BMV`, 7,315 rows, appears in NO row of 2026-08-28) and the producer's source names a fifth that appears in none of them. Fixes: the loaded date SPINE is a REQUIRED argument with no default, and neutrality is decided by the VALUE. (b) also corrupted a number C1 turns on -- the specimen read days_linked=37/neutral=0 and is now 36/1; the return never moved, the DAY COUNT did, and trading-days-vs-calendar-days IS C1's discriminator. **Honest computed-rate fell 81.25% -> 25.0% when both were fixed. That number moving DOWN is the reason to trust it.**

**Not applied, deliberately, and both are still expressible:** day-count is emitted BOTH ways (`days_linked`, `calendar_days`) and neither is used as a correction -- C1 is the hypothesis under test and re-basing is a P3 comparison-layer act at CTO's gate. Annualisation is not applied (BD's block carries `returnMethod: "Annualized"`); cumulative is emitted with the annualisation inputs carried.

**The BD half is untouched.** Bronze holds exactly ONE performance object -- `reporting_performance/2026-07-17/reporting_performance_22596361_2026-06-30.json` -- so the probe cannot be built from existing bronze and needs a live pull, which is gate 1.

**Open, owned elsewhere:** the `r_gross` sign observation is seated at `0.4.0_DS_ClientPlatform~N` as `ADVI_49F.c02-GROSSLEG`, first act a DETERMINATION with three declared outcomes (code wrong / name wrong / reading mistaken). **A corrected gross leg does not exist anywhere in the 534-date history until a re-emission that cell does not authorize.** My linker carries both legs unchanged and will print which leg any parity cell used, so a ruling re-points the comparison without re-running the harness.

---

## The window-53 deploy, and the consent defect I authored (20:00-20:20Z)

`8ae7a3ab82` was the **first deploy-scope file in six MSTR windows**. MSTR opened window 53 naming it and invited any seat to object. I answered NO HOLD -- correctly: the module has no network surface and cannot touch Andrew's egress gate.

⛔ **THEN I MADE A DECISION THAT HAD NO MECHANISM BEHIND IT.** Citing Rule 13's *"404 = loud skip, first-mints explicit"* (which I took from `0.7.0_AE_CloudOps` 83612 and re-published as my own), I declared: *"as the committing lane I DECLINE to declare the first mint... 0 IS THE EXPECTED COUNT AT YOUR CLOSE, AND IT IS NOT A FINDING."*

**MEASURED AT THE CLOSE: 1 object served.** `s3://opal-data-49financial/_code/parity_period_returns.py`, 28,572 B, ETag == local md5.

**MECHANISM, read at source after the fact:** the membership guard applies only where `layer in tree["shared_repo_homes"]` (`safe_deploy_core.py:1209`). Trees carrying that key: **mdpf ONLY** (`{silver, assets_gold}`); `advi` has none. **So no first-mint gate ever stood in this path, there was no declaration to withhold, and the file deployed correctly.** For a deploy-gated tree with no shared home, **COMMIT IS CONSENT** -- which MSTR's own OPEN had stated plainly and every seat read past.

⛔⛔ **AND THE PART THAT IS MINE ALONE. MSTR's OPEN NAMED THE ACTUAL CONTROL TO ME, IN THE SENTENCE ANNOUNCING MY FILE:** *"carries NO `DEPLOY-SERVE-HELD` sentinel, so the pre-push gate WILL upload it."* **I read past it and answered with a message.** A sentinel in the file is a mechanism; a dispatch declining consent is a description of a preference -- and I spent two dispatches asserting one. My own tripwire (*"if the count comes back 1, that would mean a first mint happened without a lane declaring it"*) fired, **and even its interpretation was wrong**: there was no declaration step to skip.

⭐ **THE FORWARD RULE, stated to be reusable rather than confessional: for a deploy-gated tree with no shared home, the commit IS the deploy. If a build-only module must not reach the served plane, `# DEPLOY-SERVE-HELD` goes IN THE FILE, IN THE SAME COMMIT. No message does this, and asking the integrator to hold is not a substitute for a line the author owns.**

**THE CALL, routed to me by `0.7.0_AE_CloudOps` 83686 and made at 83694: DO NOT REMOVE IT.** Inert on the merits (no S3 client, no import that has one, `chain_49f_entrypoint.py:322` never calls it -- corroborated by two AE seats), served bytes == committed bytes, and deployed correctly under Rule 13. **Deleting a byte-verified inert object from a live prefix to satisfy a preference the governing rule does not grant me is manufacturing friction** -- and `0.7.0_AE_CloudOps~L` measured that the chain SSM doc (`advi-49f-chain-dispatch` v3) syncs `_code/` with `--delete`, so the prefix is a MIRROR and churning it is neither free nor local. **Explicitly refused the tidy-looking middle option:** adding the sentinel while leaving the served copy would freeze a served object against its source and let the two diverge silently -- worse than either clean end-state. Bound stated with the call: "inert" is my analysis of my own module, corroborated but never adversarially tested; `3.0.0_SA_CVO` or `1.0.0_SA_CTO` reopens it on their word and I will not defend the object.

**Two other seats disclosed their own errors in the same window** and the record is better for it: MSTR's pre-push "correction" predicted 0 on `opal-data-inf`/`opal-data-bd` -- **a wrong plane carrying MORE apparent evidence than the thing it replaced**, with a positive control that proved a true absence of a file that was never going there. `0.7.0_AE_CloudOps` settled the destination by RUNNING `file_to_s3_target` instead of reading it. I ran it independently and concurrently, same tuple, plus the negative control that falsified MSTR's stated "`runners_49f` renames to `runners_inf` in S3" -- **they are different trees** (`data/inf/scripts/gold/runners_inf/` -> `opal-data-inf`), and a rename claim left standing is worse than a wrong prefix because the next reader inherits it as a mapping fact.

**Docstring corrected this session** (`serves nothing, publishes nothing` -> where it actually lands, that it is uninvoked, and the served/build-only distinction the old wording conflated). Self-test re-run after the edit: 18 of 18, rc=0; commit gate clean.

---

## Next Steps

⛔ **ITEMS 1 AND 2 WERE ANSWERED AFTER THIS LOG'S WINDOW -- ANDREW-DIRECT 2026-08-29T212315Z, RECORDED VERBATIM @`7a4d8a1888`. DO NOT RE-ASK THEM.** A successor reading the original wording below would re-open settled law, which is the single most damaging thing this record could do. Original text struck, ruling stated:

> **"RECS APPROVED BUT THIS IS A MATTER THAT SHOULD BE HANDLED BY 3.0.0_SA_CVO, NOT CRO"**

1. ~~[Andrew] the vendor-egress word~~ **GRANTED.** "RECS APPROVED" landed on a rec whose text was YES to ONE bounded BD reporting pull. **Scope is exactly the card's and no wider: ruled QTD/YTD/1Y/SI periods, 3-5 probe accounts, NO standing schedule, NO cadence, NO widening of any grant.** A recurring pull is a separate card. ⛔ **AND THE APPROVED REC CARRIED ITS OWN SEQUENCING -- "answer it together with CALL 2, not before it" -- SO THE PULL STAYS UNFIRED until item 3 lands.**
2. ~~[Andrew] which lane holds the methodology~~ **RULED: `3.0.0_SA_CVO`, NOT `4.0.0_SA_CRO`** -- against this seat's own recommendation, which had said CRO. The earlier filing to CRO (msg 83415, QUEUED, never delivered) is **SUPERSEDED; do not re-send or re-point it there.** Scope beyond the two methodology cells (e.g. rider-4 SELECTION, which the faces also place at CRO) was **surfaced and NOT adjudicated by this seat** -- it is `2.0.0_SA_COO`'s with `1.0.0_SA_CTO`.
3. **[`3.0.0_SA_CVO`, once re-seated]** The two cells that now gate the authorized pull: **(i)** which inception anchors SI -- trade-start, BD funding-inception, or our first-linked-date; **(ii)** cumulative or annualised for QTD/YTD. ⚠ **THAT SEAT'S BASE HAD ALREADY ENDED WHEN THE RULING LANDED** (MSTR 83936) and the broadcast returned QUEUED -- **a sovereign-approved item is sitting in a dead seat's inbox, not a queued one.** Flagged to MSTR for the reinstantiation order at 21:3xZ.
4. **[`0.4.0_DS_ClientPlatform~C`, on gates 1+2]** Fire the pull, build the probe table (BP1-2), name mechanisms (BP1-3), then BP1-4's census design, then the BP1-5 proof instance at `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ADVI_BDPARITY.P1-PROBE_PROOF_OF_SPEC.json` (currently ABSENT -- the work is genuinely unstarted).
5. **[`0.4.0_DS_ClientPlatform~N`]** The c02-GROSSLEG determination. Not this seat's; noted so a successor does not re-report it.
