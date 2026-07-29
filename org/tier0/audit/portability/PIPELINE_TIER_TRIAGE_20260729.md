# PIPELINE_CODE tier — triage, severity correction, and routing

**Author:** `0.0.0_AB_MSTR~Z` · 2026-07-29
**Register of record:** `org/tier0/audit/portability/` (base confirmed this is canonical, amb-b-0008)
**Status:** triaged, NOT fixed — routed to owners. See §4 for why I did not touch these.

---

## 1. The numbers, with the denominator

From `census-siteZ-20260729.json` (24,778 tracked / 22,964 read / 1,814 unreadable):

| tier | count | meaning |
|---|---|---|
| live-code hardcode, executable | **103** | the raw candidate set |
| of those, **DEPLOYED** (in `lambda-source-map.json`) | 13 | |
| of those, **PIPELINE** `gold/silver/bronze` | 2 | |
| **one-off analysis / probes / misc** | 89 | |

## 2. SEVERITY CORRECTION — the "13 deployed" figure overstates the risk

**I am flagging this against my own numbers, because the raw count invites the wrong conclusion.**

The `smartx` `config.py` family (3 copies: `data/smartx/scripts/`,
`infra/aws/ec2/smartx-exporter/…`, `infra/aws/lambda/smartx_ingestion_pipeline/`) carries:

```python
# Local development paths
if platform.system() == "Windows":
    LOCAL_STAGING_DIR = r"C:\Users\AndrewBerman\OneDrive - Opal Capital\Desktop\ajb_workspace\..."
```

**That branch cannot execute on Lambda — Lambda is Linux.** So the DEPLOYED RUNTIME IS NOT
AFFECTED by these. The exposure is **local execution on a Windows device that is not base**, which
is exactly site Z, and nowhere else.

This is the same over-severity error I made on the six `comp-*` tools, where I labelled a
never-taken fallback as "breaks Z now." **A tier label that overstates spends attention in the
wrong place just as surely as one that understates.** The honest reading:

- **deployed runtime risk: NONE** from this family
- **local-dev-at-Z risk: REAL** — a Z developer running these gets a path that does not exist
- **`/mnt/c/Users/AndrewBerman/.win32s`** (same files, line 15) is a **WSL** secrets path — a
  *fourth* path flavour after `/c/`, `/cygdrive/c/`, and `/mnt/c/…/OneDrive…`

## 3. The genuinely-live one

`data/black_diamond/scripts/silver/merge-capital-gains.py:29`
```python
DOWNLOADS = Path(r'C:\Users\AndrewBerman\Downloads')
```
Not a guarded branch — an unconditional assignment reading base's Downloads folder. It is a
manual-input script (its header names a hand-downloaded `.xlsx`), so it is not on a schedule,
but it *would* fail immediately at Z with no fallback.

## 4. WHY I DID NOT FIX ANY OF THESE — ownership, not caution

**CLAUDE.md Rule 13 is explicit:** DS owns `data/*/scripts/{gold,silver,bronze}/*.py` end to end;
DT/AE own infra. Every file in §2–§3 is on one of those lanes, not mine. My charter is device
portability; it is not a licence to edit other lanes' pipeline code, and a portability fix that
lands in DS's silver tier without DS is exactly the kind of cross-lane edit the ownership rule
exists to prevent.

**Routing instead:**

| files | owner | recommended change |
|---|---|---|
| `smartx` `config.py` ×3 + `compute_account_distribution.py` ×2 + `consolidate_smartx_to_parquet.py` ×2 | **DS** (+ AE for the infra copies) | derive the Windows branch from the script's own location, or read an env var; the `.win32s` WSL path needs the same |
| `black_diamond/scripts/silver/merge-capital-gains.py` | **DS** | `Path.home()/"Downloads"` — portable, no site literal |
| `infra/aws/lambda/smartx_*` copies | **AE/DT** | same fix as the DS copies; note these are **duplicated** source, so a fix in one place does not travel |

**A structural note worth more than the individual fixes:** `config.py`,
`compute_account_distribution.py` and `consolidate_smartx_to_parquet.py` each exist in **three
copies** (`data/`, `infra/aws/ec2/…`, `infra/aws/lambda/…`) carrying the **same** literals. That is
one defect stamped three times, and fixing one copy leaves two. Whoever takes this should treat
the duplication as the primary finding and the path literal as its symptom.

## 5. The 89 one-off scripts

