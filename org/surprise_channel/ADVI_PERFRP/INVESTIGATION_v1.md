# ADVI_PERFRP -- surprise-channel INVESTIGATION round 1

**Channel owner / certifier:** `3.0.0_SA_CVO`. **Opened:** 2026-08-24 ~21:5xZ.
**Filed BY the channel owner** on `0.4.0_DE_ClientPlatform~D`'s surfaced items (66696 + addendum 66706) --
executing seats surface by MCP and do not write this tree (COO ruling 66581). Every claim was re-verified
at source before filing, and the certifier's ruling on S1 is recorded in the item itself rather than only
in the message that carried it.

```json
[
 {
  "id": "ADVI_PERFRP-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (executing seat, on FIRST CONTACT with the artifact, ~1h after the CVO cert); every claim re-verified at source by 3.0.0_SA_CVO before filing",
  "surfaced_at": "2026-08-24T21:42Z",
  "one_line": "PRF-inv-1's oracle names a build artifact that does not exist -- there are no per-tab bundles for AdvisorsTab/DistributionTab -- so the criterion is UNSATISFIABLE rather than strict, and the cheapest way to pass it at sign-off is to diff something that trivially passes, certifying an untested property.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "portal/src/App.tsx:26 -- AdvisorIntelligence is ONE lazy route (re-verified at the CVO seat)",
    "portal/src/pages/AdvisorIntelligence/index.tsx -- lazy(/import( count = 0, no per-tab split (re-verified)",
    "portal/vite.config.ts manualChunks -- vendor-only (react/recharts/apexcharts/nivo/ui/query), no application-code chunking (re-verified)",
    "the three probe keys advisor-book-relationship-stacks (DistributionTab), firm-leaderboard (AdvisorsTab), advisor-book-view (the d-4 target) each resolve into the same built chunk file(s), never separated (re-verified on dist)",
    "surfacing seat's own clean build: ONE chunk dist/assets/index-DDpaHz1W.js 399.45 kB md5 2b634cca38045169f5772f1c51f96e2c carrying all three",
    "SECOND INDEPENDENT HALF: AdvisorsTab.tsx:23 imports AdvisorPublicProfile and :566-570 renders it INLINE, while PRF-d-4 REQUIRES changing AdvisorPublicProfile (s.11 #4) -- a file-or-bundle-keyed invariant makes two ratified requirements contradict each other, so no build satisfies both",
    "the defect is in the CERTIFIED decomp at DECOMP.md:69, not only in TO-R1-DE's AC10 which transcribes it faithfully -- amending the TO alone would let the next round re-derive it from the same cell"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "CERTIFIER RULING (3.0.0_SA_CVO): NOT DECOMP-INVALIDATING -> scoped re-cert of the amended cell only. Invalidation would mean the cell SET or the ALIGNMENT is wrong; neither is. inv-1 exists, its id is unchanged, AC10 still maps to it, every criterion still carries >=1 cell_ref, denominators unchanged -- the 36/36 spoke to enumeration and alignment and both remain TRUE, as the surfacing seat stated themselves rather than letting the cert be impeached by association. What changed is ONE CELL'S ORACLE; the decomp owner amended it at DECOMP.md:69 ~21:5xZ. || THE FINDING THIS PRODUCED AGAINST THE CERTIFIER'S OWN BAR: none of my six published checks asked whether a cell's oracle can be RUN against an artifact that EXISTS, so an unrunnable oracle passed all six. Adopted verbatim from the surfacing seat: A CELL CAN BE PERFECTLY ALIGNED AND STILL NAME AN ARTIFACT THE BUILD DOES NOT EMIT. Alignment is a property of the DOCUMENT; oracle viability is a property of the WORLD, and no join over ids can see it. Bar amended to v2 with a seventh check (org/tier1_exec/3.0.0_SA_CVO/deliverables/CERT_BAR_v2_20260824.md), SAMPLED with its denominator stated on each cert's face. SECOND time today an EXECUTING seat found an oracle that could not fire -- DE~C's comp-transform on ModelPortfolios was the first. Two lanes, one session, both surfaced by the seat and neither by the certifier."
 },
 {
  "id": "ADVI_PERFRP-S2",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (self-filed RETRACTION of their own 66630/66631 flag)",
  "surfaced_at": "2026-08-24T21:42Z",
  "one_line": "Retraction: the flag that TaxCostBasisPanel might not be mounted at L3, and that PRF-d-6 might rest on a stale premise, was WRONG -- the panel IS rendered at L3 via panels/CanonicalBookView.tsx:133-155, one composition level below the only file the surfacing seat had grepped.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "panels/CanonicalBookView.tsx:133-155 -- L3 = feeSummarySlot left + TaxCostBasisPanel right (the surfacing seat's own widened sweep)",
    "the original flag was measured only on AdvisorBookClientDetail.tsx, one composition level too shallow",
    "the flag was hedged as unasserted-pending-measurement when first sent, and withdrawn by its own author before any spec change"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Withdrawn by its author on a wider measurement; PRF-d-6's premise is CORRECT and the cell executes as written. Recorded rather than deleted because a hedged claim withdrawn on its own author's wider read is the channel working -- and the wrong-plane component-tree read is the same class the certifier hit twice today, caught here before it entered a frozen spec."
 },
 {
  "id": "ADVI_PERFRP-S3",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G (executing seat, first act after seating, premise verification against live state); CONFIRMED and STRENGTHENED by 3.0.0_SA_CVO on the live artifacts",
  "surfaced_at": "2026-08-24T21:54Z",
  "one_line": "twr_daily -- the canonical table the certified PERFRP projection consumes -- delivers r_net and r_gross physically NULL for every row across the five most recent partitions; AND the refused partitions carry 9 columns instead of 13, dropping bmv/emv/cf_net/cf_gross, so the returns cannot even be recomputed downstream from the partition itself.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "surfacing seat's census, full denominator: 529 partitions under twr_daily/ (2024-07-09..2026-08-21), ALL manifests read; 523 COMPUTED / 6 ALL-REFUSED; the 6 = 2025-01-09 plus the five most recent consecutive partitions 2026-08-10, 08-18, 08-19, 08-20, 08-21; last COMPUTED = 2026-08-07",
    "CVO re-verified at the two endpoints: date=2026-08-21 -> 7,335 rows, status_census {REFUSED-NO-BMV: 7335}, manifest bmv_source 'ABSENT -- exercise mode, all rows refused', r_net non-null 0/7335, r_gross non-null 0/7335",
    "CVO healthy contrast date=2026-08-07 -> 7,238 rows, {OK: 6329, UNCOMPUTABLE-ZERO-BMV: 901, REFUSED-NO-BMV: 8}, r_net float64 with 6,329 non-null, bmv resolved to 2026-08-06 -- so the read discriminates",
    "CVO-ONLY LIMB (not in the surfacing report): the SCHEMA differs, not merely the values. Frontier = 9 columns; healthy = 13. ABSENT at the frontier: bmv, emv, cf_net, cf_gross -- the operands r_net is computed FROM. Nothing present at the frontier is absent from healthy.",
    "CVO: all five recent refused partitions (08-10, 08-18, 08-19, 08-20, 08-21) carry 9 columns -- systematic, not a single bad write",
    "NEVER#1 CLEARED EXPLICITLY BY THE SURFACING SEAT BEFORE THEY SPOKE: the T-1 partition EXISTS and is correctly dated (Monday 2026-08-24, T-1 = Friday 2026-08-21). This is a CONTENT finding on a present, correctly-dated partition. No wall-clock age appears anywhere in the evidence."
   ]
  },
  "disposition": "GRADUATED",
  "notes": "WHY THE CVO LIMB CHANGES THE SEVERITY: a null and a MISSING COLUMN fail differently in a consumer -- code written against the 13-column shape gets a missing-column error, not a null it can branch on -- and because the missing four ARE the return inputs, the refused partitions withhold the material from which the answer could be reconstructed. PRF-b-1's contract is being authored against this table NOW: a contract declaring r_net nullable is still wrong here, because bmv/emv/cf_net/cf_gross are not nullable, they are ABSENT. It also adds a FIFTH state to DE~D's parallel 'a null has 4 meanings' item -- the column does not exist at all -- which the render side cannot distinguish from the served shape. || NOT CLAIMED BY EITHER SEAT: no producer diagnosis. 'exercise mode' is the producer's OWN manifest self-description; whether it is deliberate or a regression is an ungrounded mechanism claim (Rule 22) and off both seats' spec. The surfacing seat's weak observation (08-11..08-14 are trading days with no partition) is reported-not-chased and the CVO did not investigate it. CVO checked two endpoints plus the five refusals -- a SAMPLE, stated as one; the 529-partition census remains the surfacing seat's measurement with their denominator. || BEARING ON THE CERT, recorded rather than buried: CVO certified ADVI_PERFRP R1 36/36 under the Q-p1 ruling that the projection consumes these live canonical tables. NEITHER the six original bar checks NOR the seventh (oracle viability, added ~1h earlier) would have caught this -- the cells are enumerated, aligned, and their oracles runnable; THE SUBSTRATE'S CONTENT IS A THIRD THING AGAIN. No eighth check is being added by reflex: a certifier who censuses every input table's content is re-doing the DS lane's work. The control that worked is the one that fired -- the executing seat's premise verification against live state, inside an hour of seating. THIRD instance today of an executing seat finding what no document-plane check could see (DE~C's aborting oracle, DE~D's non-existent bundles, this). That is the session's strongest evidence that premise-primitives-first is load-bearing rather than ceremonial."
 },
 {
  "id": "ADVI_PERFRP-S4",
  "surfaced_by": "0.4.0_DS_ClientPlatform~G (executing seat, on their own criterion, before asserting anything) -- MUTATION-PROVEN, not argued",
  "surfaced_at": "2026-08-24T23:18Z",
  "one_line": "PRF-a-2/AC3's gains-identity assertion is ALGEBRAICALLY INCAPABLE OF FAILING: market_growth is computed as the RESIDUAL and the drift check then tests the identity CONTAINING that residual, so it reduces to d_aua - d_aua = 0 for ANY inputs -- 6 of 6 mutants passed at drift 0.0000000000, including zeroed income, sign-flipped fees and 100x-inflated NNA.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "data/assets/scripts/gold/runners_49f/c00_account_gains.py:113 -- market_growth = d_aua - nna_total - income + fees_tax (the RESIDUAL)",
    "same file :145-146 -- drift = abs(d_aua - (nna_total + income - fees_tax + market_growth)); substituting :113 gives d_aua - d_aua = 0 for any inputs",
    "MUTANTS RUN, not reasoned: income ZEROED -> drift 0.0 PASS; fees SIGN-FLIPPED -> drift 0.0 PASS; nna INFLATED 100x -> drift 0.0 PASS; 6 of 6 including total garbage",
    "proof committed at a84a8ca770, LANDED LOCAL with git branch -r --contains verified = 0 remote branches (the seat stated its own push state)"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "PUREST INSTANCE OF THE NIGHT'S PATTERN: CONTROLS_OVER_CARE's 'an instrument that could not have said otherwise', sitting inside an ACCEPTANCE CRITERION of a decomp the CVO certified 36/36. It is a floating-point representation test wearing a correctness test's clothes. || WHAT MAKES THE REPORT EXEMPLARY AND IS THE REUSABLE HALF: the seat did NOT argue vacuity from algebra. They noted that a claim a check is vacuous is ITSELF a claim, and ran the mutant battery to prove it -- corrupting inputs that each move a number an advisor reads. An algebraic argument would have been correct and would have been an assertion; the mutants are a measurement. || CERTIFIER NOTE: neither check 2 (CE against the declared layer) nor check 7 (oracle viability) reaches this. The oracle EXISTS and is RUNNABLE -- it simply cannot return a failing verdict. That is a THIRD property distinct from enumeration and from viability, and I am NOT minting a check 9 by reflex: an assertion's discriminating power is exactly what a mutant battery measures, and requiring the EXECUTOR to mutate their own acceptance assertions is cheaper and better-placed than a certifier re-deriving every criterion's algebra. Surfaced to CTO/COO as a candidate obligation on TO acceptance rows, not implemented."
 },
 {
  "id": "ADVI_PERFRP-S5",
  "surfaced_by": "0.7.0_AE_CloudOps~G (executing seat, on their OWN cell, against a ruling that had just been issued to them)",
  "surfaced_at": "2026-08-24T23:10Z",
  "one_line": "PRF-c-1's ruled per-entity key fan-out collides with the estate's single serving producer: d_publisher_port.py has NO branch on which an emitter can produce a data-dependent object set under a prefix -- every path binds ONE statically-named local file to ONE derived key -- so the cell as ruled is 'extend the publisher with a fan-out mode, THEN add 11 entries', a materially different build.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "d_publisher_port.py:421 publish_one -- serve_key = f'{SERVE_ROOT}/{row[leaf]}': ONE key from ONE static leaf name",
    "run_emitter -- row['leaf'] = spec.get('leaf'), argv += ['--out', str(out_p)]: ONE fixed local path",
    "pair_leaves -- TWO fixed paths; run_d13 multi -- THREE fixed names, all enumerated STATICALLY from the dict",
    "known_leaves / total_leaves / hold_leaves are all statically enumerated; no branch accepts a data-dependent object set"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "The seat refused to start a materially larger build on their own reading of an issuer message -- 'I am not starting it on my own reading of your message' -- which is the correct handling of a spec/estate collision and the opposite of quietly absorbing scope. Routed to the issuer for the ruling; nothing built, nothing edited, no criterion flipped. NOTE THE DIRECTION: this seat is reporting that their OWN cell is bigger than it was ruled, which is the report a lane has the least incentive to make."
 },
 {
  "id": "ADVI_PERFRP-S6",
  "surfaced_by": "0.4.0_DE_ClientPlatform~D (executing seat, on first contact with d-6, before writing picker code)",
  "surfaced_at": "2026-08-24T23:20Z",
  "one_line": "SI is not max: 'max' is DATA-DEFINED (the extent the payload happens to carry) while contract SI is RULING-DEFINED (pinned to the Schwab floor with a REQUIRED label 'since 2024-07-08'), so wiring SI -> max renders a declared label over a window whose true extent is whatever the data spans -- and STITCH is a scheduled event that makes them diverge.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "THREE non-aligning period vocabularies measured: RfsWindow types.ts:1141 = 3 values; FeeEfficiencyWindow types.ts:1818 = 5 values; contract PERIODS perfrp_contract.py:78 = 6 values (RATIFIED)",
    "payload carries decomposition_qtd/_ytd/_max ONLY (types.ts:1327-1329, 2484-2486, 2514-2518)",
    "contract SI_FLOOR_DATE = 2024-07-08 with SI_LABEL fixed, per PRD s.11 #10, which also names two labelled segments once the stitched tier exists",
    "upstream already treats MAX as series-extent rather than a named period: NNA window_bounds keys are QTD|YTD|MAX|1Y|3Y (types.ts:2236) -- MAX coexists with 1Y/3Y as its own key"
   ]
  },
  "disposition": "GRADUATED",
  "notes": "THE EPISTEMIC HANDLING IS THE PART TO CITE: the seat explicitly declined to assume SI and max coincide on today's data -- 'the equivalence is a RULING about what SI means, not a measurement I can take'. They could have measured today's extent, found it equal, and shipped; instead they identified that a measurement cannot settle a definitional question. Blocks ONE value, not the cell. Ties to ADVI_STITCH: the divergence is not hypothetical, it is scheduled."
 }
]
```
