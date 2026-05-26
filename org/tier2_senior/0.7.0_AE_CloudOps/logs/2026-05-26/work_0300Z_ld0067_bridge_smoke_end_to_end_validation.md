# /work 03:00Z -- LD-0067 v1 bridge smoke test end-to-end validation (3 bug-fixes + scan_complete)
**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE
**Date:** 2026-05-26
**Serial:** 0.7.0_AE_CloudOps
**Cron-tick:** /work manual fire post-Andrew "docker now online" + smoke test completion
**Tier-0 commit hash at smoke completion:** `3107931c1` (Dockerfile.download zip fix; latest at smoke-complete moment)

---

## §1 -- Frame

Prior session 2026-05-26T~01:30Z shipped LD-0067 v1 bridge code (`f5b1bcda2`) but Docker daemon was 500 (Linux engine down post-restart). Andrew-side recovery 2026-05-26T~02:45Z unblocked smoke test surface. First end-to-end execution surfaced 3 sequential bridge bugs (path-form, missing zip pkg, zip-extension naming) each fixed + re-fired in same cycle. 3rd attempt completed end-to-end with all phases OK + JSON emission.

---

## §2 -- Bug-fix sequence (3 bugs surfaced + fixed)

### Bug 1 -- Docker-on-Windows build-context path bug

| | |
|---|---|
| Surface | `b1iyihob1` first end-to-end smoke 2026-05-26T~02:46Z |
| Error | `failed to build: unable to prepare context: path "/c/Users/AndrewBerman/Desktop/ajb_workspace/projects/case_find_bridge" not found` |
| Root cause | `MSYS_NO_PATHCONV=1` (needed for `-v` volume args) ALSO suppresses path conversion for `docker build` context; Docker-on-Windows can't resolve `/c/Users/...` Git Bash paths -- needs `C:\Users\...` form |
| Fix | `cygpath -w` conversion for build-context paths only; volume args (named volumes, no host path) unaffected |
| Commit | `e753824ad` work-cycle:0001 |
| Verification | `bash -n` syntax-validated + re-fire surfaced bug 2 (proves bug 1 cleared) |

### Bug 2 -- Missing `zip` in download image

| | |
|---|---|
| Surface | `b3e2wdro0` 2nd smoke 2026-05-26T~02:50Z |
| Error | `/opt/safe_download.sh: line 79: zip: command not found` -- Stage 3a exited 127 |
| Root cause | `Dockerfile.download` apk install missed `zip`; `safe_download.sh` github-repo branch uses `zip -rq` to package git-cloned working tree |
| Fix | Add `zip` to apk install alongside `git curl ca-certificates bash coreutils` |
| Commit | `3107931c1` work-cycle:0002 |
| Verification | Re-fire (after `docker image rm opal-case-find-download:v1` to force rebuild) surfaced bug 3 |

### Bug 3 -- zip auto-appends .zip extension

| | |
|---|---|
| Surface | `bkosjayu8` 3rd smoke 2026-05-26T~02:53Z |
| Error | `ERROR: downloaded blob is empty or missing` -- exit 4 from `safe_download.sh` line 104 |
| Diagnosis | Interactive Stage 3a debug container revealed `zip -rq /dl/blob .` actually wrote `/dl/blob.zip` (1.4MB) -- Info-ZIP auto-appends `.zip` when output path has no extension |
| Fix | `zip -rq "${BLOB}.zip" . && mv "${BLOB}.zip" "${BLOB}"` -- explicit `.zip` output then rename to honor `/dl/blob` artifact contract |
| Commit | (bundled with smoke re-fire `b5zvrb4bq`; commit landed mid-bg-task at unknown hash; will surface in next cycle) -- per `safe-commit.sh` log; work-cycle:0003 trailer |
| Verification | `b5zvrb4bq` 3rd smoke 2026-05-26T~02:58Z reached end-to-end completion |

---

## §3 -- End-to-end smoke test result (3rd attempt `b5zvrb4bq`)

**Status:** scanner `REVIEW_REQUIRED` (exit code 1); bridge mechanism CLEAN end-to-end.

| Surface | Result |
|---|---|
| Stage 3a download container (`--network=bridge`, named volume, nobody user) | OK -- git clone anthropic/anthropic-sdk-python.git, zip 5MB working tree to blob, sha256 + metadata emitted |
| Stage 3b analysis container (`--network=none`, named volume RO mount, no host bind) | OK -- scan_archive.py ran YARA + AST + magic-byte + suspicious-pattern detectors |
| Phase 6 cleanup trap | OK -- volume destroyed; both containers `--rm` auto-removed |
| JSON report emission | OK -- `projects/case_find_bridge/reports/case_find_20260526T025834Z.json` (6KB structured findings) |
| Exit code | 1 = REVIEW_REQUIRED |

### §3.1 -- Scanner findings classification (all FALSE POSITIVES on benign SDK)

| Severity | Count | Type | Reality |
|---|---|---|---|
| INFO | 20 | `executable_magic` (shebang scripts) + `autorun_path` (pyproject.toml) | Legitimate dev tooling (`scripts/test`, `scripts/lint`, etc.); pyproject.toml is standard Python project config; correct INFO classification |
| MEDIUM | 4 | `suspicious_pattern` (hex-encoded shellcode + base64 decode call) | TEST fixtures with hex-encoded data + legitimate MCP base64 usage in `src/anthropic/lib/tools/mcp.py` |
| HIGH | 5 | `yara_match` rule `credential_harvester` | Matches on legitimate credential-handling code (`src/anthropic/lib/credentials/_constants.py` + 4 auth tests) -- scanner over-fits on any credential mentions |

