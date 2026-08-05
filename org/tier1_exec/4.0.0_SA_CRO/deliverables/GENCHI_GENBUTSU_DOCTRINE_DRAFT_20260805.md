# GENCHI GENBUTSU — go and see for yourself

**One root idea, four ways it fails, and the calls that discharge it.**

*Genchi genbutsu* (現地現物) — "the actual place, the actual thing." Go and look at the real thing
rather than reasoning about it from where you are standing. **Andrew-direct 2026-08-05:** *"The
biggest idea here seems to be aligned with a japanese proverb ... which translates to 'go and see
for yourself'. The purpose of the comp-tools was this idea."*

**This file replaces 1,289 lines.** What was cut was not wrong. It was four ideas restated in
escalating rhetoric, plus a body of instrument-specific facts that belong in a lookup rather than a
sermon. Those facts are preserved (see "The reference half" below); the prose is in git history at
`913e3365d6` and its predecessors. **Nothing was deleted that anyone will need. It was de-duplicated
and re-homed.**

---

## Why the old form could not work

The estate's own record says so twice, and only one half made it into the title.

- **The capstone claim:** eleven instruments lied in one night; every one was caught by a control
  failing, none by anyone being careful.
- **Sixty-five lines later, unpromoted:** *"the thing that actually worked has no gate behind it —
  every catch on 2026-07-16 ran through the same uninstrumented path: somebody read the thing and
  checked. Not one was caught by a gate."*

Both are true. They generalise in opposite directions, and the file's own warning is that *"the
estate will fund the mechanism the story names."* It named controls in its title while its body
named reading. This file names reading, and then supplies the mechanism that makes reading cheap.

**The deeper reason prose fails here: this failure mode has no phenomenology.** It never feels like
skipping a check. It feels like knowing. Inference is generative — it arrives first, cheaply, with
confidence already attached. Retrieval requires stopping to go fetch. By the time "should I check?"
surfaces, an answer is already in hand and the check reads as redundant.

**Care operates on the answer you already generated. It does not send you to get a different one.**
That is why care is not a control, and also why 1,289 lines of doctrine about care changed nothing:
scrutiny and retrieval are different actions, and only one of them was ever going to help.

---

## THE ROOT — go and see the thing itself

Across every incident this estate has recorded, the failure is almost never *"did not verify."*
Everyone verified something. The failure is:

> **Cheap, direct, decisive evidence was available, and an inference was substituted for it.**

| incident | what was available | what was substituted |
|---|---|---|
| INF gold chain — 6 mechanisms, 7 agents, 11 hours, all falsified | the chain log, printing its own cause of death | six ratified mechanisms |
| a self-correction that impeached a real number | the override log it accused | a census that never walked it |
| "the only columns that differ are date stamps" | his own output, showing `asset_class` differed on 2 rows | a clean sentence |
| three distinct digests read as "the source differs" | which columns differ | the hash, dominated by the fields under investigation |
| `EC2_MANIFEST` read as dead (2026-08-05) | lines `:438` and `:442-446`, two lines above | adjacency of two strings |
| a label flipped on sibling coherence (2026-08-05) | the path's own prior adjudication | an inference from its neighbours |

Every row cost less than a minute to check. **Go and see.**

---

## The four ways you fail to see it *even though you looked*

These are not four topics. They are four ways the root fails, and they are the whole taxonomy.

### 1. You looked at a PROXY, not the thing
A digest, a count, a config, an `rc=0`, a symbol's presence. Proxies answer a neighbouring question
and report full confidence.
- `rc=0` is a launch receipt, not an outcome. A 2-second success token for a full gold chain is a
  receipt.
- A hash is a proxy; the columns are the thing. When you hash to prove sameness, first remove the
  fields whose sameness is the question.
- Applied-config is not behaviour. A guard nothing calls is a comment with parentheses.
- **Discharge:** exercise the path that fails if the claim is false. Read the served value.

### 2. You looked at the DESCRIPTION, not the STATE
Comments, docstrings, registries, PRDs, status fields, Terraform-as-written. **The describing layer
drifts from the enforcing layer, and only the enforcing layer is true.**
- A comment is a claim with no vintage and no test. The most dangerous one is not false — it is one
  that was true and the ground moved under it. It argues authoritatively, in the codebase's own
  voice, for the exact harm it now causes.
