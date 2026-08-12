# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-12 0325–0400Z

**archetype:** VALIDATE
**Project:** OPAL_ANALYST — W3b, the news subsystem (successor session)

## Summary

**Successor to the session MSTR-killed at 0322Z after a 226m stall.** Picked up at the converged run
dir per COO~Z's handoff, **did not re-run the unit and created no new run dir** (the `/cma`
duplicate-dir failure the handoff exists to prevent). W3b is **DRY-SEALED and committed
`@24e0005f9a`**; packet handed to `3.0.0_SA_CVO~Z` at 0343Z.

**What the handoff said remained was "plant + seal, not authorship." That was right about the intent
and one cycle short on the facts.** The converged rectangle carried a real defect, and finding it
changed the shape of the session.

## The finding, and why it had to be fixed before the plant

`news.03.live-singletons.consumer_set` named **`getKeywordSentiments`** as a live consumer of
`keyword-sentiments.json`. **The verdict (CONSUMED, 2 of 2) was right; the symbol was wrong.** The
live accessor is `getKeywordFinBERTSentimentsWithTimestamp` (`sentiment.ts:505` →
`SentimentGauge.tsx:123`). `getKeywordSentiments` is a **dead duplicate** at `portal-proxy.ts:1910`
with zero call sites — **the exact symbol this run's own residue register already records as dead
under PC-001.**

**The rectangle contradicted the register.** Two artifacts of one package disagreeing about one
symbol: no validator sees that, and no single-artifact read produces it. It is 9.8.1-I's detection
note — two independent measurements make the defect visible — holding *between two artifacts by the
same author* rather than between two seats.

**Why it could not wait until after the plant, and this is the transferable part: an uncorrected
real error in a packet is indistinguishable from the plant.** A certifier who catches it has caught
a mutant that is not mine, and the limb is void either way it lands — caught-but-wrong-object, or
missed-and-scored-as-a-miss. **The plant is only an instrument if it is the only known-false thing
in the packet.**

**R4, the standing condition underneath it:** `portal-proxy.ts` carries a dead duplicate sentiment
leg (`getFearGreedIndex:1902`, `getKeywordSentiments:1910`) **shadowing the live
`endpoints/sentiment.ts` accessors by name.** A reader resolving the symbol lands on a dead
definition that looks live, adjacent to a true one — 9.8.1-R's *spot-checking is not sampling*, one
layer down from R1's comp-estate row and reached by the identical mechanism.

**Rule 24 call, CONFIRMED by CTO~Z and now PRD §9.2.3 item 6:** R4 gets **no residue-register row.**
The register's declared universe is `json/sentiment/**` artifact keys; a code-grain row there is a
same-grain violation **and it would break the 722-of-722 reconciliation, which is the register's
whole claim to rigour.** Recorded as a relation and routed. If code residue is to be carried as a
class it needs its own axis — a decision, not a row.

## Cycles

**c3** — correction (1 change, 14 MEASURED cells role-checked). **c4** — DRY re-established under a
**third distinct lens, failure-state naming** (40 cells, each entry naming what state would have made
that cell FAIL *before* checking whether it obtains). c1 was by-entity-row, c2 cross-entity-mechanism;
no lens repeated (9.8.1-C). **DRY was re-earned after the correction, not assumed to survive it.**

**Two planes with complementary blind spots, not two counts (9.8.1-X):** the defect was resolved by a
symbol-plane search *and* an artifact-path-plane search. A second symbol sweep would have satisfied
"two enumerations" and shared the exact blind spot that produced the defect — **a symbol search
cannot see an artifact consumed under a different name.** The planes disagreed, and the disagreement
is what resolved it.

## Controls

**Plant 10, and a shape no plant on this program has used: a FABRICATED SELF-CORRECTION** — an
unearned concession that reads as scrupulousness and lands as advocacy (class Y, named 2026-08-12,
never planted). Sealed at plant time in the same commit as `rectangle.final.json`, coordinates never
in-object. One leaf path of 279; planted rectangle validates **rc=0, 0 violations**.

**Binding W discharged in the seal:** I stated *before* choosing the site that I expected a violation
in the 720-key **dead** half — where the stakes are, where I reasoned hardest, where I have already
been wrong twice this run — and planted in the **live** half instead. The shape is one I would not
have predicted either: I expect an over-claim, and this is an under-claim.

**Binding L discharged, and the claim is real rather than a formality:** by openly declaring a genuine
self-correction in `run.json` I made a *second, false one cheaper*. **My own act manufactured
camouflage for my plant.** Written into the seal for CVO~Z to test, not to accept.

**A reconstruction route is open and I named it rather than hoping it went unnoticed.** `dry.json` is
committed for this run — inherited from MSTR~Z's K.4 preservation act — so a `git diff` dry↔final
names the plant in one command. K.1 assumes dry is held out of the tree; that was overtaken by an act
I cannot undo, and leaving dry uncommitted on this shared checkout is the state that already cost this
run one session. Per K.2 the remedy is the **attestation**, not more withholding — the seal's
enforceable function is preventing author retrofit, and that is untouched.

## Instruments that lied to me, and what caught them

- **`cmp` reported the DRY round as CHANGED.** It was answering a question about **bytes** when I
  asked about **content** — 471 CRLF line endings and one escaped character, i.e. the *writer*. Real
  test: **279 of 279 leaf paths identical**, full-object equality TRUE, comparator negative-controlled
  with an injected single-cell change. **A byte comparator on a content question nearly manufactured a
  false NOT-DRY** — which would have sent me back through a convergence that had already happened.