**Verdict:** all findings are scanner-conservativeness on a known-benign package (Anthropic's own SDK). The bridge MECHANISM is validated; scanner-tuning concerns route to CL CVO consumer-of-record per spec §10.

---

## §4 -- Expected vs actual

Prior session log next-step (`ld0070_postpostuse_hook_audit.md` table) predicted:

> AE 0.7: Bridge smoke test on Docker recovery: `./projects/case_find_bridge/run_quarantine.sh https://github.com/anthropics/anthropic-sdk-python` → expected CLEAN exit 0

**Actual:** exit code 1 (REVIEW_REQUIRED) -- bridge mechanism validated end-to-end BUT not the CLEAN exit-0 expected.

**Cause of mismatch:** `anthropic-sdk-python` was assumed to be a clean "benign" demo URL but it contains legitimate credential-handling code that triggers the conservative YARA `credential_harvester` rule. Not a bridge failure; not a scanner failure; an unfortunate test-candidate-vs-scanner-rule interaction.

**Implication for spec §8 WB-6:** Per spec, "End-to-end smoke test with 3 candidate URLs (1 benign, 1 obfuscated-eval, 1 setup.py-network)" -- the "benign" candidate needs to be a TRULY minimal repo with no credential code. Options:
- `https://github.com/sindresorhus/is-fullwidth-code-point` (1-function utility; ~10 lines; no credentials/network/auth)
- `https://github.com/visionmedia/dom-classes` (small utility)
- A purpose-built `opal-benign-fixture` repo with just `print("hello")`

Recommend WB-6 acceptance criterion explicitly cite the benign-test URL (with rationale that it has zero credential / network / dynamic-import surface). Captured as design-note for impl spec.

---

## §5 -- WB-1 substance status

Per CASE_FIND_SECURITY_PROTOCOL.md §8 WB-1 = "Build `opal-case-find-download` + `opal-case-find-analysis` images; push to ECR; pin digests; track digests in `infra/aws/ec2/case-find-quarantine/IMAGE_DIGESTS.json`."

| Substance | Status |
|---|---|
| Build `opal-case-find-download:v1` | DONE (local; not yet ECR) |
| Build `opal-docker-exam:1.1` | DONE (local; not yet ECR; image is from `projects/docker_exam/` -- predates LD-0067) |
| Push to ECR | NOT DONE (this is full WB-1; v1 bridge is local-only pre-positioning per LD-0067 Path-1 directive Andrew 2026-05-26T~0040Z) |
| Pin digests | NOT DONE (no ECR push yet) |
| `IMAGE_DIGESTS.json` ledger | NOT DONE |

**Distinction:** today's smoke test validates the **v1 bridge MECHANISM** (two-stage container pattern + named-volume blob transit + scanner contract) using locally-built images. **Full WB-1** (ECR push + digest ledger + IMAGE_DIGESTS.json + iptables egress per CV-A1 + IAM hard constraint per CV-A5) sequences post-LD-0078 spec-amendment RATIFY + WS-B impl spec authoring.

v1 bridge = working artifact CL CVO can consume for `/case-find` consumer interface development NOW. Full WB-1 production-grade ECR-backed runner lands per Workstream B planned phasing.

---

## §6 -- Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `comp-blast` | Not run | Bridge code changes are localized to `projects/case_find_bridge/*.sh` + `Dockerfile.download` (3 files); no portal/Lambda/EC2/IAM/Terraform changes. Per CLAUDE.md AE row, comp-blast on isolated bridge-project changes returns empty (no graph edges into rest-of-system yet -- CL CVO `/case-find` consumer interface will be the first edge). |
| `comp-iam service` / `comp-iam gaps` | Not applicable | No iam.tf change in this work (full WB-1 IAM provisioning lands in WB-2 per spec §8). |
| `comp-pipescript deployed` | Not applicable | Not a gold/silver/bronze script change. |

---

## §7 -- Authority + cross-references

- **LD-0067** (Andrew direct 2026-05-25T~22:35Z) -- security quarantine protocol; AE owns Workstream B
- **LD-0068** (Andrew sovereign 2026-05-25T~23:05Z) -- base AE re-spawn
- **LD-0077** (MSTR `cf0b2cdc5` 2026-05-26T01:55Z) -- batched ratification + WB-1 parallel auth
- **CVO LD-0077 independent verdict** (`07059979a`) -- CV-additives folded into design-readout `109db1fa8`
- **WB-1 design-readout matrix** (`109db1fa8`) -- this work-cycle log is the WB-1 substance-validation companion
- **Andrew direct unblock 2026-05-26T~02:45Z** -- "docker now online"
- **3 bug-fix commits:** `e753824ad` (path) + `3107931c1` (zip apk) + work-cycle:0003 (zip extension)

---

## §8 -- Next-step dispatch

1. RAVC2-Request to ws COO with smoke-validation evidence + scanner-finding classification + benign-test-URL recommendation for WB-6
2. CC Andrew, ws CTO, ws CVO (real-time stakeholder visibility)
3. v1 bridge consumable by CL CVO `/case-find` consumer interface (orthogonal to ratification chain)
4. Full WB-1 (ECR push + digest ledger + IAM-locked runner) queues post-LD-0078 RATIFY

---

-- 0.7.0_AE_CloudOps
2026-05-26