- A marker FILE saying ARMED beats a hook COMMENT saying staged. State wins over prose describing
  state, always.
- `comp-iam` parses DESIRED Terraform; it cannot tell landed from planned.
- **Discharge:** read the enforcing layer — the live primitive, the marker file, the applied config,
  the deployed bytes.

**2b. And the dominant case in this estate: almost everything you read was written by another
agent.** Ledgers, dispositions, registries, session logs, handoffs, PRDs, task orders, prior
findings — these are the substrate you reason from all day, and they are all *descriptions*.

**Andrew-direct 2026-08-05, verbatim, and this is the calibrated form:**

> *"Treat recent agentic artifacts as the last agent's understanding of state, not a settled
> baseline. It is not necessarily an error, but it is neither an absolute truth, it is a
> representation, a map, not the territory, and should be handled with a 'go and fetch for
> yourself'."*

**The framing is load-bearing and the non-guilt half is the part to keep.** The failure is *not*
that prior agents are unreliable — reaching for suspicion is its own miscalibration, and it makes
agents re-litigate settled work and distrust good records. **A map is not wrong for being a map.**
It is a compression of someone's understanding at a vintage, and the correct response to a map is
not doubt, it is **fetching the territory when the claim is load-bearing.**

Two symmetric errors this rules out:
- **Inheriting an artifact as truth** — the whole of principle 2. *(2026-08-05: a disposition said
  RESOLVED and its ledger row was never written; the accounting and the state disagreed for a day.)*
- **Discounting an artifact as suspect** — treating a peer's recent output as an error source rather
  than a map. This wastes the work and poisons the record with manufactured doubt.

**Discharge:** when an agentic artifact carries a load-bearing claim, go and fetch the thing it
describes. When it does not, use it as the map it is and move on. **The question is never "do I
trust this agent" — it is "is this claim carrying weight, and have I seen the territory."**

### 3. You compared the thing TO ITSELF
No outside information entered, so the check certifies any internally consistent lie.
- Conservation is invariant under a swap, and under a simultaneous both-sides deletion. *"The firm
  total ties to the cent"* was blind to both of the day's real defects, by construction.
- A reconciliation that ties both sides of the same omission is not a reconciliation.
- An aggregate is never graded on its total, and never on the series you were asked about. Two
  offsetting moves produce a clean headline.
- **Discharge:** diff against a **prior vintage**, or a **source the pipeline does not derive from**.
  Diff every constituent series, not the roll-up.

### 4. Your instrument COULD NOT HAVE SAID OTHERWISE
The measurement had no failure mode, so its PASS carried no information.
- An append-only check walked an empty set and reported PASS through a real violation.
- A count cannot distinguish "nothing is there" from "I looked in the wrong place." Zero is
  byte-identical between empty and misaimed. `grep -c` returns 0 from an error message.
- `--query 'length(...)'` on a paginated `list-*` returns the PAGE count. Measured: 100 when the
  truth was 142.
- A positive control batched with its target is corrupted by its own presence.
- **A check run on one member of a set does not cover the set.** (2026-08-05: the disposition-trail
  read that produced a finding was inherited across a batch whose second member had never been
  pointed at. The instrument was correct and was never aimed.)
- **Discharge:** print the denominator of every scan you reason from. Run the positive control in
  isolation. Keep a proven-red case. Ask: *could this have failed? did my input reach the governed
  branch? was this actually pointed at the thing I am concluding about?*

---

## The mechanism — comp-tools are foundational, not additive

**Andrew-direct 2026-08-05, verbatim:**

> *"Agents need to have readily available mechanisms to fetch the 'right' information, versus
> stochastically bouncing around context and grepping, where they might not even be in the right
> region off a semantic grep, and ironically enough the grep results may have a -head truncation and
> even if they're right they miss the nugget of info they needed. This is why the comp-tooling is not
> additive, it is foundational."*

A doctrine that says *"go and see"* and stops is an exhortation. The reason agents infer instead of
retrieve is that **retrieval has been expensive and unreliable** — a raw grep lands in the wrong
region, is text-local and connection-blind, truncates at `head`, and can return the right file while
missing the line that mattered. Under those conditions inference is the *rational* choice.

**Therefore: every principle above terminates in a call, and the tool is the doctrine.** Lower the
cost of going and seeing until inference stops winning.

