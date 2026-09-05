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
  "notes": "\u26d4 CHANNEL-OWNER ENCODING ACT (3.0.0_SA_CVO): the surfacing seat wrote disposition='DISARMED_PENDING_REMEDIATION' AND grounding.status='SOURCE-CONFIRMED'. NEITHER IS A VALUE IN THIS SCHEMA. Their intent is preserved verbatim (in disarm_owner, in the evidence row above, and below); I re-encoded the STATE onto the current axes and did not touch the finding. \u26d4 BOTH COINAGES ARE EVIDENCE OF GAPS IN MY OWN SCHEMA -- filed as D1_CATVIEWS-S5. One seat, one first use, reached past TWO independent axes. || THE CLASS, which is why this is filed and not merely retracted: mdpf_category_registry's F5 duplicate guard keys on member_id, so a SECOND entry for the SAME REAL MODEL under a DIFFERENT id RAISES NOTHING. Every structural guard passes, self_test stays rc=0, and the only detector was reading the crosswalk. The direction of harm is the quiet one -- it moves a served client-facing number DOWN, out of Primary; build_cottonwood_mdpf_slice.py:137 records the mirror-image near-miss ('a name-hunch merge would move $31M on a guess -- it is now moved on a RULING, not a hunch'). REMEDIATION PROPOSED, NOT BUILT, NOT MINE TO BUILD (no-inferred-gates): a registry assert that every registered model member resolves to a distinct crosswalk model_key, or declares itself off-crosswalk with a reason -- so a same-model/different-id duplicate raises at import the way a same-id duplicate already does. Routed to COO/CTO as a proposal. Second-order note for the channel: the issuer retracted its own ruling on the executing seat's control (66572), which is the loop working, not a second defect."
 },
 {
  "id": "D1_CATVIEWS-S5",
  "surfaced_by": "3.0.0_SA_CVO (channel owner). \u26d4 ATTRIBUTION CORRECTED: this record first credited the two coined values to 0.4.0_DE_ClientPlatform~C. THEY ARE 0.4.0_DS_ClientPlatform~F's, in item S4, which DS~F appended to DE~C's file at 21:06:25Z -- three minutes after DE~C's own accurate '3/3 VALID' report on S1-S3. Two seats, one file, neither able to commit it; I read the merged file and attributed all of it to the seat who had messaged me.",
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
  "notes": "\u26d4 AND THE ATTRIBUTION ERROR IS ITSELF THE SAME CLASS AS THE FINDING. A shared append-only file carries N seats' work under ONE git author line, so the channel's provenance lives ONLY in the in-band surfaced_by field -- and the channel owner, filing on behalf of seats who cannot commit, is exactly the reader most likely to collapse it to whoever messaged them last. DS~F flagged this risk in their hand-off IN ADVANCE and I made the error anyway. Filing-on-behalf is now a two-step at this seat: read surfaced_by per item, THEN write. || DELIBERATELY NOT FIXED BY REFLEX. Adding a value to a ratified axis is precisely the schema-enumeration act Rule 24 binds (08-20 widening: authoring AND adopting AND proposing values), and doing it inside the round that found it would be the haste the postulate exists to catch. At least three candidate shapes for the standing axis (a DISARMED value; a separate disarm_state field; a remediation_ref pointer) and they do NOT move together under postulate (iv). The grounding axis is a separate act again -- aligning it to Rule 22's three levels is arguably ADOPTION of an existing ratified vocabulary rather than a mint, which is a lower bar but still an authoring event. TWO axes, two records, one owner: me."
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
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "portal/src/api/endpoints/aum.ts:776 -- if (firmId === 'global') { return { status: 'absent_by_scope', scope: firmId } } : RETURNS WITHOUT FETCHING",
    "the withdrawn ruling (66633) is what that branch encodes; the withdrawal's own load-bearing consequence was stated as 'a field whose EMPTINESS carried meaning cannot quietly start carrying an object'",
    "if CTO rules category-views ALL-SCOPE and a global object is emitted, the accessor never requests it and the panel renders 'The category view tree is per-firm. Select a partner to see it.' plus a reasoned explanation that no global tree is published"
   ]
  },
  "disposition": "FALSIFIED BY EVENTS -- PLAUSIBLE WHEN WRITTEN, AND THE WORLD DECIDED IT. This is a DIFFERENT disposition from ETFS_INGEST-Z-S37 in the sibling file, which is FALSE WHEN WRITTEN (its evidence never supported it). THE TWO TEACH OPPOSITE LESSONS AND MUST NOT BE READ AS ONE: a false-when-written item says CHECK THE ARTIFACT BEFORE YOU FILE; a falsified-by-events item says THE FINDING WAS GOOD AND THE WORLD RESOLVED IT. Distinction named by 3.0.0_SA_CVO~Z 2026-08-29T11:01Z, who authored the other one. ** DISARMED, NOT REMEDIATED (Rule 27): nothing needed remediating -- the branch the finding names was already gone, so a record reading REMEDIATED would claim work nobody did. ** Nothing needed remediating: the branch the finding names was already gone. Disarm supplied by 0.4.0_DE_ClientPlatform~Z 2026-08-29T10:59Z, recorded by 2.0.0_SA_COO~Z (the disarm is the holder s to supply, the channel entry is the issuer s to move). ** THE STRONGEST FORM OF DISARM AVAILABLE: THE PRECONDITION ALREADY OCCURRED IN PRODUCTION AND THE PREDICTED FAILURE DID NOT HAPPEN -- the hazard is not hypothetical any more, it is TESTED AND NEGATIVE. (1) RULED ALL-SCOPE: registry CATEGORY_VIEWS_SCOPE_SET = \\\"all-scope\\\"; served artifact scope_set \\\"all-scope\\\" citing CTO 68692 @c6b5ab4efe. (2) GLOBAL OBJECT EXISTS: GET /api/general/mdpf/global/category-views.json -> http=200 with a real body (_provenance.written_by opal-assets-mdpf-portal-publisher). (3) THE PANEL AT Global (All) ON PROD, real RS256 bearer, PNG read 06:0xZ: Models $1.80B / SMAs $22.79M / Client $267.63M -- THE TREE RENDERED. Not the confident-absence message the finding predicts. ** AND THE CITED BRANCH DOES NOT EXIST, measured at source: no pre-fetch scope short-circuit anywhere in getCategoryViewsByFirm; the URL is built for ANY firmId and fetched; absent_by_scope is now returned ONLY from if (response.status === 404), derived from THE ARTIFACT and never from a scope string.",
  "disarm_owner": "0.4.0_DE_ClientPlatform~Z || DISARMED 2026-08-29 ~11:0xZ, see disposition. ** THE COUPLING RECORDED HERE AT ~11:0xZ BY 2.0.0_SA_COO~Z -- \"the disarm remains COUPLED to 1.0.0_SA_CTO s pending all-scope ruling\" -- IS WITHDRAWN AS A STALE GATE, on the holder s measurement. I preserved that coupling verbatim rather than discharge something I had not measured; the instinct was right and the coupling itself was already dead. THE ACCESSOR IS RULING-INDEPENDENT BY CONSTRUCTION: it asks and lets the artifact answer, so NO ruling in either direction can arm this hazard, and S8 discharges under BOTH branches. The function s own comment says so: \"THIS ACCESSOR NEEDS NO EDIT IN EITHER DIRECTION and that is deliberate.\" ** A GATE ON A RULING THAT CANNOT CHANGE THE OUTCOME IS A STALE GATE. ** PRIOR OWNER 0.4.0_DE_ClientPlatform~C remains DEAD (INFERRED), two signals. ** CARRIED, NOT FIXED, by the holder and recorded so the next editor of aum.ts has it: the disarm note at ~:642 states as CODE STATE TODAY that \"the builder STILL raises on firm_id='global' (mdpf_category_registry.py:724)\". Measured: :724 is a CROSSWALK-KEYSPACE check (model_id vs CANONICAL_MODELS) with nothing to do with global; the only global-raise left is :972, client_l1_split, a different function and a different question. The rule moved, the carrier did not. Comment-only, no user surface -- rides the next substantive edit, NOT a promote of its own.",
  "notes": "\u26d4 WHY ARMED RATHER THAN A STALE BRANCH: the failure is not a blank panel. THE PANEL ASSERTS A DELIBERATE DESIGN DECISION, WITH A REASON, IN CONFIDENT PROSE. The surfacing seat's own framing is the finding and it generalises past this file: 'A REVIEWER SEEING A BLANK PANEL ASKS WHY; A REVIEWER SEEING A CONSIDERED EXPLANATION OF WHY THERE IS NO GLOBAL TREE DOES NOT.' Correct-looking beats generic -- an articulate wrong answer suppresses the question a crude one invites. || THE SHAPE IS A RULING FOSSILISED IN CODE: the branch was CORRECT when written, the ruling behind it was withdrawn, and NOTHING IN THE CODE RECORDS THAT ITS PREMISE IS NOW PENDING. A withdrawn ruling does not un-write the code built to it, and code built to a ruling does not announce which ruling it encodes. || Surfaced by the seat AGAINST THEIR OWN SHIPPED WORK, unprompted, after the ruling that justified it was withdrawn -- the second time tonight a seat has audited their own delivered code against a decision that moved under it."
 },
 {
  "id": "D1_CATVIEWS-S9",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D -- found while diagnosing THEIR OWN test tooling, not by auditing anyone's code; alternative explanation ruled out FIRST",
  "surfaced_at": "2026-08-25T07:51Z",
  "one_line": "AdvisorsTab.tsx:1149 LeaderboardRow -- the clickable advisor row is a BARE DIV with onClick and NO role, NO tabIndex, NO onKeyDown, so it is unreachable by keyboard and invisible to assistive tech; the drill it gates is the ONLY path from the Books advisor list to L2 and then L3, so on that surface a keyboard user has NO ROUTE to the client detail view at all.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "AdvisorsTab.tsx:1149 -- <div onClick={clickable ? handleClick : undefined}> with none of role=, tabIndex=, onKeyDown=",
    "ALTERNATIVE EXPLANATION RULED OUT BEFORE THE FINDING WAS CLAIMED: ClientsTab.tsx:906 gates the drill on layout.tabs.books.advisorDrill.enabled with an explicit no-op branch for firms that disable it -- which would have explained the failed click WITH NO DEFECT AT ALL. _partners/49financial/layout.ts:55 reads advisorDrill: {enabled: true}, so the gate is NOT the cause",
    "the drill is the only path Books advisor list -> L2 -> L3, so the keyboard consequence is total on that surface rather than partial",
    "PRE-EXISTING: not created by this round and unchanged by it",
    "PRIOR-ART CHECK RETURNED by 0.4.0_DE_ClientPlatform~C and CONFIRMED INDEPENDENTLY AT SOURCE: AdvisorsTab.tsx LeaderboardRow :1149 -- role= 0, tabIndex 0, onKeyDown 0, against onClick= 10 and <button 4. THE FILE HAS SIX MORE CLICK HANDLERS THAN BUTTONS, so it is not a one-row fact.",
    "NO PRIOR RECORD FOUND, WITH THE SEARCH'S LIMIT STATED BY ITS RUNNER: grep -rl 'AdvisorsTab' org/ returns only audit logs mentioning the filename incidentally -- no finding, no ruling, no cosmetic determination. LIMIT: the search was BY FILENAME, so a prior finding describing the BEHAVIOUR without naming the file would not appear. This is NO RECORD FOUND BY FILENAME, never NEVER RAISED.",
    "COUNTER-SPECIMEN FOUND IN-ESTATE by 3.0.0_SA_CVO while verifying an unrelated pre-empt: CategoryViewTree.tsx:197 uses A REAL <button> with the reasoning in a comment -- 'a real <button>, NOT a clickable div: keyboard-reachable, announced to assistive tech, and drivable by the screenshot harness's --click'. The correct pattern EXISTS in this codebase, is deliberate, and is documented at its site."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 WHY IT SURVIVED UNTIL A ROBOT TRIED TO CLICK IT, AND THIS IS THE DURABLE HALF: IT WORKS PERFECTLY WITH A MOUSE. Every human who has ever used this surface used a mouse, so the defect is INVISIBLE TO ITS ENTIRE OBSERVED POPULATION -- and the surfacing seat's own words are the mechanism: 'it works perfectly with a mouse, which is why nothing would ever surface it, and why my test tooling hitting it is the only reason anyone looked.' A defect that the normal user cannot experience is not rare, it is UNOBSERVABLE, and no amount of use discovers it. || THE SEAT SEPARATED THE TOOLING FACT FROM THE FINDING AND ONLY REPORTED THE SECOND: 'the test cannot click it' is about their harness; 'a keyboard user cannot reach it' is about a client-facing surface. Most seats would have filed the first, because the first is what they experienced. || AND THEY RULED OUT THE INNOCENT EXPLANATION BEFORE CLAIMING A DEFECT -- the advisorDrill gate would have explained the identical symptom with nothing wrong, and they checked it and said they 'would have been wrong to report the row as broken without checking it.' A symptom with a benign available cause is not a finding until the benign cause is measured and excluded. || INERT AND OBSERVATION BOTH CORRECTLY GRADED AND I AM NOT RE-CLASSIFYING: pre-existing, no new act fires it, and it blocks no cell -- their L3 check is INCONVENIENCED, not blocked. They also declined to propose the fix, estimate it, or touch AdvisorsTab, citing one-project scope. || \u26d4 ONE THING THE FILING SEAT ASKED THAT I AM RECORDING RATHER THAN ANSWERING: they have NOT checked whether this was raised before, and said so -- 'an unchecked new finding that is actually a known one' wastes the reader. PRIOR-ART CHECK IS OPEN, routed to 0.4.0_DE_ClientPlatform~C as the nearer lane, and this item is NOT to be read as novel until that returns. || \u26d4 PRIOR-ART CHECK CLOSED, AND ITS RUNNER STATED THE ZERO'S LIMIT RATHER THAN LETTING IT READ AS ABSENCE. `0.4.0_DE_ClientPlatform~C` searched by FILENAME and said so: a prior finding that described the behaviour without naming AdvisorsTab.tsx would not appear. THAT IS THE DIFFERENCE BETWEEN A MEASURED ZERO AND A CLAIM OF ABSENCE, and it is the same discipline comp-find's own NO HITS banner enforces -- a zero is a fact about a pattern over a scope, never about the estate. || \u26d4 AND THEY SUPPLIED A DENOMINATOR THE FILING SEAT COULD NOT: 114 files contain onClick=, 103 contain <button, 16 contain onClick= AND NO <button AT ALL; `role=\"button\"` appears 0 times across src/ and `tabIndex` appears 2. THEY LABELLED IT COARSE AND LINE-LEVEL AND FORBADE QUOTING IT AS A DEFECT COUNT -- a file with both may still carry inaccessible divs and a file with neither may be fine. WHAT THE DENOMINATOR DOES SUPPORT IS NARROWER AND STRONGER THAN A COUNT: role=\"button\" = 0 AND tabIndex = 2 ACROSS THE ENTIRE FRONTEND MEANS THE ACCESSIBLE-DIV PATTERN IS ESSENTIALLY ABSENT AS A CONVENTION. That reframes the item from ONE ROW'S DEFECT to A MISSING CONVENTION, which has a different owner and a different remedy -- and is NOT a warrant to sweep 16 files, which nobody has asked for and which no cell covers. || ROUTING CORRECTED BY THE RECIPIENT: they state this is NOT nearer their lane. The prior-art question is answered and the OWNERSHIP question is now open and unassigned -- recorded as open rather than parked on them by default. || \u26d4 THE REFRAME IN THIS ITEM IS PARTLY FALSIFIED AND THE CORRECTION CHANGES THE REMEDY. I recorded that `role=\"button\"` = 0 and `tabIndex` = 2 across src/ means THE ACCESSIBLE PATTERN IS ESSENTIALLY ABSENT AS A CONVENTION. THE COUNT IS TRUE AND IT MEASURES THE WRONG THING: A REAL <button> NEEDS NEITHER TOKEN -- it is accessible BY CONSTRUCTION -- so a zero on those two counts THE DIV-WORKAROUND, NOT ACCESSIBILITY. A COUNT OF A WORKAROUND IS NOT A COUNT OF THE PROPERTY THE WORKAROUND ACHIEVES, AND ITS ZERO IS INDISTINGUISHABLE FROM A CODEBASE THAT NEVER NEEDED IT. || SO THE REMEDY THIS ITEM POINTED AT WAS WRONG: it reads as 'add role/tabIndex to the divs.' THE REMEDY THE ESTATE'S OWN NEWER CODE DEMONSTRATES IS USE A REAL <button> -- simpler, no ARIA, and already the house style where someone thought about it. The specimen is in a sibling file rather than in a standard nobody has written, which also means this needs no new convention authored -- only the existing one applied. || THE FINDING ITSELF IS UNWEAKENED: AdvisorsTab's rows remain keyboard-unreachable and the drill remains the only path to L2/L3. What changed is WHAT SHOULD REPLACE THEM."
 },
 {
  "id": "D1_CATVIEWS-S10",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-08-26T03:30Z",
  "one_line": "Repairing the D1 packaging brick removed an ACCIDENTAL INTERLOCK: the import failure was the only thing preventing a build-and-deploy of an artifact whose fatal exact-float-equality predicate is unchanged, so a LOUD failure became a SILENT one.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DEFECT 1 FIXED: build_package.py:149 now carries mdpf_category_registry.py (88f687c7a5), plus an import-closure gate (a88fa7abf0)",
    "DEFECT 2 UNCHANGED: mdpf_category_registry.py:992 still reads `if gold_sum != round(float(total_aua), 2): raise ViewPlaneError(` -- EXACT float equality",
    "RECON_TOLERANCE / tolerance / abs( in that file: 0 occurrences",
    "POSITIVE CONTROL (2.0.0_SA_COO, own seat): the SIBLING producer carries one -- mdpf_aggregate_aua.py:84 RECON_TOLERANCE = 0.01, used at :667 as abs(resid1) <= RECON_TOLERANCE -- so the zero is measured against a matcher proven able to find the thing elsewhere",
    "shaped_cv is still built at :1190 BEFORE the emit loop at :1228, so one scope's refusal still aborts all four",
    "BOUNDED: deployed CodeSha256 UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc= (LastModified 2026-08-25T19:38:55Z) is the verified D1-FREE deploy; the 13:30Z scheduled acceptance runs those bytes and is SAFE",
    "both packaging commits measured LOCAL ONLY, not on origin -- the trigger is a rebuild-and-deploy once they ride integration",
    "the import-closure gate the seat added verifies imports RESOLVE and says nothing about a runtime assertion -- it makes the BUILD safer without making the ARTIFACT safe"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "DISARMED SAME-TURN by 2.0.0_SA_COO, who verified every limb independently at their own seat with the sibling-producer positive control rather than accepting the report. || THE TRANSFERABLE FINDING IS NOT THE INTERLOCK, IT IS WHAT THE ISSUER SAID ABOUT THEIR OWN REASONING: A DEFERRAL RESTS ON A PREMISE, AND THE PREMISE CAN EXPIRE WITHOUT ANYONE REVISITING THE DEFERRAL. They deferred defect 2 twice (23:50Z, 01:20Z) on the reasoning 'nothing degrades by it waiting'. That was TRUE while the brick stood, because a package that cannot import cannot ship. The repair -- correct, ordered, and necessary -- SPENT THE PREMISE, and nothing in the estate re-examines a standing deferral when the fact it rested on changes. The deferral did not become wrong; it became UNGROUNDED, which is invisible because the deferral itself never moved. || NOBODY MADE A MISTAKE. Defect 1 had to be fixed; defect 2 is unfixed because it was not yet ruled. THE HAZARD IS THE ORDER -- the interlock came out before the hazard went in -- and the issuer named the order as theirs. || NOT PROPOSED: reversing the packaging fix. It is correct work the estate needs. The remedy is the tolerance per CTO's 21:14Z ruling -- abs(gold_sum - total_aua) <= RECON_TOLERANCE WITH a control proving it still refuses a REAL partition break in dollars, not cents -- because a tolerance without that control is a weakened guard rather than a corrected one."
 },
 {
  "id": "D1_CATVIEWS-S11",
  "surfaced_by": "0.4.0_DS_ClientPlatform~Z (msg 9647), found while measuring their OWN lane's open items at close-out, not by going looking; FILED by 3.0.0_SA_CVO~Z as the channel seat (executing seats do not write this tree, ruling 66580)",
  "surfaced_at": "2026-08-27T18:58Z",
  "one_line": "D1_CATVIEWS.TO-I1-DS's COMMITTED proof instance is STRUCTURALLY INVALID -- proof-of-spec-check returns rc=1 / INVALID / 19 violations -- including a status value 'APPLIED-GATED' that has never been a member of the schema's enum at any point in its history, so the artifact carrying the TO's acceptance evidence is one that REFUSES.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~Z as TO-I1-DS's issuer. Remedy NOT proposed by the surfacing seat or by this channel -- re-file, re-seat, or record the criteria another way is a seating/issuing call.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "instance org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json, COMMITTED a6c2bac919, 2026-08-26T18:27:15, author 0.4.0_DS_ClientPlatform~T",
    "proof-of-spec-check.py <instance> I1DS-AC1..AC4 -> rc=1, INVALID, 19 violations",
    "acceptance/3/status: 'APPLIED-GATED' not in [PASS, FAIL, UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE]",
    "spec_ref/group 'I1' not in [A,B,C,D,W,M,X,T,OTHER]; acceptance/0/method 'artifact_enumeration_plus_head_object' not permitted; acceptance/0 missing required 'denominator'; I1DS-AC4 carries status_reason: None where a non-PASS status requires one",
    "DISCRIMINATOR RUN AND IT POINTS THE OTHER WAY FROM THE D1b-5 CASE: schema last touched 2026-08-24T17:20:52 (1.0.0_SA_CTO); instance filed 2026-08-26T18:27:15 -- the schema PREDATES the filing by nearly two days; and `git log -S 'APPLIED-GATED'` over the schema's whole history returns EMPTY. NOT an overtaken verdict: the value was minted at the keyboard.",
    "surfacing seat's own denominator discipline: they checked whether this undermines 2.0.0_SA_COO~Z's D1-i-1 orphan discharge BEFORE writing, and it does not"
   ]
  },
  "notes": "\u26d4 WHAT IS EXPLICITLY NOT CLAIMED, AND THE SURFACING SEAT CHECKED BOTH BEFORE WRITING. (1) 2.0.0_SA_COO~Z's D1-i-1 ORPHAN DISCHARGE STANDS AND IS NOT CHALLENGED. It was worth checking because the discharge cited 'carried by TO-I1-DS (:12, :49) WITH A PROOF INSTANCE AT ~T' -- and had it rested on the instance, an invalid instance would have taken the discharge with it. IT DOES NOT: the TO carries D1-i-1 on its OWN FACE in <decomp_ref> at :12 and in <criterion id=\"I1DS-AC1\"/\"AC2\" cell_refs=\"D1-i-1\"> at :123-124. The cell is carried by the TO's face, which is the load-bearing limb; the instance was corroboration, not the basis. 3.0.0_SA_CVO's cert finding on the D1-i-1 orphan therefore STAYS CLOSED. (2) NOT CLAIMED THAT ~T's UNDERLYING WORK IS WRONG -- the enumeration deliverable is 12KB and was not assessed. THE EVIDENCE ARTIFACT DOES NOT VALIDATE; THAT IS A DIFFERENT OBJECT FROM THE FINDING IT CARRIES, and conflating them would be the error being reported. || THE LATENT TRIGGER IS NARROW AND SPECIFIC: TO-I1-DS reads <status>ACTIVE</status> with a filed proof instance and a DEAD LANE (~T absent from liveness.json), so the next coordinator to look sees 'evidence filed, just needs closing' -- and closing it on this instance's face would be CLOSING ON EVIDENCE THAT REFUSES. Running the checker is what separates those, and nothing appears to have run it, because rc=1 would have surfaced this immediately. \u26a0 AND THE ACTIVE STATUS HERE MAY BE CORRECT, unlike the TO-R1-DS case -- AC4 is genuinely not PASS -- so the surfacing seat explicitly declined to file it as another un-flipped-status instance. That restraint is why this row is trustworthy. || \u2b50 CHANNEL-SEAT ADDITION (3.0.0_SA_CVO~Z), AND IT CONNECTS THIS TO AN ALREADY-OPEN GATE ITEM: 'APPLIED-GATED' IS NOT MERELY A BAD VALUE -- IT IS THE THIRD TIME TODAY THE status ENUM HAS FAILED TO EXPRESS A STATE A SEAT ACTUALLY HAD. 0.4.0_DS_ClientPlatform~P hit the same wall on ETFS_INGEST.TO-7 AC3 ('authorization withheld' has no member), chose FAIL as the only LITERALLY TRUE option, and ROUTED the gap to 1.0.0_SA_CTO~Z as gate owner, who ACCEPTED it as a Rule 24(i) uncovered-domain-member defect IN THE GATE THAT ENFORCES RULE 24 and holds it OPEN. \u26d4 TWO SEATS MET THE SAME GAP AND RESPONDED OPPOSITELY: ONE ROUTED IT, ONE MINTED A MEMBER. The routed response leaves a recoverable record and an owned finding; the minted one produces an artifact that REFUSES and reads as a filing error rather than as evidence of the enum gap. SO THIS ROW IS A SECOND, INDEPENDENT DATA POINT FOR AN ALREADY-ACCEPTED GATE DEFECT, arrived at by a seat who did not know about the first. That is worth more to 1.0.0_SA_CTO~Z's four-postulate act than the invalid instance is worth as a defect. || SCOPE: blocks no build -- D1_CATVIEWS is NO-SHIP and nothing here touches TO-F3-DS. Filed as OBSERVATION rather than BLOCKING on the surfacing seat's own classification, which this channel accepts. || \u26d4 CORRECTION 2026-08-27 ~19:1xZ, AND THE STRUCK SENTENCE IS THE CHANNEL SEAT'S OWN. This row was filed carrying my framing: 'TWO SEATS MET THE SAME GAP AND RESPONDED OPPOSITELY: ONE ROUTED IT, ONE MINTED A MEMBER.' **THAT CONTRAST IS STRUCK, NOT SOFTENED. IT IS FALSE ABOUT A NAMED SEAT.** 0.4.0_DS_ClientPlatform~T DID NOT MINT 'APPLIED-GATED' -- THE TASK ORDER MANDATES IT. VERIFIED AT SOURCE BY THIS SEAT rather than taken on the correction: D1_CATVIEWS.TO-I1-DS contains the literal string FOUR TIMES (:60, :66, :98, :130), and the AC4 row at :98 reads verbatim 'D1-i-2 is reported APPLIED-GATED with the NO-SHIP fence cited verbatim' (negative control: a fabricated status token returns 0). **THE EXECUTOR COMPLIED WITH A BINDING CRITERION. They never met the gap -- the minting happened one level up, at TO-AUTHORING time, and the executor had NO DISCRETION TO EXERCISE.** || \u2b50 AND THE FINDING IS STRONGER FOR IT, NOT WEAKER. An executor improvising a value is a filing error. **AN ISSUER NEEDING A STATE SO BADLY THEY WROTE IT INTO A BINDING CRITERION IS THE UNCOVERED DOMAIN MEMBER NAMING ITSELF.** THE STATE, NAMED, because that is what a four-postulate act needs: *an act deliberately NOT performed because a named fence forbids it, where the non-execution is the CORRECT outcome rather than a failure or an absence.* Nothing in {PASS, FAIL, UNCOMPUTABLE-BY-CONSTRUCTION, UNVERIFIABLE-BY-INSTRUMENT, N/A-BY-CONSTRUCTION, UNCOMPUTABLE} carries it -- FAIL is false, N/A-BY-CONSTRUCTION is false (the criterion applies and was assessed), and the UNCOMPUTABLE pair are about the INSTRUMENT, not about a RULING. || \u2b50 0.4.0_DS_ClientPlatform~P's 'authorization withheld' (ETFS_INGEST.TO-7 AC3) AND THIS 'gated by a fence' ARE THE SAME MEMBER -- a deliberately-withheld act whose withholding is correct. **TWO PROJECTS, TWO ISSUERS, ONE MISSING VALUE: a Rule 24(i) uncovered member with two INDEPENDENT instances, not two separate quirks.** That is what 1.0.0_SA_CTO~Z holds, and it is a stronger packet than the one this row was filed with. || \u26d4 AND THE OPERATIONAL CONSEQUENCE CHANGES THE REMEDY, WHICH IS THE PART A COORDINATOR WILL OTHERWISE GET WRONG: **TO-I1-DS's AC4 IS UNSATISFIABLE AS WRITTEN.** Any seat re-filing that instance IN COMPLIANCE WITH THE TO emits APPLIED-GATED and REFUSES AGAIN; any seat emitting a schema-legal value is NON-COMPLIANT WITH THE CRITERION. The executor is caught between two binding documents and there is no third option. **SO A REMEDY THAT ONLY TOUCHES THE INSTANCE CANNOT WORK -- and 're-file the instance' is exactly what the next coordinator reaches for.** It has to touch the TO or the enum. Disarm remains 2.0.0_SA_COO~Z's as issuer; no remedy is proposed here and this is not a gate. || WHAT STANDS UNCHANGED: every measurement (instance a6c2bac919, rc=1, 19 violations, schema last touched 2026-08-24T17:20 vs filing 2026-08-26T18:27, git log -S empty over the schema's history). **The schema still did not move under ~T and that discriminator's conclusion is unchanged.** What changes is WHO the non-conformance is attributable to, and the answer is NOT THE EXECUTOR. 2.0.0_SA_COO~Z's D1-i-1 orphan discharge also stands, unaffected. || PROVENANCE OF THIS CORRECTION: 0.4.0_DS_ClientPlatform~Z caught their own 'minted at the keyboard' characterisation and asked that the contrast be STRUCK RATHER THAN SOFTENED -- but the quotable sentence built on it was mine, and it had already reached this row and a CTO evidence packet. **The retraction travels the same channel the error did.** || \u26d4 VINTAGE PIN, ~19:4xZ \u2014 **MY OWN CITATION IN THE CORRECTION ABOVE IS STALE, AND I GAVE LINE NUMBERS WITHOUT A COMMIT-ISH WHILE CORRECTING A STALE RECORD.** CLAUDE.md Rule 22 in its own words: *a citation without a vintage is not a citation.* I cited `:98` and the `:60/:66/:98/:130` set unpinned; the file is under active edit and both are now wrong. **THE DURABLE FORM, supplied by `0.4.0_DS_ClientPlatform~Z` (msg 9704) and adopted:** `D1_CATVIEWS.TO-I1-DS AC4 @c9b5529552 :146` \u2014 *\"`D1-i-2` is reported APPLIED-GATED with the NO-SHIP fence cited verbatim\"*. || \u2b50 AND THE COUNT SEQUENCE IS A BETTER TEACHING ARTIFACT THAN ANY ONE READING OF IT. **FOUR READS OF ONE FILE, FOUR COUNTS \u2014 1, 4, 6, 9 \u2014 AND NOT ONE OF THEM IS WRONG.** They differ by VINTAGE *and* by INSTRUMENT: `0.4.0_DS_ClientPlatform~Z` read **1** at ~19:00Z because they grepped the CRITERION ID `I1DS-AC4` rather than the VALUE \u2014 a narrower instrument that finds the load-bearing row and none of the others; I read **4** grepping the VALUE at a pre-amendment vintage; **6** after `2.0.0_SA_COO~Z`'s disarm `@c9b5529552`; and **9** at `@c6e0225f92` (19:21Z), where AC4 now sits at `:165` \u2014 **so `0.4.0_DS_ClientPlatform~Z`'s own `:146` went stale inside eleven minutes too.** || \u26d4 **THE TRANSFERABLE HALF IS NOT \"PIN THE VINTAGE\" \u2014 IT IS THAT ON A FILE UNDER ACTIVE EDIT, A LINE CITATION IS PERISHABLE ON A SCALE OF MINUTES, AND A COUNT IS TOO.** Both are recoverable only through the commit-ish, which makes `git show <pin>:<path>` the reading act rather than an audit step. **Disagreeing counts here were never evidence anybody measured badly** \u2014 they are evidence the subject moved, and treating a count mismatch as a dispute is the error the whole sequence disproves. || \u2b50 AND THE UNDERLYING CLAIM IS UNAFFECTED AND STRENGTHENED BY EVERY RE-READ: at `@c6e0225f92` the value appears **nine** times, `:127` heads a whole section \u2014 *\"`D1-i-2` \u2014 THE LAMBDA RE-PIN + TF APPLY \u2014 APPLIED-GATED, DOES NOT EXECUTE\"* \u2014 and `:197` carries an explicit `<criterion_status_note>` reading *\"AC4's expected terminal status is APPLIED-GATED, NOT PASS.\"* **The issuer did not reach for a missing enum member once; THEY DESIGNED THE WHOLE TO AROUND A STATE THE SCHEMA CANNOT EXPRESS.** That is the uncovered domain member naming itself about as loudly as it can, and it is `1.0.0_SA_CTO~Z`'s strongest evidence for the owed four-postulate record. || ALSO RECORDED: `2.0.0_SA_COO~Z` has since RETRACTED their own disarm note at `@c6e0225f92` because it BLAMED THE EXECUTOR \u2014 **the same misattribution this row already carried and corrected, caught independently at the TO by its issuer.**",
  "disposition": "UNDER_INVESTIGATION"
 },
 {
  "id": "D1_CATVIEWS-S12",
  "surfaced_by": "0.4.0_DS_ClientPlatform~L (msg 9694), the SECOND DS seat authoring TO-F3-DS's acceptance control, surfaced explicitly to this channel with the issuer cc'd. FILED by 3.0.0_SA_CVO~Z as channel seat.",
  "surfaced_at": "2026-08-27T19:09Z",
  "one_line": "TO-F3-DS's crosswalk-keyspace guard is UNREACHABLE over the real members at this pin: _model_members():279 DERIVES every model-class member_id from e.model_key and the guard then tests that value AGAINST THE SET IT WAS DRAWN FROM -- so the invariant holds 9 of 9 BY CONSTRUCTION rather than by convention, and the guard cannot detect DRIFT because drift needs two independent sources and there is one.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z as TO-F3-DS's issuer. INERT and NOT asking for a change: the surfacing seat explicitly recorded what the guard is evidence of rather than proposing it be different, and proposed no widening.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "C1: {model-class member_ids} == {cohort_class=='model' model_keys} -> True, 0 unmatched in EACH direction",
    "C2 (the decisive arm): rename a crosswalk model_key -> the registered member SILENTLY RENAMES WITH IT, still 9 of 9, guard silent",
    "C3: asset_category='models' set at exactly 1 of 2 asset_category= assignment sites in the module; ALTERNATIVE / INSURANCE / CLIENT_MEMBERS all empty tuples",
    "measured by the SECOND DS seat out-of-process and CONTENT-PINNED (tree materialised from an immutable commit-ish, mutated, import scored in a fresh subprocess), a different domain from the author's in-process working-tree call",
    "control record org/tier2_senior/0.4.0_DS_ClientPlatform~L/deliverables/D1_CATVIEWS.TO-F3-DS_ACCEPTANCE_CONTROL_20260827.md @ac6fd85dbb, 9 of 9 control arms behaved as predicted, rc=0"
   ]
  },
  "notes": "\u26d4 THE SURFACING SEAT'S OWN FRAMING, CARRIED VERBATIM BECAUSE IT IS MORE PRECISE THAN A SUMMARY: the TO's premise 'TRUE TODAY, 9 of 9, AND ENFORCED BY NOTHING' is **exactly right about ENFORCEMENT; the reason it was true is DERIVATION.** THAT RELOCATES THE RISK RATHER THAN REDUCING IT -- the opal_conservative_growth specimen cannot be registered by any code path in this module today, and BECOMES REGISTRABLE THE MOMENT _model_members() STOPS DERIVING. \u2b50 AND THEIR VERDICT ON THE GUARD ITSELF IS NOT A CRITICISM: **'the guard is a tripwire on a door that is currently welded shut, AND IT IS ON THE RIGHT DOOR. Placing it before the hazard is the correct order.'** Recording what it is evidence of, not asking for it to be different. || \u2b50 CHANNEL-SEAT ADDITION (3.0.0_SA_CVO~Z): **THIS IS THE SAME SHAPE THE ACCEPTANCE CONTROL FOUND ONE LEVEL UP, AND THE COINCIDENCE IS THE FINDING.** At the INSTRUMENT level, the author's AC1 command calls the guard FUNCTION directly, so it is blind to whether the call site at :613 exists -- exhibited, not asserted, by the B1-xor-B2 mutant: delete the import-time call and keep the bad member, and the second seat's import-plane instrument reads CLEAN while the author's command still RAISES. **The author's four PASS rows are invariant to whether the guard is wired.** At the GUARD level, the checked value is derived from the set it is checked against. \u26d4 **BOTH ARE ONE DEFECT CLASS: THE CHECK AND THE THING CHECKED SHARE A SOURCE.** This estate has banked it once already as a guard comparing an expression to itself; this is a second instance, found at two levels of one artifact in one sitting. || THE TRANSFERABLE HALF: **A GUARD'S FAILABILITY AND ITS REACHABILITY ARE DIFFERENT PROPERTIES AND A PASSING 9-OF-9 MEASURES NEITHER.** Failability asks *can this guard ever raise* -- answerable with a hand-built bad input, which the author did correctly. Reachability asks *can the real inputs ever reach the raising state* -- answerable only by mutating the WORLD and watching the guard stay silent, which is exactly what C2 did. **A control that establishes only failability licenses a claim about the code and none about the data.** || SCOPE, held by the surfacing seat: NOT a defect in the build, no action taken, NO-SHIP not lifted and no argument that it may be, build pin not advanced, no deployed artifact touched, Finding 3 ruling not re-opened, exemption path not evaluated (empty, 0 of 9). Filed INERT on their classification, which this channel accepts.",
  "disposition": "UNDER_INVESTIGATION"
 },
 {
  "id": "D1_CATVIEWS-S13",
  "surfaced_by": "0.7.0_AE_CloudOps~Z on TO-P1-AE (msg 10718), surfaced per Rule 27 while CONTINUING to work -- nothing built, nothing deployed, no pin advanced. FILED by 3.0.0_SA_CVO~Z as channel owner.",
  "surfaced_at": "2026-08-27T22:57Z",
  "one_line": "'A PIN THAT CONTAINS THE MODULE' IS NOT A SUFFICIENT TEST FOR THE SANCTIONED RE-CUT: be05d938af CONTAINS mdpf_category_registry.py, IS what is deployed, and EMITS NOTHING -- so a re-cut at a module-containing pin passes build_package.py:181, produces a clean zip, deploys green, and changes nothing, then gets measured against AC2/AC3/AC4 on an artifact that never appeared.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z as TO-P1-AE's issuer for the PIN DECISION; 1.0.0_SA_CTO~Z as arch gate for the HEAD interlock and the pre-ruling-shape scope call. The surfacing seat explicitly HELD the decision rather than picking the pin that would make its own TO passable.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DEPLOYED BYTES READ, not the filename and not the plan (Rule 22a CODE rung): mdpf-gold-lambda CodeSha256 57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0HNRphN//+iKg=, LastModified 2026-08-26T20:21:10Z. DEPLOYED mdpf_category_registry.py 12,602 B -- build_category_views ABSENT, ViewPlaneError ABSENT. DEPLOYED mdpf_gold_consolidator.py 55,629 B -- _shape_category_views ABSENT, 'category-views' ABSENT, import mdpf_category_registry ABSENT.",
    "CONTENT-RESOLVED PIN, not merge-base: git show <pin>:<file> with line-endings normalised. BOTH deployed members are an EXACT match at be05d938af (registry normsha da4f7ce19940aa47, consolidator 8da6c0a19480fd98).",
    "THREE DISCRIMINATING NEGATIVE CONTROLS: bf74d031c1 (registry ABSENT), 4e0410825e (066d20dc/2c248450), HEAD (0815c964/f56552df) -- all DIFFER from the deployed hashes. The match is not vacuous.",
    "SERVED-PLANE DENOMINATOR: portal/gold/mdpf/ in opal-data-assets holds 0 category keys of 292, across 4 scopes and 5 artifact types that DO exist.",
    "PIN TABLE, measured: be05d938af emit-path NO (= deployed, a no-op re-cut); 4e0410825e emit-path YES, L1 machinery YES, SMA_BUCKETS NO; HEAD emit-path YES, L1 YES, SMA_BUCKETS YES (2) but the interlock forbids HEAD until the NO-SHIP is lifted BY NAME."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "\u26d4 **THE FINDING IS THAT A GREEN BUILD IS NOT A CHANGED BUILD.** `build_package.py`'s `:181` refusal tests that the pin CONTAINS the module. **`be05d938af` satisfies that test and is precisely the code already running.** So the sanctioned re-cut, executed exactly as specified, produces **a silent no-op wearing a successful build** -- and the next three acceptance criteria would then be measured against an artifact that was never going to appear. **Every gate passes and nothing moves.** || \u2b50 **THE CORRECT TEST, NAMED: DOES THE PIN CARRY THE EMIT PATH** -- `_shape_category_views` plus `\"category-views\"` in the consolidator's A4 loop -- **not merely the module file.** A module is a capability; **an emit path is the exercise of it**, and only the second produces an artifact. || \u2b50 **AND IT SUPPLIES THE MECHANISM FOR THE NO-SHIP, WHICH HAS BEEN HELD ALL EVENING ON A BARE FACT.** The ruling's ground was *the projection has never produced served output*. **This says WHY: the deployed code cannot produce it.** Not a config gap, not a scheduling gap, not a bug -- **AN OLD BUILD.** Per this fabric's own rule tonight, a true conclusion recorded without its mechanism is re-derivable wrongly; **the NO-SHIP now has its mechanism and is much harder to lift by accident.** || \u26d4 **THE PIN DECISION IS NOT THIS CHANNEL'S AND NOT THE SURFACING SEAT'S.** `4e0410825e` carries the emit path but **lacks `SMA_BUCKETS`** -- the `{ETF Strategies, ALT Strategies}` split **ANDREW RULED ~20:5xZ TODAY**. So a re-cut there **would emit a REAL artifact carrying a PRE-RULING SMA STRUCTURE**, which is a client-facing shape the sovereign superseded hours earlier. **Whether that is acceptable for this round is a scope call above the executing lane.** || \u2b50 **AND THE SURFACING SEAT MEASURED ITS OWN STRONGER HYPOTHESIS FALSE BEFORE SENDING IT:** they expected `4e0410825e` to yield EMPTY L1 sets and therefore fail AC3's *'an L1 set that sums because it is EMPTY is not a pass'*. **Not supported -- the L1 vocabulary counts are IDENTICAL at both pins** (l1_nodes 7, members_present 4, render_state 2, absent_reason 3). **The real delta is narrow and specific, and killing the wider claim is what makes the narrow one usable.** || **SELF-DISCLOSED INSTRUMENT ERROR, recorded because it changes a denominator:** their first sweep used `gold/mdpf/` and returned 10 July manifests -- **a wrong prefix, not an absence.** The 292 figure is the corrected read against `A4_PREFIX = \"portal/gold/mdpf\"` (consolidator `:88`). || **CERTIFIER'S NOTE:** this does not lift or soften the NO-SHIP, and it is not a gate on `TO-P1-AE` -- the seat is working. **What it forbids is reading a green re-cut as evidence.** || \u2b50 **DISARMED + GRADUATED ~23:0xZ BY THE CHANNEL OWNER, VERIFIED AT THIS SEAT.** `2.0.0_SA_COO~Z` re-ruled the pin to **`14b077f559`** `@0c04b480a4` and released the hold. **THE FINDING WAS ADOPTED AS THE TEST:** the decision was made on IMPORT + EMIT PATH + `SMA_BUCKETS`, not on module containment. || **RE-DERIVED HERE, NOT ACCEPTED ON THE REPORT, with the DEPLOYED pin as the negative control:** at `14b077f559` the consolidator carries `_shape_category_views` **2**, `category-views` **13**, `SMA_BUCKETS` **1**, `import mdpf_category_registry` **1**; the registry carries `category-views` **2**, `SMA_BUCKETS` **2**. \u26d4 **At `be05d938af` -- the DEPLOYED pin -- ALL SIX COUNTS ARE ZERO. The check discriminates; it is not a token that appears everywhere.** || \u26d4 **AND THE DEEPER FINDING IS THE ISSUER'S OWN, NOT THIS ROW'S: A NAMED SET IS NOT A MEASURED SET.** They ruled among `{be05d938af, 4e0410825e, HEAD}` -- **the three pins already written down in the interlock and the TO.** `0.7.0_AE_CloudOps~Z` swept the ACTUAL population: every commit touching either module in `be05d938af..HEAD`, **DENOMINATOR 19** -- and **`4e0410825e` was not in it at all**, while `14b077f559` was the ONLY member carrying all three properties. >> **This is the denominator law applied to a DECISION rather than a count: the issuer printed no denominator because they never noticed they were choosing from a SAMPLE.** << || \u2b50 **AND IT DISSOLVED A TRADE-OFF RATHER THAN RESOLVING ONE.** The earlier ruling held that *getting data flowing* and *getting the new tree* were TWO acts -- **which was true only under the belief that every emit-capable pin lacked `SMA_BUCKETS`.** `14b077f559` carries both, so **it is ONE act**, and the warning issued to `0.4.0_DE_ClientPlatform~Z` that their panel would receive the OLD tree first was **withdrawn**: it receives Andrew's ~20:5xZ ETF/ALT shape. || \u2b50 **CLOSURE NOTE FROM THIS SEAT: `14b077f559` IS THE COMMIT I CERTIFIED TONIGHT** as `TL2DS-AC2/AC4/AC5` -- the SMA L1/L2 restructure and scope-B emit as one act. **The same object arrived from two directions: certified as a restructure implementation, and independently selected as the only pin that can emit the ruled shape.** Neither derivation used the other. || \u26d4 **DISARMED != REMEDIATED. WHAT IS DISARMED IS THE PIN-SELECTION HAZARD** -- a green no-op re-cut is no longer reachable through the sanctioned procedure. **WHAT REMAINS: the re-cut has not been executed, nothing is deployed, and `category_views` still does not exist on the served plane. The `D1_CATVIEWS` NO-SHIP STANDS**, and this row does not touch it."
 },
 {
  "id": "D1_CATVIEWS-Z-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C (msg 12055 s.5a), diagnosed only after that seat first attributed the symptom to its own regression. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:25Z",
  "one_line": "TaskStop leaves a live vite child holding [::1]:PORT, and because the orphan holds only the MORE SPECIFIC loopback address a replacement server BINDS SUCCESSFULLY on 0.0.0.0/[::] -- so TWO listeners serve one port, requests split nondeterministically, and a page renders its unavailable fallback in a way indistinguishable from a component the developer just broke.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "0.4.0_DE_ClientPlatform~C",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "observed live: a backgrounded `vite --port 5175` was stopped, the wrapper died and the child survived as pid 10420",
    "the replacement fixture proxy then bound 0.0.0.0 / [::] on the SAME port SUCCESSFULLY -- no EADDRINUSE, because the orphan held only the more specific [::1]",
    "consequence measured at the page: one render silently showed the `unavailable` fallback, and the surfacing seat diagnosed it as its own regression FIRST",
    "the discriminator that actually resolved it was TWO PIDS ON ONE PORT from Get-NetTCPConnection -- nothing visible in the page could separate the two causes"
   ]
  },
  "notes": "*** THIS IS THE ORPHAN-WATCHER SHAPE ON A DIFFERENT PROCESS CLASS, and the estate's existing doctrine cannot reach it: /watcher's ORPHAN HAZARD is written entirely about inbox-watch.sh children surviving TaskStop. THE SAME PARENT-DEATH MECHANIC APPLIES TO ANY BACKGROUNDED SERVER, and here it produced a WORSE failure than the documented one, because a dev server that is merely orphaned would at least refuse the port. *** ⛔ THE SHARP HALF IS THE BIND SUCCEEDING. An EADDRINUSE would have been a loud, correct, self-explaining failure. Instead the specific-vs-wildcard address split let BOTH listeners live, which converts a process-hygiene problem into a NONDETERMINISTIC DATA problem: identical requests reach different origins on different attempts. *** THE TRANSFERABLE RULE: A PORT PROBE RETURNING 200 DOES NOT TELL YOU WHICH LISTENER ANSWERED. Liveness on a port is not identity of the thing on it -- the same conflation as ps proving a watcher process exists while saying nothing about whether any consumer reads its stdout. *** AND THE FIXTURE PROXY'S OWN HEADER ALREADY WARNS OF A NEIGHBOURING CASE -- a cached bundle talking to the real origin renders the SAME EMPTY PANEL as a working fixture -- so this is the same terminal symptom reached by a SECOND ROUTE the header does not name. A warning that enumerates causes is only as good as its enumeration. *** INERT because it requires a TaskStop-then-rebind sequence to arise and produces no wrong artifact when it does not; it cost the surfacing seat a misattributed diagnosis, not a shipped defect. ⚠ But the failure DIRECTION is the expensive one: it presents as YOUR OWN CODE BEING BROKEN, so the time is spent in the wrong place before the real cause is even a candidate."
 },
 {
  "id": "D1_CATVIEWS-Z-S2",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C (msg 12055 s.5b), visible in every exhibit filed with the TO-Q1-DE design pass. FILED by 3.0.0_SA_CVO~Z as the channel seat.",
  "surfaced_at": "2026-08-28T02:25Z",
  "one_line": "AUMGrowthMetrics renders honest-absent cells (N/A) in the LOUDEST style in its tile -- large bold white -- while their labels are small and muted, so ABSENCE receives the visual emphasis a present value would get.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "visible in every exhibit filed with the TO-Q1-DE design pass -- eleven READ renders, not a source reading",
    "the N/A cells carry the tile's large bold white treatment while their labels are small and muted, so the emphasis hierarchy is inverted relative to the information content",
    "AUMGrowthMetrics is a SHARED component used off this page, so the surface is wider than the TO that found it"
   ]
  },
  "notes": "*** WHY THIS IS FILED RATHER THAN FIXED, AND THE RESTRAINT IS THE CERTIFIABLE PART: the component is SHARED and used off this page, so changing its emphasis hierarchy reaches surfaces the TO never measured. The surfacing seat named it and DID NOT NAME AN OWNER, which is correct -- an owner assigned by inference is the unowned-list failure, and that seat has no standing to allocate one. disarm_owner is set to the issuer as the seat that can cut a cell, NOT as the seat that owns the component. *** THE SUBSTANCE IS A CLAIM-CARRYING QUESTION, WHICH IS WHY IT IS NOT MERELY COSMETIC: an N/A is an HONEST ABSENCE and rendering it in the tile's loudest treatment makes the absence read as the headline datum. CLAUDE.md's 'A VALUE MUST CARRY ITS CLAIM' governs the FIELD; this is its render-layer twin -- a presentation that gives absence the emphasis of a measurement. Whether that is wrong depends on the reader the tile is for, which is a design decision and NOT this seat's to rule. *** SCOPE: nothing here blocks TO-Q1-DE, which is delivered 5/5 and certified separately. This item exists so the observation is not lost with the TO that produced it."
 },
 {
  "id": "D1_CATVIEWS-Z-S3",
  "surfaced_by": "0.4.0_DE_ClientPlatform~C (msg 12105), correcting a MECHANISM in another seat's message whose CONCLUSION was right -- and doing so because that message was going to Andrew. Re-derived and WIDENED at this seat. FILED by 3.0.0_SA_CVO~Z.",
  "surfaced_at": "2026-08-28T02:32Z",
  "one_line": "This repository has GITLINKS WITH NO SUBMODULE CONFIG AT ALL: .gitmodules exists but is ZERO BYTES, so every `git submodule` verb FAILS FATAL rather than no-opping -- and the estate's own 'portal submodule' vocabulary (CLAUDE.md Git section) predicts a no-op, which is the opposite of what happens.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "0.0.0_AB_MSTR~Z",
  "disposition": "UNDER_INVESTIGATION",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    ".gitmodules exists and is 0 bytes; `git config -f .gitmodules --list` returns 0 entries",
    "`git submodule status portal` -> fatal: no submodule mapping found in .gitmodules for path 'portal'",
    "`git ls-files -s portal` -> 160000 4ac152f8b93a... : a REAL gitlink with no submodule config behind it",
    "WIDENING measured at this seat, NOT in the surfacing message: bare `git submodule status` fatals FIRST on models/factor_scanner -- so there are AT LEAST TWO gitlinks and the fatal is reached before portal is even considered",
    "the recorded pointer 4ac152f8b9 is 25 COMMITS BEHIND origin/DEV and was already stale before the surfacing seat was seated"
   ]
  },
  "notes": "*** THE CONCLUSION WAS RIGHT AND THE MECHANISM WAS NOT, AND THE MECHANISM IS THE PART AN INTEGRATOR ACTS ON. Saying portal 'does not ride the workspace pushes' is true and predicts a NO-OP from a submodule verb. What actually happens is FATAL. An integrator reaching for `git submodule update`, `--recurse-submodules`, or `submodule status` gets an ERROR, not a quiet skip. THE ONLY WORKING FORM IS `git -C portal <verb>`. *** ⭐ MY WIDENING: bare `git submodule status` fatals on models/factor_scanner BEFORE reaching portal, so this is not a portal quirk -- the repo carries MULTIPLE gitlinks against an entirely empty .gitmodules. Anyone diagnosing this by running the bare verb gets an error naming a path they were not asking about, which is a confusing first symptom. *** THREE LEGS, NOT TWO, AND THE THIRD HAS NO OWNER: (1) workspace evidence ON ORIGIN; (2) portal DEV code LOCAL, needing `git -C portal push origin DEV`; (3) THE WORKSPACE'S RECORDED POINTER, 25 commits behind origin/DEV, an ancestor of it, stale before tonight. LANDING LEG 2 ALONE DOES NOT MAKE THE WORKSPACE POINT AT THE NEW CODE. Leg 3 is a separate decision with a separate owner and a 25-commit move -- explicitly NOT to be done as a side effect of landing a DE change, and the surfacing seat correctly declined to bump it from a pathspec-scoped lane. *** ⭐ THE SHAPE IS THE ONE THIS CHANNEL RECORDED AN HOUR EARLIER ON A DIFFERENT PLANE: D1_CATVIEWS-Z-S1 rules that a port probe returning 200 does not tell you WHICH LISTENER answered. Here, 'portal exists at f93fb832' and 'the workspace points at the new portal' are TWO CLAIMS, and the recorded pointer is 25 commits from either answer. The surfacing seat filed a two-leg split an hour ago and it was itself incomplete -- they had checked the two legs they TOUCHED and not the one they had not. *** INERT: nothing is blocked, no act is proposed, and the PNGs Andrew can look at are unaffected. The cost is a wrong mechanism in an integrator's hands and a vocabulary in CLAUDE.md's Git section that predicts the wrong failure. disarm_owner is the integrator seat as the only one who acts on submodule verbs; the doctrine wording is a separate act and is NOT ruled here."
 },
 {
  "id": "D1_CATVIEWS-Z-S4",
  "project": "D1_CATVIEWS",
  "fabric": "site-z",
  "surfaced_by": "2.0.0_SA_COO~Z -- TO-I1-DS's ISSUER and D1_CATVIEWS-S11's named disarm_owner -- on the /canonical-flow --report-only pass of 2026-09-03 (0.0.0_AB_MSTR~Z routing 19433). This row is the DISARM RECORD, not a new finding and not an adjudication (no `adjudicates`; L9 is 3.0.0_SA_CVO's).",
  "surfaced_at": "2026-09-03T07:03Z",
  "one_line": "DISARM RECORD for D1_CATVIEWS-S11 by its named owner, seven days after it was named: TO-I1-DS's COMMITTED proof instance re-measures INVALID (rc=1) at HEAD b80b692a1d with the same instrument S11 cited. The face annotation that was to carry the standing on TO-I1-DS's own <status> line was REFUSED at commit by .tools/to-pipeline-gate.py layer 2 ('flips to complete on PIPELINE-REGISTERED project D1_CATVIEWS, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip') -- the gate reads ANY change to a complete status line as a flip and requires a VALID instance for it, so the face CANNOT be annotated while the instance is invalid, and this row is the ONLY carrier of the standing. The RE-FILE of the instance is NOT this row's act: it belongs to the D1_CATVIEWS research round, fourth in Andrew's 2026-09-03 ~06:4xZ sequence (0.0.0_AB_MSTR~Z 19441).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "S11 (surfaced 2026-08-27T18:58Z) names disarm_owner '2.0.0_SA_COO~Z as TO-I1-DS's issuer' and the L7 rule (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md, L7 Surprise) says an ARMED row is disarmed in the same turn by its named owner; TO-I1-DS's <status> read 'complete -- CERTIFIED. THE CERTIFICATE EXISTS AND IS ON ORIGIN' with no mention of the instance's validity.",
  "world_is": "No disarm act was recorded between 2026-08-27T18:58Z and 2026-09-03 (the seat was down 2026-09-01 18:07Z to 2026-09-03 06:30Z across a fabric wind-down and a device reboot; the two COO~Z sessions in between never opened S11). Re-measured 2026-09-03 06:4xZ at HEAD b80b692a1d: python .tools/proof-of-spec-check.py org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json -> INVALID (rc=1): acceptance/3/status 'APPLIED-GATED' not in the enum; spec_ref/group 'I1' not in the enum; one artifact row's commit_or_etag 'see commit of this instance' is not a commit-ish; plus 3 surprises entries carrying no row id (ANNOUNCE only, flat root). The violation COUNT moved from 19 (S11, 2026-08-27) to 3 -- the checker's rungs changed in the interval (the 88109 content rung and the surprises limb are newer than S11), so the two counts are not the same instrument; the VERDICT is the same: INVALID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "instance org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json, COMMITTED a6c2bac919 (S11's own pin); bytes unchanged at HEAD b80b692a1d",
    "proof-of-spec-check.py at HEAD b80b692a1d, run 2026-09-03 06:4xZ by 2.0.0_SA_COO~Z (a seat other than S11's surfacing seat 0.4.0_DS_ClientPlatform~Z and other than the instance's author 0.4.0_DS_ClientPlatform~T): INVALID rc=1, 3 VIOLATION lines + 3 surprises-announce lines; the checker's own WARN: 'alignment above is computed on a STRUCTURALLY INVALID instance'",
    "the disarm act ATTEMPTED and REFUSED: an ISSUER NOTE after the leading 'complete' token of TO-I1-DS's <status> was staged 2026-09-03 ~07:0xZ and .tools/to-pipeline-gate.py layer 2 REFUSED the commit (verbatim: \"flips to 'complete' on PIPELINE-REGISTERED project D1_CATVIEWS, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.\"); the audited '# pipeline-override:' escape was NOT spent -- a prose note is not worth an override, and the refusal is itself the mechanism that keeps this face from being re-flipped complete without a VALID instance. The face edit was reverted (git checkout); 0 lines of the face changed.",
    "S11's own bound, re-read and unchanged: 2.0.0_SA_COO~Z's D1-i-1 orphan discharge does NOT rest on this instance (S11 notes)",
    "why the re-file is not taken here: Andrew-direct 2026-09-03 ~06:4xZ (0.0.0_AB_MSTR~Z 19441) -- one project per fabric, D1_CATVIEWS FOURTH as a research round; the instance's author seat ~T is not registered (get_live_agents 06:49Z: 4 live, all Tier-0/1)"
   ]
  },
  "notes": "WHAT THIS DISARM IS: the standing of TO-I1-DS's certificate -- it rests on the certifier's read of the criteria and NOT on a valid instance -- is now on the record where the L8 rollup reads it, and the L6 gate refuses any future complete flip on that face without a VALID instance. WHAT IT IS NOT: a re-file (the DS-class act of writing a valid instance for I1DS-AC1..AC4), a re-certification (3.0.0_SA_CVO~Z's), a face edit (refused, see evidence), or a disposition of S11 (this row carries no `adjudicates`; S11 stays UNDER_INVESTIGATION until the CVO's row). SEVEN DAYS LATE, STATED: the same-turn rule was not met and the reason (seat down 2026-09-01 18:07Z to 2026-09-03 06:30Z; no successor opened the row) is a fabric fact, not a mitigation. TWO TRANSFERABLE HALVES: (1) a disarm_owner named on a row is an obligation that does not travel with a session -- nothing in B.0 or the inbox surfaces it; the /canonical-flow --report-only pass is what surfaced it, which argues for that pass at every seat load on a project the seat has ever issued into. (2) THE GATE CANNOT TELL AN ANNOTATION FROM A FLIP: check_complete_flip keys on the staged status line reading 'complete', so an issuer cannot record a caveat ON a complete face without a valid instance -- the caveat has to live in the channel, which is where the spine puts it anyway (the row is the carrier).",
  "disposition": "UNDER_INVESTIGATION"
 }
]
```

### ROUND KEEPER (cross-fabric) -- 77027/COO 77030: **A TOOL-MINTED SENTINEL LEFT UNCOMMITTED AT THE AUTHORING DEVICE READS STRANDED ON EVERY OTHER DEVICE**

3.0.0_SA_CVO, ~23:4xZ, banked at the instance's home. THE INSTANCE: COO's tick-6 scan flagged site Z's d1-catviews-recut-14b077f559 deploy ledger as sentinel-less; MSTR measured the boundary -- the sentinel EXISTS at ~Z's tree (tool-minted 23:05Z, 3,857 B) but was NEVER COMMITTED (tracked 0 at origin/CLOUD AND origin/SITEZ; positive control: 2 other sentinels tracked). The .md record travelled on the merge; its index entry did not. COO's finding: TRUE about this tree, FALSE about the entry -- re-home withdrawn (would mint a duplicate); remedy = one commit at ~Z over the bus. THE CLASS: the cross-fabric form of "untracked-but-present is invisible to every instrument" -- the gate-bypass scan's STRANDED verdict is a property of THIS DEVICE'S TREE, not of the entry, and diverges for any entry authored on the other fabric whenever a mint is left uncommitted; it lands as a RECOGNISED defect pattern ("no sentinel"), which is what makes it credible. CANDIDATE REMEDY (MSTR's, tool owner at the cut): the scan hedges "sentinel absent HERE -- may be uncommitted at the authoring device" for other-fabric author suffixes, naming the origin-tracked check as the discriminator. Sits beside the hand-authored-ledgers keeper: same gate, opposite failure direction.
