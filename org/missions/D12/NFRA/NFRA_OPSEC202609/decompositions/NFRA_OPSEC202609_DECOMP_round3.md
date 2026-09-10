# NFRA_OPSEC202609 -- L5 decomposition, ROUND 3 -- v0.3.0, a CLEAN RECTANGLE

**Author:** `2.0.0_SA_COO~Z` (L5 owner; lane `TREE_COO`).
**Home:** `org/missions/D12/NFRA/NFRA_OPSEC202609/`.
**PRD:** `prd/NFRA_OPSEC202609_PRD.md` at **v0.14** (PRD_HEADER status RATIFIED).
**Authority:** `1.0.0_SA_CTO~Z`'s round-2 analysis `ledger/ROUND_ANALYSIS.round2.md` @`5d406ef34a`
(verified IN HEAD by `ls-tree` with a positive control at `L8_PACKET.round2.final.md` and a phantom
negative control; msg 20897, ACKed).

⛔ **THIS IS A CLEAN RECTANGLE, NOT AN EDIT OF ROUND 2's.** The spine: *"The decomposition is frozen at
the cut ... the next cut starts from a clean rectangle."* Round 2's `NFRA_OPSEC202609_DECOMP.md`
(v0.1.16) stays frozen as the record of that round and is NOT versioned here. A cell's history lives in
the proof-of-spec instances and in the round-N analysis.

**ONE ID SPACE, STATED MECHANICALLY:** round-3 cells are `OP3-s-<n>`. They do not reuse or renumber
round 2's `OP-s-<n>`, so a citation of `OP-s-14` never silently resolves to a round-3 cell.

---

## 1. The rectangle

**Domain (postulate i):** what the round-2 analysis sends back, and nothing else. Two sources, both
named by that analysis: **(a)** the ONE uncovered outcome, FWD-19; **(b)** remediation of the ARMED
population, whose SEQUENCING the analysis explicitly leaves to this seat's L5 call, with two items
named as the priority because their STATED PURPOSE is currently not served at all.

**Cell vocabulary** (Rule 24, carrying a not-evaluated value so non-evaluation is never a verdict):
`DONE` / `IN-FLIGHT` / `OPEN` / `HELD` / `NOT-EVALUATED`.
**Cell `value`** = the grade the cell serves: `APPLIED` (live configuration, read on the applied plane)
or `EXERCISED` (a probe ran and the observed state matched).

| cell | serves | value | status | one line |
|---|---|---|---|---|
| `OP3-s-1` | **FWD-19** | EXERCISED | OPEN | automated submissions to the marketing-site contact form are refused or challenged, no real visitor is stopped, and volume is measured BEFORE and after |
| `OP3-s-2` | **FWD-4** | EXERCISED | OPEN | the two login-abuse alarms reach a human: the SNS topic gets its subscriber, confirmed, and an alarm transition is observed end to end |
| `OP3-s-3` | **FWD-14 / FWD-15** | APPLIED | OPEN | the blocked-IP sets stop being silently reverted by a second writer -- Terraform declares `addresses = []` on all four |

**CARRIED, NOT CUT** -- the five round-1 graduations that never reached any slug (`3.0.0_SA_CVO~Z`'s
C-S35). They need no cell; they need to not be lost again. They are carried in `COMPLETION_REPORT.round2`
so the join exists in a record rather than in a seat's memory. **The analysis ranks this ABOVE the row
gate's cost curve, because it loses security findings SILENTLY -- and it did, for a full round.**

**OUT OF SCOPE, and named so the recut does not absorb it:** the rotation stop, whose remedies are
already APPLIED on the deployed plane -- not a recut item, and also not yet a REALIZED grade.

---

## 1a. The cells

### `OP3-s-1` -- FWD-19, and it is CUT FIRST

