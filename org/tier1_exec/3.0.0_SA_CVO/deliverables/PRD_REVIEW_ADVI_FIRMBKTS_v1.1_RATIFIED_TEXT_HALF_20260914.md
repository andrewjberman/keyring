# PRD REVIEW -- ADVI_FIRMBKTS v1.1 @2a9ae97c19 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96564.

**Prior:** v1.0 was REFUSED on R1, R2 and R3, in the review @`10729854d0`. The v1.0 stamp never landed.
`prd-signoff` refused it because the shared tree already held the uncommitted v1.1 bytes, so that review is the only
record of the v1.0 verdict.

**v1.1 was not written against that review.** It was committed at 10:11:38Z, and the review's message reached
`1.0.0_SA_CTO` at 10:11:05Z, 33 seconds earlier. v1.1 answers `4.0.0_SA_CRO`'s refusal of v1.0. It closes this seat's
R2 and R3 on its own and leaves R1 as it was.

**Read, UTC 2026-09-14, after 10:12:02Z:**
- The PRD @`2a9ae97c19`. The working copy is identical to the pin.
- A section-by-section diff against v1.0 @`ecac007bf3`, through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- The three changed CONTRACTS rows, read in full.
- `LGIC_NAMING`-S7 @`acc5f3782b`.
- The sources read for v1.0, at the same vintages.

**Half hash reviewed:** ratified-text `c46ed3a59272e222bdfe325fd5c3a501b9c2ae660c2b4afe3decfb8f02b5d68d`. It matches the
notifier's `c46ed3a59272`.

## VERDICT: REFUSE -- one change, R1 (unchanged from v1.0). R2 and R3 are closed.

## THE DIFF OF THIS HALF, v1.0 -> v1.1

- **ENDPOINT is byte-unchanged,** so v1.0's finding carries: 8 of 8 outcomes verbatim, and every constraint outside the block is carried.
- **CONTRACTS changed on three rows:** the key string, the serving grants and the tenant assertion.

## R2 -- CLOSED (the tenant assertion)

| what the v1.0 review asked | v1.1's row |
|---|---|
| define the session's firm through the registry, aliases included | *"the path's firm segment resolves through the registry, aliases included, to one firm"* |
| admit internal staff by their selection | *"for internal Opal staff (`opal-capital`) the `?firm=` selection they already supply"*. That matches `advisor-intelligence.ts:303` and `index.mjs:227-241` |
| use the router's boundary, not the bare test | *"that firm's bucket equals the caller's validated tenant bucket ... today's boundary, no wider and no narrower (`index.mjs:367-373`)"* |
| keep DEC-3's protection against twins | *"The key is then BUILT with `{scope}` equal to the resolved firm, never copied from the raw path, so a key's scope always equals its bucket's firm"* |

This is stronger than the fix asked for. Building the key from the resolved firm makes the scope check hold by
construction. And with per-firm buckets, LD-0442's latent bucket-equals-firm hazard stays closed.

## R3 -- CLOSED (the serving grants)

- **The grant is now in the key's own grammar:** *"`{source}/{firm}/platinum/*` for each served source, GENERATED from the mapping table's platinum destinations (F2) and the consuming projects' declared prefixes ... never a bucket-wide grant"*.
- **It covers the counterpart:** `MDPF_CANON`'s slice, `mdpf/{firm}/platinum/{table}/{leaf}.json`, sits under `mdpf/{firm}/platinum/*`. So the row now agrees with `MDPF_CANON_PRD.md:180`.
- **The legacy `gold/*` grant is not carried.** Gold is not served (R12), and a CloudFront read under a legacy `gold/` key is either a platinum file for the table to place or a table fault. That is coherent with FWD-2.

## The key-string row's other change holds

- **Code is HELD, not typed.** `{tier}` in a firm bucket is now gold, platinum or state, and `code` is held pending `LGIC_NAMING`-S7 (@`acc5f3782b`). S7's disarm owner names this same hold.
- **The rule covers held families too:** *"a family the builders cannot yet construct is HELD, never hand-spelled"*.
- **Both holds are named:** S6 for entity-keyed files, and S7 for code.

## R1 (blocking, unchanged) -- the platinum vector keeps a snake_case served name that the schema says is kebab

- **The vector is byte-identical to v1.0's:** `key("advi", "49financial", "platinum", "firm", "header_metrics.json")`.
- **The schema:** `NAMING_SCHEMA.json:35` (*"a platinum leaf is a kebab-case .json file (the served names)"*) and `LGIC_NAMING` S1 (`:125`).
- **The world:** 12 of the 15 ADVI served leaves are snake_case (`adviKeyRepoint.ts` @portal `3ade1aba`), and `MDPF_CANON` v2.2's vector uses kebab-case.

**The fix is unchanged from v1.0 R1.** Say which rule governs a legacy served name:
- **(a)** it is kept byte-for-byte, with `LGIC_NAMING`'s admission of that exception named as a dependency, the way the row already names S6 and S7; or
- **(b)** the object is renamed to kebab-case behind a per-leaf edge mapping.

REC: (a). The decision is `LGIC_NAMING`'s, and it is carried there as row `LGIC_NAMING`-S8, filed with this review.
With (a), this row only has to name the hold, as it does for code.

## NOTES (non-blocking)

- **N1:** carries (the entity family waits on S6).
- **N2:** carries (`IRPT_BCKEND` parity is NOT EVALUATED).

## NOT CLAIMED

- **The brief half.** It is `4.0.0_SA_CRO`'s. Five of its sections changed in v1.1, and they are not graded here.
- **That either vector runs.** `lib/opal_naming.py` does not exist yet.
- **That the generated grant list or the edge rule can be built.** That is F4's and F6's, at L5.
