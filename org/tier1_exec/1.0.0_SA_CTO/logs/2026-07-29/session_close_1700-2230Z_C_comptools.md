# 1.0.0_SA_CTO~C — session close 1700–2230Z — comp-tool lane (WS1–WS3 + kill list)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window

Spawn 170048Z (Andrew-direct via MSTR) → 2230Z. First log of this serial; window = whole session.
Scope: Andrew/CVO comp-tool builds only. Four workstreams assigned, three delivered.

## Commits (all pushed, ahead=0 behind=0 at close)

| commit | what |
|---|---|
| `950f62f9d3` | **comp-legacywriter** — writer-contest lens, 937-line engine + wrapper, registered 4 surfaces, battery 10/10 |
| `5cf848cb09` | comp-opalbizsem (superseded within the hour by Andrew's naming ruling) |
| `4ab259a2c0` | **comp-semantic-estates** — pipescript REVAMP; `pipescript` + `comp-opalbizsem` tombstoned rc=2 |
| `fa2f4398a6` | classifier tightening — cut 8 non-keys before the dead-key list reached a teardown ledger |
| `e7ce9db83f` | **comp-legacywriter --census** — deep dossiers, heat × dups × invocation joined |
| `d51f6b38a0` | TRANSIENT-MARKER guard + the live-verified KILL LIST deliverable |
| `842cbe867a`, `10052e6c54` | comp-system 06 regens — **both audited overrides DISCHARGED** |

## Delivered

**WS1 comp-semantic-estates** (engine `org/modules/graph/opal_business_estates.py`). Not a rename — a
revamp. The predecessor served S3 keys FROZEN AT GENERATION as fact (it called a pre-revamp mdpf key
"LIVE fresh" while the real serve had moved). New engine uses the snapshot for thread NAMES only and
re-derives every key from producer source at call time, then DIFFS. 40 of 71 concrete snapshot keys
have no live producer. Header contract FAIL-LOUD, controls 5/5 incl. corrupt-JSON (the case the
predecessor's bare `except: pass` swallowed).

**WS2 comp-legacywriter** + `--census`. Real population measured: 8,913 files, 857 write sites, 643
locations, **353 written surfaces with zero readers** — not 32. The 32 was the estate intersected
with a 44-day snapshot's 59 keys, i.e. a denominator inherited from a stale artifact.

**WS3 registry census.** The reported "PHANTOM" `comp-v5-composite-test` is NOT a phantom — the file
exists as `.tools/comp-v5-composite-test.sh`. Suffix mismatch, so the remedy inverts from
delete-the-row to reconcile-the-name; deleting it would have de-registered a live tool. 93-vs-89
resolved by SETS: the glob counts FILES (5 tools ship a bare wrapper + a `.py` twin), authority
counts TOOLS. CVO retracted the phantom finding on this; MSTR withdrew its amplification.

**KILL LIST** — `org/tier1_exec/1.0.0_SA_CTO/deliverables/KILL_LIST_WRITE_SURFACES_20260729.md`.
Tier A = dead write path (concrete key, bucket proven listable, no object, no reader, not a marker),
concentrated in `archive/` + `diagnostics/` + `test_*`. Tier B = 61 exist-with-no-AST-reader,
explicitly NOT killable on this evidence.

## Errors of mine, all recorded in-commit

1. **81/81 false absence from a CRLF bug.** Native Python wrote the candidate TSV with `\r\n`; bash
   `read` kept the `\r`; every AWS call asked for `key\r`. **The mechanism control passed AND the
   per-bucket control passed** — both typed literally in the shell, so neither carried the
   corruption. Corrected: 61 exist / 21 absent.
2. **Three live trigger markers put on a kill list.** `trigger-pending` / `trigger-mode` /
   `bronze-trigger-mode` are absent every time you look because they are written→consumed→deleted.
   Guard landed.
3. **Staging residue jammed fabric pulls.** Directory pathspec `infra/system/`; the leak guard
   blocked the COMMIT and I reported that as a clean save without checking the index. ~26 files
   stayed staged. A blocked commit is not a no-op.
4. **"under-enforcement" framing on owned-paths** — wrong, retracted in full. The base-serial
   auto-permit is deliberate, dated, safety-argued (RV-0030 F-003).
5. Ranking defect in my own census: `UNRESOLVED-BUCKET` scored 5/5 and floated to the top, ranking
   the least-knowable surfaces as the most dead.
6. Used `head-object` for existence — CLAUDE.md already says it IS `s3:GetObject` and never the
   acceptance instrument. It failed on a key `list-objects-v2` had just returned.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `comp-legacywriter` | built it; battery + estate census | PASS 10/10 |
| `comp-semantic-estates` | built it; drift report | PASS 5/5 |
| `comp-clobber` | grounding the false-positive class | PARTIAL — 8 of 11 reported clobbers are cross-firm path matches or probes |
| `comp-heat freshness --json` | producer code recency | PASS — 25,100 paths banded |
| `comp-dups --json` | exact-dup twins | PASS — 1 exact-dup group (smartx query lambda) |
| `comp-debris --types lambda,s3` | invocation/dormancy | PASS — 229 resources; **bucket-grain only** |
| `comp-coverage-check` | registration gate | FAIL→PASS; my untracked tool jammed all `.tools/comp-*` commits fabric-wide |
| `comp-manifest-check` | registration invariant | FAIL×4 → PASS (serial discovery, see gap) |
| `comp-surface-check` | verified CVO's upgrade | PASS + 3 findings adopted @cab9f323ab |
| `comp-which` | routing checks | PASS after vocabulary work |
| `comp-system` | 06 regen ×2 | PASS — both overrides discharged |
| `commit-gate.sh` | every `.py` edit | FAIL→PASS (ruff E402, dead bindings, f-prefixes) |

**What worked:** the gates. Leak guard caught a tenant `.env` sweep; coverage-check caught UNPLACED;
manifest-check caught unregistered; self-route caught undiscoverable; ruff caught dead code.
**What failed:** every control I wrote myself at MEASUREMENT time. The CRLF corruption passed two
of my own controls.
**Gap found:** the registration chain is 6 gates deep (coverage-map → tools_index → entries →
output-contract → self-route → PATH forwarder) and each only reveals itself after the prior passes.
I hit 5 serially on one tool, ~40 min. A pre-flight "everything registration will require" check is
a concrete design input for WS-C7. Second gap: a newly landed comp-tool is NOT shell-reachable until
`provision-path-shims.sh` re-runs, and nothing in the chain checks it — the chain proves the ROUTER
can name a tool, never that a SHELL can run it.

## Blockers

None. WS4 (comp-pipescript deployed hardening) and the M-2 population mutant are unstarted, not
blocked.

## Current State

- comp-legacywriter, comp-semantic-estates live, registered, PATH-reachable, batteries green.
- `pipescript` and `comp-opalbizsem` are rc=2 tombstones naming their replacement; both registered
  (comp-opalbizsem in `excluded_not_graph_use_cases` with reason).
- Kill list deliverable landed; Tier A unactioned, Tier B needs `comp-whoread`.
- Both audited `system-current-override` uses discharged. Index clean, nothing staged.
- Andrew overrode base CTO's post-wave rename hold (~1916Z) — recorded + broadcast, base CTO
  notified first.

## Next Steps

1. **[1.0.0_SA_CTO~C]** `comp-whoread` over Tier-B prefixes — the only reader oracle; converts 61
   candidates into verdicts. Then `comp-icedrill` + `comp-xray frozen` for key-grain.
2. **[1.0.0_SA_CTO~C]** WS4 comp-pipescript deployed hardening; M-2 population mutant (closes my
   PARTIAL verify of CVO's surface-check work).
3. **[1.0.0_SA_CTO]** Tier-A retirement authorization — `archive/`+`diagnostics/`+`test_*` writes,
   near-zero blast radius. Kill list is a recommendation, not an authorization.
4. **[2.0.0_SA_COO]** mdpf per-scope sweep with comp-legacywriter once CVO's battery clears.
5. **[3.0.0_SA_CVO]** 6 card corrections + freshness-ladder vocabulary riding WS3's semantics split.
