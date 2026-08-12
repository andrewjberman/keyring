# ANDREW-DIRECT 2026-08-12 — two rulings off `/open-calls` at the CRO~Z terminal

**Channel:** direct, at the `4.0.0_SA_CRO~Z` terminal (site Z).
**Time:** ~1948Z, in response to `/open-calls` run at this seat ~1947Z.
**Recorded by:** `4.0.0_SA_CRO~Z`. Broadcast to MSTR~Z + CTO~Z + COO~Z same turn, per `org/XXX.md`.

## VERBATIM

> **"Call 1 A, Call 2 B"**

**The phrasing is terse and is NOT ambiguous, because the cards it answers were two-option by
construction.** Recording the cards alongside it so the ruling stays interpretable without this
session's context — *a terse ruling detached from the question it answered is not a record.*

---

## RULING 1 — Part 3 is GO (`A`)

**The call as put:** *"Start Part 3 now — the document-extract research project? (a) go (b) hold"*
**Answer: (a) GO.**

**My recommendation, which the `A` adopts:** *"go, and scope it to a SPEC before any build."*
⚠ **THE SPEC-BEFORE-BUILD HALF RIDES WITH THE GO** — it was inside the option he selected, not
alongside it. Part 3 produces a **specification**, not an implementation, until he says otherwise.

**Originating directive (same terminal, earlier 2026-08-12), VERBATIM:**

> *"figure out what document/pdf extract tools need to be built in here and a strategy for how this
> should work in the cloud. I think probably the best way to approach this is to figure out on the
> public ms sharepoint cloud how to develop a system that parses all documents to text across
> filetypes and figure out how to organize that data by file provenance (what file ref),
> modification date, maybe some other vectors you can think of, and then a registry setup for how
> agents can effectively scan that registry, this whole thing should also live on the aws graph
> somewhere so this is a big research project."*

**The measured gap it addresses** (W7, exercised 2026-08-12): `read_document` returns a **rendition
and no text**, so `.docx` / `.pdf` / `.pptx` are reachable and unreadable. `.xlsx` reads fully.

**CONSEQUENCE FOR PART 2, and this is his to close rather than mine to assume:** my card stated that
Part 2 (*"properly hooked up to read sharepoint documents"*) **is not satisfied today** on the
document classes. He selected GO on the project that closes that gap. **He did NOT say Part 2 is
rejected, and I am not recording that he did** — the ruling authorises Part 3; it does not
adjudicate Part 2's acceptance. If that matters downstream, it is a separate question at him.

## RULING 2 — the Terminal credential is ACCEPTED as-is (`B`)

**The call as put:** *"Rotate the Bloomberg Terminal credential, or accept it as-is? (a) rotate
(b) accept"*
**Answer: (b) ACCEPT.**

**Effect:** `0.0.3_BG_BBGTerminal`'s 2026-08-11 rotation recommendation is **DISCHARGED by sovereign
decision** — not by anyone concluding the risk went away. The credential stays as-is across its
existing copies; `bloomberg/terminal/login` remains the authoritative programmatic home.

⛔ **SCOPE, stated so nobody widens it:** this closes **the rotation question for THIS credential**.
It is **not** a general ruling on credential handling, not a licence to place other secrets in chat
surfaces, and **not** a reversal of the runbook's CREDENTIAL HANDLING section as guidance for future
credentials. **His word binds the addressed question, verbatim scope, nothing wider**
(`org/XXX.md` — surface, do not adjudicate).

---

## Acts taken on this record

1. Both rulings recorded here verbatim and committed (this file).
2. Broadcast to `0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z` — same turn.
3. `0.0.3_BG_BBGTerminal` notified that its rotation rec is discharged by ruling 2, with the scope
   bound above.
4. Part 3 opened as a **specification** effort.
