# PRD template carrier re-grade -- CVO~A

**Date:** 2026-09-02  
**Order:** CTO message 92702  
**Implementation pinned:** `75ead40079b9d6e594ab4e411518ce73ccb6c474`  
**Verdict:** **PARTIAL.** The carrier now contains the header and manifest skeleton, but the claim that a PRD authored from the full template passes limb 5 by construction is false, and the widened `brief_ref` pattern does not enforce its declared two-shape domain.

The two implementation files were byte-identical between the pinned commit and
the live bytes exercised below, with no worktree divergence.

## Green limbs

- `_PRD_TEMPLATE.md` now has a first fenced `json` block containing the
  `PRD_HEADER` skeleton, the exact unbackticked ENDPOINT title, and a non-empty
  section 7 SURFACE MANIFEST skeleton. The prior carrier had none of them.
- The template does not copy COO's frozen ETFS instance. It carries generic
  schema/rules and one placeholder row.
- The stale prose describing the ENDPOINT refusal as proposed is corrected to
  name the two live step-6 limbs.
- `PRD_HEADER.schema.json` passes the Draft-07 meta-schema.
- The common `brief_ref` controls behave as claimed: a vintage-pinned CRO brief
  and the actual Andrew-direct record pass; no vintage, a short vintage, a
  non-Andrew-direct deliverable, and an unrelated ordinary path refuse.
- When only the skeleton beginning at `# {PROJECT_CODE}` is instantiated with
  legal values, `_prd_conformance()` reports zero complaints.

This closes the original **absence** defect: an author who deliberately extracts
and fills the skeleton has a usable header and manifest carrier.

## Falsifier 1 -- the full template does not pass limb 5

The rules above the skeleton quote the exact ENDPOINT heading inside a code
fence. Both endpoint limbs use a plain first-occurrence search rather than a
Markdown section parser. On an otherwise valid instantiation of the full
template, the gate selects that illustrative occurrence, sees no definitions in
its following text, and returns:

```text
PRD_HEADER.endpoint_outcomes lists FWD-1, FWD-2 but the ENDPOINT section
defines no such outcome
```

The illustrative occurrence is before the `PRD_HEADER`; the real skeleton
heading is later. Skeleton-only passes, full-template fails. Therefore "passes
by construction" requires either an explicit machine-extractable skeleton
boundary/generator or a gate parser that finds a real top-level heading outside
code fences. The latter is the same parser repair already owed for the
code-fenced SURFACE MANIFEST bypass in the limb-5 re-grade at `d019922d68`.

## Falsifier 2 -- the carrier changes the adopted manifest field

The adopted COO contract names the load-bearing field `outcome_ref` and permits
`FWD-n` or `NONE -- <reason>`. The new template table instead carries a column
named `outcome` and a placeholder `FWD-n or --`.

```text
template occurrences of outcome_ref = 0
template table field                 = outcome
```

That is not the adopted row schema. Restore the adopted field name and its
truthful no-outcome form, or obtain and record an explicit schema amendment;
the carrier must not silently fork the contract it is meant to carry.

## Falsifier 3 -- `brief_ref` admits paths outside the declared domain

The new pattern uses `[^@]+`, which includes path separators and traversal. The
following all validate although none is one of the declared canonical shapes:

```text
docs/briefs/../architecture/_PRD_TEMPLATE.md@abcdef0
docs/briefs/not-a-brief.txt@abcdef0
org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_x/../../OTHER.md@abcdef0
```

At minimum, each branch must reject `..`, constrain path segments rather than
matching across `/`, and make the accepted CRO extension explicit. Because the
field claims to identify a vintage-pinned artifact, proving that the referenced
path exists at the cited commit would require a consuming check; a regex can
validate a citation's shape but cannot prove its referent. Such a check is a
separate refusal condition and must not be added without Andrew's authorization.

## Carried open conditions

- The `PRD_HEADER.status` enum remains unadopted under the Rule-24 ruling in
  `CANONICAL_LOOP_RC2_RC4_LIMB5_REGRADE_20260902_CVO_A.md`; this commit carries
  the existing enum but does not cure its no-successor lifecycle hole.
- NFRA_CLDGRPH decomposition remains unblocked. Its owner still owes the header
  and manifest in a version-bumped PRD before the first TO.
- No new refusal condition is authorized or proposed by this carrier review.

-- 3.0.0_SA_CVO~A
