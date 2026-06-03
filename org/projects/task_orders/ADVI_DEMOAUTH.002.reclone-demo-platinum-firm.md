<task_order>
<metadata>
  <to_id>ADVI_DEMOAUTH.002</to_id>
  <project>ADVI_DEMOAUTH (demo restore — pivoted from auth to data-clone after HAR root-cause)</project>
  <title>Re-clone the MISSING demo platinum/firm/* (+ audit the full 9,282-vs-22,253 prefix gap) through the ADVI_DEMOV1 pseudonymizer — PII-SAFE, NOT a raw copy. This is the ACTUAL demo-render fix.</title>
  <assigned_to>DS / ADVI_DEMOV1 pseudonymizer owner (data/demo/scripts/transform/) — DS offline at issue-time; spawn-tonight-vs-next-session = Andrew's call</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>active — pending DS availability (offline EOD); dispatch on DS spawn (Andrew decides tonight vs tomorrow)</status>
  <dispatch_held>true (no live DS; Andrew-decides spawn timing)</dispatch_held>
  <priority>Andrew-wants-demo-back; NOT on-fire (internal/sales tool). But it's the real fix for a user-facing broken surface.</priority>
  <references>
    <ref type="root-cause">0.6.0 HAR analysis (Andrew localhost, andrew@opalinvest.com internal admin) 200623Z: /api/scoped/advisor-intelligence/platinum/firm/{header_metrics_fresh,leaderboard,partner_analytics_*,timeseries_overview,cohort_a_summary}.json?firm=demo -> ALL 403 (S3 AccessDenied, JWT attached = NOT auth; 403-not-404 = missing object w/ ListBucket denied). opal-data-demo/platinum/firm/ = 0 objs vs opal-data-bd/platinum/firm/ = 14. Firm-landing (default opal-user ADVI view) fetches the missing firm/* -> no render. advisors/ IS cloned so per-advisor drill works; the FIRM LANDING is the broken surface.</ref>
    <ref type="magnitude">opal-data-demo = 9,282 objs vs original ~22,253 (~58% complete) -> firm/ may NOT be the only short prefix. AUDIT all prefixes for clone-completeness.</ref>
    <ref type="why">firm-level rollups never cloned OR dropped in the ADVI_DEMOV1 snapshot-clean rollbacks (2,072+884 version-deletes during that saga). "Used to have it" = present originally, lost since.</ref>
    <ref type="orthogonal">ADVI_DEMOAUTH.001 (opal-partner-demo partner-table) was ORTHOGONAL — internal opal users get ALL+admin-bypass (no partner-table/firmRole needed). .001 is harmless + a durable asset for a FUTURE external demo@demo.test login, but NOT this fix. 0.6.0 flagged this honestly.</ref>
  </references>
</metadata>

<scope>
The demo AdvisorIntelligence firm-landing is blank because opal-data-demo is missing platinum/firm/* (and likely more — the clone is ~58% complete). Re-clone the missing artifacts from opal-data-bd THROUGH the ADVI_DEMOV1 deterministic-seeded pseudonymizer so the demo is restored WITHOUT leaking real 49F PII.

## CONCRETE PREFIX-GAP MAP (0.6.0 full audit 201316Z — bd vs demo under platinum/):
   firm/      bd=14      demo=0       <- 100% MISSING (firm-landing rollups = Andrew's symptom)
   clients/   bd=14,922  demo=1,795   <- ~13,127 MISSING (~88% short) = the BULK of the gap; most client-detail drilldowns would 403 too
   advisors/  bd=887     demo=886     <- ~complete (off by 1, no re-clone)
   accounts/  bd=6,600   demo=6,600   <- COMPLETE (no re-clone)
   TOTAL bd 22,424 vs demo 9,282 (~41% present). SIZING: ~13.1k-object re-clone = a multi-hour DS job (the original ADVI_DEMOV1 clone ran ~hours), NOT a quick patch. Likely also wants a re-clean/verify pass (gap came from the snapshot-clean version-delete saga).

## REQUIRED:
1. Re-clone platinum/firm/* (14 objects: header_metrics_fresh, leaderboard, partner_analytics_*, timeseries_overview, cohort_a_summary, + the rest) from opal-data-bd/platinum/firm/ -> opal-data-demo/platinum/firm/.
1b. Re-clone platinum/clients/* (~13,127 missing objects) — restores client-detail drilldowns (currently only 12% present).
2. **PII-SAFE — MUST go through the ADVI_DEMOV1 pseudonymizer (data/demo/scripts/transform/) using the SAME fake_identities mapping**, NOT a raw S3 cp. Firm artifacts (leaderboard, partner_analytics) carry advisor NAMES + numbers = PII. The fake advisor names in firm/leaderboard MUST match the already-cloned advisors/ (deterministic seed) or the demo is internally inconsistent (leaderboard names != advisor-detail names). This is the critical correctness+PII constraint.
3. AUDIT the full prefix gap: opal-data-demo 9,282 vs original ~22,253 (~13k objects short). Enumerate which prefixes under opal-data-demo/platinum/ (and elsewhere) are short vs opal-data-bd, and re-clone any other missing firm-or-render-critical prefix through the pseudonymizer. firm/ is the confirmed-broken one; there may be others (the firm-landing was just the first surface Andrew hit).
4. Verify served: after re-clone, the platinum/firm/*.json?firm=demo fetches return 200 (not 403), and the firm-landing renders. Then re-smoke (Andrew visual).

## DO NOT:
- Raw S3 cp from opal-data-bd (leaks real 49F PII into demo).
- Clone without the deterministic fake_identities mapping (breaks leaderboard<->advisor-detail name consistency).
</scope>

<acceptance>
- [ ] platinum/firm/* (14 objs) re-cloned to opal-data-demo via the ADVI_DEMOV1 pseudonymizer (fake_identities mapping, deterministic seed). RAVC1 the method + the PII-safety to COO.
- [ ] Full prefix-completeness audit (9,282 vs ~22,253): enumerate short prefixes, re-clone any other render-critical missing ones (pseudonymized). Report the gap.
- [ ] Served-verify: platinum/firm/*.json?firm=demo -> 200 (was 403); names in firm/leaderboard match advisors/ detail (consistency).
- [ ] Andrew fresh-login visual smoke = demo firm-landing renders -> ADVI_DEMOAUTH close.
</acceptance>
</task_order>
