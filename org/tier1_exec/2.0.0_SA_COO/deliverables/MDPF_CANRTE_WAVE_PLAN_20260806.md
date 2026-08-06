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
| `P6-0` port-completeness discharge · `P6-1` retirement+teardown · `P6-2` negative route evidence · `P6-3` ledger | AE~Z · AE~Z · CVO~Z · COO~Z | see §3a |

### 3a. P6-0 NEEDS A SECOND AXIS — A NECESSARY THING THAT IS NOT CODE

CVO~Z's framing, relayed by AE~Z: **"THE RATIONALE IS A NECESSARY THING THAT IS NOT CODE. Andrew's
condition is not discharged by porting the file if THE REASON dies with the box."**

**P6-0's three buckets are MECE on a FILE axis** — byte-identical to a committed source / ported and
hash-tied / demonstrated unnecessary. **A COMMENT INSIDE A FILE THAT IS ITSELF SCHEDULED FOR DELETION
PASSES BUCKET (a) CLEANLY AND STILL VANISHES.** The buckets are sound; this sits off their axis.

⛔ **RESOLUTION: THIS IS NOT A FOURTH BUCKET. IT IS A SEPARATE CRITERION ON A DIFFERENT AXIS.**
CTO~Z made "no fourth bucket" *arithmetically checkable* via `|b1 ∪ b2 ∪ b3| == denominator`, where the
forbidden fourth bucket is "files nobody found." **Adding a rationale bucket would break that arithmetic
and disarm the control.** The file axis stays three-and-MECE; rationale gets its own row.

**THE CRITERION:** before `infra/aws/ec2/mdpf-daily-runner/` is deleted, **any RATIONALE it uniquely
carries is PORTED to where the constrained thing now lives — not merely confirmed present in git history.**

**TIMING, measured and better than first thought:** the `<5` pin rationale is at
`mdpf-daily-dispatch.sh:175-182`, **TRACKED IN THE REPO** (last commit `e366e889c`, positive control on an
invented sibling returns empty), repo == deployed byte-for-byte, and `comp-grep` over 21,250 of 22,982
files finds it nowhere else. **So it SURVIVES EC2 teardown completely and dies at PHASE 6**, when route
retirement deletes that directory. A deletion guard on a directory we control — a far better position than
a guard on an instance we are destroying. **Not a P0-7 capture item and not at risk tomorrow.**

⚠ **"IT IS IN GIT HISTORY" IS NOT A REMEDY. GIT HISTORY IS NOT WHERE SOMEONE DOING DEPENDENCY HYGIENE
LOOKS — THEY LOOK AT THE PIN.** The failure shape is Rule 22a's least-privilege-cleanup class arriving
through a dependency pin: a future engineer finds `<5` on a python3.11 function, **correctly** observes
that 3.11 has no PEP-604 problem, removes it, **and silently changes the trading calendar** — on NEVER#1.

*And the pin itself is a DECISION, not a discharge: CVO~Z withdrew their original escalation once they
grounded that the pin protects IMPORTABILITY on 3.9 rather than correctness — but were careful that
"the reason dissolves" is NOT "5.x is safe." **Nobody has ever tested 5.x's calendar BEHAVIOUR against
this code, because on 3.9 they could not import it to try.** So retention on 3.11 requires a calendar
tie-out whichever way it goes.*

**GENERALISES PAST THE PIN:** that directory is 688 lines of dispatch script carrying a lot of accumulated
*why*, and the pin comment is simply the instance found because someone went looking at source.

⚠ **NEW P1 DESIGN INPUT — PENDING ANDREW'S WORD, BUT P1-1 MUST NOT BAKE THE CURRENT SHAPE FORWARD
SILENTLY.** Grounded by content read (MSTR~Z, ~2137Z): the unscoped `aggregate_aua/{date}.json` carries
**MULTIPLE PARTNERS IN ONE DOCUMENT** (49financial + inflection present, cottonwood absent).

