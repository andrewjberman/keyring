# PRD template carrier re-grade -- CVO~A

**Date:** 2026-09-02  
**Order:** CTO message 92702  
**Pass-1 implementation pinned:** `75ead40079b9d6e594ab4e411518ce73ccb6c474`
**Pass-2 implementation pinned:** `f5f7481015`
**Pass-4 implementation pinned:** `ef6a37e098`
**Current verdict:** **PARTIAL.** Pass 4 closes all six pass-2 falsifiers, but its fence grammar covers only exact column-zero three-character markers and its `brief_ref` exclusions can be bypassed across a newline.

The original pass-1 verdict and falsifiers are retained below as the historical
red-first record. The pass-2 disposition is appended after them.

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

## Pass-2 re-grade -- `f5f7481015`

The four graded implementation/control files at the pinned commit are
byte-identical to the live bytes exercised. The commit is an ancestor of
`HEAD`; there is no worktree divergence in those paths.

### Closed by pass 2

- The committed battery is green: **14/14 core, 10/10 `brief_ref`, and 2/2
  wrapper controls**, with zero reported defects.
- A filled copy of the **full** `_PRD_TEMPLATE.md`, including its illustrative
  fenced ENDPOINT title before the real title, now passes `_prd_conformance()`.
- The template carries the adopted `outcome_ref` field and the truthful
  `FWD-n | NONE -- <reason>` form. It no longer forks the manifest contract to
  `outcome`.
- An empty manifest and a manifest title inside an ordinary triple-backtick
  fence refuse.
- The wrapper reads the staged project-register blob: a staged `directive=D9`
  against a worktree/header `D8` refuses.
- Ruff, Python compilation, and the Draft-07 schema meta-check are green.

### Open falsifier 1 -- `_top_section()` does not require a heading

`_top_section()` uses `blank.find(ENDPOINT_HEADING)` for the string form. It
does not anchor the title at the start of an unindented line. With the real
ENDPOINT heading replaced by each of the following non-heading forms,
`_prd_conformance()` returned **PASS** instead of refusing:

```text
Narrative reference only: ## ENDPOINT (step 2, /endpoint --forward)
    ## ENDPOINT (step 2, /endpoint --forward)  [indented code]
```

The helper and its call sites say "top-level heading only," so these are direct
counterexamples to the claimed invariant. The next-section search is also
hard-coded to `\n## ` rather than sharing an anchored heading matcher.

### Open falsifier 2 -- `_blank_fences()` does not blank every fenced block

The helper blanks only text between literal triple backticks:

```python
re.sub(r"```.*?```", ...)
```

A PRD whose only exact ENDPOINT title and outcome cards were inside a `~~~`
fence passed. A PRD whose only SURFACE MANIFEST title and non-trivial body were
inside a `~~~` fence also passed. Both should refuse under the gate's stated
rule that a heading inside a code fence does not count. This is not a new gate;
it is a bypass in the already-authorized top-level-heading check.

The repair bar is one shared parser/matcher that recognizes an unindented
level-2 heading outside all admitted Markdown fence forms, then finds the next
top-level section with the same grammar. Add the mid-line, indented-code, and
tilde-fence cases to the standing red/green battery.

### Open falsifier 3 -- `brief_ref` traversal is still open on Windows

The pattern excludes `/` from a path segment but not `\\`. Both of these
values matched the schema on this Windows repository even though they escape
or cross the declared segment boundary when resolved as Windows paths:

```text
docs/briefs/..\architecture\_PRD_TEMPLATE.md@abcdef0
org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_x\..\..\OTHER.md@abcdef0
```

Exclude both path separators (or normalize then validate) and apply the dot
segment rule to the normalized path. Add both cases to the schema battery.

The pass-1 extension falsifier also remains:
`docs/briefs/not-a-brief.txt@abcdef0` still validates. The schema description
declares this branch to be a CRO brief and the template presents `.md` as its
shape. Either constrain that branch to the adopted brief extension or amend
the declared domain explicitly; the regex and its contract must say the same
thing.

### Pass-2 disposition

