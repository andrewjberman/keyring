# ADVI_PERFRP — STEP-1 BRIEF for the MERGE-FORWARD

**Author:** `4.0.0_SA_CRO~A` · **UTC:** 2026-09-01
**Commissioned by:** `1.0.0_SA_CTO`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CRO_BRIEF_COMMISSION_ADVI_PERFRP_MERGE_FORWARD_20260901.md`
**Authority:** Andrew-direct 2026-09-01 at the CTO terminal — *"i am ok with doing it the official way... we do this properly."*
**Consumer:** STEP 2, `/endpoint --forward`, built 2026-09-01 @`3e2244fee1`.
**Scope addition, Andrew-direct to this seat 2026-09-01 (this session, verbatim):** *"make sure the
engineering that it sits on is in a canonical pattern. We are doing it right now solely for 49
Financial but we really are going to need to do this for all partners."* — Part IV and Part V exist
because of that sentence and are not in the CTO commission.

---

## 0. HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

The commission §2 requires this brief be authored **blind to the in-flight task-order set**, so the
endpoint does not silently ratify what is already open. Andrew independently instructed this seat
mid-session: *"Actually do not look at TOs."* The two agree, so there was no conflict to resolve.

**NOT READ:** any `org/**/task_orders/ADVI_PERFRP.*`; the project JSON's `phase` / `blocking` fields.

**READ, and permitted by §2:** the PRD's purpose + acceptance sections, the ratified rulings, the
served plane measured live, and the agent session logs 2026-08-25 → 2026-09-01.

⛔ **WHERE IT BENT, STATED RATHER THAN HIDDEN.** Andrew asked for current status wide and deep. The
session logs *are* branch material — they describe what is in flight. **Resolution: Parts I–III are
authored from PURPOSE and SERVED REALITY only, and `/endpoint --forward` must cut its outcomes from
those parts alone. Part VI is the status scoping Andrew asked for and is explicitly NOT
outcome-bearing.** A `SOURCE:` line pointing into Part VI is a defect in the forward pass, not a
traceable outcome.

---

# PART I — THE OUTCOME TERRITORY

Written as what an advisor can DO that they cannot do today. Each is qualitative and disputable: it
names who, what, and the alternative it displaces. No numbers are invented anywhere in this part.

### O1 — An advisor sees their own book's performance without opening Black Diamond
An advisor opens their Book in Advisor Intelligence, picks a period, and reads what their book is
worth, what it earned, what came in and went out, and how many relationships they gained or lost.
Today that answer exists only in the Black Diamond Advisor dashboard, which is a separate product
with separate credentials.
**Disputable by:** an advisor who still opens Black Diamond to answer a book-level question.

### O2 — An advisor answers "how did this household do, and why" in one place
An advisor opens one client relationship and reads the four figure families together: what it holds,
what it is worth and what moved (activity), what it returned (performance), and what it gained or
lost against cost (gain/loss). "Why" is served by the decomposition being visible — the return sits
beside the flows and the allocation that produced it, not on four unrelated screens.
**Disputable by:** an advisor who has to leave the relationship view, or reconcile two products, to
explain a client's quarter.

### O3 — The advisor moves between grains without losing their place
An advisor drills from the relationship to a single account, and back, keeping the same period and
the same figure vocabulary. The account view is the same cards, not a different report.
**Disputable by:** a grain switch that resets the period, renames a column, or opens a new route.

### O4 — An advisor can always tell a real figure from an absent one
Every figure the report shows is computed. Everything it cannot compute is either absent by design
or named on its own face with the reason. A held-away account, a position-only account, an account
not held the entire period, and a deferred column are four different absences and read as four
different things.
**Disputable by:** any blank cell, any zero standing in for an unknown, any empty card with no
explanation — and by an advisor who quotes a number to a client that the system should have refused
to show.
⭐ *This is the outcome most likely to be dropped as "polish". It is the one that decides whether an
advisor trusts the product enough to use it in front of a client.*

### O5 — The advisor can take the figure out of the system
An advisor exports a table for a client conversation or a spreadsheet, rather than retyping it.
**Disputable by:** an advisor who screenshots or retypes.

### O6 — A since-inception figure tells the truth about the 2024 seam
When an advisor asks for since-inception, they get a figure that is honest about where our history
starts and where it is stitched from legacy Black Diamond history — labelled, never silently blended.
**Disputable by:** an SI figure a reader cannot tell the provenance of.

### O7 — Insurance is visible beside the performance figures, never inside them
An advisor sees the client's insurance business in the same view without it contaminating a single
asset-management figure.
**Disputable by:** any AM figure that changes when insurance data lands.

### O8 — A 49F leader reads the book rollup and it ties
The advisor Book view's tiles and client table are the same figures as the relationship views,
joined — not a second computation that can disagree.
**Disputable by:** a tile that disagrees with the sum of the rows beneath it.

### O9 — An advisor who checks against Black Diamond finds nothing they cannot have explained
Black Diamond is the parity oracle, never a dependency. Where our figure differs, the difference is
known, explained, and on the record before an advisor finds it.
**Disputable by:** an advisor discovering a discrepancy the fabric had not already characterised.
⛔ *Andrew's 2026-08-31 record states parity "as I understand has already been proven." Measured
against `ADVI_BDPARITY`, it has not — a five-account probe is complete; the population census has
not run and known calculation differences remain open. That correction was surfaced by
`1.0.0_SA_CTO` and is restated here because this outcome depends on it.*

### O10 — It is simply there each morning
The report is produced on the canonical schedule with one producer per served key. Nobody runs
anything by hand for an advisor to have today's view.
**Disputable by:** any ad-hoc run standing in for a scheduled one, and by a day the view is silently
stale.
⛔ *The failure mode this outcome must defeat is not a crash. It is a run that produces nothing and
reports success — see Part IV, finding C.*

### O11 — The second partner is a binding, not a build
The work stands up for 49 Financial in a form where Inflection and Cottonwood are parameter
bindings of one runner, one publisher key family, one interface — so the second partner costs a
configuration and a gate, not a second implementation.
**Disputable by:** any partner-named branch in code, any second copy of the projection logic, any
per-partner frontend structure outside the ratified Tier A / Tier B split.

---

# PART II — WHERE THE BOUNDARY SITS

What PERFRP **owns**: the per-client projection contract over the ratified facts; the served leaf
family set; the Books L2/L3/L4 and Book-view interface; the schedule and publisher wiring for its
own keys; its own parity harness activation.

What PERFRP **relies on and does not own**:

| project | PERFRP relies on | PERFRP does NOT own |
|---|---|---|
| `ADVI_STITCH` | the labelled pre-2024 tier, and `dim_account_xref` as the existence source for known-not-held accounts | the migration classification itself, or the stitched history build |
| `ADVI_INSURE` | the insurance rows rendering beside the figures | insurance ingestion, its gold shape, or its own surfaces |
| `ADVI_BDPARITY` | the parity verdict that discharges O9 | the parity method, the census, or the calculation-difference resolution |
| `ADVI_ROSTERCOLS` | — | (relationship currently UNRESOLVED; see Part VI note 4) |
| `ADVI_COTKEY` | Cottonwood's advisor keying, before any COT binding | the keying investigation itself |
| `D10` pipeline consolidation | the eventual canonical per-partner bucket homes | the consolidation |

**Deliberately NOT this project** (ruled, not re-litigated here): the performance METHOD; benchmarks,
MWR and asset-level contribution; target allocations; projected income; fixed income; wallet share;
statement PDFs and Run Report; the Advisor and Distribution tabs; the frontend UI/UX design project
Andrew has said follows this one; the switch-flip mechanics.

---

# PART III — THE QUALITATIVE BAR

Per Andrew, verbatim in the commission: *"This does not have to be a deliverable contract. It can be
qualitative because we will not know enough about the quantitative mechanics at this point."*

**No number in this brief is a target.** Every figure that appears anywhere in it is a measurement
with a source and a timestamp, and appears only in Part VI. If a later stage finds a number in
Parts I–III, that is an error in this document and not a ratified quantity.

The bar each outcome must pass is **disputability** — a person can point at the running product and
say "no, that isn't true." Each outcome above carries its own *Disputable by* line for exactly that.

---

# PART IV — THE ENGINEERING SUBSTRATE: IS IT IN A CANONICAL PATTERN?

Andrew asked this directly. The answer is **partly, and the deviation is load-bearing.**

The governing standard is the **RATIFIED** `MDPF_ADVI_UNIFIED_CANONICAL_PATTERN_SPEC_20260811.md`
(Andrew-direct 2026-08-11, *"im cool with your recs"*), as amended 2026-08-18 to put the ADVI product
gold home in the per-client bucket.

### FINDING A — PERFRP has NO persisted gold projection tier, and the pattern requires one

MEASURED at source and on the live plane, this session:

```
perfrp_emit_core.py:40-41   GOLD = "opal-data-49financial"   GOLD_ROOT = "gold/advi"
perfrp_emit_core.py:113     reads {GOLD_ROOT}/canonical/{table}/date={D}/data.parquet
perfrp_emit_core.py:23-25   "THIS EMITS LOCALLY. It writes the file the port asks for and
                             touches no S3 key. ... this module has no S3 write path at all."
