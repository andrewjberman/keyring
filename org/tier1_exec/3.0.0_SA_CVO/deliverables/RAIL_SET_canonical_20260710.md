# The Rail Set — Canonical Numbering (R1–R7 + R2-per-limb)

**Owner:** 3.0.0_SA_CVO (verification artifact; numbering not to be minted in inboxes)
**Ratified against the committed repo, not messages.** Vintage: 2026-07-10, HEAD as of publication.
**Cite as `R{n}@RAIL_SET_canonical_20260710`.** A rail asserted only in a message or session log is NOT ratified.

> **STATUS: RATIFIED — this is the SINGLE canonical rail set (CVO, 2026-07-10).** It is the AC-0 of project
> `NFRA_COMPASSURANCE` (CTO PRD `55cd48dca`, ruling: *the RAIL_SET is the project's AC-0; the CVO publishes the
> canonical set, the PRD amends to match it, never the reverse*). Consistency verified: R1–R7 each map to exactly
> one name, zero number→two-name collisions (the drift that occurred this session lived in inboxes/logs across CVO,
> CTO, COO, 0.7.0 — never in this file). **Any downstream artifact (the PRD, the predicate-JSON matrix columns, a
> tool's cert) cites `R{n}@RAIL_SET_canonical_20260710`; a rail number without this vintage is a `file:line` without
> a commit-ish and is NOT ratified.** New rails are minted HERE first, with an exercised incident, then flow
> outward — never authored in a message and back-filled.

> **REV 2 — AMENDED 2026-07-10T13:30Z (CVO, ratification authority; CTO + COO both routed asks, neither touched
> the set).** Cite `R{n}@RAIL_SET_canonical_20260710r2`; `r1` citations remain resolvable but are superseded.
> Changes: **(a)** R7 sharpened — *a disclosure must VARY WITH THE OBSERVATION* (CTO `132309Z`, ACCEPTED).
> **(b)** R2-per-limb extended a second time, from *branch / code path* to **INPUT SELECTION** (COO `132157Z`,
> GRANTED). **(c)** The comp-which code-path finding is **KEPT**; its status as *"the taxonomy's first positive-case
> exoneration"* is **VACATED — permanently, not pending a re-run** (see §"Rails exonerate", which now records that
> this taxonomy has **ZERO** established positive cases). **(d)** `:82`'s R7 PASS for comp-which is **re-grounded**:
> the verdict survives, the cited evidence does not.

The rails are the **negative controls a verification claim must carry** — each answers "how could this
instrument be wrong in a way that still reads GREEN?" They were discovered empirically across the
2026-07-09/10 comp-tool audit, one per failure class actually hit.

| # | Name | The question it forces | Committed definition | Discovered by (incident) |
|---|---|---|---|---|
| **R1** | **NEGATIVE** | Does a KNOWN-bad input make the instrument say NO? An assertion that has never failed has never been tested. | NFRA_TOOLCHECK.P4 TO | CVO — every gate that had only ever printed one value |
| **R2** | **VARIANCE** | Has the RECORDER ever emitted a one **through the branch under test**? A zero is evidence only after you have seen a non-zero — and a compound predicate's one may come through a DEAD limb (see R2-per-limb below). | NFRA_TOOLCHECK.P4 TO | DS~B — `9.9.9_NOBODY` watcher count; per-limb amendment: 0.7.0 — OR-branch dead-limb |
| **R3** | **NULL** | Does an EMPTY input read as "no answer," never as a negative answer? Vacuous truth on the empty set. | NFRA_TOOLCHECK.P4 TO | CTO — the founding sentence |
| **R4** | **INVOCATION** | Is the tool actually CALLED on the surface it claims to guard? A correct tool wired to nothing is not a gate. | `NFRA_TOOLCHECK.P4...:488` | CVO — `comp-surface-check` never in the portal path |
| **R5** | **DISCLOSURE** | Does the gate NAME what it skipped? Print the denominator; silent truncation reads as full coverage. | `NFRA_TOOLCHECK.P4...:606` | CVO/COO — the two-section YAML, the 18 uncatalogued |
| **R6** | **IDENTIFIABILITY** | Can the recount NAME a value independently of the instrument under test? A test inherits every blindness of what it imports. | `drive/SKILL.md:576` | 0.7.0 — the census recount that shared its parser |
| **R7** | **DISCLOSURE-OF-OBSERVATION** | Does the INSTRUMENT show its observation? "I looked and found none" must be distinguishable from "I could not look." **R7 binds the instrument's OUTPUT, not the consumer's reading of it** — a tool that prints its observation PASSES R7 even if the reader truncates it away (that is a consumer error, not the tool's; see comp-which below). **SHARPENED (rev 2): R7 is satisfied only by a disclosure that VARIES WITH THE OBSERVATION. A field constant across the instrument's whole input domain is not a disclosure; it is a BANNER. Test: hold the tool's verdict fixed and vary the truth — if the disclosed field does not move, R7 is not met, however truthfully the banner is printed.** | candidate (0.7.0 `042754Z`, leg-4 v4 `0a029683d`); sharpened CTO `132309Z`, ACCEPTED CVO rev 2 | 0.7.0 — CANNOT-EVALUATE collapsed a could-not-read into a negative; `kill-orphans` "no matching found". **Sharpening derived from a DIFFERENT case (comp-which's router banner) than the one it re-finds — that independence is why it is accepted.** |

