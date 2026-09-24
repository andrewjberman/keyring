# 3.0.0_SA_CVO~Z -- delta 0110-0315Z: two mandates accepted, four artifacts, two self-corrections

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

**Window:** 2026-09-24 01:10Z -> 03:15Z. **4 commits.** Prior log:
`2026-09-23/r12_class_census_delta_2330-0110Z.md` @`cd0268a4f4`.

## THE SHAPE OF THIS WINDOW

Two mandates arrived and **no pinned candidate exists for either**. So the work was **perishable-first**:
capture the before-states that cannot be recovered once a build lands, and grade what already exists.
**That choice is the reusable part of this entry.**

## WHAT WAS DELIVERED

| artifact | commit | what it establishes |
|---|---|---|
| Peers B04/P1 pre-build baseline | `99f8d35d37` | all 5 selections match their stated today-state; `ASML_US_Equity` **confirmed stranded**; the **191** corroborated |
| Lead Panel pre-10:00Z capture | `82d4749ada` | the hour-axis **before** half; the `dated` **type-boundary** finding |
| H03 independent pre-build baseline | `0c802d124d` | deployed chatter identity, role, source class; `names_with_links=3 of 250` |
| H03 preflight grade `de0487e9fe` | `d8f0251c85` | artifact identity corroborated across two encodings; blocker endorsed |

## FINDINGS A SUCCESSOR SHOULD NOT HAVE TO RE-DERIVE

**1. The stranded-set blind spot (Peers).** The route records **two different things** for two failures
and only one leaves a trace: an **UNRESOLVED identity** yields `peer_read {}` -- empty, no read attempted,
**no record of a failed read**; a **resolved-but-absent** key yields a populated `peer_read` with
`status: ABSENT` and a reason. ⛔ **So a stranded set is indistinguishable, from the response, from a
security that never existed.** That is how 111 of them sat unnoticed. **Acceptance consequence: a future
"`peer_read` empty" must not be graded ABSENT-and-fine.**

**2. The `dated` gap is a TYPE-BOUNDARY drop (Lead Panel).** The deployed route **emits** `dated` and
`requested_as_of`; `RankingSet` (`types.ts:181`) and `GenerationFields` (`:93`) **declare neither**. The
information needed to stop a reader being misled by a fresh `generated_at` is **already computed, served
and paid for, then discarded at the client type**. Remedy is client-side; the 2026-09-29 fallback expiry
can be made visible without touching anything that serves.

**3. A cross-check neither lane claimed (H03).** The gold snapshot is **1,596 rows: 1,595 DENIED + 1
PARTIAL** -- **exactly** the migration scope ratified in `C-HV-DAILY-STATUS` and signed by this seat at
`fa4257b65ca7`. Two independent measurements, different seats, different purposes, **agreeing to the
row**. And `denied=0` in that lane's replay is **clause 6 observed working**.

**4. The unit-change warning worth more than the blocker it sat behind.** `names_with_links` **changes
meaning** on gold. ⛔ **Bound here: a rising `names_with_links` is NOT link improvement unless the
population counted is stated and unchanged. A moved denominator is not a better numerator.**

## COMPILER TOOLS

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `lambda invoke` (deployed) | 5 Peers selections, 2 coverage/peers, 3 rankings | PASS | The grading instrument the mandate names; real S3 data plane. |
| `comp-find --corpus aws` | `chatter` LAMBDA | PASS | Rail-directed after a `.tf` grep was gated. Found `amgt-resapp-chatter-axis`, 1 of 217 nodes, with vintage printed. |
| `comp-find` (content) | `RankingSet`, route segments, `names_with_links` | PASS | Denominators printed each time; the `0 hits / 2,361 files` read is what grounded a claim I had asserted. |
| `s3api list-objects-v2` | `peers/v1/` | PASS | 797 objects / 191 keys -- corroborated the mandate's 191. |
| `logs filter-log-events` | chatter producer | PASS | Producer run lines; `names_with_links` is a runtime denominator, not an API field. |
| comp rail | 3 gates fired | **ALL CORRECT** | A recursive `grep` routed to `comp-find`; a `comp-find | tail` refused for erasing the denominator; a `.tf` grep routed to the AWS-plane tool. |

