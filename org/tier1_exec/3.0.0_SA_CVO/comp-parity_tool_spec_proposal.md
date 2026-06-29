# Tool Spec Proposal — `comp-lambdamap parity` (a.k.a. comp-derivedrift): the read-only 3-leg deploy-parity classifier

**archetype:** IMPLEMENT (spec)
**Author:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 1.0.0_SA_CTO (arch-gate: tool-vs-subcommand + naming) + 0.7.0_AE_CloudOps~B (build, owns comp-lambdamap) · cc 2.0.0_SA_COO
**Origin:** Andrew-direct 2026-06-29 ("there should be a comp-derivedrift purpose-built comp tool for this kind of thing"). CVO proposes the spec; CTO arch-gates; AE builds. CVO does not build the comp-tool.

## Why (the gap)
`comp-lambdamap sha` is a **2-leg** read (source-map record ↔ live CodeSha256): it detects drift but not its **CAUSE** — and the cause is the whole decision (the molecule `657a9ff76` established the 7-suspect estate as "all code-OK, 0 half-landed" only by adding the **3rd leg**, the actual S3 deploy artifact, by hand). `classify_reconcile` (`979c1b8a7`) already added that 3rd leg — but it lives **inside `derive`'s `--write` decision path**. This spec promotes it to a **read-only standing capability**: "is my deployed estate in true parity, and if not, WHY" — queryable any time, on the rail, without invoking the reconcile/write path.

## What — the 3-leg classification
Per Lambda, read the three shas and classify:
- **record** = source-map `functions{}.artifact_sha256`
- **live** = AWS `get-function-configuration.CodeSha256`
- **s3** = the deploy artifact's `Metadata.content-sha256` (builders stamp it at upload; verified == CodeSha256, e.g. bd-portal-publisher `VEMK3JYTCF/Py5XN..` on all three legs — molecule + gate re-verify)

| Verdict | record vs live | live vs s3 | meaning / route |
|---|---|---|---|
| **MATCH** | == | (== implied) | clean — no action |
| **STALE-RECORD** | ≠ | **==** | live IS the correct deployable; record stale → safe `derive --write` |
| **POSSIBLE-HALF-LANDED** | ≠ | **≠** | live running a different artifact → **deploy problem; investigate, do NOT reconcile** |
| **CORRUPT-RECORD** | record non-base64 | — | source-map write bug (MSYS-mangle class) → builder fix + re-record |
| **DISPOSITIONED** | ≠ | (by `_note`) | intentional-leave (`intentional-leave\|ignore_changes\|not-to-apply`) → leave |
| **UNVERIFIABLE** | ≠ | s3 unreadable | content-sha256 metadata absent → HOLD, report honestly (never silently MATCH) |
| **NOT-LIVE** | recorded, absent live | — | orphan record (function gone / wrong region) |

This table IS: (a) the parity answer, (b) the `derive --write` gate decision (STALE-RECORD safe vs the rest HELD — already enforced per gate verdict `ed13b714a`), (c) the half-landed-deploy detector the NEVER-half-landed rule wants.

## Shape (recommendation — CTO arch-gates the call)
**Promote `classify_reconcile` into a read-only `comp-lambdamap parity` subcommand**, reusing the existing live-read + source-map-read + S3-head machinery — NOT a from-scratch separate `comp-derivedrift` binary (which would duplicate the boto/parse layer). If a distinct discoverable name is wanted, register `comp-derivedrift` in comp-which routing → `comp-lambdamap parity` (alias, not a second implementation). Two surfaces on one engine: `parity` = READ (classify, no mutation), `derive --write` = WRITE (acts on the same classification, STALE-RECORD only).

## Cost guard (mandatory)
Two-leg first (record vs live — the existing `sha` pass, zero S3 reads); **S3-head ONLY the non-MATCH subset** (the drift candidates, usually a handful). Never head-object all ~135 per run. `head-object` (no download) reads `Metadata.content-sha256` — cheap.

## Output
- Per-Lambda verdict line + a summary count (`MATCH: n | STALE-RECORD: n | HALF-LANDED: n | CORRUPT: n | DISPOSITIONED: n | UNVERIFIABLE: n | NOT-LIVE: n`).
- `--json` mode for piping (CI / downstream).
- Exit code: **0** when nothing actionable (all MATCH/STALE-RECORD/DISPOSITIONED); **1** when any HALF-LANDED / CORRUPT / NOT-LIVE / UNVERIFIABLE (the actionable classes) — so it's a usable CI gate ("is the estate truly in parity").

## Coverage caveat (honest-limit, from the gate re-verify)
STALE-RECORD vs HALF-LANDED discrimination depends on the `content-sha256` metadata being present. Artifacts uploaded by a path that didn't stamp it (legacy `deploy.sh` / console) → **UNVERIFIABLE**, reported explicitly, never silently folded into MATCH. Coverage = the fraction of the estate carrying the metadata; worth a one-line surface in the summary so the operator knows how much the parity verdict actually covers.

## Rail + lane
- comp-which-discoverable; register in `org/modules/graph/graph-call-manifest.yaml` tools_index + an entry routing "is my deployed estate in parity / why did a lambda drift". NFRA_COMPRAIL on-rail.
- Lane: comp-tool → **CTO arch-gate** (tool-vs-subcommand + naming + the exit-code/CI-gate semantics) + **0.7.0_AE build** (owns comp-lambdamap + the classify_reconcile engine). CVO verifies the build (the molecule defined its behavior empirically; I co-verify the read surface against live like the `sha` increment).

## Asks
- **CTO:** rule subcommand-vs-alias + name (`comp-lambdamap parity` recommended; `comp-derivedrift` as a comp-which alias if a distinct surface is wanted) + the exit-code/CI-gate contract; arch-gate.
- **AE:** build the read-only surface on the existing `classify_reconcile` + the cost-guarded 2-leg-then-S3 flow + the coverage-line; comp-which registration.
- Non-urgent (the classifier engine already exists + is gate-verified); this is the read-surface + discoverability layer.

— 3.0.0_SA_CVO
