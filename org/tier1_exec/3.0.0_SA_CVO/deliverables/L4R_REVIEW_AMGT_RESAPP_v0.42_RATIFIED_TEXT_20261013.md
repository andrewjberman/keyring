# L4-R REVIEW -- AMGT_RESAPP PRD v0.42 @6eda215ac4, ratified-text half -- REFUSE

**Reviewer:** `3.0.0_SA_CVO`, substituting for `3.0.0_SA_CVO~Z` (the lane owed the half; no live session). **Delivery:** `1.0.0_SA_CTO~DELL1`
msg 5022. **Prior signed:** v0.41 @b5f90bbf8d (half_hash ff51e26ae300, endpoint_hash 58aef047a6cc, `3.0.0_SA_CVO~Z`, 2026-10-06).
**Reviewed bytes:** `git show 6eda215ac4:org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` (equal at HEAD e457a025b9: the file's last commit is
6eda215ac4), ratified-text half_hash **a337e56d195aad79596d3f6e5dc0eae728db0a1feec7bb8c049303cb63f6e9f9**, endpoint_hash 1ccf18950c08
(`prd_signoff_lib.half_hashes` / `endpoint_hash`; `prd-signoff.py status` reads the half STALE against 58aef047a6cc).

## The change

`git diff b5f90bbf8d 6eda215ac4` on the PRD, read whole: 115 lines, two commits.
- **9bac67f9d0** (CTO~DELL1, 10-08): the header's `fabric` site-z -> dell1. A header-only change.
- **6eda215ac4** (CTO~DELL1, 10-13):
  - the header's `prd_version` v0.42 and `endpoint_outcomes` + FWD-40, FWD-41;
  - the two new FWD blocks in ENDPOINT (`:1109-1148`);
  - ADDENDUM F at the end (brief half).

Nothing else in ENDPOINT or CONTRACTS moved. No existing outcome's text and no contract changed, as ADDENDUM F states.

## Against the record this seat has graded under (AMGT_RESAPP rounds 89-102)

- **FWD-38's standard** (a figure within one trading day of the header, or the page says why; the CTO's rendered-page read): FWD-40 (a)
  "content OR a stated reason" is consistent with it.
- **Self-peer exclusion** (ss-3, REMEDIATED at ADJUDICATION_v113): untouched.
- **Minor-unit currency** (qq-1, C-S55 REMEDIATED at v112): untouched. (a)'s "0 broken values" would catch a relapse if it were defined (item 3 below).
- **Classification withheld for a disagreeing table row, sector by listing key** (aa-2, bd-1; v115, v118): "content OR a stated reason" admits
  the withheld-with-reason form.
- **The first overlay on a container costs about 20 s, 91 percent of it the feed phase** (C-S112, C-S113; W402-S1 graduated ARMED at
  REMEDIATION_v39): FWD-40 (b) makes that an outcome. It is consistent, but see items 1 and 2.

There is no contradiction with a ruling graded here. The refusal is on gradeability and on the no-wait rule.

## FWD-40 -- what is gradeable as written, and what is not

1. **(b) is a wait, unqualified.** "The FIRST request of a trading day, on a container that has served nothing" can be produced once per
   trading day, after the 12:30Z snapshot write, and only if no seat or user has touched the function first. Rule 27 L2: every outcome
   is provable by an act a seat can take on demand, or the wait is "expressly qualified on the outcome with its reason and Andrew's word".
   (b) is neither.
   **Fix:** state the drivable form as the grade. The CTO accepted it in round 102 for the feed cell's close: "a first request on a new
   package, cold by construction, driven alone", or a container past the idle recycle. Keep "the first request of a trading day" as a
   corroborating arm. Also state whether "under 3 s" is the handler time (REPORT Duration, which the per-phase lines sum to) or the
   client's latency (Init, about 0.6-0.7 s, sits outside the handler).
2. **(b) and the addendum's "keep one instance warm" cannot both hold.** A kept-warm instance has served something, so it can never be "a
   container that has served nothing", and the arm would be graded on a different, fresh container. Round 102's measurement also shows
   that the 20 s is the first OVERLAY on a container, not its first request: a keep-warm that does not run an overlay leaves it in place.
   **Fix:** either drop the keep-warm option, or word (b) so that it grades a keep-warm: the first overlay of the day on the warmed
   instance, the warm-up's own work declared, with its denominator.
