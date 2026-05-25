# LD-0067 Workstream B — Docker quarantine pre-positioning one-pager
**archetype:** EXPLORE
**secondary_archetypes:** TRACE
**Date:** 2026-05-25
**Serial:** 0.7.0_AE_CloudOps
**Authority:** LD-0068 spawn-with-direction §2 immediate work; LD-0067 Workstream B owner
**Status:** PRE-POSITIONING ONLY — implementation gated on ws CTO Workstream A spec landing (~1-2 day ETA)

---

## TL;DR

**Existing `projects/docker_exam/` is empirically a working v0 of LD-0067's quarantine protocol.** It implements every security primitive LD-0067 specifies (`--network none`, `--read-only`, `--tmpfs` scratch, `--cap-drop ALL`, `--security-opt no-new-privileges`, non-root user, RO bind-mount inputs, sentinel-based completion verification, YARA + pattern-analysis with zero execution). Operationally validated on 3 untrusted zips 2026-03-26. Docker runtime present and healthy on the workspace machine (`Docker 29.4.3`). **~80% of the security infrastructure is reusable; WS-A spec needs to define the ~20% delta** (input-source class, Phases 1/2/5/6 semantics, AST parser integration). Strong de-risking signal for the WS-B implementation ETA.

---

## §1 — Workstream B scope recap (from LD-0067)

| | |
|---|---|
| **Owner** | 0.7.0_AE_CloudOps (this serial, base lane per LD-0068) |
| **Gating dependency** | ws CTO Workstream A security protocol spec landing at `docs/architecture/CASE_FIND_SECURITY_PROTOCOL.md` (~1-2 day ETA) |
| **Original LD-0067 ETA** | ~3-5 days post-spawn |
| **Goal** | Docker quarantine infrastructure on workspace machine; lifecycle scripts (container spin-up / file injection / analysis-tool integration / teardown); integration interface for /case-find Python invocation; testing harness verifying isolation actually holds |
| **Phased rollout** | /case-find v1 (NOW) = Phase 1 metadata-only (text-only, zero-risk, no quarantine); /case-find v2 (post WS-B) adds Phases 2-6 quarantine-dependent deep-inspection |

LD-0067 6-phase quarantine pattern (canonical):

| Phase | Activity | Risk profile |
|---|---|---|
| 1 — Metadata only | Fetch README / package metadata / license / basic stats / dependency tree | Zero (text-only) |
| 2 — Assess | /case-find judges: is deeper inspection warranted? | Zero (judgment) |
| 3 — Quarantine | Docker container `--network=none`, no host fs mount, read-only ephemeral storage, resource limits; download specific files INTO container | Bounded (network-isolated, no host exposure) |
| 4 — Analyze | AST parse, dependency walk, pattern shape extraction, suspicious-indicator detection — NEVER execute downloaded code | Bounded (no execution; static analysis only) |
| 5 — Extract | Abstract Case insight only ("library X uses pattern Y via mechanism Z"); discard raw files | Zero residual |
| 6 — Cleanup | Wipe quarantine container; zero persistent storage of external code on host | Zero residual |

---

## §2 — Major reuse finding: `projects/docker_exam/`

Discovered during pre-pass audit. Pre-existing workspace infrastructure that implements ~80% of WS-B's security primitives. Treat as the architectural foundation for WS-B, not a reference.

### What docker_exam does

Air-gapped Docker scanner for untrusted zip archives. Inputs are mounted read-only; everything else is RAM-only or denied. Produces a JSON severity report with phase-by-phase progress logging. Sentinel-based completion verification catches mid-scan container crashes.

### Security primitives implemented (line-by-line LD-0067 alignment)

Source: `projects/docker_exam/run_exam.sh:61-72` + `projects/docker_exam/Dockerfile`

