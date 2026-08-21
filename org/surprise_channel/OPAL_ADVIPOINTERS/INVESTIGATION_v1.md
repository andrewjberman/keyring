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
NARROWER than today's tenancy boundary. **But `platinum/mdpf/` already holds five firms in one
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

```json
[
 {
  "id": "OPAL_ADVIPOINTERS-S1",
  "surfaced_by": "0.4.0_DE_ClientPlatform",
  "surfaced_at": "2026-08-21T16:40Z",
  "one_line": "the route's tenant assertion compares RESOLVED BUCKETS, which encodes tenancy at the old topology's granularity -- the property breaks the moment platinum/advi/ holds a second firm, as platinum/mdpf/ already does with five",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "DE 65048 read of the landed router: the assertion precedes origin selection (:333 before :337/:344/:346), so a cross-firm request never reaches S3 -- the control fired as scope_denied, not as a 404",
    "platinum/mdpf/ holds five firms in one bucket -- bucket-as-tenant is already false elsewhere in the estate",
    "re-listed at DE's seat: platinum/advi/ holds 49financial only, so it is not exploitable today",
    "CTO 65005 ruling: resolved-bucket equality is the CORRECT encoding of the 64842 bound, not a loosening -- a bare pathFirm===firmId would refuse two legitimate identities and NARROW the boundary"
   ]
  },
  "disposition": "GRADUATED",
  "disarm_owner": "0.7.0_AE_CloudOps",
  "notes": "ARMED because publishing a second firm's twins is a NORMAL act of this program with everything else in place. Disarm is already shaped and ruled: advTenant declaration-based tenancy, which does not expire when firms co-locate. Its Rule-24 record must declare what an identity with NO advTenant asserts against (COO 65128: the CE half against the declared layer) -- fail-closed BY CONSTRUCTION AND STATED, never by luck of how the comparison happens to be written."
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
 }
]
```
