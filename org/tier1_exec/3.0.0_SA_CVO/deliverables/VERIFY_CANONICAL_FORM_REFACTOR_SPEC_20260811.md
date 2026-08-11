# VERIFICATION -- CRO's CANONICAL-FORM REFACTOR + DECOM SPEC @85e1d6d980 (+1c @b0e6815764)

**Verifier:** 3.0.0_SA_CVO (named in-commission) · **2026-08-11, pass 0747-0755Z** · **archetype:** VALIDATE
**Method:** the spec's own six sec6 hooks, attacked in materiality order; live/at-rest measurement
wherever a hook is measurable. Live reads 07:48-07:54Z. The mid-pass sec1c amendment (@b0e6815764,
Andrew's A-or-B bucket reshaping) is folded -- my hooks are orthogonal to that decision and every
verdict below survives either option, consistent with the spec's own claim.

---

## VERDICT: **VERIFIED-WITH-AMENDMENTS** -- the five-layer form, the 19-row disposition table, the
## repoint map, and the gate-carrying all stand; ZERO dispositions refused; FOUR amendments, two of
## them measured tonight rather than argued. Build may decompose (post-FINAL) on the amended spec.

## HOOK RESULTS

**(1) "No gold-JSON consumer outside the publisher" -- CONFIRMED, WITH A NAMING AMENDMENT.**
Independent census: 417 hits / 25,251 files (CRO's 411 + today's own commits -- the estate moved
under the census again, expected variance). 34 distinct non-doc files, every one classified:
writers (consolidator/accrual/aum_metrics + the W-1a emitter) · publisher-family readers ·
instruments+config (pipeline_cli, safe_deploy_core, nerves-edges, manifests) · TF/IAM · tests/
evidence/fixtures. NO consumer outside the publisher family. **THE AMENDMENT: "the publisher" is a
FAMILY OF TWO** -- `opal-assets-mdpf-portal-publisher` (same-bucket, live 13:50Z) AND
`mdpf_egress_publisher.tf` (cross-bucket successor, reads `portal/gold/mdpf/*`, writes portal-v2
staging+live prefixes; the wo2 repoint schedule sits in `.open_deploys/`). M7's repoint row says
"publisher" singular -- **it must name both members, and the input-format flip must be sequenced
WITH the in-flight wo2 publisher transition as one ordered act, not two independent flips on one
family** (a format flip landing mid-repoint is a collision candidate).

**(2) M1 per-feed silver-equivalence -- THE PRECONDITION'S METHOD IS REFUSED AS STATED; the
disposition stands.** Measured (the headline feed, model_aua_positions/49financial, vs
fact_allocation_account_map): join coverage 7,220/7,230 ties; TOTALS tie within 0.237%
($1.4676B vs $1.4711B -- one-trading-day-plausible); **row-wise value tie = 9 of 7,220 (0.12%)
across the closest available vintages -- and the SAME-STATE pair is STRUCTURALLY UNAVAILABLE AT
REST: the map's weekend partition is EMPTY (0 rows, date=2026-08-08) while the feed labels weekend
dates; the channels pull on different clocks (03:31Z TUE-SAT vs 13:55Z daily).** So "one at-rest
diff each" cannot discriminate content-inequivalence from clock skew, structurally. **AMENDED
METHOD, required: the per-feed equivalence check is either (a) SAME-STATE -- both pulls fired in
one window at build, diffed -- or (b) tolerance-framed with the inter-pull market delta priced
EX-ANTE and both denominators printed.** The M1 rebuild-then-retire disposition itself is sound.

**(3) M8 bell-repoint safety -- INHERITS (2), WITH THE STAKES NAMED.** The spec is right that the
equivalence IS the never-widen evidence -- which is exactly why the at-rest method cannot carry
it: **a never-widen co-sign on the client-facing bells cannot rest on a diff that a weekend of
market movement would also produce.** Same-state method REQUIRED for the M8 window. (The bells'
live state re-confirmed this session: 49financial+inflection 08-10T11:30:39Z.)

**(4) The Group-D emitter-format cell -- CONFIRMED, no conflict.** My D spec's emitters consume
C-canonicals with no JSON-format assumption, serve via the publisher pattern, and the B/C
canonical artifacts are parquet tables under the same partition grammar -- gold-as-parquet is
CONSISTENT with the archetype as specced. One clarification folded at next touch: state "canonical
= parquet" explicitly in B §1 so the format is a contract, not an implication.

**(5) Citation resolution -- CONFIRMED.** All 8 pinned commits resolve (`git cat-file -t` =
commit x8); the DEBTCLEAN :830 verbatim confirmed in place; the map's daily partition series
(since 07-14) corroborates the M1 substrate claims. Sec1c's added measurements accepted as
scope-growth per the mid-pass flag.

**(6) No-shadow compliance -- ONE SEAM AMENDMENT; no standing-channel smell anywhere else.**
Every port row is flip+rollback. **The seam: P1 (builders rebuilt parquet-writing) and P2
(publisher input flip) are separate phases, so each served family has an UNSTATED window where
either (a) old JSON writers and new parquet builders both run -- an unnamed bounded parallel --
or (b) old writers stop at P1 and the served surface starves until P2.** Neither is stated.
**AMENDMENT: per-family atomicity -- builder flip + publisher-input flip in ONE window per served
family (rollback = both re-point back), OR the interim old-writer continuation NAMED with its end
condition and date.** A bounded, named transition is build-correct-and-port; an unstated overlap
is how a shadow is born without anyone deciding to build one.

## WHAT RIDES TO WHOM

- CRO: fold amendments 1/2/3/6 (a paragraph each); (4) is mine to fold in B at next touch.
- CTO: the wo2-collision sequencing note (amendment 1) touches your arch gate; the sec1c A-or-B
  naming decision is at Andrew with CRO's rec A -- my verify is deliberately orthogonal to it.
- COO: decomposition (post-FINAL) inherits the amended preconditions -- M1/M8 rows carry the
  same-state method as their named precondition.

## What you should have asked but did not (Doctrine §7)

What the EMPTY weekend map partition means for L2's event-driven law generally: a converter that
fires on bronze landing and writes an EMPTY partition on no-data days is emitting a
well-formed-but-vacuous artifact -- downstream joins silently lose coverage on exactly the days
nobody is watching (my hook-2 discriminator died on one). The refactor's L2 contract should say
which of empty-partition / no-partition / carry-forward is the law on no-data days -- one line,
and every consumer's join semantics become decidable instead of discovered.

-- 3.0.0_SA_CVO
