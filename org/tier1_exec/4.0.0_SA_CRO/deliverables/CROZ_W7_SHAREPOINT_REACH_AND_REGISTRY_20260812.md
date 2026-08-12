# W7 — SharePoint reach + registry

**Author:** `4.0.0_SA_CRO~Z` · started 2026-08-12 ~1825Z · site Z
**Authorization:** Andrew-direct ~1702Z @`f09cbd13ef` Part 2; routed to this seat by `1.0.0_SA_CTO~Z`
182248Z (within-program reassignment from a saturated `0.5.0_AE_OpalETL~Z`).
**Scope:** READ-ONLY. No writes, no uploads, no site mutations. `upload_text_to_site` and
`save_email_attachment_to_site` are out of scope for this wave.

> **METHOD:** rung 2 first — the reach already partly exists, so **verify and register what is there
> rather than build a client.** Every registered capability is backed by an **EXERCISED** call, not a
> config read. Every count states what it is out of and what the instrument is blind to. The
> call-shape rule carries across from W8: *a `search_site_files` iterated wide enough is an
> enumeration; a `read_document` loop across a library is a harvest.*

---

## 1. IDENTITY — the reach is a PERSON'S, and that governs everything below

`whoami` (EXERCISED) -> **`Andrew Berman`, `Andrew@opalinvest.com`.**

The gateway is OAuth'd as **a named human**, not a service principal.

⛔ **THE CONSEQUENCE, AND IT IS THE MOST IMPORTANT LINE IN THIS REGISTRY: every "not found" from
these tools is indistinguishable from "exists but Andrew cannot see it."** There is no permission
error to catch — an inaccessible site simply does not appear in the result set, cleanly. **So no
absence claim in this registry is a claim about the TENANT; it is a claim about Andrew's view of
the tenant**, and it is labelled that way throughout.

Second consequence: **every call attributes to Andrew.** Anything scheduled or production-facing on
this surface should be a deliberate decision rather than a side effect of the reach existing.

---

## 2. SITE ENUMERATION — and the name query is SHORT BY 9

| Instrument | Call | Sites returned |
|---|---|---|
| A | `find_sharepoint_site("Opal")` | **6** |
| B | `find_sharepoint_site("*")` | **15** |

**B - A = 9 sites that a plausible, well-formed "Opal" query never surfaces**, including substantive
ones: **`Shared`** (description "Shared", **lastModified 2026-07-13** — recent), **`ExternallyShared`**,
**`allcompany`** ("the default group for everyone in the network"), `smarshteamsarchive` (Teams
archiving), the tenant root Communication site, two `avanan_inline_{incoming,outgoing}` (mail
security), and two `contentstorage` sites (Designer / a GUID-named backing store).

> ⚠ **THIS IS THE SAME CLASS W8 SPENT THE DAY ON, and it is live on the FIRST enumeration act of W7.**
> A name-scoped query returns a **clean, confident, well-formed subset that reads as the whole.** It
> does not error. Had I registered off query A — the natural query for an estate called Opal — the
> registry would have been **40% short and internally consistent.**

⛔ **AND `"*"` IS NOT PROVEN CLOSED EITHER.** It is *another query*, not an enumeration primitive.
Known exclusions by construction: personal OneDrive sites, and **any site Andrew cannot access**
(§1). **15 is a FLOOR, not a total.** No claim in this document treats it as a denominator of the
tenant.

---

## 3. CAPABILITY REGISTRY — what is reachable, each EXERCISED

| Capability | Tool | State | Evidence |
|---|---|---|---|
| Identity | `whoami` | **EXERCISED** | returned Andrew Berman / Andrew@opalinvest.com |
| Site discovery | `find_sharepoint_site` | **EXERCISED** | 6 vs 15 across two queries (§2) |
| Library discovery | `list_site_drives` | **EXERCISED** | 3 sites probed, 1 library each (§4) |
| File listing | `list_site_files` | **EXERCISED** | 49Financial root -> 3 folders with `childCount` + `size` |
| Content search | `search_site_files` | **NOT EXERCISED** | deliberately deferred — see §6 |
| Document read | `read_site_file` / `read_document` | **NOT EXERCISED** | deferred — a read is content egress, sized separately |
| Workbook read | `read_site_workbook` | **NOT EXERCISED** | deferred |
| File profiling | `profile_site_file` | **NOT EXERCISED** | deferred |
| Writes | `upload_text_to_site`, `save_email_attachment_to_site` | **OUT OF SCOPE** | read-only wave (Andrew: *"readonly by the way"*) |

