# RCN-0011 — Should `_authz` be a LAYER so a per-route fork cannot recur?

**Seat:** `4.0.0_SA_CRO`. **Date:** 2026-09-19 ~08:20-09:0xZ. **Asked by:** `1.0.0_SA_CTO`, msg 98186.
**Status:** RESEARCH. No recommendation is made and none is implied; the decision is `1.0.0_SA_CTO`'s.
**Nothing is blocked on this** — `IB-rtf-8` lands the fold regardless.

---

## THE HEADLINE, AND IT ANSWERS THE FORK EMPIRICALLY RATHER THAN BY ARGUMENT

⛔ **THE LAYER ALREADY EXISTS. THE FORKED ROUTE ALREADY ATTACHES IT. THE FORK HAPPENED ANYWAY.**

`infra/aws/terraform/investor-reporting/holdings/lambda.tf:58` reads
`layers = [data.aws_lambda_layer_version.irpt_common.arn]` — and `holdings` is the single route, of 7,
that carries its own local `enforce.py`. So the proposition "a layer prevents a per-route fork of shared
code" is not a hypothesis in this estate; **it has been run, on this exact route, and it did not prevent
this fork.**

`1.0.0_SA_CTO` asked to be checked on its LAYER instinct before anyone looked. This is the check, and the
instinct does not survive it in the form stated.

---

## Q1 — PAST PATTERNS, WITH DENOMINATORS

**13 layer directories** exist under `infra/aws/lambda/layers/`: `anthropic-sdk-deps`,
`deck-generation-deps`, `find-insure-browser-deps`, `find-insure-deps`, `find-insure-parse-deps`,
**`irpt-common`**, `mdpf-gold-calendar-deps`, `news-trending-deps`, `opal-trading-calendar-layer`,
`openpyxl-layer`, `pandas-pyarrow-requests-layer`, `pyiceberg-nessie-deps`, `security-scanner-deps`.
**12 of 13 are DEPENDENCY layers** (third-party wheels). **`irpt-common` is the only FIRST-PARTY
SHARED-CODE layer**, and it is this project's own, built 2026-09-10/11 across 8 commits.

### `irpt-common` is the precedent, and it is a rich one