| LD-0067 requirement | docker_exam implementation | Status |
|---|---|---|
| Network isolation | `--network none` | ✅ identical |
| No host filesystem mount | Only RO bind-mount for input zips: `-v abs:container:ro` | ✅ identical |
| Read-only ephemeral storage | `--read-only` (container fs) + `--tmpfs /workspace:rw,noexec,size=512m` + `--tmpfs /tmp:rw,noexec,size=64m` | ✅ identical (+adds `noexec` and size cap) |
| Capability drops | `--cap-drop ALL` | ✅ identical |
| No privilege escalation | `--security-opt no-new-privileges` | ✅ identical (additive over LD-0067 minimum) |
| Non-root user | `useradd -m -s /bin/bash examiner; USER examiner` (Dockerfile) | ✅ additive over LD-0067 minimum |
| No code execution | `scan_archive.py` uses `zipfile.ZipFile.read()` for content inspection only; magic-byte + YARA + regex; never `exec()`/`import`/`subprocess` on archive content | ✅ identical |
| Suspicious-indicator detection | YARA rules in `projects/docker_exam/yara_rules/malware_basics.yar` (reverse shells, miners, obfuscated python, credential harvesters) + 8 regex patterns + 3 shell-only patterns | ✅ ready-extensible |
| Completion verification | Sentinel line `SENTINEL: SCAN_COMPLETE` on stderr; `run_exam.sh:81-86` greps for it; mid-scan container crash → no sentinel → wrapper exits 1 | ✅ additive over LD-0067 minimum |
| Phased structure | 5 phases (zip structure → bombs/traversal → exec scan → pattern scan → YARA) with per-phase `phases_completed` tracking | ✅ mirrors LD-0067 Phases 3-5 partially |

### Empirical validation

`projects/docker_exam/reports/scan_v1.1_fixed.json` (2026-03-26T13:39Z) shows 3 untrusted zips processed cleanly: pi-autoresearch-main (916KB), impeccable-main (9.1MB), and a third — all reach `all_phases_complete: true` with status `CLEAN_WITH_NOTES`. Pattern works in practice on real-world inputs of the scale LD-0067 targets.

### Deltas vs LD-0067 (~20% to specify in WS-A)

| Delta | Current docker_exam | LD-0067 requires | WS-B implementation work |
|---|---|---|---|
| **Input source class** | Zip archives mounted RO | GitHub repos / PyPI packages / arbitrary HTTPS-downloaded code | Container-internal `git clone` OR `pip download --no-deps` OR `curl/wget`; happens AFTER `--network` is briefly enabled OR via pre-fetched RO mount (Phase 1 + Phase 3 architecture call belongs to WS-A) |
| **Phase 1 (metadata-only)** | n/a | Fetch README / package metadata / license / deps tree text-only | NEW: lightweight non-quarantined fetcher path; either `pip show` / GitHub API / PyPI JSON API; runs OUTSIDE quarantine (text-only metadata) |
| **Phase 2 (assess)** | n/a | /case-find judgment gate: deeper-inspect or skip | NEW: invocation surface for CL CVO judgment; returns boolean for Phase 3 escalation |
| **Phase 4 (analyze)** — AST parsing | n/a (regex + YARA only) | AST parse + dependency walk + pattern shape extraction | NEW: add Python `ast` module integration; possibly `tree-sitter` for multi-language; emits structured AST findings |
| **Phase 5 (extract)** — Case insight format | JSON report (severity-classified findings) | "Abstract Case insight only — library X uses pattern Y via mechanism Z" | NEW: Case-shape emitter (separate from severity report); defines what goes into Case queue |
| **Phase 6 (cleanup)** — explicit wipe | `--rm` removes container | "Wipe quarantine container; zero persistent storage of external code on host" | Mostly satisfied by `--rm` + tmpfs RAM-only; add explicit attestation log line proving no host-fs residue |
| **Resource limits (CPU/memory)** | Tmpfs sizes capped (512m + 64m) | "memory/CPU caps" | Add `--memory`, `--cpus`, `--pids-limit` flags |
| **Runtime budget** | None | (LD-0067 implicit) | Add `--timeout` wrapper or container-level kill clock |

---

## §3 — Docker security best-practices survey

Cross-referenced against LD-0067 + docker_exam + standard Docker hardening guidance. The full list of flags that should be in WS-B's canonical `docker run`:

```bash
docker run --rm \
    --network none \                          # LD-0067 §3 / docker_exam:62
    --read-only \                             # docker_exam:63
    --tmpfs /workspace:rw,noexec,size=512m \  # docker_exam:64
    --tmpfs /tmp:rw,noexec,size=64m \         # docker_exam:65
    --cap-drop ALL \                          # docker_exam:66
    --security-opt no-new-privileges \        # docker_exam:67
    --security-opt seccomp=default \          # additive: kernel-syscall filter (Docker default OK)
    --pids-limit 256 \                        # additive: fork-bomb cap
    --memory 1g \                             # additive: OOM cap
    --memory-swap 1g \                        # additive: no swap escape
    --cpus 2.0 \                              # additive: CPU cap
    --ulimit nofile=1024:1024 \               # additive: fd exhaustion cap
    --user examiner \                         # additive: explicit non-root (covered by Dockerfile USER)
    -v "${INPUT}:/quarantine/input:ro" \      # RO bind-mount only
    -v "${OUTPUT}:/quarantine/output:rw" \    # RW output (Case insight emit ONLY; not raw code)
    "${IMAGE_NAME}" \
    "${ANALYZE_ARGS[@]}"
```

