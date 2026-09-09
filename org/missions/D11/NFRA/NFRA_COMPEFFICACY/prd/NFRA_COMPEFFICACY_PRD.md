# NFRA_COMPEFFICACY — comp-tool efficacy: every named comp-tool validated per-tool, remediated, and CLEARED

**Directive:** D11 Substrate/Tooling Enhancements (Andrew-direct 2026-09-02, VERBATIM: *"This would go in D11
Substrate/Tooling."*) · **Fabric:** laptop (D11 placement row; membership and fabric agree, per the ETFS_GUARDRAIL
D8 precedent) · **dep_stage:** PRD
**Author (draft; step-3 input @`86a5538003`):** `3.0.0_SA_CVO` (the Andrew-designated comp-tool lane @`98b1a59907`; NOT the driver from L4 on — Andrew-direct at the CVO terminal 2026-09-03 ~02:1xZ, VERBATIM *"you are not going to be driving this, we are doing canonical order flow"*, record @`96af269f47`; the canonical roles are the Limb-check record @`9a4d508ae5`: L2–L4 CTO only, L5–L6 COO only, CVO first engaged at L8) · **L4 owner:** `1.0.0_SA_CTO` · **Executor:** `0.8.0_AE_CloudComp`
(Andrew-direct @`1bb6769055`) · **Sequencer:** `2.0.0_SA_COO` · **PRD gate:** `1.0.0_SA_CTO` · **Register owner:** `0.0.0_AB_MSTR`
**Version:** v0.8, 2026-09-04 (**v0.8 = FWD-5's written answers landed as s.5a from CE-q-1 @22388f7195 -- the CVO's text, the CTO's version, on Andrew's "a" (the project closes on its CVO limbs) and the round-6 analysis @de9a194c7b; no outcome, ruling or manifest row changed. v0.7 = s.7 rows G-2 and G-3 CARRIED to `NFRA_CLDGRPH`'s cells CG-s-8 / CG-s-9 / CG-x-7 on the L5 owner's tick-7 call -- the sibling's port retires the very surface these cells would bound, so an order here would be a second writer on an engine being ported (the S15 precedent); FWD-7's ask keeps an owner, which is its `DONE WHEN APPLIED` bar; no FWD changed**; v0.6 = the second L2 re-entry, on the round-5 `SCOPE_CHANGE` route S17 (3.0.0_SA_CVO stamp @b5d228fe62), adjudicated by the L4 owner -- record `CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T1535Z.md`: R-4's condition measured NOT MET, comp-trace NOT retired, T-19 CLOSED NOT-RETIRED, the three carryable flags into blast under CE-t-6; s.6 R-4 and s.7 T-19 corrected; no FWD changed**; v0.5 = the L2 re-entry on the round-4 `SCOPE_CHANGE` route S14 (3.0.0_SA_CVO stamp @153522a509), adjudicated by the L4 owner under spine v2.3 -- record `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T0930Z.md`: FWD-10 appended (a verdict-bearing tool never returns its clean verdict from a partial run), s.4.4 gains the `verdict-bearing` row of Rule T's form, s.4.3 gains the distinguishability GRAIN sentence (T-7 F2)**; v0.4 = the two STAGE-0 decisions; v0.2 landed at the tree home @e906c6f156 -- L4; v0.3 = 3.0.0_SA_CVO's four L4-read deltas D1-D4 + the AC reading rule, 00:3xZ; **v0.4 = the two STAGE-0 decisions landed at L4 on the L4 owner's authority after 2.0.0_SA_COO withdrew TO-CE-DISC-2 and TO-CE-TP-1 (92927, Andrew-direct ~02:2xZ *"Only tier2 agents are workers"*): s.4.3's four answer-state spellings RATIFIED AS DATA in `org/standards/COMPTOOL_ANSWER_STATE.enum.json` + s.4.7's "until ratified" clause closed + the NOT_APPLICABLE finding; s.4.4 carries RULE T's FORM (input 3.0.0_SA_CVO 92932, two amendments); the roles line above**) · **Vintage of every measurement below:** repo HEAD `f90ab3936b` unless a cell pins otherwise
**archetype:** IMPLEMENT (spec) / VALIDATE (rows)

```json

{
  "project": "NFRA_COMPEFFICACY",
  "directive": "D11",
  "fabric": "laptop",
  "prd_version": "v0.9",
  "step": 4,
  "brief_ref": "org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md@f90ab3936b",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10"
  ],
  "status": "RATIFIED"
}
```
*PRD_HEADER block (`org/standards/PRD_HEADER.schema.json`; limb 5 of `to-pipeline-gate.py` @`689960ce16`). `brief_ref` is
the Andrew-direct RECORD, not a `docs/briefs` file — admitted by the pattern widened @`75ead40079` on this seat's Rule 24
finding. `status` flips to `RATIFIED` when `1.0.0_SA_CTO` lands this at `docs/architecture/NFRA_COMPEFFICACY_PRD.md`.*

---

## 0. AUTHORITY — his words, verbatim

Record: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md`
@`f90ab3936b`. The operative clauses:

> "...draft a spec that covers end to end how to validate and streamline their purpose, how they are called, their
> timeout and pagination mechanics, any disclosures on denominator/coverage/risk factors. I need you to drive this
> project with 0.8.0_AE_CloudComp to completion where the desired final output is complete efficacy with all of
> these functions, this is why I had CRO send you the passcraft analysis, to assist in your validation and
> remediation process for these tools. I think you need to start by listing/enumerating the tool list we described
> and then we methodically go through all of them, whereby you hand off the list to 0.8.0_AE, they go through each
> tool and return results in a specified schema deliverable that covers everything we need, you review those and
> mark the tool cleared. This is one project I need you to proceed, i think while you are on the subject we can also
> have you and 0.8.0_AE address the globgraph-cloud-compile-and-gateway-traversal-20260901.md brief that CRO did
> yesterday since it is directly related to the efficacy of these tools."

> "This would go in D11 Substrate/Tooling."

Prior word, same thread (CloudComp terminal ~16:53Z, @`1bb6769055`): *"...team up with CVO Base ... comprehensive
audit and fix of the tools of interest, and I want them to parallelize that work through a delegation process with you."*

**Two rulings he has separately given that bind rows below:** *"comp-kuzu/kuzu-inc should be consolidated as
described"* (held on the KUZUSPLIT reconciliation now at him — §6 R-3) and *"comp-trace ... if so it should be
retired"* (condition met — §7 row T-19).

---

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  Every tool Andrew named is on one list, and the two names that are not tools are on it as such
         DONE WHEN  APPLIED -- the list is in the PRD
         ACCEPT     Andrew can read the list and find every tool he named, the three roll-up
                    questions attached to the one he asked about, and the two names that turned
                    out not to be tools -- without asking where anything went
         SOURCE     brief :13 "take every single comp-tool i mentioned"; :33-34 "start by
                    listing/enumerating the tool list"; :78-81 (CVO's scope resolution: two named
                    tools do not exist and are "recorded as such, not silently dropped")

  FWD-2  Each tool has one written account -- what it is for, how you call it, what happens when
         it runs long, how it pages through results -- and every account is in the same shape
         DONE WHEN  EXERCISED -- at least one account has been filled by the executor and read by
                    the reviewer, and the shape survived the reading
         ACCEPT     a reader who has never used the tool can tell from its account what it is for
                    and how to call it, and any two accounts can be laid side by side and compared
                    line for line
         SOURCE     brief :28-30 "draft a spec that covers end to end how to validate and
                    streamline their purpose, how they are called, their timeout and pagination
                    mechanics"; :35-36 "return results in a specified schema deliverable"

  FWD-3  Each tool says what it counted and what it could not see -- in its account and in its own
         output when it runs
         DONE WHEN  EXERCISED -- a real run's output has been read against its stated disclosure
         ACCEPT     when a tool answers, the reader can see how much of the estate it looked at and
                    what it might have missed, without having to know how the tool works
         SOURCE     brief :30 "any disclosures on denominator/coverage/risk factors"

  FWD-4  Every tool on the list ends in one of three states -- cleared by the reviewer, retired or
         merged by Andrew's ruling, or elevated to the short list -- and none is left in limbo
         DONE WHEN  EXERCISED -- the last tool's state has been read by Andrew
         ACCEPT     Andrew can ask about any tool on his list and get one of three answers --
                    cleared, retired-or-merged with his ruling cited, or on the short list -- and
                    never "we have not got to it"
         SOURCE     brief :31 "the desired final output is complete efficacy with all of these
                    functions"; :36-37 "you review those and mark the tool cleared"; :14-15 "retire/
                    archive groups of comp-tools and elevate a few to the marquis list"; :73-77
                    (retirements are findings with owners, not acts on this word alone)

  FWD-5  Andrew's specific questions are answered in writing: whether the one he was unsure of is a
         tool or a built-in; whether the deny-tester is needed in practice; whether the similarity
         tool supplants the three roll-ups; what the pulse, heat and system tools actually do and
         whether they work; whether trace is just dataflow; where cache sits against platinum, and
         how platinum's coverage universe is assembled
         DONE WHEN  APPLIED -- each question has a written answer he can dispute
         ACCEPT     for each question in his message there is an answer in plain English that says
                    what the thing actually does, and where he asked "is this just X?" the answer
                    says yes or no and why
         SOURCE     brief :15-27, the parenthetical questions in his own text; :22-24 the kuzu
                    one-command question (separately RULED per :75-76)

  FWD-6  The independent security review's findings about these tools are used up: each is fixed
         or accepted in writing with the reason
         DONE WHEN  EXERCISED -- the last finding has a disposition someone other than the fixer read
         ACCEPT     nothing that review flagged about these tools is left without a written
                    "fixed" or "not fixing, and here is why"
         SOURCE     brief :31-33 "this is why I had CRO send you the passcraft analysis, to assist
                    in your validation and remediation process"; :60-61 "an INPUT ... not a sibling
                    project"

  FWD-7  The cloud-compile and gateway-traversal brief is addressed inside this work, not parked
         DONE WHEN  APPLIED -- each of its asks is in the plan with an owner, or ruled out with a reason
         ACCEPT     someone reading that brief can find, for each thing it asks, where in this
                    project it is being done or the sentence saying why it is not
         SOURCE     brief :37-40 "also have you and 0.8.0_AE address the globgraph-cloud-compile-
                    and-gateway-traversal-20260901.md brief ... directly related to the efficacy
                    of these tools"; :62-63 (IN SCOPE)

  FWD-8  A short list of the tools everyone reaches for first exists, is the one Andrew ratified,
         and is what a seat actually starts from
         DONE WHEN  EXERCISED -- a seat has started a piece of work from the short list
         ACCEPT     an agent starting work can see the short list; it matches what Andrew said we
                    absolutely need; anything he named that is not on it has a stated reason
         SOURCE     brief :15 "elevate a few to the marquis list. The ones I know we absolutely
                    need are ..." (the enumeration stays in the PRD, not here)

  FWD-9  A tool cleared here stays cleared: the fix is on the shared branch, never only on one
         machine, and the tool behaves as cleared from any seat
         DONE WHEN  EXERCISED -- a cleared tool has been used from a seat other than the one that
                    fixed it, and behaved as cleared
         ACCEPT     a tool marked cleared can be used from any seat on any machine and behaves as
                    cleared; a fix that lives on one machine does not count as done
         SOURCE     brief :31 "the desired final output is complete efficacy with all of these
                    functions" (efficacy that evaporates on another clone is not complete); the
                    incompleteness was found in 3.0.0_SA_CVO's draft card FWD-6 (below, AC-6) at L4 --
                    RIGHT AND INCOMPLETE, so a NEW id at the next unused number (skill F0 rule), never
                    a renumbering

  FWD-10 A tool whose exit code is its verdict never returns the clean verdict from a partial run:
         at budget expiry it says so in its own voice and exits in a way no reader can mistake for
         clean, and it tells the reader where to resume
         DONE WHEN  EXERCISED -- a budget-cut sweep of a verdict-bearing tool has been read by an
                    rc-only consumer (a hook, a script, an `&&`) as NOT clean, and its resume cursor
                    has been followed to completion
         ACCEPT     for every marquis tool whose rc carries a verdict (a gate, a deny-test, a check):
                    at BUDGET REACHED the line prints as Rule T requires AND the rc is a non-clean value
                    distinct from both the clean verdict and the failing one, carrying the
                    PARTIAL_OR_BLIND state in the tool's voice (`NOT-DECIDABLE`); a consumer that reads
                    only the rc cannot read a prefix as CLEAN; the cursor resumes as in s.4.4
         SOURCE     brief :31 "complete efficacy with all of these functions" (a gate that reports CLEAN on
                    a sweep it did not finish has no efficacy); found at L7 by the comp-dataflow cell as
                    NFRA_COMPEFFICACY-S14 and routed SCOPE_CHANGE (REQUIRES_UNNAMED_OUTCOME) at the
                    round-4 L10 stamp; adjudicated at L2 by the L4 owner (CTO_ADJUDICATION record) --
                    RIGHT AND INCOMPLETE, a NEW id at the next unused number, never a renumbering
```


### Re-pointing record -- CVO's draft ids -> the landed ids (the ids above are the contract from this commit on)

`3.0.0_SA_CVO`'s draft (`NFRA_COMPEFFICACY_PRD_DRAFT_v0.1.md` @86a5538003, DRAFT, never at a home) carried its own
seven FWD cards at engineering grain. L2 (`/endpoint --forward` on the foundational record, Andrew's GO, @b886c164d2)
is the first list that LANDS, so its ids are the ones `outcome_ref` cites from here on. Every section-7 row was
re-pointed by this table (set union per row, deduplicated); CVO's cards are kept verbatim below as ACCEPTANCE
CRITERIA `AC-1..AC-7` -- the engineering tests behind the plain-English outcomes, not a second endpoint.

| CVO draft id | landed id(s) | why |
|---|---|---|
| FWD-1 (one schema, N deliverables) | FWD-2, FWD-4 | the account's shape + every tool dispositioned |
| FWD-2 (absence is machine-rejectable) | FWD-3 | what it could not see, stated so a reader can act on it |
| FWD-3 (where it looked, how much, how old) | FWD-3 | the disclosure |
| FWD-4 (a long/wide scan says what it did not finish) | FWD-2, FWD-3 | what happens when it runs long + the disclosure |
| FWD-5 (redundancy named with evidence; retirements on his ruling) | FWD-4, FWD-5, FWD-8 | dispositions, his questions answered, the short list |
| FWD-6 (a cleared tool stays cleared, on origin) | **FWD-9 (new)** | right and incomplete in L2 -- added, not renumbered |
| FWD-7 (graph tools answer from a bounded-age graph) | FWD-7 | the cloud-compile/gateway-traversal brief addressed |

**Reading rule (3.0.0_SA_CVO's L4 read, 00:31Z; no row of the table was wrong): a row closes on its AC where the AC is
stricter than the landed card.** NOTE A -- FWD-3 ("says what it could not see") does not carry AC-2's property that the
absence is MACHINE-REJECTABLE (four distinct answer states, planted not asserted); rows whose verb is 4.3 (T-1, T-2, T-16
and every 4.3 grade to come) close on AC-2, not on a disclosure sentence. NOTE B -- FWD-7 is DONE WHEN APPLIED (each ask
has an owner or is ruled out); AC-7 is EXERCISED (an answer from a bounded-age graph); rows G-1..G-3 close on AC-7.
Assigning owners meets FWD-7 and is not the end of the brief.

### Acceptance criteria at engineering grain -- 3.0.0_SA_CVO's draft cards, verbatim, relabelled AC-n


Emitted from his words alone, before any task order exists. `FWD-n` ids are **permanent and never reused**; a retired
outcome leaves its number vacant.

> ⛔ **"Frozen" is a CONTRACT here, not a CONTROL** — measured by this seat 2026-09-02 against its own gate:
> `.tools/surprise-row-gate.py:53` @`c6c3627269` validates `outcome_ref` by SHAPE (`^FWD-[0-9]+$`), never by
> existence. A row citing a FWD-n that was never cut passes. Named so the word is not read as a mechanism.

```
  AC-1  Every comp-tool on his list has been examined against ONE schema, and the
         result for each is on the record in that schema
         DONE WHEN  EXERCISED -- N per-tool deliverables exist, one per enumerated tool,
                    each conforming to s.4's schema, each graded by CVO
         ACCEPT     the enumerated list (s.7) has no row without a graded deliverable;
                    the two tools that do not exist are recorded as such, not skipped
         SOURCE     "start by listing/enumerating ... hand off the list ... return results
                    in a specified schema deliverable ... you review those and mark the
                    tool cleared"

  AC-2  A tool that cannot answer says so in a way a machine can reject, instead of
         returning a zero that reads like an answer
         DONE WHEN  EXERCISED -- for every CLEARED tool, a known-absent subject, a
                    present-with-zero-result subject, and a not-decidable case each
                    produce a DIFFERENT, rejectable answer-state
         ACCEPT     the four-state distinction of s.4.3 holds on every CLEARED tool,
                    tested with a planted case per state, not asserted
         SOURCE     "any disclosures on denominator/coverage/risk factors"; CVO~A brief s.3

  AC-3  Every CLEARED tool prints where it looked, how much, and how old
         DONE WHEN  EXERCISED -- engine path (not shim), corpus/backend, vintage,
                    denominator, resolved/unresolved counts appear on a live run
         ACCEPT     s.4.2's disclosure fields present on every CLEARED tool's default
                    output, verified by a reader who did not write the tool
         SOURCE     "their timeout and pagination mechanics, any disclosures on
                    denominator/coverage"; comp-similar D1-D3 (2026-09-02) is the
                    exemplar of the defect and its repair

  AC-4  A long or wide scan tells the operator what it did NOT finish, instead of
         stopping silently
         DONE WHEN  EXERCISED -- a CLEARED tool driven past its ceiling (time or size)
                    emits a truncation/timeout disclosure carrying the reached
                    denominator, and that disclosure is distinguishable from a clean
                    empty result
         ACCEPT     s.4.4 holds: no CLEARED tool has an unbounded subprocess; every
                    bound is disclosed at the ceiling; pagination, where present, prints
                    PAGE i of N and the true total
         SOURCE     "when we issue a timeout or if there's a default timeout ... we need
                    to know what's being truncated" (transcript 1056); MEASURED 76 of 94
                    implementations set no explicit timeout, 5 of 106 paginate

  AC-5  Redundant tools are named as redundant with evidence, and the ones he
         separately ruled on are consolidated
         DONE WHEN  EXERCISED -- comp-trace retired into comp-blast (his conditional
                    ruling, condition met); comp-kuzu/-inc/-full resolved per his
                    KUZUSPLIT reconciliation; comp-dups disposed by its owner; every
                    other candidate carries a finding with an owner, not an act
         ACCEPT     no tool is retired on this project's judgment alone; every
                    retirement cites his word or the owner's disposition
         SOURCE     "retire/archive groups of comp-tools and elevate a few to the
                    marquis list" -- a direction of inquiry; "if so it should be retired"
                    -- a ruling

  AC-6  A tool cleared here stays cleared: the fix reaches the shared branch and the
         tool has a battery that can go red
         DONE WHEN  EXERCISED -- every CLEARED tool's remediation commit is ON origin
                    (measured by is-ancestor, not claimed), and its battery collects >0
                    tests under the runner the gates use, with a planted mutant that
                    reddens it
         ACCEPT     no CLEARED status is granted on a LOCAL commit; comp-find, which has
                    3,722 invocations/30d and NO battery, gains one
         SOURCE     CVO~A brief NON-GOALS: "Do not leave a fix local: integration/
                    version availability is part of completion"; 92625 s.5(b)

  AC-7  The agent-facing graph tools answer from a graph whose age is bounded and
         disclosed, and the freshness surface points at the artifact agents actually
         read
         DONE WHEN  EXERCISED -- comp-graph status reports kuzu_nessie_db (not the two
                    legacy artifacts); every graph-derived answer from comp-kuzu /
                    comp-similar / comp-estate carries the DB's built: vintage; the
                    stale-served path (F5) is either bounded by a schedule or the
                    bound is stated on the answer
         ACCEPT     globgrph brief O3/O3b/O7 on the agent surface; F6 corrected; F4's
                    QUALIFIED verdict carried or fixed, never silently ported
         SOURCE     "address the globgraph-cloud-compile-and-gateway-traversal brief
                    ... directly related to the efficacy of these tools"; brief F4-F6
```

**Not cut, deliberately:** an outcome for "the marquis list." He said *"we may want to"* — the enumeration and
evidence in s.7 make that decision possible; making it is his.

> ⛔ **BINDING ON FWD-7 AND THE G-ROWS — Andrew-direct 2026-09-02 ~18:12Z, VERBATIM:** *"right now i think the
> estate pipeline is probably junk for the most part, until the tools at the front of that pipeline are properly
> rectified and generating real outputs/data, i dont think that pipeline makes sense to analyze analyses from."*
> **So the daily Semantic Evolution Pipeline is DOWNSTREAM of this project, not beside it.** Its outputs are not
> adjudicated until the tools it consumes are CLEARED here (the 24 PENDING manifest days stay PENDING by his word).
> This matches the measurement in §7 rows G-1..G-3 and the review §5b: the runner's propagation stratum returns
> `INSTRUMENT_UNAVAILABLE` daily and invokes zero comp-tools. **Not read into it:** stopping or changing the
> runner; it keeps running, nobody acts on its output. Record:
> `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1812Z_OPEN_CALLS_RULINGS_KUZU_ESTATE_NOTIFIER.md`.

---

## 1. The arc

The estate has **106 `comp-*` entrypoints over 94 distinct implementations**, and **61 of the 106 are wrappers**
that forward to an engine elsewhere. Measured 2026-09-02 across both usage instruments (because each is blind to
tools the other logs — the first defect this project found was in its own census): the top 20 tools carry
**99.6% of 30-day invocations**, so his instinct that ~20 tools matter is right. What is wrong is the coverage
underneath them: **5 of 106 paginate; 34 of 106 print a denominator; 18 of 94 set any timeout, with 14 different
constants nobody chose; 76 of 94 have no ceiling at all.** The most-run tool (comp-pulse, 8,364/30d) is a commit
hook that agents invoke by hand 5 times a month. The two most doctrinally central (comp-find, comp-read) were
invisible to the estate's own traffic feed until unit 1 landed today.

The same day produced the pattern this project exists to end, three times: **a tool that turns "subject absent",
"zero result" and "not decidable" into one answer.** comp-similar reported no vintage and its self-test scored the
missing half PASS (fixed @`b8a73cc064`). comp-pulse's traffic reads clean over a feed that omits comp-find. A
comp-kuzu build inside a call read as a laptop-local defect. Each was a correct number over the wrong denominator,
and each was caught by a second instrument, not by the tool.

**So the arc is not "make every tool cover everything."** It is: **every tool on his list tells the truth about its
own boundary, in fields a machine can reject on**, and the ones that are redundant are said to be — with evidence
and an owner — rather than quietly kept. CVO~A's brief states the bar exactly: *"A tool that clearly reports its
boundary is working; a tool that turns 'subject absent,' 'zero result,' and 'not decidable' into the same answer is
dangerous."*

**The method is his and it is prescribed** (s.0): enumerate (s.7) → one schema (s.4) → CloudComp fills it per tool →
CVO grades → CLEARED. The schema is the deliverable that makes the rest mechanical; it is authored here under
Rule 24 with its record and census (s.4.5).

---

## 2. Purpose — what DONE means

**DONE = "complete efficacy with all of these functions"** (his words), operationalised as: **every row in s.7 carries
a CVO-graded deliverable in the s.4 schema, and every row's disposition is one of:**

```
  CLEARED        the tool meets s.4.1-4.4 on a live run, its fix (if any) is ON origin,
                 and it has a battery that can go red
  RETIRED        on his word or the owner's disposition, with the replacement named and
                 callers redirected -- never on this project's judgment alone
  DOES-NOT-EXIST comp-hud, comp-legacy -- recorded, not dropped
  CARRIED        blocked on a named decision outside this project (e.g. R-3), with the
                 blocker's owner stated
```
No row may end in any other state. **A row that is "mostly fine" is not CLEARED.**

---

## 3. Territory — what this owns, and what it only relies on

| | |
|---|---|
| **OWNS** | the per-tool result **schema** (s.4); the **enumeration** (s.7) and each row's disposition; the **grading** of every CloudComp deliverable; the **disclosure contract** every CLEARED tool must meet; the **timeout/pagination policy** as a spec (s.4.4); the **globgrph brief workstream** at the agent-facing surface (FWD-7): `comp-graph status` correctness, vintage on graph-derived answers, the stale-served bound |
| **RELIES ON, does not own** | every tool's **code** (owner lanes; `0.8.0_AE_CloudComp` executes fixes in its lane, other lanes via placement); `.tools/tests` batteries (ownership at Andrew, CTO 92581); `comp-tool-hud.sh` and the rail (CloudComp by CTO ruling; the intermittency diagnosis is released there and this project CONSUMES it); `org/mcp/comp-tool-runs.jsonl` + `comp-which-rail.log` (the two usage instruments); `NFRA_PASSCRAFT`'s 8 moves + 12 shapes (`docs/architecture/NFRA_PASSCRAFT_PRD.md` @`362272cce2` §3a/3b — cited, never re-derived); the `boundary_report` type (`org/modules/graph/boundary_report.py`, dict-native — the disclosure contract is a sibling, not a rival) |
| **TOUCHES BUT MUST NOT CHANGE** | **`NFRA_KUZUSPLIT`'s full/inc semantics** — the NEVER-full property must survive any consolidation (§6 R-3); **`NFRA_GLOBGRPH`'s derive / Nessie / stitch** (CLOSED-COMPLETE; globgrph brief Part II puts them OUT); **CTO arch-gate ruling 3** separating comp-dups from comp-similar (the disposition is CTO's); **truthful non-application** — comp-schedule's NOT-DECIDABLE and comp-denytest's zero population are correct results and are not converted into work (CVO~A s.11) |

---

## 4. THE PER-TOOL RESULT SCHEMA — what `0.8.0_AE_CloudComp` returns for each tool, and what CVO grades

One file per tool, one fenced JSON block + prose. **HOME (corrected 2026-09-02, CloudComp 92803 + COO 92809):**
the project tree, which NFRA_COMPEFFICACY entered at L3 @`41d11d178d` (2026-09-03 00:0xZ): `org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/<serial>/<tool>.result.md`
(lane TREE_DELIVERABLES resolves the owner from `<serial>/`, CTO @`20d1c60866`, ruled @`5f8b774a5d`). The interim home
was the filler's own lane (`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPEFFICACY_T16_<tool>.result.md`);
CloudComp's T-16 file may move to the tree home bytes-unchanged at CloudComp's hand (D1, CVO 00:31Z). The
first draft named `org/projects/NFRA_COMPEFFICACY/results/`, an ANY_EXEC lane the filler could not commit to;
safe-commit refused it and the first deliverable landed in the filler's lane with its bytes unchanged. Every
field is REQUIRED; a missing field is a non-conforming deliverable and is returned, not graded.

### 4.1 IDENTITY — the wrong-object trap, closed at the schema
```
  tool            the entrypoint name as typed                          e.g. comp-similar
  shim_path       .tools/<name>, with its line count                    e.g. .tools/comp-similar (38)
  engine_path     the RESOLVED implementation, read from the shim body  e.g. org/modules/graph/debtscan/comp_similar.py (538)
  engine_vintage  git log -1 --format=%h -- <engine_path>
  aliases         other entrypoints resolving to the same engine        e.g. comp-kuzu-inc -> kuzu_cli.py --mode inc
  purpose_1line   from the ENGINE's header, not the shim's
  self_identifies whether --help/--about prints engine_path + version    (CVO~A s.9; passcraft MOVE 1)
```
> Both of this seat's wrong-object errors today (comp-dups, comp-trace) were shim-header reads. The schema makes
> the engine the object; the shim is a pointer.

### 4.2 DISCLOSURE — what every default run must print (CVO~A s.3, adopted)
```
  subject               the exact subject the run examined
  corpus_or_backend     what was examined (repo corpus / kuzu DB / AWS plane / portal src / ...)
  vintage               corpus or build vintage, as the tool prints it     ABSENT is a finding
  denominator           N scanned, as printed                              ABSENT is a finding
  resolved_unresolved   counts, as printed
  blind_spots           declared blind spots, as printed                   (e.g. comp-iam "cannot answer deny")
  pagination            {none | PAGE i of N with true total | truncates silently}
  timeout               {none | explicit N s | inherited from caller}, and what is printed AT the ceiling
```
Each is graded PRESENT / ABSENT / PRESENT-BUT-WRONG with the run's own output quoted.

### 4.3 ANSWER-STATE — the four-way distinction, tested not asserted
For each tool, CloudComp plants one case per state and records what the tool printed:
```
  SUBJECT_ABSENT_FROM_CORPUS   the subject does not exist where the tool looks
  PRESENT_WITH_ZERO_RESULTS    the subject exists; the measured answer is genuinely zero
  PARTIAL_OR_BLIND             the tool examined part of the space and says which part
  NOT_APPLICABLE               the question does not apply to this subject/tool
```
**PASS** = four cases, four distinguishable outputs. **FAIL** = any two states print alike. This is FWD-2 and it is
the load-bearing test of the project. **GRAIN (v0.5, T-7 F2, CTO adjudication):** distinguishability is judged within
ONE invocation's output by the STATE TOKEN in the tool's own voice; two subcommands answering two questions may share an
rc, but each must print which of the four states it is -- a bare REFUSE shape whose state is carried only by the echoed
argument is FAIL on the token, not on the rc. **RATIFIED AS DATA (v0.4, L4, `1.0.0_SA_CTO`): the four state names above ARE the
spellings — `org/standards/COMPTOOL_ANSWER_STATE.enum.json`, exactly one per state; the keys of every deliverable's
`answer_state` block are compared against that file (T-16 @`d101d4fe20` already conforms, 4 of 4), and a key outside it
is a non-conforming deliverable (s.4). Where a LIVE carrier prints a state in a tool's own voice the file ADOPTS that
token as the state's tool-voice: `PARTIAL_OR_BLIND` <- `NOT-DECIDABLE` (comp-schedule, exercised 02:18Z), `NOT_APPLICABLE`
<- `NOT_APPLICABLE` (nerves_resolve); `SUBJECT_ABSENT_FROM_CORPUS` and `PRESENT_WITH_ZERO_RESULTS` are minted (no code
carrier; comp-find's denominator shape is their kin, not a token). Rule 24 record + census: s.4.7 and the file. It binds
BY READING — no code consumer, no gate (s.5).**

### 4.4 BOUNDS — timeout and pagination mechanics
```
  subprocess_timeouts   every timeout= in the engine, with value and what it wraps
  ceiling_behaviour     what the tool prints when it hits one (exercised, not read)
  page_contract         --page/--limit present? true total printed? "PAGE i of N"?
  size_invariance       does the ceiling scale with corpus width, or is it a constant?
```
**POSTURE — Andrew-approved 2026-09-02 ~18:38Z, VERBATIM: *"I agree with this posturing, incorporate it into the
document."*** Two rules, both size-invariant by construction; measured baseline in §4.4.1.

**RULE P (output): comp-find's page contract is the SHARED OUTPUT CONTRACT, not a shared library.** Every marquis
tool that can emit more than one page of rows carries `--limit` / `--page` / `--all`, prints `PAGE i of N` and the
**TRUE TOTAL on every page**, and treats a bare `--top N` that does not print what it dropped as **non-conforming**.
The consumer half already exists in law (CLAUDE.md Rule 21: never `head` a census; a page is not an answer).
Size-invariance comes from the page, never from making output smaller.

**RULE T (work): a tool never exceeds a ceiling it was not told.** Every marquis tool **accepts a budget** (flag or
env; default 90 s, BELOW the harness's 120 s Bash ceiling — THE FORM below), **spends it against the WORK, not the
call**, and at expiry **prints the reached denominator with a resume cursor** — *"scanned 12,400 of 144,933 when the
budget hit; re-run `--cursor <last-unit>` / `--budget 600`."* A timeout thereby becomes a page boundary, not a kill.
**P and T are one solution:** a time budget that ends on a resumable cursor IS pagination over work. Internal
`timeout=` constants stay but must be **≤ the declared budget** or they are dead code.

**RULE T's FORM (v0.4, L4 landing by `1.0.0_SA_CTO`; input `3.0.0_SA_CVO`'s decision record @`790d92c6fa` + msg 92932,
adopted with two amendments — B1 the source word on the line, B2 the non-application corrected below; the record is
history, this section is the ONE carrier):**
```
  carrier         --budget <seconds>  >  env COMP_BUDGET_S  >  the tool's documented default
  default         90 s -- BELOW the 120 s outer ceiling, so the tool always speaks before the harness kills it
  unbounded       --budget 0 -> the denominator line prints "budget: unbounded (--budget 0)"
  on every        "budget: <S> s (flag | env COMP_BUDGET_S | default)" -- the SOURCE word travels with the value
  denominator     (a value must carry its claim: without it a reader cannot tell where a ceiling came from)
  at expiry       on stdout, BEFORE the summary, rc stays 0 (the LINE is the rejectable state, not the rc):
                  "BUDGET REACHED: <S> s (<source>); scanned <n> of <N> <unit>; results are a PREFIX, not the
                   answer; resume: <tool> <args> --cursor <last-unit>"
  on completion   "WITHIN BUDGET: scanned <N> of <N> <unit>; budget: <S> s (<source>), used <t> s"
  verdict-bearing (v0.5, FWD-10, S14) a tool whose rc IS its verdict -- a gate, a deny-test, a check -- prints the
                  BUDGET REACHED line exactly as above and returns a NON-CLEAN rc distinct from both the clean
                  verdict and the failing one, carrying PARTIAL_OR_BLIND in its own voice ("NOT-DECIDABLE", the
                  enum's tool-voice token; iam_cli.py returns it as rc 2 today); the "rc stays 0" clause above
                  governs every NON-verdict tool and nothing else; the cursor is unchanged. A verdict-bearing tool
                  that returns its clean rc at expiry FAILS Rule T whatever its line says.
  cursor          the last FULLY processed unit in the tool's DETERMINISTIC scan order; --cursor resumes after
                  it; the union of runs reaches N (size-invariant by construction -- Rule P along time)
  subprocesses    every timeout= derives from remaining(); a call that would outlive the budget is DEFERRED in
                  T-16's always-printed bucket: "DEFERRED: k of K <unit>(s) did not return -- each names its
                  reason below" (k may be 0; the bucket prints on a healthy run, so absence is never zero)
  discriminators  TWO, independent: D1 the token (WITHIN BUDGET | BUDGET REACHED); D2 "scanned n of N", n == N
                  vs n < N. Either alone separates the pair; a consumer greps one.
  shared code     ONE sibling `.tools/_compbudget.py`, never per-tool copies (build ladder rung 2)
```
**Word-boundary census at ratification** (`3.0.0_SA_CVO`, comp-find `--files --all`, ~145.9k files, 92932 C): `BUDGET
REACHED` 7 hits, all the decision record and its message copies (0 prior occupancy in code); `WITHIN BUDGET` 0;
`SCAN COMPLETE` 8 hits INCLUDING `infra/aws/nfra_terraform_p1/drift_scan.sh` — COLLIDES, not used; `COMP_BUDGET_S` 5,
all the record's own. **Uncovered member, named: KILLED-OUTSIDE** — the harness kills the process and NO line prints
(indistinguishable from a crash; live specimen 92932 E: a fourth comp-find sweep killed at a 300 s Bash ceiling, exit
143, no line). That is why the default sits below the outer ceiling; mitigated, never eliminated. **State coherence
(iv):** raising `--budget` moves BUDGET REACHED -> WITHIN BUDGET; it moves neither KILLED-OUTSIDE (only the harness
ceiling does) nor a DEFERRED-for-a-non-time-reason. **Grader's arm for every 4.4 grade from here:** plant `--budget 1`
on the default corpus -> BUDGET REACHED, n < N, rc 0, "(flag)"; plant `--budget 0` on a zero-hit pattern -> WITHIN
BUDGET, n == N, no "BUDGET REACHED"; `COMP_BUDGET_S=1` with no flag -> as the first with "(env COMP_BUDGET_S)";
`--cursor <unit>` -> "resumed after <unit>", n1 + n2 == N; a temp-copy mutant that prints the clean token at expiry
goes RED. Falsifier already exercised on the grammar (92932 D, scratch, no tool code): planted pair DISTINGUISHABLE,
mutant INDISTINGUISHABLE -> control fired, two runs STABLE, 3 arms of 3. **First target T-1 (`comp-find`), facts at
HEAD `96af269f47`:** `:158 timeout=600` wraps the comp-kuzu subprocess (`--corpus aws`), `:607 timeout=20` wraps the
telemetry sink; page contract present (`:240`, `:522` "PAGE i of N"); NO `--budget` / env / deadline / cursor anywhere
(census 0). Its 600 s inner constant EXCEEDS the outer ceiling — the dead-code clause above, live.

**Non-application (corrected v0.4, 92932 B2):** a tool with NO loop whose iteration count depends on corpus width AND
NO subprocess carrying a timeout constant (`comp-which`, `comp-denytest`, `comp-schedule`'s five carriers) carries Rule
P's disclosure line and nothing else. **Output caps do NOT make a tool non-application:** caps bound OUTPUT (Rule P),
not WALL-CLOCK — `comp-adversary` (caps 25/12/2400 B) is IN scope; its own T-16 grade reads `size_invariance.time`
*"NOT budgeted ... worst case 12 x 60 s = 720 s + 120 s comp-state, against a 120 s outer ceiling the tool cannot see"*
and Rule T *"NOT MET ... owed"* (`comp-adversary.result.md:71` @`d101d4fe20`); its route is the `subprocesses` clause
above (`comp-adversary:401-402` at HEAD). **Reference implementations:** T-1 (`comp-find`) and T-2 (`comp-read`) — the
only two that already satisfy P; T binds them first. **Cost, stated:** T is a code change on ~18 marquis
implementations; P on ~10.

#### 4.4.1 Measured baseline (2026-09-02, 20 marquis tools; help-text census + source grep)
```
  --page          2 of 20  (comp-find, comp-read)       --limit  3 of 20   --top  3 of 20   --all  4 of 20
  prints a true total when capped        8 of 20  (help-text heuristic -- weak; graded per tool in 4.2)
  knows / accepts the OUTER harness budget   0 of 19 implementations  (no BASH_*_TIMEOUT, --budget, deadline,
                                                                       SIGTERM handler, or alarm anywhere)
  outer ceiling the tools cannot see     120,000 ms default / 600,000 ms max (harness contract)
  inner ceilings                         18 of 94 set one; 14 distinct constants; comp-find's 600s EXCEEDS the outer
```
Live specimens the same day: comp-find killed silent at 120s twice (its 600s never reached); comp-similar imposing
180s on comp-kuzu from outside; the rail hook straddling its own 5s harness deadline and writing DENY rows for
searches that ran (fixed @`d2eb720bde` by raising the ceiling, confirmed at 4 of 4 Claude seats) — **every one is a
tool that did not know its budget.**

### 4.5 PASSCRAFT LEG — the 8 moves, run, and the shapes hunted
```
  moves_1_to_8    each: DONE / SLOT (hand-run) / N-A, with the falsifier's answer
  archetype       from the 12-shape taxonomy (comp-passcraft taxonomy), with lead probes hunted
  findings        each finding -> one of the 12 shapes, with file:line @ vintage
```
Cite `NFRA_PASSCRAFT_PRD.md` §3a/3b; do not restate the taxonomy in the deliverable.

### 4.6 USAGE + DISPOSITION PROPOSAL
```
  runs_30d        from BOTH instruments (runs.jsonl AND rail log), stated separately
                  TRAP (0.8.0_AE_CloudComp, unit 3a @4c3b848c97): the runs.jsonl SINK cuts
                  args_head at 80 chars (comp_log_auto.py:349), not the 200 the emitters pass.
                  A token-based acceptance on this sink matches ZERO rows while rows are being
                  written if the token sits past char 80 of "<tool> <args>" -- unit 1's passed
                  only because its args were short. Place the token inside the first 80 chars,
                  or count rows by tool+serial+rc, never by a late token.
  hook_driven     fraction of runs from a hook vs by hand
  battery         path, collects >0 under pytest?, has a red-first mutant?
                  TWO GRAINS, both stated (0.8.0_AE_CloudComp 92794, ARMED, disarmed by its
                  owner): "collects >0" at the FILE grain AND under the lane's DIRECTORY sweep
                  (pytest .tools/tests/). Measured 2026-09-02: 8 of 22 files abort collection
                  with a module-scope SystemExit, so the directory run sees 0 of 37 tests while
                  every per-file collect passes -- Rule 22's members-vs-shared trap on the
                  battery field itself. A FILE-grain PASS alone is written "FILE-grain only".
  overlap         tools it duplicates or subsumes, with the EXECUTABLE-BODY evidence
  proposed        CLEARED-candidate | RETIRE-candidate (owner named) | CARRIED (blocker named)
```

### 4.7 Rule 24 four-postulate record for this schema (authored here; CVO does not self-certify — `1.0.0_SA_CTO` gates)
- **(i) MECE over a DECLARED domain.** Domain = the tools in s.7. Every row has exactly one deliverable; every
  deliverable maps to one row. The two nonexistent tools get a DOES-NOT-EXIST deliverable, not silence.
- **(ii) SAME GRAIN.** One deliverable = one ENGINE. Aliases (comp-kuzu-inc, comp-trace) are fields on their
  engine's deliverable, not separate deliverables — which is what makes the overlap visible.
- **(iii) INTENT COHERENCE.** One axis: *does this tool tell the truth about its boundary.* The schema is not a
  status tracker and must not grow a `done` column; disposition lives in s.7, not in the deliverable.
- **(iv) STATE COHERENCE.** The answer-state enum (4.3) classifies a RUN, never a tool. A tool is not "ABSENT"; a
  run's subject is. No remedy moves NOT_APPLICABLE — it is a correct result (CVO~A s.11).
- **Census — RUN 2026-09-02 ~17:5xZ (word-boundary, 8-token alternation, `corpus=all`): 653 hits across
  144,933 files; DEF=4 SURFACED=44 CONFIG=307 TEST=3 DOC=288.** Per-token in CODE/DEF bands of first-party
  source (comp-read `--enumerate`, whole-value):
  ```
    DECLARED-NOT-APPLICABLE   x5   .tools/to-pipeline-gate.py:46 DISPOSITION_RE       (this seat's gate)
    NOT-DECIDABLE             x3   .tools/comp-schedule (the decidability schema)        (this seat's tool)
    NOT_APPLICABLE            x2   org/modules/graph/nerves_resolve.py
    INSTRUMENT_UNAVAILABLE    x1   infra/aws/ec2/estate-report-runner/estate_report_runner.py
    SUBJECT_ABSENT            0    (the single estate-wide hit was THIS draft)
    PRESENT_WITH_ZERO         0
    OUT-OF-CORPUS             0 in CODE/DEF -- lives in comp-find's PROSE output + CLAUDE.md Rule 21
  ```
  **WHAT THE CENSUS SETTLES:** two of 4.3's four states already have LIVE carriers and must ADOPT, not mint —
  `NOT_DECIDABLE` → **`NOT-DECIDABLE`** (comp-schedule's spelling; hyphen), and `NOT_APPLICABLE` already exists
  in TWO spellings (`NOT_APPLICABLE` underscore in nerves_resolve; `DECLARED-NOT-APPLICABLE` hyphen in my own
  gate) — **that split is a finding this project inherits, not one it may paper over.** The other two states
  (`SUBJECT_ABSENT_FROM_CORPUS`, `PRESENT_WITH_ZERO_RESULTS`) have **no carrier anywhere in code** and are
  genuinely new; comp-find's `OUT-OF-CORPUS` prose is the nearest kin to the first and should be reconciled
  with it rather than duplicated. **RATIFIED 2026-09-03 (v0.4, `1.0.0_SA_CTO`, L4): the spellings are DATA in
  `org/standards/COMPTOOL_ANSWER_STATE.enum.json`; 4.3 binds by reading against that file (no code consumer, no gate —
  s.5). Three corrections to the census reading above, carried in the file: (a) `NOT_DECIDABLE -> NOT-DECIDABLE` names
  the TOOL-VOICE token of the state `PARTIAL_OR_BLIND` (s.4.3's third state, exercised by T-16) — a tool's printed token
  and a state's spelling are two grains, and s.4.3 has no fifth state; `NOT_DECIDABLE` (underscore) has no code carrier
  and is retired as a spelling. (b) `DECLARED-NOT-APPLICABLE` is the preflight DISPOSITION enum of `to-pipeline-gate.py`
  (`:55` at HEAD `96af269f47`; `:46` above was a dated read) — an AUTHOR's declaration about a lens, a different axis
  (postulate iii), so the NOT_APPLICABLE "split" resolves to ONE spelling, `NOT_APPLICABLE` (nerves_resolve's, a RUN's
  answer), with NO change owed to the gate's token (owner `3.0.0_SA_CVO`; the finding, with the losing carrier and its
  owner, is in the file). (c) `OUT-OF-CORPUS` is not a token comp-find prints (comp-read `--enumerate` over
  `.tools/comp-find`, 615 lines: 0 hits; in code only as a comment, `.tools/_comprail.py:382`); it is the PROSE name
  CLAUDE.md Rule 21 gives comp-find's `0 hit(s) across 0 file(s)` shape, and that shape is `SUBJECT_ABSENT_FROM_CORPUS`'s
  kin — the pathspec, not the pattern, is the absent subject. T-16's `answer_state` keys already match, 4 of 4.** Cost of the census on this box: the 8-way alternation exceeded a 120s
  foreground ceiling twice and completed only in the background — itself a FWD-4 specimen on comp-find
  (its own 600s internal timeout exceeds the caller's ceiling, and nothing at the ceiling says so).

---

## 5. Out of scope — and truthful non-application is not work
- **Making blind tools fabricate** to satisfy a preflight (CVO~A NON-GOALS). A tool that prints NOT-DECIDABLE
  with a denominator has PASSED 4.3.
- **Widening every tool to every resource family.** ETFS is not added to comp-pipescript's registry because it
  appeared in one preflight (CVO~A s.9).
- **comp-schedule and comp-denytest remediation** on this run's evidence — both returned correct bounded results
  (CVO~A s.11). They are graded, not repaired.
- **The KUZUSPLIT semantics, the GLOBGRPH derive, D6 GraphQL, gateway auth** (globgrph brief Part II).
- **A cloud Kuzu coexisting indefinitely with a local Kuzu** — that is a duplicate output path and a NEVER (CLAUDE.md
  §5); any cloud port under FWD-7 is a port with a retirement or it is out of scope.
- **The marquis list decision.** Evidence yes; decision his.
- **Any gate.** Nothing here refuses anything. Andrew has not asked for one.

---

## 5a. His seven questions, answered in writing (FWD-5 -- CE-q-1: `3.0.0_SA_CVO` authors, `1.0.0_SA_CTO` lands)

The CVO's text from `../deliverables/3.0.0_SA_CVO/CE-q-1.seven-answers.md` @22388f7195, landed here unchanged at v0.8 as the
written answers FWD-5 names ("each question has a written answer he can dispute"). Each answer points at the s.7 row and the
proof-of-spec instance that measured it; every instance was re-validated by the CVO with the author read from git. What the
answers do not decide: the marquis list (s.5, his), any retirement (T-11, T-13 -- candidates surfaced; his and the CTO's), and
CE-g-4 (HELD, `CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260904T0715Z.md`). R-4 in s.6 is the same answer to question 4 in ruling form.

| # | His question | The answer | Row |
|---|---|---|---|
| 1 | **How is comp-platinum defined; what coverage universe?** | A composite: portal component dataflow -> routing table -> firm gold DAG (transform + routes + pipescript), page-first. Universe: **22 component files under `portal/src/pages`**, named by stem (four `index` stems collide and are disclosed as a limitation). One `--budget` carrier over the three legs; `page FactorTilts --budget 0` traced 3 of 3 components in 3.2 s at the issuer's FWD-9. Honest state: two of four boundary modes and the executable red-mutant arms are unbuilt (T24-AC2, AC5 disclosed as UNCOMPUTABLE-BY-CONSTRUCTION in the instance). | T-24 @`3052545c56` (0.8.0_AE_CloudComp~L), `comp-platinum.result.md` |
| 2 | **What does comp-system do?** | It compiles repository-local cross-surface evidence into `infra/system/06_current_state.{md,json}` -- the SYSTEM home's dynamic half (584 runs). `--check` is the auto-refresh verdict surface (rc 0 current / 2 / 1; `--check --budget` prints BUDGET REACHED, rc 3). Its invariant is no fabrication: an unreadable required source is named, the compile reads NOT-DECIDABLE with `compile_complete=false`, and no complete record is written on a partial. It is not a monitor and not a report; it is the compiler of one file pair. | T-21 @`82b73ff68f` (0.8.0_AE_CloudComp~N), `comp-system.result.md` |
| 3 | **Is comp-cache the same thing as comp-platinum?** | **No.** comp-cache is React Query cache-key analysis across `portal/src` (415 of 415 files scanned, 118 useQuery call sites captured) -- a portal-local grain: shared keys, collisions, type mismatches. comp-platinum is the portal-page -> gold-script plane. Different corpus, different question; the deliverable names the two planes apart. | T-23 (0.8.0_AE_CloudComp~J), `comp-cache.result.md` |
| 4 | **Is comp-trace just dataflow?** (and, the R-4 form: just a subset of blast?) | **No, on both.** Not dataflow: comp-dataflow answers origin / gate questions over pipeline data lineage with a verdict-bearing rc; comp-trace walks the code graph from a file or symbol. Not a subset of blast: measured two ways (S17, PRD v0.6 R-4) -- trace carries `--exact`, `--all` and the direction spellings that blast rejects (rc 1), and blast resolves only 38.6% of trace's own node ids (58.2% under the most generous mapping). R-4's condition failed, so its conditional ruling did not fire: comp-trace is **kept**, T-19 closed NOT-RETIRED, and the three carryable flags moved into blast under CE-t-6. (The decomp's cell text still reads "it is a subset of BLAST" -- that is the superseded v0.4 line-range read; this answer follows the measurement.) | T-19 WITHDRAWN / NOT-RETIRED; S17 @`a140eed779`; CE-t-6 @`dad11b5207` |
| 5 | **Is comp-denytest needed?** | It **works** (four exact answer states; a conditioned-grant false deny is deferred as NOT-DECIDABLE rc 2 rather than reported as a verdict; the AWS subprocess is Rule-T bound; battery 4 of 4) and it is **barely used**: 2 runs in 30 days, 8 ever; a zero population when no IAM change is in the plan is correct behaviour, not disuse. It is the only tool that derives the *expected* verdict from an IAM change type. **REC: keep**, as the gate-side check an IAM change runs, not a daily tool; its retirement is surfaced as a candidate on usage and the decision is yours. | T-11 @`7c2dbf6611` (0.8.0_AE_CloudComp~E), `comp-denytest.result.md` |
| 6 | **Does comp-similar supplant the three roll-ups (dups, drift, similar)?** | **No.** comp-similar compares *purpose summaries* (1,871 ARN resources; 1,514 with a summary, 357 UNKNOWN-thin) and joins heat; comp-dups compares *names and bodies* -- its own engine by CTO ruling 3, 0 runs ever, a RETIRE-candidate whose disposition is the CTO's; comp-drift is *propagation* across seam engines (13 topology bindings, 15 sweep units), not function. The overlap with similar is by name only. | T-12 @`685023581d` (~F); T-13 (CTO, record); T-14 @`9334701e71` (~G) |
| 7 | **What do comp-pulse and comp-heat do, and do they work?** | **comp-pulse** is the pre-commit risk reflex: 8,359 of 8,364 runs were the commit hook's `diff`, 5 by hand; it scores a proposed file set against the danger map before commit. It works (issuer FWD-9: rc 0, PRESENT_WITH_ZERO_RESULTS, a 1,906-node denominator) and it is a hook, not a morning read. **comp-heat** is a five-subcommand freshness / drift / score CLI over one git-history snapshot; it works as a CLI (four answer states, battery 2 tests / 8 subtests) and **is used by nothing**: 0 CLI runs, its only library consumer (`comp-similar.load_heat_live`) returned `{}` before reaching it (S29), the daily-report wiring @`09355b6d93` invokes it from nowhere. One grade against it stands in this round: T20-AC4 **FAIL** -- `comp-heat freshness` with no path scores the whole repo and accepts no `--budget` (adjudication C-S5). | T-18 @`cd5e84ae2f` (~M); T-20 @`4e96cfba07` (~I) |

---

## 6. Rulings that BIND
- **R-1 (Andrew, 16:53Z):** team with CVO base; delegation-parallelised. Lane ownership unchanged (three seats
  concurred: 92605/92607/92611).
- **R-2 (Andrew, 17:15Z):** the method — enumerate → schema deliverable → CVO grades → CLEARED. This PRD is that method.
- **R-3 (Andrew, 2026-07-17, KUZUSPLIT O-3) vs (Andrew, 2026-09-02, "consolidate"):** same engine, two words on
  the CLI surface. **HELD at Andrew** — reconciliation options put to him via `/open-calls` CALL 1. No kuzu wrapper
  moves until his word.
- **R-4 (Andrew, 2026-09-02):** *"comp-trace ... if so it should be retired."* **Condition NOT MET (v0.6, CTO
  adjudication `CTO_ADJUDICATION_NFRA_COMPEFFICACY_20260903T1535Z.md`, on S17 @a140eed779):** the v0.4 note "Condition
  MET (trace ⊂ blast at `cli.py:1478-1530`)" was the L4 owner's line-range read taken as a measurement; the lane
  measured two ways -- at the flag grain trace carries `--exact`, `--all` and the direction spellings that blast rejects
  (rc 1), and at the traversal grain the two tools answer over different graphs (blast resolves 38.6% of trace's own
  node ids; 58.2% under the most generous mapping). A conditional ruling whose condition fails does not fire:
  **comp-trace is NOT retired; T-19 closes NOT-RETIRED**; the three carryable flags enter blast under CE-t-6; the
  universe axis is the graph engine's (NFRA_CLDGRPH). This IS the written answer to his question for FWD-5.
- **R-5 (CTO arch-gate ruling 3, 2026-07-19):** comp-dups is its own tool, not a comp-similar mode. Disposition of
  comp-dups (0 runs ever) is CTO's.
- **R-6 (CLAUDE.md Rule 21, Andrew-direct 2026-08-28):** comp-find/comp-read are the rail. Their batteries and
  disclosure are P0 by traffic (3,722 + 2,401 / 30d).
- **R-7 (CVO adjudication 92566/92598, corroborated CTO 92568):** the rail log is a record of rows it managed to
  write, not a census of searches; no seat-coverage claim may be derived from it. Binds every usage figure here.

---

## 7. SURFACE MANIFEST (step 4 → step 5) — the enumeration, one row per ENGINE

Contract: the step-4 manifest as adopted @`ecaa7c7dcb` (amended: `claim: measured` requires a dated pin;
`BASIS_RANK` governs transitions). `outcome` = FWD-n. `claim` is about the SURFACE ADDRESS. `verb` ∈ {audit, fix,
retire, verify, record}. **Every row's lane is `0.8.0_AE_CloudComp` for `audit` unless stated; `fix` rows re-home to
the engine's owner if not CloudComp.** Usage = 30d, both instruments, at `f90ab3936b`.

| id | outcome_ref | surface (engine) | claim | evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| T-1 | FWD-2, FWD-3, FWD-4, FWD-9 | `comp-find` → `.tools/comp-find` (Python, self-contained) | measured | 3,722 runs (rail); **unit 1 @`f34122edfb` ON origin — now also writes runs.jsonl (0→2 `comp_log_auto` calls), CLEARED by exercise at this seat**; paginates (Rule P reference); 600s internal timeout **exceeds the 120s outer ceiling — Rule T's first target** | CloudComp | audit+fix | — | 4.1-4.6 | **BATTERY LANDED — unit 3b @`1e6206a267`** (`.tools/tests/test_comp_find_battery.py`, 6 arms on the measured output contract). CLEARED at this seat 21:5xZ by exercise: collect 0.05 s (import-inert), pytest 1 passed 11 s, direct 6/6 denominator 6, **a planted DENOMINATOR mutant in a temp copy → 5 of 6 arms RED, rc 1** (`COMP_FIND_TOOL` hook). FWD-6's battery gate is met. Still owed: Rule T budget + reached-denominator at expiry (600 s internal > 120 s outer) |
| T-2 | FWD-2, FWD-3, FWD-4, FWD-9 | `comp-read` → `.tools/comp-read` (Python) | measured | 2,401 runs (rail); **unit 1 @`f34122edfb` ON origin (0→2 `comp_log_auto`), CLEARED; `_shape()` shebang routing @`8ed23144cb` ON origin** (extensionless comp-* now parse via python-ast: 10→22 sections on comp-adversary); `--enumerate` writes NO rail row (92625 s.5a); battery 8/8 | CloudComp | audit+fix | — | 4.1-4.6 | enumerate-path logging gap is a finding, not a fix in this row; Rule P reference |
| T-3 | FWD-2, FWD-3, FWD-4 | `comp-which` → `.tools/comp-which` | measured | 520 runs.jsonl + 9,643 rail; paginates; 20/60s | CloudComp | audit | — | 4.1-4.6 | the router — its NOFIT-POSTERIOR path is a 4.3 case |
| T-4 | FWD-2, FWD-4 | `comp-hud` | absent | **no such entrypoint**; the HUD is `.tools/hooks/comp-tool-hud.sh` (a hook) | CVO | record | — | 4.1 | DOES-NOT-EXIST; rail hook is CloudComp's by ruling and OUT of this project |
| T-5 | FWD-2, FWD-3, FWD-4 | `comp-schedule` → `.tools/comp-schedule` (Python) | measured | 0 runs.jsonl/30d; five carriers; NOT-DECIDABLE is a designed result | CloudComp | audit | — | 4.1-4.6 | **no remediation on this run's evidence** (CVO~A s.11); ARNs absent BY DESIGN — record, do not "fix" |
| T-6 | FWD-2, FWD-3, FWD-4 | `comp-blast` → `org/modules/graph/cli.py blast` | measured | 167 runs; no explicit timeout | CloudComp | audit+fix | T-19 | 4.3 esp. | **NOT-FOUND ≠ zero radius** (CVO~A s.5): subject-existence check + graph vintage + node denominator |
| T-7 | FWD-2, FWD-3, FWD-4 | `comp-dataflow` → `comp_dataflow.py` | measured | 11 runs; `origin`/`gate` modes; no timeout | CloudComp | audit+fix | — | 4.3 | preserve 4/4 honest-unresolved; enrich unresolved print (CVO~A s.6); never guess through deploy-time config |
| T-8 | FWD-2, FWD-3, FWD-4 | `comp-iam` → `.tools/comp-iam` (Python, 14 subcommands) | measured | 113 runs; no timeout; "cannot answer deny" is a declared blind spot | CloudComp | audit+fix | — | 4.3 three-state | **effective-deny mode** (CVO~A s.8): explicit deny / no deny over complete carrier set / NOT DECIDABLE. Never "no parsed deny" → allowed |
| T-9 | FWD-2, FWD-3, FWD-4 | `comp-trigger` → `comp_trigger.py` | measured | 80 runs; EventBridge+Scheduler only; blind to S3 notifications (COO preflight) | CloudComp | audit+fix | — | 4.3 | declare scope in header OR add S3-notification backend via shared event graph — check existing machinery first (CVO~A s.7) |
| T-10 | FWD-2, FWD-3, FWD-4 | `comp-pipescript` → `.tools/comp-pipescript` | measured | 571 runs; 6 timeouts 10-30s; F9 gate GREEN @`4a6f564c6f` ON origin (141 passed, exercised on 5 later commits; 19/19; live arm asserts the PROPERTY not a pinned digest; **SKIPPED is a third verdict**, per CTO's Q5 ruling) — the tool itself untouched | CloudComp | audit+fix | — | 4.1 | shim self-identification (CVO~A s.9); do NOT add ETFS to registry on one preflight |
| T-11 | FWD-2, FWD-3, FWD-4 | `comp-denytest` → `.tools/comp-denytest` | measured | 2 runs/30d, 8 ever; zero population when no IAM change is CORRECT | CloudComp | audit | — | 4.1-4.6 | no remediation (CVO~A s.11); disposition on USAGE is his — RETIRE-candidate surfaced, not acted |
| T-12 | FWD-2, FWD-3, FWD-4, FWD-7, FWD-9 | `comp-similar` → `debtscan/comp_similar.py` | measured | 30 runs; D1-D3 fixed @`b8a73cc064` **ON origin** (is-ancestor of `c9ea7b3b63`, read 18:15:44Z); vintage prints, exercised at two seats | CloudComp | audit | — | FWD-6 | **integration condition MET** (CVO~A s.10). Remaining for CLEARED: the s.4 deliverable (identity, 4.3 four-case test, bounds); D1-D3 are the vintage/disclosure half only. ⛔ **DEPLOYED ≠ COMMITTED (CLAUDE.md 22a): `summary_corpus.py` is baked into the globgrph derive IMAGE, which carries PRE-fix bytes** (CloudComp 92718; owner `0.7.0_AE_CloudOps`) — the repo says D1 fixed, the running image says not; carried to G-rows |
| T-13 | FWD-2, FWD-4, FWD-5, FWD-8 | `comp-dups` → `debtscan/dup_scan.py` | measured | **0 runs ever**; separate engine by CTO ruling 3 (names+bodies vs summaries) | CTO | record | — | R-5 | RETIRE-candidate on usage; **do not fold** into comp-similar; CTO's disposition |
| T-14 | FWD-2, FWD-4, FWD-5, FWD-8 | `comp-drift` → `.tools/comp-drift` | measured | 1 run/30d; orchestrator over seam engines; `--deep` cost-guarded | CloudComp | audit | — | 4.1-4.6 | overlap with comp-similar is by NAME only (drift = propagation; similar = function) — record |
| T-15 | FWD-2, FWD-4 | `comp-legacy` | absent | **no such entrypoint** (0 of 106) | CVO | record | — | 4.1 | DOES-NOT-EXIST |
| T-16 | FWD-2, FWD-3, FWD-4, FWD-9 | `comp-adversary` → `.tools/comp-adversary` (Python, 526) | measured | 0 runs.jsonl/30d; gate-ENFORCED at `to-pipeline-gate.py:45`; **THREE surfaces (CloudComp 92718): TOOL — `:49` COMMIT_RE backtick + zero-pin guard @`a9dc767e34` ON origin (graded by this seat 15:29Z), digest-basis declaration @`8ed23144cb` ON origin; BATTERY — pass 1 @`e66d5e698d` ON origin (collector lives; 135 s import — PARTIAL), pass 2 @`03cf4d17a` **LOCAL** — P0.1 CLEARED at this seat 2026-09-02 19:3xZ by exercise: `--collect-only` → 1 collected in 0.07 s (2 s wall); module level now constants only, both `compose` calls inside functions (`:94`, `:142`); 1 file touched (+116/-85), production untouched; production MUTANT via `COMP_ADVERSARY_TOOL` temp copy → pytest FAIL on a real arm (1 of 7, rc 1) — the battery discriminates the TOOL, not just the runner** | CloudComp | audit+fix | — | CVO~A P0.1 **MET** | P0.1 limbs all met → RC5 may close (~A's call; CTO gate). **CLEARED @`bbba0db0e9`** (3.0.0_SA_CVO 92842, 2026-09-03 00:2xZ: the s.4 deliverable landed and both re-measurements met on CVO's own run; the row closes on AC-2 per the reading rule under the re-pointing table); **Unit-1 gap CLOSED — unit 3a @`4c3b848c97` ON origin: `comp_log_auto` 0→2; exercised at this seat, one `compose` → exactly one runs.jsonl row (serial, rc, args_head); the third traffic-feed blind spot is gone.** `--json` = native L0a form (ruled 92527), separate row |
| T-17 | FWD-2, FWD-3, FWD-4, FWD-7 | `comp-estate` → `org/modules/graph/opal_estate_infrastructure.py` | measured | 281 runs; `<name>`/`--list`/`--resource` | CloudComp | audit | T-22 | 4.2 | his word: *"need to lock in C(N) ontology for this to actually be useful"* — C(N) is `NFRA_C3MATERIALIZE` (D11 sibling); depends_on, not owns |
| T-18 | FWD-2, FWD-3, FWD-4 | `comp-pulse` → `org/modules/graph/comp_pulse.py` (707) | measured | **8,364 runs, 8,359 = `diff` from the commit hook; 5 by hand**; L2 traffic source = runs.jsonl | CloudComp | audit | T-1,T-2 | 4.2 | it is a HOOK, not a morning read; its traffic was blind to T-1/T-2 until unit 1 — re-measure after |
| T-19 | FWD-4, FWD-5, FWD-8 | `comp-trace` → `org/modules/graph/cli.py trace` | measured (v0.6: two instruments, S17) | 45 runs; **NOT a subset of blast** -- flags `--exact`/`--all`/direction spellings blast rejects; blast resolves 38.6% of trace's node ids (58.2% best mapping) | CloudComp | **keep -- CLOSED NOT-RETIRED** | T-6 | R-4 | his conditional ruling, **condition NOT MET**; the three carryable flags move into blast under CE-t-6; the universe axis is NFRA_CLDGRPH's; the 45 callers keep comp-trace; **not platinum** |
| T-20 | FWD-2, FWD-3, FWD-4 | `comp-heat` → `.tools/comp-heat` (377) | measured | 0 CLI runs; library consumer = comp-similar `load_heat_live()`; named in the estate-report runner's docstring, **invoked by nothing** | CloudComp | audit | — | 4.2 | his interest; "delivered/described better" — the disclosure fields ARE that; wiring into the daily report is `@09355b6d93`'s, not this row's |
| T-21 | FWD-2, FWD-3, FWD-4 | `comp-system` → `org/modules/graph/comp_system.py` (1751) | measured | 584 runs; compiles `infra/system/06_current_state.{md,json}`; `--check` 0/2/1; self-test carries the no-fabrication invariant | CloudComp | audit | — | 4.2 | his ask: "understand what this one does" — the deliverable's purpose_1line + 4.2 answer it; it regenerated on unit 1's commit (side effect, not a scope widening) |
| T-22 | FWD-4, FWD-5, FWD-7, FWD-8 | `comp-kuzu` + `comp-kuzu-inc` + `comp-kuzu-full` → `infra/aws/globgrph/kuzu_cli.py` (`--mode inc|full`) | measured | 1,591 + 14 + ? runs; three wrappers, one engine, one flag | CloudComp | **retire** | — | R-3 **RULED (a)** | **UNHELD 18:12Z — Andrew: "recs approved except 2."** `--mode inc|full` is the surface (already exists: `kuzu_cli.py:165`, choices auto/full/inc); both name-wrappers retire; NEVER-full moves onto `--mode inc` EXPLICITLY. ⛔ **RE-SCOPED 19:3xZ on CloudComp's census (92718, denominator 145,054 files): ~15 LIVE carriers, not 5** — comp-describe, comp-kuzu, both wrappers, comp-which, `kuzu_cli.py:39/:168`, COMPTOOL_REGISTRATION_FLOW.md, comp-coverage-map.yaml, comp-output-contracts.yaml, comp-tools.yaml, NFRA_COMPREG.json, NFRA_KUZUSPLIT.json, KUZUSPLIT PRD, two dated briefs. **Split by lane, not one commit:** CODE+REGISTRY carriers (CloudComp, one commit) · KUZUSPLIT PRD P1/P3 (CTO, same window) · the two briefs are dated RECORDS and are NOT rewritten. **CODE HALF LANDED @`dffbee781c` (15 files, +87/−145, LOCAL) — CLEARED by exercise at this seat 21:1xZ:** both wrappers deleted; forwarders no longer resolve on this device (positive control `comp-kuzu` resolves); `retired_aliases` declared with successor + dated order (manifest `:63`, `:75`); `comp-manifest-check retired-alias` PASS (9 declared / 99 live); `--mode inc` on a live query took the inc branch, 6 s, 27,122 nodes, `built:` unchanged; comp-which routes "behind" → `--mode inc` and "full reset" → `--mode full`. **Still open: the KUZUSPLIT PRD P1/P3 amendment (CTO) — until it lands, the PRD text names wrappers that do not exist.** Acceptance baseline for this unit: `comp-which-routing-baseline.json` @`610bb9e31e` (the routing test rewrote it mid-edit; CloudComp measured and recorded it rather than letting the 74-file revert closure look reopened). Forwarders on OTHER devices are DESIRED until each re-provisions (the provisioner only ADDS; a stale one fails loud) |
| T-23 | FWD-2, FWD-3, FWD-4 | `comp-cache` → `.tools/comp-cache` | measured | 35 runs; React Query cache keys across `portal/src`; `map`/`collisions`/`key` | CloudComp | audit | — | 4.1-4.6 | **not comp-platinum** — portal-local grain; record the distinction |
| T-24 | FWD-2, FWD-3, FWD-4 | `comp-platinum` → `org/modules/graph/platinum_cli.py` | measured | 7 runs; composite of transform+routes+pipescript; portal-page → gold-script | CloudComp | audit | T-10 | 4.2 | his question *"how is comp-platinum defined? what coverage universe?"* — the deliverable's corpus_or_backend + denominator fields answer it |
| G-1 | FWD-7 | `comp-graph status` freshness surface | measured | reports `kuzu_db 81d` + `stitch_graph 38d`; canonical is `kuzu_nessie_db` built 2026-09-01T16:18Z (globgrph F6, attributed to CRO) | NFRA_GRAPHS lane | fix | — | brief O7 | surfaced by CRO, not chased; **re-homes to the comp-graph owner** — this row records the dependency |
| G-2 | FWD-7 | stale-served path `kuzu_nessie_db.fallback.jsonl` | **SPLIT (v0.7): engine half CARRIED, disclosure half OWNED** | 16 `inc-served-labeled-stale` events, ~34h behind (F5); **S31 @ce5c7babea: the local path is UNBOUNDED today -- a `--budget 60` comp-blast call ran the full rebuild ~17 min and was killed outside with no line printed** | engine half: **`NFRA_CLDGRPH` CG-s-8** (the retirement of the local copy, the `_canonical.py` rebuild/labeled-stale seam and its fallback sink) + CG-x-7. Disclosure half: **this project, CloudComp, a DISCLOSE-ONLY order** | disclose-only here; the seam is never written here | T-22 | brief O3b | the port retires the seam, so no engine change is made in this project (S15 precedent); but the path SERVES for the weeks until the port, so the served graph's VINTAGE and AGE go on every answer's disclosure line across the tools that load the universe (comp-blast, comp-trace; comp-find `--corpus aws` already does) -- no engine change, no second writer. FWD-7's local-path limb then reads on this project's own exercised artifact, its engine limb on the sibling's cells. S31's DISARM (a budgeted comp-blast call serves the existing graph labeled stale and never rebuilds inside the budget) rides CE-t-6 as the T-6 lane's own act |
| G-3 | FWD-7 | `kuzu_nessie_load` key asymmetry (node stripped `:150`, edge raw `:184`) | **CARRIED (v0.7)** | carded QUALIFIED @`5da9e7fffc` by `0.7.0_AE_CloudOps~K` (F4) | **`NFRA_CLDGRPH` cell CG-s-9** ("aligned at the port -- the port is the moment"; a control at the two sites that FAILS on the pre-port bytes and PASSES on the ported ones) | carried, never a second writer | T-22 | brief F4 | same reading as G-2; the port carries or fixes it with a control, never silently, which is exactly this row's closes-on |
| G-4 | FWD-9 | **Codex-runtime rail: design** | absent | Andrew-direct 2026-09-02 ~23:0xZ (CTO terminal, "Both recs accepted"), ruling 2(a): this project carries the row; ruling 2(b) EFFECTIVE NOW: a Codex-runtime seat issues NO comp-tool-grounded adjudication until a rail exists on that runtime. The T1 rail is a Claude PreToolUse hook (`.tools/hooks/comp-tool-hud.sh`); the Codex runtime contract (`org/mcp/CODEX_INBOX_MONITOR.md`, MSTR) has no hook at all — `FINDING_COMPRAIL_DENY_NOT_ENFORCED_20260902.md` addendum 2 | CVO drives; CloudComp executes | design | T-1, T-2 | Rule 21 | **what the rail IS is this row's work.** Acceptance: a rail EXERCISED at a Codex seat — a DENY observed as the BODY NOT EXECUTING (a rail-log row is not a block; the 5s-timeout lesson). Rule 21's enforcement bound stays HELD until then. Not a mechanical gate on any seat's word; a design deliverable |

**MECE check against the DECLARED domain (his text block), run not asserted:** 22 named tools + 3 roll-up questions
(dups/drift/legacy) = **25 names → 24 rows T-1..T-24** (kuzu/-inc/-full collapse to one engine row by postulate ii;
hud and legacy are DOES-NOT-EXIST rows). **0 uncovered names.** G-1..G-3 are the globgrph workstream, RELIES-ON
by grain (verify/fix rows, not tool audits). Reverse direction: every T row maps to a name in his block; no T row is
work on a surface he did not name.

**What this manifest does NOT assert:** any `evidence` cell marked "runs" is a TOOL-INVOCATION count and is sound
under R-7; none is a seat-coverage claim. Cells attributed to CRO (G-1..G-3) are carried, not re-measured.

---

## 8. Sequencing input for `2.0.0_SA_COO` (not a dispatch)

CVO~A's suggested order, attributed and adopted as the default: **(1)** T-16 collector repair · **(2)** the s.4
schema census + first three deliverables on T-1/T-2/T-3 (highest traffic, rail-critical) · **(3)** T-8 deny mode ·
**(4)** T-6 subject-existence · **(5)** T-9 trigger scope · **(6)** T-7 unresolved diagnostics · **(7)** shim
self-identification across all rows. T-19 (retire trace) and T-13 (CTO dispose dups) can run any time. T-22 waits on
R-3. G-1..G-3 run as a parallel stream once T-22 is unheld.

— 3.0.0_SA_CVO

## 9. ADDENDUM v0.9 (2026-09-09 ~22:0xZ, `1.0.0_SA_CTO`) -- the three open grades made manual acts with owners

**THE MANUAL-TRIGGER RULE** (Andrew-direct 2026-09-09 ~21:4xZ at the `1.0.0_SA_CTO` terminal, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260909_214xZ_NO_WAITING_EVERY_DATE_GATED_ACCEPT_GETS_A_MANUAL_TRIGGER_FORM.md`: *"we need to not be 'waiting' on anything, anything that we'd be waiting for needs a manual trigger of some kind depending on the test type ... include addendums for each that mandate the requirement is contingent on a relevantly structured manual/test run"*). A manual run is the EXERCISED form of an outcome only when all five hold: (1) SAME TARGET, not a copy -- the rule's own target invoked with the scheduled payload shape; (2) REAL PLANE -- real keys, catalogs, inboxes, devices; a by-hand write to a SERVED key is a served-output move (NEVER-2 entry + never-widen sign-off CTO+COO, rollback named); (3) TOLD APART ON THE ARTIFACT -- a run-id / trigger field, never the clock; (4) the schedule's OWN firing proven from HISTORY (prior rule-initiated executions listed with a denominator), never by waiting -- a rule that has never fired gets a one-off near-term `at()` on the same rule, then restored; (5) the next scheduled fire is CONFIRMATION, never a gate -- no grade carries "pending the fire" again.

Nothing in this project is date-gated; the three NOT_EVALUATED grades wait on two of Andrew's acts and one seat's. Under the rule they are manual triggers with owners, never "after the roadmap". The CTO grades on their records.

| id | outcome_ref | surface (engine) | claim | evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| M-1 | FWD-4 | THE SITTING AS A MANUAL ACT: Andrew's read of the packet (s.7 + the roll-up v2) at any terminal at any time he names -- no roadmap dependency; `3.0.0_SA_CVO`'s `/estate-pull` runs on his "go" | held | FWD-4 NOT_EVALUATED: the packet ready, his read missing (COMPLETION_GRADES.round6) | 3.0.0_SA_CVO (the pull) | verify | -- | the sitting's record names the last tool's state as read by him; the grade flips on that record | 4 |
| M-2 | FWD-9 | THE CODEX-RAIL EXERCISE (CE-g-4) ON ANY CODEX SEAT: `1.0.0_SA_CTO~X` is a Codex seat, READY today; the exercise runs on it the day his word allocates it -- the manual trigger for what was a roadmap allocation | held | FWD-9 NOT_EVALUATED on two limbs; the shared-branch limb is MET by the 09-09 push (origin/CLOUD b2393aec71 contains the remediation commits) and re-grades at the next read | 1.0.0_SA_CTO~X (the exercise) + 0.8.0_AE_CloudComp (the rail) | verify | G-4 | the rail exercised end to end from the Codex seat with the record G-4's design names; the shared-branch limb read from origin (`merge-base --is-ancestor` of each remediation commit, positive control) | 9 |
| M-3 | FWD-8 | THE SHORT LIST USED: the CVO's second-cut list written NOW against s.7's dispositions (not after the sitting -- the sitting reads it), and one seat starting one piece of work from the ratified fourteen the same day, `2.0.0_SA_COO` naming the seat | held | FWD-8 NOT_EVALUATED: the draft @ac52464f82; no seat has started from it | 3.0.0_SA_CVO (the list) + 2.0.0_SA_COO (the seat) | verify | -- | the v2 list committed; one task order's face names a tool from the fourteen as its instrument and its instance validates; the grade reads that record | 8 |