**What worked.** Exercising deployed bytes rather than reading source and reasoning. Every finding above
came from an invoke or a live read.

**What failed -- mine, and both are the same shape.**
1. **I wrote a headline my own stated limit contradicted.** Measured four *adapters*, wrote *"tabs ARE
   independent"*, and put *"I did NOT trace which component invokes which function"* in a limits
   paragraph below it. ⛔ **A disclosed limit under a headline that contradicts it is not a limit -- it is
   a footnote on an overreach.**
2. **I read my own best evidence backwards.** Offered CloudFront counts 21/17/6 as *refuting* a shared
   fetch; they **corroborate** it -- thesis leads because four tabs drive it. **A count that differs
   across members is the SIGNATURE of a shared upstream, not evidence against one.** I had the
   discriminating data, cited it, and inverted it because I had already formed the conclusion.

Both banked: `unequal-counts-are-the-signature-of-a-shared-upstream-not-evidence-against-one`.

**Gap found.** Five `.tf` files carry a CRLF blob against their own `eol: lf` attribute (of 46 estate-wide);
remedy is a re-commit under the rule `.gitattributes` already carries. Routed, not done.

## MCP TRAFFIC

~12 messages, all acked. Significant sends: the slate shared-fetch challenge and my acceptance of
correction 1a; the Peers mandate acceptance with baseline; the `dated` type-boundary finding; the H03
baseline and preflight grade. **Every send to a COO lane is refused by the correspondence guard**, so all
four COO-directed items carry an explicit "relay owed" line rather than assuming delivery.

## BLOCKERS

**None owned by this seat.** Awaiting pinned candidates for both mandates.

**Held elsewhere, evidence-cited:**
- **`E0`** -- blocker filed by `2.0.0_SA_COO~Z` at 02:30Z: no browser connector, CDP 9222/9223
  unreachable, no accessible admin+Dev session. **Not agent-closable.** Everything else sits upstream.
- **H03 input** -- `0/191` admissible windows; the relabel cannot manufacture coverage.
- **The incident's remediation act** -- Andrew's by class, unchanged.

## CURRENT STATE

- **Trunk consolidated:** `origin` has exactly **one head, `CLOUD`**. `SITEZ` is retired. This seat is on
  `CLOUD` in the **shared tree**, which moves under it -- HEAD advanced between two consecutive commands
  this window. **Any coordinate quoted here has a vintage of seconds.**
- **Peers:** baseline captured; `BA`/`992_HK` serve 12 members from `2026-09-17T0240Z` objects; `ASML_US`
  stranded (4 objects, route UNRESOLVED); `CAT_US` resolved with 0 objects.
- **Lead Panel:** chatter `CodeSha256 I6eitcaI...` (= hex `23a7a2b5...`), unchanged since 2026-09-19;
  ranking rows 2 / 0 at 02:39Z; producer `names_with_links 3 of 250` stable across both logged runs.
- ⚠ **`2.0.0_SA_COO~Y`'s deploy ledger is OPEN** (`.open_deploys/amgt-h03-leadpanel-y-20260924.json`).
  **Not this seat's to close** -- flagged because an open entry outlives the conversation that opened it.

## NEXT STEPS

1. **[3.0.0_SA_CVO~Z]** Grade the first pinned candidate on either mandate. For Peers: **one reconciled
   trace per case**, both consumers (`PostureTab.tsx:339-347` calls `usePeerSet` twice -- Peers alone is
   half-graded). For Lead Panel: the **after-10:00Z** half against `82d4749ada`.
2. **[2.0.0_SA_COO~Y]** The open ledger entry, and the CTO ruling requested on the H03 input blocker.
3. **[Andrew]** `E0`, and the incident's remediation act. Both unchanged and both his.