main():2073-2095            writes --out, a LOCAL Path, as json.dumps(...)
```
`@7f5b0c7cc8` (2026-09-01, `0.4.0_DS_ClientPlatform~G`) — the vintage is stated because this file
was rewritten 19,742 → 118,465 bytes inside the last 24 hours.

Live plane: `s3://opal-data-49financial/gold/advi/` holds `_logs/ canonical/ dimensions/ insurance/
reference/`. A recursive listing for `perfrp` returns **zero objects**. There is no PERFRP gold table.

The ratified pattern states the opposite shape, verbatim: *"The gold runner's FINAL OUTPUT IS PARQUET
— JSON leaves the gold tier entirely"* and *"Every platinum publisher READS PARQUET, never JSON — the
publisher is the estate's ONLY JSON producer, minting serving-shape JSON exactly once at the platinum
boundary; the one-producer-per-served-key law becomes enforceable BY CONSTRUCTION."*

>> **PERFRP INVERTS THAT.** The serving-shape JSON is minted by eleven emitter scripts inside the gold
runner; the publisher copies bytes it did not mint. So one-producer-per-served-key is not enforceable
by construction here — it is a convention held across eleven wrappers. <<

**Three consequences, and they are why this is not merely a conformance note:**

1. **The projection is unobservable after the fact.** Its only artifact is a local file on an
   ephemeral EC2 runner that self-halts. When the chain produced nothing on 2026-09-01, the decisive
   manifest was on the `/tmp` of a stopped host, and reading it required authorising an instance
   start that risked destroying it. A gold tier would have made that a query.
2. **Partner binding is against eleven scripts, not a table.** O11 asks that a second partner be a
   binding. Binding a table is a parameter; binding an eleven-script emit layer plus a publisher is
   closer to a port.
3. **Parity has nothing persisted to compare.** O9 wants a figure-for-figure comparison across days.
   There is no stored object holding what we said yesterday.

⚠ **Stated as a finding for adjudication, not as a ruling.** This seat is recon→specs and dispatches
nothing. The remedy shape — whether PERFRP lands a gold projection table, or whether the pattern
carries a named exception for projection-class products — is a CTO architecture call. Both are
defensible; what is not defensible is the current state being *undeclared*, because a future partner
binding will be designed against a pattern the reference implementation does not follow.

### FINDING B — the emitter core is one implementation, and that half IS canonical
Eleven thin wrappers over one shared core (`perfrp_emit_core.py`), with an explicit never-blend guard
that fails closed. That is the correct shape and should be preserved through any remedy to Finding A.

### FINDING C — a stage that produces nothing reports success
`chain_49f_entrypoint.py` maps any non-zero emitter rc to `emitter_refused`, and `emitter_refused` is
excluded from `hard_fail`. **Eleven by-design refusals and a total failure of all eleven produce
byte-identical stage output (`STAGE OK rc=0 hard_fail=0`).** There is no floor on `built`.
This is why a four-day repeat of one as-of, and then a total production stop, were both invisible
from any single run. **O10 cannot be discharged while this is true** — "it is simply there each
morning" is unfalsifiable against a stage that cannot report its own absence.

### FINDING D — refusal reasons are written and never surfaced
Three carriers hold a refusal's reason (`reason`, `emitter_tail`, `error`) and no consumer reads all
three; the chain log renders a bare dash because it reads stdout while tracebacks go to stderr. At
least two seats ruled an absence off one field of one carrier and withdrew it. The observability gap
the commission flags is real and measured.

---

# PART V — ALL PARTNERS: WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Andrew: *"We don't have to scope doing it for every partner just yet but that is the ultimate
intention."* This part therefore names **constraints on the 49F build**, not a partner programme.

The governing law is already ratified — D2 PRD §11, the **ADVI PARTNER UNIFORMITY LAW**
(Andrew-direct 2026-08-24): Tier A = 49 Financial (full surface, leaderboard); Tier B = Inflection =
Cottonwood, one structure and the same view exactly, with insurance as an option keyed on the partner
fact "has an insurance book". A new ADVI function is built on 49F and bound to Tier B as parameter
bindings — never a per-partner implementation.

**What the 49F build must therefore not do, if O11 is to hold:**

1. **No partner name in code.** The firm is a required argument with no default (the
   `master_for()` refuse-on-unknown pattern, already ruled in PRD §12). Options key on a registry
   partner fact.
2. **One invocation per firm, never one spanning firms.** Cross-firm read is NEVER#2. Each
   invocation reads only its own firm's trees and writes only its own firm's keys.
3. **The projection contract must be expressible as a table, not only as a rendering.** This is
   Finding A restated as a partner constraint: whatever binds a second partner should be the
   thing 49F produces, and today 49F produces an ephemeral local file.
4. **No per-partner frontend structure.** Tier B partners get Inflection's view exactly.

**Named boundary, Andrew-direct this session:** the per-partner bucket homes today are
`opal-data-inf` and `opal-data-cot` (measured live; `opal-data-inflection` /
`opal-data-cottonwood` do not exist). **The canonical per-partner bucket naming is a component of
D10, the pipeline consolidation** — his words. PERFRP must not pre-empt D10's naming, and D10 should
know PERFRP is a consumer of whatever it lands.

**Sequencing constraint that already exists:** Cottonwood's PERFRP binding sequences AFTER
`ADVI_COTKEY`. A book keyed wrong yields a per-client report keyed wrong.

---

# PART VI — STATUS SCOPING (NOT OUTCOME-BEARING)

⛔ **`/endpoint --forward` MUST NOT cut capability outcomes from this part.** It is the wide-and-deep
scoping Andrew asked for, and it is branch material by construction. Every figure carries its source.

### 1. What is actually served today — measured live this session, `s3api` (UTC)

`s3://opal-data-portal-v2/platinum/advi/49financial/` — **19 keys, 4 of them PERFRP:**

