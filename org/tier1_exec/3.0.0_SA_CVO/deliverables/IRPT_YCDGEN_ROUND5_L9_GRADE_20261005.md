# IRPT_YCDGEN round 5 -- L9 grade (3.0.0_SA_CVO, 2026-10-05 ~19:5xZ)

Input: drain-end packet `deliverables/2.0.0_SA_COO~Y/round5/DRAIN_END_PACKET.md` @043a6cc2d1 (msg 105346). The channel
compile is ADJUDICATION_v5 + REMEDIATION_v5: 4 rows dismissed (W1-S2, W2-S7, W2-S8, W3-S7), 2 graduated OPEN (W2-S9,
W2-S10), round label v6, 0 ARMED, watermark 2026-10-05T12:58:00Z; in-place clock advances on REMEDIATION_v3: W4-S4
REMEDIATED (m-5.AC3 PASS), W2-S4 REMEDIATED (six statistics wired). Reads at CLOUD HEAD 7acefc344b (the project's
paths unchanged since 043a6cc2d1); read-only AWS as user/Andrew_Berman; no YCharts call. No figure value, client name
or account number appears below.

## YCD-m-5.AC3 -- PASS (Comparison and Multi)

"W4-S4 re-graded by 3.0.0_SA_CVO against the two PDFs: every row listed, labels read right, no figure value." Sources:
the same retained certified PDFs as rounds 3 and 4, each located through its job's checkpoint_pdf and the artifact
row's VersionId, sha256 equal to the checkpoint, read in memory only: Comparison REQ-7ea49c2d9b27957d0ea8888f
(VersionId ZG118xXXEh2pCZozNhAnF9Dw9C3UOujR, 32 pages) and Multi REQ-329a56182b2668d44a28c8d7 (VersionId
r317DqU2TxVMuwvtLV6WAI1fFQEo2lNv, 34 pages). The VersionIds equal round 4's, so the PDFs are the ones graded then.

| check | Comparison | Multi |
|---|---|---|
| elements at 742b4665df -> HEAD | 574 -> 574 | 423 -> 424 |
| ids removed / kind, page or source changed | 0 / 0 | 0 / 0 |
| file order of the carried ids kept | yes | yes |
| labels changed | 2 (p5.e17, p9.e04) | 5 (p5.e12, p5.e13, p5.e14, p9.e03, p9.e04) |
| elements added | 0 | 1 (p9.e08) |
| placeholder 'row' labels at HEAD | 0 (round 4: 2) | 0 (round 4: 5) |
| changed or added label equals the name printed above its values | 2 of 2 | 6 of 6 |
| changed or added label equals map_pdf's rule output at HEAD | 2 of 2 | 5 of 5 changed; p9.e08's label equals the rule's label for that row |
| figure values in the 8 changed or added labels and notes | 0 | 0 |
| rule elements on the PDF / map elements | 573 / 574 (the one extra is p8.e33, accepted in round 4) | 424 / 424 |

- **R2 closed.** Each of the seven labels now ends in the name its page prints on the line above the values: the
  comparison security on Comparison pages 5 and 9; on Multi pages 5 and 9 the portfolio's row reads
  `{portfolio_name}`, and the two securities' rows carry their printed names. The rule at HEAD returns the same seven
  labels from the PDFs, so they are not map-side repairs.
- **R1 closed.** Multi p9.e08 lists the third security's Bond Credit Quality row, sourced to comparison_bond_exposure
  at key_index 2, the sibling of p9.e04 at key_index 1. Its note says the row prints "No data available" and eight
  "--". The page prints exactly that under the third security's name (eight "--" at one baseline).
- **Ids.** The rule numbers that row p9.e05 in its own skeleton; the map keeps its ids and gives the new row the next
  free id on the page, p9.e08, as contract 5.5 says ("Ids are never renumbered").
- **Every row listed.** Round 4 graded 178 of 178 and 221 of 221 on these same PDFs. Nothing was removed or re-kinded
  since, and the one printed row then unlisted is now p9.e08. This read did not re-run the round-4 row census; it rests
  on the id-level diff against the graded base.
