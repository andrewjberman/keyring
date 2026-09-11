# AMGT_RESAPP.TO-AMGT-rd-8 -- THE SURFACE ITSELF: a persistent Lead Panel above three tabs (Thesis / Peers / Coverage), Print as a header export, the Model tab CUT and its figures rehomed

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~2</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, row S16, FWD-15)

```
AMGT-rd-8. THE SURFACE ITSELF. The `.tsx` Andrew approved: a persistent LEAD PANEL for universe discovery
-- Trending / Breakout x Price / Chatter, List / Chart, a Security overlay, and Starred -- sitting above
THREE TABS: Thesis, Peers, Coverage.

THREE SHAPE DECISIONS ARE ANDREW'S AND ARE NOT YOURS TO REOPEN:
  - PRINT IS A HEADER EXPORT ACTION, not a tab.
  - THE MODEL TAB IS CUT, and its figures are REHOMED into Thesis and the Security overlay. Cutting it
    without rehoming the figures loses them; that is the failure this clause names.
  - THE LEAD PANEL IS PERSISTENT -- it stays while the tabs change beneath it.

IT READS PRE-COMPUTED ROWS AND NEVER RE-DERIVES A RANKING AT RENDER TIME (`C-SERVER-SIDE-RANKING`). The
rankings come from **`opal-harvest-security-metrics`** -- RENAMED 2026-09-11 ~20:1xZ from `opal-amgt-security-metrics`, WHICH IS DROPPED AND NO LONGER RESOLVES (42 rows migrated, verified on full item equality; env knob `HARVEST_METRICS_TABLE`) -- written by `AMGT-rd-5` (chatter) and `AMGT-rd-6` (price).
A client-side sort, a score computed on load, or a scan-then-rank is the defect this constraint exists to
prevent -- the page must be able to render the ranked set without doing the ranking.

`C-DESIGN-SPEC-FIRST` IS LIFTED FOR THIS PROJECT (PRD s.3b). `.tsx` is authorized in this round.

WHAT TO PRODUCE, under portal/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~2/:

  (a) THE LEAD PANEL  persistent, with the two ranking axes crossed against the two modes
      (Trending/Breakout x Price/Chatter), a List and a Chart view, the Security overlay, and Starred --
      reading pre-computed rows only.

  (b) THE THREE TABS  Thesis, Peers, Coverage. The Model tab is CUT and its figures appear in Thesis and
      the Security overlay -- name in your deliverable WHERE each rehomed figure went.

  (c) THE PRINT HEADER ACTION  Print as an export action in the header, wired to the landed print
      renderer, not a fourth tab.

  (d) THE RENDER CHECK  a headless render of the route, READ (not merely captured), checked against the
      silver-canvas colour law. Light text or ghost-white buttons outside a dark Panel are the recurring
      defect a grep cannot see.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-5`, `AMGT-rd-6` AND `AMGT-rd-7`** -- it reads the chatter rows, the price rows and
the starred state. It is the LAST cell in slot ~2's queue and converges all three. It also reads rounds
1-4's landed work: the provenance face (S3), the check face (S10), the peer set (S8), the coverage reader
(S4) and the print renderer (S5).

## BOUNDS

