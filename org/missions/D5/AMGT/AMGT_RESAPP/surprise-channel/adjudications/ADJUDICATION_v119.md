# AMGT_RESAPP -- round 98 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-11T23:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T23:10:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 4159,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round98/DRAIN_END_PACKET.md @b3d4856531 (blob 625f129f8e, sha256 63f63b32..., verified).
2 of 2 orders complete. be-1 is cited from AMGT_CORPUS round 48's grade (400c84ed5c) and not re-graded (C-S94). The one JUDGMENT, be-2 AC2, is MET
(C-S95). 2 rows swept since v118 (watermark 2026-10-11T21:30Z; 2 of 1074 investigation rows after it): both dismissed. No BLOCKING or ARMED row is
open on this project's carrier from this round (AMGT_CORPUS-D1-C-S64 is ARMED on AMGT_CORPUS's own carrier).

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S94",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T23:10:00Z",
    "one_line": "be-1 (the /13 corpus redeploy, IpaCHo5h -> mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w=, applied 22:14:54Z, held under the CTO's KEEP) is NOT re-graded here: its served page is graded in AMGT_CORPUS's own channel, round 48, commit 400c84ed5c (ADJUDICATION_v63: FWD-12 MET; FWD-20 PARTIAL with a new ARMED row AMGT_CORPUS-D1-C-S64, 62 case-block rows rendering under history years on 13 names). That ARMED row lives on AMGT_CORPUS's carrier and is not carried here. This seat confirmed the live CodeSha256 mbGRmy1H.. and ran no live sweep of the function this round (the packet's own overlap control: a sweep beside an applier's replay is how round 98's 29 s timeout arose).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "be-1 (the /13 corpus redeploy, IpaCHo5h -> mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w=, applied 22:14:54Z, held under the CTO's KEEP) is NOT re-graded here: its served page is graded in AMGT_CORPUS's own channel, round 48, commit 400c84ed5c (ADJUDICATION_v63: FWD-12 MET; FWD-20 PARTIAL with a new ARMED row AMGT_CORPUS-D1-C-S64, 62 case-block rows rendering under history years on 13 names). That ARMED row lives on AMGT_CORPUS's carrier and is not carried here. This seat confirmed the live CodeSha256 mbGRmy1H.. and ran no live sweep of the function this round (the packet's own overlap control: a sweep beside an applier's replay is how round 98's 29 s timeout arose).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "AMGT_CORPUS commit 400c84ed5c (ancestor of box/dell1 HEAD), its ADJUDICATION_v63",
        "3.0.0_SA_CVO lambda get-function-configuration opal-amgt-scoped-api 2026-10-11T23:0xZ: mbGRmy1H..",
        "round98/DRAIN_END_PACKET.md sections 1-3"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "be-1 (the /13 corpus redeploy, IpaCHo5h -> mbGRmy1Hnh7M6Gtt9LchHPmt17lYS/oyCl6s10lJO+w=, applied 22:14:54Z, held under the CTO's KEEP) is NOT re-graded here: its served page is graded in AMGT_CORPUS's own channel, round 48, commit 400c84ed5c (ADJUDICATION_v63: FWD-12 MET; FWD-20 PARTIAL with a new ARMED row AMGT_CORPUS-D1-C-S64, 62 case-block rows rendering under history years on 13 names). That ARMED row lives on AMGT_CORPUS's carrier and is not carried here. This seat confirmed the live CodeSha256 mbGRmy1H.. and ran no live sweep of the function this round (the packet's own overlap control: a sweep beside an applier's replay is how round 98's 29 s timeout arose)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S95",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T23:10:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-be-2.read-which-thesis-payload-keys-each-portal-build-reads AC2: MET. The three outcomes (fiscal_year_figures, model.fiscal_year_figures and check_face each READ-BY-BOTH) follow from the evidence: this seat's git grep of origin/DEV 44ec7e70a9 and origin/PROD 37aa1247ee reproduces every counted site, the control (team_sheet: DEV 2, PROD 0) distinguishes the builds, current origin/DEV changes nothing under src/pages/SecurityAnalysis, and one live thesis read shows the served payload carries all three keys. No unread surface can reverse an outcome: the built bundles, print renderers and the route server could only add reads, and the other API clients sit outside the question though any later removal must census them. One packet paraphrase is narrower than the code: the footer's time list reads only the model-block vintage.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "This seat's re-run of section 4 in the nested portal (git grep -n -e fiscal_year_figures -e check_face <ref> -- src, harness excluded) at the reading's refs origin/DEV 44ec7e70a9 and origin/PROD 37aa1247ee reproduces every counted site: fiscal_year_figures at ModelTab.tsx:593/:602 (DEV) and :543/:550 (PROD), CardFooter.tsx:188 and postureCites.ts:369 in both; model.fiscal_year_figures only as string paths at CardFooter.tsx:187-188 in both; check_face at the six ModelTab.tsx sites per build; CardFooter.tsx:192 (whatChangedSources) present and uncounted. The control team_sheet reads DEV 2 (ModelTab.tsx) and PROD 0, so the sweep distinguishes the builds. Current origin/DEV ad774c6f has moved past 44ec7e70a9 but changes nothing under src/pages/SecurityAnalysis (git diff --stat empty), and origin/PROD is unchanged at 37aa1247. The footer code (CardFooter.tsx footerFor.model at 44ec7e70a9) reads times from ['generated_at', 'model.generated_at', 'model.fiscal_year_figures[].vintage', 'model.forecast_figures[].vintage'] and sources from ['model.fiscal_year_figures[].source', 'model.forecast_figures[].source', 'fiscal_year_figures[].source'], each path walked by values() on the served bundle, so the model-block key is a real runtime read. One live read of /security/ASML_NA_Equity/thesis on mbGRmy1H.. serves both keys (799 entries each, vintages and sources equal) and check_face, so those paths resolve. Unread surfaces, and whether each could change the conclusion: (a) the built bundles -- cannot reverse READ-BY-BOTH, because every counted site sits in a live component (ModelTab, PostureTab's resolver, the footer called from ModelTab) that a build keeps; a bundle could only add a runtime-computed read; inference. (b) the Thesis route server -- the served key set, read here on one name (measured for ASML only). (c) print and PDF renderers outside src/ -- could only add reads; the reading's whole-tree sweep found no file outside src/ naming the keys. (d) other API clients (mcportal, opal_ai, dry_portal_vite) -- outside the question (the portal's builds), so they cannot change these outcomes, but they bear on any later REMOVAL: a drop must census them first. One correction to the packet's paraphrase, not to the reading: model.fiscal_year_figures is not only an entry of a union list -- the footer's TIME list names model.fiscal_year_figures[].vintage and no top-level vintage path, so it is the footer's only fiscal-year vintage source; only the SOURCE list unions it with the top-level path. A removal of the model-block key would empty that vintage unless the times list is repointed first.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_RESAPP~394/BE2_PAYLOAD_KEY_READING_20261011.md (read whole)",
        "3.0.0_SA_CVO git -C portal grep -n -e fiscal_year_figures -e check_face {44ec7e70a9,37aa1247ee,ad774c6f} -- src; team_sheet counts; git diff --stat 44ec7e70a9 ad774c6f -- src/pages/SecurityAnalysis: empty",
        "3.0.0_SA_CVO git -C portal show 44ec7e70a9:src/pages/SecurityAnalysis/components/CardFooter.tsx (footerFor.model, values(), read())",
        "3.0.0_SA_CVO lambda invoke GET /security/ASML_NA_Equity/thesis on mbGRmy1H..: both keys 799 entries, check_face present"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-be-2.read-which-thesis-payload-keys-each-portal-build-reads AC2: MET. The three outcomes (fiscal_year_figures, model.fiscal_year_figures and check_face each READ-BY-BOTH) follow from the evidence: this seat's git grep of origin/DEV 44ec7e70a9 and origin/PROD 37aa1247ee reproduces every counted site, the control (team_sheet: DEV 2, PROD 0) distinguishes the builds, current origin/DEV changes nothing under src/pages/SecurityAnalysis, and one live thesis read shows the served payload carries all three keys. No unread surface can reverse an outcome: the built bundles, print renderers and the route server could only add reads, and the other API clients sit outside the question though any later removal must census them. One packet paraphrase is narrower than the code: the footer's time list reads only the model-block vintage."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S96",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T23:10:00Z",
    "one_line": "D1-W394-S1 and D1-W394-S2 (INERT) dismissed: the model-block key is read only as dotted string paths walked by CardFooter's values() (confirmed in the code here, and it is a real runtime read, C-S95), and CardFooter.whatChangedSources has no caller in either build (the reading excludes it from the counts, and this seat's sweep finds no caller site).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W394-S1",
      "AMGT_RESAPP-D1-W394-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W394-S1 and D1-W394-S2 (INERT) dismissed: the model-block key is read only as dotted string paths walked by CardFooter's values() (confirmed in the code here, and it is a real runtime read, C-S95), and CardFooter.whatChangedSources has no caller in either build (the reading excludes it from the counts, and this seat's sweep finds no caller site).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W394-S1, D1-W394-S2",
        "adjudication row AMGT_RESAPP-D1-C-S95"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W394-S1 and D1-W394-S2 (INERT) dismissed: the model-block key is read only as dotted string paths walked by CardFooter's values() (confirmed in the code here, and it is a real runtime read, C-S95), and CardFooter.whatChangedSources has no caller in either build (the reading excludes it from the counts, and this seat's sweep finds no caller site)."
  }
]
```
