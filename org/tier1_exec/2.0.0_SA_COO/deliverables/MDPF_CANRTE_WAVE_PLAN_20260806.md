# MDPF_CANRTE — Phases 0–6 wave plan and current state

**Author:** `2.0.0_SA_COO~Z` (site Z) · 2026-08-06 · **LIVE DOCUMENT — this is the program's single
current source of truth.** Twenty-odd rulings landed in the four hours after decomposition began and the
state is otherwise scattered across MCP traffic.

**Source pack:** `projects/MDPF_PROPVALIDATION/` (5 docs, CVO-authored read-only review)
**Decomposed off:** `1.0.0_SA_CTO~Z`'s corrected classification @70733b907 — **NOT** doc 04 §6's raw list.
**Canonical home:** `MDPF_CANRTE` (MSTR~Z approved). `MDPF_GLOBAL.json`'s own `blocking` field rules that
T1 route-canon and T5 legacy-decommission *"execute AS PART OF CANRTE"*; W-1a is mid-cutover inside this
scope with L7/L8/L9 held, so a fresh project code would fork the ledger from the rows Phase 6 must close.

> ⛔ **NO GATE ANYWHERE IN THIS PROGRAM.** Not one row below is an approval step, co-sign, hold, or review
> choke point. `3.0.0_SA_CVO~Z` is a VERIFICATION seat — its findings are findings, never a hold anyone
> clears, and no TO makes its sign-off a precondition. Pre-existing mechanical rails (safe-commit,
> safe-apply, safe-deploy, owned-paths, commit-gate) stand untouched. Two items attach to irreversible
> physical acts and both are pre-existing law, not new gates.

---

## 1. Lanes

| Lane | Owns | Basis |
|---|---|---|
| `0.4.0_DS_ClientPlatform~Z` | gold computation modules, end-to-end incl. QA-deploy | Rule 13 |
| `0.7.0_AE_CloudOps~Z` | Lambda package/layer, Terraform, IAM, schedules, clock probes, build+deploy, retirement | Rule 13 |
| `1.0.0_SA_CTO~Z` | architecture + rulings | MSTR~Z framing |
| `3.0.0_SA_CVO~Z` | verification of ABSENCE claims | seat, not gate |
| `2.0.0_SA_COO~Z` | decomposition, drive, cross-domain coordination, ledger | this doc |

---

## 2. Wave 1 — Phase 0. ALL DISPATCHED.

| TO | Lane | State |
|---|---|---|
| `P0-1` evidence freeze + rollback baseline + schema baseline | AE~Z | **COMPLETE** @db5f37b11 |
| `P0-2` H1 Inflection early-clock probe | AE~Z | pending · window 08:05–08:40 ET |
| `P0-3` H2 SmartX early-clock probe | AE~Z | pending · re-targeted, see §4 |
| `P0-4` H3 source census over the CAPTURED closure | DS~Z | criteria 5/6/9 closed |
| `P0-5` H3 deployed-plane census + H8 | AE~Z | in flight, interim delivered |
| `P0-6` H10 external-reader bounded negative | CVO~Z | **COMPLETE** @49e236bff + 2 self-corrections |
| `P0-7` EC2 capture before terminate | AE~Z | snapshot done; enumeration at the 09:00 ET production window |

TO commits: `ebaf5700a` `f50291f06` `7c7c549f7` `253e6c893` `5b4411c1e` `3c1ba6c11` `4eb24256a`
`a2357b421` `ac4723068`.

---

## 3. Wave 2–5 — NOT YET AUTHORED

| TO | Lane | Gating fact |
|---|---|---|
| `P1-1` gold spine **+ Cottonwood producer family — ONE ATOMIC UNIT** | DS~Z | port scope is the P0-7 capture's output |
| `P1-2` `mdpf-gold-lambda` package | AE~Z | module list from the closure |
| `P1-3` gold-run manifest | joint | — |
| `P2-1` deployable config + IAM | AE~Z | ready — see §5 |
| `P3-1` publisher correction + H8 | AE~Z | **ordered after P2-1**, see §5 |
| `P4-1` Terraform route cutover | AE~Z | probe branches must be resolved first |
| `P5-1` build + deploy order · `P5-2` un-targeted zero-diff | AE~Z · CVO~Z | — |
| `P6-0` port-completeness discharge · `P6-1` retirement+teardown · `P6-2` negative route evidence · `P6-3` ledger | AE~Z · AE~Z · CVO~Z · COO~Z | — |

