# MACRO ENUM for D0 / D8 / D11 -- the Rule 24 four-postulate record + word-boundary token census

**Author:** `2.0.0_SA_COO`, 2026-09-02 ~21:3xZ. **Prerequisite 1 of the project tree** (spec s.8
@31463f1286; calls 1-4 RULED @5f8b774a5d; START ruled @a8d63f097c). **Carrier (DATA):**
`org/missions/MACROS.yaml` -- read by `.tools/missions-tree-index.py` refusal R2.
**Ratifies:** Andrew, per directive (spec s.5a "who ratifies"). This record is the PROPOSAL; nothing
here is ratified until his word flips `ratification:` on the carrier, quoting this file.

## 1. The proposal

| directive | macros (the enum) | evidence (rows with that `directive`, 352-row register @d413196285) |
|---|---|---|
| D0 | `NFRA` | 5 of 5 rows: prefix NFRA, `macro_code` NFRA |
| D8 | `ETFS`, `MDPF`, `AUTH` | 4 of 4 rows: MDPF x2, ETFS x1, AUTH x1; `macro_code` == prefix on every row |
| D11 | `NFRA` | 2 of 2 rows: NFRA; `NFRA_COMPEFFICACY` (no row yet; Andrew ~21:0xZ "laptop under D11") conforms |

A macro repeats across directives by design (`NFRA` under D0 and D11); each directive's list is its
own enum and is ratified on its own.

## 2. The declared domain (postulate i needs one before MECE means anything)

**Domain:** *the macro a NEW project may register under, per directive, INTO the tree.* Nothing else.
The 352 flat rows are outside the domain (spec s.8: prospective only, no migration); a directive not
in {D0, D8, D11} has no enum yet and therefore no tree entry can be made under it (that is a refusal,
not a gap: the tool reads `MACROS.yaml` and R2 fires on an absent directive too).

## 3. The four postulates

**(i) MECE over the declared domain.** Members = the macro prefixes of the directive's CURRENT
members (table above) -- every live member is covered (exhaustive by census), and no code has two
prefixes (exclusive by grammar: `^[A-Z]{4}_[A-Z0-9]{4,12}$`, one underscore). **The uncovered-member
hunt:** a future project whose prefix is not in the list is REFUSED at registration (R2), so an
uncovered member cannot exist silently; it can only exist as a proposal to extend the enum, which
is this record's shape again. D8's list is the one where the hunt found something: the spec's
first draft wrote "NFRA and ETFS, two macros" from the water-test minimum; the census shows D8's
live members carry THREE prefixes, and an enum that refuses `MDPF_*` on day one under the
directive whose title is *Model Portfolios Pipeline Fortification* is a bare prohibition, not a
taxonomy. Hence three.

**(ii) Same grain.** Every value is a four-letter NAMESPACE (s.5a: a macro can only be ABANDONED,
never DONE). No value is a project, a directive, a fabric or a status. The grammar enforces the
grain mechanically (`^[A-Z]{4}$` on the folder name; a five-letter or lower-case folder is R1).

**(iii) Intent coherence.** One axis: *which product/system line does this project belong to.*
The one-line charters on the carrier say what each namespace is FOR; none encodes where work runs
(that is `fabric`, Andrew's field) or what it is for (that is the directive, in the path).

**(iv) State coherence -- which values one remedy does NOT move.** Ratifying D8's list does not
ratify D0's or D11's; adding a macro to D8 moves nothing under D0; retiring a macro (abandoning a
line) is a separate act per directive. `NFRA` appearing twice is two entries with two ratifications,
and the carrier holds them as two keys so a single edit cannot move both. The flat register's
`macro_code` field is NOT moved by anything here (352 rows untouched).

## 4. Word-boundary token census (denominators printed; read 2026-09-02 ~21:2xZ)

Instrument: python over `org/projects/*.json` (whole-value `macro_code` and the code prefix before
the first `_`, two different carriers, both counted) and a `\b`-bounded regex over
`org/missions/DIRECTIVES.yaml`. **Denominator: 352 rows, 0 parse errors, HEAD @d413196285.**

| macro | `macro_code` whole-value | prefix | both agree | active rows | by directive |
|---|---|---|---|---|---|
| NFRA | 87 | 85 | 83 | 9 | D0 5, D11 2, none 78 |
| ETFS | 9 | 9 | 9 | 1 | D8 1, D4 4, none 4 |
| MDPF | 23 | 20 | 20 | 3 | D8 2, none 18 |
| AUTH | 3 | 3 | 3 | 1 | D8 1, none 2 |

`DIRECTIVES.yaml` as code prefixes (`\bNFRA_`): NFRA 8, ETFS 27, MDPF 8, AUTH 3; as bare words
(`\bNFRA\b`): 0, 2, 1, 0 -- the register speaks in project codes, not macro names, which is why the
enum has to be a carrier of its own and cannot be scraped from prose.

**The convention, measured on the prefix carrier:** 31 of 44 distinct prefixes are exactly four
uppercase letters, and those 31 cover **334 of 352 rows**; 308 of 352 codes conform to the full
grammar. (The spec's "31 of 38" counted distinct `macro_code` VALUES; this census counts distinct
CODE PREFIXES -- a different instrument, both reported, neither corrected into the other.) The 13
non-conforming prefixes (18 rows) are all flat, all pre-existing, all untouched: `ASSETCLASS`,
`GLOBALALARM`, `PLATFORM`, `PORTAL`, `BD`, `D1`, `D3`, `D12`, `EXPAND`, `HEATMAP`, `COT`, `WSE`, and
**2 rows whose `project_code` begins `projects\MDPF`** -- a path fragment leaked into the code field.
That last one is a register-hygiene SURPRISE (OBSERVATION class), surfaced to `3.0.0_SA_CVO` in the
session log, not chased here; it is why R1 tests the ROW's `project_code` and not only the folder.

## 5. What makes the enum BIND (the consuming half)

`.tools/missions-tree-index.py check` refuses (R2) any tree project whose macro is absent from its
directive's list OR whose directive's `ratification` does not begin `RATIFIED`. Exercised:
`--self-test` 18/18 PASS, including the mutant "enum PROPOSED, not RATIFIED -> [R2, R5]" and
"macro not in enum -> [R2, R5]"; against the live estate (empty tree) `check` reads 0 violations
over 352 flat rows / 38 register entries -- the s.8 red-first baseline, measured, not assumed.
**Until Andrew ratifies, the tree accepts NOTHING.** That is the sovereign residual the finished
prerequisite set carries to him, and it is the only item in the set that is his.

## 6. Alternatives named and rejected

- **D8 = `ETFS` only** (the water-test minimum). Rejected above (postulate i).
- **Carry the enum as `macros:` keys inside `DIRECTIVES.yaml`** (the spec's first wording). Rejected:
  that file is `TIER0_DIRECTIVES_REGISTER` (MSTR + CTO) with a `comp-directives check` FORM tripwire
  ("members are references only"); a sibling DATA file beside it keeps the tripwire intact and
  gives the enum its own lane. The spec's intent (per-directive, ratified, data) is kept.
- **Derive the enum from the flat rows at run time.** Rejected: an enum that recomputes itself from
  the population it governs cannot refuse anything (every prefix that exists is, by construction,
  allowed).

## 7. Ratification mechanics (so the flip is a record, not an edit)

On Andrew's word, per directive: `ratification: "RATIFIED <this file> <date> -- verbatim: '...'"`.
The word itself is recorded verbatim in an ANDREW_DIRECT record and cited on the carrier. Adding a
macro later = a new section in a record of this shape + the census + his word; never a bare edit.