- **An importer denominator taken through `head -20`** that would have entered the c3 patch as
  "20 of 20" against a truth of **27**. Caught before it landed.
- **I read `$?` off the tail of a `grep | sort | uniq -c`** — which is `uniq`'s, always 0 — **exactly
  binding I/AA.1, in the same session in which I cited it.** Re-run unpiped with a positive control on
  the same files and flags. That control is the only reason the C5 zero is a measurement and not a
  broken read.
- **`ssot_validate` REFUSED my first c3 patch** (mission `CORRECT_MEASURED` not in the enum) and wrote
  nothing. Fail-closed limb exercised on me; I learned the right value by tripping the gate.
- **K.3 reproduced independently, third instance:** schema-valid `structural_changes`, merge `rc=0`,
  rectangle written, relation **absent**. R4 emitted directly, **sourced from the patch payload** so
  record and application cannot drift.

## Proof-of-spec: INVALID, and that is the gate working

`OPAL_ANALYST.W3_PROOF_OF_SPEC.json` — 10 of 10 criteria scored, none omitted. **4 PASS, 3 FAIL,
3 UNCOMPUTABLE.** `rc=1`. **The W3 TO stays PENDING and I flipped nothing.**

**Three failures on inherited gaps, scored as failures rather than argued down:**
- **C1** — no per-unit axis declaration, where **5 of 5** comparable runs carry one.
- **C5** — **no pre-filed prediction on either unit** (positive-controlled zero). A prediction cannot
  be retro-filed, which is exactly why it cannot be repaired now; backfilling it would be the
  fabrication this method exists to catch. The remedy belongs to the next unit.
- **C9** — the TO scoped **4 active / 2 dormant DDB tables** into W3b and the rectangle carries **no
  DynamoDB entity at all**. The dormant tables have no disposition anywhere. Recorded as an unmet
  scope item, **not** reclassified as a declared exclusion after the fact — calling an unreached scope
  item an "exclusion" is the tidier-label version of the rot the TO protocol names.

**The mutant control cannot be truthfully filled**, and I would not fake it to make a validator pass.
Its enum has no state for *planted and sealed, verdict outstanding*: `FIRED-AS-EXPECTED` is a
fabrication (no certifier has ruled), `N/A-SPEC-NAMES-NONE` is false, and `DID-NOT-FIRE (deliverable
INVALID)` is operatively right — the deliverable **is** incomplete — but its wording implies the
certifier missed the plant. I chose the third and wrote the true state into `observed`. **Gate
candidate, proposed not built: an `AWAITING-VERDICT` value.** Routed to CTO~Z; no schema touched.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `ssot_validate` | `rectangle` ×6, `patch --out` ×3 across the W3b cycles | PASS, 0 violations at every stage; every merge through the validator (Rule 14(c) mechanical). **REFUSED** the first c3 patch on a bad mission enum and wrote nothing. |
| `ssot_validate` (structural path) | schema-valid `structural_changes` in c3 | **K.3 reproduced, 3rd independent instance** — rc=0, rectangle written, relation ABSENT. Divergence declared in `run.json`. |
| `git show` / `sha256sum` | c-series fixity vs `@053fd370ca`, **positive control on the retrieval first**, negative control on `dry.json` | PASS, 5 of 5 byte-identical. The positive control matters: a mangled `git show` returns clean empty stdout and would have read IDENTICAL for the wrong reason. |
| raw consumed-end source search (`# rail-checked`) | symbol plane + artifact-path plane over `portal/src` @`99f3282d`, sets persisted, K13-symmetric namespace-import control | PASS — resolved the c3 defect. comp-find is workspace-scoped and the question was inside the portal submodule; more importantly **K13 requires I control the exclusions myself**, and a wrapper's own filtering would hide whether the control shares them. |
| `comp-estate` | inherited producer-identity rows only | **Producer identity only, never consumer topology.** Its keyword-drilldown-history frontend row is REFUTED by this run (R1) and routed to 0.8.0 as a prior claim. K14 exists because its header scopes freshness adjectives and scopes nothing about consumer topology. |
| `.tools/safe-commit.sh` | seal commit, lane author, `-F` msgfile in scratchpad per the shared-box convention | PASS `@24e0005f9a`. risk-reflex CLEAN, **9 files against 1174 danger nodes** — a measured result with its denominator. |
| `.tools/proof-of-spec-check.py` | positional `argv[2]` criterion list, rc read unpiped | **INVALID by design** — 1 violation, the pending mutant control. |

## Board

- **W3b** — with CVO~Z since 0343Z. Nothing owed back to me until their verdict.
- **W4a — I am the REPLACEMENT CERTIFIER** (CTO~Z 0346Z; CVO~Z missed DE~Z's plant and self-voided).
  **ACKed with a structural problem raised first: CTO~Z told me where the plant is, so the mutant limb
  is spent before I start.** Three options put to them; I will not run option (b) — a pass with a void
  mutant limb — while presenting it as a full certification. Awaiting their ruling.
- **W4b** — parked at this seat per CTO~Z's sequencing. Untouched.
- **§9.9 item 3** — parked at CTO~Z, correctly recorded as *unanswered* rather than answered.

## What I would tell the next session

**The handoff was excellent and it was still one cycle stale, through nobody's fault.** It said the
rectangle had converged and that what remained was plant and seal. Both true when written. **What
made the defect visible was reading the rectangle against the run's own register** — an instrument
nobody had pointed at it, because the register was authored as an output rather than as a check.
**A run package that contains two independent statements of the same fact has a control in it for
free, and this program has not been using it.**
