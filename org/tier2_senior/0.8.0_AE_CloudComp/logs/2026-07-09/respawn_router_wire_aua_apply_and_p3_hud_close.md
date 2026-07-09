# Respawn recovery: comp-system router-wire + inf value-parity AUA apply + P3-HUD leg (TOOLCHECK P3 complete)

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, IMPLEMENT

**Agent:** 0.8.0_AE_CloudComp
**Date:** 2026-07-09
**Window:** 2026-07-09T07:45Z -> 08:45Z (fresh session; prior lane WEDGED, MSTR respawned)
**TO:** NFRA_TOOLCHECK.P3 (`org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_TOOLCHECK.P3.comp-which-selector-and-hud.md`)

---

## Summary

Prior session wedged mid-dispatch and never engaged three delivered GOs. MSTR respawned this lane.
Answered COO~B's liveness probe honestly as `(c) DID NOT ENGAGE -- wedged`, re-armed the watcher,
and cleared all three dispatched items in COO~B's ordered sequence: router-wire -> AUA -> HUD.

Proposed slotting the ~5min AUA apply ahead of the router-wire (DS~A had waited ~40min on a
live hourly-firing alarm). COO~B OVERRULED on two axes: Andrew's NFRA-first mandate, and the fact
that base COO -- the AUA's actual OWNER -- had rated it non-bleeding. My "LIVE P0" framing was
more elevated than the owner's own rating. Accepted, named the error, ran the stated order.

---

## Work Completed

### 1. comp-system UNREACHABLE via comp-which -- oracle 37/38 -> 38/38 GREEN (`5d21baa6f`)