Additional hardening considerations (WS-A spec call):

- **User-namespace remapping** (`--userns=host` vs `dockerd --userns-remap`): host-remap better isolates UID; ws CTO call whether worth complexity for workspace single-tenant
- **Rootless Docker** vs root daemon: rootless better isolated but Windows-host complications (`Docker Desktop` runs daemon in WSL2 VM — already isolated from host kernel)
- **AppArmor / SELinux profiles**: Linux-only; Windows host = N/A; document fallback
- **Image-build trust chain**: pin base image SHA (`python:3.12-slim-bookworm@sha256:...`); rebuild trigger ledger; immutable image tags
- **Container restart policy**: `--restart=no` (default with `--rm`); ensure no auto-restart on crash hides analysis failure

---

## §4 — Phase 4 (analyze) tool survey

LD-0067 Phase 4 = AST parse + dependency walk + pattern shape extraction + suspicious-indicator detection. Existing comp-* tooling assessment:

| Tool | Capability | Phase 4 fit |
|---|---|---|
| **`comp-trace`** | dependency tracing across workspace nodes | NO direct fit — operates on workspace artifacts, not arbitrary external code |
| **`comp-blast`** | blast radius from workspace node | NO direct fit — same |
| **Python `ast` module** | AST parse for Python | YES — primary tool for Phase 4 on Python sources (PyPI packages, GitHub Python repos) |
| **`tree-sitter`** | multi-language AST parsing | YES — needed for JS/TS/Go/Rust GitHub repos (Sources A, B, C, E per LD-0067) |
| **`grep`/`ripgrep`** with curated patterns | Suspicious-indicator detection (eg. `subprocess.`, `exec(`, `eval(`, network primitives) | YES — docker_exam already implements 8 regex patterns + 3 shell-only patterns; extensible |
| **YARA via `yara-python`** | Structural rule matching | YES — docker_exam already uses; rules extensible at `projects/docker_exam/yara_rules/*.yar` |
| **`pip-licenses` / `licensecheck`** | License-text extraction | YES — Phase 1 metadata-only fits |
| **`safety` / `pip-audit`** | Known-CVE check against requirements | OPTIONAL Phase 4 sub-check (advisory; not blocking) |
| **`bandit`** | Python static security scanner | OPTIONAL — overlaps with custom regex but more comprehensive Python-only |

**Recommendation for WS-B implementation:** start with Python `ast` + tree-sitter (for non-Python) + existing YARA rules; layer in `bandit` / `safety` later if signal-quality warrants. AST-parse-without-import is the load-bearing primitive — never `import` external module to read its AST; use `ast.parse(source_text)` against file bytes only.

---

## §5 — PyPI supply-chain attack indicator taxonomy candidates

