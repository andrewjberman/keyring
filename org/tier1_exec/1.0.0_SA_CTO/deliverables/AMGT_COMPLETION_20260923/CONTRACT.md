# AMGT PRODUCT COMPLETION -- CONTRACT v1.0

**`1.0.0_SA_CTO~Z`, 2026-09-23.** `/closer` Step 2 artifact. Andrew's word gates the build phase and he
gave it: *"string up the relevant COOs with clear brief instructions and their goal is to just build to
end to end completion, with iterative enhancement runs after data e2e is proven."*

**THE BRIEF SET IS `4.0.0_SA_CRO~Z`'s, AT A PIN, AND IS NOT RESTATED HERE.**
`org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_COO_SPLIT_PROPOSAL_20260923/{PROPOSAL.md,TRACE_BRIEF_SET.md}`
@`fd51c46d81`. Ten briefs **B00-B09**, their connector walks, their anchors and their closure boundaries
live there. This contract assigns them, names one writer per shared surface, and states the review rule.

---

## 1. THE OUTCOME JOURNEYS

**`FWD-1`, the one live thread, is `B00` and NOTHING COUNTS BEFORE IT:** a real permitted identity logs
in, reaches `/security-analysis/:securityKey` for one real security through `ProtectedRoute(requireDev,
requireAdmin)`, and the intended screen renders with real data. ⛔ **A working `/market` redirect FAILS
this case** -- `ProtectedRoute.tsx:105`/`:115` redirect a missing claim silently, so the tester sees a
working page and never learns the route was never reached.

| lane | seat | briefs | acceptance IDs |
|---|---|---|---|
| **EXPERIENCE** (shared first hop + all mounted UI/client) | `2.0.0_SA_COO~Z` | **B00**, then B01-B06 | **E0**, L1-L4, W1, F1, T1, M1, P1, N1, O1 |
| **SERVED RUNTIME** (shared API / report / generation / consumer contracts) | `2.0.0_SA_COO~Z` | **B07** | R1-R4 |
| **CORPUS** | `2.0.0_SA_COO~X` | **B08** | C1-C3 |
| **HARVST** | `2.0.0_SA_COO~Y` | **B09** | H1-H4 |

⭐ **FOUR LANES, THREE SEATS, AND THAT IS A RULING NOT AN OVERSIGHT.** `4.0.0_SA_CRO~Z` priced every
split by the one countable that matters -- how many times it crosses a shared surface: **by-project/3 =
5 · six-UI+backend/7 = 4 · hybrid/4 = 9 · frame+backend/2 = 18 · corpus-fragment/8 = 13.** Seven seats
buys **one** fewer crossing for **four** more seats, against a verbatim standing three-COO cap.
**Decided at this seat on its own rec, not carded to Andrew**, because `/self-drive`'s routing puts every
open call at the driver by default and the over-reservation defect is the failure mode it warns about.

## 2. OPERATING MODE

- **NO TASK ORDERS for in-scope work.** This contract plus a MANDATE is the whole carrier. No rounds, no
  recuts, no decomp cells. A FAIL is fixed directly and re-pinned.
- **LIVE FIRST.** Offline closures are permitted and **grade nothing** until `B00`/`E0` passes. A thread
  with any fixture-fed hop is not done. `2.0.0_SA_COO~X` and `2.0.0_SA_COO~Y` keep building during
  `B00`; they simply bank no acceptance credit until it lands.
- **FILES OVER MAIL.** `STATUS.md` is a fixed-shape current-state file **overwritten in place**, ~5 KB,
  in each seat's own `deliverables/AMGT_<LANE>/`. Git history is the journal. A message carries exactly
  one of: **interface published · blocker · review handoff.** No ACKs between peers.
- **NO SIDE-QUESTS.** Anything off the thread is one parked line naming the question, its owner and the
  condition that un-parks it.
- **ENHANCEMENT AFTER E2E, per Andrew.** Once `E0` plus one positive product case are independently
  accepted, the matrix expands through the remaining briefs. Each lane's next iteration is **the first
  failing connector in its own named trace**, one pinned candidate at a time.

## 3. ONE WRITER PER SHARED SURFACE

⛔ **A more specific row beats a broader one. A consumer sends a pinned patch; the owner integrates.**

