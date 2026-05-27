# FIND_INSURE Phase 1 RAVC2-Accept template (ready-to-fire at Stage 2 close)

**Authoring:** `2.0.0_SA_COO` 2026-05-27T~23:18Z
**Purpose:** pre-author the joint Tier-1 RAVC2-Accept verdict mechanics for FIND_INSURE Phase 1 close so the accept lands same-cycle when AE 0.7~A Stage 2 closes
**Authority anchor:** Andrew sovereign goal-set 2026-05-27T~22:49Z + [[feedback_cvo_proactive_verdict_landing_pattern]] applied to joint-Tier-1 ratify mechanics
**Status:** TEMPLATE — placeholder fields `{TBD-AT-CLOSE}`; instantiate at Stage 2 RAVC2-Request moment

---

## Trigger conditions (Phase 1 RAVC2-Accept = ALL must hold)

1. **FIND_INSURE.008 Stage 1 PASS** — AC3 grade-json `recommended_proceed: true` (FP≤20% + FN≤20% + empty-body≤40%) AND joint COO+CTO+CVO Stage 1 ACK
2. **FIND_INSURE.008 Stage 2 AC7** — 99/99 IMO prefixes in `s3://opal-data-imo/corp/` confirmed via `aws s3 ls | wc -l` = 99
3. **AC-T1 telemetry emission** — `s3://opal-data-imo/telemetry/` no longer empty; per-IMO `max_depth_reached` + `page_count_vs_max_pages_cap_ratio` records present per PRD AC-T1 (closes CVO (b)(iv) REPAIR-AMENDMENT)
4. **AC-T2 EMPTY-BODY rate evaluation** — universe-wide empty-body rate empirically calculated; if >5-10%, scraping_browser1 v0.3.0 escape-valve dispatched (CVO P4) — does NOT block RAVC2-Accept on Phase 1 first-pass; escape-valve runs as follow-on
5. **CVO Mode B re-grade post-universe-run** — C1 axis F → A flip + W3 re-grade post-`.023` ship + Mode B re-validation acceptance
6. **FIND_INSURE.007 (Rule 17 silver patch)** — ALREADY CLOSED at `3ee6ee869` + RAVC2-ACCEPT-CLOSE `23:08Z`; AC7 sister-deploy via AE Lambda redeploy in this same cycle closes the implementation leg fully
7. **REPAIR-AMENDMENT (a) closure** — PRD §1 + §4 amended by ws CTO to reflect actual 99/99 universe-coverage delivered (closes CVO (a) trigger; ships via /ws-charter cycle in close window)

**REPAIR-AMENDMENT triggers expected to PERSIST past Phase 1 RAVC2-Accept** (do NOT block Phase 1 close):
- (b)(i) W1 threshold semantics — affects Phase 2A subset-cut framework (Andrew Q1 gate); Phase 1 close-eligible without
- (b)(iii) code/ prefix mirror — alignment-class finding; affects future deploy hygiene not Phase 1 substance
- These two close at later Tier-1 or Andrew-gate moments

---

## Joint Tier-1 verdict shape

Per LD-0084 §2 4-shape verdict taxonomy applied to Phase 1 close:

**Most likely outcome: CORROBORATE-with-additives** (per [[feedback_corroborate_with_additives_materializes_immediately]])
- Phase 1 substance: 99/99 IMOs crawled + Rule 17 silver compliance + decision-useful gold scoring per Mode B re-grade
- Additives: (a) AC-T2 follow-on dispatch if empty-body>threshold (b) telemetry/ emission verification (c) rollup_score 100-cap saturation v0.2 refinement candidate per Step 3.5 meaning-axis CONCERN (d) FIND_INSURE.json `phase` narrative refresh to v0.5/v0.6 per CVO Sub-class X authoring-cascade

**LD-0095 verification-class taxonomy:** Phase 1 close is **empirical-smoke-class** (universe-coverage + discrimination-grade), not rationale-narrative-class. CVO Mode B grades the empirical; CTO + COO ratify the substantive close.

---

## Step 1 — `org/projects/FIND_INSURE.json` phase narrative refresh

**Update phase field** (preserve all other fields; this is alignment-metadata + Phase 1 close substance):

