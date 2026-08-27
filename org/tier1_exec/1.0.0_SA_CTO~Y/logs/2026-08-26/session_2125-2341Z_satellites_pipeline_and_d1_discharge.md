# 1.0.0_SA_CTO~Y -- Opal Satellites (commission -> registered -> subsumed -> site-Z) + D1 discharge cert

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, VALIDATE, SCRIBE
**Window:** 2026-08-26 ~21:25Z -> 23:41Z (since `session_2050-2120Z_d1catviews_recert.md` @65069aab10)

## What happened

### Thread 1 -- Opal Satellites: Andrew-direct commission driven to full pipeline entry

Andrew, live at this terminal, commissioned a read of the Tax SMA Teams thread (Manav Shah / Yang
Liu / him) on a new Cottonwood product -- "Opal Satellites," fixed-weight blends of 1-2 Opal models
each -- and a fold-in brainstorm for the portal. Sequence, each word verbatim-recorded + committed
same turn per the record+broadcast law:

1. **Commission + figure-provenance ruling** (@6c3c05e4da): thread read via opal-gateway
   (chat 19:d43ca87dc...); both images parsed locally (his files); RULED the images bind STRUCTURE
   only, figures never authoritative.
2. **Positioning redirect** (@a757e0568e): fold-in = the POSITIONING page, third top-of-page mode
   pill beside MODELS & ETFS, Cottonwood firm-id + Opal only. Viability read delivered: the
   bookSet.ts declared-membership axis + the POSN_CUSTOM.001 custom-blend engine make satellites
   the built-for path; all Positioning Summary sections (yield incl.), Portfolio Composition,
   Holdings Breakdown derivable client-side from served model payloads. Name gate closed by his
   ruling **'Opal Conservative Growth' == LT**.
3. **/open-calls** (2 cards) -> both ruled (@d376f68b8f): Call 1 register-D4 APPROVED; Call 2 --
   **weights come DIRECTLY from the rebalancing pipelines' displayed weights**, the basis for all
   per-satellite Characteristics/Performance/Weights.
4. **Registration + stage-2 PRD** (@25b116f8ac): `org/projects/ETFS_SATELLITES.json` + REGISTRY row
   + `docs/architecture/D4_OPAL_SATELLITES_PRD.md`. Substrate MEASURED at registration:
   - weights LIVE daily at `s3://opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_model_detail/{date}/{id}.json`
     field `hierarchy.children[].relativeAllocation` (producer cot-rebalancer-runner :20/:314,
     opal_closure seeding covers Opal-named satellites by construction); EXERCISED: Opal Satellite
     40 = Opal Intermediate-Term 0.5 + Opal Short-Term 0.5 (today's partition).
   - roster census 64 models, **TEN Opal satellites** {15,30,40,50,60,70,80,90,98,UltraShortTerm}
     -- **Satellite 98 (11 accounts) ABSENT from Manav's image**; PRD fixes membership as the
     measured predicate, never a hand list.
   - the one new seam: **zero firm-id references** in portal/src/pages/Positioning/ today.
5. **Placement seam** (COO 73957, correct question): my registration's bare `placement: laptop` was
   a REC in a ruled-reading field -- owned + repaired (@96f5f4edfb, AT-ANDREW with the rec
   labelled); COO 73971 carries it as the first measured NFRA_TORECORD-class instance in a project
   JSON. MSTR closed the register membership gap (D4 += ETFS_SATELLITES @5780da5da5, ON origin).
6. **Subsumption ruling** (@2acd5d7098), VERBATIM: *"Yes this needs to subsume D4 if it has not
   already."* Full D4 membership (MSTR's append satisfied the 'if not already'); no carve-out ->
   the D4 row's placement-attaches-to-the-directive clause resolves placement **SITEZ**; laptop
   COO RELEASED from the stage-3 decomp; assignment routed to the site-Z fabric's COO lane via
   MSTR (carry follows the next integrator publish, since the packet rides integration).

### Thread 2 -- D1_CATVIEWS discharge cert

COO's absorbing amendment s.4b landed @eb73d94342 (signal 73756) and the same-day re-read ran
same-turn: **CERTIFIED -- 36 cells, four postulates PASS, my whole-artifact refusal DISCHARGED**
(@961cee64fe). All 14 findings verified absorbed (A1-A5 -> k-1..k-4 + i-3; B1-B9 unsoftened);
i-3's (i)-placement CONCURRED on independent derivation; the TO-I1-DS trap confirmed (i-3 joins
the surface, not the TO); second CE hunt over the amended domain found no further member. Two
non-blocking riders: superseded oracles still standing in the s.2 tables (restate before criteria
cut) + the 'Amended cells: 9' count convention. NOTHING-ELSE-CUTS lifted; NO-SHIP untouched.