| surface | sole writer |
|---|---|
| `portal/src/pages/SecurityAnalysis/**` (incl. `LeadPanel`, all five tabs) | `2.0.0_SA_COO~Z` |
| `portal/src/api/endpoints/amgt-lead-panel.ts` | `2.0.0_SA_COO~Z` |
| `portal/src/App.tsx` -- **AMGT route rows only** | `2.0.0_SA_COO~Z` |
| `portal/scripts/dev-live.mjs` · `portal/vite.config.ts` -- **AMGT entries only** | `2.0.0_SA_COO~Z` |
| `lib/research/api/scoped_amgt.py` and the `opal-amgt-scoped-api` package | `2.0.0_SA_COO~Z` |
| `lib/research/identity/**` (crosswalk, coverage_pass) | `2.0.0_SA_COO~Z` (Served Runtime) |
| `lib/research/corpus/**` | `2.0.0_SA_COO~X` |
| `lib/research/coverage/pool_reader.py` | `2.0.0_SA_COO~Y` |
| `lib/research/metrics/{chatter_axis,generation_writer}.py` | `2.0.0_SA_COO~Y` |
| `lib/opal_data_harvest/**` · `lib/research/harvest/**` | `2.0.0_SA_COO~Y` |
| `docs/` + `org/missions/D5/AMGT/*/prd/**` | `1.0.0_SA_CTO~Z` |

⚠ **DEPARTURE FROM `/closer` STEP 2, STATED RATHER THAN HIDDEN.** That step says the CTO lands each row
as an `.owned-paths.yaml` lane granting only the named seat, in this same commit. **It is NOT done here,
and the reason is measured:** `2.0.0_SA_COO~X` and `2.0.0_SA_COO~Z` have **zero** explicit rows in that
file while the base `2.0.0_SA_COO` has **114**, so the lanes inherit the base grant -- which is why all
three seats are committing successfully today. **Writing lane-only rows would NARROW three live seats
mid-drive and could refuse them at their next commit.** The table above is the authority by reading; the
grant file is left additive and untouched. **A seat refused at a path this table gives it reports the
refusal as a blocker and the grant is added same-turn.** `3.0.0_SA_CVO~Z` may overturn this departure.

**DEPARTURE UPHELD, NOT OVERTURNED** (`3.0.0_SA_CVO~Z`, msg 25069, ruling @`60dde3b252`) -- and it was
upheld on BETTER evidence than this seat had. That seat DROVE `.tools/owned-paths-validate.py`
(`resolve_lane` + `check_agent`) at HEAD against this table's own paths, with `OWNED_PATHS_MODE`
defaulting to **block, not warn**, and found the mechanism this seat had only inferred: the four Python
surfaces resolve to lane `BASE_EXEC` and permit `~X`, `~Y` and `~Z` alike, and **`resolve_lane` is
LONGEST-MATCH-WINS, so a narrow row OVERRIDES `BASE_EXEC` rather than adding to it** -- it would refuse
the other two lanes AND the base, hard.

⛔ **AND THE MEASURED STATE IS WORSE THAN THE DEPARTURE IMPLIED: ACROSS ALL TEN SURFACES IN THIS TABLE,
ONE-WRITER-PER-SURFACE IS MECHANICALLY UNENFORCED -- four by OVER-PERMISSION, six by the ABSENCE OF ANY
HOOK.** The six `portal/` rows resolve to `POD_DE_ANY`, but `portal` is a gitlink at mode `160000` whose
toplevel carries no `.owned-paths.yaml`, `core.hooksPath` is unset at system, global, local and
submodule scope, and `portal/.git/hooks` holds only `.sample` files -- **so no hook evaluates a commit
made inside `portal` at all.** The departure did not create that, and landing the rows would not close
it: it would move four surfaces to over-restrictive while the six stayed identical. **That is the
strongest argument for upholding it.**

⭐ **`2.0.0_SA_COO~Z` IS NOT BLOCKED, and that seat corrected its own first reading to say so** -- it
initially read the `POD_DE_ANY` `False` as a live hard blocker in front of `B00`/`E0`, then measured that
no hook grades a `portal` commit, so the `False` is a number its own invocation produced rather than a
state any commit meets. The parent-side gitlink bump stages `portal` with no trailing slash, resolving
to lane `ANY`.

⛔ **RESIDUAL 1 -- THE LIVE EXPOSURE IS FALSE-PERMIT, AND THIS DEPARTURE'S OWN FALLBACK DOES NOT COVER
IT.** The fallback above handles a false-REFUSE (a seat blocked at a path this table grants it). The real
hazard is the opposite: **two lanes writing one shared surface, with no refusal ever emitted and no
signal at all.** Discriminator, one command per surface at each drain:
`git log --format='%an' <since>..HEAD -- <surface>`, requiring **exactly one distinct author**. COST: one
command per surface in this table. NON-APPLICATION: a surface with no commits in the window. **Named by
`3.0.0_SA_CVO~Z` and not built by it, correctly -- that seat does not fix what it grades.**

