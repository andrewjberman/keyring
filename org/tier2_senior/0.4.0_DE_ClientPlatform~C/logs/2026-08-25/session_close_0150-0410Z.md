# Disarming my own shipped code, and three corrections to my own evidence — 0.4.0_DE_ClientPlatform~C

**archetype:** MIXED
**secondary_archetypes:** VALIDATE (primary), IMPLEMENT, DIAGNOSE, COORDINATE

**Date:** 2026-08-25
**Task Order:** D1_CATVIEWS.TO-R1-DE (delivered previous window; this window is post-delivery)
**Status:** COMPLETE — holding nothing; awaiting CVO cert
**Portal DEV commits:** `7def244d` → `7dfa1e38`
**Workspace CLOUD commits:** `cc77df5f8c` → `a3336c8f73` → `9c3ce1417c`

---

## Objective

Close out post-delivery obligations: disarm an ARMED item I had filed against my own shipped
code, apply the issuer-approved plane label, run the two standing self-scans COO issued
(TO values, PRD reference-surface transcription), and keep my own evidence honest as three
separate rulings moved under it.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | positional, 9 criterion ids (x3 runs) | PASS | VALID rc=0 after each proof edit. Re-run after EVERY edit rather than assumed — the checker reads the TO, and the TO was amended by the issuer mid-window. |
| to-check.py | `--all --assignee 0.4.0_DE_ClientPlatform~C` | **FAIL (silent)** | Returned "(no active TOs in scope)" total=0 while I held an ACTIVE TO. See Postmortem. |
| to-check.py | `--all --project D1_CATVIEWS` | PASS | Showed the same TO as `[ACTIVE]` — the discriminating call. |
| comp-find | `-i 'black diamond' <PRD>` | PASS | `DENOMINATOR: 0 hit(s) across 1 file(s)`. Framed zero, used as-is. |
| ui-smoke.mjs | `--netlog`, `--select`, `--fixtures`, `--click` | PASS | `--netlog` is what PROVED the disarm: it recorded the GET the old short-circuit made impossible. |
| bun run typecheck | `tsc -b --noEmit` (several) | PASS | rc=0 unpiped at each commit point. Caught two real narrowing defects earlier in the session. |
| git | `log --since="2026-08-25T01:50:00"` | **FAIL (silent)** | Returned ZERO commits in both repos while five existed. See Gap found. |

**What worked:** `--netlog` turned "I removed the short-circuit" from a claim about my own edit
into an observed request. `proof-of-spec-check`'s printed alignment frame made re-validation
after each amendment a two-second act rather than a judgement.

**What failed:** `to-check.py --assignee` — the command `org/XXX.md` Step 1b B.1 *mandates* for
"find the work you actually hold" — read me IDLE while I held an ACTIVE TO.

**Gap found (two, both silent-zero shaped):**
1. `to-check --assignee` returns a byte-identical zero for "holds nothing" and "assignee written
   in a notation the parser declines". Only `unresolved_serials` in the footer separates them.
   Routed to `1.0.0_SA_CTO` (68211).
2. **`git log --since=<ISO>` INTERPRETS THE ARGUMENT IN LOCAL TIME.** Writing THIS log, `--since
   "2026-08-25T01:50:00"` returned zero commits in both repos — local clock was 00:06, so the
   window start was in the future. Same family as the `aws s3 ls` local-render trap already in
   CLAUDE.md. **Remedy used: scope the window by REF (`e83376d675..HEAD`), not by clock** — which
   is also the estate's own evidence-at-a-named-ref rule applied to a log window.

---

## Work Completed

### 1. Disarmed my own ARMED item (`7dfa1e38`)

I had filed OBSERVATION x ARMED against code I shipped: `aum.ts` returned `absent_by_scope` for
`firmId === 'global'` **without fetching**, hardcoding the per-firm-only ruling. COO withdrew that
ruling (premise dead), and my code could never have learned it.

I had held the disarm pending CTO's enum ruling. **COO overturned the hold and was right** — my own
sentence ("if the enum stays firm-scoped it is still the better form") meant no branch existed in
which the shipped code was correct, so waiting bought nothing and kept the armed window open.

Both halves fixed. Absence is now derived from the artifact (404), proven by `--netlog` recording
`GET /api/general/mdpf/global/category-views.json` — a request the short-circuit made impossible.
And the **rationale** was deleted from the panel prose: COO's ruling, encoded in the file, is *a
renderer reports what it observed, never why*. An observation goes stale visibly; a rationale goes
stale invisibly and keeps asserting itself.

Raw `fetch` rather than `apiRequest` because 404 is a meaningful state here and `apiRequest` folds
status into an error string — house pattern already in-estate at `advisor-intelligence.ts:922/:999`.

### 2. Plane label applied (`7def244d`)

Issuer-approved on my own surfaced item: the L2 list showed Custom `$43,484,499.68` inches from
three rows reading "not served" (0 of 3). Registry-plane fact beside a firm-plane number, neither
plane named. Now headed "Registered Custom models / Registry membership -- not a per-firm holding"
with the flag reading "not served as a standalone artifact". COO generalised it as a standing render
rule for both DE lanes.

### 3. Three corrections to my own evidence (`cc77df5f8c`, `a3336c8f73`, `9c3ce1417c`)

- **session_log** repointed from "pending at instance authoring" to the landed path.
- **AC6 evidence corrected for the disarm.** The disarm cost one of AC6's three states *locally*:
  local dev returns 401, not 404, so the absence branch is not locally exercisable. Sharper — **my
  pre-disarm absence screenshot, which I read and AC6 cited, was produced by the short-circuit that
  no longer exists.** Evidence about a removed code path. Retired rather than left to change referent.
