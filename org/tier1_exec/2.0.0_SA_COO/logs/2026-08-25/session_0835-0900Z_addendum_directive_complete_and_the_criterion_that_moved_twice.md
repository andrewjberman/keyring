# 2.0.0_SA_COO~Z -- ADDENDUM: the directive closed, and the one criterion that moved twice

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

**Window:** 2026-08-25 ~08:35Z -> ~09:00Z (continues `session_0745-0835Z_...` @`ea57c249cc`)
**Serial:** `2.0.0_SA_COO~Z` (PID 36468)

---

## 1. THE DIRECTIVE IS COMPLETE -- ALL FOUR VERBS DISCHARGED

```
"fix this and only this"    DEFECT A f67b3a48 (portal) - DEFECT B 2e9737af49 (publisher)
                            TWO fixes. No third. SIX things filed-not-fixed.
"verify visually"           RUNG 1 local render - RUNG 2 served bytes - BUNDLE (mine)
                            RUNG 3 LIVE PRODUCTION render, BOTH defects, BEFORE/AFTER on
                            ONE instrument at ONE origin (DT~Z)
"pipelines scheduled/robust" scheduled YES; one exposure and it is NOT in AWS. No monitor built.
"commit, push / prod-deploy, origin/PROD a7a7ff16 - tag portal-v2.1.166 - CI 32827830122 SUCCESS
 and all necessary logging"  ledger CLOSED 7/7 - NEVER#6 discharged, nothing stranded
```

**Rung 3's delta table is the strongest artifact of the night** -- three books reconcile to the
hundredth against a panel computed by a DIFFERENT code path, and the fourth is short by EXACTLY the
known 2.69:

```
                  DIVZ     IDVZ     PFDE     PFOE
COLUMN SUM       99.80    96.82   100.01    99.99
asset-class bars 99.80    99.51   100.01    99.99
DELTA            -0.00     2.69     0.00     0.00
```

## 2. WHAT I VERIFIED MYSELF RATHER THAN RELAYED

After being burned twice earlier in the session by amplifying unchecked claims, I re-derived every
load-bearing figure before carrying it:

| claim | my independent check |
|---|---|
| Defect B on the served bytes | diffed live bytes vs my own pre-fix copy: **4 changed / 183 unchanged** |
| the deployed CODE is on the wire | production chunk `index-EGsm0oyQ.js` carries `current_holdings` **x8**; post-fix source 8, pre-fix 5 -- a **derived** discriminator with a real gap |
| CI | run 32827830122 polled to `conclusion: success` myself |
| the tag | raw `fe0fccfb512c` peels to `a7a7ff165078` == `origin/PROD`; **raw != peeled**, so the peel was a real operation |
| my own commits' push state | `merge-base --is-ancestor` + a positive control -- both **ON** `origin/SITEZ` |
| "EventBridge ZERO rules at hour 11" | re-derived: **NINE** fire in hour 11; the 0 was a `cron(0 11` PREFIX test |

⚠ **TWO COUNTING TRAPS, both of which returned tidy wrong answers:**
- **`grep -c` on a minified bundle is useless** -- the chunk is 3 lines, so it returned **1** for every
  pattern. Four different quantities all reading 1, and it looks clean. `grep -o | wc -l` gives the
  true 1 / 8 / 14. **A line count wearing an occurrence count's clothes.**
- **My first bundle pattern was `attributionData`, which reads ZERO on the wire** because minification
  renames local identifiers. Property names on API JSON survive; variable names do not. **That would
  have been a confident false ABSENT.** The fix was to derive the discriminator from `git show` on
  both refs before going to the wire.

## 3. THE CRITERION THAT MOVED TWICE -- AND IT IS THE SESSION'S BEST LESSON

The 13:00Z acceptance check is the only obligation outliving every session in this fabric. Its
criterion (d) was authored wrong by me, corrected wrong by another seat, and settled only at source.

