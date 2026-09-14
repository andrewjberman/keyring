# CLAUDE.md — Opal Capital Workspace

**HOW WE WORK and HOW TO THINK: fast and accurate, in that order.** Read sections 1–3 before acting.
This is the LAW INDEX: every rule = imperative + mechanism + pointer. The full annotated text behind
every rule (incidents, measured numbers, history) is `docs/doctrine/CLAUDE_ANNEX.md` — cite it when
a rule's reasoning is contested. Startup mechanics: `org/XXX.md`. Also when you talk to another agent,
*YOU MUST REFER TO THEM BY FULL SERIAL; NEVER SAY HER/HIM/THEM/YOU WHEN COMMUNICATING WITH OTHER AGENTS!*

⛔ **RULE NUMBERS ARE STABLE IDs, NOT READING ORDER** — the list has gaps; sections carry the order.
Rules 4–12, 18 live in `/cloud-ops`; rules **15, 17, 17a, 17b** (data architecture) and **19, 23,
25, 26** (portal/SES/dormancy/apply-locality) live in `docs/doctrine/CLAUDE_ANNEX.md` — numbers
stable, citations resolve there. DS/AE seats read their sections before touching those surfaces.

---

## 1. HOW WE WORK

27. **Every directive/project runs the CANONICAL WORKFLOW L1–L10, ONE OWNER PER STEP, IN ORDER: L1 brief
    (`4.0.0_SA_CRO` only) → L2 endpoint (`1.0.0_SA_CTO` only; ⛔ **NO FWD IS A WAIT** — every outcome is provable by
    an act a seat can take ON DEMAND, and one whose only proof is an event nobody controls is re-cut so its MECHANISM
    is driven deliberately, the organic case kept as the negative arm; a genuinely essential wait is EXPRESSLY
    QUALIFIED on the outcome with its reason and Andrew's word. Andrew-direct 2026-09-10: *"no FWD is ever a 'wait'
    unless explicitly advised otherwise ... sprint, execute, validate, and close"*. Measured the same night:
    `ETFS_GUARDRAIL` FWD-7 sat NOT_EVALUATED as "a real terminal failure, rare by design" while its send guard could
    not fire AT ALL — waiting would have waited forever) → L3 register (`1.0.0_SA_CTO` only, **AND THE CTO WRITES EVERY
    CARRIER ITSELF IN ITS OWN COMMIT** — the tree row, the generated index, the `DIRECTIVES.yaml` members line and the
    `MACROS.yaml` macro enum; `0.0.0_AB_MSTR` is PERMIT on the last two as an integrator fallback and HOLDS NO GATE OVER
    ANY OF THEM. Andrew-direct 2026-09-10 ~20:1xZ: *"anything from L2 up to the L5 handoff to COO for decomp needs to be
    able to be handled by CTO so we dont have this arbitrary mcp'ing"* — the round trip is retired; measured that night:
    five of five L2–L5 carriers were already PERMIT for the CTO and two IRPT projects sat unregistered across four seats'
    messages anyway, because the blocker was this sentence, not a lane) → L4 PRD (`1.0.0_SA_CTO` only — no COO, no CVO) → **L4-R SIGN-OFF GATE (spine v3.15): the PRD has TWO HALVES, each signed as a file
    in lane `TREE_PRD_SIGNOFF` bound to the HASH of its sections, never to `prd_version` -- `3.0.0_SA_CVO` signs the
    RATIFIED-TEXT half (ENDPOINT + CONTRACTS), always; `4.0.0_SA_CRO` signs the BRIEF half (everything else), or a live
    `2.0.0_SA_COO` not holding the round in its stead. The stamp is `python .tools/prd-signoff.py sign|refuse <CODE>
    --half ... --review <path>@<pin>`; `status <CODE>` is the one read of what is owed. The L4 notifier delivers each
    half still owed to its routed reviewer, WITHHOLDS the COO delivery until both are SIGNED at the current bytes,
    nudges an OVERDUE half after 60 minutes with the CTO copied, and re-routes an overdue brief half to a live COO;
    `.tools/to-pipeline-gate.py` LIMB 6 REFUSES a **NEWLY-ADDED** task order against a PRD with a half
    not SIGNED. ⛔ **IT DOES NOT FIRE ON A MODIFICATION, AND THIS LINE USED TO SAY SO WITHOUT THE
    QUALIFIER -- SO THE LAW READ STRONGER THAN THE TOOL BEHAVES AND THREE SEATS INHERITED THE BELIEF
    FROM IT IN ONE EVENING.** The gate's own docstring (`_newly_added`, `:1015` @cd399d339d) is explicit, AND
    IT NAMES THE EXCEPTION ITSELF: *"A rename (R) counts as added at its new path ... A
    modification (M) does not: no limb that reads THIS set refuses an existing TO. The ONE limb
    that grades a modification -- GATE (viii) ... -- reads its own set, `_staged_modified()`, so
    this set's contract is unchanged."* ⚠ **THIS LINE QUOTED THAT DOCSTRING AS SAYING "this gate never
    refuses an existing TO" UNTIL 2026-09-14 -- A CLAIM ABOUT THE WHOLE GATE, WHERE THE SOURCE
    SCOPES IT TO THE LIMBS THAT READ ONE SET AND THEN NAMES (viii) AS THE EXCEPTION.** The line
    number and the vintage were both CORRECT, so every citation test passed; only the QUOTED
    BYTES were stale, and they denied an exception this same rule states four sentences later.
    ⛔ **A CITATION AGES SEPARATELY FROM THE TEXT IT QUOTES** -- re-reading the rule catches
    neither. ⛔ **AND SEARCHING FOR A QUOTE IS NOT CHECKING IT: PRINT THE BYTES AT THE CITED
    LINE.** A rewritten passage does NOT delete its own old words from the file -- they survive
    in the comment that quotes them. Measured at BOTH vintages: the superseded phrase *"this
    gate never refuses an existing TO"* occurs exactly ONCE in `to-pipeline-gate.py`, at
    `:374` of 2072 @`cd399d339d` and `:377` of 2764 at HEAD, **inside a comment quoting the old
    docstring, closing quote mark and all** -- while the live text sits at `:1019` / `:1706`.
    **So a reader who greps the file to verify this rule's quote gets ONE CLEAN HIT IN QUOTATION
    MARKS and concludes the law quoted accurately.** The search confirms the wrong object.
    Found by `2.0.0_SA_COO~Z`, which ran it as a NEGATIVE control expecting ABSENT and got
    TRUE. COST: one `cat-file -p | sed -n '<line>p'` instead of a grep. NON-APPLICATION: a
    citation with no quoted text -- there is nothing to stale. Found by `2.0.0_SA_COO~Z`
    (`POSN_ASTTAX-Z-S61` @`2299206da6`) on the SAME class one level down, in a loop body citing
    a bare `:809-831` that now lands on gate (viii)'s own self-test table. Measured 2026-09-11 by `2.0.0_SA_COO~ZZZ` as a discriminating pair on
    ONE project in ONE hour: the add path refused its new order **three times** (missing
    `<issued_by>`, missing `<preflight>`, then the preflight's line shapes) while **ten task-order
    MODIFICATIONS went ungraded.** ⚠ **SO ON A RE-CUT OR A MID-FLIGHT AMENDMENT, "do not cut against
    a stale half" IS A HUMAN DISCIPLINE, NOT A GATE** -- and the sharpest exposure is not the signed
    half at all: a modification can change a criterion's grammar, a `<paths>` grant, or the inlined
    cell text of a face **a worker is reading at that moment**, and the worker never sees a refusal.
    The prospective-only scoping is Andrew's own (`:21`), and he has widened it EXACTLY ONCE, by card:
    **GATE (viii) -- the `<placeholders>` declaration -- ALSO grades a task order staged as MODIFIED when
    that order ALREADY DECLARES `<placeholders>` at HEAD** (Andrew-direct card 6, ~18:4xZ 2026-09-13, *"recs
    approved"*, record @e2210bf34c; built as `IRPT_FNTEND` FE-s-29 limb 4, drained @cd399d339d; gate docstring
    `:24-30`). Nothing is back-filled, LIMB 6 and every other limb stay NEWLY-ADDED only, so the human discipline
    above still binds every modification except that one element's; any further widening is HIS call and is
    carded, not assumed. One rule for all
    three: `.tools/prd_signoff_lib.py`. Andrew-direct 2026-09-10 ~21:2xZ: *"CRO and CVO should have to sign off on
    PRD before COO gets it"*; 2026-09-11 ~05:3xZ: *"CVO should always be included. If CRO is not online, can do COO
    in their stead"*. Measured 2026-09-10/11: thirteen PRD versions in one night, a half re-signed three times
    unchanged under the version-bound rule. COST: two reads per CHANGED half. NON-APPLICATION: a header-only bump
    re-opens nothing; an L10 addendum re-opens only the half it changed** →
    L5 decomp + battery → L6 ONE ISSUANCE covering EVERY cell (`2.0.0_SA_COO` only; fan-out derived from the
    decomp's dependency chains and stated as `fanout:` data in the issuance commit, default cap 8) → L7
    execute (WORKER SUBAGENTS of the COO, `0.9.0_WK_<CODE>~<n>`, one worktree each, NO send tool; the TO's
    WORKER FACE is the worker's whole context — cell text, absolute paths, ONE clause per criterion with its
    invocation and expectation; the RECORD FACE never travels; a compound criterion is refused at the cut) →
    L8 compile (**`3.0.0_SA_CVO`, AND ITS ENGAGEMENT WITH THE PROJECT BEGINS HERE, NOT AT L9** — spine
    `:320`, `:475` and `:489`, three places; this line said "L9, its FIRST engagement" until 2026-09-10 and
    ⛔ **THAT WAS THIS RULE CONTRADICTING ITS OWN SOURCE.** ⚠ AND THE SPINE'S L8 IS THE **CHANNEL** COMPILE
    — input "new investigation rows … and no others", output the compiled channel and the CVO's watermark.
    The task-order packet the COO produces at drain-end is a **DIFFERENT ARTIFACT SHARING THIS LABEL** and
    the spine does not name it; that ambiguity is PLACED, not resolved, and no round changes owner on it) →
    L9 adjudicate (JUDGMENT criteria are graded HERE and
    never self-graded) → L10 ONE SLUG to the CTO, ALWAYS, only after every TO is terminal and every row
    dispositioned; ⛔ **AND THE L10 ORDER -- slug -> the CTO's ROUND-N ANALYSIS -> the COO's recut --
    IS LOAD-BEARING, NOT STYLISTIC. A ROUND N+1 ISSUANCE CUT BEFORE ROUND N's SLUG DEADLOCKS ROUND
    N's L10 UNTIL N+1 FULLY DRAINS**, because the refuser counts open orders PER PROJECT and never
    per round (LD-0521). Measured 2026-09-11 on AMGT_RESAPP, by the seat that did it: round 6 was cut
    straight off the L9 adjudication at 22:24Z, flipping `rd-8` superseded and opening `re-1` staged
    IN THE SAME COMMIT -- so the open count never reached zero, and `3.0.0_SA_CVO~Z`, already
    correctly gated and having NAMED `rd-8` as its blocker, silently acquired a different one. ⚠ The
    cost lands on ANOTHER SEAT and is invisible to the one that caused it; the CTO answers with a PRD addendum (an FWD no cell served) or the ROUND-N ANALYSIS the
    COO recuts in ONE issuance; CLOSED when every FWD grades REALIZED.** The three route tokens are RETIRED.
    Three tracks share FILES, never messages: the CVO's one send is the slug, the CTO's one send is the
    analysis, a worker cannot be messaged. `0.0.0_AB_MSTR` integrates and never works a project. Mid-round
    the spec AND the decomposition are FROZEN; the only off-spec act is a surprise ROW (§2 below).
    ⛔ **ONE ISSUER PER ROUND — and a WORKSTREAM IS A SCOPE, NOT A ROUND.** L6's ONE ISSUANCE is cut by ONE
    COO instance; two instances issuing into the SAME round is the collision (two cuts, two issuances, an
    ambiguous L8). ⛔ **It binds the ROUND, NEVER THE PROJECT: one project may carry several WORKSTREAMS with
    DISJOINT boundaries and DISJOINT write surfaces, held by different `~lane` instances** — that is four
    SCOPES, not four issuers. ⛔ **AND A SEATING RULE DOES EXIST — AT TIER 2 ONLY. DO NOT READ THIS CLAUSE AS
    "NO SEATING CONSTRAINT."** `ONE PROJECT PER TIER-2 SEAT INSTANCE` (Andrew-direct 2026-08-24 ~19:29Z,
    protecting THE SEAT'S CONTEXT, not the box) is REAL, is ENFORCED by `.tools/to-decomp-ref-lint.py`'s seating
    check, and that enforcement is LEGITIMATE — it refuses a new TO addressed to an instance already holding open
    TOs on another pipeline project. **What was never real is its GENERALISATION TO ALL TIERS:** the phrase
    "one project per instance" DROPPED "TIER-2" and circulated for weeks citing THIS rule by number, and on it a
    TIER-1 seat twice declined to seat a TIER-1 lane. ⛔ **ASKED AND ANSWERED — IT DOES **NOT** REACH TIER 1.**
    Andrew-direct 2026-09-10 ~17:3xZ, VERBATIM *"One project per COO/seat."*, answering the direct question
    *"does the one-project-per-seat rule extend to Tier-1 lanes?"* — he named the **COO**, a TIER-2 seat.
    **So the rule binds at the TIER-2 SEAT INSTANCE, exactly as the lint already enforces, and NO TIER-1 LANE
    IS CONSTRAINED BY IT.** A Tier-1 seat may hold several projects and may seat several Tier-1 lanes.
    Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_173xZ_SEVEN_OPEN_CALLS_ANSWERED.md`.
    ⚠ The recorded read is the NARROW one and is stated as such in that record; his sentence admits a wider
    one, and taking the wider one silently is the exact widening that created this question. COST: none. Measured
    2026-09-10 by `2.0.0_SA_COO` and `0.0.0_AB_MSTR`, each correcting its own prior answer: **both first censused
    "documents that STATE law" and got ZERO, because the rule lives in an ENFORCEMENT SURFACE and an
    Andrew-direct — neither is a law file.** The wider census (799 files) was not wider in the direction that
    mattered. ⭐ **AN UNSCOPED READ ONLY FALSIFIES A DOMAIN IF YOU THEN INSPECT WHAT IT FOUND OUTSIDE IT** — the
    390 unscoped hits included `.tools/`, and nobody looked.
    COST: none — this names what "ONE ISSUANCE" already implied. NON-APPLICATION: separate rounds; and
    workstreams whose write surfaces do not intersect. Gate:
    `.tools/to-pipeline-gate.py` (the L6 neck). Spec: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`
    — the ONE process document (constitutional; v3 from the CRO's spec @`29bf9265ea` + §13 @`9dc97d860d`).
    ⛔ **NO VERSION IS PINNED HERE, DELIBERATELY. CITE THE SPINE BY PATH AND READ IT AT HEAD.** This line
    pinned `v3.2` until 2026-09-10 while the spine's own ladder had reached **v3.13** — ELEVEN amendments,
    TWO of them authored by this seat the same day it was still citing v3.2. **A constitutional pointer
    carrying a version number is a promise to do maintenance nobody remembers, and it is UNFALSIFIABLE AT A
    GLANCE precisely because the number looks authoritative.** Un-pinning makes the staleness structurally
    impossible rather than merely corrected. **The catch and the remedy are `0.0.0_AB_MSTR~Z`'s** (site Z's
    Rule 27 rewrite); it did not survive the 2026-09-10 merge, which took this fabric's side, so it is
    re-landed here on its own merit. ⚠ **WHERE THIS RULE AND THE SPINE DIFFER, THE SPINE WINS AND THIS RULE
    IS THE DEFECT** — Rule 27 is a REPRESENTATION of `/canonical-flow`, never an independent source.
    A worker's write surface is exactly the `<paths>` its non-terminal order names (no lane enumerates a worker;
    `.tools/owned-paths-validate.py`), its rows mint `<CODE>-W<n>-S<k>`, and it writes no telemetry (L7 reads from
    git). ⚠ The eight v3 carriers are BUILT and refuse (spine §3), and so is the drain's refuser on the merged index
    (`.tools/safe-merge.sh`); what still binds by reading is spine §4 — the step log's L7 read from git.

## 2. HOW MUCH TO CHECK — the speed governor

⛔ **VERIFICATION SCALES WITH THE COST OF BEING WRONG. WHEN THE NEXT CHECK WOULD NOT CHANGE WHAT YOU DO,
STOP.** Most work checks nothing; an unneeded check burns the context the high-stakes judgment needs
later — a CORRECTNESS cost, not a speed one.

22. **EVIDENCE LAW — four axes; who eats the error decides how many you check.**
    | If being wrong costs… | Ask |
    |---|---|
    | me, this turn | nothing. Act. |
    | me later, or another seat | **GRAIN + COVERAGE** |
    | the record (commit, message, TO, report) | **+ STATE** |
    | the world (deploy, delete, grant, served key, claim to Andrew) | **+ DISCRIMINATION** |

    **GRAIN** — the object read IS the object claimed, at the level and vintage claimed. **COVERAGE** —
    evidence spans the claimed set; PRINT THE DENOMINATOR. **STATE** — DESIRED ≠ APPLIED ≠ EXERCISED; a
    description is never a state. **DISCRIMINATION** — could the evidence differ if the claim were false?
    ⛔ **The ORDER is the mechanism: DISCRIMINATION passes inside a wrong GRAIN/COVERAGE/STATE** — every
    instrument then agrees about the same wrong thing. ⛔ **A second seat's confirmation via the FIRST
    seat's method is REPETITION, not corroboration** — name your instrument and whether it differs.
    ⛔ **A CHECK SCOPED TO THE MEMBERS CANNOT SEE A DEFECT IN WHAT THE MEMBERS SHARE.** Verifying each
    member of a set certifies the set CLEAN while a shared dependency beneath it is broken — and every
    per-member arm passes, so nothing fails. **Ask what the members have in COMMON, and check THAT on
    its own; then re-read the population UNSCOPED once.** COST: one extra unscoped read after a scoped pass. NON-APPLICATION: members with
    no shared dependency, and a scoped check that IS the whole question rather than evidence for a
    wider one.
    **"proof / root cause / definitively / source-confirmed" are RESERVED** — legal only past STATE at
    EXERCISED; cite `file:line @ <commit-ish>` (a citation without a vintage is not a citation). It
    governs SUPPLEMENTARY controls, never the substance of the act; size by the claim your work FEEDS;
    re-derive with a DIFFERENT instrument or cite the peer's — never re-run the same command.
    Catalogue: `docs/doctrine/CONTROLS_OVER_CARE.md`.

⛔ **FOUND SOMETHING ODD OFF-TASK? Do NOT halt-and-investigate — APPEND ONE ROW (`spec_asserts` + `world_is`)
to the project's surprise channel and KEEP WORKING. A broker message is NEVER the carrier** (a notifier watching files cannot see an inbox). Tree project: `org/missions/D*/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v{N}.md`
or legacy flat `org/surprise_channel/<CODE>/INVESTIGATION_v{N}.md` — BOTH lane ANY:
the seat that sees it appends its own row; REMEDIATION rows stay CVO's. An ARMED hazard still disarms same-turn via the row's
`disarm_owner`. Gates: `.tools/surprise-row-gate.py` (the row, at commit) + `.tools/proof-of-spec-check.py`
SURPRISES LIMB (a `surprises` entry with no resolving row id blocks a tree TO's `complete` flip).
`docs/doctrine/THE_SURPRISE_CHANNEL.md`.

⛔ **DO NOT MANUFACTURE FRICTION:** (a) **NEVER implement an approval gate on any work unless Andrew
explicitly asks** — an agent-made gate is invisible to him (pre-existing mechanical gates stand; proposing
is legal, implementing is not); (b) **NEVER convert Andrew's word to ONE agent into a gate/stop on
another** — verbatim scope; relay, never adjudicate wider OR narrower; if wider seems plausible, ASK.
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260804_1827Z_NO_INFERRED_GATES_NO_SHADOW_PIPELINES.md`.

## 3. FINDING THINGS FAST

21. **`comp-which "<plain-English question>"` is the reflex; a comp-tool is the DEFAULT for search +
    inspection, raw grep the exception** (text-local, connection-blind). ⛔ **EVERY standalone repo search
    in Bash — `grep/rg/egrep/fgrep/findstr/ack/ag` recursive or directory-scoped, `find` with anything — is
    DENIED per SEGMENT (`&&`/`;`/newline split) and routed to `comp-find`; raw-`aws` INSPECTION is classified
    on ITS OWN SEGMENT.** Mechanism: `.tools/hooks/comp-tool-hud.sh` (kill switch `org/mcp/comprail-gate1.enforce`;
    ⛔ **A RAIL DENIAL ABORTS THE WHOLE BASH CALL, so every LATER SEGMENT is a SILENT NO-OP.** A denied `grep`
    segment in a compound call does not just lose that segment -- the status flip, the write or the commit chained
    after it never runs, and nothing says so. Only a VERIFY-AFTER-WRITE catches it. Put a gated read in its OWN
    call, or verify the later segment's EFFECT rather than its exit. Measured 2026-09-10 by a worker whose
    believed-completed status flip had not happened. COST: one extra call, or one read-back. NON-APPLICATION: a
    single-segment call.
    falsifier `.tools/comprail-gate1-fptest.sh`). NOT gated: a pipe-RECEIVER grep (`cmd | grep`),
    `# rail-checked: <why>`, `/freeform`, native `Grep`/`Glob`, `Read`, operational `aws`. `comp-grep` is a
    forwarder onto `comp-find`.
    ⛔ **A SINGLE-FILE GREP ROUTES TO `comp-read`.** `comp-read <file> --for "<question>"` returns the file's
    SHAPE, regions tagged AUTHORITATIVE-vs-DESCRIPTIVE, every QUALIFIER that limits/negates/corrects a nearby
    claim, intra-file CONTRADICTIONS, and an UNREAD LEDGER; `comp-read <file> --enumerate '<regex>'` prints its
    DENOMINATOR, bands hits (DOCSTRING/COMMENT/DEF/CODE), separates WHOLE-VALUE from SUBSTRING, and WARNs when
    every hit is a fragment — a count is not a reason to reach for `grep`. **NON-APPLICATION:** `grep -q` as a
    pure predicate; any pipe-RECEIVER; FILES OUTSIDE THE REPO CORPUS (a transient tool log, a `/tmp` run output,
    a scratch file — grepping one is NOT off-rail); WRONG-OBJECT errors (comp-read cannot tell you that you
    handed it the WRONG FILE). ⚠ **MECHANISM IS DESIRED-NOT-APPLIED until `comp-tool-hud.sh` changes:** the
    single-file carve-out is live at `:138`/`:141`, `:155-156` and `:182`; until those route to `comp-read`, this
    clause binds agents by reading and nothing by enforcement.
    Traps before quoting any comp-find number (case, substring, denominator certifies the SWEEP not
    the pattern): `docs/architecture/NFRA_COMPRAIL_PRD.md`.
    ⛔ **Never `head` ANY census — `comp-find` OR A RAW GREP.** Use `--band HEAD/DEF`, `--files`,
    `--limit/--page`, `--all`, and `-i` for any token census.
    ⛔ **A PAGE IS NOT AN ANSWER; never conclude from page 1.**
    ⛔ **Do not stop at the first plausible hit** — an early stop and a true absence read identically.
    ⛔ **SCOPED COVERAGE QUALIFIERS: the corpus is `.gitignore`-BOUNDED, NOT tracked-only** — **the DEFAULT is
    `all`** = tracked + untracked + gitignored minus a PRINTED ephemeral floor; `default` = tracked +
    untracked-not-ignored; `ignored` = only-gitignored MINUS the same printed floor; `raw` = everything (an
    every-file denominator uses `raw` — `all` AND `ignored` understate by the floor, disclosed on their own
    denominator lines). comp-find is REPO-ONLY by ruling (a pathspec outside the worktree is not a zero, it is
    `git rc=128`) — **except `--corpus aws`: the LIVE AWS plane** — regex over every aws CloudNode's
    name+arn+props, pathspecs = node_type filters, `drift_class` per hit (`LIVE-no-DECLARED` = in AWS, not in
    the repo), denominator = nodes scanned, vintage = the DB's own `built:` line. **`--hidden <path>` is the
    census verb: run it before converting a zero into an absence, and `0 hit(s) across 0 file(s)` IS
    OUT-OF-CORPUS, NOT ABSENCE.**
20. **Check the dependency graph BEFORE any cloud/infra/data change and before frontend commits** — pick
    from `org/modules/graph/graph-call-manifest.yaml`; QUERY, never rebuild; read the provenance header;
    verify your OWN fresh change against live artifacts, never the graph. `comp-surface-check` is RETIRED
    (no commit-time guard on MP/benchmark/ADVI). `docs/architecture/NFRA_GRAPHS.md`.

## 4. CLAIMS AND SCHEMAS

**THE BUILD LADDER — new code is the LAST resort, in order:** (1) YAGNI; (2) the estate already has it —
`comp-which` for code, `comp-estate --layers/--definitions` for infra + ratified terms; (3) stdlib;
(4) native platform feature; (5) already-installed dependency; (6) one line; (7) only then the MINIMUM
code that works. **No non-ASCII in production code/logs/AWS** — use `OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`.
⛔ **AND IN A FILE THAT ALREADY CARRIES MANY, DO NOT DELETE THE ONE GLYPH THAT MAKES A NAIVE READ
RAISE — IT IS THE ONLY THING STOPPING SILENT CORRUPTION.** A default text-mode read on this device is
cp1252, which raises ONLY on a byte undefined there (`0x81 0x8D 0x8F 0x90 0x9D`); every other
non-ASCII character decodes to the WRONG character and reports success. Measured 2026-09-14 on the
three files every seat reads at startup: `CLAUDE.md` 213 non-ASCII, `org/XXX.md` 138,
`docs/doctrine/CLAUDE_ANNEX.md` 252 — **each raises because of a SINGLE `U+2B50`**, and removing just
that glyph leaves 212 / 135 / 251 characters that decode CLEAN AND WRONG. **Deleting it converts a
loud failure into silent mojibake, which is strictly worse and looks like compliance.** So the only
two safe moves are ALL non-ASCII out, or every reader explicit (`encoding='utf-8'`) — **never a
subset.** ⭐ Detector, one expression and zero cost: `len(b) - len(b.decode('utf-8'))` is 0 on a pure
ASCII file. **COST: none — a do-not-do.** **NON-APPLICATION: a file that is ALREADY pure ASCII (keep
it that way), and any file whose every reader is known explicit.** Measured beside it: 29 of 91
`.tools/*.py` carry non-ASCII (8 raising, 21 silent) and `.owned-paths.yaml` — the LANE-GRANT file —
is in the SILENT class at 204. `2.0.0_SA_COO~Z` / `2.0.0_SA_COO~ZZZ` / `0.0.0_AB_MSTR~Z`, corroborated
on three instruments.

⛔ **A VALUE MUST CARRY ITS CLAIM — in a field a consumer can reject on** (`measured/inferred/held/absent`);
no such field → you may NOT treat it as measured. **The consuming half is the whole mechanism** — an
unenforced provenance field drifts to unpopulated. `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`.

24. **TAXONOMY LAW — four postulates for ANY schema an agent authors or ADOPTS:** (i) MECE over a DECLARED
    domain (hunt the uncovered member); ⛔ **AND HUNT IT BY SUBTRACTION, NEVER BY RECALL: write the
    enumeration as *the printed denominator MINUS what you exclude*, never as a forward list of what you
    thought of.** A forward list covers what its author had in mind and omits silently; the same set written
    as a subtraction from a denominator cannot lose a member without the count disagreeing. COST: one
    denominator read. NON-APPLICATION: a set whose members are the literal argument you were handed.
    ⛔ **AND THE SUBTRACTION'S DOMAIN MUST BE THE CLAIM'S POPULATION — CHOOSING THE DOMAIN IS ITSELF A CLAIM,
    FALSIFIED BEFORE THE SUBTRACTION RUNS:** one UNSCOPED read of the term over the corpus, denominator
    printed, compared against what the domain holds; a member the domain does not hold VOIDS the subtraction.
    A subtraction over the wrong domain is BLINDER than recall — it arrives with a printed denominator and so
    reads as MEASURED, and **a denominator certifies the SWEEP, never the SET.** ⛔ **THE FAILURE MODE IS A
    GREEN:** a wrong domain returning NON-EMPTY gets argued with; returning EMPTY it gets ACTED ON. Measured
    2026-09-10, `NFRA_CLDGRPH` W1-S38: a retirement's authorizing census read 0 of 78 over the declared
    manifest while the unscoped read over 31,293 files found FIVE live consumers — the empty set WAS the
    authorizing branch, surfaced only because the seat being graded ran the read nobody asked for. COST: one
    unscoped read with its denominator. NON-APPLICATION: a domain that IS the corpus (nothing was narrowed).
    Measured 2026-09-10, FIVE instances in one night across five seats: `NFRA_OUTSET`-S36; `NFRA_COMPEFFICACY`-W1-S2;
    a COO arm naming two partners of three; `ETFS_GUARDRAIL` row S16 doing the same inside an ACCEPT (so a
    GRADE would have read REALIZED on the violation); and a manual-trigger addendum that enumerated the
    outcomes it covered instead of subtracting from the outcomes that NAME a date, leaving `NFRA_OUTSET`
    FWD-5 uncovered. Found by `2.0.0_SA_COO`, which had committed the same shape an hour earlier. (ii) SAME GRAIN; (iii) INTENT COHERENCE (one axis, one intent);
    (iv) STATE COHERENCE (name which values one remedy does NOT move). **Outcome arrays, typed-result sets
    and predicates ARE schemas.** A value-enum proposal arrives WITH its four-postulate record + word-boundary
    token census, or it is not a proposal. `rcg/rulings/RULINGS.jsonl` R-0006/R-0009.
22a. **INSTRUMENT TRAPS you cannot re-derive at the call site.** CODE: diff deployed bytes against the
    BUILD INPUT (source-map/manifest), never by filename; a cherry-picked/ephemeral pin is resolved by
    CONTENT (`git show <pin>:<file>` + negative control), never `merge-base --is-ancestor`; running-bytes-
    older-than-built passes every rung. DELIVERY: SENT ≠ EMITTED ≠ READ — only an agent-side ACK is a
    sound oracle; an orphaned watcher reads REACHABLE *because* the agent is deaf (anti-correlated).
    RETRIEVAL: a failed retrieval returns a VALUE; paginated `list-*` + `--query length()` returns the
    PAGE count and `--no-paginate` is the hazard; `aws s3 ls` renders LOCAL time, `s3api` UTC; never type
    a literal `Z` into a `--date=format` (renders local, stamps UTC). IAM traps: `/cloud-ops`.
    **ROSTER: `get_agent_status(<serial>)` IS THREE LIMBS WITH DIFFERENT SCOPES.** Liveness / PID /
    `Working on` are per-LANE; ⛔ **`Pending task orders` and `Latest logs`/`Blockers` are BASE-scoped
    AND exact-string-match a FREE-TEXT `<status>`** -- so they are never a lane's orders and never a
    count of what is open. To ask what a LANE owes, parse `<issued_to>` from the order files. ⚠ **The
    one limb that needs no disclaimer carries one, and the two that do carry none**, so the careful
    sentence certifies the silent limbs. Measured 2026-09-14: 6 of 6 orders reported for
    `3.0.0_SA_CVO~Z` were lane `~Y`'s; across **2237** seat orders (88 folders, `.md` only -- a first
    count said 2278 by admitting 41 `.gitkeep`) **679** carry prose `<status>` and **75** carry none,
    leaving **31** open orders invisible -- exact-match PROVEN at
    `0.7.0_AE_CloudOps` (3 reported, 5 genuinely pending). **COST: none -- a reading rule.**
    **NON-APPLICATION:** the lane half does not bind a query on a BASE serial; the free-text half binds
    every query, base or lane. `AMGT_RESAPP-Z-S79`/`Z-S80` @`e1a4e917f2`. Annex §22a.
28. **THE SUBSTRATE TEST — before you BUILD ON a resource, card it: 7 questions, 3 grains** — PROCESS
    (1 methodology, 2 cadence/trigger DESIRED-vs-APPLIED), ARTIFACT (3 persistence/authority, 4 exact
    location), TRUST (5 coverage + denominator, 6 key/identity space, 7 failure mode distinguishable from
    a genuine negative). **Every row carries its OWNER** (remedies do not move together). Binds only when the resource becomes LOAD-BEARING;
    never card what you merely consult. Contract: `org/standards/SUBSTRATE_CARD.schema.json`. Annex §28.
- **NEVER** trust a producer's self-report or rc=0 — verify against the SERVED artifact / live state.

## 5. HARD STOPS (NEVER)

- **NEVER** move served output without never-widen sign-off (CTO+COO); verified DELTA=0 needs no hold.
  ⛔ **A SIGN-OFF NAMES THE ACT'S BLAST RADIUS, NEVER THE PRODUCER'S DECISION.** Both halves cover *what the act
  MAY touch and the rollback for each key*, so the act stays covered whichever branch the producer takes. Where a
  half names an EXPECTED OUTCOME ("the publish keys stay absent", "the keys will be dated tomorrow"), that outcome
  is READ FROM THE PRODUCER'S OWN RULE at signing — never predicted from the input's shape — and the half covers
  BOTH branches or it is not signed. ⛔ **AND FIRST COUNT THE WRITERS OF THE NAMED PROPERTY: a property with N
  writers needs N rules read, and N is a number the half PRINTS.** Reading one producer's rule on a two-writer
  surface is Rule 22's shared-dependency blindness moved up to the signature. COST: one writer census + one source
  read per named outcome. NON-APPLICATION: an act whose write set is a literal key list the actor controls. Measured 2026-09-09/10, THREE TIMES in one night, both halves
  signed every time: `NFRA_OUTSET`-S34 (the window comes from the schedule mark, not the calendar, so a "tomorrow's keys" run
  rewrote today's) and `ETFS_GUARDRAIL` EG-s-15 (a class-D hole is carry-and-disclose, not refuse, so a "will
  refuse" run published and mailed); and `NFRA_CLDGRPH` W2-S67/S98, where both halves read the FOLD's rule (the
  stamp writer genuinely retired, `stamped=0` printed) on a property a SECOND writer also set, so the served count
  did not move — the blast-radius half was correct and complete, and its own discriminator is what caught the miss.
  ⛔ **And a `--month`-style override that lets a scheduled producer run off its
  own clock CREATES A NEW REACHABLE STATE on the manual path: the sign-off covers that state or the override does
  not land.**
- **NEVER** leave a confirmed deploy half-landed — finish in-session or roll back + escalate loud; ledger
  entry in `org/critical_paths/change_management/` opened at start, closed at completion. **An IMAGE act (a
  build, a push, a tag move) names in that entry EVERY task family that pulls the tag it moves** — a shared
  `:latest` reaches every family at once and no Terraform-plane control can see it (NFRA_CLDGRPH-S31: two
  builds re-pointed seven families in one night, five counted); pin per family by digest where a family must
  not move. COST: one `describe-task-definition` sweep per image act. NON-APPLICATION: a tag no task
  definition references. ⛔ **An entry a
  device left OPEN proves only that THIS device saw no completion** — before acting on any open/`--red`
  entry, measure the ARTIFACT (rev-parse + describe + is-ancestor with positive control); world-done →
  close SUPERSEDED, never re-execute (a re-execute of an overtaken promote is a REWIND). Annex §NEVER-2.
- **NEVER rebase on a shared branch** (CLOUD/DEV/PROD/main); rejected push = pull-merge, re-push. Gate:
  `.tools/hooks/never-rules-gate.sh`; audited override `# never-override: <reason>`. Scratch branches free.
- **NEVER call a pipeline stale/broken until you resolve the TRADING CALENDAR — count trading days.**
  Everything is `T-1` unless declared; Friday IS Monday's answer. One frontier: `lib/trading_calendar.py`;
  a `comp-freshness` entry lacking `freshness_basis: trading-day-frontier` false-alarms every Monday.
- **NEVER stand up a shadow/build-alongside pipeline, duplicate output path, or standing parity
  comparator** (Andrew complete veto) — build correctly, port directly, same-window rollback; consolidation
  fine. `memory/feedback_no_shadow_channels_veto_build_correctly_and_port.md`.
- **NEVER build an alert/alarm/SNS/SES-send/notification/freshness-checker/monitor unless Andrew explicitly
  asks. Standing moratorium** — canonical routes FIRST; a monitor on an unsettled route measures the wrong
  thing precisely. Findings land as gates or owned blocking items. `docs/architecture/MDPF_DEBTCLEAN_PRD.md` §11–12.
- **Ad-hoc gold runs are PERMITTED FOR QA; production pipelines MUST be scheduled** — success-of-upstream
  as the only trigger is a defect; ad-hoc artifacts are never production evidence.
- **NEVER write device-specific logic into ajb_workspace/portal — DERIVE, don't hardcode** (workspace root
  → `git rev-parse --show-toplevel`; drive prefix → `test -d /cygdrive/c`). Legit only when device-ness is
  the code's PURPOSE. Direction ratified, remediation NOT authorized — surface, don't chase. `LD-0405`.
- **NEVER** bare `terraform apply` (use `safe-apply`), bare `git commit` (use `safe-commit.sh`), or
  `aws lambda update-function-code` (Terraform only). ⛔ Only the terraform limb is mechanically gated —
  the other two are imperatives enforced by nobody. Annex §NEVER-9.
- **NEVER** reference another firm's data from a pipeline tree — **BUCKET *or* KEY-PREFIX**. ⛔ **THE
  MECHANISM IS SUBSTRATE-SHAPED AND BOTH SHAPES ARE LIVE:** shared bucket → key-prefix + IAM condition;
  per-firm buckets → bucket-scoped Deny. **An enumerated ban list lapses SILENTLY when a name changes**. Gate: `.tools/ds-precommit-check.py`
  `_CROSS_FIRM_FOREIGN_{BUCKETS,KEY_PREFIXES}` — **the guard is only as wide as its enumeration, so a
  new firm name is a GATE EDIT, not just an infra act.** ⚠ IAM limb: **DESIRED, apply UNVERIFIED**.

## 6. LANE + COMMIT MECHANICS

13. **DS owns commit→QA-deploy for `data/*/scripts/{gold,silver,bronze}/*.py`** incl. `aws s3 cp`; DT/AE =
    infra/PROD-triggers/multi-pipeline. Enforced by `.tools/safe-deploy.sh`; shared homes deploy under the
    S3-membership guard (404 = loud skip, first-mints explicit). **cot is a separate firm from bd — never
    mirror/sync.** `docs/architecture/ADHC_DSFLOW.md`.
14. **Every `.py` edit passes `.tools/commit-gate.sh`** (py_compile + ds-precommit + ruff py39). Universal.
14a. **Commit via `.tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -F <msgfile> -- <paths>`;
    do NOT pre-`git add`; `-F` not `-m`** — and the message file must be written by a NON-SHELL writer
    (Write tool / python): a `printf`/heredoc-built file re-opens the injection one step earlier. `--force`
    bypasses only contamination checks, never a lane refusal — that escape is `GIT_COMMIT_AUTHOR_OVERRIDE=
    <LANE>`, audited, SINGULAR (N lanes = N commits). `docs/architecture/ADHC_OWNPTH.md`.
14b. **While other seats are LIVE, commit anything bigger than a one-file edit in YOUR OWN linked
    worktree and merge it back in a gap** — five seats plus their worker subagents share ONE MUTABLE
    INDEX, so the check-then-act window is now shorter than the staging cadence: `2.0.0_SA_COO` measured
    `staged=0` and had the very next merge refuse on a file staged in the seconds between. Mechanism:
    `git worktree add ../<slot> -b <branch>` — a linked worktree carries its OWN index AND its own merge
    state, which is why `/dispatch` already mandates one per worker slot; merge back with
    `.tools/safe-merge.sh` (its `--continue` limb keeps a conflicted drain inside the guards).
    ⛔ **THE GUARDS ARE NOT THE PROBLEM — every refusal measured so far was CORRECT and each prevented a
    real sweep** (`org/git-author-override-audit.log`: 3 audited `MERGE-REFUSED`, 2 on `2.0.0_SA_COO`
    and 1 on `1.0.0_SA_CTO`, each naming a FOREIGN MERGE_HEAD and `nothing staged by this run`). Only
    those three are offered as contention evidence: two further refusals the same evening were traced by
    their own author partly to itself, and a self-inflicted block is not a crowding measurement.
    The refusal RATE rises with the live-seat count, and a correct refusal you could have avoided still
    costs a retry and sometimes a round trip.
    ⛔ **IT INVERTS FOR AN APPEND-ONLY SHARED FILE AND YOU MUST NOT ISOLATE THERE** (`2.0.0_SA_COO~A`,
    accepted by `2.0.0_SA_COO` without reservation): two branches appending to one channel land at the
    SAME OFFSET and both restate the header, so a side branch converts a SECONDS-LONG STAGING RACE into a
    GUARANTEED CONFLICT — measured 3 of 3 on round 4's drains (NFRA_CLDGRPH-S36). Trading a probabilistic
    race for a certain conflict is a bad trade, and the conflict path is the one that cost this estate a
    hand-finished merge with neither guard running. So:
        a file only YOU touch          -> ISOLATE (a worktree costs 30 s and touches nobody)
        an APPEND-ONLY SHARED file     -> DO NOT ISOLATE; take the shared index's seconds-long race
        (a surprise channel, a log)
    ⛔ **AND EDIT IN THE WORKTREE WHERE YOU WILL COMMIT.** Copying an edit out to a branch leaves the
    original behind in the shared tree as a blocker against your OWN merge ("local changes the merge would
    overwrite"), and it reads exactly like another seat's contention until you read the refusal text.
    `2.0.0_SA_COO` traced two of its own four "contention" instances to precisely this and said so.
    COST: one `git worktree add` plus a merge back. NON-APPLICATION: a trivial one-file commit; a seat
    working alone; an append-only shared file (above); and any commit that MUST be graded against the
    shared index (a drain — that is what `safe-merge.sh` grades). Found by `2.0.0_SA_COO` 2026-09-04
    after it and `0.0.0_AB_MSTR` hit the same contention from opposite sides within minutes and chose
    opposite remedies, both defensible — which is the tell that the contended RESOURCE, not either seat,
    was the problem.
16. **Local bash = Git Bash 3.6.7 default utilities only** (no pgrep/pkill/flock/pidof/setsid/wget without
    guarded fallback). `.tools/jq.exe` is vendored — resolve it first, fail closed loud. ⛔ **Never
    `2>/dev/null` a read whose EMPTINESS carries a verdict.** `docs/architecture/ADHC_BASHFIX.md`.

## Agent Autonomy

**Do NOT ask permission** to read/write/build/test/commit/push CLOUD-DEV/run scripts/call Opal-owned APIs.
**Excluded: all egress off Opal infrastructure.** Human confirmation ONLY for: recursive deletion,
destructive git, dropping tables/S3 deletes, stopping EC2, anything unrecoverable.
- **NEVER call an external vendor API without Andrew's explicit per-use word** — availability is not
  authorization. `memory/feedback_availability_is_not_authorization_vendor_egress.md`.

**NEVER self-wind-down, never default to "tonight"** — drive every addressable task NOW; wind-down only on
Andrew's word. **"Waiting for the scheduled run" is the same coast-failure** — fire the ad-hoc QA run (it
tests; the scheduled fire stays the acceptance); the one exception is when the ad-hoc would destroy the
discriminator the scheduled run exists to produce — name that evidence or the wait is the defect.

29. **A REPORT IS NOT THE DELIVERABLE WHILE UNBLOCKED WORK REMAINS — the turn ends when the WORK does.**
    The tell: a forward-looking closer ("cutting the TOs now"). Gate before ending ANY turn: *"is there an
    act this turn said it would do that it has not done?"* — yes + unblocked → do it, report after.
    Ending on a report is CORRECT only when the next act is blocked/gated/out-of-lane — SAY WHICH. Cost
    zero: the rule reorders a turn. `LD-0461`.

## Detailed Documentation

Deploy protocols `docs/deployment/` · graph `docs/architecture/NFRA_GLOBGRPH_PRD.md` · critical surfaces
`org/critical_paths/README.md` · start guide `org/XXX.md` · **Bloomberg, ANY scenario: READ
`integrations/bloomberg/READ_HERE.md` FIRST** (two-phase budgeted sign-in; a refusal names the SURFACE;
derived layer is current-day-only; never mint `data/bloomberg/`).

## Git

- Working branch `CLOUD`; portal submodule `DEV`/`PROD`. Shims reach shells via `~/bin` FORWARDERS (profiles
  never load): on WARN run `bash .tools/provision-path-shims.sh`. AWS via the `.tools/aws` shim (+`aws.cmd`,
  both or neither); never bare `MSYS_NO_PATHCONV=1 aws`.
- `MSYS_NO_PATHCONV=1` only for TF imports/ARN args and `git show <ref>:<path>` with a slashed ref; NEVER
  for `git push`/`safe-apply`. **Never `2>/dev/null` a `git show`** — the mangle returns clean-empty; run a
  positive control beside any ABSENT verdict.
- Python/PS shelling to bash → `.tools/git_bash_resolver.py`; Python spawning ANY MSYS binary →
  `.tools/msys_argv_guard.py msys_safe_run()` — never bare unix names in argv. Corruption oracle: echo the
  argument back.
- **Put the control on the RETRIEVAL:** outputs don't carry their own frame — print the denominator beside
  the number; paginated `list-*` auto-paginate then count client-side; name the QUESTION'S plane before the
  sweep's (no control inside the wrong plane catches a wrong-plane error; authorship is not evidence).
- **A commit message is an EXECUTION VECTOR** — `-F <file>` authored by a non-shell writer; `-m` deprecated
  for any body with special characters. `LD-0276`.
- **NEVER compose a report of a COMPLETED act in the SAME tool call as the act — read the number, then
  write the sentence.** Does not bind the `safe-commit -F` message file (atomic by necessity). Envelope
  sibling: verify a substantive send by `wc -c` on the delivered file.
- **Never "you/your" about a specific seat in a multi-recipient message — name the serial + msg-id**
  (second person resolves per reader).
- ⛔ **"Queued if not live" is a WISH, not a delivery. A BASE serial with no base session is a silent
  hole** — an inbox is a per-recipient slice, so mail to a base while only LANES are live gets no bounce,
  no ack and no staleness signal, and reads as delivered. Address a LIVE recipient, or PARK the item on
  its own carrier with an OWNER and the CONDITION that un-parks it. Measured 2026-09-10: five messages,
  all from one seat, unread in `0.7.0_AE_CloudOps` for 6-9 days across a device crash; two carried live
  scope decisions that were neither working nor waiting.
- **A commit report states its PUSH STATE as a MEASURED value:** "on origin @hash (ls-remote read)" ·
  "LOCAL @hash (ls-remote read)" · "push state UNREAD" — never a default; the claim is perishable and ages
  the moment an integrator runs.

## Portal

- `portal/` — `bun install && bun run dev --port 5175`; resolve bun via profile, don't bake a path.

## Changing this file

**A rule = imperative (≤2 lines) + mechanism + pointer — gates teach at violation time; prose taxes every
session.** A new verification rule STATES ITS COST AND NON-APPLICATION or it does not land (without that
clause the file only ratchets). **A law edit has THREE surfaces: commit + same-turn MCP broadcast to live
seats + push state stated in the broadcast** — the commit fixes the record, only the broadcast fixes the
fabric. **Where things go:** imperative+mechanism → here; principle → `docs/doctrine/`; what happened →
`docs/references/`; session mechanics → `org/XXX.md`; decision → `org/tier0/ledger/`. **Never cut a
MECHANISM to save space — but the incident that taught it is not the rule**; a principle earns its place by
being actionable WITHOUT its incident. Long-form text of any rule: `docs/doctrine/CLAUDE_ANNEX.md`.
