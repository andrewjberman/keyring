# AMGT_RESAPP.TO-AMGT-rd-4 -- THE FOUR HARVESTERS: Seeking Alpha, FT, Bloomberg and WSJ writing per-ticker articles into `opal-amgt-articles`, each dispatching on the PLATFORM'S OWN identifier, never a bare ticker

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rd-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~1</issued_to>

## THE CELL, INLINED IN FULL (round 5/v5, rows S4 + S13, FWD-4 / FWD-11)

```
AMGT-rd-4. THE FOUR HARVESTERS. Seeking Alpha, FT, Bloomberg and WSJ, running on the ONE shared box
`AMGT-rd-3` stood up, writing per-ticker article content into `opal-amgt-articles`.

TWO RULES GOVERN WHAT MAY BE WRITTEN, and both already exist -- neither is invented here:

  1. ADMISSION IS THE NEWS/SOCIAL RULE `AMGT-s-11` ALREADY STATES. An item is admitted by that rule or it
     is not written. Do NOT mint a new qualification threshold: no threshold exists anywhere upstream in
     this project and none may be invented (the PRD says so in terms). If the landed rule refuses an item,
     that refusal is the correct behaviour and is evidence, not a bug.

  2. IDENTITY BEFORE DISPATCH, VIA S12. Each platform's OWN identifier is resolved through the S12
     identity layer BEFORE the fetch: the Seeking Alpha symbol-slug, Bloomberg's `"TICKER US Equity"`,
     the FT id. NEVER dispatch on a bare ticker.

WHY RULE 2 IS THE ONE THAT BITES. This is the direct carry-forward of F6 -- 48 of 54 existing packs carry
another company's peer set because an identity was assumed rather than resolved. An acquisition cell that
dispatches on a bare ticker REBUILDS THAT DEFECT ON A NEW AXIS: you will silently harvest the wrong
company's articles for any name whose ticker is ambiguous across platforms, and the page will look right.

RAW VENDOR BYTES LAND BEFORE DERIVATION. The fetched payload is persisted as received; sentiment,
normalisation and any derived field come after, from the persisted raw.

WHAT TO PRODUCE, under integrations/ + lib/research/ + .../deliverables/0.9.0_WK_AMGT_RESAPP~1/:

  (a) THE FOUR HARVESTERS  one per platform, each resolving identity through S12 first, each admitting by
      AMGT-s-11's rule, each writing to `opal-amgt-articles` with ticker/security_key and platform set.

  (b) THE IDENTITY-REFUSAL PATH  a name whose platform identifier CANNOT be resolved is NOT harvested on
      a guessed identifier. It is skipped with a stated reason that a reader can see.

  (c) THE RAW-BEFORE-DERIVED RECORD  a deliverable showing, for at least one real name per platform, the
      raw payload landing before any derived field is computed from it.
```

## DEPENDENCIES

**DEPENDS ON `AMGT-rd-3` (the harvester box), AND THAT DEPENDENCY IS A VENDOR-WORD GATE, NOT ONLY A HOST
GATE.** `C-VENDOR-WORD-HARVESTERS` gives the per-use word for these four vendors **effective when the
harvester box is stood up and ready to run -- NOT before.** So until `AMGT-rd-3` has landed, you may not
egress to Seeking Alpha, FT, Bloomberg or WSJ at all. Worked THIRD in slot ~1's queue. Also reads
`AMGT-rd-1`'s landed table and the landed S11/S12 work from rounds 1-4.

## BOUNDS

