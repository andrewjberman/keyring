# ENDPOINT -- NFRA_COMPEFFICACY (step 2, `/endpoint --forward`) -- the first test run of the canonical workflow

**Run by:** `1.0.0_SA_CTO`, 2026-09-02 ~23:3xZ, on Andrew's GO (*"run /endpoint --forward on the relevant path ... lets
take compefficacy through the whole canonical process ... Starting with L2"*, record
`ANDREW_DIRECT_20260902_231xZ_GO_COMPEFFICACY_FIRST_TEST_RUN_FROM_L2.md`).
**Phase 0 (greenfield path).** Not a re-entry.

## F1 -- the brief

```
  path      org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260902_1715Z_COMPTOOL_EFFICACY_PROJECT.md
  vintage   @f90ab3936b (2026-09-02 13:19Z, 3.0.0_SA_CVO; worktree IDENTICAL to the blob; ON origin per CVO 23:01Z)
  size      6,128 bytes / 83 lines, read in full
  form      an Andrew-direct RECORD, not a CRO brief -- the admitted second form of `brief_ref`
            (org/tier[0-9]_*/<seat>/deliverables/ANDREW_DIRECT_*.md@<sha>); no `generated` line by construction
  named as the FOUNDATION by 3.0.0_SA_CVO 23:01Z (re 92807): the PRD draft is the existing step-3 object, not the foundation
```

## F2/F3 -- capability outcomes (qualitative; ACCEPT in plain English, no system vocabulary)

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
```

`FWD-n` ids are PERMANENT for the life of the project (contract with `3.0.0_SA_CVO`, `outcome_ref`).
A retired outcome leaves its number vacant; a new one takes the next unused number.

## F4 -- where this lands

**NOT YET LANDED.** The PRD does not exist at its home. Under the project tree (ruled 2026-09-02, contract
`org/standards/PROJECT_TREE.contract.json` v0.1.0, `prd_path: prd/{project_code}_PRD.md`) the home is:

```
  org/missions/D11/NFRA/NFRA_COMPEFFICACY/prd/NFRA_COMPEFFICACY_PRD.md
  section title, exact:   ## ENDPOINT (step 2, /endpoint --forward)
```

`D11` is the directive Andrew placed it under (*"NFRA_COMPEFFICACY = laptop under D11"*, @`a8d63f097c`) and its
macro enum is RATIFIED (MSTR terminal ~22:3xZ). `3.0.0_SA_CVO`'s `NFRA_COMPEFFICACY_PRD_DRAFT_v0.1.md`
(@`86a5538003`, DRAFT) is the existing step-3 object; at L4 this block is inserted into the PRD that lands at
the home above -- this seat's edit, that turn, never any other section of CVO's draft.

## F5 -- provenance

```
  GROUNDED ON  the brief above, @f90ab3936b, all 83 lines; every outcome cites its lines.
               Andrew's GO record ANDREW_DIRECT_20260902_231xZ_GO_COMPEFFICACY_FIRST_TEST_RUN_FROM_L2.md
               (for the run itself, not for any outcome).
  NOT READ     the TO register (none exists for this project, and Phase 0 refuses it by design);
               org/projects/ (no row exists -- registration is L3, from scratch under the tree);
               3.0.0_SA_CVO's PRD draft (deliberately: a step-3 object read at step 2 would blend
               its outcomes into the endpoint, and step 10 could not tell whose they were);
               the passcraft recon and the globgrph brief themselves (named by the brief as INPUT
               and IN SCOPE; their contents are L4's and L5's reading, not the endpoint's).
```

## What this run measured about the workflow itself (the point of the test)

- **The `brief_ref` second form did its job:** an Andrew-direct record served as the step-1 brief with no CRO
  brief in `docs/briefs/`; F1 did not refuse and did not synthesise. The `generated` line is absent by
  construction on that form -- the skill's F1 says "if it carries one"; recorded, not a defect.
- **F4's "PRD does not exist" arm is the one that fired**, as the skill calls the normal case -- with the twist
  that a DRAFT exists elsewhere. The skill's rule ("never edit any other section of someone's PRD") held; the
  draft was not opened.
- **The endpoint has eight outcomes and one of them (FWD-5's kuzu question) is already RULED and partly landed
  outside this loop** (comp-kuzu consolidation, CloudComp 20:13Z). Step 10 will meet it as an outcome whose
  ACCEPT is already testable; that is the correct place to discover it, not here.