It already carries first-party shared code — not just wheels: `ids.py` + `raw_keys.json` +
`firm_registry.json` (the ONE opaque-id normalizer, IB-rt-3, on this seat's reading of CTO ruling 4),
`keys.py`, **five** contract schemas, and an AST-closure extract of six Black Diamond helpers.
161 members, 644,526 bytes, `s3://opal-313476888478-lambda-layers/irpt-common.zip`.

**So the estate has already decided, once, that IRPT shared code belongs in a layer — and `_authz` was
not put in it.** The fork question is therefore narrower than "layer or not": it is *why this module was
left out of a layer the route already attaches*, which is a question about what the layer is FOR, not
about the mechanism.

### THE THREE FAILURE MODES THE LAYER ROUTE HAS ALREADY COST, all from its own BUILD_MANIFEST and history

The CTO asked specifically for a layer that was tried and went wrong. All three are measured and
recorded by the seat that hit them:

1. ⛔ **A LOST-UPDATE HAZARD ON A SHARED MUTABLE ARTIFACT — mitigated BY HAND.** The manifest carries a
   `carried_forward_members` block whose stated reason is: *"published in irpt-common:4 by a CONCURRENT
   round-2 cell (row W4-S10's export contracts and the key grammar); carried so this build does not
   revert a peer's landed deploy on a shared artifact. Each was verified byte-equal to the live layer
   member before it was declared."* **A layer version is a whole artifact: rebuilding it from one cell's
   inputs SILENTLY DROPS another cell's landed members unless a human carries them forward.** This is the
   single most important finding for the fork, because it is the divergence class the layer is being
   proposed to close, reappearing one level up with a WORSE detector — a dropped member is invisible
   until something imports it.
2. **A build defect that reached the RUNTIME.** `8e5d8cadad`: *"the assembled bd_helpers raised NameError
   AT IMPORT on the runtime -- the AST closure missed module-level IMPORTS, and the build now has the
   falsifier that would have caught it."* The layer's own assembly step is code, and it shipped broken.
3. **Non-reproducibility from the build host.** `a290b61eed`: three builds of identical inputs differed,
   because pip console-script `.exe` launchers on a Windows host are non-deterministic members; the fix
   was excluding them. Recorded in the manifest as `_excluded_members`.

**NONE of these argues against a layer on its own.** All three were found and fixed, and the manifest is
unusually disciplined (pinned transitive closure, fixed timestamps, `--only-binary=:all:`, a measured
import check). What they establish is the honest cost column: **a layer is not a free single-source —
it is a second build system with its own concurrency, determinism and import-time failure modes.**

---

## Q2 — DOES A LAYER REMOVE THE RESOLUTION, OR MOVE IT? **IT MOVES IT, AND TO A WEAKER POSITION.**

This is the load-bearing question and the answer is not favourable.

On AWS Lambda, the function package unpacks to `/var/task` and layers to `/opt/python`, and **`/var/task`
precedes `/opt/python` on `sys.path`.** So a module present in BOTH resolves to the **package copy**,
silently, with nothing reporting a conflict.

⚠ **STATED AS A PLATFORM PROPERTY, NOT AS A MEASUREMENT I RAN.** I did not exercise a Lambda to observe
the ordering, and the honest status is DESIRED/documented rather than EXERCISED. **It is also the single
fact the whole fork turns on, so it should be exercised before it is relied on** — a five-minute test
(one function, one module in both places, log `__file__`) settles it, and I did not run it because
nothing here is blocked and the decision is not mine.

If it holds, the consequence is sharp:

| | fork detectability TODAY | under a layer |
|---|---|---|
| what the fork IS | a second `enforce.py` **file in git** | a second `enforce.py` file in git that also **shadows the layer** |
| who can see it | `os.walk` census over `entry.py` — **the CTO's S82 instrument found it exactly this way** | same census, PLUS a now-unused correct copy in the layer that reports nothing |
| what the layer adds | — | a copy that is **present, correct, and not the one that runs** |

⛔ **So a layer does not close the hole; it adds a second, correct copy that a stale local copy silently
outranks.** That is strictly harder to reason about than today's state, where there is exactly one copy
per route and a census can count them. **The layer's value is distribution, not enforcement** — and the
fork is an enforcement problem.

**On the build path specifically:** the estate's build tool resolves `source_dir` first (W1-S29's own
account is that this is what shipped the stale copy). A layer does not remove that resolution — the
function package is still built from `source_dir`, and whatever `source_dir` contains still wins at
import. **The resolution that caused the incident is untouched by layering.**

---

## Q3 — THE CHEAPER ALTERNATIVE, WEIGHED HONESTLY

**A check already exists and its enumeration trap is already documented — by its own author.**
`.tools/check-lambda-layer-deps` audits Lambda imports against layer requirements. Its docstring declares
the limitation unprompted: *"Opaque-layer registry currently has only `pandas-pyarrow-layer`. Other
pipelines that use externally-built layers ... will produce false-positive FAILs."* So the estate's
existing layer check is **enumeration-bound and known-incomplete**, which is exactly the class CLAUDE.md
flags on the cross-firm guard (*"an enumerated ban list lapses SILENTLY when a name changes"*).

**What a duplicate-`_authz` check should key on, and the trap to avoid:**

- ⛔ **NOT a filename allow/deny list.** `enforce.py` renamed to `authz.py` lapses it silently — the
  cross-firm guard's exact failure mode, and the reason `_CROSS_FIRM_FOREIGN_BUCKETS` is called out in
  CLAUDE.md as a GATE EDIT rather than an infra act.
- ⭐ **KEY ON THE STRUCTURE THE INCIDENT ACTUALLY HAD, WHICH IS A COUNT, NOT A NAME.** The S82 instrument
  is already the right shape: an `os.walk` over `investor-reporting/`, full denominator (7 `entry.py`),
  asserting that the authorization module each route RESOLVES is the shared one. A count with a printed
  denominator does not lapse on a rename — a renamed second copy is still a second copy.
- ⭐ **STRONGER STILL, AND IT SURVIVES THE RENAME COMPLETELY: key on the IMPORT, not the file.** Parse each
  `entry.py`'s AST for what it binds as its enforcement module and assert every route resolves to one
  path. That is the property the incident violated — `holdings/entry.py:62` imports the SHARED `served`
  while binding the LOCAL `enforce` — and a filename check cannot see a mixed binding at all.
- **COST:** one AST pass per `entry.py` at commit time; the S82 census already exists as working code.
  **NON-APPLICATION:** a route deliberately carrying a divergent boundary, which would need an explicit
  declared exemption — and the estate's exemption pattern (`exemptions.json`) is the shape for that.

⚠ **And the check has the same reach problem as any gate: it binds the repo plane only.** It cannot see a
layer member dropped by a concurrent rebuild (Q1 finding 1), because that divergence never appears in git.

---

## Q4 — LGIC BEARING: **THE CANON EXPRESSLY DOES NOT RULE THIS**

This is NOT a conformance question with an existing answer. R16 is the only candidate rule and it carries
an express non-application:

> **R16 — ONE CODE HOME PER PIPELINE** … *non-application: the git source tree (a different plane:
> repository, not deployment home); **Lambda deployment artifacts** (`lambda-source-map.json`
> `artifact_s3_key`) — they keep the source-map tie, **R16 does not reach them** (GAP-2 RULED, Andrew
> ~01:3xZ 09-13 card 6: "no"). Their KEY's grammar is still graded (R1).*
> — `infra/logic/02_DOCTRINE.md:522-530`

So: **shared-code homes for lambdas are outside what LGIC rules today**, by Andrew's own card. Rule 30
still reaches the artifact's NAME (R1 grades the key), so if a layer is created its name comes from
`lib/opal_naming.py name()` and a builder refusal is a registry row, never a hand-typed workaround.

⚠ **A CITATION HAZARD IN THE CANON ITSELF, flagged for whoever reads it next.** `02_DOCTRINE.md` §6 still
carries GAP-2's **superseded pre-ruling text** — *"Whether R16 reaches them … is unruled. Until ruled,
such surfaces grade UNDETERMINED"* — sitting directly beneath the heading that says both GAPs were RULED
and that the text is "kept for the record". Other superseded items in that section are struck through
(`~~…~~`); **GAP-2's is not.** A reader landing on §6 can cite UNDETERMINED from the live file in good
faith. This is CLAUDE.md's own documented shape: *a rewritten passage does not delete its own old words.*
The authoritative text is R16's non-application clause at `:529`, not §6's paragraph. **Not edited here —
`infra/logic/**` is this seat's lane but the canon's rulings are not this seat's to restate; flagged so
`1.0.0_SA_CTO` can route it.**

---

## WHAT THE EVIDENCE BEARS ON — stated as findings, not as a recommendation

1. The fork recurrence question is **not** "layer vs vendored". The layer is already there on the failing
   route. The question the evidence actually poses is **"what makes a route's authorization binding
   verifiable at commit time"**, and the only instrument that has ever caught this class here is a census
   with a printed denominator — twice: S82 found the fork, and the layer's own manifest needed a
   hand-carried member list to avoid a lost update.
2. A layer changes WHERE the copy lives. It does not change WHO WINS at import, and on the documented
   path ordering the loser is the layer. **Any layer decision that rests on "then the fork cannot happen"
   should be gated on exercising the `/var/task` vs `/opt/python` ordering first** — it is cheap and it is
   the fact the whole argument stands on.
3. The layer route carries a real, measured cost column the fold does not: a second build system with a
   concurrent-rebuild lost-update hazard that this estate has already hit once and mitigated by hand.

**NOT ASKED AND NOT ANSWERED:** whether `_authz` SHOULD join `irpt-common` on distribution grounds (one
deploy instead of seven), which is a separate and possibly good reason to layer it that has nothing to do
with preventing a fork. The CTO's fork question and the distribution question have different answers and
should not be decided as one.

---

## INSTRUMENTS

| Question | Instrument | Denominator |
|---|---|---|
| declared layers | `comp-find 'aws_lambda_layer_version' --all` | 444 hits / 168,713 files |
| layer dirs | directory listing | 13 |
| irpt-common reach | `comp-find 'irpt-common' --files --all` | 540 hits / 168,715 files; 8 investor-reporting `.tf` |
| **the crux** | `holdings/lambda.tf:58`, bytes printed | 1 of 7 routes forked, and it attaches the layer |
| layer history | `git log` on the layer dir | 8 commits, 2026-09-10/11 |
| LGIC bearing | `02_DOCTRINE.md:522-530`, `:223`, `§6` | R16 non-application, Andrew card 6 |
| existing check | `.tools/check-lambda-layer-deps` docstring | its own declared MVP limitation |

**NOT EXERCISED, and each is named rather than assumed:** the `sys.path` ordering (the load-bearing fact);
the live AWS layer versions and which function versions actually attach them; whether the other 6 routes'
`entry.py` bind the shared `enforce` (S82 measured the file census, and I did not re-derive the binding).

---

# ADDENDUM A — the second case, found after the first send, and it REFINES the headline

Written ~08:5xZ, same seat, ~20 minutes after the body. **It changes the headline's force and it is
recorded here rather than by editing the sentence above.**

## A SECOND FIRST-PARTY LAYER EXISTS, AND IT HAS THE SAME SHAPE

`opal-trading-calendar-layer`. Its governing ruling is quoted verbatim inside a live Lambda
(`infra/aws/lambda/bd-pipeline/bd-49f-etf-ownership-daily/lambda_function.py:38-42`):

> *"THE CALENDAR COMES FROM THE PUBLISHED LAYER, NOT A COMMITTED COPY (CTO~Z ruling msg 5462
> @1da1e2b73b, **"MINT THE LAYER, NOT A FIFTH COPY"**): `import trading_calendar` below is a BARE import
> resolved via the Lambda layer mount at /opt/python/ … **No trading_calendar.py is vendored into this
> directory or added to the source map.**"*

