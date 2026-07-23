# CVO~Z session log — NFRA_PSTMRT s.7 item 1 registry-parity verify

**archetype:** VALIDATE
**Serial:** `3.0.0_SA_CVO~Z` (fresh session, PID 34180) · **Window:** 2026-07-23 0047–0056Z

## Startup

- Launcher carried an identity contradiction: header `~Z`, body = the base-CVO 1b-F row. Resolved by
  MEASUREMENT, not inference: base `3.0.0_SA_CVO` LIVE at PID 24744 (peer session); `~Z` NOT REGISTERED
  with 3 unread inbox messages addressed to the ~Z seat. Registered `~Z`, serial file written (LD-0290),
  audit-archive-invoker rc=0/0 findings, watcher Monitor armed (task `bnmud6mxh`). Base peer's watcher
  (PIDs 1149265/1149316, base serial) left untouched.
- LD-0319 load control: `comp-system --check` = **SYSTEM CURRENT** (0 drifted regions) — AT PARITY, proceed.
- NFRA_SYSPARITY read ACTIVE/ONGOING → scoped 30-min loop RE-ARMED per XXX.md 1b-F ~Z row: cron
  `952ef5bb` (13,43 * * * *), body = per-domain /molecule + /verify rotation, verdicts to MSTR only.

## Work: NFRA_PSTMRT PRD s.7 item 1 (Andrew-nudged via CTO~Z)

ACK'd all 3 inbox messages same turn. Verified `data/firm_registry.json` @ HEAD `3449c8733` against all
three `_meta.grounding` sources. **Verdict: DOES NOT FULLY TIE** — F1 cottonwood display_name vs
firm-config.mjs:53 ("Cottonwood Capital Advisors" landed @3e0f224e2 06-09; CTO~Z's no-entry premise
false at source); F2 `demo` firm (firm-config.mjs:42, ADVI_DEMOV1) unregistered — the seed
under-enumerates vs its own cited source, the postmortem's own class; F3 email_domain uncited (content
ties to comp-constants FIRM_EMAIL_DOMAINS canonical). All else PASS with printed denominators
(FIRM_CONFIG 11/12; variance catalog 9/9 + alias-normalization convention note; PUBLISH_MAP mdpf
segments exact, global pseudo + mockadv absent honored). Deliverable
`deliverables/NFRA_PSTMRT_S7I1_REGISTRY_PARITY_VERIFY_20260723.md` @`1b650071d`; verdict MCP'd to
CTO~Z 005511Z. Items 2–4 untouched (build-gated per charter).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-system | `--check` (LD-0319 load control) | SYSTEM CURRENT, 0 drifted |
| comp-glob | firm-config.mjs / variance_dimensions.yaml | located sources on-rails |
| comp-grep | PUBLISH_MAP; cottonwood.com; 49financial.com; inflectionwealthmgmt | grounded email_domain to comp-constants.config.yaml:620 canonical |
| rail-checked greps | single-file PUBLISH_MAP extract; PRD section extract | inline markers cited |

No gaps found in tool coverage for this task.

## Open on ~Z

1. NFRA_PSTMRT s.7 items 2–4: build-gated (0.8.0 gate builds + P2 YAML) — verify on land.
2. NFRA_SYSPARITY 30-min loop live (cron 952ef5bb) while project active.
3. Content-eval answer key (716 pairs): queued at Andrew's word for the Andrew+~Z joint review.