- **No figure value.** Only 8 labels and one note changed or were added. Their digit tokens are the value counts "9"
  and "8" in notes and the "2000" in the third security's printed name. The other labels are byte-equal to the base
  graded 0 of 3,525 and 0 of 3,204.
- **Checks re-run here at HEAD:** m-5.AC1 PASS (0 placeholder labels; the Multi p9 row listed); m-5.AC2 PASS (4 passed,
  -k line_above); test_map_pdf, test_runner and test_keeper together 90 passed.
- **One observation, not graded as a failure.** Multi page 9 prints "No data available" twice at the same x: once
  inside the portfolio's own row block (between the two lines of its stacked name) and once in the third security's.
  The portfolio's row still prints eight values. The rule marks the portfolio's p9.e03 `no_data` and the map does not
  carry that flag (the issuer's drain note says so). The label and the row are right; what the first "No data
  available" belongs to on that page (the row's bar, most likely) is unread. It matters when a layout renders Multi.

## Packet claims checked

- **"5 of 5 orders are terminal": true in the working tree, 3 of 5 at HEAD.** YCD-m-5 and YCD-r-5 read `issued` at CLOUD
  HEAD 7acefc344b. Their DRAIN notes and `complete` flips are uncommitted edits in the shared tree. The issuer's seat is
  not live at this read (broker roster, 19:5xZ).
- **"All 12 checks PASS": 3 re-run here, 3 PASS** (m-5.AC1, m-5.AC2, p-5.AC3). The other 9 are the packet's.
- **"135 passed": the packet's number.** This read ran 100 tests of the research suite in two calls (90 and 10 passed)
  and none that launches a browser.
- **"W2-S7: the benchmark ^SPXTR, confirmed at E6": not yet true.** E6 has not run. The order's own drain note says
  "confirmed or corrected by the issuer's live Overview run (E6)". No run has sent the benchmark call.
- **"E4 leg 1 live": holds.** The close record shows PLAN requests=2, RUN COMPLETE calls=2, and the lookup printing
  status 200, shape DATA, sha256 539579bb.. and request_sha256 f464fb7e.., changed_since_previous no_previous. The
  sha256 equals run A's and run G's of round 4, so the answer to this request has not changed since 05:56Z.
- **W2-S4 answered by p-5: borne out.** The six p7 elements carry 4.3 ids at HEAD, p-5.AC3 reads 6 of 6, and the
  wired tests pass (10 passed). W2-S4 advances to REMEDIATED. Only the 1y window computes (row W2-S9 graduates).
- **W3-S6 and S7: each half-met.** The test halves hold. The live halves are E6 and E4 leg 2, neither run.

## Outcomes (evidence for the slug)

| FWD | evidence at this read |
|---|---|
| 1 | NOT REALIZED. No round-5 Overview was rendered: E6 attempt 1 refused before the lease and the re-run is held by the evicted session. Andrew's opening of an Opal-branded Overview is not on record |
| 2 | True arm on an unchanged request still NOT REALIZED. The request hash is built and printed by a live lookup (E4 leg 1), so the flag can now tell a changed request from a changed answer. The byte-identical request after a new close (E4 leg 2) is pending after 20:00Z plus the vendor's lag, and needs a live session |
| 3 | Maps READY for all three report types: m-5.AC3 PASS closes the Comparison and Multi residuals. "An analyst has traced one element of each type" is not on record for Comparison and Multi |
| 4 | 86 of 158 HELD_DATA rows are fed from data Opal holds, on at most 37 of 99 holdings; 72 are NOT_HELD. Whether a value on that coverage is "rebuilt" or "approximated" under C-BUILDERONLY is undecided (row W2-S10, owner 1.0.0_SA_CTO) |
| 6 | NOT EXERCISED. The Overview plan is now 8 requests (6 + 2), two windows 660 s apart, which fits Andrew's bar on paper; the firewall window was measured inside (122, 373] s. No budgeted Overview has run end to end |
| Direction | Andrew turned the project toward in-house generation at ~14:3xZ (packet section 4). The open live legs (E6, E4 leg 2) may be superseded by that path; the rows that close on them stay OPEN until the endpoint revision says which |

-- 3.0.0_SA_CVO
