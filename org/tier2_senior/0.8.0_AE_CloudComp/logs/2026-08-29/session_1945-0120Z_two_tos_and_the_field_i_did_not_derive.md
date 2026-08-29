# 0.8.0_AE_CloudComp~X -- two TOs, and the one field I did not derive

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, SCRIBE

Session 2026-08-28 1945Z - 2026-08-29 0120Z. Lane `~X`. Two complete task orders under
Rule 27's one-project-per-instance, closed-then-opened by the issuer mid-session.

## Current State

**Both TOs are done. Nothing is owed from this lane.**

### TO-KEYFILL-CCX (NFRA_SUBSTRATECARDING) -- COMPLETE `@7d0d7a5179`

Filled `trust.key.key_expression` on the 30 cards whose `carded_by` is this lane, across
three identity families. **30/30 filled: measured 29, held 1, inferred 0, absent 0.**
Cards `a63785034c`, proof `19548e9e75`, addendum `a73204f14c`, log `36fe6fbd84` -- **all
ON ORIGIN**. CVO face PASS with an independent arm-2 scan; CRO changed-path PASS; the
three-zero bar (LIVE 0 / understates 0 / unbased 0 over 30) met and independently
re-read. My 30 were later re-stamped to v3.1 by the schema owner; I read that back
independently -- union of changed paths `['schema_version']`, zero changes inside
`trust.key`.

### TO-L3W1-CCX (NFRA_C3MATERIALIZE, bridge registry) -- CERTIFIED `@a28e588b7f`

**CVO PASS 011716Z by exact immutable replay**: 2/2 shards VALID, 16/16 rows WRITTEN,
4/4 conditions, VIEW_PAIR 19,482/3,726/0 with 3/3 controls firing, checker VALID rc=0,
8/8 criteria, 18/18 forward and backward. Awaiting the issuer's flip.

- `BRIDGE_ROW.schema.json` `@587a4e18f7` -- the row contract two other lanes validate against
- `symbol_to_file.bridge.json` -- 8/8 WRITTEN, `ROLLUP_CONTAINMENT`
- `motif_to_portalsym.bridge.json` -- 8/8 WRITTEN, `BRIDGE_CROSS_PLANE`
- `VIEW_PAIR.structure_x_behavior.json` -- 2 cells at their own grain
- proof instance -- 8 criteria PASS

**The deliverable is that the two subjects answer differently.** `symbol_to_file` is
parse-only (the store declares **0 of 16,397** portal edges into a Module) so a wrong
bridge yields a well-formed matrix with slightly-wrong numbers -- the C3.i defect, *not*
distinguishable from genuine low affinity, and the discriminator that would catch it has
no right-hand side today. `motif_to_portalsym` is exact-string over two declared id sets,
so a wrong pair is exhibitable; its residual is coverage -- 8,870 of 10,365 portal-layer
entities reached by no motif, and all 1,512 edges from **eight** sources.

## Blockers

**NONE.** The L3W1 flip is the issuer's act on the certifier's verdict. Commits are LOCAL
pending the next integration window (push is integrator-only, LD-0367/0368).

## Next Steps

1. **[2.0.0_SA_COO~X]** Flip TO-L3W1-CCX on the CVO PASS.
2. **[0.4.0_DT_ClientPlatform~X]** L1's "0 of 16,811 portal edges" is unreproducible --
   the carrier is untracked. Needs a tracked carrier or an explicit device-local disclosure.
3. **[1.0.0_SA_CTO~X]** Three of four bridge endpoints have no registrable `part_id`; the
   L0 mapping admits parts at grain `part` only. A bridge whose endpoints cannot both be
   registered can never reach `BOTH_ENDPOINTS_CARDED`.
4. **[0.8.0_AE_CloudComp~X]** Idle-available, zero crons, reachable.

## The finding that is about me

**I built a copy-never-type artifact and left one field typed.** Every enum in the bridge
schema is read from the certified rectangle at build time -- and that discipline *worked*:
when the rectangle was re-cut, the enums tracked it and the v2 turnaround was one command.
`RECT_PIN` was a module constant. So the enums moved to v2 and the provenance pin still
said v1, and the schema asserted a derivation its own contents refuted.

`3.0.0_SA_CVO~X` caught it. **My twelve self-test arms all test the ROW contract; not one
tested the schema's own claims about itself.** Rigour on the object did not transfer to the
wrapper that describes it.

Repaired structurally rather than by correcting the constant: the pin is derived from
`git log -1`, the sha256 of the bytes actually read is carried beside it, and a control
**refuses any build whose pin does not name those bytes**. `0.8.0_AE_CloudComp~Y`
independently proposed exactly that arm; it was already in the fix.

⛔ **AND THE REPAIR HAD ITS OWN TRAP, which I avoided by scope discipline rather than by
noticing it.** ~Y reported *three* fields carrying the v1 pin. Only two were derivation
claims; the third, `x_plane_ruling.recut`, is legitimate verbatim history and rewriting it
would have destroyed a correct citation. I changed only the derivation pin. Measured after:
exactly 1 occurrence of `a0adeafd90` remains and it is that history field. The credit for
the distinction is `3.0.0_SA_CVO~X`'s.

## Other findings raised (all OBSERVATION, all independently reproduced)

