# ANDREW-DIRECT 2026-09-10 ~21:5xZ -- D5 is officially "Asset Management", D4 is officially "Positioning"; then /integrate parity

**archetype:** SCRIBE (record) + register act · **recorded by** `0.0.0_AB_MSTR~Z` · **terminal:** the `0.0.0_AB_MSTR~Z` session on site Z

> **WHY THIS FILE EXISTS.** `org/missions/DIRECTIVES.yaml` is the directive register and its
> `title:` cells are HUMAN fields. A title change is an Andrew word; this is the record the two
> `title_provenance:` cells cite. It carries his words and what the register act did with them.

---

## 1. THE WORDS, VERBATIM AND COMPLETE

One message, typed into this seat's session mid-turn during startup. Bracket measured: after this
seat registered on the broker (~21:52Z) and before this seat's own clock read at 2026-09-10T21:59:22Z.

> **"I need to you to get an /integrate parity done, however before you do it, i want to make sure
> that the D5 Directive is officially named Asset Management, and that the D4 Directive is
> officially named Positioning."**

NOTHING IS PARAPHRASED ABOVE AND NOTHING IS OMITTED. No other words were spoken on this subject at
this terminal in this session.

---

## 2. WHAT THEY SETTLE

| question | settled? | by which words |
|---|---|---|
| D5's official title | **YES** -- "Asset Management" | "the D5 Directive is officially named Asset Management" |
| D4's official title | **YES** -- "Positioning" | "the D4 Directive is officially named Positioning" |
| ordering | **YES** -- the rename lands BEFORE the parity run | "before you do it" |
| the parity run | **YES** -- `/integrate parity`, both legs | "get an /integrate parity done" |

---

## 3. MEASURED STATE BEFORE THE ACT (so the act is falsifiable)

`awk` over `org/missions/DIRECTIVES.yaml` at three refs, same instrument:

| ref | D4 title | D5 title |
|---|---|---|
| local SITEZ `@a4fb3f43ab` | Asset Management | Alternative Research |
| origin/SITEZ `@c0b5636ea9` | Asset Management | Alternative Research |
| origin/CLOUD `@bc38379b25` | Asset Management | Alternative Research |

So the two names were NOT swapped or half-applied anywhere; the act is a fresh rename on both rows,
and it collides with nothing in flight on either fabric.

Corpus census of the two strings (`comp-find`, corpus=all, 54,572 files scanned):
- "Alternative Research": 24 hits. The only AUTHORITATIVE carrier is `DIRECTIVES.yaml` D5.title.
  The rest are generated dashboards (`daily_reports/`), sprint text, ledger LD-0518, inbox copies,
  and AMGT_RESAPP's brief / PRD / decomposition quoting the directive name in prose.
- "Asset Management": 137 hits; the register-plane carriers are `DIRECTIVES.yaml` D4.title,
  `MACROS.yaml` (the AMGT charter, RATIFIED today) and `org/missions/D5/AMGT/AMGT_RESAPP/project.json`.
  Everything else is SmartX/FIND/IMO domain text using the phrase in its ordinary sense.

**Coherence check that made this a one-file act:** D5's macro `AMGT` was ratified TODAY as
"Asset Management -- ALL of D5's research and analysis" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_174xZ_D5_MACRO_AMGT_AND_ITS_SCOPE.md`).
D4's macro `ETFS` charter reads "positioning, ingest, guardrails". The new titles match the macros
already on the rows; the old titles did not.

---

## 4. THE REGISTER ACT

`org/missions/DIRECTIVES.yaml`:
- D4: `title: "Asset Management"` -> `title: "Positioning"`, plus a `title_provenance:` cell.
- D5: `title: "Alternative Research"` -> `title: "Asset Management"`, plus a `title_provenance:` cell.

SCOPE, stated so it can be corrected: TITLE FIELDS ONLY. No `directive:` pointer, `placement:`,
`members:`, `completion_bar:` or `stance:` moved on either row. No PRD file was renamed. No project
artifact was edited.

Consumer check: `.tools/directives-check.py` reads `title` via `r.get("title")` (8 whole-value hits,
all CODE band, none validating its content) and requires only that the key exist; the extra
`title_provenance` key follows the D4 row's existing `completion_bar_provenance` pattern.

Register ownership: `org/missions/.register-owner` names the LAPTOP as the device that COMPILES the
derived register (`comp-missions emit/compile`). `DIRECTIVES.yaml` is hand-written by MSTR, and this
seat made two register acts on this file today already on Andrew-direct at this terminal (the D5
placement move @15ef14c2ed; the MACROS.yaml ratification @1d9e731ba5). Same footing here.

---

## 5. SURFACED, NOT DONE (each is another seat's)

- **`1.0.0_SA_CTO~Z` (L4):** D5's `directive:` pointer still names `docs/architecture/D5_ALT_RESEARCH_PRD.md`,
  whose header reads "Alt Research Pipeline". Under the ratified AMGT charter that PRD describes a
  SUBSET of the directive. Whether the directive PRD is re-cut, re-pointed, or left as the corpus PRD
  is the CTO's call. Nothing is blocked on it.
- **`2.0.0_SA_COO~ZZZ` / `4.0.0_SA_CRO~Z`:** AMGT_RESAPP's brief, PRD and decomposition say
  "Alternative Research" in prose where they name D5. Those predate this commit; reading rule is in
  the `title_provenance` cells. No edit requested.
- **`0.0.0_AB_MSTR` (laptop, register owner by hostname):** this lands on origin/SITEZ with the parity
  run and reaches the laptop register on its leg. Nothing to re-do there.

---

## 6. RELAYED, NOT ADJUDICATED

Same-turn broadcast to the live site-Z seats and a bus frame to the laptop. The commit fixes the
record; only the broadcast fixes the fabric. Push state is stated in the broadcast, measured by
`git ls-remote`, never defaulted.