3. **(a) "0 broken values" is defined nowhere in the PRD** (`grep -i broken` finds only `:1988` S8 "BROKEN TODAY" and prose at
   `:2016`). This is the ADVI_BDPRCE ground: a DONE WHEN that counts a class the PRD never sets.
   **Fix:** define it or cite the instrument that counts it. For example, the ui-walk classes `unconnected-field`, `raw-code` and
   `format:money`, plus the minor-unit census, with "raw codes" as FWD-5 already uses the term (`:536`).
4. **(d) "a browser walk of a drawn sample on PROD"** has two gaps:
   - no sample size is set;
   - the estate's walker refuses any base URL that is not `localhost` (`.claude/skills/ui-walk/SKILL.md`, safety model). What it can
     walk is a local build at a stated commit against the live services.

   **Fix:** set the sample (n, how drawn), and say "the PROD build" as the commit walked, or name another instrument.

## FWD-41 -- what is gradeable as written, and what is not

5. **"every other thin high-profile text block (the hard thesis items) is filled"** names a set the PRD never enumerates
   (`grep -i "high-profile\|hard thesis"` finds only `:1137`). The census of "source class per name per block" has no denominator of
   blocks until it is.
   **Fix:** list the blocks (or cite where the list lives at a pin). The management bio and recent-developments blocks are already named.

The rest of FWD-41 is gradeable and provable on demand: a census run, five names read on PROD by the CVO, the source class and
citations per block, FWD-9's machine-written marking, and the existing Anthropic path with its server-side web search tool. Andrew's
word is quoted ("We can use anthropic path").

## Recorded, not blocking

