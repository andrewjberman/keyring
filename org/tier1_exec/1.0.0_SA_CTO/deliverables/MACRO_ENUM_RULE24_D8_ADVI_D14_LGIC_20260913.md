# MACRO ENUM PROPOSAL (Rule 24) -- D8 += [ADVI] and D14 = [LGIC]

**Author:** `1.0.0_SA_CTO` (MACROS.yaml is the CTO's to write at L3 -- Rule 27, Andrew-direct 2026-09-10). **Status:
PROPOSED.** Ratification is Andrew's alone (MACROS.yaml header). **MACROS.yaml is NOT edited by this record** --
flipping D8's `ratification` line to PROPOSED would make `missions-tree-index.py` refuse every D8 registration,
MDPF_CANON included, so both edits land together on his word.

**Credit:** the recommendations are `4.0.0_SA_CRO~D`'s (msg 96403, 2026-09-13T20:29:54Z), made on Andrew's ~19:1xZ word
to that seat -- *"collaborate with CTO to get this done, you give your recs"* -- and his ~19:2xZ priority word,
*"I want to proceed with the Logic projects into the MDPF and so on"* (relayed 96400). **Every measurement below is
this seat's, at this seat's vintage (2026-09-13 ~20:3xZ-20:5xZ)**, re-run rather than inherited -- a record carries
its author's measurement (the D4 precedent). Where this seat's number differs from the recommending seat's, the
difference is stated.

**Grammar, read from `org/standards/PROJECT_TREE.contract.json` at HEAD, never from prose:** `levels[1]` macro
`^[A-Z]{4}$`; `levels[2]` project `^[A-Z]{4}_[A-Z0-9]{3,18}$`.

---

## PROPOSAL 1 -- D14 "Platform Logic": macros [LGIC]

**Charter:** "Platform Logic -- the canon (rules, ledger, identity spine), the naming schema, and the executable
layer (registry, builders, flagger); owns the RULE and the FLAG, never a remediation (D14)".

**Projects it admits, codes conforming:** `LGIC_CANON` (tail 5), `LGIC_NAMING` (tail 6), `LGIC_ENFORCE` (tail 7) --
the three D14 briefs with L2 cut and DONE WHEN confirmed ~18:4xZ: `ENDPOINT_FWD_D14_PIPELINE_CANON_20260912.md`,
`ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md`, `ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md`.

**Token census, word-boundary, UNSCOPED:** `comp-find '\bLGIC\b'` -> **7 hits across 170,238 files [corpus=all]**
(104,670 ephemeral-floor, 4,495 binary and 12 unreadable files DISCLOSED as not covered). Bands SURFACED 3, DOC 4.
**All 7 are this proposal's own traffic:** three tool-log lines of `4.0.0_SA_CRO~D`'s census run and four lines of its
message to this seat. **Zero prior use; no collision.** ⚠ The recommending seat reported "3 hits, all substrings inside
NEURALGIC / NOSTALGIC" -- that was a SUBSTRING search; at word boundary those do not match. Same conclusion, different
instrument, stated.

**(i) MECE by subtraction.** Denominator = D14's population: `DIRECTIVES.yaml` D14 `members.projects` = **0**; flat
rows with `directive: D14` = **0 of 362 parsed (0 parse errors)**. The entering population is the three briefs above --
3 of 3 fit LGIC. Nothing else enters D14 by construction: Andrew's ~03:5xZ ruling (a) puts every remediation "where the
resource lives" (D8, D12), and D14 owns only the rule, the registry, the builders and the flagger. **Uncovered: none.**
**(ii) Same grain.** One product family, three briefs; the executable layer CONSUMES the naming schema, which is an arc
inside one family, not a family boundary.
**(iii) Intent coherence.** One axis: the platform's own law and its mechanical enforcement.
**(iv) State coherence -- what ratifying does NOT move:** it moves D14 only. It registers nothing (each project's L3 is
a separate act, this seat's), mints no folder, writes no PRD, grants no seat, and changes no other directive's list.

**Alternatives named:** three macros (e.g. CANN / NAME / ENFC) -- REJECTED: each brief becomes a family of one forever,
a bare partition, not a taxonomy. `CANON` -- not a legal macro (five letters) and it already collides with three
registered project tails (Andrew's own 09-12 finding). `LOGC`, `PLGC` -- measured clean by the recommending seat, not
re-run here; LGIC is preferred because it reads as the directive's own word.

---

## PROPOSAL 2 -- D8 "Data Pipelines": macros [ETFS, MDPF, AUTH] -> [ETFS, MDPF, AUTH, ADVI]

**Charter:** "Advisor Intelligence -- the per-firm serving stacks (firm, advisors, clients, accounts) and the firm
buckets that hold them (D2, D8)".

**Project it admits:** `ADVI_FIRMBKTS` (tail 8, conforms) -- the D8 legacy-firm-buckets migration
(`ENDPOINT_FWD_D8_LEGACY_FIRM_BUCKETS_MIGRATION_20260913.md`, DONE WHEN confirmed ~18:4xZ). `ADVI_LEGACYBKTS` also
conforms; FIRMBKTS is preferred because the project outlives the legacy buckets it retires.

**Token census, word-boundary, UNSCOPED:** `comp-find '\bADVI\b'` -> **10,339 hits across 170,238 files [corpus=all]**,
bands DEF 5, SURFACED 4,565, CONFIG 648, TEST 3, DOC 5,118. (The recommending seat's 8,091 was scoped to `org/` +
`docs/`; this is the unscoped read Rule 24 requires before a domain choice.) **Referent, read on all 5 DEF hits:** two
are the advisor-intelligence product itself (`/api/scoped/advisor-intelligence/` in the edge router's test;
`ADVI/NNA`, the inf pipeline's metric namespace, in its Lambda and its Terraform); two name a Schwab account "the ADVI
account's OWN silver" -- a narrower use inside the same product line. **Project rows:** 101 codes begin `ADVI_`, **all
101 carry `macro_code: ADVI`**; 9 sit under D2, 92 under no directive; 11 non-terminal. Among them is
`ADVI_FIRMSEP` (firm separation of these same buckets). **So prior use is the SAME REFERENT and is SUPPORT, not
collision** -- the POSN precedent in D4's record. ADVI is in no directive's ratified list today (D2 has no MACROS.yaml
entry), so this is its first ratification.

**(i) MECE by subtraction.** Denominator = `DIRECTIVES.yaml` D8 `members.projects` = **6**: MDPF_COTREMEDIATION,
MDPF_HEALGAP, AUTH_SELFHEAL, ETFS_GUARDRAIL, GLOBALALARM, MDPF_CANON. [ETFS, MDPF, AUTH] covers 5 of 6; GLOBALALARM is
the recorded pre-macro row (MACROS.yaml D8 census, unchanged by this). The entrant fits NONE of the three
(`missions-tree-index.py:248-254` refuses it today; this seat's d2ceedadbb finding) and fits ADVI. With ADVI: 5 of 6
members plus the entrant; GLOBALALARM stays the one recorded exception. **Uncovered: none new.**
**(ii) Same grain.** ADVI names a product family, as ETFS, MDPF and AUTH do.
**(iii) Intent coherence -- THE ONE JUDGMENT IN THIS PROPOSAL, stated rather than buried:** the migration does NOT move
advisor-intelligence data only. Its own boundary (`docs/briefs/d8-legacy-firm-buckets-migration-brief-20260913.md`
Part II) cuts over gold, platinum, state and code for three firms, and moves their bronze and silver out to
`opal-data-assets`. **ADVI is chosen because the advi serving stacks are what these buckets predominantly are** -- the
recommending seat measured 24,631 + 8,673 + 1,136 platinum objects against 13 MDPF slices (cited as that seat's, not
re-derived) -- and because the MDPF and IRPT slices in the same buckets are moved by MDPF_CANON and IRPT_BCKEND, not by
this project. If Andrew reads the project as cross-cutting firm infrastructure rather than product work, the honest
alternative is a new macro, below.
**(iv) State coherence -- what ratifying does NOT move:** it moves D8's list only. ETFS, MDPF and AUTH are unchanged; no
existing D8 row changes macro; ADVI's 101 flat rows under D2 or no directive are untouched (MACROS.yaml scope is
PROSPECTIVE ONLY); ratifying it for D8 ratifies nothing for D2.

**Alternatives named:** `FIRM` (0 prior use) -- REJECTED by the recommending seat and by this one: it names the
project's SHAPE (a bucket migration), not a family, and a second firm-bucket migration would have nowhere else to go.
`MDPF` -- REJECTED: it names the smaller share of these buckets and would put an advisor-data migration under the
model-portfolio family. **Kept open for Andrew: a cross-cutting infrastructure reading** -- if he does not want
firm-bucket work under a product macro, the enum needs a new infra-shaped macro and its own census; this record does
not mint one.

---

## ON RATIFICATION (his word), THIS SEAT'S L3 ACTS, IN ONE COMMIT EACH

1. `MACROS.yaml`: add `D14: macros [LGIC]` with its ratification string and census; append ADVI to D8's list and
   re-write D8's ratification string to cite this record beside the 09-03 one; add both charters.
2. Register `LGIC_CANON`, `LGIC_NAMING`, `LGIC_ENFORCE` under D14 and `ADVI_FIRMBKTS` under D8 -- tree row, generated
   index, `DIRECTIVES.yaml` members line -- one commit per project, `missions-tree-index.py --self-test` first.
3. Then L4 per project, starting where Andrew's priority word points: the Logic projects into MDPF.