> **A SINGLE MULTI-PARTNER FILE CANNOT BE CHANNEL-INDEPENDENT.** One writer writes every partner, so a
> partner failure either blocks the whole file or **silently drops that partner out — WHICH IS THE GLOBAL
> CLAMP MECHANISM.** Per-scope pathing (`{scope}/aggregate_aua/{date}.json` or equivalent at gold) makes
> channel independence **physically enforceable** rather than a property the builder must remember to honour.

This is MDPF_CHANNEL_INDEPENDENCE's contract meeting its own storage layout. The re-path-with-the-port
question is **with Andrew**; until he rules, P1-1 designs against the requirement and **flags the shape
rather than reproducing it unexamined.**

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
- **A RULING IS NOT LANDED UNTIL THE DEPLOYED OBJECT CARRIES IT** (CTO~Z, standing — stated by them
  because it was their own 08-03 ruling that nearly got lost). **Ruling in the repo does not change
  production.** Corollaries, both measured here: **"the repo says X" is NEVER evidence about what
  production used** — the committed roster is `_load_partner_roster()`'s *candidate 2*, the dev/QA
  fallback reached only off-runner; and **nothing detects the divergence**, because a resolver that
  silently prefers candidate 1 emits no signal when the two disagree. The run-manifest config hash is
  precisely the detection that was absent for nine days.
- **TWO INDEPENDENT ORDERINGS LIVE INSIDE PHASE 4/6 AND A NAIVE "RETIRE THE EC2" STEP VIOLATES BOTH:**
  (i) capture → discharge → terminate (§2A″, evidence destroyed by the act it discharges);
  (ii) `mdpf-gold-lambda` has its roster **before the sync stops** (the copy dies with the dispatch
  route, a different event from the accrual-bridge retirement). **Sequence them explicitly.**

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

> ### ✅ THE RULE WAS VALIDATED WITHIN THE HOUR, AND BY THE EXPENSIVE CASE
> Andrew worked the deletion question directly with MSTR~Z (2026-08-06 ~2137Z). **`s3://opal-data-mdpf/mdpf/feeds/*`
> IS NOT DELETABLE.** Traced live: `wsb-49f-model-aua-daily` WRITES it (today 09:33),
> `opal-smartx-ingestion-pipeline` (3 modules, deployed, in the source map) READS it, and the output is the
> served `{scope}/account-distribution.json` (today 09:50). **`wsb`/`wsd` are PRODUCERS OF A SERVED SURFACE,
> not dead schedules.**
> MSTR~Z's verdict on our own censuses, and it is the sentence to keep: **"The census NOT-OBSERVABLE verdict
> was technically right and PRACTICALLY WRONG."** Three surfaces returned no reader for a prefix that a
> live producer writes and a deployed pipeline reads into a served artifact. **Had NOT-OBSERVABLE been
> allowed to compose into "safe to delete," this program would have deleted a live producer of a served
> surface.** The rule above is what stood between those two outcomes.
>
> **AND THE CONVERSE — WHAT AFFIRMATIVE EVIDENCE ACTUALLY LOOKS LIKE.** The portal read-path is now
> CONFIRMED SCOPED for all four scopes on **three independent oracles that converge rather than three
> silences that agree**: MECHANISM (the DEPLOYED `opal-portal-data-proxy` package, pulled via
> `get-function` — not repo source — constructs ZERO mdpf keys, positive-controlled against its 73 real S3
> refs; sole MDPF route is CF `/api/general/mdpf/*` → `platinum/mdpf/*`); CONTENT SHAPE (the Global 07-30
> clamp requires cottonwood in `cohort_provenance`; the scoped global file has it, **the root bare file
> never mentions cottonwood** — the on-screen clamp is uncomputable from the root object); and BEHAVIOR
> (firm scopes display 08-03, root lineage ends 07-31 with no per-firm objects).
> **That closes "does the PORTAL read these" outright.** It does not close the unregistered-external-reader
> residual — nothing can — and the distinction is exactly the one §6a exists to hold.

### H13 — PARTIALLY ANSWERED BY ANDREW, 2026-08-06 ~2137Z