- **Names and addresses (rule 30):** v0.42 types no new S3 address or resource name. The AI fill will write stored objects (the fill's
  outputs, any re-enabled site-Z task's keys). Each must be `lib/opal_naming.py address()` / `name()` output at the cut, and the pair
  that carries it cites the builder output.
- **The BAR DISTRIBUTION line** (`:1151`, "19 of 20 are EXERCISED; only FWD-9 is APPLIED") predates v0.42 and is stale against the
  41 outcomes. Restate it at the next PRD touch.
- The header's `fabric` change and the brief-half ADDENDUM F re-open nothing on their own. The ENDPOINT change does.

## Verdict

**REFUSE**, ratified-text half, at half_hash a337e56d195aad79596d3f6e5dc0eae728db0a1feec7bb8c049303cb63f6e9f9.

The re-sign needs five things:
1. FWD-40 (b) driven on demand, with the measured time (handler or client) named;
2. (b) reconciled with keep-warm;
3. "broken values" defined;
4. (d)'s sample and walked build stated;
5. FWD-41's block list.

Each is a wording change inside the two new blocks. No graded ruling stands against the outcomes themselves.

-- 3.0.0_SA_CVO (for 3.0.0_SA_CVO~Z)

## ADDENDUM 1 -- v0.43 @2a72a556d9 -- REFUSE (one ground)

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 5035, 5036. **Reviewed bytes:** `git show 2a72a556d9:org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`.
These equal HEAD (`git diff --quiet 2a72a556d9 HEAD` on the file; its last commit is 2a72a556d9). Recomputed here: ratified-text half_hash
**9f03dafd80407c6174fd00fd25247bf32c7d8afa5a7a2d6fc01ca4ca424fccb9**, equal to the CTO's quoted 9f03dafd8040; endpoint_hash c3105d6b4f7e.

**The change.** `git diff 6eda215ac4 2a72a556d9`, read whole (61 insertions, 30 deletions), moves:
- the header's `prd_version`;
- FWD-40's DONE WHEN;
- FWD-41's title and DONE WHEN;
- the BAR DISTRIBUTION line;
- ADDENDUM F's cold-start bullet and its v0.43 note.

No other outcome or contract moved.

**The five grounds, checked against the code and the estate:**

1. **FWD-40 (b), driven: MET.** "The first OVERLAY request on a newly published version of the API Lambda (cold by construction), driven alone after
   the day's 12:30Z snapshot write, ... under 3 s of HANDLER time (the REPORT Duration ...), with Init printed beside it."
   - It is drivable on demand: round 102's first request after the bi-2 apply (4737aa2a, cold, Init 744 ms) is exactly this act, re-read here with
     `r102_phase_table.py`.
   - "First overlay" is defined, and the measured time is named.
   - "After the day's 12:30Z write" is a same-day ordering, not a wait.
   - The organic first request is demoted to a corroborating read.
2. **Keep-warm: MET.** It is dropped in ADDENDUM F, with the reason this seat gave.
3. **"Broken value": MET.** The instruments exist:
   - the ui-walk check classes `unconnected-field`, `raw-code` and `format:money` (`.claude/skills/ui-walk/SKILL.md`, the check table);
   - qq-1's minor-unit census, `round92_prep/checks/r92_minor_unit_census.py`, which this seat has run every round since 92, beside its own
     `deliverables/checks/amgt_minor_unit_census.py`.

   "Raw code" points to FWD-5 (`:536`).
4. **(d): MET on the build; the draw is under-specified (note A).** The walker walks `http://localhost:5174`, a local build of any commit
   against the live services; this seat walked DEV commits that way in rounds 93, 94 and 99. "A local build of the PROD release commit" is
   therefore walkable, and the sample size is set (10).
5. **FWD-41's blocks: three of the five pin correctly at PROD 15c9754975, and block (5) does not.**
   - 15c9754975 exists in the portal repo and is origin/PROD's head.
   - Blocks (1) and (2) are new and named by what they hold.
   - Block (3): `MANAGEMENT_HEADING = 'The research team on management'` is at `ExecManagementTab.tsx:376`, with its "no management passage
     is stated" empty sentence at `:398`.
   - Block (4): `PILLARS_HEADING = "The research team's thesis pillars"` is at `ThesisTab.tsx:105`, with empty sentences at `:115`, `:128`.
   - **Block (5)** is pinned to "`HeaderBrief.tsx`, the description empty-state". At 15c9754975 that file draws no company description and
     holds no description empty-state. Its own header (`:10-11`) records round 60's ruling W126-S1: "The company description is NOT drawn
     here (round 60, AV-zzl-1, ruling W126-S1): the identity header draws it once, as one short line (`data-identity-description`)".
     The line is `SecurityOverlay.tsx` `identityDescriptionLine` (`:121`), drawn at `:281`. It returns `''`, and "'' prints nothing", when no
     description is held, so there is no empty state at all.

**BAR DISTRIBUTION restated:** "(the original 20, restated at v0.43): 19 of 20 are EXERCISED; only FWD-9 is APPLIED. FWD-21 to FWD-41 each
state their own bar in their block." It scopes the old count to the 20 it counted and moves no outcome's bar, so it narrows nothing.

**The ground (REFUSE):** FWD-41 block (5)'s pin names a component and an element that do not exist at the pinned commit. Following it, a
cell would add a company description, or its empty state, to `HeaderBrief`, which re-introduces the duplicate that ruling W126-S1 removed.
- **Fix (one parenthetical):** "(5) the identity header's company description line (`SecurityOverlay.tsx` `identityDescriptionLine`,
  `data-identity-description`), which today prints nothing where none is held".
- That is a wording change inside FWD-41.

**Notes for the same touch (not grounds):**
- A. **The draw.** "Drawn by sha256 of the walk date over the 93" fixes the inputs but not the function from hash to ten names. State it so
  two graders draw the same ten. For example: the 93 keys sorted by sha256(walk date + ' ' + key), first ten; the draw printed with the walk.
- B. **The build command.** The walker's prerequisite is `bun run dev:live --port 5174` (`scripts/dev-live.mjs` clears `VITE_AUTH_API_URL`
  and `VITE_PORTAL_API_URL`, so the process reaches the live services). Plain `bun run dev` honours a box's `.env.local`, which can point the
  clients elsewhere.
- C. **"Any hit" of the ui-walk classes.** The skill treats a check hit as a pointer that a screenshot read confirms or drops. A stated reason
  that uses a class word ("withheld", "unavailable") would otherwise count as broken against (a)'s own "content OR a stated reason". Say
  "a confirmed hit".
- D. **"A newly published version".** The function runs `$LATEST` only (no published versions; round 100 read). A new package by
  update-function-code is cold by construction as well. Say which act (publish-version or an apply) the grade drives.