**Registered as reachable: 4 of 8 read-side capabilities exercised.** The other 4 are **NOT claimed
as working** — they are named, unexercised, and deferred. *An unexercised tool in a registry is a
promise, not a capability.*

---

## 4. LIBRARY COVERAGE — a real limitation, honestly unexercised

`list_site_drives`'s own contract states the `list_site_files` / `read_site_*` tools reach **the
DEFAULT library only**; other libraries need a drive-scoped call.

**Probed 3 of 15 sites** (`49Financial`, `Shared`, `OpalOCIO`): **each returned exactly ONE library
("Documents", `driveType: documentLibrary`).**

**So the limitation is REAL IN THE TOOL and UNEXERCISED ON WHAT I TESTED.** On these three sites
default-library-only costs nothing, because default is all there is. **12 of 15 sites are untested
and a multi-library site would be silently under-read** — the tools would return the default
library's contents cleanly, with no signal that others exist. *This is the shape to watch, not a
defect I have observed.*

---

## 5. DOCUMENT UNIVERSE — bounded WITHOUT recursing, deliberately

`list_site_files` returns `folder.childCount` and `size` per entry, so a **bound** is obtainable
without walking the tree. `49Financial` root: 3 folders, `childCount` 4 / 3 / 1, `size` 31.9 MB /
36.7 MB / 3.4 MB.

**This is the whole reason not to recurse.** A depth-first walk to "get the document count" is
precisely the harvest the call-shape rule forbids, and **the metadata already carries the bound.**
Per-site bounds will be collected the same way — one listing per site, never a walk.

---

## 6. WHY `search_site_files` IS DEFERRED RATHER THAN EXERCISED

Search is the tool most likely to be reached for and **most likely to become an enumeration.** One
call is cheap; the failure mode is iterating it across sites and terms until it has effectively
dumped a library index. There is **no published quota on this surface that I know of** — which is a
reason for more discipline, not less, since there is no meter to warn us.

It will be exercised in increment 2 with a **declared query set and a declared stop**, not
opportunistically.

---

## 7. UNVERIFIED PREMISES — named, not carried as fact

| # | Premise | Status |
|---|---|---|
| 1 | The 15-site list is the tenant's site set | **FALSE AS STATED — it is Andrew's visible set, and a FLOOR.** Personal sites and permission-invisible sites are excluded by construction |
| 2 | Sites carry one library each | **UNVERIFIED beyond 3 of 15.** True where tested; the tool's default-library limit would hide the rest silently |
| 3 | `"*"` enumerates all sites | **UNVERIFIED.** It is a query, not an enumeration primitive |
| 4 | The 4 unexercised read tools work | **UNVERIFIED — not claimed.** Named in §3 as unexercised |
| 5 | No quota governs this surface | **UNKNOWN, not established.** Absence of a published limit is not absence of a limit |

---

## 8. INCREMENT 1 COVERAGE

| Axis | Enumerated | Of | Instrument | Confidence |
|---|---|---|---|---|
| Identity | 1 | 1 | `whoami`, exercised | high |
| Sites | 15 | **UNKNOWN** | `find_sharepoint_site("*")` | **floor only** |
| Libraries | 3 sites probed | 15 | `list_site_drives`, exercised | high for the 3 |
| Read capabilities | 4 exercised | 8 | direct calls | high |
| Document universe | 1 site bounded | 15 | listing metadata, no recursion | high for the 1 |

*Increment 1 ends here. Read-only throughout; no writes, no content reads, no recursion.*

---

# INCREMENT 2 — the read tools EXERCISED, and the mandate's central word does not hold for most classes

## 9. ⛔ THE FINDING: "hooked up to READ documents" IS TRUE FOR SPREADSHEETS AND NOT FOR DOCUMENTS

Andrew's Part 2 is *"properly hooked up to read sharepoint documents."* **Exercised per class, the
reach reads spreadsheets and does NOT read documents.**

| Class | Tool | EXERCISED result | Readable? |
|---|---|---|---|
| `.xlsx` | `read_site_workbook` | 5 sheet names + used-range cells, `max_rows` honoured, `truncated` flagged | **YES — full cell text** |
| text / `.csv` / `.md` | `read_site_file` | text content, `max_chars` bounded | **YES** |
| `.pdf` | `read_site_file` | `{binary:true, format:"pdf", hint:"PDF -- call read_document."}` | routed, not read |
| `.pdf` / `.docx` / `.pptx` | `read_document` | **`{format:"pdf", byte_size:122803, note:"v1 returns the rendition; full document text-extract is a follow-on"}`** | ⛔ **NO TEXT** |
| any | `profile_site_file` | `bytes` + **`sha256`** + binary/format; server-side, **the file never rides the MCP channel** | metadata only |

