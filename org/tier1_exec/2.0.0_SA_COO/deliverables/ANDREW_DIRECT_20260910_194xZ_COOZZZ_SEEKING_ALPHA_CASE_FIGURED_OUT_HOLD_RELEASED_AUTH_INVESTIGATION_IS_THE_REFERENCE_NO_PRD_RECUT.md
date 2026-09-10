# ANDREW-DIRECT 2026-09-10 ~19:4xZ -- the Seeking Alpha case is figured out; the hold is released; the CRO's auth investigation is THE REFERENCE for SA-procurement task orders; no PRD recut

**archetype:** SCRIBE (record) - **recorded by** `2.0.0_SA_COO~ZZZ` - **terminal:** the `2.0.0_SA_COO~ZZZ` terminal (the lane Andrew spawned for `AMGT_RESAPP`)
**channel:** three messages typed into this session mid-turn, in order, the third of this hour's sequence after @ee0eacab07 (the SA word) and @8c609decf7 (the hold). Bracketed by this lane's own acts: after its request to `0.0.3_BG_BBGTerminal` at `2026-09-10T19:42:27Z`, before the clock read taken beside this file, `2026-09-10T19:54:09Z`.

> **WHY THIS FILE EXISTS.** `org/XXX.md`: *"ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN. DURABLE: a commit quoting him VERBATIM. NEVER A PARAPHRASE. THE PHRASING IS THE RULING. SCOPE: The receiving agent does NOT adjudicate scope. SURFACE, DO NOT ADJUDICATE."* This is that commit. Section 1 is his words and nothing else.

---

## 1. THE WORDS, VERBATIM AND COMPLETE -- three messages, in order

> **"We have figured out the Seeking Alpha case"**

> **"I think you can just review the brief here: org\tier1_exec\4.0.0_SA_CRO\deliver…\AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md"**

> **"Shouldnt need to recut the details on the PRD, it is right here, this is just what should be referenced for any TOs associated with SA news procural for this project."**

NOTHING IS PARAPHRASED ABOVE AND NOTHING IS OMITTED. The second message carries the path as it arrived, with the elision character in the middle segment; it resolves, uniquely, to
`org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md`
(10,773 bytes, committed @b1656bbebc by `4.0.0_SA_CRO~Z`; the only file under that folder matching the stated head and tail).

---

## 2. WHAT THE WORDS BIND -- SURFACED, NOT ADJUDICATED

| his words | what they bind | where it lands |
|---|---|---|
| "We have figured out the Seeking Alpha case" | the open question his hold @8c609decf7 was waiting on is CLOSED | the hold's release condition -- *"i may provide updated information to this end"* -- is met. The held cell `AMGT-s-b4` moves `HELD -> OPEN`; nothing else moves (decomposition s.2 (iv)). |
| "review the brief here: ... AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md" | the updated information IS that document | this lane reads it in full before writing the SA cell's worker face; the face cites it by path and hash. |
| "Shouldnt need to recut the details on the PRD" | no L4 recut is asked of anyone by this word | this lane recuts nothing at L4 (not its limb) and cites the PRD at whatever version L4 has landed. |
| "this is just what should be referenced for any TOs associated with SA news procural for this project" | the document is THE REFERENCE for every task order whose subject is SA news procurement | every such order carries it in its worker face and in its `<paths>` as a read; the SA cell's criteria are cut against it. |

**READ AS "ANY TOs associated with SA news procural":** at this cut that is `AMGT-s-b4` (the SA backend) and, to the extent it consumes SA content, `AMGT-s-4` (the coverage reader) and `AMGT-s-9` (the drafting face). The identity layer `AMGT-s-12` resolves the SA symbol as a key and is not a procurement order. **If he meant a wider or narrower set, that is one word.**

---

## 3. WHAT THIS RECORD DOES NOT DO

- It does not summarise the referenced document. The document is the reference; a summary here would be a second carrier that drifts.
- It does not recut the PRD, and does not read "shouldn't need to" as a prohibition on L4 -- that limb is `1.0.0_SA_CTO`'s and its own message on a v0.3 is read on its own terms.
- It does not touch the vendor-egress ruling (`C-SA-VENDOR-WORD`, PRD s.3a) except as the referenced document itself bears on it.

**Broadcast:** MCP to `1.0.0_SA_CTO~Z` and `0.0.0_AB_MSTR~Z` in the same turn as this commit.
**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` holds all pushes.
