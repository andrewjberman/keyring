# ws-charter cycle:0027 — 2026-06-02 2127Z

**CLASS:** REPAIR-AMENDMENT (Andrew sovereign ruling → INFPRM scope refinement)

## Inbox classification
- **ANDREW_DIRECTION (via COO 211530Z + 211957Z):** "no usertype tiering on Distribution; nothing on it has PII non-admins are blocked from seeing" + "any usertype tiering on distribution tab is misguided and not desired." **Supersedes CTO ruling-(a)** (cross-advisor drill 403 by-design). Non-admins must drill ANY advisor in Distribution.
- **DRIVE_ESCALATION (COO):** Joe LOGIN-LOOP (live P0) — routed me the security-model scope; AE on the loop fix.
- **CVO_CC:** 23982a8c additive-confirm (banked — gate reopened, so superseded as the sole gate).
- **AE consult (crossed):** independently landed option (i) = my data-layer split. Converged.

## Action
1. **Code-traced the seam to ground truth** (not abstract): DistributionTab:1977 drill consumes ONLY `book.relationship_stacked_periods` (aggregate); `book.json` co-mingles aggregate + `clients[].display_name` PII roster; `tier_policy.mjs` is FIRM-GENERIC (49F/BD = real names) → wholesale `book.json`→L0 relax leaks 49F real roster cross-advisor. **UNACCEPTABLE.**
2. **Ruled the security model (W5):** gate by payload-sensitivity, not user-type-on-a-tab. Resolution = **DATA-LAYER SPLIT** — roster-free aggregate → L0/non-.004a allowlist (comp-pii-proven); `book.json` stays L1+.004a (own-advisor); `clients/` stays L2; firm-containment invariant. FE repoints drill to the aggregate artifact.
3. **Answered AE's Q2 (session-hold):** valid firmId-JWT holds session + L0 access **regardless of advisorId**; .004a/.004c apply ONLY to PII resource paths. Kills the bootstrap-loop class structurally.
4. **Scribed W5 to INFPRM** (doc-of-record) + Status→ACTIVE. Routed full edge scope + rigor gates to AE (CTO approves diff pre-safe-apply); ship-path fork to Andrew via COO.

## Commits
- `3bce72da1` repair(ADVI_INFPRM): W5 Distribution-untier security-model ruling (pushed CLOUD).

## Login-loop
RESOLVED by AE `486556175` — JWT claims mint from `opal-partner-{firmId}` not `opal-users-v2`; Joe partner-table entry created → session holds. Corrects W4 ROOT-1 premise.

## Follow-on dependencies
- **AE:** check existing aggregate artifact (timeseries/drilldown_summary) carries `relationship_stacked_periods` → if yes, split collapses to {edge allowlist + FE repoint, no DS emit}. Then edge diff → CTO approval → safe-apply.
- **DS:** emit roster-free aggregate artifact IF none exists.
- **RD~C:** repoint Distribution drill to the aggregate artifact.
- **CVO:** re-verify the NEW access model (cross-advisor aggregate readable, roster still gated, no cross-FIRM leak).
- **Andrew:** ship-path fork A (ship 23982a8c now + W5 fast-follow [CTO lean]) vs B (hold until W5 lands).

## Next-cycle expected state
Promote HELD pending Andrew ship-path pick + AE existing-artifact report. On A: fire 23982a8c GO; W5 becomes fast-follow. On B: hold until W5 edge+data+FE land + CVO re-verify + Andrew re-smoke.
