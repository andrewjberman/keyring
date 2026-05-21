# Task Order Compiler Gate Standard
**Owner:** 2.0.0_SA_COO + 1.0.0_SA_CTO
**Effective:** 2026-04-09
**Motivation:** ADVI_49PUSH wave (session 22 post-mortem) — four failures shipped as "complete" because agents used "code runs, build clean" as the acceptance bar. Compiler tools would have caught all four in <2s. This standard makes them mandatory, not optional.

---

## Rule 1: Final Check Before Marking Complete

Every task order that touches a **frontend component**, **gold script**, or **API endpoint** must run at least one compiler check as its final step before marking the TO complete.

The check output — the exact command run and whether it revealed issues — must be recorded in the session log.

**"No issues found" is a valid result. Skipping the check is not.**

---

## Rule 2: Required Check by Work Type

| Work type | Required check | What it verifies |
|-----------|---------------|------------------|
| Frontend component (new or modified) | `comp-transform fields <Component>` | All data fields rendered by the component exist in the TypeScript response type |
| Frontend component that reads gold data | `comp-platinum page <Component>` | Full stack confirmed: fetch → CF → S3 key → gold script that actually writes it |
| Gold script (D_00–D_04, C-chain, A-chain) | `comp-blast <script> --function <function>` | All downstream consumers (portal components, other scripts) are aware of any output changes |
| Gold script that adds/removes a JSON key | `comp-platinum reverse <s3_key>` | Every component that reads that key has been updated or is unaffected |
| API endpoint (new or modified) | `comp-routes trace <endpoint>` | Serving path is correct; auth layers match |
| Any work touching a file also in another active TO | Lateral MCP message to that TO's agent + `comp-blast` | Explicitly documented in the TO completion report |

---

## Rule 3: Cross-Domain Flagging in TOs and PRDs

When COO or CTO writes task orders for a parallelized wave, **any TO that touches a file, S3 key, or data contract shared with another TO must be explicitly flagged.**

### In the PRD/thread design phase (CTO responsibility):
- Run `comp-blast` on every affected component/script before decomposing into TOs.
- Any node with 2+ TOs in its blast radius gets a **CROSS-DOMAIN** flag in the PRD.
- The PRD must list which TOs share the resource and which agent owns the "last write."

### In the TO itself (COO responsibility):
Every TO that shares a resource with another must include a section:

```
## Cross-Domain Coordination
- Shared resource: DistributionTab.tsx (also touched by .034, .035)
- Owner of last write: DE~B (.035 lands after .029)
- Required: message DE~B before committing to DistributionTab.tsx
- Required: pull origin/DEV and rebase before pushing
```

### At execution time (agent responsibility):
Before committing to any file flagged as cross-domain:
1. Send an MCP message to the other agent: "About to commit to `DistributionTab.tsx` for .029 — confirm you are not mid-edit"
2. Pull latest origin before writing
3. Run `comp-blast` on the changed function to verify no new consumers were added by the other agent

If the other agent does not respond within 2 minutes, proceed but note the unacknowledged message in the session log.

---

## Rule 4: Gold Scripts Must Be Executed Before Marking Complete

No DS agent may mark a gold script TO complete without having executed the script at least to the step that produces the targeted output.

**Minimum verification:**
- Script runs to completion without error (no NameError, no missing column crash)
- At least one output file is spot-checked: the specific field the TO was supposed to produce has a non-zero / non-null value for at least one representative entity

**This is the lesson from:**
- `assignments_scd` NameError (D_02 never run — would have crashed on line 1)
- `fee_earning_aua` zeros (D_02 ran but fee fields not spot-checked — would have shown $0 immediately)

---

## Rule 5: Silent Failure Patterns Require Explicit Verification

Anytime code contains any of these patterns, the TO must include an explicit output check:

| Pattern | Required check |
|---------|---------------|
| `if col in df.columns:` (column guard) | Verify the column IS in the dataframe after loading |
| `data?.key ?? {}` (optional chaining with default) | Verify the key is present in the actual API response |
| `.get('key', default)` (dict get with default) | Verify `'key'` is actually in the dict, not just silently defaulting |
| `if not df.empty:` (empty guard) | Verify the dataframe is actually populated with expected rows |

These patterns were written for resilience. They are not acceptance criteria. A guard that's always firing means missing data — not graceful degradation.

---

## Rule 6: Compiler Tools Run in This Order

For any non-trivial TO (more than a 1-line fix):

