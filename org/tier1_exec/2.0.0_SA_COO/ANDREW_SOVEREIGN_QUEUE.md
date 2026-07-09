# Andrew Sovereign Queue (COO-maintained) -- items awaiting Andrew's decision, routed on re-engage

**Purpose:** a durable home for every item that requires an Andrew sovereign call, so none falls off
the COO's radar the way NFRA_GCONTR.TO-3 fell off the fabric's (dormant ~3wk behind a stale registry
entry). Updated each /drive cycle that touches a sovereign item; routed as a consolidated batch when
Andrew re-engages. **This tracks; it does not decide -- the calls are Andrew-only.**

Last updated: 2026-07-09T14:19Z (COO)

| # | Item | Nature | State / what's pre-staged | Route trigger |
|---|---|---|---|---|
| 1 | **NFRA_GCONTR SEV1 row sign-off** | §9 TIERED: SEV1 = Andrew-only | 3 SEV1 rows (model_portfolios.benchmark, headline, advisor_intelligence/NNA) authored HELD-not-written-as-ratified by CVO. Benchmark row done; headline + advisor_intelligence next. | Route CONSOLIDATED 3-row sign-off when Andrew re-engages AND all 3 authored. CVO owns authoring; COO owns routing. SEV2 (peers/aum) proceed in parallel CTO+COO-ratified (NOT here). |
| 2 | **Phase A canary path-decision** | operational-vs-sovereign path | I proposed operational (temp bcrypt password on existing non-firm demo@demo.test); MSTR escalated sovereign. Per my stated fallback = sovereign-HELD (Andrew's call). Non-urgent (Phase A also held-external on reader next-runs). | Andrew/MSTR confirms operational -> 0.5.0 runs 2-step verify -> Phase A closes -> revoke. Else stays sovereign-HELD. |
| 3 | **GitHub read-only PAT** (secret github-token-6FYoJ6) -- **COUPLED, read the note** | credential provision | Blocks freshguard-leg5-v2 parity-drift verify (0.7.0~B). HELD-SOVEREIGN-GATED. **COUPLING (0.5.0 143312Z):** this ONE secret has exactly ONE reader in 180 roles + value NEVER rotated since 2025-12-23 (6mo). TWO open items depend on it: (a) freshguard-leg5 needs Andrew's read-only PAT; (b) the daily-agenda SEV2 fix would repoint news-ingestion-lambda-role's grant to this SAME secret. Fix-in-isolation breaks the other. | Andrew provisions the read-only PAT for freshguard (repo-contents/commit-listing scope on Opal-Capital/ajb_workspace+portal if it's to serve both). **Do NOT let daily-agenda silently repoint to this shared token as a side-effect** -- sequence: provision -> scope-confirm -> THEN decide daily-agenda's grant. Default TWO purpose-scoped secrets over one union-scoped shared PAT (shared = each reader inherits the other's capability = over-grant). |
| 4 | **MS identity / M365 credential-gate** | credential provision | (carried from prior queue) | Andrew provisions. |
| 5 | **cottonwood credentials orphan -- delete recommendation** | destructive (delete = human-only) | CARVED-OUT pending Andrew; delete is Andrew-only per autonomy rules (never agent-unilateral secret/S3 delete). | Andrew rules delete-vs-retain. |
| 6 | **cot DATEMODE** | pipeline policy | HELD by Andrew (carried). | Andrew rules. |
| 7 | **Rule-14 wording** | governance | (carried; MSTR/Andrew) | Andrew/MSTR. |
| 8 | **NFRA_COMPTEAM B2-ACTIVATE -- teammate-onboarding policy** | policy decision | B2 access-control activation gated on Andrew's teammate-onboarding policy decision (found in the 2026-07-09 registry sweep; NFRA project). A1 verification + B2 build proceed around it. | Andrew rules the onboarding policy -> B2 activates. |

**Discipline:** route these as a batch when Andrew re-engages (he was just PushNotified the credential
milestone -- may re-engage soon). Do NOT force-push a sovereign call mid-cycle; pre-stage and route on
re-engage. Each item that resolves gets struck here with the resolution + date.