| leaf | size | last modified (UTC) |
|---|---|---|
| `perfrp_book_advisor.json` | 15,000,091 | 2026-09-01T07:27:05Z |
| `perfrp_gainloss_account.json` | 11,896,644 | 2026-09-01T03:17:03Z |
| `perfrp_gainloss_relationship.json` | 7,419,826 | 2026-09-01T03:16:43Z |
| `perfrp_performance_account.json` | 1,923,593 | 2026-09-01T03:16:07Z |

Of **eleven declared families** (`perfrp_emitters.py`), 4 are served. Three the frontend requires are
not (`performance_relationship`, `allocation_account`, `allocation_relationship`); `transactions_relationship`
is a ruled sovereign deferral; `roster_relationship` has an unmet precondition.
⛔ **The L3 Performance card — the grain on Andrew's original screenshot — is among the unserved.**

`latest.json` currently points at a manifest written to a **double-slash key**
(`_manifests//4b36d4f5743c.json`), derived from an empty `asof`.

### 2. The live production regression — OPEN, uncaused

The daily chain's `perfrp_projection` stage built 6 of 11 families each day 08-27 → 08-31 and **0 of
11 on 2026-09-01**. Seven-plus hypotheses were raised and killed across five seats: the fix, the
invocation, a disabled schedule, staging flags, an empty `asof`, a Python-version delta, stale bytes,
an IAM denial (a **false deny** — a conditioned grant simulated without context), and "no new data".
`2.0.0_SA_COO` ruled no new causal story until someone measures what the chain run actually did.

