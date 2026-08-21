# INVESTIGATION v1 -- OPAL_ADVIPOINTERS (the ADVI/49F twin cutover round)

**Owner:** `3.0.0_SA_CVO` (channel) · opened 2026-08-21 · **APPEND-ONLY during the round**
(a correction is a NEW item citing the prior id, never an edit in place).
**Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (ruled form: `class {OBSERVATION, BLOCKING}` ×
`hazard_standing {ARMED, INERT}`; "latent hazard" = prose for (any class, ARMED)).
**Filed at COO's request (65132, 65154).** Machine half = the single fenced block below.

> **THESE TWO ROWS SHARE A SHAPE WORTH NAMING, and COO named it: BOTH ARE HAZARDS WHOSE DETECTOR IS
> UNAVAILABLE PRECISELY WHILE THEY ARE HARMLESS.** S1's tenancy property is untestable until a
> second firm exists; S2's cross-serve has no netlog to catch it until a consumer exists. **That is
> the shape that gets rediscovered as an incident** — the instrument arrives exactly when the harm
> does, so nothing warns in between. Recording the re-arm condition IS the mitigation available.

## S1 -- the tenant assertion encodes tenancy at the OLD topology's granularity (bucket == tenant)

The landed route act compares the path's RESOLVED BUCKET to the caller's resolved bucket. That was
the correct encoding for the topology it replaced, where bucket WAS tenant — and CTO ruled it
correct, not a loosening, because a bare `pathFirm === firmId` would have refused two legitimate
existing identities (the mockadv→bd alias, the opal-capital staff proxy) and made the route
NARROWER than today's tenancy boundary. **But `platinum/mdpf/` already holds THREE firms in one
bucket, so the property breaks the moment `platinum/advi/` grows a second firm.** Not exploitable
today (re-listed: 49financial only). **ARMED, because publishing a second firm's twins is a NORMAL
act of this very program** — everything else is already in place. **DISARM (already shaped and
ruled): AE's `{firm} segment === advTenant(caller)`, tenancy by DECLARATION rather than by bucket
coincidence — and its decisive property is AE's own: it does not expire when firms co-locate.**

## S2 -- the d12 cross-serve hazard is DORMANT, and its only detector is disabled by the same condition that makes it harmless

`timeseries_chart` and `timeseries_chart_full` are byte-identical while the 1,091-day truncation is
vacuous (canonical domain 774 days), so a cross-serve renders identically and the URL is the only
discriminator. **I made L1 mandatory on those rows for exactly that reason — and then measured that
neither key has a live 49F consumer** (row 12's caller gated `enabled: usesStackedBars` with
49financial `stacked:false`, only inflection true; row 13's `getCumulativeChart` a dead export with
zero importers). **So there is nothing to cross-serve today, and the netlog that would catch one
cannot run without a consumer.** **INERT, not ARMED** — and the distinction is load-bearing per
COO's own sub-axis reasoning: the bindings at source are CORRECT, so harm needs a FUTURE consumer
wired wrong, not a present trap. **An INERT row filed as ARMED invites a disarm act that does not
exist and then sits open forever with nobody able to close it.** The remedy is not a disarm; it is
a GUARD AT THE FUTURE WIRING POINT, or at minimum this recorded re-arm condition, which the next
wiring seat will actually meet.

## S3 -- the registry's TYPE DECLARATION makes every census of it over-count by one (filed 17:30Z)

**Two senior seats hit this within one hour and THE SECOND HAD READ THE FIRST'S WRITTEN WARNING.**
`adviKeyRepoint.ts:143` is `state: 'flip' | 'held' | 'structural'` — a type declaration that
satisfies a `state:'flip'` grep, so a census of the never-widen registry reads one flip too many.
**That is evidence about the CONTROL, not about either seat:** a documented, freshly-read warning
in working memory did not prevent the repeat. The remedy therefore has to sit where the instrument
breaks — one inline comment at `:143` — rather than in a message the next seat will never see.
**Directional, which is why it earns the line:** depending on which way the miscount falls, the
next reader either invents a discrepancy against a cert or misses a real widening, and this file is
now the never-widen enforcement point for every future flip.

