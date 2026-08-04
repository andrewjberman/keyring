# Startup, tranche-1 verify, weight ruling, and the DIVERGENT board's collapse into join artifacts

**archetype:** MIXED (VALIDATE + DIAGNOSE + COORDINATE)
**Serial:** `1.0.0_SA_CTO~B` (RCG execution-coordination seat; fresh session, Andrew-direct:
*"I am bringing you online to work with 4.0.0_SA_CRO. Finish your startup and check in with them
at startup readiness."*)
**Window:** 2026-08-04 13:30Z - 15:40Z
**Counterpart:** `4.0.0_SA_CRO` (live throughout; 5 messages received, 5 sent). Also
`0.7.0_AE_CloudOps` (one routed commit request, pending).
**Commits (mine):** `240e00113` (.gitignore), `74a539af8` (PNG rehome), custody commit for 18
.tools files (HEAD of that motion). Derive the exact set:
`git log --author="1.0.0_SA_CTO~B" 240e00113^..HEAD`.

## Startup

Registered as the full lane serial (PID 1412), Monitor `bufztnx4s` armed + TaskOutput-confirmed
running, serial file written, audit-archive-invoker rc=0/0 findings, PATH 94/94 + comp-which
exercised (banner, not just resolution), zero stale crons, zero formal TOs (work arrives via
CRO/Andrew). Cited commits verified before acting: protocol @d504050e5, sweep @ac147b78a, and
the Andrew-GO relay @ff160d0b5 (base CTO's verbatim start-slate record).

## Decisions issued (this seat as execution gate)

1. **Cycle-3 protocol ACK, both asks granted** (135024Z): new LABELS source
   `cycle3_adjudication` @ weight 3.0 (parity-with-delegation, revisit at cycle-4 once E-0004
   calibration exists); DIVERGENT-routes-to-CTO~B as drafted. Tranche-1 GO.
2. **Correction-source weight ruling** (145728Z), grounded by reading the 4,114 rows before
   ruling: `precedence_correction` (4,110 rows, all R-0022 restorations of Andrew-ratified
   cohort verdicts) = **5.0** — the census had exposed a real inversion: at silent-default 2.0
   they trained BELOW the delegation rows (3.0) that contradicted them.
   `coherence_correction` (4 rows, R-0023 + CTOB-RCG-001 dependency holds) = **3.0**, NOT the
   proposed blanket 5.0 — they are evidence-based agent adjudication, the same epistemic class
   as cycle3_adjudication. **Principle: weight follows the WARRANT'S ORIGIN, not the writing
   hand; the discriminator is whether the row adds judgment.** Calibration flag attached
   (+4,110 KEEP-mass at 5.0 — watch archive-recall in E-0004). CRO wired it @1ba9301bfd,
   census-verified zero unruled sources.

## Verification (the seat's re-derive habit, and what it caught)

- **Tranche 1 @bc34f46af re-derived from the commit:** 333 rows exact (318 KEEP@HIGH =
  94+224, 11 ARCHIVE@LEAN, 3 MIGRATE@LEAN, 1 REFERENCE_KEEP@HIGH); ARCHIVE rows sit in
  exactly the 4 uncontested orphan trees; **zero** labeled rows inside any DIVERGENT tree.
  CRO's message was right and their commit subject (337/228) wrong, as they self-flagged.
- **Machine-table defect (my 142159Z finding, CRO fixed @7548e90c7):** the evidence-table
  JSON still carried the retracted trending_image ORPHAN verdict — the single stale tree
  explaining the whole 71-vs-75 / 27-vs-28 / 6-vs-7 reconciliation. Subject and message were
  each internally consistent **with different records** — the pyiceberg prose-vs-artifact
  class in machine-readable form.

## The DIVERGENT board: every driven item so far is a JOIN-KEY artifact

Of 28 DIVERGENT trees, 5 driven to ground this session; **all 5 resolved to instrument join
artifacts, not estate incoherence** (plus 1 true gap + 1 dead tree):

| Item | Truth | Resolution |
|---|---|---|
| inf-gold-trigger "registry gap" | Registered; canonical = `inf-pipeline/inf-gold-trigger/` (last commit `056106aa3` == map's `last_deployed_commit`). Adjudication tree = stray pre-move copy, 2026-05-07, 673 diff lines behind | ARCHIVE evidence to CRO |
| public-data-router "registry gap" | Registered; canonical = `lambda-edge/public-data-router/` (2026-07-28). Stray tree 2026-01-19 | ARCHIVE evidence to CRO |
| m365-ms-ingest-liveness | **The one TRUE Rule-4 gap.** Entry drafted in-tree (mirrors sibling m365-otp-liveness, from ms-ingest.tf:74-82); owned-paths correctly refused CTO~B (YANG_PIPELINE_DEPLOY); routed to 0.7.0_AE to land per the a536173f0b precedent | At AE, pending |
| portal_authorizer "TF-declared not live" | `opal-portal-authorizer` **IS live** (get-function OK) — prefix-join miss, the trending_image class again. Registry+TF+live all cohere on `infra/aws/users/lambda/portal-authorizer/`. Stray 2-file tree (2026-04-06) | ARCHIVE evidence to CRO |
| finbert "TF-declared not live" | Tree genuinely dead (not live — exercised ResourceNotFound; not registered) **but its TF signal was policy-NAME noise**: `lambda-invoke-finbert`'s actual Resource is `opal-news-ai-sentiment`, which IS live (rc=0). Live grant, live function, historical name — not IAM debt | ARCHIVE evidence to CRO (s.4 recipe pass applies) |

Instrument synthesis sent to CRO: path-keyed registry joins vs name-keyed live/TF joins
manufacture DIVERGENT wherever a source moved or a name carries a prefix; recommend reading
the remaining ~17 class-(i) rows under that prior. smartx config.py:128 downgraded on read:
the `smartx_query` literal is the **fallback default behind a Secrets-Manager primary** —
latent-path finding for the exporter owner, not a live break.

## Root cleanup (CRO 065740Z, all landed)

`.gitignore` +`.ruff_cache/`+`catboost_info/` @240e00113 (BASE_EXEC held via tilde
inheritance, `.owned-paths.yaml:43` + the auto-permit at `owned-paths-validate.py:125-160`);
PNG rehomed to `docs/architecture/` @74a539af8 (CRO's AD staged residue cleared in the same
motion); **18** orphaned sole-copy .tools files custody-tracked (CRO's count of 75 had fallen
to 18 by measurement time; incl. the check-inbox/inbox-watch comms shims + the /prd-delta
engine; two lint-only touches to pass the universal gate). **Deliberately excluded:** the two
2026-08-04T10:0xZ pipescript-suite git-hooks files — ADHOC F9's live in-flight work, not
orphans.

## Errors I made, and what caught each

1. **Accepted "3 registry gaps" into my own board message before grounding them** — two were
   not gaps. Caught by checking the registry under the FUNCTION name rather than the tree
   path before editing. The correction went on the record to CRO same-session.
2. **A `list-functions --query contains(...)` probe returned empty for a function proven live
   one call earlier** — bad oracle discarded, single `get-function` per name substituted.
   Same class again minutes later: three piped `get-function` calls printed nothing at all
   (`2>&1 | head -1` swallowed stderr); re-run clean, the answer appeared with `rc=255`.
   *Put the control on the retrieval* — twice in one hour.

## Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-which "how do I grep the repo"` | PASS | startup A.3 — forwarder RAN (banner). PATH 94/94 bare |
| `comp-surface-check` (via safe-commit) | OK x3 | no critical surface touched (gitignore/PNG/custody commits) |
| `comp-pulse diff` (risk-reflex) | CLEAN x3, 1 nudge | source-map commit attempt fired the immune-response citation (untracked-production-source gate memory); read |
| `commit-gate.sh` | BLOCKED then PASS | 3 ruff errors in 2 custody .py files (F401 x2, F541); fixed minimally, behavior unchanged |
| `owned-paths-check` | **BLOCKED (correct)** | refused CTO~B on lambda-source-map.json (YANG_PIPELINE_DEPLOY) — gate exercised, routed to AE rather than overridden |
| raw `git`/`python`/`aws` | used | ledger row arithmetic, tree-vintage forensics, live get-function grounding — no comp-tool models the label-ledger/registry/live three-way join. Operational `aws` calls (get-function) are off-rail per CLAUDE.md |

## Blockers

**NONE.** One pending external: 0.7.0_AE landing the drafted source-map entry (non-P0, no
deadline; I validate on their hash).

## Next Steps

- **[this seat]** class-(i) tf_file metadata backfill drafts (~17 registry entries) for the
  AE lane; validate the m365 source-map commit when AE reports; record the smartx fallback
  finding to the exporter owner; feed CRO's remaining 75-label set as resolutions land.
- **[`4.0.0_SA_CRO`]** label calls on the 4 stray/dead trees per my evidence (their lane);
  11-file micro-batch (must cite independence from the PARKED json/mdpf/* teardown — accepted);
  CVO~B blinds spec for E-0004.
- **[`0.7.0_AE_CloudOps`]** the 1-file source-map commit (command included in the 152305Z
  message).
