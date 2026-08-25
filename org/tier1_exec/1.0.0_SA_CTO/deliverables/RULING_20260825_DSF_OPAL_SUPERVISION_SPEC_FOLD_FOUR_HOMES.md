# RULING -- WHERE DS~F's OPAL-SUPERVISION SPEC FOLDS IN: FOUR HOMES, AND THE INGEST HALF ALREADY HAS AN OWNER

**Ruled by:** `1.0.0_SA_CTO` on Andrew's ask 2026-08-25 ~06:0xZ (*"See this spec from DS~F, we need to
figure out where to fold this in"*). **Subject:** `org/tier2_senior/0.4.0_DS_ClientPlatform~F/deliverables/SPEC_COT_OPAL_SUPERVISION_PREDICATE_20260825.md` @`23ff21e750`.
**Archetype:** COORDINATE. **Push state:** landed LOCAL, rides MSTR integration. **Distribution:** not CRO.

## THE TEST I APPLIED, AND IT IS THE ONE I SET ON COT_CANON458

*A Rule 24(iv) failure ACROSS a registration boundary is the boundary telling you where the work goes.*
Name the state axis, then ask whether ONE remedy moves every piece together. **It does not -- the spec is
four pieces with four different remedies, and folding it into one home would bury three of them.**

## THE FOLD

| piece of the spec | HOME | why this home and not another |
|---|---|---|
| **GAP A** -- the `opal_closure` scope, the coverage assert, derive-daily (s.2, s.8, A1/A2'/A3/A4'/S1-S3) | **`WSE_COTMDL`**, re-scoped and entered at Rule 27 stage 2 | **SOURCE-CONFIRMED OWNERSHIP:** `infra/aws/terraform/opal-assets/cot_rebalancer_runner.tf` tags the producer `Project = "WSE_COTMDL"`, and that registration is **ACTIVE** (deliberately not closed 2026-08-05). **AND 30-of-64 IS THE ANSWER TO ITS OWN SINGLE OPEN QUESTION** -- its `blocking` field reads verbatim: *"5 serving models vs the WS-E discovery's '17 strict-Opal / 14 assigned' ... this is probably correct-and-complete, but it is UNVERIFIED and must be confirmed before any close."* It is now verified, and it is NOT complete. |
| **the PREDICATE + the labels** (s.4, S1/S2) | **`D1_CATVIEWS`** | D1 s.8.6 already carries this as open item (i): *"whether `advisory_scope=advised` equals fee-taking on every firm's data, or a fee predicate replaces it (the COT_SUPERVISED live filter is rung-2 prior art)."* **The Cottonwood predicate IS that answer for one firm.** The two display labels are values on D1's ruled Client L1 axis. |
| **GAP B** -- the stopped `fact_holdings` producer (s.3) | **`ADVI_COTETL`** -- UNCHANGED | already ruled; carried as a declared cross-project dependency on `COT-e-1`'s face. Nothing to fold; it needs only SEQUENCING, which the spec's s.5 states correctly. |
| **s.7's measured facts + the STOP** | **`COT_CANON458` / `COT-e-1`** -- already absorbed @`73fbb92e50` | no action. |

## THE SENTENCE THAT DRAWS THE BOUNDARY, AND COO WROTE IT

`COT-e-1` says: **"the 458,053,742.19 TOTAL is on the COTTONWOOD basis and does NOT depend on the Opal
predicate. WHAT DOES NOT: every Opal-basis figure beneath it."**
**That is the boundary.** COT_CANON458 owns THE TOTAL. The Opal predicate governs THE BREAKDOWN BENEATH IT.
So GAP A and the predicate are not COT_CANON458 work, however completely they block `COT-e-1` -- **a
blocking dependency is not a scope claim**, and that distinction is the whole reason GAP B went to
`ADVI_COTETL` three hours ago rather than being absorbed.

## WHY I DID NOT MINT A NEW PROJECT (Build Ladder rung 2, applied to registrations)

My first read was that GAP A was homeless and needed a registration. **It is not homeless; I had not looked
before reaching for the mint.** The TF tag resolves the owner in one read. Two near-misses worth naming:

- **`MDPF_3FIRMS` carries a STAGED TO literally named "cot rebalancer liveness"** -- adjacent, and WRONG.
  **Liveness is answered GREEN** (the pull fired 02:00:4x on 08-24 and produced 30 files) **while the defect
  sits inside the answer.** A liveness question cannot see a scope question. Folding here would have filed a
  live blocker into a 13-TO untriaged heap, under a TO whose own verdict is already green -- and my own
  2026-08-05 note on that project says *"DO NOT decompose the staged set as written without that triage."*
- **`MDPF_COTMDL` is CLOSED-as-superseded** and points at WS-E -- so a reader chasing "Cottonwood models"
  through the project registry lands on a closed row and stops one hop short of the live owner.

## WHAT I AM AUTHORIZING, AND WHAT IT DOES NOT CLOSE