⛔ **P1-1 ATOMICITY (CTO~Z ruled).** `build_cottonwood_mdpf_pair.py:64` imports **`_distribution_stats`** —
a PRIVATE symbol — from `dim_mdpf_account_distribution`, across trees, via a `sys.path` hop. A P1-1
refactor of that module **breaks Cottonwood with no signal in the mdpf tree**: a leading underscore
declares that nobody outside depends on it, so nothing warns the refactorer that someone does.
**P1-1 AND THE COTTONWOOD PRODUCERS MOVE IN ONE WAVE.** Naming the shared resource is necessary;
**the sequencing is the actual control.** Internal order: backfill → slice → spine.

⛔ **TEARDOWN IS NOT ONE STEP, AND IT IS ALSO NOT THREE.** CVO~Z measured `DeleteOnTermination=TRUE` on
the sole volume — **terminate and EBS-delete are ONE API call**, so the sovereign condition has exactly
one enforcement point, not a stop→detach→delete ladder. Sequence: capture (P0-7) → discharge (P6-0) →
terminate (P6-1).

---

## 4. Rulings that changed the plan after it was drafted

**Andrew-direct @c801ec9d5** — *"Teardown is fine just need to make sure any necessary code on that ec2 is
properly ported to the lambda."* H4's authority half CLOSED. Its condition became ordering-critical: **the
act he authorized destroys the evidence that discharges its own condition.** The capture moved from Phase 6
to Phase 0 (MSTR~Z approved) because it is read-only and **its output is a Phase 1 input — at Phase 0 the
enumeration SCOPES the port; at Phase 6 it merely audits one already built and cut over.**

**Calendar binding (CTO~Z).** Bind `lib/trading_calendar` via the WS-1 layer; retire the shim and both
inlined privates. Four conditions; the tie-out is EXERCISED with a mutant (discharged: n=1096 in-window
dates, 0 disagreements, falsifier fired, **2027 shows 10 disagreements — every 2027 NYSE holiday reads as a
trading day**). The `<5` pin ports WITH its full rationale — it survives the shim's retirement because
`lib` uses the same try/except shape and a 5.x TypeError is uncaught there too.

**Resource-TYPE rule (CTO~Z, re-ruled).** Not per-vendor. EventBridge **Scheduler** entries carry
`ScheduleExpressionTimezone` and can be ET-anchored; **classic rules have no timezone field and are
structurally UTC-only.** 6/6 correlation. *"SmartX moves, Orion does not"* was a true generalization with a
false member because it generalized on the wrong axis. **Write P4-1 to check the type, not the name.**
General case: every classic rule in the estate carrying an ET wall-clock contract drifts an hour
seasonally **by construction**.

**H11 floor: 08:05 ET (12:05Z), not 08:15.** 35-minute EDT window. Clock v3 Amendment 1 **records 12:15Z
while the plane runs 12:05Z** — the governing clock document is wrong about the single member it exists to
pin. **Cite the plane, never the ruling doc.** A pre-floor probe result is not weak evidence, it is NOT
EVIDENCE: below the floor a PASS is yesterday's token inside its 10h TTL and a FAILURE is a credential
artifact.

**H12: the probe-fail branch already exists.** Clock v3 rules it — shifts land on probe PASS; vendor
lateness is labeled carry, **never a held publish**. A negative probe is a COMPLETE probe.

**Doc 03's H2 remedy targets the wrong schedules.** `smartx-assets-daily-pull` carries the OnSuccess
destination; `smartx-rest-pull` has **zero** event-invoke-configs. Executed literally the remedy moves the
JWT and rest-pull, leaves the 09:30 producer, silver lands ~09:40 as before — **and reports as delivered.**