```
"phase": "Phase 0 -> Phase 1 CLOSED {TBD-AT-CLOSE: YYYY-MM-DD HH:MMZ} — joint Tier-1 RAVC2-Accept on 99/99 IMO universe-coverage + Rule 17 silver compliance + decision-useful gold scoring. Phase 1 deliverable arc: AE 0.7~A .004 crawl-web Lambda + DS~A .005 parse-web silver + DS~B .006 score-web gold + DS~A .007 Rule 17 passthrough patch (3ee6ee869) + AE 0.7~A .008 99-IMO universe-run 2-stage fan-out (Stage 1 {TBD: commit-hash} + Stage 2 {TBD: commit-hash}). Empirical state at close: 99 corp/{slug}/{bronze,silver,gold}/ medallion prefixes complete; serving/scoring.json STAGED for Phase 3 consolidation .023; telemetry/ AC-T1 records emission confirmed; AC-T2 empty-body rate {TBD: rate}% (escape-valve {TBD: status}). CVO Mode B re-grade C1 F->A + S1 B+ + W3 INCOMPLETE->ADVANCING + M1 METHODOLOGICALLY-MEANINGFUL+EMPIRICALLY-{TBD: complete OR pending-Phase-3}. REPAIR-AMENDMENT triggers closed: (a) mechanical-untruth (via ws CTO PRD amend {TBD: commit}); (b)(ii) Rule 17 silver field-drop (via 3ee6ee869); triggers persisting through Phase 2A: (b)(i) W1 threshold semantics (gates Andrew Q1); (b)(iii) code/ prefix mirror (alignment-class). Phase 2A entry: STANDBY-PREP-READY per .011 skeleton ship; gates on Andrew Q1 subset-cut ratify + FIND_INSURE.024 LIVE-DISPATCH STAGED. Phase 2B entry: STAGE Bα HAR-staged per Andrew supply; FIND_INSURE.025 HAR parser STAGED. Phase 3 close-gate: .023 serving consolidation + IR-team consumer sign-off via .021 protocol + Phase 3 close-commit template at docs/briefs/find-insure-phase3-close-template.md (3-step atomic ready-to-fire).",
"blocking": "(1) Phase 2A entry — Andrew Q1 subset-cut decision (top-quintile + Series-license-mention OR refined) — sovereign gate. (2) Phase 2B Stage Bα entry — Andrew HAR captures for job-postings boards (Glassdoor + Indeed + LinkedIn-jobs) — sovereign gate. (3) Phase 3 close-gate — IR-team consumer individual identification per CVO ADDITIVE-1 — sovereign gate. (4) Rolling: ws CTO PRD v0.7 scribe absorbing (b)(i) W1 threshold + (b)(iii) code/ mirror + (b)(iv) telemetry/ AC-T1 record write-through if any persist. (5) DS~E .022 + .023 Phase 3 enabling ship — STAGED + pre-staging design + code per [[feedback_pre_staged_recovery_path_pattern_delivers_autonomous_post_cap_dispatch]]."
```

**Surgical-edit pattern:**
```bash
jq --arg phase "$PHASE_NARRATIVE" --arg blocking "$BLOCKING_NARRATIVE" \
  '.phase = $phase | .blocking = $blocking' \
  org/projects/FIND_INSURE.json > /tmp/FIND_INSURE.json.tmp \
  && mv /tmp/FIND_INSURE.json.tmp org/projects/FIND_INSURE.json
jq . org/projects/FIND_INSURE.json | head -20  # validation
```

---

## Step 2 — Joint Tier-1 RAVC2-Accept commit

Single COO-authored commit landing the Phase 1 close — Phase 1 RAVC2-Accept is NOT the project close (Phase 3 close is); this is just the Phase 1 leg ratify.

```bash
.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" \
  -m "FIND_INSURE(Phase 1 RAVC2-Accept): joint Tier-1 ratify on 99/99 IMO universe-coverage + Rule 17 silver compliance + decision-useful gold scoring. Stage 1 grade {TBD} + Stage 2 universe AC7 {TBD} + AC-T1 telemetry emission verified + AC-T2 empty-body rate {TBD}%. CVO Mode B re-grade C1 F->A + S1 B+ post-Rule-17-fix + W3 INCOMPLETE->ADVANCING (Phase 3 .023 staged). REPAIR-AMENDMENT (a)+(b)(ii) CLOSED; (b)(i)+(b)(iii)+(b)(iv) PERSIST per CTO PRD scribe schedule. Andrew goal-set 22:49Z driving toward Phase 3 close — Phase 2A entry next-gate per Andrew Q1 subset-cut ratify." \
  -- org/projects/FIND_INSURE.json
```

---

## Step 3 — RAVC2-ACCEPT MCP fanout

Joint Tier-1 verdict notification (no formal multi-author commit; each Tier-1 issues their own ACK):

- **ws COO MCP to AE 0.7~A:** `[RAVC2-ACCEPT-CLOSE] FIND_INSURE.008 Phase 1 RAVC2-Accept — joint Tier-1 ratify confirmed; Stage 2 universe AC7 close discharge` — closes the .008 RAVC2 loop
- **ws COO MCP to MSTR:** `[Phase 1 CLOSED] FIND_INSURE — joint Tier-1 RAVC2-Accept; Phase 2A entry next-gate per Andrew Q1` — fabric awareness
- **CVO MCP (independent):** Mode B re-grade artifact + verdict close
- **CTO MCP (independent):** REPAIR-AMENDMENT (a) PRD §1+§4 amend ship + close

---

## Post-Phase-1-Accept discipline

After Phase 1 RAVC2-Accept lands:

1. **Heartbeat COO** with Phase 1 close + Phase 2A entry-gate status
2. **Fire `[GO] FIND_INSURE.023`** to DS~E (gate-clear; .023 empirical run can now execute against the 99-IMO universe gold output)
3. **Surface to Andrew:** `[ANDREW-GATE] Phase 2A Q1 subset-cut decision ready for ratify — Phase 1 ranked output at serving/scoring.json post-.023-ship` (this fires post-.023 since the consolidated table is needed for the subset-cut to be operative)
4. **Drive log:** write `org/tier1_exec/2.0.0_SA_COO/logs/{YYYY-MM-DD}/coo_drive_cycle_{N}_find_insure_phase1_ravc2_accept.md`
5. **/allocation cycle:** SPAWN-NEEDED forecast for Phase 2A/2B (DS~C + DS~D LIVE) — surface to MSTR

---

## Template-instance pre-fill discipline

This template is the **fire-at-Stage-2-close** artifact. At Stage 2 AC7 RAVC2-Request moment, ws COO substitutes `{TBD-AT-CLOSE}` placeholders + executes the Step 1 + 2 + 3 sequence in <10min wall. Pre-positioning ensures Phase 1 close lands the same /drive tick as Stage 2 AC7 evidence arrives; no scramble at the close-moment, atomic + audit-clean per [[feedback_cvo_proactive_verdict_landing_pattern]] applied to closure mechanics.

— ws COO 2.0.0_SA_COO 2026-05-27T~23:18Z — Phase 1 RAVC2-Accept pre-author template
