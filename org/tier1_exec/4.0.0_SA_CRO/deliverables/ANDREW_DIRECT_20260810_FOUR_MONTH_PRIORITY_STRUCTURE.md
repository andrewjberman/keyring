# ANDREW-DIRECT 2026-08-10 ~10:30 ET -- THE FOUR-MONTH PRIORITY STRUCTURE

**Recorded by:** `4.0.0_SA_CRO` (Chief Research Officer)
**Channel:** image posted at the CRO terminal, 2026-08-10 ~10:30 ET (~14:30Z)
**Status:** SOVEREIGN DIRECTION. Recorded VERBATIM. Broadcast to COO + CTO + MSTR same turn.
**Scope adjudication:** NOT performed by me. Surfaced, not interpreted. See section 3.

---

## 1. VERBATIM

Transcribed exactly as written, including the original's own numbering inconsistency
(`3.` where `1.)` and `2.)` carry a parenthesis). **Not tidied** -- a verbatim record that has been
cleaned up is not a verbatim record.

> I was thinking about it over the weekend and I think the priority list as a function of
> sequencing/dependency looks something like this, going chronologically:
>
> **1.) Sort out "Custom" model pull from Cottonwood Black Diamond (Scanning any "Opal" constituent)**
> Have already scouted/spec'd this, it's doable.
>
> **2.) Begin ADVI Analytics EC2 Refactor.**
> Have spec'd this but it's large because there is the 49 aspect, the other firm aspects, and the
> foundational architectural aspect.
>
> **a.) 49F + Architectural**
> Because 49 are the only ones we have Custodian access for, that means they must become the
> archetype. We need to build everything direct from the raw data and be extremely rigid about
> logging and defining every single field/staging table/output shape/methodology/etc. This way we
> have a true template for every script/dependency which we must reuse for the foreseeable/known
> future.
>
> **b.) Inflection / Cottonwood**
> Once we have this foundational structure off clean/raw data, then we need to go through every
> single endpoint (documented) for both of these firms across Orion/Eclipse/BD and restructure them
> to rely on those defined data fields. We are never doing one-offs ever again on scripting, patches
> only if absolutely necessary.
>
> **3. Thread/Overlay Model Holdings data firm-by-firm on top of ADVI**
> Once ADVI is completely in the clear, need to assess how to take model holdings data on the
> client-level and match those accounts to the account-level counterpart in ADVI. Model Portfolios
> work the last several weeks has resulted in consolidated staging at the firm level, I think that
> same logic would need to be applied at account-level, and that would open up the ability to join
> and then have account->relationship/household->advisor->firm aggregates in the existing ADVI
> spline.

Followed, same message thread:

> This is what I'd like to be able to accomplish over the next 3-4 months ^

> 1.) is not that hard that's this week priority.
> 2.) I have been scoping from all angles and just need to dive into but it will be the heaviest
> part, maybe 6-8 weeks, at best maybe 4-6.
> 3.) Conceptually this should be solid, maybe 4 weeks at most.

And, in the accompanying message at the CRO terminal:

> This structure is the highest priority of our work at Opal over the next 4 months ahead of 2027.
> We have taken stabs at this (repo root/projects/ ADVI refactor project spec) and trying to make the
> atom_decomp structure so that when we really get into the thick of this stuff we can properly break
> it down so we dont end up mired in data engineering hell. But this is it. All the NFRA work we've
> been doing, all the ontology and the comp-tools, the whole purpose of all of this has been to do
> what is described in the above image, to build and scale this system to the partners. Let's
> discuss.

---

## 2. WHAT THIS ESTABLISHES

- **A ratified four-month program ordering**, chronological and dependency-shaped, with his own
  duration estimates: item 1 = this week; item 2 = 6-8 weeks (best case 4-6); item 3 = <=4 weeks.
- **The purpose statement for the whole NFRA / ontology / comp-tools body of work**, stated by him
  directly: it exists to enable this program. That is a retrospective framing of work already done,
  and it binds how that work is prioritized from here.
- **A standing rule inside item 2b**, verbatim and unambiguous: *"We are never doing one-offs ever
  again on scripting, patches only if absolutely necessary."*
- **A named archetype decision** in 2a: 49F becomes THE template because it is the only firm with
  Custodian access; everything else conforms to it.

---

## 3. SCOPE -- SURFACED, NOT ADJUDICATED

Per `org/XXX.md` ("SURFACE, DO NOT ADJUDICATE") and the CLAUDE.md no-inferred-gates rules, I am
recording the following as an OPEN QUESTION AT ANDREW and taking no action on it, in either
direction:

**`ADVI_PERFORMANCE`'s own ratified PRD carries a start condition that this message does not
mention.** `projects/ADVI_REFACTOR/ADVI_PERFORMANCE_PRD.md` ADDENDUM A.2 ("Sequencing -- NFRA_VELOCITY
COMPLETES FIRST, END TO END", Andrew-direct 2026-07-29) makes NFRA_VELOCITY's end-to-end completion a
precondition for ADVI_PERFORMANCE beginning. Both `NFRA_VELOCITY_CORE` and `NFRA_VELOCITY_ESTATE` are
currently `[SUSPENDED-TEMPORARY 2026-08-03, Andrew-direct at the CRO terminal: RCG first; resumes on
his word]` (`org/projects/REGISTRY.md:125-126`).

Today's message orders ADVI as item 2 with no reference to that gate. **Whether today's ordering
supersedes A.2, or whether A.2 still binds, is his call and only his.** It is recorded here so the
question is visible rather than resolved by whoever reaches it first.

**No hold has been placed on anything as a result of this note.**

---

## 4. GROUNDING FOR THE ABOVE

| Claim | Evidence |
|---|---|
| ADVI_PERFORMANCE is registered + active | `org/projects/ADVI_PERFORMANCE.json` -> `status: active` |
| Its spec body exists and is substantial | `projects/ADVI_REFACTOR/` -- 52 files, 51 git-tracked; PRD 706L, E2E standardization plan 1146L |
| The A.2 start condition | `projects/ADVI_REFACTOR/ADVI_PERFORMANCE_PRD.md` ADDENDUM A.2 |
| VELOCITY suspended | `org/projects/REGISTRY.md:125-126` |
| ATOM_DECOMP exists, case study is ADVI | `projects/ATOM_DECOMP/01_ADVI_CASE_STUDY.md` |
| ATOM_DECOMP has never been executed | CRO audit 2026-08-07, `org/tier1_exec/4.0.0_SA_CRO/logs/2026-08-07/atom_decomp_STATE_AND_NEXT_STEPS_1825-2130Z.md` s.4 |