> ### ⛔ THE GOVERNING ACCEPTANCE CRITERION (CTO~Z, standing across every clock TO)
> **ACCEPTANCE ASSERTS ON THE OUTCOME, NEVER ON THE INTERVENTION.**
> The criterion is *"canonical vendor silver OBJECT exists by 08:40 ET."*
> It is **NOT** *"the schedules were moved to 07:45/08:00."*
> *"Did the schedules move?"* is precisely the check that passes while the remedy fails. **An outcome
> assertion is immune to targeting the wrong resource, because a wrong target does not produce the
> outcome.** Same shape as the `calendar_source()` ruling: assert the thing, not the act supposed to cause it.

---

## 5. Ordering constraints that are CORRECTNESS, not preference

**DEPLOY BEFORE ENV** (DS~Z, measured on W-1a). Env-first would have made the emitter read copied history,
log a valid key, report 11 cohorts and read GREEN while the live partition landed elsewhere unwatched.
**THE ROLLBACK MITIGATION IS WHAT WOULD HAVE MADE THE FAILURE SILENT.** Same shape at Phase 4's 09:00
repoint: **an empty new-gold prefix fails LOUD, a pre-populated one does not** — so do not pre-populate to
"de-risk"; that converts a loud failure into a silent one and is also a shadow.

**P2-1 BEFORE P3-1.** Measured live at 21:13Z: there is **no `config/` top-level prefix in
`opal-data-assets` at all** (positive-controlled). P2-1 CREATES a prefix, it does not populate one. And the
deployed publisher's complete env carries **no roster variables** — the roster-completeness feature IS NOT
DEPLOYED, so the 404 breaks nothing today *because the deployed publisher never reads it*, and **a blind
rebuild from repo tip is what would introduce the read.**

**A THIRD ROSTER EXISTS, DEPLOYED, AND IT IS *THE* PRODUCTION ROSTER FOR THE ENTIRE GOLD SPINE.**
`s3://opal-data-mdpf/code/scripts/gold/partner_roster.json`. Phase 2 says *"do not create a hand-maintained
second roster"* — **one already exists and production reads it.**

> ⚠ **CORRECTED 2026-08-06 ~2122Z — MY FIRST READING WAS FALSIFIED, AND THE CORRECTION IS LARGER THAN THE
> ORIGINAL FINDING.** This section previously said the copy's only known reader was `mdpf-accrual-trigger`
> and would therefore "die with its only reader" when Phase 4 retires the accrual bridge. **THAT IS WRONG.**
> I asked AE~Z to verify rather than confirm; they falsified it.
> **THE MECHANISM IS A SHELL `s3 sync`, INVISIBLE TO ANY LAMBDA ENV SWEEP.** `mdpf-daily-dispatch.sh:125`
> runs `aws s3 sync s3://opal-data-mdpf/code/scripts/ $SCRIPTS_DIR/ --delete`, and the roster lives INSIDE
> that synced prefix — so every production run copies it onto the box next to the gold modules.
> `dim_mdpf_aggregate_aua_timeseries.py:1718-1731` `_load_partner_roster()` — its own docstring calls it
> **"THE ONE SOURCE OF EXPECTED-NESS"** — resolves `os.path.join(here, "partner_roster.json")` FIRST, where
> `here` is the module's own (synced) directory. **CANDIDATE 1 WINS AND IT IS THE S3 COPY**; the repo path
> is explicitly the dev/QA fallback, reached only off-runner.
> Readers: the 2587-line spine at `:1203` (`gate_policy.per_partner_max_lag_trading_days`) and `:1897`,
> `dim_mdpf_account_distribution.py:62,387`, `build_cottonwood_mdpf_slice.py:871-874`,
> `build_portal_gold_accrual.py:51,110,114`. **That is the gold path itself, not a peripheral trigger.**
> The env var was the copy's most VISIBLE reader, not its most important one.

⛔ **ORDERING CONSEQUENCE FOR P2-1 / P4-1:** the third copy dies when the **EC2/dispatch route** dies, which
is a DIFFERENT event on a different schedule from the accrual-bridge retirement. **`mdpf-gold-lambda` must
have its roster BEFORE the sync stops**, or the spine loses THE ONE SOURCE OF EXPECTED-NESS mid-cutover.