His grammar point: the root-grain objects **"is trash"**, the unscoped `mdpf/` root path **"doesnt even
really make sense"**; scoped folders are the correct grammar.

| Candidate | Verdict | Sequencing |
|---|---|---|
| 4 OWNTS objects | **TRASH** | zero consumers confirmed |
| root bare `aggregate_aua_timeseries.json` | **TRASH** | sole consumer is `mdpf-freshness-checker`, itself retiring — **checker first, then object** |
| 3 scoped UNDERSCORE twins | **TRASH** | already-ruled retired pair (cottonwood never had one) |
| `platinum/mdpf/aggregate_aua/` (439 dated) | not portal-read; the `PLATINUM_AGG_PREFIX` name is DEAD CONFIG | ✅ **ARCHIVED — see below** |
| `s3://opal-data-mdpf/mdpf/feeds/*` | ⛔ **NOT DELETABLE — LIVE PRODUCER** | leaves the deletion set entirely |
| `opal-data-mdpf` overall | `code/` + `feeds/` + `telemetry/` LIVE until the port lands | `cache/` (05-19) + `bmkaud-evidence/` (06-01) dead weight |

### ✅ EXECUTED 2026-08-06 ~2144Z — THE ROOT-GRAIN SET IS ARCHIVED, NOT PENDING

**Andrew-direct, VERBATIM:** *"yeah just get it the fuck out of the root there, it can go to
opal-data-portal-v2/platinum/mdpf/archive or something"* — executed same session by MSTR~Z personally,
record **@4a2651063**.

**444 objects → `platinum/mdpf/archive/`**: the bare `aggregate_aua_timeseries.json`,
`etf_ownership_timeseries/` (4), and `aggregate_aua/` (439). **444/444 denominator-verified, 0 leftovers.**
Root is now exactly `{49financial, inflection, cottonwood, global, archive}`. Served hyphen surface
untouched at today's vintage. **An ARCHIVE-MOVE, not a deletion — reversible and versioned.**

Pre-move grounding: portal proven scoped-only; `mdpf-daily-trigger`'s **DEPLOYED** env already re-points
`PLATINUM_AGG_PREFIX` to `gold/mdpf_revamp/_aggregate_aua` (**the code default naming platinum is DEAD
CONFIG**); and `mdpf-freshness-checker` DOES NOT EXIST as a deployed function.
⚠ **That last one is a ninth instrument entry: the bare object's "one consumer" WAS A PHANTOM THE WHOLE
TIME** — the retirement sequencing built around "checker first, then object" was ordering against a
function that had already ceased to exist.

⛔ **CONSEQUENCES THAT MAKE PENDING TO LANGUAGE STALE — this table was written 20 minutes before the move:**
1. **H13 for the root-grain set is DISCHARGED BY EXECUTION.** Remove those rows from any pending
   Andrew-ask. What REMAINS of H13: `opal-data-mdpf` `cache/` + `bmkaud-evidence/` (his word needed only
   if we want actual *deletion* rather than leaving them), and **the scoped UNDERSCORE twins, which stay on
   the F7 CTO-GO path — they sit inside scope folders and were DELIBERATELY NOT in this move. DO NOT LET
   ANYONE WIDEN HIS ROOT INSTRUCTION TO COVER THEM.**
2. **P4/P5: any step referencing `platinum/mdpf/aggregate_aua/` as a LIVE path is now stale.** The dated
   partitions live under `archive/` and **the real contract is `gold/mdpf_revamp/_aggregate_aua`** — already
   the trigger's deployed env. **DS~Z's port spec treats the platinum dated prefix as GONE, not as a
   contract to preserve.**
3. **PHASE-4 ACCEPTANCE ROW:** a successful pre-port EC2 chain run may RE-MINT one
   `aggregate_aua/{date}.json` at the old root (Stage 6 writes by its own constant; the chain is currently
   wedged at Stage 5). **If Phase 4's cutover acceptance sweeps the root and finds it clean, THAT IS THE
   CHECK** — a re-minted file found there is one re-archive command, not an incident.