**Two things are established and should not be re-derived:** (a) 08-29/30/31 all re-processed
`asof=2026-08-28` (correct trading-calendar behaviour — Friday is Monday's answer), so the
before/after comparison had no valid *before*; (b) the discontinuity is nonetheless real — today's
partition holds ~6% more data than the last-good one and fourteen other stages consumed it and wrote
output, while only the eleven emitters produced nothing.

The narrowing that survives: `perfrp_emit_core.py` went 19,742 → 114,406 → 118,465 bytes across the
last-good/first-fail boundary. The cause sits inside the new logic, not in what it imports.

### 3. Two stale carriers that will mislead a reader

- ⛔ **`docs/architecture/ADVI_PERFRP_PRD.md` header still reads: *"DISTRIBUTION RESTRICTION (Andrew
  ~16:1xZ): nothing on this subject to `4.0.0_SA_CRO`."*** That is this seat. It is superseded by the
  2026-09-01 CTO commission and by Andrew's direct instruction this session — but the text is live in
  the PRD and a future seat will read it and route around the CRO. **Surfaced, not adjudicated, not
  edited by this seat.**
- `advi_49f_publisher.tf:58-59` asserts *"Zero PERFRP leaves served is the correct state"* as a
  current-state fact. Four leaves are served. Already found by `1.0.0_SA_CTO`; noted because the
  stale carrier is the **restrictive** one, so a reader trusting it may "remediate" authorised output.

