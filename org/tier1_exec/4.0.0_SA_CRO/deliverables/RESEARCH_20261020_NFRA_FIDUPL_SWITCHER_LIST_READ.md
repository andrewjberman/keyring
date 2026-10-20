# RESEARCH 2026-10-20 -- NFRA_FIDUPL: how to read the G Number Switcher's full list (names only)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8785 (PRD v0.4.6: pulls cover every G number on the
switcher; the per-G secret becomes a check, not the source).
**Sources:** Andrew's HARs 1 and 4 (off git). Field/element names only; no G-number values.

## The authoritative source: the G Number Selection form

- **Open it:** GET `https://wealthcentral.advisorchannel.com/ac/wc/channel/jsp/support/ria_changegnum.jsp` -> 302 ->
  GET `https://www2.advisorchannel.com/wc/channel/jsp/support/ria_changegnum.jsp` -> 200 (server-rendered HTML). Session cookies only.
- **Parse the form** `name="pgChangeGN"`:
  - `select name="gnumClientNm"` holds **one `<option>` per G number the login can switch to**. Each option is
    `<option value="G{8 digits}">G{8 digits} - {FIRM LABEL}</option>`. In Andrew's capture there were **31 options**.
  - The page also renders `Current: {G} - {label}` and `Default: {G} - {label}` cells.
- **This is the same form the switch POSTs to** (`gnumClientNm=<G>&process=change`), so its option list is exactly the set of G numbers
  the session can pull. It is the right "every G number on the switcher" source.

**How the run reads it:** GET the page, extract `select[name=gnumClientNm] > option` -> for each, `value` (the G number) and the option
text (the firm label). Build `{G -> firm label}`. Map each label to a registry firm by substring:
`COTTONWOOD -> cottonwood`, `INFLECTION -> inflection`, `49 FINANCIAL -> 49financial`, `KEIL -> keilfinancial`,
`ABIDING -> abidingwealth`, `LIGHTHOUSE -> lighthousewealth`, `VM WEALTH -> vmwealth`, `ALONGSIDE -> alongside`. A label matching no
registry firm (e.g. the one advisor-name-only G) lands under `alongside` and is named in the run record.

## Secondary source (same list, JSON): the worklist criteria

- `GET /ssc/worklist/wc/channel/worklist/criteria-fields.json` -> section heading "Access Attributes", field `name:"gnumber"`
  ("G Number(s)"), `inputType:"MultiSelectLookUp"`. Its `options[]` carry `value` (the G number) and `title`/`description` (the firm
  label) -- the same 31. Useful if an HTML parse is unwanted; the JSON is cleaner but is a worklist endpoint, not the switch endpoint.

## Recommendation

Read the switcher list from the **`ria_changegnum.jsp` select** (the authoritative switch source), parse value + label per option, map to
firm by the substring table above. The per-G SSM secret (`fidelity/alongside/perg-list`, CTO msg 8674) becomes the **cross-check**: the
run asserts the live list matches, and flags any add/drop, so a firm added or removed on the Wealthscape side surfaces instead of being
silently missed.

## Firm-label -> registry mapping (measured labels, 2026-10-19/20)

| Wealthscape label (substring) | registry firm scope |
|---|---|
| ALONGSIDE, LLC | alongside |
| COTTONWOOD CAPITAL ADVISORS (+ PRIMARY/SECONDARY/SHIPLEY/RUBOTTOM/BASS/ADVISOR PAYS) | cottonwood |
| INFLECTION WEALTH MANAGEMENT | inflection |
| 49 FINANCIAL | 49financial |
| KEIL FINANCIAL PARTNERS (+ advisor names) | keilfinancial |
| ABIDING WEALTH PARTNERS | abidingwealth |
| LIGHTHOUSE WEALTH PARTNERS | lighthousewealth |
| VM WEALTH PARTNERS | vmwealth |
| (an individual advisor name only, no firm) | alongside (unattributed; named in the run record) |

## Not measured

- Whether the switcher list changes between sessions (the cross-check against the secret is what catches that).
