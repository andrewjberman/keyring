# 4.0.0_SA_CRO -- the doctrine consolidation programme + the memory-corpus audit (2026-08-05 14:52Z -> 22:05Z)

**archetype:** MIXED
**secondary_archetypes:** SCRIBE, DIAGNOSE, VALIDATE, COORDINATE

## Window

14:52Z -> 22:05Z, 14 commits. Prior log: `logs/2026-08-05/dc007_disposition_ledger_gap_1250-1452Z.md`
@ddf22cd5a.

## What happened (chronological spine)

1. **Andrew challenged the verification doctrine directly** -- *"the doctrine is just bureaucracy, it
   is dogmatic but miscalibrated for actually solving problems"*; `CONTROLS_OVER_CARE` is *"mostly
   slop and emblematic of this trend."* Asked for a failure analysis across my own error, CTO~B's, and
   the doctrine corpus.

2. **Failure analysis delivered.** The unifying mechanism: **cheap, direct, decisive evidence was
   available and an inference was substituted for it** -- not "failed to verify"; everyone verified
   *something*. Why care cannot fix it: **care operates on the answer you already generated; it does
   not send you to get a different one.** Measured against the corpus: `CONTROLS_OVER_CARE` grew
   320 -> 1,289 lines in 18 days (457 lines on 07-25 alone), and its headline thesis is contradicted
   by its own body 65 lines in (capstone: *"every one caught by a control"*; line 78: *"not one was
   caught by a gate -- somebody read the thing"*).

3. **Andrew ruled the rewrite** (4 rulings, recorded + broadcast same turn per XXX.md):
   R1 cut to the 4-5 real ideas · R2 **genchi genbutsu** as the organizing principle and
   **"the comp-tooling is not additive, it is foundational"** · R3 **agentic artifacts are a MAP, not
   the territory** (a REFINEMENT of my own over-guilty framing to CVO~B, which I corrected) ·
   R4 **incidents do not live in governance docs**, reference an id.

4. **Owned-paths grant** for CRO on process-architecture surfaces (Andrew-direct). Measured my own
   lane state with a firing negative control, then **routed to CTO rather than self-landing (SoD)**.
   Landed @df9981935; CTO deliberately granted ANY_CTO in FULL, declining my narrower offer on the
   grounds that narrowing a sovereign word is the same adjudication class as widening it.

5. **THE DOCTRINE PASS, 5 splits, complete.** `docs/doctrine` **1,820 -> 1,371** across 9 files, with
   **5 new instance-records** carrying every measured number. Nothing deleted; evidence moved and
   linked both ways.
   - `CONTROLS_OVER_CARE` 1,289 -> 259, retitled GENCHI GENBUTSU. Path KEPT: **156 files cite it**.
   - `INSTRUMENTS_AND_AXES` 384 -> 136 (was organized *by incident*, s7a-s7f).
   - `INTENT_DENOMINATOR` 380 -> 411 -- **grew**, absorbing the 313-line route model.
   - `MECHANISM_LAWS` + `VERIFICATION_LAW` 461 -> 242 + 45 pointer, **merged** on Andrew-direct.
   - `CHECK_LIVE_NOT_FROZEN` 120 -> 90 · `A_VALUE_MUST_CARRY_ITS_CLAIM` 150 -> 90.
   - `TRIGGER_LAYER` untouched -- it was already the model.

6. **DENOMINATOR centralized (Andrew-direct).** He asked me to expand it to denominator work as a
   whole AND said *"check the art to confirm"* on his own A/B/C recollection. **The check changed the
   content:** A confirmed; **B corrected** (grain shift is orthogonal shape #2, a C, not a B);
   **C corrected** (the art's own s7 is titled *"'C = new axis' UNDERCOUNTS C"*). Route model
   ABSORBED from `infra/system/ontology`, `ROUTE_LOGIC` repointed -- **moved, not copied**; path
   chosen on measured inbound counts (45 vs 12).

7. **Rule 24 gains a FOURTH POSTULATE -- STATE COHERENCE** (Andrew-direct, verbatim in CLAUDE.md).
   It **earned itself on first exercise**: auditing the five orthogonal shapes found the detectability
   split **3/2** -- the residue detector reaches #1/#2/#5a and **structurally cannot** reach #3/#4 --
   so **a build plan for that detector delivers three fifths of its own axis and reports itself
   complete.** The other three postulates all failed too (audit @dc0769349).

8. **CTO ruled the blocking item and OVERRULED MY RECOMMENDATION, correctly:** *"re-cutting the axis
   to make the plan look complete would DELETE THE EVIDENCE of a real instrument gap."* I drafted the
   detectability column to their gate @eecc2d49f.

9. **Q1 + Q2 closed, Andrew-ratified, and consolidated** @61352e784. Both had been reached
   independently by `3.0.0_SA_CVO` (empirically, 13-instance census) and this desk (structurally,
   Rule-24 audit). #5 declared a composite **and split into 5a/5b** because its single detector caught
   SPLIT only -- a MERGE was undetectable under a shape named for it. #3 moved to a **second field**,
   and the field already existed (the s6 2x2 is a concealment classification).

10. **MEMORY CORPUS AUDIT** @5b7ab845d4, testing Andrew's prior (*"deprecated/unused temp folder"*).
    **The prior is false:** 1,012 files, 5.8MB, **99.7% recall-addressable**. Real findings: it was
    **UNVERSIONED** and the two corpora were **UNWIRED** (doctrine->memory citations: **zero**).

11. **All four recs executed** on Andrew's word: `memory/` under git (genesis `6843c2f`, 1,013 files,
    `autocrlf=false`) · 3 frontmatter defects repaired -> **100% recall-addressable** ·
    doctrine<->memory wired, **0 -> 8 files citing** · no pruning.

12. **RCN-0005 recovered** @3f87abf4c1. DS's courtesy note about an unrelated staging conflict
    surfaced **~460KB of Andrew-facing work sitting UNTRACKED** -- the MDPF Portfolio Ontology spec
    from today's Andrew/Yang session + 2 diagrams + a register row, authored under my serial by a CRO
    session that is not this one. Committed for DURABILITY, explicitly not ratification.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-grep | ~15 runs: inbound-pointer censuses (CONTROLS_OVER_CARE 156, INTENT_DENOM 45, ROUTE_LOGIC 12, MECHANISM_LAWS 20, VERIFICATION_LAW 10), Route A/B/C prior-art, shape-number citations | PASS | **the pointer counts drove every path decision in the pass** -- no rename was made on preference |
| comp-state | `--self-test` x2 | PASS 3/3 | gate for the /exec-sum |
| comp-which / comp-surface-check / comp-pulse | via safe-commit x14 | PASS | surface-check clean each time; risk-reflex CLEAN with denominator printed |
| owned-paths-validate | exercised directly, positive + negative controls | PASS | measured my own lane BEFORE asking for the grant; negative control (`org/tier0/ledger`) fired |
| git (as instrument) | `git show <sha>:<path>` vintage reads, `--diff-filter=A`, byte-level `python` diffs | PASS | the byte-level CR/LF comparison is what killed the "tamper" finding |

**What worked:** measuring inbound citations before every rename -- it is the single practice that
prevented a dangling-reference cascade across a 5-file rewrite. And **checking shape-number citations
before renumbering**, which caught a live near-miss.
**What failed:** my link-extraction join in the memory audit did not normalize hyphen-vs-underscore,
producing a false "9 dangling rows" (true: 0). Two of my commit messages stated line counts I had not
re-read off the measurement printed seconds earlier (262/200 vs true 282/239).
**Gap found:** `docs/doctrine` had **zero** pointers into the agent-memory corpus that holds its
grounded evidence -- and my own merge had severed the only four that existed.

## Files Modified

see commit messages: `73c5c9da8`, `49d4537e6`, `4defd7ff3e`, `b51513a69`, `b0f0cf2f9`, `d98149ea6`,
`dc0769349`, `dc9c930e6`, `b5cbafdac`, `eecc2d49f`, `61352e784`, `5b7ab845d4`, `3f87abf4c1`,
`e9d89a997`. Plus the memory repo (separate): `6843c2f` genesis, `edb8446` repairs.

## MCP traffic

~18 significant exchanges. OUT: 3-ruling Andrew-direct BROADCAST to MSTR/CTO/COO; owned-paths grant
request to CTO (SoD-routed, not self-landed); OWNED BLOCKING ITEM to CTO on the five shapes; 4 to CVO
(Class-3 answered, fold notice, two corrections of my own framing); 2 to CVO~B (seal design accepted,
then corrected); ACK to DS. IN: CTO x4 (grant landed, missed-my-message self-correction, the
blocking-item ruling, provenance claim I then corrected); CVO x4; CVO~B x1; MSTR x1; DS x1.

## Blockers

**None.** Open items are Andrew-paced or at owning lanes.

## Current State (zero-context handoff)

`docs/doctrine` = 1,371 lines / 9 files + `DENOMINATOR_ERRORS` (CVO's, folded subordinate) +
`DERIVED_UNIVERSE` (CTO's, landed independently). Canonical homes: **GENCHI GENBUTSU** (how you fail
to see) · **ASSERTION LAWS** (VL#1-14 checklist + M1-M14 taxonomy, **both ID spaces are public
interfaces -- never renumber**) · **DENOMINATOR** (the ontology of coverage; two-tier two-field, all
shape numbers preserved) · `TRIGGER_LAYER` · `CHECK_LIVE_NOT_FROZEN` · `A_VALUE_MUST_CARRY_ITS_CLAIM`
· `INSTRUMENTS_AND_AXES`. Five instance-records under `docs/references/`. CLAUDE.md Rule 22 re-pointed,
Rule 24 now four postulates, and the incidents-not-in-governance-docs rule is in "Changing this file".
`memory/` is a git repo at `~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`
(HEAD `edb8446`, 1,013 tracked, autocrlf=false) -- **it is NOT part of the workspace repo and has no
remote.**

## Next Steps

1. **[Andrew]** RCN-0005 (MDPF Portfolio Ontology, `briefs/`) is staged for his review -- recovered,
   unratified, unread by me. Also: `memory/` has no REMOTE, so it is versioned but not backed up
   off-device.
2. **[1.0.0_SA_CTO]** gate the ARCHETYPAL detectability column @eecc2d49f; doctrine read still queued
   behind MDPF.
3. **[3.0.0_SA_CVO]** fold accepted; restore anything the fold cut that was doing work.
4. **[4.0.0_SA_CRO]** OPEN + UNMEASURED: **content staleness across the 1,010 memory files** -- I read
   3 closely and cannot say how many are still TRUE, and a recall-addressable file asserting a
   retracted rule is worse than an orphan. Also open: the `#2`/`#4` field-2 mapping rows are REASONED,
   not exercised -- do not build on them until walked.
5. **[Andrew, parked by him]** how to enforce reading/understanding of the fetch. Today produced three
   more specimens, including two of mine.