4. **The per-scope re-path question is OBE FOR PLATINUM** — the dated partitions are out of the serving
   tier entirely. **The multi-partner-single-document question now lives ONLY at the GOLD contract**, which
   is DS~Z's port design surface.

⚠ **PHANTOM, so nobody cites it:** `platinum/mdpf/account-distribution.json` (top-level) **DOES NOT EXIST**
— versions=0, positive control on the 49financial scoped key returns 18 versions. `comp-clobber` over the
served prefix: 465 keys, **ZERO active clobber** — the duality is producer-duality over time, not
interleaved-writer clobber.

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

### 7a. THE NINTH — AND IT IS MINE, IN A REMEDY I WAS ROUTING

I relayed to CTO~Z that `lambda-source-map.json` carries *"51 non-ASCII bytes, all U+00A7 section signs"*
and characterised it as a **CI-blocking** defect. **I took that on report and did not measure it.** CTO~Z
did, before routing:

- The **51** is right; the composition is not. ~6 are section signs, 1 em dash — and **~14 are MOJIBAKE**
  from a UTF-8-read-as-cp1252 round trip (`â€š` / `â‚¬` / `Ã¢`), **plus two C1 CONTROL CHARACTERS** sitting
  inside JSON strings.
- **THE CRASH IS NOT WHERE I SAID.** The failure is `can't decode byte 0x9d at position 30154` — the
  control character. **`§` encodes as `0xC2 0xA7` and cp1252 decodes both bytes happily; it would never
  crash.** So a section-sign cleanup leaves the mojibake, leaves the control characters, **and leaves the
  crash — while looking done and passing an ASCII-count check that went 51 → 45.**
- **"CI-blocking" is UNVERIFIED and I overstated it.** Tracked tooling is already belted with explicit
  `utf-8` (`deploy_ledger.py:226`, `check-lambda-layer-deps:284`, `backfill-lambda-iam-mapping.py:169`).
  What broke on this box was an **ad-hoc `json.load(open(p))`, not a tracked tool.** Only
  `.github/workflows/lambda-deploy.yml:70` lacks an explicit encoding, and ubuntu-latest defaults to UTF-8.

**This is the sixth instance of the day's shape and the first that was about to be routed AS A REMEDY.**
The lesson is not about encodings: **I passed on a diagnosis without grounding it, to the seat whose job is
to act on it.** AE~Z had re-derived CTO~Z's 12:05Z correction from the primitive rather than accept it on
report; I did not extend the same discipline to a finding I was forwarding.
**Disposition:** AE~Z's P5 edit uses explicit `utf-8` and adds no non-ASCII (binding regardless); we do NOT
absorb the cleanup; it routes to CTO base **with the corrected diagnosis**, because a section-sign cleanup
would close the ticket without fixing the file.

### 7b. THE TOOL FINDINGS ARE NOT RANDOM — THEY CLUSTER ON RETIREMENT

CTO~Z's read of the three: `comp-blast`'s false zero matters **when deleting**; `comp-estate`'s phantom
matters **when establishing what is still there**; `comp-which`'s gap is literally *"inventory an EC2
before you kill it."*

> **THE COMP-TOOL ESTATE IS WELL COVERED FOR BUILDING AND THINLY COVERED FOR RETIRING — because the estate
> grew by building.** This program is the first large RETIREMENT, so it is hitting the thin side
> systematically rather than by bad luck.

And the two failure modes are **opposite in risk**: a false ZERO under-reports CONSUMPTION → risk is
**deleting something needed**; a PHANTOM over-reports EXISTENCE → risk is **working on something that is
not there**.
**Consequence to state plainly in the ledger: THE EC2 INVENTORY WILL BE DONE BY HAND** — and a hand-built
denominator is exactly what §2A″'s condition exists to protect. **We do NOT build tooling inside this
program** (one-time act; absorbing tool-building is the widening we keep refusing). The
retirement-coverage pattern routes to CTO base as an estate-level observation.
*Cross-check in our favour: doc 02 already records the freshness-checker as "already absent" — so here the
PACK is right and the CENSUS is wrong, the reverse of the day's pattern.*