1. **Before writing any code:** `comp-blast <target>` — understand what you're about to affect downstream
2. **Before committing:** `comp-transform fields <Component>` or `comp-platinum page <Component>` — verify the data contract is intact
3. **After committing:** `comp-blast <changed function>` — confirm no unintended blast radius expansion

The pre-write check is the most important. Agents that skip it are building blind.

---

## Failure Mode Reference (from ADVI_49PUSH session 22)

| Failure | What compiler check would have caught it | Time to catch |
|---------|------------------------------------------|---------------|
| `geo_drill` absent from `cumulative_chart.json` | `comp-platinum page DistributionTab` — shows `geo_drill` resolves to D_00 `geo_city` which requires `client_city` in adim | <2s |
| D_02 `assignments_scd` NameError | Execution gate (Rule 4) — NameError on first run | <10s |
| `fee_earning_aua` all zeros | Execution gate + spot-check (Rule 4) — $0 for all advisors is obvious | <30s |
| Portal drill logic broken by 3 agents | Cross-domain flag (Rule 3) — `.029`, `.034`, `.035` all flagged as sharing DistributionTab.tsx; coordinate before committing | Before first commit |

---

## Rule 7: Acceptance Criteria Flex Requires CTO Pre-Flag (Non-Negotiable)

**Effective:** 2026-04-15 (RF01 incident — COO unilaterally reinterpreted two `<expect>` clauses during acceptance without surfacing the call).

Any time a validator (COO, CTO, or peer agent) is about to accept a TO with ANY of the following deviations from the authored `<acceptance_criteria>` or `<compiler_tools_mandate>`, they MUST send a one-line MCP heads-up to the CTO BEFORE flipping `<status>complete</status>`:

- A `<run>` was skipped (and not re-run retroactively).
- The observed output does not match the `<expect>` clause exactly, but is being accepted on a reinterpretation.
- An acceptance criterion is being waived, downgraded ("document, not pass/fail"), or substituted with a different observation.
- A criterion is being deferred to a follow-up TO instead of resolved in place.

**Format of the heads-up MCP:**
```
Subject: ACCEPTANCE FLEX — {TO_ID} — {one-line summary}
Body: Original <expect>: "..."
      Substituted observation: "..."
      Reasoning: ...
      Proceeding to accept unless you redline within 5 min.
```

**Closeout requirement:** when the TO is finally marked complete, the completion comment MUST cite (a) what was reinterpreted, (b) why it was acceptable, (c) the original `<expect>` text and the substituted observation. One paragraph minimum. The audit corpus depends on visibility into where criteria flex.

**Why this rule exists:** Loose-prose acceptance is the failure mode that compiler-tool corpus discipline is designed to prevent. If validators silently bend `<expect>` clauses, the auto-appended log rows in `org/compiler-tools-log.md` become noise. Andrew called this out 2026-04-15 after the RF01 acceptance reinterpretation. "If the rule is that important make sure it is written in stone."

---

## Rule 8: RAVC1 Reviewer Protocol for Canonicalization-Class Refactors (Non-Negotiable)

**Trigger:** RAVC1 review of any commit touching a Lambda boundary, Lambda@Edge function, JWT issuer / claim path, DynamoDB partition key or GSI, Secrets Manager secret name with firm/tenant suffix, CloudFront behavior / origin selection rule, or any canonicalization / namespace literal change.

**Required pre-push reviewer steps (in addition to commit-message read + visual logic-walk):**

| Step | Tool/command | What it verifies |
|------|-------------|------------------|
| 1 | `comp-routes trace <endpoint>` for every modified endpoint | Full CF → auth → S3 path; flags 401 → HTML masquerade risk |
| 2 | `aws s3 ls opal-data-{firmId}/` for each affected firm | Verifies real bucket names match the canonical form portal would send |
| 3 | `aws dynamodb scan FIRM_TABLE --filter ...` | Verifies DDB partition keys match the canonical form portal would send |
| 4 | `git grep -rE "{literal-value}" portal/src/` PORTAL-WIDE | Cross-tree literal grep; catches cross-cutting consumers (Auth contexts, prefetchers, dev-mode env-readers) that subtree-only audits miss |
| 5 | Per-callsite annotation: which param-key / header / path-param, which downstream consumer, which canonical form expected | Surfaces wire-protocol divergence where same-boundary param-keys have different canonicals |

