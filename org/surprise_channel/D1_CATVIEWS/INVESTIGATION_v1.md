# INVESTIGATION v1 -- D1_CATVIEWS (round 1)

**Owner:** `3.0.0_SA_CVO` (channel) · home MINTED 2026-08-24T20:52Z by `0.4.0_DE_ClientPlatform~C` on
the first item, per the stated trigger (the home mints on an item, never as an empty file).
**APPEND-ONLY during the round.**
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` — `class {OBSERVATION, BLOCKING}` ×
`hazard_standing {ARMED, INERT}`; "latent hazard" = prose for (any class, ARMED).

**Laptop fabric.** Items are `D1_CATVIEWS-S{n}`.

---

## S1 — AC1's named oracle cannot fire on the one file the TO is about, and its silence reads as a pass

**BLOCKING × INERT. SURFACED TO THE ISSUER SAME TURN (66518), RULED SAME TURN (COO 66521),
DISCHARGED BY AMENDING THE TO — NOT THE DECOMP. Cell coverage unchanged (8 cells / 9 criteria,
`cell_refs` still `D1-c-1`).** Logged here for the channel record, not as an open item.

`D1R1DE-AC1` named `comp-transform schema-check ModelPortfolios` clean (no MISSING). On this file
the tool emits **one line and rc=1**:

```
[WARN] types-resolution: no types.ts found near .../ModelPortfolios.tsx (searched co-located + 3 parent dirs + _shared/)
```

`MISSING` count is 0 — **and it never printed its own `SCHEMA CHECK:` header, i.e. it aborted
before running the check.** A zero that could not have been anything else.

**The positive control is what made this a finding rather than a suspicion**, and it is the whole
reason it did not get recorded as "AC1 met": on components that *do* carry a `types.ts` the tool
behaves completely differently — `Correlation` rc=0 *"All rendered fields match their response
types"*; `FactorTilts` rc=0 **and it names a real gap** (*"getAUMMetrics() ->
AUMFlowsWithMetricsResponse: type not found in types.ts"*). The instrument discriminates fine. It
simply has **no domain on this page**.

**Mechanism, measured:** `ModelPortfolios.tsx` is a flat single-file page; its types are 4 **inline**
declarations plus response types imported from `@/api/endpoints/aum` (`MdpfPerFirmTimeSeries`,
`MdpfFirmAUMMetrics`). There is no `types.ts` for the resolver to find, and **no way of calling the
tool differently creates one** — the DESIGNED half of the retrieval-control law, not a call-shape
problem.

**Why it mattered here specifically:** AC1's limb exists to catch *"renders a field the response
type does not carry"* (MISSING = runtime undefined). This TO's entire content is rendering a **new**
block with nested L1/L2 sub-nodes — exactly that failure class. The one instrument named to guard it
is structurally silent on this exact file.

**Ruling (COO, issuer):** declare the `category_views` response types in `@/api/endpoints/aum`
beside the existing MDPF interfaces (Build Ladder rung 2 — the estate already has the pattern), and
`bun run typecheck` (already AC9) becomes the exercised discriminator, **proven once with a mutant**
(render a field absent from the type → typecheck FAILS → remove). The `comp-transform` call stays on
record **run-with-its-domain-disclosed**; it is not deleted.

---

## S2 — a pre-existing React Query cache-key collision on the page this TO edits

**OBSERVATION × INERT. No action taken; not mine to fix.** `comp-cache collisions` reports key
`['model-portfolio-benchmarks']` shared by `portal/src/pages/ModelPortfolios.tsx:533` and
`portal/src/components/ModelPortfolioModal.tsx:114`, both calling `getModelPortfolioBenchmarks()`.

Recorded because it is **on my edit surface and constrains me**, not because it is a defect I am
claiming: two call sites sharing one key with the same accessor is the benign shape of this pattern.
The operative consequence for this TO is one line — **when `category_views` is wired, it gets its own
key; no colliding key is added.** COO concurred (66521).

---

## S3 — the portal promote worktree is still registered and local PROD sits ahead of origin/PROD

**OBSERVATION × INERT. DT's, not mine. No action taken.**

Measured at `0.4.0_DE_ClientPlatform~C` startup:
`git -C portal worktree list` still carries
`.runtmp/portal-promote-20260824T124621Z` at `a239e4a9 [PROD]`, and
`git -C portal rev-parse PROD origin/PROD` → local `a239e4a9023c…` vs origin `8a96c91654ed…` — a
**staged local PROD ref ahead of the remote**, i.e. the pollution `/prod-deploy` Step 2/3 exists to
clear.

**Classified INERT, and the discriminator is stated rather than assumed:** the hazard fires only on a
*promote action*, the disarm (`/prod-deploy` Step 3 `update-ref` + `worktree prune`) is a **mandatory
step of the very procedure that would trigger it**, and the PROD push is currently held at Andrew's
word. A latent hazard whose disarm is already a required step of its own trigger path is not ARMED.
**Were the promote to be run outside that procedure, this would fire silently** — which is why it is
on the record with the two hashes rather than left as a startup impression.

My cells are DEV-only and nothing promote-adjacent is in flight at this seat. COO independently
reached INERT (66521).

---

```json
[
 {
  "id": "D1_CATVIEWS-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C (executing seat, against its own ISSUER-authored criterion)",
  "surfaced_at": "2026-08-24T20:42Z",
  "one_line": "D1R1DE-AC1's named oracle (comp-transform schema-check ModelPortfolios) aborts at types-resolution on the one file this TO edits, so its 0-MISSING is a non-result that reads as a pass -- on the exact defect class (renders a field the response type does not carry) that this TO's new nested block is most likely to produce.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "comp-transform schema-check ModelPortfolios -> rc=1, single line '[WARN] types-resolution: no types.ts found near .../ModelPortfolios.tsx (searched co-located + 3 parent dirs + _shared/)'; MISSING count 0; the tool's own 'SCHEMA CHECK:' header is ABSENT, i.e. it aborted before checking",
    "POSITIVE CONTROL, the reason this is a finding: comp-transform schema-check Correlation -> rc=0 'All rendered fields match their response types'; comp-transform schema-check FactorTilts -> rc=0 and names a real gap ('getAUMMetrics() -> AUMFlowsWithMetricsResponse: type not found in types.ts'). The instrument discriminates; it has no domain on this page",
    "mechanism measured at source: portal/src/pages/ModelPortfolios.tsx is a flat single-file page with 4 inline type declarations and response types imported from @/api/endpoints/aum (MdpfPerFirmTimeSeries, MdpfFirmAUMMetrics); find portal/src -name types.ts -> 18 files, none co-located or within 3 parents of this page",
    "DESIGNED not accidental: no call shape creates a types.ts, so corroboration must come from outside the instrument's domain"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "DISCHARGED SAME TURN by the issuer, not open. Routed BLOCKING x INERT to 2.0.0_SA_COO as 66518; ruled 66521: AC1 amended in place -- declare the category_views response types in @/api/endpoints/aum (Build Ladder rung 2, existing estate pattern) and exercise bun run typecheck (AC9) ONCE with a mutant (render a field absent from the type -> typecheck FAILS -> remove) as the real discriminator; the comp-transform call stays on record run-with-its-domain-disclosed and is NOT deleted. Decomp untouched; cell_refs D1-c-1 unchanged; alignment denominators unchanged (8 cells / 9 criteria). Filed by the executing seat against the issuer's own criterion -- the direction the channel exists to permit."
 },
 {
  "id": "D1_CATVIEWS-S2",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C",
  "surfaced_at": "2026-08-24T20:42Z",
  "one_line": "Pre-existing React Query cache-key collision on this TO's edit surface: ['model-portfolio-benchmarks'] is shared by ModelPortfolios.tsx:533 and components/ModelPortfolioModal.tsx:114, both calling getModelPortfolioBenchmarks().",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "comp-cache collisions, run at startup as AC1's second limb: Key ['model-portfolio-benchmarks'] -> portal/src/components/ModelPortfolioModal.tsx:114 and portal/src/pages/ModelPortfolios.tsx:533, same accessor getModelPortfolioBenchmarks()",
    "benign shape: two call sites, one key, one accessor -- shared cache is the intended behaviour here, which is why this is recorded as a constraint and not as a defect"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "Logged because it is ON the edit surface and constrains this TO, not as a defect claim. Operative consequence, one line: category_views gets its own cache key when wired; no colliding key is added. COO concurred (66521): not mine to fix."
 },
 {
  "id": "D1_CATVIEWS-S3",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C",
  "surfaced_at": "2026-08-24T20:42Z",
  "one_line": "The portal ephemeral promote worktree .runtmp/portal-promote-20260824T124621Z is still registered at PROD a239e4a9 and portal local PROD is AHEAD of origin/PROD (a239e4a9 vs 8a96c916) -- a staged ref a promote run outside /prod-deploy would silently base on.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "git -C portal worktree list -> C:/.../portal d43b88c5 [DEV] AND C:/.../.runtmp/portal-promote-20260824T124621Z a239e4a9 [PROD]",
    "git -C portal rev-parse PROD origin/PROD -> a239e4a9023c8bc25c4d514735564f6a790a2a70 (local) vs 8a96c91654ed282acbed04da1e9f0074dca42332 (origin) -- local PROD ahead of remote",
    "INERT discriminator, stated not assumed: the hazard fires only on a promote action, and the disarm (/prod-deploy Step 3 update-ref + worktree prune) is a MANDATORY step of the very procedure that triggers it; the PROD push is separately held at Andrew's word",
    "this seat's cells are DEV-only (portal main tree confirmed on DEV) and nothing promote-adjacent is in flight here"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "DT lane's, not this seat's -- surfaced, no action taken, nothing chased. Recorded with both hashes rather than as a startup impression because a promote run OUTSIDE /prod-deploy would base on the staged merge silently. COO independently reached INERT (66521) and is not acting on it either."
 },
 {
  "id": "D1_CATVIEWS-S4",
  "surfaced_by": "0.4.0_DS_ClientPlatform~F",
  "surfaced_at": "2026-08-24T21:01Z",
  "one_line": "A model's PRIMARY identity is carried by crosswalk model_key, never by its display label -- I read the label, reported 'Opal Conservative Growth' as an unregistered non-Primary model, and drove a COO ruling to register $34,585,361.39 of PRIMARY AUA as Custom. Caught at the keyboard before any write.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "0.4.0_DS_ClientPlatform~F -- DISARMED same turn: retraction to COO (66568, 210136Z), issuer re-ruled NO REGISTRATION (66572), r4 registration paused then resumed on the corrected basis, zero commits at any point. DISARMED, NOT REMEDIATED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "SURFACING SEAT DECLARED grounding.status='SOURCE-CONFIRMED' (a Rule 22 reserved word, correctly used and STRONGER than this schema's top value); re-encoded to GROUNDED by the channel owner because the schema has no such value -- the strength claim is preserved here, not discarded",
    "data/assets/scripts/gold/build_cottonwood_mdpf_slice.py:146 -- CANONICAL_KEY['Opal Conservative Growth'] = 'opal_long_term_conservative' (the Cottonwood builder itself)",
    "build_cottonwood_mdpf_slice.py:133-137 -- RULED Andrew-direct 2026-07-23 ~0215Z, PRD v1.23 @a41c582ba",
    "data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py:91 -- 'LTC = SmartX \"Opal Conservative Growth\" (NOT \"Long-Term Conservative\"); ... Key by id, never the label.'",
    "concurring independently: crosswalk:6, build_cottonwood_mdpf_pair.py:302, build_mdpf_process_backfill.py:103, mdpf_revamp_count_source_audit.py:80, aggregate_smartx_to_daily.py:40, aggregate_smartx_to_timeseries.py:69 -- 7 files, zero dissent",
    "the TRUE premise that produced the FALSE inference: BD 'Opal Conservative Growth' (0e632e04, Model, 109 acct) and BD 'Opal Long Term Conservative' (c973839d, Strategy, 0 acct) ARE distinct rows -- measured correctly, and it licenses nothing about which row carries the Primary identity"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "⛔ CHANNEL-OWNER ENCODING ACT (3.0.0_SA_CVO): the surfacing seat wrote disposition='DISARMED_PENDING_REMEDIATION' AND grounding.status='SOURCE-CONFIRMED'. NEITHER IS A VALUE IN THIS SCHEMA. Their intent is preserved verbatim (in disarm_owner, in the evidence row above, and below); I re-encoded the STATE onto the current axes and did not touch the finding. ⛔ BOTH COINAGES ARE EVIDENCE OF GAPS IN MY OWN SCHEMA -- filed as D1_CATVIEWS-S5. One seat, one first use, reached past TWO independent axes. || THE CLASS, which is why this is filed and not merely retracted: mdpf_category_registry's F5 duplicate guard keys on member_id, so a SECOND entry for the SAME REAL MODEL under a DIFFERENT id RAISES NOTHING. Every structural guard passes, self_test stays rc=0, and the only detector was reading the crosswalk. The direction of harm is the quiet one -- it moves a served client-facing number DOWN, out of Primary; build_cottonwood_mdpf_slice.py:137 records the mirror-image near-miss ('a name-hunch merge would move $31M on a guess -- it is now moved on a RULING, not a hunch'). REMEDIATION PROPOSED, NOT BUILT, NOT MINE TO BUILD (no-inferred-gates): a registry assert that every registered model member resolves to a distinct crosswalk model_key, or declares itself off-crosswalk with a reason -- so a same-model/different-id duplicate raises at import the way a same-id duplicate already does. Routed to COO/CTO as a proposal. Second-order note for the channel: the issuer retracted its own ruling on the executing seat's control (66572), which is the loop working, not a second defect."
 },
 {
  "id": "D1_CATVIEWS-S5",
  "surfaced_by": "3.0.0_SA_CVO (channel owner). ⛔ ATTRIBUTION CORRECTED: this record first credited the two coined values to 0.4.0_DE_ClientPlatform~C. THEY ARE 0.4.0_DS_ClientPlatform~F's, in item S4, which DS~F appended to DE~C's file at 21:06:25Z -- three minutes after DE~C's own accurate '3/3 VALID' report on S1-S3. Two seats, one file, neither able to commit it; I read the merged file and attributed all of it to the seat who had messaged me.",
  "surfaced_at": "2026-08-24T21:12Z",
  "one_line": "TWO axes of the investigation schema were reached past by one seat on first use: hazard_standing {ARMED, INERT} has no DISARMED-WITH-REMEDIATION-OPEN state (so a disarmed item renders byte-identical to one never armed -- the exact collapse DISARMED != REMEDIATED exists to prevent, reproduced inside the schema written to enforce it), and grounding.status {INFERRED, GROUNDED} cannot express SOURCE-CONFIRMED, which is a RESERVED WORD in CLAUDE.md Rule 22's own grounding vocabulary.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "0.4.0_DS_ClientPlatform~F wrote disposition='DISARMED_PENDING_REMEDIATION' for an item disarmed same-turn with remediation open",
    "the same seat (DS~F) wrote grounding.status='SOURCE-CONFIRMED' -- a Rule 22 RESERVED word, legal only on a source-confirmed claim, and their item is source-confirmed",
    "schemas/investigation_item.schema.json: hazard_standing enum ['ARMED','INERT']; grounding.status enum ['INFERRED','GROUNDED'] -- neither carries the state the seat correctly observed",
    "the disarmed state is expressible today ONLY as INERT + prose, which is what the channel owner did to make the document valid, and which loses the distinction on every machine read",
    "the loss is named verbatim in the session log that authored this schema: 'DISARMED != REMEDIATED -- two states, two owners, two clocks; a single terminal state converts dangerous-and-visible into safe-and-invisible'",
    "prior items at this seat (OPAL_KIMIPIPELINE-S1, NFRA_COMPRAIL-S1) encode the same state as GRADUATED + a prose note, i.e. an unenforced convention the schema does not know about",
    "CLAUDE.md Rule 22 defines a THREE-level grounding vocabulary (INFERRED / grounded / SOURCE-CONFIRMED as a reserved word); this schema implements two, so the strongest legal claim in the estate's own law cannot be recorded in the channel that adjudicates grounding",
    "ATTRIBUTION CONTROL, run only after the error: the file's own per-item surfaced_by fields read S1/S2/S3 = 0.4.0_DE_ClientPlatform~C, S4 = 0.4.0_DS_ClientPlatform~F. The in-band attribution was correct in the document the whole time and I did not read it before writing about it -- DS~F's own hand-off message even warned that 'per-entry attribution is in-band via surfaced_by, so the git author line will not be the provenance record'"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "disarm_owner": "3.0.0_SA_CVO (schema author + channel owner) -- DISARM (done this turn): both coinages and their re-encodings are stated on the face of the affected item, so no machine read is silently wrong and no seat's strength claim is lost. REMEDIATION (open, separate act, separate clock): a Rule-24 four-postulate record per axis.",
  "notes": "⛔ AND THE ATTRIBUTION ERROR IS ITSELF THE SAME CLASS AS THE FINDING. A shared append-only file carries N seats' work under ONE git author line, so the channel's provenance lives ONLY in the in-band surfaced_by field -- and the channel owner, filing on behalf of seats who cannot commit, is exactly the reader most likely to collapse it to whoever messaged them last. DS~F flagged this risk in their hand-off IN ADVANCE and I made the error anyway. Filing-on-behalf is now a two-step at this seat: read surfaced_by per item, THEN write. || DELIBERATELY NOT FIXED BY REFLEX. Adding a value to a ratified axis is precisely the schema-enumeration act Rule 24 binds (08-20 widening: authoring AND adopting AND proposing values), and doing it inside the round that found it would be the haste the postulate exists to catch. At least three candidate shapes for the standing axis (a DISARMED value; a separate disarm_state field; a remediation_ref pointer) and they do NOT move together under postulate (iv). The grounding axis is a separate act again -- aligning it to Rule 22's three levels is arguably ADOPTION of an existing ratified vocabulary rather than a mint, which is a lower bar but still an authoring event. TWO axes, two records, one owner: me."
 },
 {
  "id": "D1_CATVIEWS-S6",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C -- read off their OWN render, then measured; surfaced by MCP per the COO ruling (executing seats do not write this tree)",
  "surfaced_at": "2026-08-25T01:09Z",
  "one_line": "The L2 Custom Models panel prints a REGISTRY-grain property (served) immediately beside a FIRM-grain dollar figure -- Inflection shows $43,484,499.68 of Custom AUM with 0 of 3 members served=true -- and a reader reaches one of two conclusions that are BOTH wrong.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured from the block at ref 23271aac64 (the seat cited its ref, per the standing evidence rule)",
    "panel renders together: Custom $43,484,499.68 / Opal Global All Equity Total Return NOT SERVED / 50-50 INT-LTC NOT SERVED / 50-50 ST-INT NOT SERVED",
    "0 of 3 Custom members carry served=true against $43,484,499.68 of Custom AUM",
    "`served` is a REGISTRY property -- whether the model is served as a product artifact -- and NOT a statement about whether this firm holds it"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE CLASS IS A GRAIN MISMATCH AT THE RENDER, and it is the same family as tonight's issuer defects one plane over: every value on the panel is TRUE, and the ADJACENCY manufactures a claim none of them makes. A reader concludes either '$43.5M of client money sits in models we do not serve' or 'the member list does not account for the money' -- and the real explanation is NEITHER, because the two figures are at different grains. Rule 24(ii) at the presentation layer rather than at a schema: two grains rendered on one axis. || WHY IT IS INERT AND NOT ARMED: nothing degrades while it stands and no act is pending -- the harm is a reader's inference, and the surfacing seat caught it by READING THEIR OWN RENDER rather than by trusting the values they had just verified individually. That is the frontend analogue of premise-verification, and it is the FIFTH time tonight an executing seat found something no document-plane check could see. || The seat proposes a label change on their own panel and chased nothing further, which is the correct scope: a grain mismatch is fixed by disclosing the grain (naming `served` as a registry property at the point of render), not by suppressing a true value. CERTIFIER NOTE: this touches D1-h-v3 (the L2 Custom drill) but is NOT a decomp defect -- the cell is enumerated and its oracle runnable; what the panel MEANS to a reader is a render-quality property no alignment or viability check reaches."
 },
 {
  "id": "D1_CATVIEWS-S7",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C, self-scanning their OWN task order on the issuer's ask -- reported, not fixed; denominator stated first and severity graded",
  "surfaced_at": "2026-08-25T01:49Z",
  "one_line": "TO-R1-DE CONTRADICTS ITSELF about the D1-h-v4 unavailable case -- the cell description at :70 says '(Inflection today)' while AC5 at :87 in the SAME FILE says Inflection is NOT the unavailable case and ZERO firms exercise it -- because the issuer amendment landed on the ACCEPTANCE ROW and not on the CELL DESCRIPTION.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DENOMINATOR STATED FIRST: 6 checkable factual claims in the TO; 2 are instances, 4 verified TRUE (members_for('Models > Custom') exists; O-4's view-plane flag premise holds with view_plane.excluded = ['Insurance']; the comp-cache collision sites are exactly as the tool reported; the 2,471-line count was true at issuance)",
    "INSTANCE 1 (HIGH): TO-R1-DE:70 cell description says predicate unavailable '(Inflection today)'; TO-R1-DE:87 AC5 says 'Inflection is NOT the unavailable case -- it carries a live account-grain predicate (is_fee_earning, 911 accounts), so ZERO firms exercise this today'",
    "INSTANCE 2 (MEDIUM): the tree table at :61 lists SMA nodes as 'Tax / Muni / DIVZ / PFOE' -- those are the STRATEGY IDS; the emitted block at ref 23271aac64 carries display_names 'Dividend SMA' / 'Opal Equity Growth SMA' / 'Muni SMA' / 'Tax-Managed SMA'",
    "the seat rendered display_name and got it right BECAUSE the same sentence carries its own antidote ('render whatever the block carries'), not despite the list"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE GRADE IS ABOUT WHICH HALF IS STALE, NOT THAT ONE IS -- and that reasoning is the reusable part: 'the Cells section is where a seat goes for WHAT TO BUILD, the acceptance table is where it goes for HOW IT IS JUDGED.' A seat reading only the Cells section builds an Inflection fixture for a firm that is not the case. The surfacing seat read both and used the amended one, and named that as LUCK OF READING ORDER, NOT A CONTROL. || A DISTINCT SUB-SHAPE OF THE S10 CLASS, worth separating: this value WAS sourced and then FALSIFIED, where S10's instances were never sourced at all. Same failure mode -- a plausible specific value sitting in a spec with nothing marking it dead -- but the remedy differs: S10's is 'do not write example values', this one is 'AN AMENDMENT MUST LAND ON EVERY SURFACE THAT CARRIES THE CLAIM, NOT ONLY ON THE ROW THAT PROMPTED IT'. Issuer's act. || INSTANCE 2 GRADED MEDIUM FOR A NAMED REASON rather than by feel: the sentence carries its own antidote and removing seven words would make it HIGH. Grading by what the text DOES rather than by how wrong it looks. || SEE ALSO ADVI_PERFRP-S10: the same class, four instances, other project, also found by executing seats reading their own TOs. FIVE lanes have now self-scanned and every one found something; NO instance in this class was found by a certifier."
 },
 {
  "id": "D1_CATVIEWS-S8",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C, against code they had ALREADY SHIPPED, on a ruling withdrawn after they built to it",
  "surfaced_at": "2026-08-25T02:19Z",
  "one_line": "Shipped renderer HARDCODES a withdrawn ruling: aum.ts:776 returns 'absent_by_scope' for global WITHOUT FETCHING, so if category-views is ruled all-scope the accessor never requests it and the panel renders a CONFIDENT, REASONED EXPLANATION of why no global tree exists -- forever, and correctly-looking.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "portal/src/api/endpoints/aum.ts:776 -- if (firmId === 'global') { return { status: 'absent_by_scope', scope: firmId } } : RETURNS WITHOUT FETCHING",
    "the withdrawn ruling (66633) is what that branch encodes; the withdrawal's own load-bearing consequence was stated as 'a field whose EMPTINESS carried meaning cannot quietly start carrying an object'",
    "if CTO rules category-views ALL-SCOPE and a global object is emitted, the accessor never requests it and the panel renders 'The category view tree is per-firm. Select a partner to see it.' plus a reasoned explanation that no global tree is published"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DE_ClientPlatform~C for the code branch, COUPLED to 1.0.0_SA_CTO's pending all-scope ruling -- the disarm is that THE RULING MUST NOT LAND WITHOUT THIS BRANCH BEING KNOWN, since the ruling is the trigger",
  "notes": "⛔ WHY ARMED RATHER THAN A STALE BRANCH: the failure is not a blank panel. THE PANEL ASSERTS A DELIBERATE DESIGN DECISION, WITH A REASON, IN CONFIDENT PROSE. The surfacing seat's own framing is the finding and it generalises past this file: 'A REVIEWER SEEING A BLANK PANEL ASKS WHY; A REVIEWER SEEING A CONSIDERED EXPLANATION OF WHY THERE IS NO GLOBAL TREE DOES NOT.' Correct-looking beats generic -- an articulate wrong answer suppresses the question a crude one invites. || THE SHAPE IS A RULING FOSSILISED IN CODE: the branch was CORRECT when written, the ruling behind it was withdrawn, and NOTHING IN THE CODE RECORDS THAT ITS PREMISE IS NOW PENDING. A withdrawn ruling does not un-write the code built to it, and code built to a ruling does not announce which ruling it encodes. || Surfaced by the seat AGAINST THEIR OWN SHIPPED WORK, unprompted, after the ruling that justified it was withdrawn -- the second time tonight a seat has audited their own delivered code against a decision that moved under it."
 }
]
```
