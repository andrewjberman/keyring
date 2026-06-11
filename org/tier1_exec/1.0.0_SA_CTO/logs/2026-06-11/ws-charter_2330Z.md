# /ws-charter cycle 0007 — Andrew-direct addendum (NFRA_GLOBGRPH §2b v0.4.1 multi-agent concurrency)
**archetype:** SCRIBE

## Classification
- **Class:** NOVEL-delta under Andrew direction (Andrew-direct scenario relayed via CVO 20260611T232824Z, same cycle) — folded into the standing §2b REPAIR-AMENDMENT as v0.4.1 before COO's AM TO-F2 decomposition.
- **Andrew scenario:** agent A asks, agent B executes a cloud change, A re-queries a now-stale graph; generalized to N concurrent agents.

## Action taken (committed with this log)
PRD §2b v0.4.1:
1. **F1 extended** — manifest pins the Nessie snapshot-id built-from; comp-kuzu compares pin vs newest warehouse metadata.json at query time → auto-refresh (post-F2) or `BEHIND Nessie HEAD by N commits` (commit-distance staleness, not just age-hours).
2. **F2 extended** — rebuild trigger = HEAD-advance (not cron); concurrent-rebuild safety = workspace mkdir-mutex + build-to-tempdir-and-atomic-rename swap (the kuzu_nessie_load half-wipe MERGE corruption class becomes routine with N agents otherwise). Multi-WRITER side noted safe by construction: agents never write the graph; CloudTrail→2b→Nessie event-sources every change regardless of author; Nessie serializes.
3. **NEW F5 doctrine** — read-your-own-writes verification goes to served-artifact/live-AWS (existing standing rule), never the graph; the graph is the traversal surface where minutes-stale-and-labeled is acceptable. CVO caveat carried: 2b delete-propagation (AE~B P1) is the hard dependency for trusting auto-refresh.
4. **AC10 extended** — (a) +commit-distance reporting; (b) +auto-refresh on HEAD-advance; NEW (c) concurrent-rebuild safety demo. TO-F2 candidate text updated to carry the requirements + AC10(b)+(c).

## Compiler Tools
No comp-* runs: doc-only amendment; the concurrency mechanics cited (S3 metadata.json list, mkdir-mutex, atomic rename) are existing workspace patterns, line-anchored by CVO's verdict. Implementation mandates ride TO-F1/TO-F2.

## Follow-on
COO AM decomposition now picks up TO-F2 WITH the concurrency requirements (no re-issue needed); CVO AC10 verification leg unchanged plus (c).