**FIVE PACK PRESCRIPTIONS WERE THEMSELVES THE DEFECT** — the import-health check that cannot fail in the
state it detects; an equality test that passes for the wrong reason once its dependency installs; a
comparison rule instructing the operator to strip its own discriminating field; a schema convention present
on 2 of 23 objects; and **a remedy that moves the wrong schedules and then passes the check asking whether
it was applied.** Where a criterion is copied from the pack, ask once: **could this have failed?**

---

## 7c. HELD ON A RULING THAT MUST ARRIVE — P1-1 and P2-1 both

**Doc 03 Phase 2 prescribes a mechanism a CTO ruling forbids by name in the code.**
*(Grounding: DS~Z measured this at 213220Z. Not independently re-derived by COO~Z — forwarded with its
provenance per §7a's lesson.)*

`dim_mdpf_aggregate_aua_timeseries.py:1718-1747` `_load_partner_roster()` docstring — *"ONE committed
authority in two locations of the same file — **NEVER an S3-read fallback** and NEVER a vendored copy …
FAIL-CLOSED when absent … (CTO ruling 230319Z: a private copy of a roster value is the sect-III-e defect
verbatim)."* Its SystemExit message ends **"Do NOT add another resolution mechanism here."**
Phase 2 says: manage the roster in S3 and *"give mdpf-gold-lambda exact GetObject access to those keys."*

Ruling requested, narrowed to two: **(a)** build-generated hash-tied copy at zip root via the existing
resolver, **no S3 GetObject leg granted**; or **(b)** S3 read via a new leg, which requires amending
230319Z. DS~Z and COO~Z both recommend **(a)** — Phase 2's own second half sanctions a build-generated
hash-tied copy, and at flat zip root `here` = `/var/task`, so **candidate 1 hits it and the existing
mechanism works unchanged, no code edit.**

⚠ **SILENCE DOES NOT PICK NOTHING — SILENCE PICKS (b)**, because P1-1 must implement something and the plan
text says S3. **This is the class where an unstated default becomes the third copy** (the calendar is three
copies today because nobody stated the binding, and every copy was added by someone with a defensible local
reading). **P2-1 is held with it:** under (a) the roster GetObject leg is never written and Phase 2's config
work covers `route_bindings.yaml` only — materially different IAM.

### ✅ AND THE ESTATE IS NOT UNIFORMLY FAIL-GREEN — PRESERVE THIS ONE

After eight fail-green instruments in one day it would be easy to treat fail-green as the estate's nature.
**This resolver is FAIL-CLOSED**: it raises `SystemExit` naming both candidates and refuses the build. It
cannot silently degrade, unlike `pandas_market_calendars` and `partner_held_etf`.

> **P1-1 PRESERVES THE FAIL-CLOSED PROPERTY AND DOES NOT "IMPROVE" IT INTO A GRACEFUL FALLBACK.**
> **Because adding a fallback is exactly the kind of change that reads as an IMPROVEMENT in review** — a
> reviewer softening `SystemExit` to a warning would believe they were hardening the pipeline. Explicit
> `do_not` in the TO, not a remembered property: **a preserved property living only in an agent's memory is
> one refactor from gone, and P1-1 is a refactor of this exact module.** (DS~Z asked for it in this form.)

---

## 8. Open at Andrew

**Vendor per-use authorization** — read-only calls to Orion Assets, Eclipse portfolios (08:05–08:40 ET) and
SmartX assets pull (~08:00 ET) on 2026-08-07, solely to establish whether MDPF-required rows return valid
early-hour data. Surfaced via MSTR~Z. **My original ask named Orion/Eclipse only; SmartX was omitted and
the correction is surfaced.** No workaround exists — running the existing pull suite early is the same wire.
**Fallback pre-approved:** bound H1/H2 on S3-side evidence and record the residual as an OPEN OBLIGATION,
never upgraded to a proof. A worse outcome, not a blocked one.
