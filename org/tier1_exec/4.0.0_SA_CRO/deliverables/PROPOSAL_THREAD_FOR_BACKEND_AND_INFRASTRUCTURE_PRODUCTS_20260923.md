# PROPOSAL -- the live thread for a purely backend or infrastructure product

**Author:** `4.0.0_SA_CRO`. **UTC:** 2026-09-23 ~17:0xZ. **Status:** PROPOSED. It is put to Andrew as one card; the
spine wording is `1.0.0_SA_CTO~C`'s to land on his yes.

**Owed by:** Andrew-direct 2026-09-23 ~16:3xZ, call 5, VERBATIM: *"That does apply for projects that have a frontend
but needs to be considered in the event it's purely a backend/infrastructure product (e.g. NFRA_GLOBGRPH,
NFRA_COMPEFFICACY, LGIC_NAMING, LGIC_LGCTFM, etc.)."* Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_163xZ_HOLD_OFF_AND_CLOSER_OPEN_CALLS_RULINGS.md`
@`7303be1bbb`.

**The text in question.** Spine L2 at v3.16 (`org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md:93-97`):
- "For a pipeline with no product surface the thread is source to served artifact."
- "NON-APPLICATION: a pure infrastructure or governance project, which has no journey."

Read literally, the second sentence exempts all four of Andrew's examples. His word says they need a thread
definition, not an exemption.

## 1. The definition

**For a backend or infrastructure product, the thread is one real CONSUMER's one real use of the product, end to end
on the real mechanism, ending in the consumer's observed result.** The consumer is whoever acts on the output:
- a seat at a terminal;
- a downstream pipeline or job;
- a person reading an artifact.

FWD-1 names the consumer.

**LIVE**, the backend counterpart of call 5(a), means all four of:
1. **The real mechanism:**
   - a tool is committed at HEAD of the working branch and invoked from an ordinary seat shell, not the author's worktree
     or a test harness;
   - a cloud component is the deployed artifact (Lambda, Step Function, ECS task, schedule);
   - a library is imported by a real caller, never only by its own tests.
2. **Real inputs:** the real corpus, the real AWS account, real S3 data, a real legacy subject. Never a synthetic
   sample.
3. **The real entry**, as the consumer uses it: the CLI, the hook at commit, the manual or scheduled trigger, under the
   consumer's real identity.
4. **The consumer's observed result**, recorded as ONE trace artifact (invocation, each hop's input and output, final
   result). The observed result is the answer printed in the consumer's terminal, the object its reader reads back, or
   the refusal seen at commit.

A fixture-fed hop fails the thread, exactly as on a product with a frontend.

**What may stay local, mirroring "the frontend may be local or DEV".** The two cases differ in which part may stay
local. With a frontend, the consumer's side may be local. With a backend or infrastructure product, the result's
destination may be:
- one machine's working branch, where availability on the shared branch and the other machine is an enrichment item;
- a QA or non-served output location, where the ad-hoc QA run is admitted (CLAUDE.md "Ad-hoc gold runs are PERMITTED
  FOR QA") and promotion to the production schedule or served keys is an enrichment item.

Served-output writes still carry the never-widen sign-off. This definition lifts no gate.

**Still exempt:** a pure GOVERNANCE project, meaning a record, a policy or a register with no mechanism anyone invokes.
The spine's non-application narrows from "infrastructure or governance" to "governance".

## 2. Andrew's four examples, as threads (grounded in each PRD's own FWD text)

| Project | Consumer | Thread: the real mechanism on real inputs, ending in the observed result | Grounding |
|---|---|---|---|
| `LGIC_LGCTFM` | the person opening a legacy subject's migration | names one real legacy subject; the installed engine runs over the live estate; the contract artifact is read by that person | its FWD-1 is already this: *"DONE WHEN EXERCISED -- run on the first real subject and read by the person opening that subject's migration"* (`prd/LGIC_LGCTFM_PRD.md:72`) |
| `LGIC_NAMING` | a seat creating one new resource | `lib/opal_naming.py` `name()`/`address()` at HEAD returns the name and address for one real new resource; the resource is created, or one QA object is written at that address on real S3; a second reader resolves it through the builder and finds it | its FWD-1 (*"two people have actually named the same new thing"*, `prd/LGIC_NAMING_PRD.md:36`) is a judgment grade; the thread is the mechanism under it |
| `NFRA_COMPEFFICACY` | a seat asking one real question | `comp-which` routes a plain-English question; the named tool runs at HEAD from an ordinary seat shell over the real corpus; the answer and its printed denominator land in that seat's terminal | its FWD-9 is the same condition: *"used from a seat other than the one that fixed it, and behaved as cleared"* (`prd/NFRA_COMPEFFICACY_PRD.md:160`) |
| `NFRA_GLOBGRPH` | a seat asking a cross-layer question | the graph is built from live sources (the certified AWS read and the repo) at its stated vintage; one real cross-layer query (portal page -> API route -> Lambda -> bucket -> role) returns the edge path in the seat's terminal | its PRD scope is "all Opal layers unified ... portal UI through IAM to external data source" (`docs/architecture/NFRA_GLOBGRPH_PRD.md:33-51`) |

## 3. Spine wording, for the CTO

At L2, replace the two sentences quoted above with:

> *"For a backend or infrastructure product the thread is one named consumer's one real use of the mechanism -- the
> real tool at HEAD from an ordinary seat shell, or the deployed component, over real inputs, through the entry the
> consumer uses -- ending in the consumer's observed result, recorded as one trace; the result may land on one
> machine's working branch or in a QA location, and shared-branch availability and production scheduling are
> enrichment items. NON-APPLICATION: a pure governance project, which has no mechanism anyone invokes."*

**Transition:** the spine's own rule applies. An open round finishes under its cut task orders. `LGIC_NAMING` is
`CLOSED` and is not reopened. `NFRA_COMPEFFICACY` and `LGIC_LGCTFM` read `EXECUTING`, so this applies from their next
issuance.

**Cost:** one spine sentence and one line in `/endpoint --forward` Step F2.
