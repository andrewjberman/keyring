# KIMI_ESTATE_FANOUT_20260812 — verbatim subagent evidence for the C4/C3.ii/Kimi CTO brief

**Commissioned:** Andrew-direct 2026-08-12 (R5, record @8447ad7293). **Collector:** `4.0.0_SA_CRO`.
**Persistence rule (Andrew-direct, mid-fanout, verbatim):** *"Make sure all this information we're
getting from each subagent is properly persisted somewhere, because if we just do one big summary it
will be lossy and probably miss data we'd like to utilize for any of these subproject needs."*
So: **each agent's full report lands here verbatim** — the CTO brief is a MAP over these files, not a
replacement for them. Formatting normalized only where the harness HTML-escaped entities; content
untouched.

**Evidence class:** agent-derived LEADS. Ground-check status per the pre-registered table
(`../../drafts/BRIEF_GROUNDCHECK_PREREGISTRATION_20260812.md`) is tracked in the brief itself.
Claims verified at this seat before use are marked in the brief, not by editing these files.

| # | file | agent scope | received | status |
|---|---|---|---|---|
| 01 | `01_MS_SHAREPOINT_ESTATE.md` | MS/SharePoint estate + producer (content-vs-metadata crux) | ~20:15Z | COMPLETE |
| 02 | `02_COVERAGE_CENSUS.md` | Deterministic coverage standing + cascade-budget arithmetic | ~20:20Z | COMPLETE |
| 03 | `03_COMPTOOLS_IMPACT.md` | comp-tools impact census (breaks / unaffected / new capability) | ~20:35Z | COMPLETE |
| 04 | `04_C4_DECOMMISSION_SURFACE.md` | C4 decommission surface (definers, consumers, literals, gates) | ~20:40Z | COMPLETE |
| 05 | `05_KIMI_PIPELINE_STATE.md` | OPAL_KIMIPIPELINE ground truth (deploy/schedule/IO/egress/drift) | ~20:50Z | COMPLETE |
| 06 | `06_POTION_NLP_CAPABILITY.md` | Potion/NLP deployed-vs-built-vs-designed | pending | RUNNING |
| 07 | `07_C3_NAMING_AND_BRIDGE.md` | C2/C3.i naming mechanics + the C3.i↔C3.ii bridge | pending | RUNNING |

## Cross-report headline findings (index only — details in the files)

- **01:** MS producer is metadata-only, TRIPLE-enforced (source allowlist / gateway strip / emit cert).
  **47.2% of MS docs (PDF/docx/pptx) have NO text-retrieval mechanism in the estate.** 12.1% of
  MS_FILE nodes are .git/cache contamination. Zero existing document classification. No Graph 429
  handling anywhere.
- **02:** THREE disjoint C2/C3 populations sharing ZERO vocabulary (canonical 12 families / live 19+4
  semctl nodes / harness 6,138+1,255 JSONs never landed). Estate deterministic-coverage CEILING is
  **39.7%** vs the ratified >=90% budget at node grain; instance grain reads 82%; **the budget does
  not say which grain it binds.** MS coverage = 0 of 5,886, declared.
- **03:** comp-estate is the ONLY C4-aware tool (5 modes break + --layers by content). comp-kuzu /
  comp-which / HUD unaffected. 64/76 routable tools touch no registry. --definitions crashed on
  Subject/Function (U+26D4 / cp1252) — **fixed at this seat 2026-08-12 ~20:5xZ, all-ASCII v2.1**.
  --refresh REGRESSES last_review to a hardcoded 2026-06-15. Seven annotation-like stores exist;
  none keys on world-model entities. c3-walk-agenda resolves the lifecycle enum by FIRST-MATCH regex
  (ordering-fragile). keep-dormant.yaml has the richest annotation schema; its declared consumer
  does not exist.
- **04:** EXACTLY ONE code read of C4 data in the repo (`opal_estate_infrastructure.py:660`). C4 is
  not in the graph, has no snapshot, no gate/hook/CI dependency. `c4_verticals` is a fossil — but a
  DUPLICATE in the RULE_BANK still reads RATIFIED and asserts the invariant R2 inverts. The
  andrew-infrastructure rename landed in prose, NOT in the data key the tool serves. The grid
  membership computation R1 assumes **does not exist yet** (38 slots are hand-assigned).
- **05:** Kimi pipeline is DEPLOYED and fired today (schedule verified at 3 layers; code currency
  ETag-verified). It does NOT emit a semantic layer — 4 prose fields on named entities, allowlist-
  enforced. **Friction/state kinds are NOT in the deployed runner** (0 occurrences; hand-fired CRO
  scripts only). **The text-input uploader is live (6 days of captures) but the runner reads NONE of
  it** — corpus frozen at 2026-07-30. The estate report IS the Kimi pipeline (one system). Andrew
  stood C3.ii down 08-06 ("Do not worry about C3.ii just yet") — today's R2 supersedes. Drift:
  EC2_MANIFEST.json stale on instance-id + deployed-commit; estate-capture-writer IAM path matches
  zero live objects (works only via ambient admin creds); ESTATE_GRAPH_KEY applied-but-unread.
