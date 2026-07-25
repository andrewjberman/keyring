# CVO~Z session log — 2026-07-25, ct-decommission (the last SYSPARITY unit) + the verdicts my kill destroyed

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bnk9yb6x2` · respawn after kill
Covers work after `40bbcb1933`.

---

## 0 · Startup (respawn)

| step | result |
|---|---|
| `/watcher` | re-registered (was STALE, prior PID 13208 → now 11384); no orphan watcher on my serial; Monitor armed |
| LD-0290 serial file | written |
| **LD-0319 load-time parity gate** | **SYSTEM CURRENT** — `06` sources unchanged, age 2h < TTL 24h; **managed regions: 24 compared across 6 file(s), 0 drifted**. The denominator fix I dispatched last session (`4d2588f35e`) is LIVE and reporting N/M — the silent-skip hole from cycle 19 is closed at its instance |
| LD-0318 cron | **re-armed** `13,43 * * * *` (job `f0291f27`) per XXX.md 1b-F; NFRA_SYSPARITY reads `active` so the scoped clause is live |

**One arming defect worth banking:** my first Monitor arm used `/c/Users/...` and died **exit 127**. This
session's shell is **Cygwin**, where the drive prefix is `/cygdrive/c/...`. The `/c/` form is what the
watcher SKILL and XXX.md both print. **A wrong path in an arm command fails LOUD (127) — but the same
prefix mismatch is what silently corrupts this session's harness exit codes** (every Bash call returns
"Exit code 1" with a trailing `claude-*-cwd: No such file or directory`; TRUE_RC captured in-stdout was
`0` throughout). Loud here, silent there, same root.

## 1 · Cycle 22 — `ct-decommission` · **RE-GROUND VERDICT: DRIFTED** (harness reads PASS)

The harness reads `[PASS] ct-decommission -- decommission family documented / found in 03_comp_tools.md`.
Re-grounding the *content* against the live estate, the representation is **one CTO ruling stale, grades an
unbuilt member as a validated prototype, and its check can detect neither.**

### F1 — the doc names a tool a CTO ruling deliberately prevented from existing

`03_comp_tools.md:18` lists **`comp-debris-ext`** as a bolded family member, and `:32` says it is
*"landing into the `org/modules/graph/` engines routed to CTO/~B (TO NFRA_DECOMTOOL.TO-1)"*.

Measured against reality:
- **CTO ruling (B), `20260718T003632Z`, rejected a separate `comp-debris-ext` explicitly** — verbatim:
  *"a separate comp-debris-ext duplicates comp-debris's surface = tool proliferation, which is the opposite
  of Andrew's canonical-flow 'reduce registration sprawl' intent."* Ordered: **EXTEND `comp-debris`
  IN-PLACE with `--types ddb,s3,ec2,events`.**
- **~B landed it** (`20260718T011104Z`); the manifest carries it at the EXISTING entry —
  `graph-call-manifest.yaml:1238` `comp-debris [--types ddb|s3|ec2|events]`, `:1494` *"Extended IN-PLACE
  (ruling B @97f6a8b70) … one classify, N adapters (`debris_adapters.py`)"*.
- **`TO NFRA_DECOMTOOL.TO-1` is `<status>complete</status>`.**
- **`comp-debris-ext` exists nowhere as a tool** — not in `.tools/`, not in `org/modules/graph/`. The only
  artifact is the pre-ruling prototype under `0.8.0_AE_CloudComp/deliverables/comp_debris_ext_prototype/`.

The doc is not *lying about history* — the prototype did exist and was live-validated. It is representing a
**superseded name as a current family member** and a **completed landing as pending**. A reader reaching for
`comp-debris-ext` finds nothing; the shipped surface is `comp-debris --types`.

### F2 — `resource_heat_snap` is graded `[BP-prototype]` and has no implementation

`:32` grades three members together: *"comp-debris-ext / comp-iam-usage / resource_heat_snap =
**[BP-prototype / F-land]** — self-tests green + live-validated against real AWS"*, then supplies evidence
for **two** of the three (`comp-debris-ext: ddb,s3=75 + ec2,events=179`; `comp-iam-usage: 209 roles`).

`resource_heat_snap` has **zero code anywhere in the repo** (`**/*resource_heat*` → 0 files; the 11 textual
hits are docs, logs and designs). Its own design doc says **`Status: RESEARCH / DESIGN`**. There is no
prototype for "self-tests green" to be true *of*.

**The shape is the point: three members share one evidence clause, two carry evidence, and the third
inherits the verdict.** Same class as an `N/A` summed as a real value — the reader cannot see which member
the evidence belongs to.

### F3 — the check is structurally incapable of catching F1 or F2

```
type: grep_present   files: [infra/system/03_comp_tools.md]
pattern: decommission|comp-debris|comp-similar|comp-iam-usage      (re.IGNORECASE, system_parity.py:427)
```
Four OR'd limbs over one file; all four currently match (2 hits each). **Any single limb passing renders the
identical verdict string.** The predicate asks only whether *names appear* — so a doc naming a **phantom**
tool matches it exactly as well as a correct doc, and naming more phantoms makes PASS *more* likely.

**This is the same defect `ct-catalog` was migrated off at cycle 10** (*"three OR'd common words that pass
whatever the catalog's real state"*). `ct-decommission` is that shape, unmigrated — a legitimate hit under
the flag-as-hit policy I set then (flag, **not** bulk-migrate).

**Correction I owe on my own working: I nearly filed a fourth finding that the first limb was DEAD** —
`grep -c decommission` returned **0** while the doc plainly says "Decommission". The doc uses capital-D and
my `grep` was case-sensitive; **`system_parity.py:427` compiles with `re.IGNORECASE`**, so the limb matches
fine. *My instrument, not the estate's.* Read the implementation before reporting the predicate.

### F4 — the sharpest one: the doc's number is still right and its claim is now false

`:18` closes with *"comp-which routes the 'find deprecated/unused/overlapping AWS resources' question at
**1.85 (weak) today** = the unrouted capability these close."*

**EXERCISED** (not read) — `comp-which "find deprecated/unused/overlapping AWS resources"`:

| rank | score | tool |
|---|---|---|
| **1** | **1.85** | **`comp-transform`** — a *React component field-render* tool |
| 2 | 1.50 | comp-aws |
| 3 | 1.50 | comp-pipescript |
| 6 | 0.40 | comp-dups |
| 18 | 0.31 | comp-similar |
| **31** | **0.27** | **`comp-iam-usage`** — built *for this exact question* |
| 33 | 0.26 | comp-deadgrant |
| **37** | **0.25** | **`comp-debris`** — the coldest-first AWS decommission ledger |

The purpose-built family occupies ranks **6, 18, 31, 33, 36, 37 of 68**, and a React tool beats the best of
them by **4.6x**. Both `comp-debris` and `comp-iam-usage` ARE registered and routable, with routing notes
that literally contain *"decommission a role or grant"* (`graph-call-manifest.yaml:149`, `:1443`).

**So the tools landed, registered, carry the right routing prose — and the router did not move at all.**

>> **THE DOC'S NUMBER IS UNCHANGED AND STILL ACCURATE, WHICH IS EXACTLY WHY NOBODY RE-CHECKED IT. A stale
>> number that happens to still read correct is worse than a wrong one: `1.85` invites no suspicion, so the
>> claim wrapped around it — "the unrouted capability *these close*" — survives untested. They did not close
>> it. It is open, measurably, at the same score.** <<

Live consequence under Rule 21, where `comp-which` is the DEFAULT entry point: an agent asked to find unused
AWS resources is routed to a **React component tool**. This is a routing gap on shipped tools, not a doc nit.

## 2 · The coverage denominator — and what my kill destroyed

I was told 21 of 22 units were swept. **Work performed ≠ verdicts on the record.** Measuring the record:

- Last substantive verify commit is `7a793f0fa7` — **cycles 16-19, "18 of 22"**.
- **No cycle-20 or cycle-21 commit exists**, and the working tree holds no uncommitted CVO~Z artifact. The
  predecessor session's verdicts for those cycles **died with the kill and are unrecoverable.**
- Grepping all 22 unit ids across the committed CVO~Z logs: **15 named by id; 7 not** (`ct-router`,
  `ct-decommission`, `ct-tenant-neutral-caveat`, `inf-substrate`, `inf-plumbing`, `eng-synthesis`,
  `eng-incorporation`). Mention-by-id is a **lower bound**, not a verdict count — a cycle may have swept a
  unit and described it in prose without its id.

**Honest statement: `ct-decommission` is closed here with a full verdict. Of the other 21, at most 15 have a
re-ground verdict retrievable from the record, and 3 sessions-worth of verdicts were lost to the kill.**

>> **THE SWEEP HAS NO REGISTER — its verdicts live only in session-log prose, so a killed session loses them
>> silently and the survivor cannot tell "swept and clean" from "never swept." The parity harness has a
>> machine denominator (`scope_contract.json`); the RE-GROUND pass, which is the half that actually decides
>> anything, has none.** << Recommendation: a per-unit verdict register keyed to the same 22 ids, written at
verdict time. Same record-is-the-only-carrier lesson as the XXX.md 1b-F cron row.

### CORRECTION (same session, ~1703Z) — my recommendation above is the WEAKER artifact. Superseded.

`0.8.0_AE_CloudComp~C` supplied the better design and it replaces mine:

>> **PERSIST THE DENOMINATOR + THE ARTIFACT POINTER, NOT THE VERDICT. A survivor can re-derive a verdict
>> from those; it can never re-derive them from a verdict.** <<

**A verdict register would have reproduced the defect it was built to fix.** A stored `verdict: clean` is a
TERMINAL CLAIM — the successor inherits it with no means to check it, which is exactly the unfalsifiability
that made the lost cycles a problem. Denominator + pointer is **re-derivable state**. Same principle as
CTO~Z's cycle-20 ruling one domain over: **store the things capable of disagreeing** — a verdict cannot
disagree with anything.

**And ~C supplied the instance, because it IS the survivor I described abstractly** (killed ~1640Z,
respawned). It could not determine from inside whether its own predecessor's registration summary
(*"per-site enumeration handed over"*) was true — it resolved that only by finding the artifact **in my
inbox**. Absent that message, *"handed over"* and *"intended to hand over"* were **byte-identical from where
it sat**.

>> **THE GAP DOES NOT MERELY LOSE VERDICTS — IT MAKES A DEAD AGENT'S CLAIM ABOUT ITS OWN WORK UNFALSIFIABLE
>> FROM INSIDE THE FABRIC. The successor inherits the CLAIM without the EVIDENCE. A CROSS-AGENT ARTIFACT
>> rescued it; no register did. That is SENT-is-not-READ one level up: A SUMMARY IS NOT A DELIVERABLE — and
>> we read broker registration summaries as state.** <<

Corrected copies: MSTR `170402Z`, CTO~Z `170418Z`, ~C `170347Z`, and this file. Design attributed to ~C.
Surfaced not adjudicated: the last point runs past SYSPARITY into the liveness/handoff convention — CTO~Z's
to route.

### And it has already cost a named decision

CTO~Z asked for the **cycle-21 marker-oracle finding** as a routed decision. It is **gone** — no commit, no
working-tree artifact. I refused to reconstruct it from memory: **a reconstructed finding is a fresh claim
wearing a forged provenance**, and he would have ruled on it believing it had been through a pass it never
had. Offered instead: a fresh sweep at today's vintage, labelled cycle-23, with no inherited credibility.
**A Tier-1 decision is blocked on a finding that no longer exists anywhere.** That is the instance behind
the argument.

## 3 · Verdict

| | |
|---|---|
| unit | `ct-decommission` (comp-tools domain, 22nd/last declared unit) |
| harness | **PASS** (mechanical presence) |
| **CVO~Z re-ground** | **DRIFTED** — F1 superseded tool name + completed-landing-shown-pending; F2 unbuilt member carrying a borrowed validation; F3 check cannot detect either; F4 the routing claim is false while its number is accidentally still true |
| routed | F1/F2 doc repairs + F3 check migration → CTO~Z. **F4 (routing gap on shipped decommission tools) is the one with live cost** — an estate-behaviour item, not a doc item |
| grounding | doc read at worktree; ruling + landing at `20260718T003632Z` / `20260718T011104Z` / `@97f6a8b70`; TO status read; `comp-which` **EXERCISED** with the full 68-row ranking enumerated, not the top-3 terminal view |

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-system --check` | **CURRENT** | gate-first per LD-0319; **now prints `24 compared across 6 file(s)`** — my cycle-19 denominator finding is fixed at the instrument |
| `system_parity.py` | 21/22 mechanical PASS, 1 FAIL | the FAIL (`ont-rulebank-version-current`) is **by design** — DENOM item A |
| `comp-which "find deprecated/unused/overlapping AWS resources"` | **1.85 → comp-transform** | EXERCISED; the terminal shows only top-3, so I enumerated all 68 from `rank-3812.yaml` — **the top-3 view alone would have hidden the whole finding** |
| `Glob **/*resource_heat*` | **0 files** | the negative that made F2 measurable |
| `graph-call-manifest.yaml` read | both tools registered + routable | separates "not registered" from "registered but unroutable" — F4 is the second |

**Two instrument errors of my own, both the same shape:** a case-sensitive `grep` I nearly filed as an
estate defect (§1 F3), and `list(d.values())[0]` on the rank YAML that returned `len(question)=48` and
printed a confident **"TOTAL RANKED: 48"** for a 68-row file. **Print the shape; read the implementation.
I have now paid for this one enough times that the lesson is not the finding — the habit is.**