✅ **AND IT HELPS THE ZIP LAYOUT:** candidate 1 is `os.path.join(here, "partner_roster.json")`, so in a flat
zip `here` is `/var/task/` and **flat-vendoring the roster at zip root satisfies the existing resolver with
no code change.** Candidate 2 resolves to garbage but is never reached. *Opposite outcome to
`build_dim_model_portfolio.py:66`'s rsplit hack from the same family of construct — which is exactly why
each `sys.path`/relative-resolution site must be checked individually rather than dispositioned as a class.*

The copy diverged by sha256 from the repo authority and **the divergence is NOT operative**: 227 leaves each
side, exactly one differing leaf, a PROSE provenance string narrating an unchanged value.
**But the near-miss is sharper than first reported.** `:1203` reads `gate_policy.per_partner_max_lag_trading_days`
FROM THAT EXACT FILE — the very key whose provenance went nine days stale against a 2026-08-03 CTO ruling
with nothing detecting it. **Had the ruling changed the VALUE rather than the narration, EVERY PRODUCTION
GOLD RUN SINCE 07-28 WOULD HAVE USED THE STALE LAG, silently.** That is Phase 2's
Terraform-managed-config-with-hashes argument *measured*, and the resolver **PREFERS the hand-uploaded copy
over the committed authority by design.**

---

## 6. Standing constraints register (Class D — these never close; re-assert at every phase boundary)

- **H6** served schema is DO-NOT-TOUCH. Measured: **seven** as-of families across 23 sampled objects, not
  the two H6 describes. `global/aggregate-aua-timeseries.json` carries `count_as_of` and its **twelve
  siblings do not** — a uniform build path drops a field from the single most visible served key, and any
  spot-check sampling a firm key would have passed. `as_of_date`, *the field the brief names as the
  platinum convention*, appears in **2 of 23** — aligning to the documented convention would rename the
  as-of field on 21 served objects.
- **H7** re-pin at EVERY phase boundary. On this device read the ref, not the tree
  (`MSYS_NO_PATHCONV=1 git show origin/CLOUD:<path>`), and never `2>/dev/null` it.
- **H9** code retention is legal; ACTIVE-PATH retention is a no-shadow violation.
- **H11/H12** as above.
- **H13 OPEN** — S3 deletion remains on CLAUDE.md's human-confirmation list. Pre-existing law, attaches
  only to the delete step, holds no phase.

---

## 6a. ⛔ THE COMPOSITION RULE — three NOT-OBSERVABLE results do not make an observed absence

**This governs P6-3's closure statement and every retirement claim in the program.**

Three independent surfaces have now returned "no reader" on the five deletion candidates:

| Surface | Seat | Verdict | Its named blindness |
|---|---|---|---|
| source-visible census | DS~Z | no source-visible reader | blind to unregistered/external readers by construction |
| CloudTrail / access telemetry | CVO~Z | **NOT-OBSERVABLE** | data events may never have been enabled; absence cannot be created retroactively |
| deployed **configuration** (env sweep, denominator 196, explicitly paginated) | AE~Z | **NOT-OBSERVABLE** | sees a reader ONLY if the prefix appears in CONFIG; blind to code-constructed keys |

> **THREE NOT-OBSERVABLE RESULTS DO NOT COMPOSE INTO AN OBSERVED ABSENCE. THEY COMPOSE INTO A BOUNDED
> NEGATIVE WITH THREE NAMED LIMITS.** Agreement between instruments that share a blind spot is not
> corroboration — it is the same silence heard three times.

**AE~Z DEMONSTRATED THEIR OWN INSTRUMENT BLIND RATHER THAN ASSERTING THE CAVEAT**, using the sharpest
available case: `opal-portal-data-proxy` — comp-estate's documented `/v1/*` portal API reading
`s3://opal-data-portal-v2/*` — has **`ENVIRONMENT VARIABLES: []`. EMPTY.** It names neither the bucket nor
any prefix; it constructs every key in code. **So the env sweep cannot see the live portal API reading the
very bucket that holds all five deletion candidates.** Nine other functions carry only the bucket name and
can construct any key inside it at runtime.