### Law traffic absorbed

Rule 29 minted (report is not the deliverable while unblocked work remains -- applied throughout
this window); CLAUDE.md slimmed 707 -> 262 -> 215 lines (index + annex; my loaded copy is the
superset; no rule changed). All broadcasts ACKed on the READ clock.

## MCP traffic

~14 in / ~9 out this window. Significant: COO 73756 (amendment signal) -> discharge cert out
73813-15; Andrew-direct relays out 73738-40, 73827-28; /open-calls execution out 73952-55 (+MSTR
D4-append 73969 back); placement seam 73957 in -> 73960-62 out -> subsumption execution 74037-40
out. Zero QUEUED/REFUSED across all sends.

## Files Modified

See commit messages: @6c3c05e4da, @a757e0568e, @d376f68b8f, @961cee64fe, @25b116f8ac, @96f5f4edfb,
@2acd5d7098 (each carries its own per-file account). Net new artifacts: ETFS_SATELLITES.json,
D4_OPAL_SATELLITES_PRD.md, the REGISTRY row, the Andrew-direct record + its four amendments, the
discharge-cert addendum.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-find --name '*Positioning*' / 'category-views.json' etc. | PASS | located the page plane + producer absence for the serving trace |
| comp-find --name '*gateway*' | PASS | located gateway source (image-fetch path, superseded by Andrew's local files) |
| .tools/aws s3 ls/cp (rebalancer bronze) | PASS | roster + Satellite-40 detail pulled; full-bucket recursive ls was the wrong first call (timed out, backgrounded; narrowed to exact prefix) |
| rail nudge honored | PASS | one gated grep re-run with `# rail-checked` on a single named .py |

What worked: the serving-chain/estate reads from the D1 session transferred directly to the
Positioning viability read -- zero re-derivation. What failed: the first S3 sweep (recursive over
the monolith bucket) -- instrument mis-sized, corrected to prefix-scoped. Gap found: none new
(the to-check lane-zero class did not arise; work arrived by dispatch + Andrew-direct).

## Blockers

None at this seat. ETFS_SATELLITES next actor is the site-Z COO lane (stage-3 decomp), carried by
[0.0.0_AB_MSTR] cross-device after the next integrator publish -- an external gate by design, not
a blocker here.

## Current State (handoff-grade)

- **ETFS_SATELLITES**: registered (macro ETFS, directive D4, `dep_stage: PRD`), SUBSUMED into D4 by
  Andrew's verbatim word, placement **SITEZ** via the directive clause, stage-3 decomp at the
  site-Z fabric's COO lane. Packet: `org/projects/ETFS_SATELLITES.json` + REGISTRY row +
  `docs/architecture/D4_OPAL_SATELLITES_PRD.md` + verbatim record
  `org/tier1_exec/1.0.0_SA_CTO~Y/deliverables/ANDREW_DIRECT_20260826_OPAL_SATELLITES_CW_DISPLAY.md`
  -- all LOCAL, rides integration. Open questions (non-gating, owners named in PRD s.5):
  characteristics-beyond-yield (Manav via Andrew), Satellite-98 display membership (defaults IN by
  predicate), performance-in-v1 sizing (decomp owner).
- **D1_CATVIEWS**: re-cert seat obligations FULLY DISCHARGED. Refusal record + discharge addendum:
  `org/tier1_exec/1.0.0_SA_CTO~Y/deliverables/D1_CATVIEWS_DECOMP_RECERT_20260826.md`
  (@81f3dbac08 + @961cee64fe). Criteria may cut on the 5 new + 9 amended cells honoring rider (1)
  (oracle restatement); TO-I1-DS proceeds; NO-SHIP holds until Andrew's by-name lift.
- Watcher: task bu36ri3sw, live. Inbox: drained, all ACKed. Tree: clean at this seat's paths.

## Next Steps

1. **[site-Z COO lane, via 0.0.0_AB_MSTR carry]** ETFS_SATELLITES stage-3 atom-decomp (Rule 27).
2. **[2.0.0_SA_COO]** D1 criteria cut on the amended cells with the oracle-restatement rider.
3. **[1.0.0_SA_CTO~Y]** none pending -- event-driven; responds to the site-Z fabric or Andrew.
