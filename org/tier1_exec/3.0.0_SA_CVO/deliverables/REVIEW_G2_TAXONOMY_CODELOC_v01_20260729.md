# CVO ADVERSARIAL REVIEW — G-2 DECIDE drafts v0.1 @476f4f71f5 (GRAPH_PROVENANCE_TAXONOMY + GRAPH_CODE_LOCATION_STANDARD)

**Reviewer:** 3.0.0_SA_CVO · 2026-07-29 ~13:15Z · **archetype:** VALIDATE
**Verdict up front: both ADOPT WITH AMENDMENTS. The taxonomy has one P0 — an adoption-day,
client-visible consequence the draft does not price. The code-location standard has one P1 gap its
own incident list proves.** Answers keyed to your three named surfaces.

## 1. PROVENANCE — the enum is right at five, but only with two amendments

**Q: is the five-state enum complete? RESTATED / QUARANTINED / SUPPRESSED?**
Complete, given one organizing rule the draft implies but never states — put it in §2 verbatim-class:
**states describe what a value IS; events and workflow describe how it GOT that way — events live in
the clock fields, workflow lives in reasons, and neither ever enters the enum.** Under that rule:
RESTATED is an event (`generated_at ≫ as_of`; WO-4b's backfill re-emits are simply MEASURED with a
late producer clock — no new state needed, and the draft's three-clocks section already carries it).
QUARANTINED/SUPPRESSED are workflow — **but they only fold cleanly if ABSENT gains a required
field.**

**P1 — ABSENT must require `absent_reason`. The draft's own lineage demands it:** the WO-4a ruling
it descends from reads "emit ABSENT with a reason, never 0," and the reason clause was dropped in
transcription. A bare null is unanswerable at certification time (suppressed? refused-partial?
source-dead? never-produced?), and it is precisely where QUARANTINED/SUPPRESSED belong:
`absent_reason: quarantined:<ref>`. This one field closes your excluded-candidates question exactly.

**P1 — declared alias map for the live dialect.** The estate already speaks provenance:
`rolled_forward` (ruled CORRECT behavior, Amendment 3), `vintage_state` (WO-4b's verify reads it),
`point_class` + `cohort_provenance` (live in the canonical global artifact I diffed this morning),
`coverage_state` (E4). Adopting a new vocabulary without a mapping table (`rolled_forward→CARRIED`,
etc.) manufactures two-records-one-subject on day one. One table in §2; migrations cite it.

**Q: per-element tractability for wide artifacts?** Per-element is not a proposal — **it is live.**
The canonical `global/aggregate-aua-timeseries.json` already carries per-point `point_class` and
`cohort_provenance` (the PIN-1 enumeration's own caveat counts "2 measured + 45 interpolated" dates
FROM those fields). Concession rule, not concession: **a per-FAMILY label is a compression that
asserts uniformity and is legal only while lossless — one mixed element breaks the family back into
elements.** No wide artifact in the MDPF set needs more than that.

**P0 — the CARRIED window law fires on live cohorts the day it is adopted.** "A carry whose true
vintage is outside the declared window is ABSENT, not carried" is correct — and the four 49F ETF
cohorts (~$522mm, true vintage 07-06, honestly `rolled_forward` per the E1 ruling) are outside any
declared window. Adoption flips them from a labeled stale number to a client-visible null while E1
(retire-and-consolidate onto wsd) is still queued behind MDPF. Sequence it explicitly: adopt AFTER
E1 lands, or carry a named grandfather (`carried_grandfathered: E1-pending`) with E1's execution as
the discharge. Same class as my RETIRECOND P0: right law, unpriced first exercise.

## 2. CODE-LOCATION — C-1 needs a pair clause; C-3 should DENY at birth

**Q: aws/aws.cmd vs C-1's generated-into-N-1 — grandfather or migrate?** Neither: **amend the
clause.** C-1's target is hand-maintained REPLICAS (same-language copies that drift). aws/aws.cmd
is a POLYGLOT PAIR — different languages, one contract, already bound by the both-files-or-neither
atomicity law. Generating .cmd from bash is not mechanical; migrating buys no defect removal and
builds machinery. Amendment: *replicas are generated from the one home; a polyglot pair is legal
with a declared pair-invariant and a parity EXERCISE* (a test that routes one call through each and
compares — behavior-grade, per 22a). jq.exe stays the per-file-remedy cautionary cite; the pair
becomes the lawful pattern instance.

**Q: C-3 warn vs DENY-from-birth?** **DENY for NEW trees, WARN for existing stock until swept** —
the Gate-1/COMPRAIL announce-then-enforce precedent, compressed because the price is already known:
the WARN alternative was measured at 7 days of silent stale runtime; a birth-time DENY costs the
author minutes and teaches at violation time (the CLAUDE.md gate ideal). Escape: audited
`# map-exempt: <why>` marker, house style. A DENY on the whole existing stock on day one would
block unrelated deploys on old debt — that half stays WARN with the sweep owning it.

**P1 — the standard's own incident list indicts a class its clauses don't cover.** Incidents #3/#4
(.tools gitignore, the stranded accrual bridge) are HOST-LOCAL TOOLING failures, but C-3's registry
enum covers only script trees / Lambdas / EC2. `.tools/ → ~/bin` forwarders IS a deploy (repo home →
deployed location) whose only mapping is the provisioner script's header — exactly the unmapped-tree
defect C-3 names. Add the fourth mechanism class: registry = a provisioner manifest, gate = the A.3
denominator probe already in XXX.md. **This overlaps MSTR~Z's live portability census
(@b9acb07c7a, 19-referenced-by-live-machinery floor) — route the clause through that census, don't
draft past it.**

C-2 and C-4 pass as written; §3's which-is-RIGHT restatement is faithful to 17a.

## 3. Contradiction check — NONE FOUND, denominator stated

Checked against: CLAUDE.md law (key grammar, naming law, roster-as-authority, T-1 reasoning — all
cited consistently), the GRAPH register execsum + MISSIONS rows (the drafts close exactly the two
named UNDECIDED halves; no DECIDED item is contradicted), OPAL_TAXONOMY.json (active,
naming/structural scope — these drafts extend it downward to value level, no collision). **NOT
deep-read: 0.8.0's OPAL_TAXONOMY_DC_LEDGER_20260717.md** — if any clause there fixed value-level
vocabulary, my no-contradiction verdict does not cover it; a 5-minute check by you or 0.8.0 closes
that residual.

## RESIDUAL CLOSED (~14:35Z, Andrew-directed): OPAL_TAXONOMY DC ledger deep-read

`OPAL_TAXONOMY_DC_LEDGER_20260717.md` read in full. **It fixes NO value-level vocabulary — the
provenance-taxonomy no-contradiction verdict now covers the whole record.** The ledger is
structural (SS-A prefix grammar / SS-B repo homes / SS-D scheduler grammar / SS-E-C OS-IAM-region).
Three CODE-LOCATION touchpoints surfaced, none a contradiction, all worth folding into v0.2:

1. **DC-7 is a prior-RULED instance of C-1 and should be cited as precedent:** `landing_guard.py`
   exists as two byte-identical copies with no canonical home — "CONFORM-BY-LUCK" — and CTO already
   ruled canonical-home + build-manifest sha-tie (W3). It is also the clean CONTRAST case for my
   polyglot-pair amendment: landing_guard is a same-language REPLICA pair (generate/canonicalize —
   C-1 as drafted applies in full); aws/aws.cmd is the polyglot pair (pair-invariant + parity
   exercise). Citing both makes the clause's boundary teachable.
2. **C-2's deployed-location enumeration is already behind a ruling:** DC-1's ruled disposition
   migrates runner shell scripts to `opal-runner-shared` — a location class C-2's prose
   (`s3://opal-data-{pipeline}/code/` or the Lambda artifact bucket) does not name. Not a conflict;
   an enumeration-drift instance ON ARRIVAL. Fix: derive the legitimate-locations set from a
   registry (the C-3 mapping files themselves) rather than enumerating in prose — prose enumerations
   are this workspace's named stale-record class.
3. **The DENY-at-birth recommendation should ride the ledger's own hard-won pattern:** RS-1's lesson
   ("an instrument that measures the wrong breadth is a gate that either floods or lies" — the raw
   `conforms` field flagged 153/154) plus the DC-8..11 enforce-grammar build (grandfather-pin 11,
   scoped exit-2, estate-wide WARN @e9b271291) is exactly the mechanism my C-3 DENY needs: measure
   how many trees are currently unmapped FIRST; grandfather-pin the stock; DENY only births past the
   pin. Same recommendation, now with its ride-surface named.

## What you should have asked but did not

**The taxonomy cannot catch a source that forges vintage INTO the data.** MEASURED's law (as_of
from the data, never key/filename/run-date) defeats the G7 forged-KEY class — but the ECLIPSE puller
incident is the other class: an instrument that cannot target a date lands its OWN RUN DATE as the
value_date, so the data column itself lies and MEASURED labels it clean. The discriminator already
exists in the estate: the roster's declared cadence — an as_of that persistently equals its own
landing date at a declared T-1 feed is a suspect measurement, not a clean one. One sentence in §2
(or a comp-validate per-state row) closes the class; without it the taxonomy certifies exactly the
false-vintage artifact that motivated the vendor-egress lesson. Second, smaller: both docs close
DECIDED halves of a register whose own thesis is "DECIDED is not the bottleneck — ADOPTION is."
Each should ship carrying its arming plan (marker file, ramp stage, owner) or they widen the 92%
gap they cite.

— 3.0.0_SA_CVO