Probes, backfills, ad-hoc analysis (`data/inf/manual_api/probe_*`, `data/analysis/nna_*`, …).
Real hardcodes, but they are historical artifacts that ran once at base. **Recommendation: leave
them.** Rewriting 89 dead scripts spends the night for no live benefit, and each edit is a
cross-lane touch. If one is ever re-run at Z it fails loudly and obviously — the cheap failure
direction. They are enumerated in the census JSON if anyone wants the list.

## 6. What this closes

- `ACTIVE_TOOLING` tier: **CLOSED** (12/12 — 6 `comp-*` @`e95fdd7e42`, 4 harnesses +
  `block-bare-inbox-watch` @`a13254d38`, `settings.local.json` is permission-allowlist strings only).
- `PIPELINE_CODE` tier: **TRIAGED AND ROUTED** — not mine to land.
- Remaining unworked: `ARCHIVE_OR_TEST` (10), `COMMENT_ONLY` (1) — lowest value, and
  comment-only may be correct to keep as incident documentation.

---

# ADDENDUM — reclassified by REACHABILITY, because the name-based buckets were unreliable

**Added 2026-07-29 by `0.0.0_AB_MSTR~Z`, after catching my own classifier twice.**

## Why this addendum exists

Everything above was bucketed by a regex reading FILE NAMES. That classifier misfiled
`.tools/test-safe-commit-deletion-staging.sh` (matched `/test` on `.tools/test-...`) into
ARCHIVE_OR_TEST, which is how I came to report ACTIVE_TOOLING "closed 12/12" while a 13th file
survived. Re-examining that bucket by hand then found TWO more genuinely-active files
(`build_sandbox.sh`, `spawn_solver.sh` — matched on "sandbox" in a filename).

**A bucket produced by an unreliable classifier is not evidence.** So the tiers above should be
read as a first pass, and this addendum as the sounder cut.

## The sounder cut: reachability, not naming

| measure | count |
|---|---|
| executable files with a LIVE-CODE base literal | **106** |
| of those, referenced by ANY other tracked file | 83 |
| of those, referenced by **LIVE MACHINERY** (`.claude/settings*`, `.tools/`, `infra/aws/lambda/ci/`, `infra/aws/terraform/`, `.github/`) and not merely by a record | **19** |

The 83 figure is **too coarse to act on** — most of those references are historical mentions in
`commits.jsonl`, session logs and READMEs. "Something once wrote this filename down" is not
reachability. The 19 is the set worth anyone's attention.

## AND MY REFINED CLASSIFIER STILL PRODUCED A FALSE POSITIVE

`org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/hud3_classify.py` appeared in the 19 because
`.tools/hooks/comp-tool-hud.sh` mentions it — **in a COMMENT** (`# Re-tune to the post-hook
re-measure (hud3_classify.py)`). It is not invoked. My filter greps basenames and never checks
whether the reference is executable, so a comment reads as a dependency.

**Third iteration of one lesson:** name-matching found archives that were not archives;
reference-matching found dependencies that were not dependencies. Each refinement was a real
improvement and each still had the same shape of error. Treat the 19 as a FLOOR with known
false positives, not a verified set.

## Disposition of the 19

- **14** are the smartx / `lambda/ci` cluster already routed above to **DS** and **AE/DT**.
- **`infra/aws/globgrph/tool_activity_emit_local.sh:34`** — NEW, and genuinely live: invoked from
  `.claude/settings.json:188` as a SessionEnd hook. Its base literal is a **FALLBACK** after a
  `git rev-parse` primary, so it is **LATENT, not broken** — exercised at Z, rc=0. Identical shape
  to the 9 already fixed tonight. **ROUTED TO [0.7.0_AE_CloudOps] — `infra/` is not my lane
  (owned-paths DENY, confirmed by probe).**
- **`org/ka_testing/runtime/__init__.py:13`** — hardcodes a `portal` working directory. Last
  touched 2026-03-19; dormant. Low priority, no owner assigned.
- **`hud3_classify.py`** — false positive, see above. No action.

**A hypothesis I raised and then withdrew:** I suspected `tool_activity_emit_local.sh` explained
the missing site-Z telemetry. It does not — it works at Z. The telemetry gap was
`post-tool-telemetry.sh` failing open on absent jq, since fixed. Recording the retraction because
the two findings were adjacent and plausible, and plausibility is exactly how a wrong cause gets
attached to a real symptom.
