# ANDREW-DIRECT INSTRUCTION — recorded verbatim per XXX.md same-turn law

**Channel:** Andrew, direct at the 0.8.0_AE_CloudComp session terminal
**Time:** 2026-07-17 ~17:1xZ (mid-turn message during session startup/wave work)
**Recorded by:** 0.8.0_AE_CloudComp (receiving agent; surfacing, NOT adjudicating scope)
**Broadcast:** MCP to 2.0.0_SA_COO + 1.0.0_SA_CTO + 0.0.0_AB_MSTR, same turn

## VERBATIM

> Something I want to explore doing here is properly expanding the use case of comp-iam. There
> is a lot of IAM information that Id like that function to return which we simply dont grab,
> please investigate that tool and assess this. FOllowing that I want to get a better
> understanding of our trino heat analytics across platfoorms. A major, major focus of the
> consolidation is establishing key patterns and consistency across AWS resources. In order to
> do this, not only do we have to establish consistent taxonomy and patterns, we also need to
> gradually phase out and decommission clearly deprecated resources as the new ones are coming
> online. Because the opal-data-assets bucket is going to be the principal monolith for all
> data storage, and the associated pipeline runners will also be consistent and migrated to use
> these buckets (e.g. the gold ec2s for inf-pipeline cot-pipeline bd-pipeline), we want to be
> able to identify stuff that is no longer in use so we can actually begin the process of
> cleaning up the cloud so agents do not get confused with deprecated or overlapping resources.
> I thought that developing the heat analytics would be instrumental for this kind of thing,
> and also comp-dups and all of that. I want you to be able to do some research for us and look
> into how we can use our tooling to efficiently facilitate this process.

## Receiving agent's read (non-binding, for the broadcast)

Three asks, sequenced by Andrew himself:
1. **comp-iam expansion assessment** — investigate what IAM information the tool does NOT
   currently return, assess expanding its use case.
2. **Trino heat analytics across platforms** — a cross-platform understanding of the heat
   analytics estate (code_heat, ms_heat, tool_activity, the *_snap delta siblings, ...).
3. **Deprecation/decommission facilitation research** — under OPAL_CONSOLIDATION: as the
   opal-data-assets monolith + consistent runners come online, use heat analytics + comp-dups
   + related tooling to IDENTIFY no-longer-in-use / deprecated / overlapping cloud resources so
   cleanup can begin and agents stop being confused by them. Research-first, not a delete wave.

Note for the record: this is research/assessment scope. Any actual decommission/delete action
remains gated by existing law (human confirmation for destructive ops; NEVER-rules; CTO applies).

## ADDENDUM — Andrew-direct, same terminal, ~18:2xZ (comp-similarity, a proposed NEW tool)

VERBATIM:

> Yes there is another part of this, a tool that does not exist yet but should. i'd call it
> comp-similarity. the idea would be that it would be some kind of bm25 lexical similarity score
> between a summary of a resource, same as comp-dups but instead of name-based, it would somehow
> get a stable summary location of the resource. i dont know if aws has a summary field somewhere
> or where we'd get that, so would have to think about hwo that would work. Depending on the
> design of comp-dups, it could likely use a very similar engine, its just the target is slightly
> different.

Receiving agent's read (non-binding): a 4th research component. comp-dups today scores BM25 over
NAMES + a content corpus; comp-similarity scores BM25 over a per-resource SUMMARY string, to catch
resources that DO the same thing under different names (the "overlapping resources" half of the
original ask). OPEN DESIGN QUESTION Andrew named explicitly: the "stable summary location" — where a
resource's purpose-summary comes from (AWS has Description fields on SOME resources — Lambda, IAM
role, EventBridge rule, SG — but not S3/DDB; tags; the TF-declared description; or the comp-graph
node summary the estate already builds). Engine reuse from comp-dups (dup_scan BM25) is the stated
intent; the novel part is the summary-corpus sourcing. Folded into the assessment as a design section.