**Serves:** FWD-19 as ratified at v0.14, verbatim: *"Automated submissions and scraping against the
marketing site are refused or challenged, and a real visitor is never stopped."*
**DONE WHEN (EXERCISED):** a scripted submission refused or challenged with no human acting; a real
submission by a person in a browser succeeding unchanged **in the same window**; and the volume of
automated submissions reaching the entry store measured **before and after**.
**ACCEPT (v0.14 calibration, Andrew-direct):** the NAIVE MAJORITY of automated fillouts stop arriving,
real advisor enquiries still arrive, and someone can say by how much it changed. *"Naive majority is
fine for now."* **A sophisticated bot still getting through is NOT a failure of this outcome.**

⛔ **THE BASELINE CENSUS IS THE FIRST ACT OF THIS CELL AND ARMS NOTHING.** C-18: *"THE
BEFORE-MEASUREMENT MUST BE TAKEN BEFORE ANY CONTROL IS ARMED OR IT IS UNOBTAINABLE."* Cut without the
before, the outcome becomes ungradeable and the round is wasted on it. The census names its **window**,
its **denominator** and its **automated/human discriminator**, and runs against the Gravity Forms entry
store and the origin access logs. It is a **re-run, not a new build** -- the same instrument censused
620,837 request lines on this box for `TO-OP-S-13`.

**BOUNDS, all three from PRD 7.6 and all three refusal-shaped:**
- **C-17** -- COUNT first; graduate to BLOCK/CHALLENGE **only on soak evidence**. *A control that
  refuses a real advisor enquiry is a VIOLATION of FWD-19, not a side effect of it.* Violated by: any
  rule entering BLOCK or CHALLENGE on day one; a graduation without soak evidence; a control with no
  measured false-positive read.
- **C-18** -- graded on volume before/after, **never on the control's existence**. Violated by: arming
  before the baseline is captured; grading on configuration; an after-read on a different window or
  denominator than the before-read.
- **C-19** -- the control set is bounded to what is achievable **WITHOUT A DNS CHANGE AT GODADDY**.
  ⛔ **THE EDGE HALF IS UNBUILDABLE, NOT DEFERRED:** AWS WAF cannot attach to a bare EC2, both candidate
  edges (CloudFront, ALB) need the record repointed at GoDaddy, and Route53 is no better because moving
  the zone changes the nameservers there. Measured 2026-09-09: apex and `www` both resolve to the EC2
  Elastic IP `18.208.18.213`, `server: LiteSpeed`, no CloudFront marker. **No time is spent on the apex.**

### `OP3-s-2` -- FWD-4's alarms reach a human

**Grounded on row `NFRA_OPSEC202609-Z-S151`** (GRADUATED, ARMED): *"FWD-4 IS GRADED COMPLETE AND CANNOT
BE SATISFIED: both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS."* The alarms exist
and fire into nothing; the subscription is the single open leg.

⭐ **THE RECIPIENT IS NO LONGER AN OPEN INPUT, WHICH IS WHY THIS IS CUTTABLE NOW AND WAS NOT BEFORE.**
Row `Z-S97` recorded the recipient as an input this project did not hold. **PRD v0.14 C-20 FWD-4-RECIPIENT
settles it: FWD-4's "named person" is `andrew@opalinvest.com`.** The cell reads C-20; it does not guess,
default to Andrew, or use a role address.

⛔ **THE ALERT MORATORIUM IS NOT BREACHED AND THE REASON IS NAMED RATHER THAN ASSUMED.** CLAUDE.md's
standing bar forbids building an alert/alarm/SNS-send/notification without Andrew's explicit ask. **FWD-4
is one of the SIX named exceptions** (FWD-4/5/6/12 by commissioning word, FWD-14/15 Andrew-direct
2026-09-02) and this cell BUILDS NOTHING NEW: the alarms and the topic already exist, and the act is
attaching the recipient C-20 names so an existing authorized alarm stops firing into a void. **No second
recipient, no new channel, no new cadence, no digest email** -- C-6's digest email remains NOT AUTHORISED.

### `OP3-s-3` -- the blocked-IP sets stop being reverted

