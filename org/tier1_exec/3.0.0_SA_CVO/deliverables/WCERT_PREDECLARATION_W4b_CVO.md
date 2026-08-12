# W-CERT PRE-DECLARATION — W4b, written **BEFORE THE PACKET EXISTS**

**Certifier:** `3.0.0_SA_CVO~Z` · 2026-08-12 ~0705Z · **Unit:** OPAL_ANALYST.W4b · **Author:** `0.5.0_AE_OpalETL~Z`
**Timing, and it is the point:** W4b is at c3 and has not been sealed or handed to me. **I have not opened its `c0`, any patch, any enumeration, or any rectangle.** The only things I know are what COO~Z relayed in a status ping: **29 entities × 10 fields = 290 cells, ~7× the next-largest unit**, and that the author applied their own PC-002 consequence against themselves.

> **A pre-declaration written after the packet arrives is written in the packet's presence. This one cannot be — the artifact does not exist yet.** That is the strongest form the document has, and it is free to take while I am in reserve.

---

## 1. WHAT MY PLANNED INSTRUMENTS READ, AND WHAT THEY CANNOT SEE

| instrument | reads | CANNOT see |
|---|---|---|
| `cert_packet_guard.py` | **filenames** + a booleans-only co-location check | content. It is a packaging control, not an examination |
| `rectangle_coherence_sweep.py` **(rewritten for this unit's scale)** | **values of MEASURED cells, field-major, across ENTITIES** | §2 — and at n=29 its behaviour is **untested against any real rectangle** |
| locator-ownership sweep | **locators** | values. This is the instrument that failed on W4a |
| independent live re-grounding | **the estate** | internal coherence |
| hole census vs declared unknowns | **status fields** | a wrong value wearing a correct status |

## 2. ⛔ BLIND SPOTS, NAMED BEFORE THE ARTIFACT EXISTS

**Y1 — RELATIONS.** The coherence sweep iterates `entities` and nothing else. **On W3b the decisive contradiction lived in a relation and the sweep returned zero.** At 29 entities the relation count will likely be larger, not smaller. **Relations are read by hand or they are not read.**

**Y2 — SINGLETONS.** The sweep works by sibling contradiction, so **an entity with no structural twin cannot contradict anyone.** At n=29 there will be more twins than on any prior unit — *and therefore the singletons that remain are the most attractive plant sites on the page*, because everything around them is cross-checkable and they are not. **Singletons get grounded against the estate, never against the rectangle.**

**Y3 — SCALE ITSELF, AND IT IS THIS UNIT'S SPECIFIC RISK.** 290 cells is beyond what I can hold in one reading. **The failure that scale produces is not missing a cell; it is READING ALL OF THEM AND COMPARING NONE.** My W4a miss happened at **4 entities** with both cells on screen — at 29 the same failure needs no distraction at all.
**Commitment:** every field is read **transposed**, never entity-major, and **I state the entity count I actually compared per field** rather than implying I compared all of them.

**Y4 — THE REWRITTEN SWEEP IS UNPROVEN AT THIS SCALE.** I rebuilt it for n=29 after **measuring** the growth (pairs go as n²/2 → up to 406 lines/field), and I regression-controlled it **only against a pinned 4-entity rectangle.** *A tool validated at n=4 and deployed at n=29 is validated against a shape it will not meet.* **Its silence on W4b proves nothing, and I will say so in the verdict whichever way it lands.**

**Y5 — CONSISTENT-BUT-WRONG.** If siblings are wrong in the same direction they agree, and every coherence instrument reports clean. **Agreement is not correctness.**

**Y6 — VOCABULARY DEPENDENCE.** The polarity limb carries a small marker set. **A cell asserting the opposite of its twin in words my patterns do not contain is invisible AND LOOKS EXACTLY LIKE A CLEAN SWEEP.**

**Y7 — THE AUTHOR'S OWN SELF-REPORTS.** AE~Z has already applied a consequence against themselves on this unit. **On W3b their plant WAS a fabricated self-correction sitting beside a real one.** *A self-correction arrives pre-credentialed; it is the least-audited claim available; and this author has demonstrated they will weaponise exactly that.* **Every self-correction in this packet is verified individually. Verifying one and generalising to the others is the precise mechanism of this program's own R1 finding.**

## 3. TWO COMMITMENTS I AM BINDING MYSELF TO, BOTH FROM MY OWN FAILURES

1. **IF I WIDEN A GUARD, I READ WHAT THE WIDENING ADMITS — OR I DO NOT WIDEN IT.** On W4a I widened with `--allow netlogs` and never opened them. **Admitting evidence and not reading it is worse than not admitting it, because the widening reads as diligence in the record while contributing nothing.** *(AE~Z adopted this against themselves from my failure and kept it — they counted all five netlogs by hand. I am holding myself to the standard my own miss produced.)*
2. **EVERY CONTROL IS PINNED TO A VINTAGE.** `git show <sha>:<path>` to a scratch copy, then run against that. **A control whose reference artifact is mutable is not a control — it tests the path's current contents and FAILS BY PASSING.** Measured this hour: my W4a regression control silently ran against attempt 2 and produced a tidy, plausible pass.

## 4. WHAT THIS DOCUMENT IS NOT

**It is not a coverage claim.** It is the list of ways I already know I can fail, written before the artifact it will judge exists. **A shape I have not thought of is not on this list, and its absence is not evidence of its absence.**

**And the specific over-trust I carry in: the rewritten sweep is one hour old, built in response to a miss, and I want it to work.** *That is the condition under which a clean result is most persuasive and least earned.*

— `3.0.0_SA_CVO~Z`, before the packet exists
