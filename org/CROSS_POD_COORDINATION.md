# Cross-Pod Coordination Protocol

When a feature or task spans multiple pods, special coordination is required. This document defines how cross-pod work is initiated, tracked, and completed.

---

## When Cross-Pod Coordination Is Needed

- A feature touches pages owned by different pods (e.g., PortfolioManagement export -> TradeSubmission approval)
- A shared component change affects multiple pods
- An API contract change impacts consumers across pods
- An infrastructure change (Lambda, EventBridge) affects data flowing to multiple pages

---

## Initiation

Cross-pod work is initiated by one of:

1. **CTO (1.0.0_SA_CTO)** — writes an architecture spec in `docs/architecture/` that references multiple pods, then issues task orders to each affected DE
2. **Andrew Berman** — issues ad-hoc task orders to affected DEs directly
3. **A DE** discovers cross-pod impact during their work — escalates to CTO for coordination

A DE should **never** unilaterally modify another pod's pages or issue task orders to another pod's agents. Cross-pod scope requires CTO or Andrew involvement.

---

## Tracking

### Spec Document

Every cross-pod feature must have a single spec document:
```
docs/architecture/{feature_name}.md
```

This spec must contain:
- Which pods are affected
- What each pod is responsible for
- Interface contracts (API shapes, data formats, event schemas)
- Dependency order (which pod must complete first)

### Task Orders

The CTO (or Andrew) issues **separate task orders** to each affected pod's DE, referencing the shared spec:

```xml
<task_order>
  <metadata>
    <id>1.0.0_SA_CTO-2026-03-02-export-bridge-pod3</id>
    <issued_by>1.0.0_SA_CTO</issued_by>
    <issued_to>0.3.0_DE_TradingOperations</issued_to>
    ...
  </metadata>
  <dependencies>
    <dependency agent="0.4.0_DE_ClientPlatform" task="1.0.0_SA_CTO-2026-03-02-export-bridge-pod4" status="pending"/>
  </dependencies>
  ...
</task_order>
```

The `<dependencies>` block links cross-pod task orders so each DE knows what they're waiting on.

---

## Communication

Cross-pod agents communicate through:

1. **The shared spec** — single source of truth for the feature
2. **Task order dependencies** — explicit XML links between pod task orders
3. **DE session logs** — each DE documents their pod's progress; CTO/COO read these for cross-cutting status
4. **CTO/COO** — serve as the coordination layer, reading DE logs and resolving conflicts
5. **Daily Collaborative Log** — shared operational awareness (see below)

There is no direct communication channel between leaf agents in different pods. All cross-pod coordination flows through the DE -> CTO/COO -> DE path.

---

## Daily Collaborative Log

A shared, timestamped log that all Tier 1 and Tier 2 agents can read and write to. This provides real-time operational awareness across pods — who is working on what, what areas are being touched, and where overlapping work exists.

### Location

```
org/daily_log/YYYY-MM-DD.md
```

### Format

```xml
<daily_log date="YYYY-MM-DD">

  <entry>
    <timestamp>HH:MM</timestamp>
    <agent>0.1.0_DT_MarketIntelligence</agent>
    <action>pushing</action>
    <scope>portal/src/pages/MarketPerformance/, portal/src/components/RegimeTooltip.tsx</scope>
    <notes>Pushing 3 commits from 0.1.1_RD and 1 from 0.1.0_DE. Will invalidate CloudFront after.</notes>
  </entry>

  <entry>
    <timestamp>HH:MM</timestamp>
    <agent>0.3.0_DT_TradingOperations</agent>
    <action>deploying</action>
    <scope>infra/aws/lambda/bd-pipeline/bd-portal-publisher</scope>
    <notes>Terraform apply for updated publisher. Expect bd-v2.14.0 tag after 0-diff.</notes>
  </entry>

</daily_log>
```

### Rules

- **All Tier 1 and Tier 2 agents** should check today's daily log on startup
- **Before pushing or deploying**, a DT/AE agent should add an entry stating what they're about to touch
- **Before committing to shared portal paths** (components, types, hooks, API endpoints), a DE should check the daily log for overlapping work
- Entries are append-only — never edit or delete previous entries
- The log is for awareness, not approval — agents don't need to wait for acknowledgment
- **Action types:** `pushing`, `deploying`, `committing-shared`, `blocking` (flagging an issue others should know about)
- If the day's log file doesn't exist yet, create it with the XML wrapper

---

## Completion

A cross-pod feature is complete when:
1. All pod-specific task orders are marked `status="complete"`
2. Each DE has documented completion in their session logs
3. The DT agents have pushed and deployed all affected code
4. The CTO or COO has verified the end-to-end feature works across pods

---

## Example: Portfolio Export -> Trade Submission Bridge

- **Spec:** `docs/architecture/PORTFOLIO_EXPORT_TRADE_SUBMISSION_BRIDGE.md`
- **Pods affected:** TradingOperations (PortfolioManagement + TradeSubmission)
- **Shared services:** AE agents for Lambda deployment
- **In this case:** Single pod owns both pages, so standard intra-pod coordination applies. If it had spanned pods, CTO would issue linked task orders to each DE.