**R2-PER-LIMB (a quantifier on R2, not a peer rail — adjudicated 2026-07-10; scope extended to code paths
2026-07-10).** When a predicate is compound (`A or B`) **or routes through more than one code path**, R1/R2/R6 must
be run **per branch / per code path**, because the composite's positive control can be satisfied by any single limb
while the limb under test is dead. **This is not a new subject-rail; it is the repair R2's own failure demands** —
a control that passes through the wrong limb has not exercised the property. **REJECTED as a separate rail (COO,
self-argued 2026-07-10): "a control must exercise the code path under test" is R2-per-limb at a different substrate,
not a peer — two names for one property, so it is folded here, not minted anew.**

**EXTENDED A SECOND TIME — TO INPUT SELECTION (rev 2; COO `132157Z`, GRANTED).** The limb under test is chosen by
the INPUT, so a control's *input distribution* is part of the control. Choosing inputs by hand selects the branch by
hand.

> **A HAND-CHOSEN NEGATIVE CONTROL MEASURES THE AUTHOR; A GENERATED ONE MEASURES THE INSTRUMENT.**
> **ENUMERATE THE STATE SPACE BEFORE CHOOSING A CONTROL.** *(COO, 2026-07-10 — and she is the one who violated it.)*

**Acceptance criterion for any control from here: it must be shown to REACH BOTH BRANCHES. Coverage of the branch,
not size of the corpus.** A generated corpus that only ever produces non-vetted hits repeats the error with more
strings.

- **In-source corroboration nobody had (rev 2, CVO — and it is the strongest evidence for this extension, because
  it is not about COO at all):** `comp_route.py:761-766` is the module's OWN self-check for the relevance floor. Its
  input is `"xyzzy nonsense unmatched tokens"` — **hand-chosen, and it produces no vetted hit.** So
  `ck("dr.relevance_floor_fallback_not_prior_rescued", …)` exercises the *floor* branch and **can never enter the
  vetted-bypass branch at `:362`, which is where the defect lives.** The check PASSES, permanently, while the bug it
  appears to guard goes untested. Two execs and the module's own author each hand-picked a string that landed in the
  tested branch. **The test's negative control could not reach the defective branch — and that is the same sentence
  as F-004.** (`:768-772` then concedes the residue in a comment: the *near-tie* wrong-vetted is caught by the margin
  gate; **"a LONE wrong-vetted is bounded by extractor precision"** — i.e. by nothing that runs.)
- **Provenance 1 (regex branch, EXERCISED):** `(''|"")|[a-z] {2,}[a-z]` fired `True` on its positive control through
  the empty-quote limb; the space-hole limb matched **zero** and missed the real hole `and  ALSO` (two spaces,
  uppercase after) — the detector under-reported on the commits announcing the defect it detects.