So the estate has RULED this exact class before, and the winning pattern is stated in terms. ⭐ **Note
what actually does the work in that sentence: not the layer, but the SECOND clause — no vendored copy,
not in the source map.** That function had to SAY SO explicitly, which is itself the tell.

## AND THE RULING DID NOT HOLD ACROSS THE PIPELINE — 3 VENDORED COPIES SURVIVE TODAY

`comp-find --name 'trading_calendar.py' --all`, denominator **6 hits / 173,621 files**: the canonical
`lib/trading_calendar.py`, its test, one ETFS fixture — and **THREE live vendored copies in Lambda
source directories**:

```
infra/aws/lambda/bd-pipeline/bd-served-vintage-alarm/trading_calendar.py
infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/trading_calendar.py
infra/aws/lambda/opal-assets-absence-check/trading_calendar.py
```

⛔ **SO BOTH OF THE ESTATE'S FIRST-PARTY LAYERS COEXIST WITH VENDORED COPIES OF THE CODE THEY PUBLISH.**
Two of two. A layer plainly does not, by itself, prevent a second copy — and this is now measured on two
independent pipelines, not argued.

## BUT THEY HAVE NOT DIVERGED — THIS IS AN EXPOSURE, NOT AN INCIDENT

All three hashed against the canonical frontier, CRLF-normalised:

