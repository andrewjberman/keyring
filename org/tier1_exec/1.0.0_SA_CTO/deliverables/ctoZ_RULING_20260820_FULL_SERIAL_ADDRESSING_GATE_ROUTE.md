# RULING — FULL-SERIAL ADDRESSING: compliance now, gate candidate ROUTED (not implemented)

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~20:47Z
**Sovereign source:** Andrew-direct ~2036Z at the `0.4.0_DT_ClientPlatform~Z` terminal, recorded verbatim by that seat @`9e1e94c4f4` (msg 2831). I received it as a relay; the durable verbatim record is theirs and is not duplicated here.

> *"It's almost certainly 0.5.0_AE_OpalETL~Z, but you are correct agents should be referring to other agents wth full serial"*

`0.4.0_DT_ClientPlatform~Z` is right that this lands hardest on my pen: the TAC-2' and W-A..W-D routings are
mine and they carry the bare form throughout (`"AE~Z: ..."`, `"DT~Z: ..."`, `"BG: ..."`).

---

## 1. COMPLIANCE — done this turn, with its own control

All three of my live deliverables were converted to full serials before commit:

```
residual bare forms (AE~Z|CVO~Z|COO~Z|DT~Z|MSTR~Z|CTO~Z|BG) : 0
double-prefix corruption (_0.5.0_ | SA_1.0.0 | 0.0.0_AB_0.0.0) : 0
positive control (full serials present)                        : 6+ per file
```

*Word-boundary note for anyone repeating this: `\bCOO~Z` does **not** match inside `2.0.0_SA_COO~Z` —
`_` is a word character, so there is no boundary before `C`. That property is what makes the conversion
safe to run twice, and I ran the guard rather than assuming it.*

## 2. WHY THE BARE FORM IS WORSE THAN IT LOOKS — upholding `0.4.0_DT_ClientPlatform~Z`'s analysis

**It fails silently and plausibly.** `send_message` to a wrong-but-real serial returns **DELIVERED** — a
clean, well-formed success receipt for a message the intended reader never sees. Nothing errors; the
sender's own instrument confirms delivery. **The wrong question asked cleanly.**

**And it DEGRADES rather than staying constant.** `"AE~Z"` resolved unambiguously right up until a second AE
seat existed — **with no signal to anyone that the meaning of an existing habit had just changed.** Two
seats mis-addressed in one window, in opposite directions, off the same shorthand. That is a class.

## 3. THE GATE CANDIDATE — **ROUTED TO ANDREW, NOT IMPLEMENTED**

I implement no gate without his explicit word (CLAUDE.md NEVER-rule, 2026-08-06). **Nothing is gated,
nothing is held, and no work waits on this.** Routed as a candidate:

**PROPOSED:** a **send-time lint on `send_message` recipients** — a `to_agent`/`to_agents` value that is not
a full registered serial is **refused, naming the candidate matches**, rather than delivered to a guess.
**The broker already holds the registry that makes this decidable** — no new source of truth, and it fails
loud at the moment of the mistake rather than silently after it.

**MY ADDITION, and it is the condition I would put on building it:** `0.4.0_DT_ClientPlatform~Z` stated the
limitation honestly and it is the load-bearing half — the **routing-prose** case (`"AE~Z: your runner is the
W-B substrate"` inside a message *body*) is **not reachable** by a recipient-field lint, and a body-text
matcher fires on every legitimate mention (the LD-0274 class this estate has already been bitten by). Their
own words: *"a gate that closes the addressable half while READING as if it closed both is worse than no
gate."*

> **RULED: if it is built, the lint must NAME ITS OWN SCOPE IN ITS REFUSAL TEXT** — "recipient fields only;
> routing prose is not checked." Otherwise a passing lint becomes evidence for a claim it never evaluated,
> which is the instrument-that-could-not-have-said-otherwise defect installed *as a control*.

## 4. INTERIM — no gate required

Full serials in every recipient field **and in routing prose**, effective now, at this seat. It costs
nothing at authoring time and is unfixable cheaply later.

`2.0.0_SA_COO~Z` is writing the W-A..W-D cut now — full serials in `<issued_to>` **and** in the prose.
`0.7.0_AE_CloudOps~Z` received a misrouted step-1 report (msg 2795) that was never theirs; recorded here too
so it does not read as work they dropped.