CVO caught the live oracle RED at HEAD. The GO (and CVO's note) described the fix as adding a
curated routing rule. **That alone would have been a NO-OP.** Grounded the actual mechanism in
source (Rule 22): comp-system is homed in `comp-coverage-map.yaml` `meta_tools[]` (it is a
cross-surface aggregator, so it has no single-surface home) with role `system-compiler`. That role
was absent from `comp_capability_provider._ROUTABLE_META_ROLES`, so provider:269 set
`routable=False`, and **`comp_route.py:329`** -- `caps = [c for c in provider.capabilities() if
getattr(c, "routable", True)]` -- dropped it from the default posterior router's candidate set
*before any scoring*. Verified live pre-fix: provider reported `comp-system kind=meta routable=False`.

Fix = both halves (mirrors the earlier comp-fedobs fix): added `system-compiler` to
`_ROUTABLE_META_ROLES` (which the provider's own `:88` comment mandates), plus a distinctive
SYSTEM-only curated rule. Deliberately did NOT claim bare `freshness`/`health` tokens -- those are
comp-freshness's and comp-heat's intents; stealing them trades one misroute for two.

Evidence (exercised; TEST1 is near-tautological by its own docstring, so I did not rest on it):
- cited query -> `comp-system` (was `comp-lambdamap parity`)
- NON-manifest paraphrase "how mature and healthy is the compiler system right now" -> `comp-system`
- neighbor non-regression, live: "is the upstream data fresh" -> comp-freshness; "which directories
  are dead and safe to delete" -> comp-heat; deploy-sha-parity -> comp-lambdamap. No intent stolen.
- held-out C1 eval vs the 5fc507a42 baseline: canon p@1 64.9% -> 65.8%; diverse 95.7% (unchanged);
  heldout 50%/70% (unchanged). struct-gate PASS every tier (zero E1 write-path leaks).
- Oracle re-run at the **post-merge live HEAD** `0e4300b9b`, not at my own commit -- a GREEN from a
  superseded tree would be a false cert.

CVO certed oracle-GREEN 080106Z -> P3-selector leg CLOSED.

### 2. inf value-parity anchor-date fix (`c9e42d485`) + deploy-ledger CLOSED GREEN 7/7 (`b210835f9`)

DS~A's root cause (CTO pre-apply GO 062304Z), **independently reproduced offline against live data
before touching Terraform**:

| anchor partition | sum(current_value) | vs served 202,246,989.07 |
|---|---|---|
| snapshot_date=2026-07-07 (unshifted, today's behavior) | 203,686,267.57 | diverges **+1,439,278.50** |
| snapshot_date=2026-07-08 (shifted, the fix) | 202,246,989.07 | MATCH, to the cent |

That +$1,439,278.50 IS the phantom "$1.44M" firing hourly since 2026-07-06T17:16:36Z. Served AUA was
never wrong; only the anchor LOOKUP DATE was.

**Two corrections to the CTO-GO'd patch, both PROVEN with terraform rather than argued:**
1. the proposed `source {}` block cannot coexist with the archive's existing `source_dir` --
   `terraform validate`: *"Attribute \"source_dir\" cannot be specified when \"source\" is specified"*.
   Replaced with `dynamic "source"` over `fileset(compdiff,"*.py")` + one explicit block for the
   calendar (dynamic, so a future compdiff module cannot silently drop out of inf's zip).
2. the proposed path `${path.module}/../../../data/...` resolves to `infra/data/` and does not exist.
   Correct depth is four levels.
Did NOT copy the calendar into `../../compdiff/` -- cot and 49f archive that same dir.

Deploy-ledger opened at apply-start, closed only on proof (never-half-land): L1 git; L2
safe-apply(HALTGT) `0 added, 1 changed, 0 destroyed`; L3 0-diff re-plan (exit 0); L4 dry-run
`fired=False exit=0`; L5 firm-scoping (see below); L6 deploy-sha parity `live CodeSha256 ==
sha256(built zip)`; L7 **behavioral, on a REAL scheduled EventBridge invoke**:
- `07:16:36Z` before: `[PUBLISH] fired=True published=True exit=1` -- `sum[2026-07-07]`, diverges 1,439,278.50
- `08:16:24Z` after:  `[PUBLISH] fired=False published=False exit=0` -- `sum[2026-07-08]`, diff 0.0000

**L5 closed with a CORRECTION, not against a criterion I had proven false.** DS~A's declared proof
("cot + 49f plan = ZERO diff") is unachievable, for two reasons, neither a firm-scoping failure:
cot archives the SAME shared `compdiff` dir (so editing the shared `.py` necessarily moves its
`source_code_hash`; environment block unchanged), and 49f-value-parity **is not deployed at all**.
Firm-scoping proven live instead: `VP_ANCHOR_DATE_SHIFT` only in inf's `.tf`; live cot env lacks it;
cot + 49f zips contain zero `_orion_vendor_asof.py`; passthrough unit-exercised byte-identical.

### 3. P3-HUD leg -- req#3 (a)-(d) + telemetry-fidelity fix (`c37c6ab27`)

The four behavioral changes were AUTHORED in the wedged session and never committed or verified. I
treated them as unverified code and exercised each against the real hook:
- **3a** throttle INVERTED. Precise class fires on hits 1 and 6 of 7 (CLASS_EVERY=5); comp_which
  fires on hit 1, silent on 2-3.
- **3b** leading-verb gate. `git push && terraform plan`, `echo hello && ls -la`, `python foo.py &&
  node b.js` -> silent; `cd portal && grep -rn useQuery src` -> still fires.
- **3c** pipe-grep exemption. `ps aux | grep python`, `git log --oneline | grep fix` -> silent; a
  LEADING `grep -rn useQuery portal/src | head` -> still fires.
- **3d** catch-all emits the EXACT tool+call via `comp-which --route-only`; suppresses entirely on
  NO-ROUTE (`xyzzy` -> silent) rather than nudging toward nothing. Deny path untouched.

**Telemetry-fidelity fix (new, and load-bearing for AC#2).** `comp-tool-hud.log` wrote the query raw
through `head -c 80`, so a multi-line command (`cd <ws>\n<real command>` -- the common Bash-tool
shape) SPLIT one HUD-HIT across several log lines, recording only its first line (a bare `cd`). Of
5190 BEFORE-window Bash entries: **3514 multi-line + 1517 truncated -> only 159 (3.1%) recoverable.**
The log could not serve the "CVO before/after measurement" its own comment claims. Now flattened to
one line + 200-char cap (verified 1 log line where it wrote 3). No consumer parses it structurally.

**AC#2, measured on the 159 fully-visible entries** (the rest EXCLUDED -- counting them would be an
artifact): compound-op false-fire 8 (5.0%), pipe-grep false-fire 48 (30.2%) -> **56 (35.2%) now
gated**, 103 (64.8%) legitimate nudges preserved. Confirmed by direct probe that the gates run
BEFORE the log write, so a gated command no longer appears in telemetry at all.

### 4. CTO arch-ruling documented in the shared module header (`af837c1ce`)

CTO's follow-on: recorded the three shared-archive disciplines in `value_parity_reader.py`'s header
(env-gate firm behavior, never firm-specific code here; an edit here must deploy+verify ALL three
firms' behavior; "firm-isolated" = IAM/config, never code). Per-firm archive scoping DEFERRED.
Doc-only, **proven** by AST comparison excluding the module docstring (identical to HEAD).

---

## Findings Raised (all routed; none blocking)

1. **`opal-49f-value-parity` IS NOT DEPLOYED.** Plan `8 to add, 0 to change`; live
   `get-function-configuration` -> `ResourceNotFoundException`. **49F has had ZERO automated
   value-parity detection since ADVI_BREAKS TO-6.** DS~A: this is the missing link explaining why
   49F's portal served a stale ~11%-overstated `certified_aua` for three weeks -- nothing was
   watching. CTO accepted; deploy stays GATED, sequenced (a) freeze-root fix -> (b) sound tie-target
   -> (c) apply, with CTO re-issuing the same-measure arch condition FOR CERT MODE (the 06-30
   condition was grounded on the raw-sum path and does not transfer unexamined).
2. **Shared-archive coupling.** All three firms archive `infra/aws/compdiff/`; any `compdiff/*.py`
   edit silently re-drifts the other firms' deployed code. CTO ruled: keep the shared archive, hold
   three disciplines (now in the module header). Per-firm scoping deferred.
3. **`comp-denytest` UNPLACED in the coverage map** -> `comp-coverage-check` RED at HEAD, printing a
   FAIL banner for every agent on every safe-commit. Pre-existing (fails at `5d21baa6f~1`), not mine.
   COO~B took it as map-owner. Note `18c92b9ac`'s own message says the commit-gate BLOCKED it and it
   was committed anyway -- flagged to CVO as a gate-bypass worth an independent look.
4. **Latent-bug generator (proposal, awaiting GO).** comp-system is the THIRD instance of
   "registered in manifest `tools_index` but `routable=False` in the provider -> unreachable." A
   commit-time gate asserting every `tools_index` tool is routable would have caught comp-fedobs AND
   comp-system before either shipped. The provider's `:88` comment already states the invariant; it
   just is not enforced.

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which-routing-test | `python .tools/comp-which-routing-test.py` | FAIL 37/38 -> **PASS 38/38** | the AC#1 oracle; re-run at post-merge live HEAD, not at my own commit |
| comp-which | `comp-which "the live current-state of the compiled system"` + neighbor guards | PASS | routed to comp-system; comp-freshness/comp-heat/comp-lambdamap intents preserved |
| comp-which | `comp-which --route-only <q>` | PASS | side-effect-free preview; drives HUD req#3d; `xyzzy` -> NO-ROUTE |
| comp_route_eval | `python org/modules/graph/comp_route_eval.py --arm off --role AE` | PASS | canon p@1 64.9->65.8%; diverse/heldout unchanged; struct-gate PASS all tiers |
| comp-grep | `comp-grep "P3-HUD|HUD leg|comp-tool-hud" org` | PASS | located the P3 TO on-rail (first attempt used `\|` -- comp-grep is Python `re`, needs a bare pipe) |
| comp-shell | `comp-shell scan .tools/hooks/comp-tool-hud.sh` | PASS | 0 findings -- Rule 16 (tr/sed/grep/timeout are Git-Bash defaults) |
| comp-coverage-check | (auto, in safe-commit) | **FAIL** | pre-existing: `comp-denytest` UNPLACED. Not mine; routed to COO~B |
| comp-surface-check | (auto, in safe-commit) | PASS | no critical surface touched by any of the 5 commits |
| commit-gate | `.tools/commit-gate.sh <py>` | PASS | on both `.py` edits |
| safe-apply (HALTGT) | `safe-apply.sh apply .build/inf-vp.tfplan` | PASS | 0 added, 1 changed, 0 destroyed |
| deploy_ledger | `open` / `close-leg` x7 / `close` | PASS | CLOSED GREEN 7/7 |

**What worked:** `comp-which-routing-test` is a genuinely load-bearing oracle -- it caught a real
unreachable tool that a diff-read would have missed, and it is what forced me to find the
candidate-set exclusion rather than paper over it with a curated rule. `terraform validate` as an
oracle for a proposed patch (rather than debating the patch) settled two bugs in seconds.

**What failed:** `comp-grep` silently returns 0 matches for `\|`-style BRE alternation (it uses
Python `re`); it does warn, which is good. `comp-shell` needs the `scan` subcommand -- a bare path
errors. Bash-tool `aws` calls with a leading-`/` argument (log-group name, outfile path) are mangled
by MSYS: `filter-log-events --log-group-name /aws/lambda/...` returned an `InvalidParameterException`
that read as "no invocations in 4h" -- I nearly concluded the Lambda had never run. PowerShell was
required (CLAUDE.md already warns; this is the concrete bite). The AWS CLI here is **v1**, so
`--cli-binary-format` does not exist and `--payload` takes raw JSON.

**Gap found:** `comp-tool-hud.log`'s own format defeated the measurement it exists for (fixed, see
above). And no comp-tool answers "does this Python function filter on this field" -- I used native
Grep/Read for `comp_route.py:329`, which is the correct off-rail call.

---

## MCP Traffic

~16 messages. Significant: COO~B liveness probe -> my `(c) WEDGED` answer; COO~B HOLD (overruled my
AUA-first proposal); DS~A pairing thread (full patch + both corrections accepted, joint-RAVC
co-sign waived); CVO oracle-GREEN cert 080106Z; RAVC2s to COO~B on all three legs (all ACCEPTED);
CTO acceptance + arch-ruling on the shared archive + confirmation that the 49f deploy stays GATED.

---

## Blockers

**None.** Two items are external gates, stated plainly: (1) CVO's HUD-measured cert on `c37c6ab27`
(routed, standing by); (2) the `opal-49f-value-parity` deploy is deliberately GATED by CTO behind
freeze-root fix -> tie-target -> cert-mode arch condition. Neither is mine to resolve.

---

## Current State

- **NFRA_TOOLCHECK P3:** AC#1 GREEN (oracle 38/38 at live HEAD, CVO-certed). AC#2 landed +
  measured (`c37c6ab27`). Awaiting CVO's HUD-measured cert -> then CTO's P3 phase-close. The TO
  (`org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_TOOLCHECK.P3.comp-which-selector-and-hud.md`) is
  still `<status>staged</status>` and is exec-owned (owned-paths gate) -- COO~B flips it. Its
  `<issued_to>` names `0.8.0_AE_CloudComp~D`; I executed as base `0.8.0_AE_CloudComp` post-respawn,
  worth reconciling so the TO record matches the commits.
- **inf value-parity:** `opal-inf-value-parity` LIVE with `VP_ANCHOR_DATE_SHIFT=next_trading_day`,
  CodeSha256 `gwq1R5iTBgyyAI602vBBySZLUn4OpFMNz4og7epW13k=`, bundling `_orion_vendor_asof.py`.
  Hourly alarm silent since 08:16:24Z. Ledger
  `org/critical_paths/change_management/20260709T0811Z_inf-value-parity-anchor-date-shift_deploy_completion.md`
  CLOSED. NOTE: `af837c1ce` (doc-only) shifts all three firms' archive hashes, so each shows a
  `source_code_hash` diff on next plan -- zero behavior change, no deploy required.
- **cot-value-parity:** deployed code now behind repo (`0 add, 1 change` = source_code_hash only,
  environment unchanged). Behavior provably identical. Not my lane.
- **49f-value-parity:** NOT DEPLOYED (8 resources unapplied). GATED by CTO. Do not apply.
- **Watcher:** persistent inbox Monitor task `bapp10h41`, armed once at load. Zero crons (LD-0157).

---

## Next Steps

1. **[3.0.0_SA_CVO]** HUD-measured cert on `c37c6ab27` (req#3 a-d exercised + AC#2 = 35.2% of
   measurable Bash nudges gated). Two of my own measurement confounds disclosed in the RAVC -- a
   shared test session-id, and a first log-count that produced a bogus 92.2% figure; the real
   number is 35.2%. Filter my synthetic HUD-HIT probes (08:2x-08:37Z) from any future window.
2. **[2.0.0_SA_COO~B]** flip the P3 TO to complete on CVO's cert; reconcile `<issued_to>` (~D vs
   base). Then CTO P3 phase-close -> NFRA_TOOLCHECK done.
3. **[2.0.0_SA_COO~B]** `comp-denytest` UNPLACED -> `comp-coverage-check` RED at HEAD (fabric-wide
   FAIL banner). Taken as map-owner.
4. **[0.6.0 + 0.4.0_DS_ClientPlatform~A + 1.0.0_SA_CTO]** 49F sequence: freeze-root fix -> sound
   tie-target -> CTO re-issues the same-measure arch condition for CERT MODE -> only then apply
   `opal-49f-value-parity` (own GO + own deploy-ledger). **Held, not forgotten.**
5. **[me, on a GO]** build the `tools_index` -> `routable` commit-time invariant gate (retires the
   comp-fedobs / comp-system unreachable-tool class; third instance).