```
BLOCK NEVER RE-DERIVE A RANKING AT RENDER TIME. Read pre-computed rows. No client-side sort of an unranked
  set, no score computed on load, no scan-then-rank.
BLOCK THE THREE SHAPE DECISIONS ARE ANDREW'S: Print is a header export, the Model tab is CUT WITH ITS
  FIGURES REHOMED, the Lead Panel is persistent. Do not restore the Model tab and do not make Print a tab.
BLOCK NOTHING PORTAL MOVES -- NO PROD AND NO DEV PROMOTE -- UNTIL ANDREW NAMES IT. Andrew-direct
  2026-09-11 ~15:0xZ, verbatim: "nobody does any portal promotes until i say so is the takeaway here."
  COMMIT your work; do NOT promote, do NOT push the portal submodule, do NOT merge to DEV or PROD.
BLOCK NEVER write device-specific logic into the portal -- DERIVE, don't hardcode.
BLOCK NO cell may claim an EXERCISED outcome REALIZED on the strength of its own artifact. Building the
  surface makes FWD-15 REACHABLE; a PERSON must still have used it. Grade the DONE WHEN state line, never
  the ACCEPT paragraph beside it. Do not mark FWD-15 REALIZED.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
WARN Bound every invocation under `timeout 120`.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
comp-cache collisions (at the cut): 415 of 415 portal files scanned. Every existing key collision is on
    ANOTHER surface -- market-performance, model-portfolio, partner-analytics, positioning -- and NO
    AMGT/research key namespace exists. So you enter CLEAN, and you must KEEP it clean: this cell
    introduces new filter/toggle/window state (the two axes, the two modes, List/Chart, Starred), which is
    exactly the auto-rule-2 trigger. RUN `comp-cache collisions` at Phase 1 against your new keys.
comp-routes behaviors (at the cut): 27 behaviors. The auth-gated `/api/scoped/*` pattern with the
    `auth-validator-edge` viewer-request is the precedent your reads follow; `/api/scoped/satellites/*`
    additionally carries the shared-advisor-router origin-request. Follow the established pattern rather
    than minting a new unauthenticated path.
comp-blast: DECLARED-NOT-APPLICABLE at the L5 cut and APPLICABLE HERE -- this is the cell that edits the
    portal shell. RUN `comp-blast` at Phase 1 on every shared component you touch.
PRD s.3b (Andrew-direct 2026-09-11 ~12:1xZ): "three tabs (Thesis / Peers / Coverage) beneath a persistent
    Lead Panel; Print as a header export action; the Model tab CUT with its figures rehomed into Thesis
    and the Security overlay. `.tsx` is authorized in the SURFACE round. FWD-15 is his confirmed outcome."
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
portal/src/
lib/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-8.lead-panel-and-three-tabs.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~2/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W2-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.
NOTE: `portal/` is its own git repo. Address it explicitly (`git -C portal ...`) and return to the
workspace root when the task ends -- a lingering portal CWD silently substitutes the WRONG repo's history
into evidence pulls, with no error.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-8"><invocation>cd portal &amp;&amp; timeout 110 npx tsc -b --pretty false 2>&amp;1 | tail -5</invocation><expect>zero TypeScript errors -- the new Lead Panel and the three tabs compile. Any error line is NOT met. A grep-based check is not a substitute: this is the language-appropriate instrument and the Rule 14 commit gate checks ZERO frontend files</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-8"><invocation>cd portal &amp;&amp; timeout 110 npx tsc --noEmit --pretty false 2>&amp;1 | tail -3</invocation><expect>zero errors on a clean no-emit pass -- confirming AC1's result is not an artifact of a stale build cache. A differing result between AC1 and AC2 means the build output was stale and is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-8"><invocation>timeout 110 comp-cache collisions 2>&amp;1 | tail -12</invocation><expect>a printed denominator of portal files scanned, and NO collision listed among the NEW AMGT/research query keys this cell introduces. Pre-existing collisions on other surfaces (market-performance, model-portfolio, partner-analytics, positioning) are expected and are NOT this cell's. A new key colliding with an existing one is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-8" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical): the surface compiles.
- **AC2** (mechanical, staleness control): AC1's green is not a cached artifact.
- **AC3** (mechanical, auto-rule 2): the new query keys do not collide in a namespace that was clean.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): does the page match the shape Andrew approved -- a PERSISTENT Lead Panel above exactly three tabs, Print as a header export rather than a tab, and the Model tab CUT WITH ITS FIGURES ACTUALLY REHOMED into Thesis and the Security overlay rather than lost -- and does it READ pre-computed rankings rather than re-deriving any ranking at render time? The rehoming and the no-re-derivation are both things a compile cannot see, and the headless render must have been READ, not merely captured.

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<!-- WHY THIS IS STILL `staged` AFTER A SUCCESSFUL DRAIN (2.0.0_SA_COO~ZZZ, 2026-09-11 ~21:1xZ,
     drained @6e764ef0aa; the worker's report and its VALID instance are both in hand):
     AC2 IS A MECHANICAL CRITERION AND IT MEASURED VACUOUS. `tsc --noEmit` against this repo's root
     tsconfig typechecks ZERO files -- the root is `"files": []` plus `references` only, and --noEmit
     does not follow project references. The worker PROVED the vacuity with a positive control: it
     injected a type error, AC1's `tsc -b` caught it (`error TS2322`), AC2's invocation did not.
     THIS SEAT CORROBORATED IT BY A DIFFERENT INSTRUMENT -- reading `portal/tsconfig.json` rather than
     re-running the worker's compiler -- and the config is exactly as reported.
     ⛔ THE DEFECT IS THIS SEAT'S, AT THE CUT. A criterion whose instrument cannot fail is the
     always-passes shape, and it should have been run against the world before it was handed over.
     THE WORKER DID THE RIGHT THING: it refused to grade PASS on a vacuous green, recorded AC2 as
     UNVERIFIABLE-BY-INSTRUMENT with `status_reason` naming the CVO, named AC1's `-b` run as the
     substitute oracle, and left the status alone. A worker that had flipped this to `complete` would
     have produced a clean-looking terminal order on an ungraded criterion.
     ⛔ AND THIS SEAT WILL NOT SELF-GRADE IT. AC2 is not a judgment criterion, so converting it into
     "graded by a substitute" is an adjudication, which is `3.0.0_SA_CVO~Z`'s at L9. The order goes
     terminal when the CVO rules on AC2's instrument defect and on AC4's judgment -- both travel in
     the round-5 packet. -->
<round>5</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b (`C-DESIGN-SPEC-FIRST` LIFTED; the approved page shape), ANDREW-DIRECT 2026-09-11 ~12:1xZ "Recs approved" -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-8) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN B tail, slot ~2. LAST in the queue -- converges `AMGT-rd-5`, `AMGT-rd-6` and `AMGT-rd-7`.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-8` row; the S16 manifest row and FWD-15.
> **NOTE (2.0.0_SA_COO~ZZZ).** The portal promote ban is repeated inside the worker face verbatim because it is the one standing order most likely to be crossed by a worker doing good frontend work and reaching for a deploy at the end. Committing is fine; promoting is not, on either branch, until Andrew names it.
> **NOTE 2.** This cell makes FWD-15 REACHABLE, not REALIZED. Fourteen of fifteen outcomes carry EXERCISED bars that no build can close. If this worker marks an outcome REALIZED, that is the exact failure the sibling project committed (eight outcomes graded REALIZED against an artifact that had never run).
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C3 = 12 standing NEVER clauses incl. the no-monitor moratorium and the portal-promote hold. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) verdicted across 96 mapped role(s); this cell adds no IAM of its own and reads through the established auth-gated route. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never resource-checked, 51 GRANTED-BROAD EXCLUDED not cleared.
comp-cache: RUN -- 415 of 415 portal files scanned; no AMGT namespace, and auto-rule 2 requires a Phase 1 re-run against this cell's NEW keys, asserted at AC3. BLIND: declared keys only, not keys built dynamically.
comp-routes: RUN -- 27 behaviors enumerated; the auth-gated /api/scoped/* + auth-validator-edge pattern is the precedent. BLIND: it reads declared behaviors, not runtime redirects.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: APPLICABLE TO THIS CELL and carried at Phase 1 -- it edits the shared portal shell, the one round-5 surface that is not new.
</preflight>
**Preflight disposition:** the only round-5 cell touching a SHARED surface (the portal shell), hence the only one where comp-blast is applicable rather than declared-not-applicable. Its two invisible-to-a-compiler hazards -- figures lost in the Model-tab cut, and a ranking re-derived at render time -- are both carried in the judgment criterion.
