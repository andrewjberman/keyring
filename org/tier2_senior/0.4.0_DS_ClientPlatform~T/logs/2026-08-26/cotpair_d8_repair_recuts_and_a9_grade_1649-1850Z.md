# 0.4.0_DS_ClientPlatform~T -- the cottonwood pair D8 repair, two re-cuts, and the A9 grade (1649-1850Z)

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (primary) · DIAGNOSE · VALIDATE

Lane seated 16:49:44Z by `0.0.0_AB_MSTR` (72603), briefed 16:50:35Z by `1.0.0_SA_CTO` (72604 GO),
ratified verbatim by `2.0.0_SA_COO` (72632). Scope: `build_cottonwood_mdpf_pair.py` ONLY.

---

## SUMMARY

The cottonwood MDPF pair filtered accounts by the **directly-assigned parent's** opal-ness BEFORE
the blend descent, so an account under a non-Opal container holding Opal children was never walked.
`$43,676,557.13` of Opal dollars never reached attribution. Repaired, re-cut twice on defects found
in my own work, exercised, and graded.

**A9 NOT MET (9/12) and the fix VERIFIED.** Those are not in tension: the cottonwood leg is green on
every pre-registered criterion including the primary discriminating arm, and what fails is a
DOWNSTREAM composition identity the repair made REACHABLE. `3.0.0_SA_CVO`'s independent verdict
`@68f61a11c5` concurs on both halves.

Five commits, all LOCAL (measured against a fetched ref with positive+negative controls, never
assumed).

---

## THE DEFECT

`data/assets/scripts/gold/build_cottonwood_mdpf_pair.py:133 @bd69bb150e`

    opal_assigned = assigned[assigned.model_id.isin(opal_ids)]

A pre-filter on the assigned PARENT's opal-ness, applied before the `:159` blend descent. Affected
accounts did not fail to attribute -- **they were never walked.**

**WHY IT SURFACED NOW:** `WSE_COTMDL`'s `MODEL_DETAIL_SCOPE` went `opal_closure` -> `all` (applied
2026-08-25T10:38:32Z), taking the blend 37->117 edges / 19->46 parents / 8->17 children. **A correct
change made a pre-existing filter defect reachable.** No seat authored a defect.

**THE ASYMMETRY THAT IS THE WHOLE STORY:** `build_dim_model_portfolio.py:329-334` had ALREADY removed
the identical pre-filter and says so in terms. The dim was right the entire time; the pair was wrong;
identical inputs, `$147.0M` vs `$190.7M`. **The fix is to make the pair ask the dim's question with the
dim's own function** -- `bdmp.attributes()` is now IMPORTED, not re-derived.

---

## WORK DONE

| commit | what |
|---|---|
| `f06cbf4a0b` | the repair: full population, leaf-grain Opal identity (roster UNION blend children), `bdmp.attributes()` wired, `Client - Opal Supervised` segment ITEMISED |
| `4e0410825e` | re-cut per CTO 72723 option (e): DROP the module-level `mdpf_category_registry` import |
| `1b7f86106e` | pre-registration of the amended A5 split, BOTH grains, measured per account per leaf |
| `bae0a826d3` | route the DIVZ SMA sleeve to SMAs(L0) key `opal_div_sma` per Andrew 17:42/17:45Z |
| `5d3dd17d9b` | release-note s.2: figures, denominators, placement |

---

## FINDINGS

### F1 -- I introduced a module-level import edge onto a module under a live NO-SHIP, and it would have failed twice over

`f06cbf4a0b` added `import mdpf_category_registry as mcr` to read the segment label -- complying with
72604's "classify FROM the D1 REGISTRY" in the shape that couples hardest, while reading that module's
own interlock neighbourhood.

- **INTERLOCK:** `build_package.py:240-283` records the bundled registry copy as INERT *because no
  packaged module imports it*. After that build, one would. **A members-only bundle diff structurally
  cannot see a reference arming an existing member.**
- **IT WOULD NOT HAVE RUN:** at bundle vintage `48c473caa1`, `display_label` / `NODE_DISPLAY_LABEL` /
  `VIEW_NODE_AXIS` ABSENT, `"Client > Opal Supervised"` 0 occurrences. Positive control at the same
  vintage (`resolve` / `members_for` / `VIEW_TREE` / `UnknownMemberError`) all PRESENT, so those are
  real absences.

**AND THE OBVIOUS ESCAPE WAS CLOSED, which is what changed the fork:** `git log -S` over the registry
shows the fatal exact-float peer-sum predicate landed `efec3ca8b5` (08-24T18:33:26-04:00) and
`display_label` landed `cd357d6319` (08-25T02:22:41-04:00). **THE DEFECT PREDATES THE API BY ~8 HOURS
-- every vintage carrying the symbol carries the armed predicate.** That killed option (a) on the
facts, not on judgement. CTO ruled option (e), which removes the dependency instead of dating it.