```
BLOCK THE VENDOR WORD IS NARROW AND TIME-SCOPED. It covers Seeking Alpha, FT, Bloomberg and WSJ, for THIS
  project's harvesters, effective only once the box is up. It is NOT a blanket grant: C-VENDOR-EGRESS
  still binds every OTHER vendor and every OTHER use, and "availability is not authorization" is
  unchanged. Calling a fifth vendor is a hard stop, not a judgment call.
BLOCK IDENTITY BEFORE DISPATCH, ALWAYS. Never a bare ticker. An unresolvable identifier is a SKIP with a
  stated reason, never a guess.
BLOCK NO NEW QUALIFICATION THRESHOLD. Admission is AMGT-s-11's landed rule. No number is invented here.
BLOCK RAW BEFORE DERIVED. Persist the vendor payload as received before computing anything from it.
BLOCK C-NO-CONTACT: NO SEAT CONTACTS ADAM MULLER. Requirements reach him through Andrew and no other route.
BLOCK NO MONITOR, NO ALARM, NO SNS, NO FRESHNESS CHECKER on the harvest. Standing moratorium.
BLOCK NO non-ASCII in code, logs or AWS.
BLOCK Credentials are LOCATED at run time (Secrets Manager); no secret name is hardcoded and no secret is
  written anywhere.
WARN Bound every invocation under `timeout 120`. Do not name a live vendor fetch as a criterion's
  invocation if it cannot terminate inside that budget -- exercise it in the cell and assert on the
  PERSISTED result.
```

## BATTERY FINDINGS THAT TOUCH THIS CELL

```
PRD s.3b C-AMGT-ARTICLES-STORE: "S12 must resolve each platform's OWN identifier before dispatch
    (SA symbol-slug, Bloomberg `"TICKER US Equity"`, FT id)." This is the cell's central bound.
PRD s.3b C-VENDOR-WORD-HARVESTERS (TIME-SCOPED): the four vendors, this project's harvesters only,
    "effective when the harvester box is stood up and ready to run -- NOT before."
F6, CITED NOT CONFIRMED (the CRO's brief; re-measure before relying on it): 48 of 54 packs (88.9%) carry
    a stale peer set copied from one workbook. The measured instance of identity-assumed-not-resolved.
PRD s.3a / C-SA-SESSION-SHAPE and siblings (from AMGT-s-b4, LANDED): the Seeking Alpha route is
    `GET /api/v3/symbols/{ticker}` -> sa_id, then the analyst/article endpoints; NO HTML parsing on the
    path; a 200 with a 2-byte body is a FAILURE; a small-challenge 403 is a RE-HARVEST signal and never an
    auth failure; no POST through the proxy. Reuse that landed route rather than re-deriving it.
comp-iam gaps (at the cut): no AMGT role existed at the cut; AMGT-rd-3 creates it. Your writes go through
    THAT role -- if a PutItem is refused, that is an IAM finding for rd-3, filed as a row, not worked around.
```

## PATHS -- your write surface IS this list, and nothing else

<paths>
integrations/bloomberg/research/
lib/research/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rd-4.four-harvesters-identity-before-dispatch.md
</paths>

Your deliverables go in `deliverables/0.9.0_WK_AMGT_RESAPP~1/`. A path missing from that block is a path you
are REFUSED on. Refuse a criterion you cannot satisfy as written and report it; file a surprise ROW
(`AMGT_RESAPP-Z-W1-S<k>` continuing your prior sequence) and STOP on that criterion if you need a surface
not listed. MINT THE ROW ID FROM A RE-READ of the channel file, never from recall.

## PROOF OF SPEC

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rd-4"><invocation>timeout 110 python -m pytest lib/research -q -k "harvest or identity" 2>&amp;1 | tail -3</invocation><expect>a summary line with a passed count and no "failed" -- the harvester tests pass, INCLUDING a test that a name whose platform identifier cannot be resolved is SKIPPED with a stated reason rather than dispatched on a bare ticker. A suite with no such test is NOT met</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rd-4"><invocation>timeout 110 .tools/aws dynamodb scan --table-name opal-amgt-articles --max-items 5 --projection-expression "ticker,platform" --output text 2>&amp;1 | tail -8</invocation><expect>at least one row carrying BOTH a non-empty ticker AND a non-empty platform -- real harvested content landed with identity attached. An empty table, or rows missing platform, is NOT met</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rd-4"><invocation>timeout 110 comp-find "symbols/" integrations lib --limit 20 2>&amp;1 | tail -12</invocation><expect>the Seeking Alpha route resolving a SYMBOL to an id before any article fetch appears in the harvester source with a printed denominator -- i.e. identity resolution precedes dispatch in the code, not only in the docstring. A denominator of 0 hits across 0 files is OUT-OF-CORPUS and proves nothing, so it is NOT met</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rd-4" judgment="true"/>
</proof_of_spec>

