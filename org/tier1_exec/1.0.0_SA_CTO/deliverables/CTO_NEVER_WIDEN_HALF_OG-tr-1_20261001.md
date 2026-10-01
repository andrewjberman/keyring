# CTO never-widen half: NFRA_OPLGTW OG-tr-1, the Tax SMA workbook route release, capability ON -- 1.0.0_SA_CTO~O, 2026-10-01 ~18:3xZ

**Ask:** `2.0.0_SA_COO~O` msg 28020,
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-tr-1_20261001.md` @930ab6d745. The second
half is `3.0.0_SA_CVO~O`'s.
**Authority:**
- Andrew-direct ~17:2xZ: site Z runs both halves; the TAXSMA exclusion is lifted for THIS release (relay @d34037d1f5).
- ~17:3xZ: "ON at this deploy".
- ~17:4xZ: priority ahead of site-Z work.
This seat's 27978 conditions are carried into the order. **Context:** `/self-drive OPALAI_MCP_SITEZ`.

## Independent reads at signing (this seat)

| claim | read here | result |
|---|---|---|
| live 0a1d9079c6 | S3 `opal-gateway-latest` `git-ref` | `0a1d9079c682c640e619612f804257681c5db357`: MATCH |
| release = 2 commits on live | `merge-base --is-ancestor`; `rev-list --count` | ancestor; 2: MATCH |
| 5 files, gateway only | `git diff --name-only 0a1d9079c6 3a7d6a7dc8` | `app/config.py`, `app/server.py`, `app/taxsma_workbook.py`, `deploy-to-ec2.sh`, `tests/test_taxsma_workbook.py`: MATCH; 0 outside the gateway |
| other routes and tools untouched | `git diff --quiet` on `ms_ingest.py`, `tools.py`, `mail_route.py`, `transcript_route.py` | all unchanged (whole-file census) |
| no OA-e-10 payload (my 27978 condition 2) | `git grep -c _login_allowed_identities 3a7d6a7dc8 -- .../app` | 0 files: EXCLUDED |
| module = the laptop spec | `sha256` of `app/taxsma_workbook.py` at 3a7d6a7dc8 | `6acc3e8ce8952cdddea67f260814af4abe6bc055f8f9a4c8300b23f3e2a6ee70` = the spec (TX-r-2 request): MATCH |
| `server.py` adds only the Tax lines | `git diff ... app/server.py` | the import, plus one `Route` registered ahead of the generic `/ms/*` routes with its OWN guard (never `_ms_guard`): MATCH |
| the edge half is live and exact | `elbv2 describe-rules` (tick 16) | rule 36 = exactly `/ms/taxsma-workbook`. A public no-bearer probe returned 404 before this release (route unmounted) |

## The half -- SIGNED

I, `1.0.0_SA_CTO~O`, sign the blast radius in section 2 of the ask on:
- release `3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7` on live `0a1d9079c682c640e619612f804257681c5db357`;
- rollback `/c/tmp/og-rb6`;
- `.env` 46 -> 48 (the other 46 unchanged);
- tools 65 unchanged;
- no Terraform, IAM or secret write in this act.
It covers both branches of every leg.

- **The served-content widening is named and accepted on Andrew's word:** `GET /ms/taxsma-workbook` LIVE with the
  capability ON, gated at the edge only by the route's own constant-time bearer. It reads one fixed worksheet as the
  bound identity and returns nine projected columns.
- **The identity is the confirmed opalbloomberg@ oid.** Two broker records match one oid; the stop condition was two
  DIFFERENT people matching, and it did not fire.

**VOID on:**
- the live ref other than 0a1d9079c6 without a re-cut;
- `tr.AC1` arm 2 (no bearer) returning anything but `UNAUTHORIZED_CAPABILITY` with no Graph call;
- the bearer rendered empty;
- the identity not the confirmed oid;
- any of the other 46 `.env` keys changed;
- any change to `/ms/*` generic, `/hx/*`, `/otp/*` or `/mcp` behavior;
- shell-sourcing the host `.env` (Z-S32).

**Carried, not blocking:** the C7 wording that keeps `/ms/*` structure-only goes to OPLGTW's next analysis. This route
holds its own bearer and guard, and is registered ahead of the generic `/ms` guard.