**CONTROL ARM, EXERCISED NOT GREPPED:** `"mdpf_category_registry" in sys.modules == False` after import
AND after a complete `build_artifacts()` run. A grep proves the line is gone from source I read; this
proves the module is not pulled in on ANY path the producer takes.

### F2 -- My DIVZ routing table was keyed lower-cased and emitted a UNIFORM $0.00

`_norm` is WHITESPACE-ONLY BY DESIGN and deliberately does not lower-case (case-folding would silently
merge genuinely different model names). My key `"divz sma"` matched nothing. The run emitted
`SMAs = $0.00` with the residual unchanged -- **a key failure wearing the shape of a real answer.**

Caught in ONE read because A5b was pre-registered at `$1,393,065.98` before the edit existed, and a
uniform `$0.00` is an INSTRUMENT SIGNATURE, not a result. **Absent the pre-registration, an empty SMA
bucket reads as "no SMAs here" and ships.** Nothing mechanical would have caught it -- it ran, and
produced a well-formed artifact. This is `0.6.2_AE_PartnerETL~A`'s own uniform-zero doctrine, earned on
three probes tonight, paid back into a different lane within the hour.

### F3 -- The same figure travelled with a WRONG DENOMINATOR four times in one thread

1. the struck `$38,103,539.26` (true `$2,869,379.04`);
2. `$2,869,379.04` described as "across ALL 129 dropped accounts" -- it is the 2-account non-Opal-parent
   subset;
3. A5b's denominator is ONE account (`Anna *9238` carries no DIVZ leg);
4. **the 18:10Z sovereign conditional quoted `~$1.48M` for a field that ships `$2,256,694.98`** -- a
   `$780,381.91` gap.

(4) is the one that mattered: it sat INSIDE a sovereign conditional on a client-facing surface, and if
it had served, the first person checking the number against the sentence authorizing it finds a $780K
gap with no way to tell shorthand from defect. Caught by measuring the FIELD against the SENTENCE
rather than trusting a relay chain that included the issuer's own message. **CTO ruled (a): the artifact
is right, the headline was the subset grain; the serve figure is corrected on the record.**

**RECOVERED POPULATION IS 2 ACCOUNTS, NOT 129.** 129 is the filter's blast radius; 127 hold no Opal
constituent and are correctly excluded by the guard carried over from the dim -- which is exactly why
identity (i) ties.

### F4 -- The cottonwood DIVZ leaf and the served `opal_div_sma` are DIFFERENT id spaces

cottonwood leaf `31f17857-3456-4f9b-8a47-a4a8e383d56c` vs crosswalk `48af6559-593a-48a9-8ac4-3c78ded93ad8`.
**A KEY-level bucket join, not an id-level one**, and no id-level resolution exists to lean on. Recorded
at the line because a later reader will assume the ids meet.

### F5 -- A9's failure is caused by this fix, and the delta names the key to the cent

    FATAL: 2026-08-25: sum(by_model cohort=model) 1,794,123,741.44
                    != model_aua                  1,802,566,138.36
                       delta -8,442,396.92

**That is exactly the Fixed Income figure ($8,442,396.91, 1c float).** cottonwood's `model_aua` carries
the recovered dollars; global's `by_model` cohort sum does not.

**THE THREE-FILE COUPLING CLASS, THIRD SIGHTING TODAY.** CTO's 72856 constraint (2) stated the general
form PROSPECTIVELY, we applied it to `opal_div_sma`, **and that is why DIVZ is clean. The key that bit
us landed in the FIRST commit -- before the lesson was stated.** We hardened the new key and never
re-checked the one already in flight.

I named the KEY with certainty and explicitly did NOT name the SITE (a global-producer read, not my
file). `3.0.0_SA_CVO` took the closing measurement I specified; `2.0.0_SA_COO` later corrected the file
name across four seats -- the site is **`dim_mdpf_aggregate_aua_timeseries.py:127` `GLOBAL_MODEL_KEYS`
/ `:2449`**, NOT `mdpf_aggregate_aua.py` (one token apart, both live).

### F6 -- Constituent grain sees what blend grain cannot (surfaced, not chased)

`fact_model_definition` shows the `Opal Short-Term` sleeve of `Blended Opal / Satellite 50` holds
**DIVZ, IDVZ and PFDE at SECURITY grain** -- three of Andrew's exact discovery-mechanism tokens, one
grain BELOW the model/sleeve space his ITEM B ruling scoped that mechanism to. **The dollars are
correctly placed today** (constituents inside an Opal Primary model that already attributes in full).
Not a defect, not a reason to touch anything. Carried to the PRD by COO; not chased.

---

## ACCEPTANCE