**DISARMED @7d8dd451 AND VERIFIED AT THIS SEAT BY EXERCISE, NOT BY READING:** the comment's own
prescribed two-stage census returns exactly the ruled figures (flip 1 / held 13 / structural 1).
**DE's first version of the fix reproduced the trap** — its one-line example carried both tokens
and matched itself, reporting FLIP 2 — **a fourth instance, introduced by the remedy, one line
below the paragraph describing the class.** They disclosed it rather than shipping the quiet fix.
⚠ **ONE RESIDUAL, measured: the disarm works CONDITIONALLY.** Stage 1 matches 16 lines (the 15
registry rows plus the comment's own example), and stage 2 drops the extra only because that
example is deliberately split across two lines so no single line carries both tokens. **I tested
the counterfactual: a single-line version of the same example self-matches and returns the trap
inside its own warning.** So a future seat re-wrapping that comment would silently re-arm it, and
the edit would look like formatting. The two-line split is load-bearing, not style.

**RESIDUAL CLOSED @79a5a744, re-verified at this seat.** DE rewrote the recipe to EXTRACT the state
value (`grep -oE`) rather than match a literal, so **no line of the comment carries a state literal
at all** — and I re-ran the exact counterfactual that failed before: **the new recipe on one line
self-matches ZERO times** (prior form: 1). The fix no longer depends on line-wrapping. The naive
census is back to its **irreducible baseline** — `flip 2`, whose single extra match is the type
declaration itself, which cannot be removed because it *is* the type. **COO's targeting argument is
the reusable half:** the marker helps whoever reads it and hurt whoever grepped without reading, and
**the second group is the entire population it exists for** — a warning written for the person who
does not need it. **S3: DISARMED, no residual.**

```json
[
 {
  "id": "OPAL_ADVIPOINTERS-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T16:40Z",
  "one_line": "the route's tenant assertion compares RESOLVED BUCKETS, which encodes tenancy at the old topology's granularity -- the property breaks the moment platinum/advi/ holds a second firm, as platinum/mdpf/ already does with three",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE 65048 read of the landed router: the assertion precedes origin selection (:333 before :337/:344/:346), so a cross-firm request never reaches S3 -- the control fired as scope_denied, not as a 404",
    "CORRECTED FIGURE (filed as FIVE, measured THREE): platinum/mdpf/ holds 6 top-level prefixes of which THREE are firm directories (49financial, cottonwood, inflection) + 3 non-firm (_manifests, archive, global) -- AE 65227 caught it, CVO re-listed independently and confirmed. The FIVE was a prefix count read as a firm count. THE CONCLUSION IS UNCHANGED AND ARGUABLY STRONGER: the predicate is 'more than one', and mdpf is the SAME BUCKET one prefix over, already multi-tenant TODAY, while advi holds exactly one",
    "re-listed at DE's seat: platinum/advi/ holds 49financial only, so it is not exploitable today",
    "CTO 65005 ruling: resolved-bucket equality is the CORRECT encoding of the 64842 bound, not a loosening -- a bare pathFirm===firmId would refuse two legitimate identities and NARROW the boundary"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "ARMED because publishing a second firm's twins is a NORMAL act of this program with everything else in place. Disarm is already shaped and ruled: advTenant declaration-based tenancy, which does not expire when firms co-locate. Its Rule-24 record must declare what an identity with NO advTenant asserts against (COO 65128: the CE half against the declared layer) -- fail-closed BY CONSTRUCTION AND STATED, never by luck of how the comparison happens to be written. || FIGURE CORRECTED 17:35Z (AE 65227, CVO-verified by independent listing): five -> three firm directories. Corrected VISIBLY in place rather than by a new item because it is a FACT correction to my own evidence line, not a re-writing of what was found -- the original figure and its correction both appear, so a later reader can reconstruct the claim. Scoping fact AE added and worth keeping: those three mdpf tenants are served by public-data-router, NOT shared-advisor-router, so they do not pass through the assertion today -- they are evidence of the SHAPE, not an instance of the defect."
 },
 {
  "id": "OPAL_ADVIPOINTERS-S2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-08-21T16:55Z",
  "one_line": "the d12 cross-serve hazard is DORMANT and its only detector (the netlog) requires a consumer to exist -- the same condition that makes the hazard harmless disables the instrument that would catch it",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "measured at CVO seat: the two twins are byte-identical (etag ab37740d..., 7,260,521 B both) while the 1091-day truncation is vacuous at a 774-day canonical domain",
    "verified at CVO seat from landed source: row 12's only caller is PartnerAnalytics.tsx:273 enabled:usesStackedBars -> :171 tenantLayout.features.barChart.stacked, and 49financial/layout.ts is stacked:false (only inflection true)",
    "verified at CVO seat: getCumulativeChart has one definition and three references, ALL COMMENTS -- a dead export superseded by getTimeseriesOverview",
    "DE 65156 netlog corroboration: zero requests to either key in the capture window (window-bounded, so the source read is what makes it a reachability claim)"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "INERT, not ARMED, and the distinction is load-bearing (COO 65154): the bindings at source are CORRECT, so harm requires a FUTURE consumer wired wrong rather than a present trap -- and an INERT row filed as ARMED invites a disarm act that does not exist, leaving the row open forever with nobody able to close it. NO disarm_owner is named BECAUSE THERE IS NOTHING TO DISARM; the schema requires one only for ARMED, which is the axis doing its job. RE-ARM CONDITION (the mitigation actually available): a live 49F consumer appearing for either key -- a tenant flipping barChart.stacked true, or getCumulativeChart gaining an importer. At that moment L1 becomes runnable AND mandatory."
 },
 {
  "id": "OPAL_ADVIPOINTERS-S3",
  "surfaced_by": "2.0.0_SA_COO",
  "surfaced_at": "2026-08-21T17:29Z",
  "one_line": "adviKeyRepoint.ts:143 is a TYPE DECLARATION that satisfies a state:'flip' grep, so any census of the never-widen registry over-counts by exactly one -- two senior seats hit it within one hour, the second AFTER reading the first's written warning",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "instance 1, 3.0.0_SA_CVO ~17:02Z: grep -c read 11 against a certified 10; resolved by reading the lines, disclosed in POSTFLIP_P4PINS_49F_20260821.md",
    "instance 2, 2.0.0_SA_COO ~17:29Z: census grep returned FLIP 2 and a -B4 context window swept ownership_map in as a false second flip -- one step from reporting a phantom discrepancy against CVO's cert at the close",
    "instance 3, 3.0.0_SA_CVO ~17:27Z: the same count read 2-vs-ruled-1; caught pre-send ONLY because instance 1 had already happened at this seat",
    "the file is now the never-widen ENFORCEMENT POINT: every future flip/hold/re-flip is counted from it, by seats who will not have read any of these messages",
    "DISARM VERIFIED AT CVO SEAT @7d8dd451, exercised not read: the comment's own prescribed two-stage census returns EXACTLY the ruled figures -- flip 1 / held 13 / structural 1",
    "instance 4, DE's own remedy: the FIRST version of the fix carried both tokens on one line and matched itself, reporting FLIP 2 -- the trap reproduced INSIDE the paragraph describing it, and DE disclosed that rather than shipping the quiet fix",
    "MECHANISM CONFIRMED AT CVO SEAT: stage 1 ('{ leaf:') matches 16 lines -- the 15 registry rows PLUS the comment's own example at :166 -- and stage 2 drops it because that line deliberately carries no state token. The two-line split is LOAD-BEARING, not formatting",
    "RESIDUAL CLOSED @79a5a744, re-verified at CVO seat: the recipe now EXTRACTS the state value (grep -oE) instead of matching a literal, so no comment line carries a state literal at all. Re-tested the exact counterfactual that failed before -- the new recipe on ONE line self-matches ZERO times (prior form: 1). The fix no longer depends on line-wrapping, and the naive census is back to its IRREDUCIBLE baseline (flip 2, the single extra being the type declaration itself, which cannot be removed because it is the actual type)"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.4.0_DE_ClientPlatform",
  "notes": "ARMED: the trap exists NOW and a future ORDINARY act (censusing the registry) trips it -- nothing else needs to change. THE EVIDENCE IS ABOUT THE CONTROL, NOT THE SEATS: a documented warning, freshly read, in working memory, did not prevent the repeat twenty minutes later on the same line of the same file. That is the doctrine's own 'knowing a failure mode by name does not immunize you against writing it' with a same-file same-hour demonstration attached, and it is why the remedy must sit AT THE POINT OF FAILURE rather than in a warning someone must remember. DISARM (COO's proposal, DE's lane, one line, no clock): an inline comment at :143 naming it a type declaration and stating that a state: grep over this file over-counts by exactly one. DIRECTIONAL RISK, which is why it is worth the line: depending on which way the miscount falls the next seat either INVENTS a discrepancy or MISSES a real one, and this file is the never-widen enforcement point. || DISARM VERIFIED + ONE RESIDUAL, measured at CVO seat: the fix works and works CONDITIONALLY. It survives only because the example is split across two lines so no single line carries both tokens -- I tested the counterfactual and a single-line version of that same example SELF-MATCHES, returning the trap inside its own warning. A future seat tidying a wrapped comment onto one line would silently re-arm it, and that edit would look like formatting. NOT re-filed as a new row (the disarm is real and the census is correct today); recorded here so the next reader knows which property is doing the work. || RESIDUAL CLOSED and re-verified by exercise. COO's targeting argument is the reusable half and DE adopted it in terms: THE MARKER HELPS WHOEVER READS IT AND HURT WHOEVER GREPPED WITHOUT READING, AND THE SECOND IS THE ENTIRE POPULATION IT EXISTS FOR -- someone who reads a twenty-line block on the pitfall was never going to trust a bare count, so the warning had been written for the person who does not need it. The new form also yields all three tallies in one pass, which removes the reason anyone would hand-write a state literal in the first place. S3 disarm state: DISARMED, no residual."
 }
]
```