**`MODEL_DETAIL_SCOPE = "all"` IS AUTHORIZED** (`cot_rebalancer_runner.tf:154`): an already-implemented,
tested branch; one env var; NOT a served change, so NEVER#3 does not attach. Rides `safe-apply` + a
deploy-completion ledger entry (NEVER#6). **Rule 26: the apply runs on the device that owns the work.**

**SEATING: COO seats it, and NOT on `0.7.0_AE_CloudOps~G`** -- that instance holds ADVI_PERFRP and is
mid-BLOCKING on the perfrp grain defect; a second project at that seat is exactly what the 08-24
one-project rule forbids.

**Two pre-apply reads, neither blocking:** does 30 -> 64 change the pull's runtime / rate-limit profile, and
does anything downstream currently benefit from the narrow set (both COO's, both fair).

**TIME-COST OF DELAY, stated so the flip is not treated as leisurely:** the pull is per-date. **Every day
unflipped is a partition permanently carrying 30 of 64 models** unless separately backfilled.

- **IT CLOSES NOTHING.** It fixes FORWARD ONLY. Whether the 08-21 canonical date is computable without a
  backfill is OPEN and is COO's stated pre-close question. **The STOP stands.**
- **DISARMED != REMEDIATED:** the hazard is already DISARMED by the STOP (nothing emits). The flip is the
  first REMEDIATION step, not the disarm -- and the durable half (a coverage assert that REFUSES on
  shortfall, the printed denominator, derive-daily) rides `WSE_COTMDL`, not the apply.

## TWO FINDINGS THIS RULING TURNED UP

1. **CELL-ID SLIP, and it mis-routes to the wrong project.** `2.0.0_SA_COO` 69020 and 68971 both say the
   circularity was folded into **`COT-c-1`**. **MEASURED at `73fbb92e50` (HEAD of that file): the
   `MODEL_DETAIL_SCOPE` / `opal_closure` text appears in exactly ONE cell, and it is `COT-e-1`.** `COT-c-1`
   is PATH A's holdings producer -- **`ADVI_COTETL`'s cross-project cell**. So a seat routing the env-var
   act off the message lands on the wrong producer AND the wrong owner. The content landed correctly; only
   the citation is wrong. *(Same seat corrected a stale-hash citation 18 minutes earlier -- this is that
   class one field over: the cell ID is the field a router reads and the one least likely to be re-derived.)*
2. **HIS NEW LABELS SUPERSEDE D1's RULED ENUM, AND D1 DOES NOT KNOW IT.** D1 s.8.6 carries his 08-24 enum
   `Client Supervised` / `Client Unsupervised` at lines 293 and 304. **`Client - Opal Supervised` occurs
   ZERO times in that PRD** (measured). His 08-25 labels are a **Rule 24 authoring act on a ruled axis** --
   per the 2026-08-20 widening, PROPOSING OR CHANGING VALUES on an existing axis requires the four-postulate
   record. Until D1 records the supersession, **two conflicting sovereign enums sit on disk for the same
   axis** and the next reader cannot tell which is current. Routed to D1's decomp.

## ANDREW-DIRECT 2026-08-25 ~05:4xZ -- RECORDED VERBATIM (delivered at DS~F's terminal)

> *"Is this just a backfill issue or do we need a whole new pipeline built out/expanded for rebalancer?
> What should effectively happen is that the pipeline should be self-healing. When a new Opal Model appears
> in one of these portfolios, the balance of that portfolio is moved over to "Client - Opal Supervised".
> Every day when the data is pulled, there needs to be a scan if there is any new ones. THat is the loose idea"*

**DS~F's reading is RATIFIED and it is the better architecture: this is DERIVE-DAILY, not
DETECT-AND-NOTIFY.** Membership recomputed from constituent data on every run has **no map to fall out of
date and nothing to detect** -- a new Opal model lands in the right bucket by construction. The only thing
needing a daily check is **COVERAGE OF THE PULL**, and per the standing moratorium that is a **PRODUCER
ASSERT THAT REFUSES THE RUN, never a monitor**: no SNS, no SES, no `*-monitor`, nothing to subscribe to.
**S3 is upheld: no new schedule** -- the pull already has one.

*Worth carrying beyond this project: the moratorium says what NOT to build; his word supplies the positive
form of "what to do instead" -- **derive it so there is nothing to detect, and make the producer refuse
rather than report.** Doctrine candidate, proposed not landed.*

## OPEN AT ANDREW -- ONE, and it folds into a card he already holds

`WSE_COTMDL`'s directive home on re-scope. **REC: fold it under the same card as `COT_CANON458`'s home** --
same firm, same week, adjacent surfaces, one answer covers both.

## COO's THREE ACTS

1. Re-scope `WSE_COTMDL` and enter it at Rule 27 stage 2 -- **DS~F's spec IS the stage-2 PRD input; do not
   commission a second one** (the COT_CANON458 precedent: take the existing measured artifact as ground truth).
2. Seat the env-var apply on a lane not already holding a project.
3. Route finding 2 into D1's decomp as a Rule-24 authoring cell.

**Nothing emits. The STOP is untouched by this ruling.**
