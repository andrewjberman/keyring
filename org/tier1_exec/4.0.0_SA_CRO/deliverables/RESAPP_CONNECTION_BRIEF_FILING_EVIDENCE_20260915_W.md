# RESAPP connection brief: filing evidence must resolve before drafting

Seat: `4.0.0_SA_CRO~W`  
Date: 2026-09-15, during the 06:13:02Z–07:13:02Z progress loop  
Recipient: `1.0.0_SA_CTO~W`  
Authority: Andrew's request to check COO~W/RESAPP progress, identify gaps, and send connection briefs. This is an implementation connection recommendation for the COO's next cut, not a task order or an amendment to the CVO-reviewed half.

## Finding

The measured filings response does not yet provide the resolvable passage evidence that the existing drafting consumer needs. Choosing a tag parser alone will not establish that connection. In addition, the existing drafting gate checks source titles, and can pass an unquoted sentence whose evidence ID resolves to nothing. These are distinct from the already reported page-level absence of drafting.

## Measured sources

- PRD `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md@2f3b65d8b842847bd31eefc63766593bcc235b42`, lines 418–434: typed filing analysis, a thesis-driver series, generated marking beside cited passages, and filing-derived executive officers/role starts.
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/SUBSTRATE_CARDS.md@5007337353`, card 1: ONE public Boeing filing, a named Item 1A + Item 7 excerpt, 76 items, 71 with inline tags, five uncited segment rows; no production pool write.
- The adjacent `BA_10K_2026-01-30_measurement.json@5007337353`: `citations_total=0`, `blocks_with_citations=0`; parsed fields are company, fiscal_year, guidance_changes, segment_revenue, top_risks, management_commentary, big_bets, big_challenges. There is no thesis-driver series, executive-officer roster, or role-start field in this measured parsed object. The saved measurement has the source URL but no saved citation-index-to-passage map. The script writes its sent text separately to scratch; that alone does not establish the model tag indices' meaning.
- `lib/research/drafting/pipeline.py@6093d06a0eaae473a07da38c7ec64579ef58122e`, lines 32–55: `_source_texts_for` skips unknown IDs and reads only `item['title']`; `_gate_sentences` checks quoted spans without independently requiring every evidence ID to resolve.
- `lib/research/drafting/schema.json` in the same drafting implementation: evidence is a nonempty array of strings, generated is true, and the description explicitly allows an empty quoted-span list. JSON Schema cannot establish that an ID resolves to source content.

Three local synthetic probes against the unchanged gate, with no vendor calls or output publication:

| Input | Observed |
|---|---|
| Unknown evidence ID; no quoted spans | 1 sentence passed, `verbatim_check=PASS` |
| Valid ID; exact passage in `text`, absent from title | 0 passed, 1 refused |
| Same valid ID; exact title quoted | 1 passed, `verbatim_check=PASS` |

This does not say title checking is wrong for the original headline fixture. It shows that replacing its producer with filing analysis requires an evidence adapter and a separate resolution check.

## Connection to cut

1. Persist the source filing and exact submitted excerpt with their content hashes, canonical security identity, accession/source filing ID, retrieval time, and the extraction/parser version. If a stored analysis is replaced, old displayed claims must still resolve to the source version they cited.
2. Choose the two-pass or tag-parser route named by the PRD, and demonstrate how each emitted claim resolves to an exact source passage. A syntactically valid `<cite index="...">` string is not proof that the passage can be located. Preserve raw output for inspection; reject or hold unresolved and uncited claims rather than mark them cited.
3. Give the drafting reader typed evidence records with stable evidence IDs and actual passage text. Validate existence, the security/document association, and source version for every cited ID before the verbatim gate. Run verbatim checks against the selected passage, not its title. Keep passage support and exact quotation checking as separate outcomes; a paraphrase has no quoted span but still requires evidence.
4. Connect accepted generated sentences to the API and render their evidence beside them. A complete machine-analysis object is not yet a working Thesis tab. Retain the existing generated marking and do not turn the five uncited numeric rows into grounded chart inputs.
5. Measure the thesis-driver and executive-management outputs separately. The current analyzer schema/excerpt did not exercise those fields. A chart requires a series identifier, observations with period/unit/basis, and resolvable figure evidence; the officer lane requires the actual officer/role-start source section or proxy. Do not infer a complete officer roster from the risk/MD&A measurement.

## Acceptance evidence for the connection

- A valid cited claim resolves through the saved analysis, source hash and passage into the displayed evidence.
- An unknown evidence ID with no quotation fails admission (the first probe above must change); a valid body quotation passes even when its words are absent from the document title.
- A made-up tag index, uncited numerical row, mismatched security, or mismatched source version is held with a reason.
- One actual thesis-driver series and one filing-derived officer/role-start record are exercised before claiming those outputs exist. A missing field is visible as missing; it is not zero or a blank successful chart.

No credentials were read, no model call was made, no publisher was hit, and no cadence was activated for this review. The production collection mechanism remains reserved to Andrew.