**Why this rule exists:** ADVI_SHARED.006 P0 cascade 2026-05-14. DT 0.4 pre-push approval on Commit C `46bfda8c` was based on commit-message read + visual logic-walk (concluded "zero behavior change at Lambda boundary"). The approval was empirically wrong on two grounds: (a) AuthContext.tsx:35 was a cross-tree consumer the subtree-only audit missed (Rule 8 step 4 would have caught it); (b) `?firm=` vs `?firmId=` wire-protocol divergence was not enumerated (Rule 8 steps 1-3 + 5 would have caught it). Net: ~33min wall-time P0 cascade with 2 forward-fix commits. Pre-push diligence on canonicalization-class refactors must be broader-than-commit-scope.

**Documented in:** post-mortem `docs/architecture/POSTMORTEM_SHARED006_CANONICALIZATION_20260514.md` §4.3.

DT/AE reviewers MAY mark RAVC1 ACCEPT only after running ALL 5 steps for canonicalization-class commits. Commit-message + visual logic-walk alone is structurally insufficient.

---

## Rule 9: Atomic-Bundle TOs Carry a Class-B Chain-Run Pre/Post Gate (Non-Negotiable)

**Effective:** 2026-05-21 (ADHC_VALGATE.007 -- Class-B gate formalization, N7).

An ATOMIC-BUNDLE TO is a multi-commit refactor that ships a producer and one or more of its consumers as one logical unit -- a helper signature change, a shared-shape change, a co-landed producer+consumer rename. This class ships clean past py_compile / ruff / tsc / human code-walk / runtime smoke AND past the chain-run A/B/C/D-stage shape sentinels, then leaks in production: a consumer the bundle did not update, a dropped sibling.

Every atomic-bundle TO MUST carry a Phase-N pre/post chain-run gate:

1. **Phase 1 (before the bundle ships):** `comp-chainrun snapshot --label pre --out {to_id}-pre.json` captures the A/B/C/D-stage shape-sentinel set -- the pre-refactor reference.
2. **Phase 3 (after the bundle ships and the chain re-runs):** `comp-chainrun snapshot --label post --out {to_id}-post.json` then `comp-chainrun diff {to_id}-pre.json {to_id}-post.json`.
3. A non-empty leak report -- any sentinel classed DROPPED (flipped green->absent), COLUMNS-LOST, or EMPTIED (row-count>0->0) -- is a partial-refactor leak. Resolve every leak before the TO is marked complete.

v1 is WARN-not-BLOCK: the diff does not fail the chain, and the WARN->BLOCK ratchet follows the same empirical-false-positive discipline as the Class-C suite (a one-line GATE_VERDICT_POLICY flip in chainrun_cli.py after ~1-2 weeks of FP data). An unaddressed leak is nonetheless a TO-acceptance blocker: COO does not accept an atomic-bundle TO whose post-diff carries an unresolved leak.

The pre/post snapshot+diff steps are filled into the TO's `<compiler_tools_mandate>` per the atomic-bundle SPECIAL CASE in the TO template (org/ref/TASK_ORDER_PROTOCOL.md).

**Why this rule exists:** DWSPLT chain #26 partial-refactor leak -- a consumer signature mismatch survived an atomic-bundle ship past every code-level check and every shape sentinel (forward-fix dd1206258, validated by chain #27). The pre/post sentinel-diff is the only gate whose reference -- the pre-refactor sentinel set -- can structurally catch it. Gate tool: comp-chainrun (ADHC_VALGATE.007). PRD: docs/architecture/ADHC_VALGATE.md section 4.B (N7).

---

## Enforcement

- COO reviews every TO completion report. If no compiler check is logged, the TO is not accepted as complete.
- CTO flags cross-domain resources during PRD decomposition. If a PRD has no `comp-blast` run before TO generation, the PRD is not accepted.
- Agents that repeatedly skip these checks will have their TOs decomposed into smaller, more constrained units in future waves.
- **Rule 7 (acceptance flex pre-flag):** missing pre-flag MCP = the TO acceptance is rejected and reverted to `<status>pending</status>` until the heads-up is filed and CTO has had the 5-minute redline window.
- **Rule 8 (RAVC1 canonicalization-class reviewer protocol):** RAVC1 ACCEPT issued on a canonicalization-class commit without the 5-step pre-push diligence = the ACCEPT is rejected and the commit reverted; reviewer re-runs the protocol before re-issuing ACCEPT.
- **Rule 9 (atomic-bundle Class-B gate):** an atomic-bundle TO marked complete with an unresolved leak in its post-diff = the acceptance is rejected and reverted to `<status>pending</status>` until every leak is resolved or explicitly waived with CTO sign-off.
