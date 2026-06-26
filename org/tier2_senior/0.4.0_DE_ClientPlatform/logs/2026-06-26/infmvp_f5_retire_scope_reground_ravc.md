# INFMVP.F5-retire migration scope -- re-ground against live tree + RAVC2 to COO
**archetype:** TRACE
**secondary_archetypes:** VALIDATE, SCRIBE

**Session:** 2026-06-26 (~13:03-13:10Z) · **Agent:** 0.4.0_DE_ClientPlatform · **Dispatch:** NNA-scope F5-retire (COO 214400Z item-3) · **Commit:** `d65b60425`

## Current State

After P2-1 was DE-side ACCEPTED + event-gated (see sibling log), COO redirected me to my live actionable lane:
the NNA-scope **F5-retire dispatch** -- migrate the partner_analytics ADV-NNA donut SOURCE (bd-gold D_01) to emit
canonical all-roles, retiring the latent-fragile FE override in DistributionTab. Deliverable = a migration
SCOPE/PLAN for COO to formalize into a tracked TO (analysis only, NOT the cutover -- safe under Andrew's still-
pending F5-vs-Cottonwood sovereign call).

Found I had AUTHORED the scope doc last session (~22:43-22:48Z) but NEVER COMMITTED it (it sat uncommitted in the
working tree; committed as a NEW file today). Header claimed "verified this session" = 06-25 = stale for a new
session. So I **re-grounded every source anchor** against the live portal DEV tree + bd-gold before RAVC'ing it to
COO (who formalizes it into a TO -- stale anchors would propagate into the TO). Three drifts caught + corrected:

1. **Path moved:** `DistributionTab.tsx` -> `_shared/tabs/DistributionTab.tsx` (my own FE1 `_shared/{tabs,panels}`
   refactor). Line anchors shifted: override block now **2601-2638**, `canonicalNna` fetch now **925**.
2. **MATERIAL correction:** `canonicalNna` is NOT prunable on the donut-retire. DistributionTab's own `heroMetrics`
   (1535-1550) reads `canonicalNna.{firm,state,city,advisor,client}.windows[W]` at every grain, independent of the
   donut override; AdvisorAnalytics + AdvisorPublicProfile also consume it. So the retire prunes ONE block
   (2601-2638), NOT the fetch -- a cleaner/smaller/lower-risk FE change than the draft implied. Step-3 corrected,
   open-item-2 resolved.
3. **Lineage strengthened** (`comp-pipescript io D_01`): D_01 ALREADY READS canonical NNA (`gold/canonical/nna/`
   <- C_01 + `nna_aua_by_advisor.parquet`) -> the migration is a re-source WITHIN D_01, no new cross-script dep,
   no new melt (kills the D_00c-class inline-reimpl risk CVO flagged). Producer path corrected
   (`data/black_diamond/scripts/gold/D_01.partner_analytics.py`; cot D_01 = SEPARATE firm, never touch); exact
   producer fn/lines flagged for DS confirm (06-25 `build_nna_adv_view` name unverified; live grep -> the
   `primary_role=='architect'` donut filter ~line 983).

Corroboration: the live override comment block (2601-2611) itself documents this exact P2 migration as the known
clean fix. Committed d65b60425, pushed. RAVC2'd COO (131004Z) with the scope + the one blocking ruling.

## Blockers
None blocking ME. Build is gated on (a) COO formalizing the TO + routing the **donut whole-semantics ruling**
(A all-roles+disclosed-overlap / B primary-role-additive / C dual-emit; my rec C-or-A), and (b) Andrew's
F5-vs-Cottonwood sovereign call (higher priority -- the whole F5 thread shelves if he picks Cottonwood). Both
genuine external gates, not idle.

## Next Steps
- **[2.0.0_SA_COO]** formalize the scope into a tracked TO + loop CVO verify-leg; route the whole-semantics ruling (DS/CVO/maybe Andrew).
- **[Andrew]** F5-vs-Cottonwood -> determines whether the F5 thread proceeds at all.
- **[0.4.0_DS]** confirm exact D_01 producer fn/lines + concur on the read-canonical single-source path.
- **[0.4.0_DE, me]** on GO + whole-semantics ruling: FE donut-override removal (2601-2638 only) + schema-check/ternary-audit + per-firm served regression + co-author the tie-out spec.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-which` | "where is the INFMVP F5 frontend override that melts partner_analytics advisor roles in the donut" | Routed to my own existing scope deliverable + D_01 sites; confirmed the override label/site set to re-ground. |
| `comp-pipescript io` | `comp-pipescript io data/black_diamond/scripts/gold/D_01.partner_analytics.py` | KEY FINDING -- D_01 READS canonical NNA already (`gold/canonical/nna/` <- C_01 + `nna_aua_by_advisor.parquet`); writes header_metrics/canonical_role_aua/aua_cert. Grounds the "re-source within D_01, no new dep" recommendation deterministically (vs grep). |
| `Grep`/`Read` (FE re-ground) | locate `_shared/tabs/DistributionTab.tsx`; map `canonicalNna` consumers (925 fetch / 2601-2638 donut override / 1535-1550 heroMetrics) | The donut override + heroMetrics are distinct consumers -> the material step-3 correction (fetch stays). Native Read/Grep on portal .tsx (operational, off-rail per the Read/pipe-grep carve-out). |

comp-which was the entry rail; comp-pipescript io carried the producer lineage. No raw-aws/raw-repo-grep override needed.
