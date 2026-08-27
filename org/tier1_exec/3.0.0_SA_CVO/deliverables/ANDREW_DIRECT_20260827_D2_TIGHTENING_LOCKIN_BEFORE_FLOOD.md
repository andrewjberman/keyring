# ANDREW-DIRECT — D2 process tightening: LOCK IN WITH CTO+COO BEFORE ANY D2 AGENT LAUNCHES

**Channel:** Andrew live at the `3.0.0_SA_CVO` base terminal (laptop fabric).
**Time:** 2026-08-27 ~14:5xZ–15:1xZ (recorded 15:13:41Z, `date -u` read same turn).
**Recorded by:** 3.0.0_SA_CVO, same turn, verbatim per org/XXX.md (the phrasing IS the ruling).
**Broadcast:** MCP to 1.0.0_SA_CTO + 2.0.0_SA_COO + 0.0.0_AB_MSTR, same turn as this commit.

---

## HIS WORDS, VERBATIM, IN ORDER

1. *"Please tell me your primary responsibilities as CVO. Namely the proof of spec and
   investigations vs remediations work. I want an assessment of this process and how consistent
   and effective it is in application."*

2. *"What needs to happen to tighten this up before flooding D2 today?/"*

3. *"I want you to build this out with CTO before launching D2 agents. COordinate with CTO and
   COO to lock this in."*

4. *"I have already held MSTR on agent launching so we can make sure we are 100% clear on this
   process first."*

## WHAT THE WORDS BIND

- **A LAUNCH HOLD IS LIVE:** Andrew has held `0.0.0_AB_MSTR` on D2 agent launching. **No D2 seat
  is instantiated until the process below is locked with 1.0.0_SA_CTO + 2.0.0_SA_COO and the
  lock-in is confirmed back to Andrew.** The hold is HIS, placed at MSTR; this record carries it
  so the release condition is on the record: lock-in confirmed -> Andrew/MSTR release.
- **The thing being built out** is the 5-point tightening plan 3.0.0_SA_CVO presented at this
  terminal immediately before word (3), against the CVO process assessment (proof-of-spec +
  investigations-vs-remediations) he requested in word (1). The plan, with owners:

| # | act | owner | state |
|---|---|---|---|
| 1 | CVO cert step-zero runs BEFORE every D2 GO (id set vs governing spec, decomp_ref present, instance path/grammar matches group shape, positional invocation on the face) | 3.0.0_SA_CVO | adopted, starts at first D2 TO mint |
| 2 | Layer-2 commit-lint: refuse a NEW pipeline-project TO lacking `<decomp_ref>` (extends `.tools/git-hooks/to-proof-of-spec-check.sh`) | tooling lane, CTO routes | build authorized 2026-08-21 ratification ("build routed"); LANDING is the D2 precondition |
| 3 | D2 channel durability rule: any mid-round ruling amending a spec/remedy lands in the project INVESTIGATION doc same-turn, landed by CVO; declared on the three doc faces at drive open | 3.0.0_SA_CVO | landed with this commit (three doc appends) |
| 4 | D2 round-close runs a REAL remediation cut: round terminates only when REMEDIATION_v1 graduates zero items; rows re-enter at stage 3 | 3.0.0_SA_CVO cuts; COO re-enters | see reading note below |
| 5 | Every D2 TO face: proof-of-spec instance validated by rc (never output string), WITH the id set, validator run itself evidence in the instance | 2.0.0_SA_COO at mint | adopted pending COO lock |

- **READING STATED PLAINLY SO ONE LINE CORRECTS IT (item 4):** the plan's item 4 was presented as
  "needs your ruling; rec = yes." His word (3) — "build this out" — is read here as ratifying the
  plan AS PRESENTED, item 4's rec included: **D2 closes through a real remediation cut.** If he
  intended item 4 to remain open, one line at any terminal corrects this record; absent that
  line, the remediation-cut close binds for D2.
- **Scope:** this lock-in governs the D2 drive (ADVI_PERFRP / ADVI_INSURE / ADVI_STITCH per
  1.0.0_SA_CTO msg 76077 + `docs/briefs/d2-critical-path-sequencing-20260827.md`). It is not a
  general law edit; if any piece should become standing law, that is a separate act on CLAUDE.md /
  the pipeline doc with its own word.

## RELEASE CONDITION (what "locked in" means, so the hold has a measurable exit)

1. CTO ACK on: layer-2 lint landed (or explicitly scheduled with the lint verified pre-first-mint),
   cert-before-GO sequenced into the drive plan, item-4 close mode acknowledged.
2. COO ACK on: item 5 folded into every D2 TO mint, cert-before-GO handshake (mint -> CVO cert ->
   GO), fresh `~lane` one-project seating per the 08-24 rule.
3. CVO (this seat): items 1+3 standing, confirmed in the lock-in report.
4. Lock-in report back to Andrew at this terminal -> he releases MSTR on launching.

— 3.0.0_SA_CVO
