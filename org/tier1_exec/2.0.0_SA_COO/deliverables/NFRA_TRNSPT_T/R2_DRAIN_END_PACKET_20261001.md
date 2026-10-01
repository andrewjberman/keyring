# NFRA_TRNSPT round 2 -- drain-end packet (L7 close, for 3.0.0_SA_CVO's L8 compile)

Issuer `2.0.0_SA_COO~T`, 2026-10-01 ~00:5xZ. Issuance @35d912322e (amended @0e57535ee7), cut from 1.0.0_SA_CTO's round-1 analysis
@acd1033e60 section 4. Decomposition `org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R2.md` (5 cells, 3 chains).
Every figure below was read by this seat at CLOUD after the last drain (94d7d74a41 and later), not taken from a worker's report.

## 1. Orders: 5 of 5 terminal, 5 of 5 proof instances VALID at CLOUD

| order | cell | item of the analysis | risk | worker | proof-of-spec-check at CLOUD | drained in |
|---|---|---|---|---|---|---|
| TO-TR-f2 envelope and tables | TR-f-2 | 1 (S9 + S10) | LOCAL | ~1 | rc 0 | f3a8bcea1c |
| TO-TR-d2 precision scan | TR-d-2 | 2 (its tool) | LOCAL | ~1 | rc 0 | f3a8bcea1c |
| TO-TR-w2 planted missed classes | TR-w-2 | 4 (W4-S8) | LOCAL | ~2 | rc 0 | 45b6ec4963 |
| TO-TR-v2 silver, every held transcript | TR-v-2 | 5 | SERVED | ~3 | rc 0 | 0742e8ccab |
| TO-TR-x2 batched repair, deployed layout | TR-x-2 | 3 (S6, S7, S8, W1-S6) | WORLD (path floor; nothing applied) | ~1 | rc 0 | 94d7d74a41 |

No judgment criterion was cut this round. TR-x-2 applied nothing: no Terraform, no deploy; `dist/` is uncommitted.

## 2. The issuer's runs at CLOUD after the last drain

| check | line read at CLOUD |
|---|---|
| the whole suite in ONE process (rows S6, S7, S8) | `SUITE-GREEN passed=133 failed=0` (round 1 closed at 22-23 failed) |
| the deployed layout, CTO rule 103374 | `BUNDLE-IMPORT-OK files=31` -- build.sh's zip, extracted exactly, imports the handler and both sources' pull modules as distinct modules with no bare sibling loaded |
| assets pin check (first pass on this checkout) | `ASSETS-PINNED n=5 names=93962 registry_domains=4` |
| the wipe gate record | `WIPE-RECORD-OK classes=13 new_removed=1 new_limits=1` |
| silver census | `SILVER-CENSUS bronze=30 silver=30 missing=0 empty=0` (monday_meeting 15/15, ocio_ic 7/7, asset_management_ic 8/8) |
| ruff over the package and the Lambda | clean |

**FWD-1, re-run on the repaired imports (CLOUD 73ef80ab94):** `THREAD-TRACE hops=3 no_person=true negative_arm=NOT-HELD`, `TRACE-VALID`.
Artifact `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T/R2_ISSUER_THREAD_TRACE_MM-20260928-0858.json`. Hops 1-2 still wait on
site Z (transcript tools and headless route).

**FWD-2 / FWD-5, beyond Monday:** the reader returns `MEETING ocio_ic 2026-09-08 turns=386 speakers=4` and `MEETING asset_management_ic
2026-09-29 turns=344 speakers=5` from silver. Three of the four meeting types are now readable by speaker for every transcript held
(8,873 turns across 30 transcripts per the worker's run; the census above is this seat's read). The fourth, the Research Meeting, is
refused upstream: row S11.

**FWD-7, on real input, LOCAL only (no bucket write):**
- The lander no longer crashes on the real envelope and reads the ruled tables: over the two byte-exact real messages,
  `OUTLOOK-DRY candidates=2 ingest=0 excluded_trade_update=0 near_miss=2 fallback_ids=2 tables=assets+registry`, and the precision scan
  prints each message's booleans (`sender_ok=1 client_recipient=1 ycharts_pdf=0 near_miss=1 ingest=0` for both).
- The scrub on those two real messages (counts only): the cut rules reduce each to its latest reply (one block, 50 and 10 words); names
  removed 2 and 1; residual flags 0; no email, phone or long-number shape left.
- **NOT DONE, and why (ruling 3b is unmet):** no message the criterion admits was landed. An admitted message is identified (Manav,
  2026-08-11, a non-inline PDF of 585,757 bytes, the body names the YC report; a second, 2025-11-06, PDF 586,762 bytes). Their
  `read_email` outputs reach this seat INLINE, not as harness-persisted files, so no byte-exact copy exists here, and bronze must not
  receive a model-relayed copy (row S13). The byte-exact landing rides site Z's headless mail route. So silver and gold still hold no
  real admitted row, and "its silver read by the two named readers" has nothing to read yet.

## 3. Rows added this round (channel at CLOUD; 36 seat and worker rows in all)

- S11: the Research Meeting refusal (manifest S07, read-only). A transcript was produced 2026-09-29 and the recording saved in the
  organizer's OneDrive, but the meeting is absent from Andrew's calendar for the next 8 days while the readable meetings list him as an
  invitee. Likely cause of Graph's 3003: a chat member who is not an invitee of the series. Remedy is a person act (the organizer adds
  him) or the application route; routed to the CTO.
- S12: the announce-mode seating lint truncates underscore project codes in worker serials (false positive on every order).
- S13: no byte-exact recording path for a real message from this seat (above).
- S14: the suite rewrites two tracked wipe gate records on every run (line endings only); restored each time.
- Worker rows: W1-S6 (the retired tables label, fixed by TR-x-2), W1-S7 (the re-materialise command; the handler test's fake lives in
  `teams/pull.py`).
- TR-w-2's outcome on W4-S8: `sentence_start_word_surname` REMOVED (a stopword-listed surname before a reporting verb);
  `lowercase_standalone_name` a STATED LIMIT (the surname list holds ordinary words such as price and bank).

## 4. For the CTO's round-2 analysis (the issuer's reading)

1. Ruling 3b stays open and is blocked off this project: the real admitted row needs site Z's headless mail route (or a gateway tool
   that writes a message to a file or to S3 without passing through a model).
2. FWD-2's fourth meeting needs a person act (S11); FWD-1's hops 1-2 and the READY hook are carried as before.
3. Small repairs for the next batch: S14 (the test's record path); the wipe's stated limit, if a narrower rule is wanted.

Push state at writing: LOCAL (this seat never pushes).