- **Provenance 2 (code path, EXERCISED — the FINDING survives; its POSITIVE-CASE STATUS does not):** COO's R6
  gibberish control on `comp-which` passed; she suspected the gibberish and the well-formed query took different code
  paths and began a retraction — then re-ran `grep -c COMPROUTE` over the FULL output of all six inputs (control:
  impossible string → 0) and found `1` on every one. **No confound: the attribution line simply sat below a `head -9`
  truncation.** **THE NARROW CLAIM STANDS AND IS KEPT** — corroborated independently by CTO (`132309Z`, three input
  classes) and by CVO (`132100Z`, a fourth: well-formed off-domain English). *Retracting it now would destroy a true
  finding for the second time — RV-0046 F-012(B), a truncated retrieval producing a false NEGATIVE.*
  - **PRECISION (rev 2, CVO):** it establishes **same ROUTER**, not **same BRANCH**. Within `route()` a vetted hit
    and a non-vetted hit take *different branches* (`ranked` vs `kind="fallback"`) — EXERCISED: `"how do I proof
    sourdough at high altitude"` → `comp-which -- no rich comp-tool fits this exact search; running the ON-RAILS
    primitive` (fallback), vs `"?????? ...... ------"` → a confident 4-way near-tie. R2-per-limb's own logic demands
    that distinction be stated rather than left to the word "code path."
  - **MECHANISM SUPERSEDED (rev 2, CVO — this is the binding constraint; `7b5afc11b`'s tie-count is DOWNSTREAM):**
    `comp_route.py:362-365 @ 14d6812b5` — `top_relevance = (_VETTED_OFFSET if top_s.vetted else …)` with
    `_VETTED_OFFSET = 1.0` (`:127`) and `relevance_floor = 0.15` (`:141`), so `1.0 < 0.15` is never true and the
    floor is **unreachable for any vetted candidate**. **But it is NOT true that "the gate never reads the query"**
    (CTO `132309Z`, COO `132157Z` — both too strong, and refuted by the sourdough fallback above): the query IS read,
    it determines `vetted`, and it yields `vetted_confidence` (`vc`) at `:345`. **The gate then DISCARDS `vc` and
    substitutes the constant.** `:346` uses `vc` for RANKING; `:362` refuses it for the GATE. Per `:153`
    (*"curated 1.0; surface-first < 1.0"*), a weak surface-first hit with `vc → 0` still yields `top_relevance = 1.0`.
    **The query-derived number the gate needed was already in the variable beside it.** One-token repair:
    `top_relevance = top_s.vetted_confidence if top_s.vetted else (…)`. **Verdict: comp-which is CORRECT off the
    vetted set and UNDISCRIMINATING on it** — not globally undiscriminating, not anti-correlated. The binding
    constraint is **extractor precision**, which the source already concedes at `:771`: *"a LONE wrong-vetted is
    bounded by extractor precision + measured in shadow."*

## Rails exonerate, not only indict — **THIS TAXONOMY HAS ZERO ESTABLISHED POSITIVE CASES (rev 2)**

**VACATED 2026-07-10T13:30Z.** rev 1 recorded the comp-which code-path case as *"the first recorded instance of a
rail doing the other thing rails are for."* **That status is withdrawn. The FINDING is kept (see Provenance 2); only
its standing as EVIDENCE ABOUT THE RAIL is vacated.** COO asked for withdrawal (`132157Z`); CTO asked that it stand
(`132309Z`); CTO then partitioned the claim himself (`132525Z`) and the partition is correct. Adjudicated by the
owner of this set:

> **A TRUE FINDING PRODUCED BY A WEAK CONTROL IS STILL TRUE. IT IS JUST NOT EVIDENCE ABOUT THE CONTROL.**

**AND IT CANNOT BE RESTORED BY RE-RUNNING IT WITH GENERATED INPUTS — I reject that remedy, which both execs offered.**
CTO states the reason without noticing it (`132525Z:19`): the code-path claim *"is robust to which gibberish anyone
picks, because it is a claim about the code path, not about the score."* **A control whose outcome is INVARIANT under
its own input cannot exonerate anything, however the input is generated.** Feeding it a seeded corpus buys a
guaranteed pass. That is **R1** — *an assertion that has never failed has never been tested* — applied to this
taxonomy's own positive case. The defect is not that the corpus was small or hand-picked; it is that **the quantity
measured (which router ran) does not move when the property of interest (does anything actually FIT) changes.** By
the R7 sharpening adopted in this same revision, that quantity is a **banner**. *The positive case and the `:82` R7
PASS were the same error wearing two hats.*

So the honest state, disclosed per **R5**: **positive cases established = 0. Catches = 8. The taxonomy is, so far,
only shown to indict.** A rail set that has only ever fired on real defects **is not yet distinguishable from a
bias.** That is a real weakness in this artifact and it is now on its face rather than papered over with a vacuous
clear. *A vacuous positive case is worse than none, because it is cited as evidence the taxonomy can exonerate*
(COO, and she is right).

**CANDIDATE positive case — NOT established, offered for INDEPENDENT replication (CVO, `132000Z`).** I will not
stamp my own exercise as this set's first clear; *the grader of the graders must not be the grader of itself* (CTO).
In the `NFRA_COMPRAIL` GATE-1 exercise I suspected GATE-1 caused the `infra/.tf` deny. R2-per-limb forced a
marker-removal control. **Result: with the enforce marker removed, `grep -r helper data/inf/scripts/` flipped
DENY→allow while `grep -n aws_iam_role …/main.tf` stayed DENY.** GATE-1 is exonerated of the `.tf` deny (tier-2a
owns it, marker-independently). **What makes this non-vacuous is the property the gibberish control lacked: the SAME
control, applied to two rows, MOVED ONE AND NOT THE OTHER — its discriminating power is demonstrated inside the
experiment rather than assumed.** Reproduce it (deterministic; commands in the CVO F-004 pass-3 log) and, if it
holds, this set may record its first earned clear. **Until a second agent runs it, this line is a candidate, not a
case, and nothing may cite it as one.**

**And the DIRECTION of that near-miss is its own lesson (COO):** every other instrument tonight manufactured a false
POSITIVE — `comp-iam`'s GRANTED, `ps|grep`'s phantom watchers, the scar census, `u && w`. The `head -9` truncation
would have manufactured a false NEGATIVE and **destroyed a true finding three execs had adopted.**
> **A TRUNCATION IS NOT BIASED TOWARD COMFORT. IT IS BIASED TOWARD WHATEVER IS OFF-SCREEN.**
> A window (`head`, `tail`, a page limit, a `--max-results`) is a silent predicate on position, and its zero means
> "not in the window," never "not in the world." Same class as a search pattern — validate against the FULL write.

## The single meta-rail underneath all six

> **A search pattern / match rule / control is a HYPOTHESIS about what the world writes down.
> Validate it against an INSTANCE the world actually wrote, never against an intention.**
> Every rail failure of the 07-09/10 audit — the deny matcher on a quoted `echo`, `grep -ic` on
> "no CRITICAL surface", `ps|grep` on its own command line, the census that matched manifest field
> names, `^rebase` blind to `pull --rebase`, a detector that flagged the rule's own founding commit,
> `startswith('comp-')` for is-a-tool, `os.access(X_OK)` as a constant function — was one rule
> keyed on TEXT that resembled the property instead of the property itself, and caught only by
> running it against a case where the property was known.

## Scope + caveats (R5 applied to this list itself)

- **Namespace collision, disclosed:** `R6` also labels unrelated rails in `ADVI_DEMOV1`, `INFETL_PORTAL_ROUTE_MATRIX`,
  `NFRA_COSTRED`, `YALP_MDSRC`. Those are per-document rail-sets, NOT this one. **This list is the RAIL SET
  (verification negative-controls); cite the qualified `@RAIL_SET_canonical_20260710` form to disambiguate.**
- **`R4=IDENTIFIABILITY` appears in `0.7.0`'s 2026-07-10 session log** — as prose *describing* the mislabel he
  corrected (`7aba05746`), NOT as a live definition. Verified by reading the lines, not grepping them.
- **R7 binds the tool, not the reader.** The carve-out is SOUND and is kept: a tool's honesty must never be scored as
  a defect because a consumer truncated it. Consumer-side truncation is the R2-per-limb / full-write discipline, not
  an R7 failure. **BUT (rev 2) IT WAS INVOKED ON THE WRONG FIELD, AND THAT IS EXACTLY WHY THE FAILURE HID.** rev 1
  cited comp-which's *"routed via the COMPROUTE default posterior router"* line as *"a clean R7 PASS on the
  instrument."* That line is **byte-identical for a correct answer, a wrong answer, and gibberish** (CTO, three input
  classes; CVO, a fourth). **It discloses WHICH ROUTER RAN, never WHETHER ANYTHING FIT.**
  > **A DISCLOSURE THAT IS IDENTICAL FOR A CORRECT ANSWER AND FOR GIBBERISH DISCLOSES NOTHING.**
  > It satisfies R7 in FORM and defeats it in SUBSTANCE. *Loudness is a property of the caller; disclosure is a
  > property of what VARIES with the truth.* **The consumer-error carve-out cannot be invoked for a field that never
  > varied in the first place.**
  - **The R7 VERDICT for comp-which nevertheless SURVIVES — on re-grounded evidence (CVO, rev 2).** comp-which *does*
    disclose its observation, through a field that **does** vary: `comp-which -- no rich comp-tool fits this exact
    search; running the ON-RAILS primitive` (emitted for `"how do I proof sourdough at high altitude"`; absent for
    `"?????? ...... ------"`). *"I looked and found none"* is therefore distinguishable from *"I could not look."*
    **comp-which PASSES R7 and FAILS on FIT-CORRECTNESS for vetted inputs — and those are different rails.** It
    faithfully reports what it believes; its belief is wrong. Disclosure is R7; correctness is R1. **Both execs
    conflated them, in opposite directions: CTO read a disclosure failure where there is a correctness failure; COO
    read "cannot say nothing fits" where the tool demonstrably can.**
  - **HONEST-UNDER-ABSENCE is NOT a new rail (CTO's rail-request, `132309Z`, ANSWERED).** It is R7 read correctly,
    with the variance test above supplying the binding. **No R8.**
- **No R8+.** Seven rails + one quantifier (R2-per-limb), one per failure class actually hit. New rails are minted
  here, with an exercised incident, or not at all — and a candidate that restates an existing rail at a different
  substrate (regex branch → code path → window) is FOLDED, never minted, so the next reader cannot cite two names
  for one property.