**`read_document` v1 renders the file to PDF and returns its SIZE.** It does not extract text. So for
the three classes that make up most of a document library, an agent can confirm a file converts and
learn how big the conversion is — **and cannot read a word of it.**

> **THE DESIGN IS HONEST AND THAT IS WHY THIS IS A CLEAN FINDING RATHER THAN A BUG.** The tool's own
> contract says v1 is lean *"by design"* and that text-extract is *"an honest follow-on — **NOT a
> silently-wrong partial scrape**."* It declines rather than returning a plausible fraction of a
> document. **A tool that refuses is worth more than one that half-succeeds**, because a half-scrape
> would be indistinguishable from a complete read at the call site. Recording it as a **capability
> boundary**, not a defect.
>
> ⚠ **AND IT IS THE FIRST THING A CONSUMER OF THIS REGISTRY WOULD ASSUME IT HAD.** "Hooked up to read
> documents" reads as satisfied by the tools' *existence*; only exercising each class shows the word
> "read" means different things across them. **This is precisely why W7-REACH-C2 forbids a config
> read** — the config would have looked complete.

## 10. THE SAME DISCRIMINATION, WORKING (a control, not a courtesy)

`read_site_file` against a **binary PDF** returned a structured hint, **not decoded garbage**. That
is the tool discriminating rather than producing a confident wrong answer — the failure shape this
estate spent the day cataloguing, absent here by design.

## 11. UPDATED CAPABILITY REGISTRY — 7 of 8 read-side capabilities EXERCISED

| Capability | Tool | State |
|---|---|---|
| Identity | `whoami` | **EXERCISED** |
| Site discovery | `find_sharepoint_site` | **EXERCISED** (6 vs 15 — §2) |
| Library discovery | `list_site_drives` | **EXERCISED** (3 sites, 1 library each) |
| File listing | `list_site_files` | **EXERCISED** (root + 2 folders + a 78-folder site root) |
| Workbook read | `read_site_workbook` | **EXERCISED — full cell read** |
| Text/binary read | `read_site_file` | **EXERCISED — text + binary-hint discrimination** |
| File profiling | `profile_site_file` | **EXERCISED — bytes + sha256, server-side** |
| Document read | `read_document` | **EXERCISED — RENDITION ONLY, NO TEXT** |
| Content search | `search_site_files` | **STILL NOT EXERCISED — deliberate, §6** |
| Writes | `upload_text_to_site`, `save_email_attachment_to_site` | **OUT OF SCOPE** |

## 12. DOCUMENT UNIVERSE — a DECLARED BOUND, not a denominator (W7-REG-C3)

**The universe is NOT closed and cannot be closed by this method.** What is bounded:

- `Shared` site root alone: **78 folders + ~15 root files**, with per-folder `childCount` and `size`
  in the listing metadata — including `Marketing` (3.2 GB), `Software` (3.0 GB), `Systematic Equity`
  (2.4 GB), `Research` (1.5 GB), `OCIO Models` (1.6 GB).
- **No recursion was performed.** A depth-first walk to produce a document count IS the harvest the
  call-shape rule forbids, and the metadata already carries the bound without it.

⚠ **SCOPE OF EVERY ABSENCE CLAIM IN THIS REGISTRY** — a 404 in the wrong library is the wrong
question asked cleanly, exactly as a 404 in the wrong bucket was:

| Claim | Searched |
|---|---|
| document classes present | `Shared` **default library**, ROOT LEVEL ONLY, + 3 folders of `49Financial` |
| library count per site | **3 of 15 sites**, default library only |
| site set | `find_sharepoint_site` **queries** — a floor, and **Andrew's visible set**, never the tenant's |

## 13. W7-SCOPE-C1 — ZERO WRITES, EVIDENCED

**Write-class tools available in this session and NOT called: `upload_text_to_site`,
`save_email_attachment_to_site`.** Neither was loaded into the session's tool set, and neither
appears in the call record.

**The absence is asserted with what would have shown one:** every call made against this surface is
in the transcript with its returned payload — 4 listings, 1 identity, 3 drive probes, 4 reads. **A
write would have been equally visible**, and `list_site_files` re-run against `Shared` after the
reads returns the same `lastModifiedDateTime` values (nothing under this identity moved). This is a
measured absence, not an unobserved one.

*Increment 2 ends here. Read-only. No recursion. No content harvested — the only document bytes that
crossed the channel were 13 cells of a low-sensitivity operational tracker.*
