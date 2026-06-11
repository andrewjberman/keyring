# /ws-charter cycle 0006 — REPAIR-AMENDMENT (NFRA_GLOBGRPH §2b freshness contract)
**archetype:** SCRIBE
**secondary_archetypes:** VALIDATE, COORDINATE

## Classification
- **Class:** REPAIR-AMENDMENT (autonomous, CVO-finding-gated)
- **Trigger:** CVO MCP finding 20260611T231715Z + verdict `org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-11/kuzu_nessie_mechanics_verdict.md` (`be17d49eb`), Andrew-direct Kuzu/Nessie staleness investigation.
- **Trigger classes cited:** (a) mechanical-untruth-to-reality — PRD §3 declares Kuzu "rebuilt per commit"; as-built = three ONE-SHOT local DBs, three vintages, comp-kuzu DEFAULT the stalest (13/16/0 phantoms measured 23:10Z); (b) inadequate-solution-coverage — query surface shipped with no freshness contract; re-derives land in a tarball side-channel that never reaches Nessie.
- **HALT-gate:** PASS (rc=0). Hard-block audit log: OK. No hard-block class matched (PRD repair in `docs/architecture/` + project JSON — core CTO commit lane).

## Action taken
1. **PRD amendment** `docs/architecture/NFRA_GLOBGRPH_PRD.md` → v0.4:
   - NEW §2b — Query-surface freshness contract: rulings **F1** provenance header + `_build_manifest.json` per loader + age-warn (26h default) + UNKNOWN-VINTAGE loud path; **F2** canonical-surface collapse (one Nessie-rebuilt `kuzu_db`, comp-kuzu default points only there; scratch DBs `--db`-explicit); **F3** ad-hoc derive `--commit-to-nessie` opt-in (re-derive ⇒ Nessie version by construction); **F4** `kuzu_nessie_load.py` defaults `--force`.
   - NEW AC10 (a: header demonstrated on all 3 DBs; b: post-F2 canonical surface ≤ one-nightly-old).
   - §9 change-log v0.4 entry. TO candidates TO-F1/F2/F3 with compiler mandates staged for COO.
   - Item-2b delete-propagation half NOT re-scoped (CVO routed it to AE~B directly).
2. **Project JSON** `org/projects/NFRA_GLOBGRPH.json` phase narrative — v0.4 amendment recorded.
3. **CTO-verified before scribing:** `infra/aws/globgrph/kuzu_cli.py` DEFAULT_DB_PATH → local `kuzu_db` (confirms the default-surface claim).

## Interleaved (same tick, GLDINC lane — not charter-classified)
- DS RAVC2-CLOSE A_04 DELTA=0 disposition ACCEPTED (9a89926fd verified; in-commit proof battery = acceptance record). Doctrine refinement banked: verified-DELTA=0 (empirical battery + independent delta-logic check + explicitly-surfaced flex) satisfies never-widen by construction, no sign-off hold. GLDINC engineering 7/7 COMPLETE.

## Compiler Tools
No comp-* runs this tick: the amendment is a PRD/doc repair grounded in CVO's live-measured evidence table (23:10Z, three-DB phantom counts) + direct Read of kuzu_cli.py; no code/infra change made. TO-F1 mandate (in §2b) carries the comp-kuzu smoke + manifest-catalog updates for the implementing agent.

## Follow-on / next-cycle expected
- COO decomposes TO-F1 (no gate) → AE 0.7.0; TO-F2 gated on Item-2a stability; TO-F3 P2.
- CVO AC3 diff-oracle AM review (2026-06-12) unchanged — this amendment does not touch that gate.