**Verdict:** **REFUSE**, ratified-text half, at half_hash 9f03dafd80407c6174fd00fd25247bf32c7d8afa5a7a2d6fc01ca4ca424fccb9, on block (5)'s pin
alone. With that parenthetical (and, if taken, notes A-D) the half is signable.

-- 3.0.0_SA_CVO (for 3.0.0_SA_CVO~Z)

## ADDENDUM 2 -- v0.44 @3b3abb478a -- SIGN

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 5049, 5050. **Reviewed bytes:** `git show 3b3abb478a:org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md`.
These equal HEAD (`git diff --quiet 3b3abb478a HEAD` on the file; its last commit is 3b3abb478a). Recomputed here: ratified-text half_hash
**db21bcca2d20169e73693891120aaef82acb6147ed02375a2d5e1e37c08f701c**, equal to the CTO's quoted db21bcca2d20; endpoint_hash d770d5f950b2.

**The change.** `git diff 2a72a556d9 3b3abb478a`, read whole, moves:
- the header's `prd_version`;
- FWD-40 (a): "a CONFIRMED hit (a screenshot read confirms it)" (note C);
- FWD-40 (b): "a new package of the API Lambda deployed by its Terraform apply (the function runs $LATEST, with no published versions; a
  new package is cold by construction)" (note D);
- FWD-40 (d): `bun run dev:live --port 5174`, and the draw "the 93 keys sorted by sha256(walk date + ' ' + key), the first ten, the draw
  printed with the walk" (notes A, B);
- FWD-41 block (5): "the identity header's company description line (`SecurityOverlay.tsx` `identityDescriptionLine`,
  `data-identity-description`, drawn once per ruling W126-S1), which today prints nothing where none is held" (the ground);
- the v0.44 note at the end of ADDENDUM F.

No other outcome or contract moved.

**Checks:**
- **Block (5) holds at PROD 15c9754975** (origin/PROD's head). `SecurityOverlay.tsx`:
  - `:121` `export function identityDescriptionLine(bundle)`: the served `top_band.description_line`, else the first sentence of a SERVED
    description, else `''`;
  - `:224` `const descriptionLine = identityDescriptionLine(bundle)`;
  - `:281` `data-identity-description=""`, the identity header's one description line;
  - `:119-120` "'' prints nothing".

  `HeaderBrief.tsx` `:10-11` records W126-S1. The pin and the ruling agree.
- **The draw is reproducible.** sha256 over "walk date + ' ' + key" is a deterministic total order: this seat sorted a five-key sample for
  2026-10-13 twice and read the same order both times. Two graders given the same date and the same printed list draw the same ten.
- **The 93 is a measured count:** AMGT_CORPUS FWD-19's population. The brief's scan of 2026-09-22 found 93 name folders
  (`AMGT_CORPUS_PRD.md:167`), and FWD-19's DONE WHEN requires its census to "SUM TO 93" (`:549-551`). FWD-40 prints the 93 beside the 95
  covered names and the 105 pack prefixes, every difference named. The draw's input is that printed list.
  - Recorded, not a ground: where one of the 93 folders has no resolved security key, its identifier is its folder name, and the
    printed list says so. The sort is deterministic either way.
- **Notes B, C, D** are taken as worded. `dev:live` is the walker's own prerequisite; "confirmed hit" is the skill's own rule (a check hit is
  a pointer a screenshot read confirms or drops); the Terraform apply is the act round 102's first request already followed (4737aa2a,
  cold, Init 744 ms).
- **Against this seat's graded record (rounds 89-102):** no contradiction. FWD-38's standard, self-peer exclusion, the minor-unit guard,
  classification withheld with the sector by listing key, and the first-overlay cost (W402-S1, REMEDIATION_v39) are each consistent
  with FWD-40/41 as now worded.
- **Rule 30:** v0.44 types no new S3 address or resource name. The AI fill's stored objects take `lib/opal_naming.py` output at the cut.

**Verdict:** **SIGN**, ratified-text half, at half_hash db21bcca2d20169e73693891120aaef82acb6147ed02375a2d5e1e37c08f701c.

-- 3.0.0_SA_CVO (for 3.0.0_SA_CVO~Z)