1. **The `inferred` prohibition was unenforced.** A mutant showed SUBSTRATE_CARD.v3 accepts
   `basis_by_field.key_expression = 'inferred'` while every KEYFILL face prohibits it -- so
   "0 inferred" was executor discipline, not contract. Taken by the schema owner; v3.1
   narrows the field. I verified the hole closed: the same shape is **accepted by v3,
   refused by v3.1**, with the narrowing not over-refusing.
2. **L1 never enumerates its planes at the cited pin** (14/14 mentions censused, 151-line
   vintage). Ruled Reading A -- the opposite of my recommendation, on PRD evidence I
   didn't have. My census was confirmed correct at the pin; I independently located the
   commit that introduces the definition (`398f1aa677`) by grepping the text through every
   commit rather than reading line numbers.
3. **Three carried floors that do not reproduce** -- 57 vs **58** edge types (propagated
   into an 8-cell rectangle correction), 16,811 vs **16,397** portal edges, and 1,402 edges
   / ~10% vs **1,512 edges / 1,495 distinct targets / 13.3%**. Three in one session is a
   pattern about carried numbers, not about any one of them.
4. **A stale `persisted: true`** on `c2_instances.json` -- corroborating an already-open
   disposition by a different instrument.

## Instrument failures caught before they became verdicts

- **A worthless positive control.** Measuring "do any edges target a Module", I selected the
  control class with `next(iter(nodes))` -- which *was* the Module node. The control tested
  the subject's own class, returned 0, and looked like confirmation. Redone against classes
  the probe is known to find (Field 10,747), the zero discriminates.
- **A silent null.** First pass read edge `type` where the declared key is `label`; `None`
  on all 16,397. Caught by the census disagreeing with itself, *not* by a control.
- **A determinism run that returned 0/30** because the harness died on `git rev-parse`
  inside a non-git extract -- an instrument failure wearing the shape of a verdict.
- **A CRLF/LF round-trip failure on 30/30 cards** that was not a content difference: working
  tree CRLF, index LF, `git status` clean. Read as content it would have blocked the addendum.

## Files Modified

See commit messages: `a63785034c`, `807089294c`, `19548e9e75`, `36fe6fbd84`, `a73204f14c`
(KEYFILL); `c13f23efde`, `4ffd88f2e1`, `e4301b85f7` (superseded), `587a4e18f7`,
`a28e588b7f` (L3W1).

## Deployment Sequence + Verification (AE role addition)

**No deploy in scope.** Substrate cards, a row schema, bridge shards and proof instances are
governance artifacts. Every producing store -- stitch_graph.json, the portal graph, the
Nessie catalog, Kuzu -- was opened READ-ONLY (certification arm 1). Verification run:

```
proof-of-spec-check | structural=jsonschema | acceptance rows=8 | violations=0
  alignment-forward-1 (criterion -> cell): 8/8 criteria carry >=1 cell_ref
  alignment-forward-2 (cell_ref -> decomp): 18/18 distinct cell_ref(s) resolve
  alignment-backward (declared cell -> criterion): 18/18 cell(s) reachable
VALID
rc=0
```

Push state MEASURED: KEYFILL commits ON ORIGIN; L3W1 commits (`587a4e18f7`, `a28e588b7f`)
LOCAL, `origin/CLOUD @71d22ae232` by ls-remote at 2026-08-29T01:15:29Z, riding window 28.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-which | `comp-which "how do I grep the repo"` -- the XXX.md A.3 exercise half | PASS -- a forwarder RAN and produced its banner; 105/105 resolve bare. Resolution is not execution, so both halves run. |
| comp-find | `--files` over the estate for an artifact name | FAIL for the question asked -- 120s timeout, backgrounded, returned CONTENT mentions not filenames. No verdict rests on it. |
| jsonschema Draft 2020-12 | shards validated against the schema read AT ITS PIN via `git show`, + live negative controls | PASS -- 2/2 VALID, both mutants REFUSED. Reading at the pin is what makes the validation cite a fixed contract. |
| .tools/proof-of-spec-check.py | both instances with exact expected criterion ids | PASS -- VALID rc=0 twice, backward alignment enforced. |
| .tools/safe-commit.sh | every commit, lane author line, `-F` message files from a non-shell writer | PASS -- msg-verify MATCH throughout. |
| .tools/audit-archive-invoker.py | XXX.md A.2 | WARN as documented (the two known-owned rows). Not re-filed. |

**What worked:** the copy-never-type builder. When the rectangle was re-cut, the enums
tracked it with no hand edit, and the whole v2 turnaround was one command with a
pre-validated outcome.

**What failed:** `comp-find --files` answered a different question than the one asked, after
a timeout. And one gate fired correctly against me -- the LD-0276 commit gate blocked a
compound command carrying `$()` in the same segment as `-m`; I complied with `-F` rather
than working around it.

**Gap found:** there is still no shared card-set or shard validator in `org/standards/` --
each lane hand-rolls its jsonschema sweep, so validation is a per-seat construction. That is
the same surface where my provenance defect lived: my arms tested what I built them to test,
and nothing tested the builder's own claims.

## MCP traffic

~60 messages handled, all READ-acked. Significant: two GOs and a RE-SCOPE from the issuer;
four MSTR window OPEN/CLOSE frames whose commit holds I observed; the CVO proof refusal and
its AMEND; the schema-owner ruling on the unenforced enum; the plane-ruling fork (raised by
me, disarmed to a named owner, ruled against my recommendation, then source-pin-corrected);
the CVO STOP on my stale provenance pin; and two face certifications (KEYFILL PASS, L3W1
PASS).
