# ANDREW-DIRECT 2026-08-27 ~18:5xZ — POSITIONING MULTI-TENANCY: ANALYSE THE PATTERNS, DESIGN THE SPEC, VALIDATE FOR BREAKAGES

**Received at:** the `1.0.0_SA_CTO~Z` terminal, 2026-08-27 ~18:5xZ
**Recorded by:** `1.0.0_SA_CTO~Z` · **Channel:** direct, in-session
**Law:** `org/XXX.md` — an Andrew-direct is RECORDED VERBATIM and BROADCAST the same turn.

---

## 1. VERBATIM. THE PHRASING IS THE RULING; THIS IS NOT PARAPHRASED.

> *"I think what needs to happen here is that we have to sort out multi-tenant functionality for the
> "Positioning" page. The "Satellites" functionality is something specific to Cottonwood, which means
> it should be available on Cottonwood's page, but nobody else. Of course that does mean that Opal
> needs to be able to see it, so the patterns that govern these things need to be deeply analyzed and
> an implementation spec designed and rigorously validated for potential breakages."*

## 2. WHAT IT RULES (his words, mapped — no additions)

| # | ruling | source phrase |
|---|---|---|
| R1 | **Satellites is COTTONWOOD-SPECIFIC** | *"specific to Cottonwood"* |
| R2 | **Cottonwood sees it; NOBODY ELSE** | *"available on Cottonwood's page, but nobody else"* |
| R3 | **OPAL MUST SEE IT TOO** | *"Opal needs to be able to see it"* |
| R4 | **The governing PATTERNS get DEEP ANALYSIS** | *"the patterns that govern these things need to be deeply analyzed"* |
| R5 | **An IMPLEMENTATION SPEC is DESIGNED** | *"an implementation spec designed"* |
| R6 | **RIGOROUSLY VALIDATED FOR POTENTIAL BREAKAGES** | *"rigorously validated for potential breakages"* |

⛔ **THE SCOPE WORD IS "the Positioning page", NOT "the satellites mode."** He names satellites as the
INSTANCE and asks for **the patterns that govern these things** — plural, general. **Reading this as
"finish the satellites gate" narrows a directive he deliberately widened.**

## 3. WHAT THE FABRIC ALREADY BUILT, AND HOW IT SITS AGAINST R1–R3

`ETFS_SATELLITES.TO-4` shipped `modesFor(firm)` at 18:3xZ (`0.4.0_DE_ClientPlatform~Y`, portal
`797c4f8d`, on `origin/DEV`), TOTAL over `firms ∪ {null}`, `null` failing closed:

```
cottonwood     -> three pills (satellites visible)     satisfies R2
opal-capital   -> three pills (internal)               satisfies R3
every other    -> two pills                            satisfies R2's "nobody else"
null (/auth/me failure) -> two pills, FAILS CLOSED     not asked for; falls out of R2 correctly
```

>> **THE BUILT BEHAVIOUR CONFORMS TO R1–R3.** That is a statement about ONE mode on ONE page and it
   is **NOT** a discharge of R4/R5/R6, which are the substance of this directive. <<

## 4. ⛔ THE QUESTION THIS DIRECTIVE FORCES, AND THE SPEC TURNS ON IT

`SAT-c-3` declared the built gate a **VISIBILITY gate, NOT an authorization boundary**, on the stated
ground that *"the underlying models payload is already served to this viewer; satellites are
arithmetic over it."* The cell explicitly reserved the other reading:

> *"IF IT IS MEANT TO BE AN AUTHORIZATION BOUNDARY, THAT IS A DIFFERENT DESIGN AND A DIFFERENT
> REVIEW."*

**His phrase is "available on Cottonwood's page, but NOBODY ELSE."** ⚠ **"Nobody else" reads
naturally as ACCESS, and the shipped gate is a CLIENT-SIDE VISIBILITY decision** — a non-Cottonwood
viewer cannot reach the mode through the UI or by tampering with the persisted toggle, but the
underlying models payload is served to them regardless, because satellites are arithmetic over data
they already receive.

>> **SO: IS "NOBODY ELSE" A UI-VISIBILITY STATEMENT, OR A DATA-ACCESS BOUNDARY?** The two produce
   materially different specs — the second moves work server-side and makes this a security review,
   not a rendering one. **This is the one question that must be settled before the spec is designed,
   and it is HIS to settle. I am not inferring it.** <<

## 5. DISPOSITION AT THIS SEAT

- **R4/R5/R6 are a CTO act** (analyse → PRD/spec) and this is a **NEW PROJECT under Rule 27**
  (register → purpose-level PRD → COO atom-decomp → execute → CVO), **not an amendment to
  `ETFS_SATELLITES`**, whose round 1 is certified and closed.
- ⛔ **BEARING ON AN OPEN CALL: the ETFS_SATELLITES PROD promote (my `/open-calls` CALL 1) IS NOW
  QUESTIONABLE AS FRAMED.** He is saying multi-tenancy *"needs to be sorted out"*, which is
  inconsistent with promoting the point solution to PROD tonight. **I am NOT treating that as a
  ruling — he did not mention the promote — but I am flagging the tension rather than promoting into
  it.** DEV is unaffected either way.
- **No gate is created by this record.** Findings land as findings.

-- `1.0.0_SA_CTO~Z`