Vintage: assignment `2026-08-26` x value `2026-08-25`. Graded against `2.0.0_SA_COO`'s pre-registered
A1-A9 `@8d87d4784c` + my A5 amendment `@1b7f86106e`. **PRE-FIX CONTROL** = the same build run from
`HEAD` at the same vintage, reproducing production exactly (models `$140,410,927.00`, decomposed
`$147,047,720.63`, 5 keys, bridge 328) -- so the deltas are attributable to this edit.

| id | expected | observed | verdict |
|---|---|---|---|
| A1 Conservative Growth | 23,337,850.45 | 23,337,850.45 | MET |
| A2 Ultra Short-Term | 11,896,309.76 | 11,896,309.77 | MET (1c float) |
| A3 Fixed Income | 8,442,396.91 | 8,442,396.91 | MET |
| A4 TOTAL recovered | 43,676,557.12 | 43,676,557.13 | MET (1c float) |
| A5a supervised (full segment) | 2,256,694.98 | 2,256,694.98 | MET -- 3 accounts |
| A5a' supervised (non-Opal-parent) | 1,476,313.07 | 1,476,313.07 | MET -- 2 accounts |
| A5b SMAs -> `opal_div_sma` | 1,393,065.98 | 1,393,065.98 | MET -- 1 account |
| A6 decomposed total | 190,724,277.75 | 190,724,277.76 | MET (1c float) |
| A7 identity gate | FAIL -> PASS | PASS | MET |
| A8 by_model keys | 5 -> 6 | 6, gains Fixed Income | MET |
| **A9 qa_local** | **12/12, errors{} empty** | **9/12, errors=['global']** | **NOT MET** |

`A5a + A5b = 3,649,760.96` -- **identical to the pre-DIVZ segment total.** The SMA ruling moved money
between two named buckets and created none. Firm AUM unchanged `$480,687,460.42` throughout.

**A9 GRADING PROTOCOL** (registered at 72813 BEFORE the result, ratified 72877):
- vintage precondition: **MET** -- `15:29:34Z -> 18:21:12Z`, `3/897ecG... -> LdShsMmF...`, both moved.
- **PRIMARY ARM (the delta, not the count): PASS** -- `delta = 0.0100` PRESENT, `43676557.1200`
  **0 occurrences**. The gate flipped on the SAME comparison that failed at 43,676,557.12.
- SECONDARY (count): FAIL, 9/12.

Reported NOT-MET against my own bar with the fix's own success sitting next to it.

---

## DELIVERABLES WRITTEN

| artifact | commit | what it is |
|---|---|---|
| `A5_AMENDED_SPLIT_PREREGISTRATION_20260826.md` | `1b7f86106e` | the A5a/A5b split measured per account per leaf, BOTH grains, written before the DIVZ edit existed |
| `COTTONWOOD_PAIR_RELEASE_NOTE_FIGURES_20260826.md` | `5d3dd17d9b` | release-note s.2: every figure carries its population on the same line |

---

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `commit-gate.sh` | per-file, x4 | PASS | pre-existing UNRESOLVED-LANE note on `FIRM_ID`/`FIRM_NAME` constants I did not touch |
| `safe-commit.sh` | x5, `-F` message files | PASS | messages authored with a non-shell writer per Rule 14a, never `printf`-built |
| `safe-deploy.sh` | x3 | PASS | `comp-pipescript deployed` MATCH each time |
| `comp-pipescript deployed` | via safe-deploy | MATCH | **see gap below** |
| `recon_predicate_control.py` | 5 arms, 40 invocations | PASS | exercises `mdpf_category_registry`, which this change does NOT modify -- independence intact |

**What worked:** the halt-gate's fail-closed identity refusal was RIGHT and caught that I had skipped
XXX.md Step 1b A.1 (session serial file). Fixed the cause rather than overriding.

**What failed:** nothing in the tools.

**GAP FOUND (worth the record):** `comp-pipescript deployed` returns **MATCH while the running lambda
bytes are stale**. It certifies the S3 code tree; the lambda executes a BUNDLED copy
(`build_package.py:151`). **DESIRED vs APPLIED -- the instrument is TRUE AND SILENT ABOUT THE LAMBDA.**
This is a second, unrelated way that tool reads green on stale bytes, distinct from the CRLF
false-STALE class and pointing the opposite direction. Nobody had cause to test the seam until a
DS-lane S3 deploy and a lambda acceptance met in one task.

---

## MCP TRAFFIC

~60 messages handled; all acked via `ack_messages` (the READ clock). Significant:

