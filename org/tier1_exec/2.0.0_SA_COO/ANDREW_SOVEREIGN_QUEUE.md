# Andrew Sovereign Queue (COO-maintained) -- items awaiting Andrew's decision, routed on re-engage

**Purpose:** a durable home for every item that requires an Andrew sovereign call, so none falls off
the COO's radar the way NFRA_GCONTR.TO-3 fell off the fabric's (dormant ~3wk behind a stale registry
entry). Updated each /drive cycle that touches a sovereign item; routed as a consolidated batch when
Andrew re-engages. **This tracks; it does not decide -- the calls are Andrew-only.**

Last updated: 2026-07-09T14:19Z (COO)

| # | Item | Nature | State / what's pre-staged | Route trigger |
|---|---|---|---|---|
| 1 | **NFRA_GCONTR SEV1 row sign-off -- 2 ROWS (corrected)** | §9 TIERED: SEV1 = Andrew-only | **CORRECTED 2026-07-09 (AE in-VPC read):** benchmark is ALREADY Andrew-signed + live+ratified (06-16) -- NOT pending. Only **2** SEV1 rows need sign-off: **headline + advisor_intelligence/NNA** (authored 06-16/17, UNSIGNED, the only unloaded rows). GCONTR is 3/5 live; SEV2 (peers/aum) done+ratified. | Route the CONSOLIDATED 2-row sign-off (headline + advisor_intelligence) when Andrew re-engages. Both authored HELD-ready. On sign -> AE loads on the hardened image -> 5/5. COO owns routing. |
| 2 | **Phase A canary path-decision** | operational-vs-sovereign path | I proposed operational (temp bcrypt password on existing non-firm demo@demo.test); MSTR escalated sovereign. Per my stated fallback = sovereign-HELD (Andrew's call). Non-urgent (Phase A also held-external on reader next-runs). | Andrew/MSTR confirms operational -> 0.5.0 runs 2-step verify -> Phase A closes -> revoke. Else stays sovereign-HELD. |
| 3 | **GitHub read-only PAT** (secret github-token-6FYoJ6) -- **COUPLED, read the note** | credential provision | Blocks freshguard-leg5-v2 parity-drift verify (0.7.0~B). HELD-SOVEREIGN-GATED. **COUPLING (0.5.0 143312Z):** this ONE secret has exactly ONE reader in 180 roles + value NEVER rotated since 2025-12-23 (6mo). TWO open items depend on it: (a) freshguard-leg5 needs Andrew's read-only PAT; (b) the daily-agenda SEV2 fix would repoint news-ingestion-lambda-role's grant to this SAME secret. Fix-in-isolation breaks the other. | Andrew provisions the read-only PAT for freshguard (repo-contents/commit-listing scope on Opal-Capital/ajb_workspace+portal if it's to serve both). **Do NOT let daily-agenda silently repoint to this shared token as a side-effect** -- sequence: provision -> scope-confirm -> THEN decide daily-agenda's grant. Default TWO purpose-scoped secrets over one union-scoped shared PAT (shared = each reader inherits the other's capability = over-grant). |
| 4 | **MS identity / M365 credential-gate** | credential provision | (carried from prior queue) | Andrew provisions. |
| 5 | **cottonwood credentials orphan -- delete recommendation** | destructive (delete = human-only) | CARVED-OUT pending Andrew; delete is Andrew-only per autonomy rules (never agent-unilateral secret/S3 delete). | Andrew rules delete-vs-retain. |
| 6 | **cot DATEMODE** | pipeline policy | HELD by Andrew (carried). | Andrew rules. |
| 7 | **Rule-14 wording** | governance | (carried; MSTR/Andrew) | Andrew/MSTR. |
| 8 | **NFRA_COMPTEAM B2-ACTIVATE -- teammate-onboarding policy** | policy decision | B2 access-control activation gated on Andrew's teammate-onboarding policy decision (found in the 2026-07-09 registry sweep; NFRA project). A1 verification + B2 build proceed around it. | Andrew rules the onboarding policy -> B2 activates. |
| 9 | **Data-plane firm-sep gap (SEV1-class, incident-gravity) -- RELAY on sweep-close. SCOPE GREW.** | relay (not a decision) | NEVER#1 miss. B2-partial APPLIED+closed 4/4 (market-update DELETE bd/gold + SEV1-overwrite GONE, verified). Sweep GREW it: **2nd principal lambda-execution-role (13 LIVE Lambdas, cross-firm WRITE to bd incl SEV1 platinum, legacy-remnant, highest-pri belt)** + **possible UNMANAGED grant** (detection-gap: firm-sep DETECT needs live-vs-TF reconcile, not TF-lint). Sweep 3/6, clean re-run pending. Tracker: INCIDENT_dataplane_firmsep_bucket_deny_gap.md. DISTINCT from credential-close (STANDS). | Relay ON SWEEP-CLOSE + belt-landed: "data-plane firm-sep gap found + closed" covering 2 principals + the detection-gap (honest, scoped, remediation-plan). NOT premature -- prove the universe (clean re-run) first. |

**Discipline:** route these as a batch when Andrew re-engages (he was just PushNotified the credential
milestone -- may re-engage soon). Do NOT force-push a sovereign call mid-cycle; pre-stage and route on
re-engage. Each item that resolves gets struck here with the resolution + date.