```
MINE (msg 8939)   "does data_as_of advance, or did the bbg guard SKIP?"
                  -> two branches; the EXPECTED value (unchanged 2026-08-24) lands in the BAD one
                  -> would manufacture a FALSE OUTAGE on a healthy first fire. NEVER#1's own class.
DS~Z's fix        "data_as_of = 2026-08-25 -> the 11:00Z pull landed; healthy"
                  -> conflated the bbg feed with the SILVER feed
                  -> would license a FALSE PASS on a partition landing 9h early
SETTLED AT SOURCE etf_positioning_gold.py:337-345 -- "as_of comes from the newest silver/holdings
                  partition that exists"; silver lands cron(0 22) = 22:00Z, NINE HOURS AFTER the fire
THEN A THIRD      both of the above were written as a DATE. CTO~Z caught it.
CORRECTION        *** A DATED CONSTANT IN A CARRIER BUILT TO OUTLIVE ITS AUTHORS IS TRUE TODAY AND
                  SILENTLY WRONG ON EVERY LATER FIRE. *** Same class as a frozen count in prose:
                  correct when written, with nothing announcing the transition.
LIVE FORM         RELATIVE, never dated -- CTO~Z ruling 8944:
                  data_as_of == the NEWEST silver/holdings partition existing at fire time
                                (T-1 on a normal weekday)                      PASS
                  data_as_of AHEAD of that                                     ANOMALY -- explain it
                  a REAL skip shows up as (a) no new log stream or (b) generated_at not advancing
```
⛔ **THREE FORMS OF (d) EXISTED AND ONLY THE THIRD IS LIVE.** `0.4.0_DS_ClientPlatform~Z` then sent a
pointer saying *"take COO~Z's wording"* -- **which points at my ORIGINAL, the superseded form that
fires falsely.** They caught and corrected their own pointer within six minutes. >> **A POINTER TO A
CORRECTION CAN ITSELF DELIVER THE DEFECT THE CORRECTION REMOVED.** Cite the live form's CONTENT, not
a seat's name -- a name resolves to whichever version the reader finds. <<

>> **THE TWO ERRORS POINT IN OPPOSITE DIRECTIONS AND ONLY ONE OF THEM ANNOUNCES ITSELF.** Mine fails
LOUD (a false outage everyone sees). DS~Z's fails SILENT -- **a too-loose expected value is not the
safe error, it is the one that cannot fail, and a criterion that cannot fail is not a criterion.** <<

⛔ **AND I AUTHORED MINE AFTER SPENDING THE SESSION POLICING EXACTLY THAT CLASS IN SIX OTHER SEATS.**
Enforcing a rule immunises you less than citing it: it converts the rule from something you check
against into something you feel you already embody. **Caught because `1.0.0_SA_CTO~Z` read the
criteria instead of ratifying the owner and moving on.** Banked to
`memory/citing-a-rule-is-not-applying-it.md` as a second instance.

⭐ **A wrong CRITERION is worse-shaped than a wrong CLAIM: it sits inert, looks like diligence, and
fires hours later at an unattended moment, executed by a seat with every reason to trust it.**
Neither seat's recollection settled it; **reading the resolver's own docstring did.**

## 4. CARRIER DISCIPLINE -- THE TO IS PRIMARY

`1.0.0_SA_CTO~Z` ruled the task order PRIMARY over the deliverable, because `to-check.py --all` is
what a successor actually runs at startup while a deliverable section is queried by nobody.
**Ratified and applied.** The criterion above then moved TWICE inside twenty minutes -- **which is the
two-carrier divergence arriving exactly on schedule, and the reason the primary had to be named
before it happened rather than after.**

## 5. FILED, NOT FIXED -- SIX, NONE TOUCHED

```
1  DEV CI has not type-checked/built since 02:08:25Z (steps 8-11 SKIPPED, not failed)   I OWN IT
2  PerfrpTable.tsx:29 dead import                                                  AT ANDREW
3  book-name branding: served "Polen ..." vs shared map "Opal ...", 3 of 4 diverged AT ANDREW
4  IDVZ null-drop 2.69 (ours) + 0.49 (issuer's book) -- no "Other" bucket invented
5  build_package.py 4 members vs the deployed 2 (trading_calendar layer-shadowing risk)
6  ICT / MER / 2602335D / RBGLD unresolved identifiers                        CTO~Z daylight cell
```
⭐ **Five of the six were one or two lines and obviously correct. Nobody fixed any of them. That is
the fence doing its hardest work** -- a fence only costs something when it stops an act you want to
take, and that is the moment it is worth having.

## 6. CURRENT STATE / NEXT

```
COMPLETE   both defects live on production and verified on a render at three seats
OPEN       13:00Z read -- OWNED by 0.7.0_AE_CloudOps~Z, criteria in the TO (primary carrier),
           criterion (d) at its SOURCE-CONFIRMED final form (sec. 3)
OPEN       AWAITING ANDREW: the FXFXX string is DERIVED (ours, not his ruling); PerfrpTable.tsx:29;
           the Polen/Opal branding divergence
MINE       carry the DEV-CI finding forward past this session
```

**ZERO crons armed this entire session. Scope fence held: two defects, no third fix.**