- **RECEIVED:** CTO 72604 GO; COO 72632 ratification + A1-A9 `@8d87d4784c`; PartnerETL~A 72618/72622
  diagnosis packet + pre-registered recovery; CTO 72711 `[STOP]` on the import edge; CTO 72723 ruling
  option (e); Andrew-direct x8 relayed (16:34Z segment; 17:42/17:45Z DIVZ-is-an-Opal-SMA;
  17:56/17:58Z discovery mechanism; 18:0xZ CA Tax-Free NOT us; 18:10Z `@666fe25b0c` conditional-YES);
  COO 72875 operative sequencing; CVO 72801 A9 bar + `@68f61a11c5` verdict.
- **SENT:** 72607 ACK; 72675 A1-A8 + the A9 BLOCKING surface; 72736 the ~8-hour-window finding that
  killed option (a); 72813 A9 grading protocol pre-registered; 72905 the NO answer + DIVZ landing;
  72930 the sovereign-conditional grain surface; **73008 the A9 grade**; 73020 predicate FALSE at
  constituent grain; 73051 capacity offer for the global fix.

---

## BLOCKERS

**None owed by this lane.**

`A9` is NOT MET, evidence-cited above -- that is a GRADE, not a blocker on me. The remaining work
(global's `GLOBAL_MODEL_KEYS`) is dispatched elsewhere and is **gated on a Rule 24 ruling, not on
capacity**: `2.0.0_SA_COO` seated this lane in principle at 73070 s.4 then AMENDED it -- adding
`opal_fixed_income` to `CANONICAL_MODELS` is a **canonical-model REGISTRATION ON A CLIENT-FACING
SERVED UNION**, i.e. a Rule 24 schema-enumeration act, not a repair. **DO NOT EDIT YET** stands.

---

## CURRENT STATE

**FILE:** `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py` -- repaired, deployed to
`s3://opal-data-assets/code/scripts/assets_gold/`, and BAKED into the live `mdpf-gold-lambda` bundle
(applied by `0.6.2_AE_PartnerETL~A` 18:21:12Z, `CodeSha256 LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=`).

**BEHAVIOUR NOW:** every assigned account is descended; Opal identity is decided AT LEAF GRAIN by the
imported `bdmp.attributes()` disjunction; `by_model` carries 6 keys incl. `Fixed Income`;
`meta.client_opal_supervised` carries `$2,256,694.98` over 3 accounts with a 3-part itemisation that is
asserted to sum per account; `meta.sma_l0.by_key["opal_div_sma"]` carries `$1,393,065.98` over 1
account and is deliberately OUT of `by_model` and the sidecar. NO import of
`mdpf_category_registry` on any code path.

**LAMBDA STATE:** 9/12, `errors=['global']`. cottonwood + partners build; global's three objects do
not. **NO ROLLBACK** (COO ruled explicitly): rolling back restores TWO failures instead of one,
destroys a verified fix, and re-buries a gap only visible because cottonwood started succeeding.
Rollback remains available and unexercised (prior artifact VersionId
`uGLKSxGv0WkvTRNfQQznjaOOzFvsCm8m`).

**SERVE:** does NOT fire. Andrew's `@666fe25b0c` conditional-YES required a green grade; the grade is
not green, and by his own words the fork returns to him. Priced fall-back if nothing else lands: the
13:30Z fire builds 9/12, global serves stale 08-24 a third day while the gate refuses loudly --
**partial advance, no wrong number served.**

**THE REMAINING SITE:** `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py:127`
(`GLOBAL_MODEL_KEYS = SERVED_MODEL_KEYS + (...)`) and `:2449`. `opal_fixed_income` is absent from the
9-key served global `by_model`. Not `mdpf_aggregate_aua.py` -- COO corrected that name across four
seats.

---

## NEXT STEPS

1. **[`0.4.0_DS_ClientPlatform~T`]** HOLD. Do not edit `dim_mdpf_aggregate_aua_timeseries.py` until the
   Rule 24 ruling lands. Seating stands in principle.
2. **[`2.0.0_SA_COO`]** Route the Rule 24 schema-enumeration ruling for registering
   `opal_fixed_income` on the served global union (four postulates + token-hygiene census).
3. **[`0.6.2_AE_PartnerETL~A`]** Violation COUNT across all 462 dates -- the gate refuses on the FIRST
   and 08-25-only is UNMEASURED. A site fixed for one date that fails on the next is a second night.
4. **[`1.0.0_SA_CTO` / Andrew]** The serve fork, with both arms priced.

---

## DO NOT

- **Do not read `comp-pipescript deployed` MATCH as evidence about the lambda.** It certifies the S3
  code tree only.
- **Do not roll back the 18:21:12Z apply.** Ruled; reasons in CURRENT STATE.
- **Do not add `opal_fixed_income` to `CANONICAL_MODELS` as a "one-line fix".** It is a schema act on a
  client-facing served union.
- **Do not quote any figure in this log without the population beside it.** Four incidents in one
  thread; every table above carries its denominator for that reason.