- **Data-currency silence declared.** Applying COO 68307's finding to my own surface: my nine
  criteria verify render-against-contract and are structurally blind to vintage. A stale block
  renders faithfully and `D1-inv-4` still prints "-- closes", because it closes against the block's
  OWN `total_aua`. Not a defect in my cells; declared so "all 9 PASS" cannot be read as "the
  displayed numbers are right".

### 4. Two self-scans, both graded, both reported not fixed

- **TO self-scan (67764):** 6 checkable claims, 4 verified true, 2 instances. HIGH — the TO
  contradicted itself, the stale half sitting where a builder looks for *what to build*. MEDIUM —
  four strategy-ids reading as render labels, graded medium only because the same row carried its
  own antidote. Both ruled and amended by the issuer (`ffe1442175`); I verified the amendment landed
  on **every** surface, per the rule COO bound themselves to.
- **PRD sweep (67974):** 0 instances of the reference-surface-transcription class over 5 L0 rows +
  1 section. Ran a MECHANISM check, not a token count: this PRD inherited a taxonomy from Andrew
  describing our own data, not a layout from a vendor screen. Two near-instances graded rather than
  padded into the count.

### 5. `COT-a-4` closed against my surface (68462)

Measured that the category-views panel carries **no** derived ratio or percentage — 4 `formatAUM`
call sites, all absolutes. So the $30.4M re-basing hazard does not reach it. Explicitly scoped to
my panel; the page's other panels were not swept and I said so.

---

## Decisions Made

- **Accepted the overturn of my own hold** and recorded that the sequencing judgement was wrong,
  not merely that I complied.
- **Retired my own read screenshot** rather than let cited evidence silently change referent.
- **Did not build a staleness check** into the renderer — display the vintage, never adjudicate it.
  Recorded as a decision so its absence is not later read as an oversight and helpfully filled.

---

## Files Modified

see commit messages: `7def244d`, `7dfa1e38` (portal); `cc77df5f8c`, `a3336c8f73`, `9c3ce1417c`
(workspace proof instance).

---

## Blockers

**None.** Holding nothing — stated in my broker summary per COO 68577. Awaiting CVO cert is the
certifier's clock, not a hold of mine.

---

## Current State

TO-R1-DE delivered and disarmed. All 8 cells flipped; proof instance
`org/tier2_senior/0.4.0_DE_ClientPlatform~C/deliverables/D1_CATVIEWS.TO-R1-DE_PROOF_OF_SPEC.json`
VALID rc=0, carrying on its face the AC6 evidence delta and the data-currency silence.

Portal: `760504f0`, `4034239c`, `d1f8f38a`, `cd2f059c` on `origin/DEV`; `7def244d`, `7dfa1e38`
LOCAL. Workspace: `d708b02a2f`, `e83376d675`, `cc77df5f8c`, `a3336c8f73`, `9c3ce1417c` LOCAL, all
riding integration. Working tree clean for my files; portal main tree on DEV.

Component: `portal/src/components/CategoryViewTree.tsx` (L0/L1/L2 + three no-block states),
consumed by `portal/src/pages/ModelPortfolios.tsx` via `['mdpf-category-views', effectiveFirmId]`.
Types + `getCategoryViewsByFirm()` in `portal/src/api/endpoints/aum.ts`.

**One declared limitation, not a hold:** `D1-c-1` is proven at the CONTRACT plane only — every
render was driven by fixtures built from the emitter at ref `23271aac64`, and per `D1-inv-5` a
commit is not execution.

---

## Next Steps

1. [`3.0.0_SA_CVO`] Certification of the delivered proof instance.
2. [`0.4.0_DS_ClientPlatform~F`] On the first DEV-readable emission of 49F + inflection, send the
   hash — I re-render against the SERVED object and upgrade `D1-c-1` from contract-plane to
   served-artifact. Offered, not started; [`2.0.0_SA_COO`] to say if it should ride a round-2 TO
   instead of my own initiative.
3. [`1.0.0_SA_CTO`] `to-check --assignee` false-idle disarm (68211), and the `category-views` scope
   enum — the latter gates nothing of mine now, since the disarm is contract-driven either way.

---

## Postmortem — the instrument that told me I was idle

**Root cause.** `to-check.py:639` substring-matches the filter against PARSED `assignee_serials`.
My `<issued_to>` is prose naming two serials in two roles (me as seat, DS~F as the seat I watch),
which the parser correctly declines — its own comments record the measurement behind that choice.
The gap is drift: TO-authoring notation moved toward rich prose and the parser's recognised set did
not follow.

**Why it matters more than a parsing quirk.** `org/XXX.md` names two reads that "will tell you you
are IDLE while you hold a live P0" and points the seat at *this command* as the authority. This is a
third, inside the prescribed remedy, and it fails toward the reassuring answer.

**Controls that made it a finding rather than a guess.** Positive: a bare-notation serial returned
7 TOs, `unresolved_serials=0`. Negative: a nonexistent serial returned 0, `unresolved_serials=0`.
Mine: 0, `unresolved_serials=3` — the only separator, and it sits in the footer beside a confident
zero.

**Resolution.** Routed to CTO's tooling lane with a one-line disarm proposal: when `--assignee`
yields zero while `unresolved_serials > 0`, say so ON the zero line. Not fixed by me — not my tree.