### What each criterion means
- **AC1** (mechanical, includes the refusal arm): the unresolvable-identity path SKIPS rather than guesses.
- **AC2** (mechanical, LIVE plane): real rows landed carrying ticker AND platform.
- **AC3** (mechanical, denominator-bearing): identity resolution precedes dispatch in the actual code.
- **AC4** (JUDGMENT -- never self-graded; UNVERIFIABLE-BY-INSTRUMENT, status_reason names `3.0.0_SA_CVO~Z`): does each of the four harvesters genuinely dispatch on the PLATFORM'S OWN identifier resolved through S12 -- so that F6's assumed-identity defect is not rebuilt on the article axis -- and was admission governed by `AMGT-s-11`'s landed rule with NO new threshold invented? Also: did any vendor egress occur BEFORE `AMGT-rd-3` landed, which the time-scoped word forbids?

Every invocation runs under `timeout 120`. A timeout is recorded AS the output.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

<status>staged</status>
<round>5</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<dep_stage>EXECUTING</dep_stage>
<issued_by>2.0.0_SA_COO~ZZZ</issued_by>

**Issuer:** `2.0.0_SA_COO~ZZZ` (L5 v0.6.1 + L6 round 5) - **Project:** AMGT_RESAPP - **PRD:** v0.4 @6c52a4e380 (L4-R ADMITTED)
**Authority chain:** L10 round-4 analysis @959ba3e947 -> PRD s.3b `C-AMGT-ARTICLES-STORE` + `C-VENDOR-WORD-HARVESTERS`, ANDREW-DIRECT 2026-09-11 ~12:1xZ -> L5 decomposition v0.6.1 @d0efe81ca8 (section 13, AMGT-rd-4) -> this round-5 issuance.
**Chain:** round 5 (v5), CHAIN A tail, slot ~1. Handed after `AMGT-rd-3` lands -- which is BOTH the host gate and the vendor-word clock.
**Provenance:** decomposition v0.6.1 section 13b's `AMGT-rd-4` row.
> **NOTE (2.0.0_SA_COO~ZZZ).** The vendor word is the sharpest thing in this order. It is time-scoped to the box being up, and a worker that starts fetching while `AMGT-rd-3` is still in flight has spent a word Andrew gave conditionally. That is why the dependency is stated as a vendor-word gate and not only a sequencing note, and why AC4 asks the CVO to check it explicitly.
<preflight>
comp-schedule: RUN -- 5 of 5 carriers; C3 = 12 standing NEVER clauses, incl. the no-monitor moratorium and the standing vendor-egress law. BLIND: C4/C5 not decidable.
comp-iam: RUN -- 836 call(s) across 96 mapped role(s); no AMGT role at the cut, so this cell's writes ride the role AMGT-rd-3 creates. BLIND: 630 UNRESOLVABLE-RESOURCE, 266 calls in 26 role-UNMAPPED services never checked, 51 GRANTED-BROAD excluded not cleared.
comp-adversary: RUN -- 1 artifact declared (decomposition v0.6.1 @d0efe81ca8). BLIND: author's stated evidence context only.
comp-blast: DECLARED-NOT-APPLICABLE -- no shared served artifact moves; the table is this project's own.
</preflight>
**Preflight disposition:** acquisition cell, vendor-egress-bearing, gated on the box. Identity-before-dispatch is the carry-forward of the only defect this project has measured in production, and it is both a BOUND and the judgment criterion.