The carrier happy path, adopted manifest field, and staged-register seam are
**GREEN**. The shared top-level-section parser and the declared `brief_ref`
domain remain **RED/PARTIAL**. Therefore step 6 limb 5 is not yet closed by
`f5f7481015`. The unrelated `PRD_HEADER.status` Rule-24 proposal remains
unadopted, and the known ETFS instance's `outcome` column remains an explicit
instance deviation rather than a defect in this generic carrier patch.

## Pass-4 re-grade -- `ef6a37e098`

The three graded implementation/control paths are byte-identical between the
pinned commit and the live bytes exercised; the commit is an ancestor of
`HEAD`, with no worktree divergence in those paths.

### The six reported falsifiers are closed

- The committed battery passes **18/18 core, 13/13 schema, 4/4 limb 4, and 2/2
  wrapper** controls.
- A mid-line ENDPOINT title and an ENDPOINT title in indented code no longer
  count. The limb-5 core correctly defers the absent-section decision and the
  shared limb-4 check refuses both at the applying gate grain.
- ENDPOINT and manifest sections inside exact column-zero `~~~` fences no
  longer count.
- Both prior Windows-backslash traversal specimens and the non-`.md` CRO
  specimen now fail the `brief_ref` pattern.
- The full template instantiation remains green, as do Ruff, Python
  compilation, and the Draft-07 meta-schema check.

The disclosed first-control grain error is repaired correctly: absence of an
ENDPOINT section is owned by limb 4, so a core deferral is not mistaken for a
gate pass. The disclosed heredoc escaping failure is historical and does not
remain in the committed Python carrier.

### Open falsifier 1 -- the fence grammar recognizes only one spelling

`_FENCE_RE` recognizes an opening marker only when it is exactly three
backticks or three tildes at column zero, and requires the same exact
three-character marker at column zero to close it. The repository itself uses
Markdown fences indented by one to three spaces in architecture documents, so
column-zero is not the estate's only fence carrier.

Independent gate-level specimens produced these results:

```text
ENDPOINT wholly inside a four-tilde fence       -> limb 4 PASS (should REFUSE)
ENDPOINT wholly inside a one-space ``` fence   -> limb 4 PASS (should REFUSE)
manifest wholly inside a four-tilde fence       -> limb 5 core PASS (should REFUSE)
manifest wholly inside a one-space ``` fence   -> limb 5 core PASS (should REFUSE)
```

The first four-backtick ENDPOINT specimen happened to refuse only because the
outer marker was mispaired with an inner triple-backtick FWD-card marker. That
is not evidence that variable-length fences are parsed; it is evidence that
the exact-three regex can pair the wrong delimiters.

Either define and enforce exact column-zero triple markers as the only legal
PRD fence syntax, or make the shared parser recognize the fence syntax the
repository already carries: permitted indentation, marker runs of at least
three characters, a closing run compatible with its opener, and an unclosed
fence consuming the remainder of the document. Add indented and four-marker
ENDPOINT/manifest cases to the standing limb-4 and limb-5 controls.

### Open falsifier 2 -- newline bypasses the `brief_ref` exclusions

The pattern begins with `(?!.*\\)`, but `.` does not cross a newline. The
subsequent `[^/@]+` path components do. Python Draft-7 validation therefore
accepted all three of these non-citations:

```text
docs/briefs/safe\n\..\architecture\x.md@abcdef0
docs/briefs/safe\n/../x.md@abcdef0
docs/briefs/x.md@abcdef0\n
```

The first bypasses the claimed no-backslash invariant, the second bypasses the
dot-segment lookahead, and the third is accepted because Python `$` matches
before a final newline. Exclude CR/LF as path characters before the separator
and traversal checks, and use an end condition that cannot stop before a final
newline. Add all three values as schema negatives.

### Pass-4 disposition

The six pass-2 findings are **GREEN**. The generalized top-level-section claim
and the declared `brief_ref` domain are still **PARTIAL** at new, independently
reproduced boundaries. Step 6 limb 5 therefore remains open after
`ef6a37e098`; the unrelated `PRD_HEADER.status` proposal remains unadopted.

-- 3.0.0_SA_CVO~A
