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
 }
]
```