That is the anti-correlation shape once more: **the instrument returns its cleanest possible result
precisely on the reader that matters most.** A zero here observes the SURFACE, not the estate.

⚠ **STAKES: CVO~Z's amendment places 5 of the 8 candidates — the four OWNTS objects and the bare
`aggregate_aua_timeseries` — in `opal-data-portal-v2`, THE LIVE SERVED BUCKET.** Deleting a
live-served-bucket object on three bounded negatives is **H13, and H13 is Andrew's**. Nothing in any of the
three halves moves it toward "safe to delete."

**The discriminating instrument for the residual is deployed Lambda CODE, not configuration** — reading the
packages of the nine bucket-carriers plus `opal-portal-data-proxy`. That is materially larger than P0-5
scopes, and AE~Z flagged it rather than silently expanding into it. **The gap's shape is now named; whether
to close it is a scoping decision, not a discovery.**

*Rows 6–8 (`wsb`, `wsd`, `mdpf/feeds`) left the deletion set on DS~Z's SOURCE-VISIBLE evidence — `wsb` is
read by `mdpf_aggregate_aua.py:239-268` and is required to calculate a PORT row. A zero from a blind
surface cannot re-open a row a sighted surface already closed in the safe direction.*

---

## 7. Instruments that lied today — all caught by controls, none by care

| Instrument | The lie | Discriminating fix |
|---|---|---|
| `comp-blast` edge count | 0 consumers for an artifact with **4** | literal-key grep + `comp-pipescript consumers`, denominator printed |
| `aws s3 ls` LastModified | prints LOCAL time; s3api returns UTC | cite the s3api ISO-8601 value **with its `+00:00`** |
| `--query 'length(...)'` | returns the PAGE count | count the materialised list |
| `--no-paginate` | returns **only page 1** — 196 Lambdas → 50 | omit the flag; let the CLI auto-paginate, count client-side |
| `<gate> \| tail` | reports **tail's** rc, not the gate's | re-run unpiped for the real rc |
| import-health on PMC | passes with the package MISSING (try/except) | assert `calendar_source() == "NYSE/pandas_market_calendars"` |
| `comp-grep` canonical-import census | matched the shim's **docstring**, reading as "no divergence" | run the import positive control |
| `comp-estate` census | lists `mdpf-freshness-checker` as a live producer; the function does not exist | live `get-function` |

**Every one failed as a CLEAN, PLAUSIBLE RESULT** — the same shape as a mangled grep and a `2>/dev/null`'d
`git show`. ⚠ **CLAUDE.md:110's own remedy clause names `--no-paginate` as the fix**; the load-bearing half
is *"+ explicit token walking"*, and an agent who stops at the first clause implements the bug the rule
exists to prevent. Routed to MSTR~Z by CTO~Z as a defect in the law's remedy clause.

**FIVE PACK PRESCRIPTIONS WERE THEMSELVES THE DEFECT** — the import-health check that cannot fail in the
state it detects; an equality test that passes for the wrong reason once its dependency installs; a
comparison rule instructing the operator to strip its own discriminating field; a schema convention present
on 2 of 23 objects; and **a remedy that moves the wrong schedules and then passes the check asking whether
it was applied.** Where a criterion is copied from the pack, ask once: **could this have failed?**

---

## 8. Open at Andrew

**Vendor per-use authorization** — read-only calls to Orion Assets, Eclipse portfolios (08:05–08:40 ET) and
SmartX assets pull (~08:00 ET) on 2026-08-07, solely to establish whether MDPF-required rows return valid
early-hour data. Surfaced via MSTR~Z. **My original ask named Orion/Eclipse only; SmartX was omitted and
the correction is surfaced.** No workaround exists — running the existing pull suite early is the same wire.
**Fallback pre-approved:** bound H1/H2 on S3-side evidence and record the residual as an OPEN OBLIGATION,
never upgraded to a proof. A worse outcome, not a blocked one.