Quick survey of public attack pattern docs (memory + general knowledge, no external fetch in this pre-pass to keep scope tight; full WS-A research is CTO's). Candidate indicators for Phase 4 suspicious-indicator catalog beyond what docker_exam already catches:

| Indicator class | Attack pattern | Detection signal |
|---|---|---|
| Typosquatting | `requests-oauth` (legit) vs `requests-oauth2` (malicious) | Name-similarity to popular packages; check against PyPI top-N download list |
| `setup.py` arbitrary exec | Package install runs malicious code at `pip install` | AST scan for `subprocess`/`os.system`/network calls inside `setup.py` — we already don't `pip install`, but flag presence |
| `__init__.py` exec on import | Trigger fires when consumer `import`s package | AST scan for `subprocess`/network calls at module top-level (not inside functions) — we don't `import`, but flag presence; this is a key bandit check |
| Encoded payload | `exec(base64.b64decode(...))` | docker_exam already catches via SUSPICIOUS_PATTERNS; extend rule set |
| Network beacon | DNS / HTTP request to attacker-controlled host on import | Static URL extraction; cross-ref against known C2 indicators; AST flag for `urllib`/`requests`/`socket`/`http.client` calls |
| Credential exfil | Reads `~/.aws/credentials` / env vars / `~/.ssh/*` | Static grep for credential file paths in source; AST flag for `os.environ.get('AWS_*')` patterns |
| Package binary content | Non-Python binary blobs shipped with package | docker_exam catches via magic-byte + extension check |
| Hidden dependency drift | Package depends on different package than declared | Compare `requirements.txt` to actual `import` statements via AST |
| Setup hook abuse | `setup.cfg` / `pyproject.toml` build-time hooks (PEP-517) | Extract build-system declarations; flag custom build hooks |
| Filesystem write at runtime | Writes to outside-tmpfs paths once `--network` is on (if Phase 3 briefly enables network for clone/download) | Container-level: tmpfs traps catch this; static: flag `open(..., 'w')` outside expected paths |

Cross-reference: this taxonomy is offered as **suggestions for WS-A spec**, not authoritative. ws CTO owns the final taxonomy structure.

---

## §6 — Implementation sketch (pre-spec; subject to WS-A ratification)

Provisional WS-B deliverable shape, assuming WS-A spec lands close to LD-0067 framing as-is:

```
projects/case_find_quarantine/
├── Dockerfile                    # python:3.12-slim + tree-sitter + bandit + safety + yara-python + ast tooling
├── README.md                     # canonical invocation pattern + security primitive table
├── run_quarantine.sh             # wrapper: validates inputs, runs docker w/ full hardening flag set, sentinel-checks
├── lifecycle/
│   ├── phase1_metadata.py        # OUTSIDE container — text-only metadata fetch (PyPI JSON API, GitHub API)
│   ├── phase2_assess.py          # OUTSIDE container — invokes CL CVO judgment, returns boolean
│   ├── phase3_quarantine.py      # spin-up container, inject specified files
│   ├── phase4_analyze.py         # INSIDE container — AST + YARA + tree-sitter + suspicious-indicator scan
│   ├── phase5_extract.py         # INSIDE container — emits abstract Case insight (no raw code)
│   └── phase6_cleanup.py         # tear-down attestation log; verify zero host-fs residue
├── analyzers/
│   ├── python_ast.py             # Python-specific AST analysis
│   ├── tree_sitter_multi.py      # JS/TS/Go/Rust/etc.
│   ├── suspicious_patterns.py    # regex catalog (extend docker_exam's SUSPICIOUS_PATTERNS)
│   └── case_insight_emit.py      # Phase 5 Case-shape emitter
├── yara_rules/                   # symlink or copy from projects/docker_exam/yara_rules/
│   ├── malware_basics.yar        # reuse
│   └── supply_chain.yar          # NEW: typosquatting, package-import-exec, etc.
├── integration/
│   └── case_find_invoke.py       # Python interface for /case-find SKILL.md invocation
└── tests/
    ├── test_isolation_holds.py   # verify --network none actually blocks; verify host-fs unreachable; verify cleanup
    ├── test_phase4_no_exec.py    # invariant: external code is NEVER executed
    ├── test_known_malicious.py   # fixture: known-bad packages flagged correctly
    └── test_known_clean.py       # fixture: known-clean packages pass without false-positive

```

**Reuse vs new (estimate):**
- ~60% of `run_quarantine.sh` = copy of `projects/docker_exam/run_exam.sh` with flag additions
- ~80% of `Dockerfile` = copy + tool additions
- ~50% of `phase4_analyze.py` = adapted from `scan_archive.py` Phases 3-5
- `yara_rules/malware_basics.yar` = direct reuse
- All `phase1_metadata.py`, `phase2_assess.py`, `phase5_extract.py`, `phase6_cleanup.py` = NEW (no docker_exam analog)
- All `analyzers/` = NEW (docker_exam doesn't AST-parse)
- All `tests/` = NEW (docker_exam has no test harness)

**ETA refinement (vs LD-0067's ~3-5 days):** with docker_exam reuse, WS-B implementation closer to ~2-3 days post-WS-A-spec-landing. Major reuse de-risks the security-primitive layer; net delta is the Phase-1/2/5/6 NEW work + analyzer integration.

---

## §7 — Open questions for ws CTO (Workstream A spec)

These are decisions WS-A should make explicit so WS-B has a clean impl target:

1. **Phase 3 input ingestion path** — option (a) container-internal `git clone` / `pip download` with brief `--network bridge` then `--network none` for analysis; option (b) host pre-fetch + RO mount into container (never enables network inside container). Trade-off: (a) simpler; (b) network always off inside quarantine — stronger guarantee but adds host-side fetch surface.
2. **Phase 4 multi-language scope** — Python-only v1, multi-language v2? Or full multi-language from day one via tree-sitter? Affects Dockerfile bloat + analysis runtime budget.
3. **Phase 5 Case insight schema** — formal JSON schema for what goes into Case queue? Or freeform structured text? Affects CL CVO /case-mgmt downstream ranking.
4. **Phase 6 cleanup attestation** — what counts as proof of "zero residual"? Container exit code + tmpfs auto-wipe vs explicit verification step + audit log line.
5. **Container image trust model** — pin base by SHA256 digest? Image rebuild trigger ledger? Where does the trust chain root?
6. **Suspicious-indicator severity action gates** — at what severity does Phase 4 trigger CVO judgment gate (Phase 4 → Phase 5 conditional)? Or do all Phase 4 outputs go to Phase 5 with severity-classification preserved for CVO downstream?
7. **Per-source quarantine cap respect** — does each `/case-find` invocation pull `Decision #7` per-source caps (A=5/B=7/C=5/D=3/E=5 = ~25 total) and respect them in the quarantine batch, or is the batch unit determined upstream?

---

## §8 — Pre-positioning summary

**Status:** PRE-POSITION COMPLETE for the ~1-2 day WS-A spec window.

**Material ready for fast WS-B implementation start once WS-A spec lands:**
- ✅ Reuse foundation identified (`projects/docker_exam/`)
- ✅ Security primitive table cross-referenced LD-0067 ↔ docker_exam
- ✅ Docker hardening flag set drafted
- ✅ Phase 4 tool survey complete (Python `ast`, tree-sitter, YARA, `bandit`, `safety`)
- ✅ PyPI supply-chain attack indicator candidates drafted
- ✅ Implementation sketch + directory structure proposed
- ✅ ETA refinement: ~2-3 days post-spec (vs LD-0067's original ~3-5 days)
- ✅ Open questions for WS-A surfaced
- ✅ Docker runtime confirmed present (`Docker 29.4.3`) + healthy on workspace machine

**No code shipped this session** (LD-0067 explicitly gates WS-B on WS-A spec landing; pre-positioning is read+survey+document only).

**Next:** turn to ADVI_DEMOV1.007 design-choice proposal per ws COO 2026-05-25T23:13:25Z GO + LD-0068 §2 carry-forward. Sequencing decision communicated in RAVC-ACK MCP `~20260525T231618Z`.

---

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-trace` | Not run | EXPLORE-class pre-positioning; survey scope was existing workspace artifacts + Docker primitives (not workspace-dependency tracing). |
| `comp-blast` | Not run | No workspace-node change in scope (pre-pass only — no code authored). |
| `comp-pipescript` | Not applicable | No pipeline-script involvement. |
| `comp-iam` | Not applicable | No IAM change. |

One-line justification per SESSION_LOG_STANDARD: pre-positioning audit had no compile-graph node touch surface; all comp-* would have been no-ops.

## Mandatory Logging

- `org/compiler-tools-log.md` — no comp-* runs this session (justified above).

## Authority Trail

- LD-0068 spawn-with-direction (Andrew sovereign 2026-05-25T~23:05Z) — base AE re-spawned for LD-0067 WS-B + .007 carry-forward
- LD-0067 (Andrew direct 2026-05-25T~22:35Z) — security quarantine protocol; AE owns WS-B
- This session: pre-positioning audit + one-pager; no code, no commits to workspace infrastructure

## Next Steps

- [self] turn to ADVI_DEMOV1.007 design-choice proposal (Option i clean-before-write vs Option ii faker-seed-by-id deterministic refactor); MCP to ws CTO for ratification with CC ws COO + CVO
- [ws CTO] Workstream A spec authoring at `docs/architecture/CASE_FIND_SECURITY_PROTOCOL.md` (~1-2 day ETA)
- [self / post-WS-A] WS-B implementation per refined sketch in §6 (~2-3 days post-spec)
- [self / parallel] check production-side ADVI_INFTXN aggregator chain — natural cron 2026-05-25T13:00Z snap=2026-05-24 Sunday should be empirical proof of weekend empty-day fix (`inf-pipeline-v1.7.66`); surface any divergence to ws COO