**Grounded on row `NFRA_OPSEC202609-Z-S136`** (GRADUATED, ARMED): *"TERRAFORM IS A SECOND WRITER OF THE
BLOCKED-IP SETS AND C-2 CANNOT SEE IT. All FOUR sets declare `addresses = []`."*

The contradiction is that the auto-block framework's whole purpose is to put an address into a set and
keep it there, while the declared state says every set is empty -- so the next apply silently reverts
every runtime block. **A control that reverts itself on a schedule nobody watches is worse than an
absent one, because the register records it as present.**

---

## 2. The four-postulate record (Rule 24)

**(i) MECE over a DECLARED domain.** Domain = *what the round-2 analysis sends back*. Partition:
{the one uncovered outcome} + {the priority remediations it names} + {carried, needing no cell} +
{out of scope, named}. The uncovered member was hunted and is FWD-19 -- and it is uncovered for a
mechanical reason, not drift: it was ratified at v0.14 AFTER round 2's decomposition was frozen, and a
frozen decomposition cannot grow a cell mid-round. **That is the rule working, not failing.**

**(ii) SAME GRAIN.** Every cell is one outcome-serving act with its own exercise. `OP3-s-1` is not
"do FWD-19" but a baseline, a control and an after-read on one window.

**(iii) INTENT COHERENCE.** One axis: *close the gap the round-2 analysis measured*. Not "improve
security", which would readmit the 67 other ARMED rows and make the round unclosable.

**(iv) STATE COHERENCE -- what one remedy does NOT move.** `OP3-s-2` moves FWD-4's delivery leg and
moves **nothing** about whether the alarms' thresholds are right. `OP3-s-3` moves the persistence of a
blocked address and moves **nothing** about which addresses deserve blocking. `OP3-s-1` moves the naive
majority and, by ACCEPT, **explicitly does not** move sophisticated bots.

---

## 3. Placement axis

All three cells execute on the **site-Z fabric** (`project.json` `fabric: site-z`). `OP3-s-1`'s subject
is the marketing site on the EC2 box reachable from here; `OP3-s-2` and `OP3-s-3` are AWS-plane acts in
this account.

## 4. Dependency edges, keyed to OBSERVED completion

```
OP3-s-1  baseline census --[the census artifact EXISTS and names window/denominator/discriminator]-->
         OP3-s-1  control armed --[soak window observed]--> OP3-s-1 after-read
         (an INTRA-cell ordering, and it is the cell's whole risk: it is not an edge to another cell)

OP3-s-2  depends on NOTHING.   OP3-s-3  depends on NOTHING.
```

**THREE INDEPENDENT CHAINS.** `OP3-s-1`, `OP3-s-2` and `OP3-s-3` share no edge, so they may run
concurrently. Fan-out is therefore **3 of 3 chains**, under the default cap of 8.

## 5. What this decomp REFUSES to assume

- **No APPLIED-plane fact is this seat's.** Every "the world is X" above is a row's measurement or a PRD
  constraint, cited by id, and the worker re-grounds it as its first act.
- **No monitor beyond the six exceptions**, and `OP3-s-2` is inside one and builds nothing new.
- **No control is armed before its baseline** (C-18), and no cell may satisfy itself on configuration.
- **No time on the apex / GoDaddy** (C-19) -- the edge half is unbuildable, not scheduled.
- **No cell is owned by a Tier-0 or Tier-1 seat.** All three go to worker subagents at L7.
- **The other 67 ARMED rows are not silently dropped** -- they are sequenced to a later round by this
  seat's L5 call, which the analysis expressly assigns here, and they remain GRADUATED and ARMED on the
  channel where the next slug reads them.

## 6. Holds

**NONE.** No cell here waits on Andrew. FWD-19 is already ratified AND calibrated by him and needs
building, not deciding; C-20 settles FWD-4's recipient; `OP3-s-3` is a declared-state correction.
The analysis says it plainly: *"NOTHING IS OWED BY ANDREW."*