⛔ **RESIDUAL 2 -- DO NOT INSTALL THE PARENT HOOK INTO THE SUBMODULE. IT IS A LANDMINE IN THE OBVIOUS WAY
TO "FINISH" STEP 2.** `owned-paths-check.sh:137-143` **exits 1 when `.owned-paths.yaml` is absent in
block mode**, so installing the parent hook into `portal` would hard-fail EVERY portal commit --
**converting an absent control into a total outage on the lane that owns `B00`/`E0`.** Landing rows in
the parent file is separately inert for `portal`.

**SO `/closer` STEP 2 IS ONLY PARTIALLY DISCHARGEABLE ON THIS ESTATE, AND THIS CONTRACT RECORDS IT
RATHER THAN LEAVING THE ROWS READING AS GOVERNED: THE SIX `portal/` ROWS IN THE TABLE ABOVE BIND BY
READING ONLY.** No mechanism enforces them. ⚠ Hook installation is per-clone, so none of this speaks for
the laptop fabric; the denominator is the ten paths this table names, not all of `.owned-paths.yaml`.

## 4. THE SHARED CONTRACTS, WHICH DOUBLE AS ACCEPTANCE IDS

`2.0.0_SA_COO~Z` owns ONE interface sheet (`INTERFACES.md`, current schema only, superseded text to
`INTERFACES_HISTORY.md`) covering: identity/scope · pool · generation admission and publication · I4
consumption · report revision · API DTOs. **One accepted and one refused example per contract.**
Producer output and frontend input are printed **side by side with field names**; no consumer invents a
key or a permission context.

⛔ **THE FIELD-LEVEL RULE, and it exists because the laptop run was burned by exactly this:** a request
contract is reconciled by printing BOTH field lists and naming the intersection. In IRPT the composer
emitted seven fields and the handler read eight, and *"the intersection is only `variant`"* -- so a
`QUEUED` answer proved transport and proved nothing about the request surviving. **Transport reachability
is never acceptance.**

**THE 16 ROUTES ARE PART OF "ALL FUNCTIONS" AND THIS SEAT RULES THEIR TREATMENT.** The server declares
16 routes; 9 distinct mounted request functions back the UI; `printPackPath` is a **path helper, not a
server function**; print is a **header action, not a tab**; `getCoverageSet` has **no mounted caller**.
**RULED:** the five auxiliary routes (`/freshness`, `/lists`, `/ledger`, `/versions`, `/compare`) and the
unmounted coverage request are **acceptance rows in `B07`'s matrix, reachability-and-shape only** -- they
are neither silently dropped from "all functions" nor promoted into UI seats. An unmounted export is
recorded as unmounted; it is not counted as a working function and is not deleted on this contract's word.

## 5. BREAKING CHANGE, AND REVIEW

- **Breaking change:** one exchange between the peers, then `1.0.0_SA_CTO~Z` rules. **Silence is not
  agreement.**
- **Review:** `3.0.0_SA_CVO~Z` grades each **pinned candidate** PASS / FAIL / NOT_EVALUATED in its own
  evidence folder, on a live trace, the deployed bytes, or a test run. ⛔ *"Offline success cannot be
  called deployed E2E PASS."* An ungraded boundary stands at NOT_EVALUATED and is **never an implied
  pass** -- no lane waits on that seat's silence or reads consent into it. **The CVO never fixes what it
  grades.** `1.0.0_SA_CTO~Z` integrates and rules ties; no single lane closes the product.

## 6. WHAT THIS CONTRACT DOES NOT LIFT

Commits via `safe-commit.sh`; code in isolated worktrees (Rule 14b), except an append-only shared channel
file, which is committed in the shared tree; **the never-widen pair on any served-output write**; vendor
egress only on Andrew's per-use word (**the America Movil induction request stays READY and MUST NOT
execute**, and its own CVO ruling is that it must REFUSE rather than pick a transposed ticker); the
monitor/alert moratorium; production promotion and deploy gates; shared-branch pushes by
`0.0.0_AB_MSTR~Z`. **No new gate is created here.**

**Two blockers sit outside every seat's reach and are Andrew's:** the session sentence that lets
`2.0.0_SA_COO~Z` take up closer work and sign its never-widen half, and an identity holding both
`user.role==='admin'` and `claims.userType==='Dev'`. **`B00` cannot pass without the second.**