```
CANONICAL lib/trading_calendar.py        sha256[:16] 41b1c0c12651c62e
bd-served-vintage-alarm/…    6979 bytes  41b1c0c12651c62e   IDENTICAL
inf-etf-ownership-daily/…    6979 bytes  41b1c0c12651c62e   IDENTICAL
opal-assets-absence-check/…  6979 bytes  41b1c0c12651c62e   IDENTICAL
denominator: 3 of 3 vendored copies vs 1 canonical frontier
```

Per CLAUDE.md Rule 22's negative mirror, **ABSENT ≠ EXERCISED-AGAINST**: three unguarded copies of the
estate's declared *"ONE frontier"* is a REAL HAZARD, and 3-of-3 identical says it has **not fired**. So
the remedy is BUILDING THE GUARD, and **nothing needs re-opening** — no calendar-derived output is
suspect on this evidence. ⚠ Measured at this vintage only; the copies are unguarded, so this reads clean
today and carries no promise about tomorrow.

## THE SENTENCE THAT MATTERS MOST FOR THE DECISION

**In BOTH first-party layer cases, the state of the copies was established by a CENSUS SOMEBODY HAPPENED
TO RUN — never by a check.** `_authz`'s fork was found by `1.0.0_SA_CTO`'s S82 `os.walk`; the calendar's
three copies and their cleanliness were found by this census, twenty minutes ago, because the fork
question sent me looking. Neither was caught by tooling. **That is the argument for Q3's check standing
independently of how the layer question resolves** — it is the only instrument that has ever detected
this class here, and today it is run by luck.

## HOW THIS REFINES THE HEADLINE

The body says the LAYER instinct "does not survive in the form stated". That stands, but it is now
sharper and slightly kinder to the instinct:

- **A layer does not ENFORCE single-source.** Measured, 2 of 2 first-party layers.
- **A layer DOES deliver single-source when paired with the no-vendored-copy discipline** — which is
  exactly what the `bd-49f` docstring spells out, and exactly what its three siblings did not do.
- **So "mint the layer" and "prevent a second copy" are two separate acts**, and the estate's one
  fully-correct precedent performs both. A decision that performs only the first buys distribution and
  no fork protection, which is the state `holdings` is already in.

**Still no recommendation.** The decision is `1.0.0_SA_CTO`'s, and the distribution question named in
the body remains separate and unanswered.

## INSTRUMENT NOTE — a false zero I caught on myself, recorded because it nearly shipped

My first census of the layer mount ran `comp-find '/opt/python'` and returned **"0 hit(s) across 168,722
files"** with a full denominator. It was a FALSE ZERO: MSYS path-mangled the leading-slash argument, and
the tool's own echo line printed what it actually searched for — `C:/Program Files/Git/opt/python`.
Re-run as `opt/python` it returns **200 hits**, including every finding in this addendum. ⭐ **The tell
was the tool ECHOING ITS OWN PATTERN; nothing else in that output was wrong.** A measured zero with a
printed denominator over the right corpus, answering a question nobody asked. Had I trusted it, this
addendum would not exist and the body's headline would have stood unrefined.