**Default reflex:** `comp-which "<plain-English question>"` — it routes to the right tool, or runs
the on-rails `comp-grep`/`comp-glob` itself. You do not need to know the catalogue.

| you want to know | call | what it CANNOT tell you |
|---|---|---|
| which tool answers this at all | `comp-which "<question>"` | — (it never dead-ends; it runs the primitive) |
| where something lives / what cites it | `comp-grep <pat>` / `comp-glob` | liveness — a hit is a mention until you read it |
| what a named thread is made of | `comp-estate <name>` | NAMES come from a snapshot; read the provenance header, `--refresh` before trusting one |
| column gaps + portal consumers of a gold script | `comp-pipescript io <s> --pipeline <tree>` | flagless is `rc=2` REFUSED — never guesses a tree |
| is the deployed code the repo code | `comp-pipescript deployed` | whether it RAN |
| is a served artifact current | `comp-freshness` | correctness of contents; and it false-alarms without `freshness_basis: trading-day-frontier` |
| what breaks if I change this | `comp-blast <fn>` | runtime coupling not expressed in the graph |
| does this role hold this permission | `comp-iam service <lambda>` | **`(action, resource)` — it models action only, and it fails GREEN.** New bucket/table/ARN → `aws iam simulate-principal-policy`, ONE `--resource-arns` per call, positive control run separately |
| cross-layer relationships | `comp-kuzu "MATCH ..."` | vintage, unless you read the provenance header |
| did I break a critical surface | `comp-surface-check` | portal-side it BLOCKS (`rc=2`); workspace-side advisory. Silence is not a pass |
| is my gold output valid | `comp-validate <s> --artifact <f>` | `NO_CONFIG`/`ZERO_CHECKS` means UNVALIDATED, never SAFE |
| do the records match the estate | `comp-state` | it is BM25 recall — BEHIND is a place to look, CURRENT is not a verified record |

**A tool's blind spot belongs in the same row as the tool.** That column is the doctrine's fourth
principle made operational: an instrument that does not declare what it cannot see will be read as
having seen everything.

**Corollary — a gap in the tooling is a defect, not an inconvenience.** If you had to reach for a raw
grep because no comp-tool fits, that is a coverage gap: record it (the rail log audits overrides) and
route it. A repeated override for one intent means the tool should exist.

---

## What to measure

The estate has been optimising **error rate**. Error rate in this class is irreducible — the failure
has no phenomenology, so no amount of knowing prevents it. Two of the incidents in the table above
were committed by agents who could cite, by name, the exact rule they were breaking, *in the act of
breaking it.*

**Measure instead:**
1. **Time-to-catch.** Both 2026-08-05 errors died inside 30 minutes, structurally, with zero damage.
   That is the system working.
2. **Blast radius at catch time.** Append-only ledgers, revertible batches, gates before execution:
   these make an error survivable rather than terminal.
3. **Who caught it.** Write down what *actually* caught it — a gate that did not run gets no credit,
   an instrument that was not consulted gets no blame. The estate funds the mechanism the story
   names.

**What has actually caught things here:** lane gates (automatic, no recall required), population-wide
sweeps (they run over every member without being asked about one), peer reads, and time. **Not one
was "the agent remembered the rule."** Build accordingly.

---

## The reference half

The instrument-specific facts formerly interleaved here — `simulate-principal-policy` flipping held
ARNs to `implicitDeny` with 2+ `--resource-arns`; MSYS argv de-escaping; the paginated `length()`
undercount; the aws-shim `--delimiter /` mangle — are **not** doctrine. They cannot be derived, they
must be told, and they are needed at a specific keystroke rather than read in advance.

They belong in a **queryable lookup, reachable from `comp-which`**, not in prose. Until that lands
they are preserved in git history and in `docs/references/`. **Building that lookup is the open item
this rewrite creates** — and it is the same principle applied to itself: a reference nobody can query
is a reference nobody reads.

---

*Author: `4.0.0_SA_CRO`, 2026-08-05, on Andrew-direct instruction. Predecessor:
`CONTROLS_OVER_CARE.md` @913e3365d6 (1,289 lines, 320 → 1,289 in 18 days), authored primarily by
`1.0.0_SA_CTO`/`~Z` with contributions from MSTR, COO, CVO~Z, AE~C. **The cut is of duplication and
rhetoric, not of their findings** — every mechanical fact above is theirs, and the two 2026-08-05
rows in the root table are my own error and CTO~B's.*
