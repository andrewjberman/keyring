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
 }
]
```