### 4. Open at Andrew (not this seat's to answer)

- The two-limb PERFRP publish question reserved by `1.0.0_SA_CTO` at 91668: (a) did the 08-25 08:5xZ
  line narrow the 04:0xZ ratification, or answer the branch/PROD question only; (b) is the attached
  condition **per-family or per-set** — where per-set is unsatisfiable by construction, because it
  is gated on a family that is a ruled deferral and will never emit.
- `ADVI_ROSTERCOLS` is a D2 member with an empty `prds` field and is not named in the parent D2 PRD;
  its relationship to PERFRP is unresolved and routed to CTO.

### 5. Prior art worth not re-buying

`ADVI_PERFORMANCE` (the ratified per-account performance facts and field contract) is reused as an
artifact — PRD §3, reuse-not-brief. The PRD's §13 premise correction is load-bearing and already
paid for: the planned `fact_account_return_daily` (~50 columns) **does not exist**; the projection
consumes the live canonical tables (`canonical_valuation`, `flow_ledger`, `nna_canonical`,
`twr_daily` — 8 tables measured live this session) and declares absent columns rather than filling
them.

---

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. **It does not claim the endpoint has changed.** The CTO expected this brief to conclude the
   endpoint is unchanged and the failure was in decomposition. **Parts I–III support that read**: the
   purpose in the PRD still looks right, and the outcomes above are a restatement of it in
   capability terms, not a replacement. **Part IV is the exception** — the substrate question Andrew
   added is genuinely not in the current endpoint, and O10/O11 are not fully derivable from the
   2026-08-24 PRD.
2. **It does not adjudicate the publish question.** Reserved to Andrew, cited in Part VI note 4.
3. **It does not solve or summarise the open producer question.** Out of scope per commission §5;
   Part VI states its status only so the merge-forward is not designed against a stale picture.
4. **It does not read the in-flight task orders**, so it cannot and does not say which are KEEP /
   AMEND / RETIRE / ENDPOINT-INCOMPLETE. That is step 4 and it is COO's.
5. ⛔ **The ENDPOINT-INCOMPLETE bucket is the guard on this document.** A task order that serves
   something real which Parts I–III fail to name is evidence **this brief is incomplete** — not
   evidence the task order is waste. The author of an endpoint is the party who benefits from a
   smaller one, and that author is this seat.

**Push state:** stated in the commit report, measured, never defaulted.
