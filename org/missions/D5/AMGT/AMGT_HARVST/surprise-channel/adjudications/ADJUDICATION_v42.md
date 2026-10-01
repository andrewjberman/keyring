# AMGT_HARVST ROUND 32 -- L8 COMPILE (the Friday round; all criteria mechanical)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-01 ~11:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round32/ROUND32_DRAIN_END_PACKET.md` @`e781945d21` (5,981 B, read to EOF), msg 27777.
**L7 re-measured:** `TO-HVST-ae-1`, `ae-2`, `ae-4`, `ae-5` read `complete` on their LAST `<status>` tag; `ae-3` (first light) is
an issuer-graded cell. 0 judgment criteria.

---

## 1. RE-READ BY THIS SEAT

- **FWD-12, the quarantine:** `s3://opal-data-harvest/seeking-alpha/harvest/silver/quarantine/date=2026-10-01/20261001T064759Z.json`
  exists (3,908 B) with `article_keys` 33 and `silver_parts` 35. That equals the packet's "33 keys" (38 rows).
- **The served gold move:** `amgt/harvest/gold/article_security_mention/date=2026-10-01/part-20261001T064839Z.parquet` exists. The
  DELTA=0 claim rests on the issuer's signing dry run (379 rows, equal digest), not re-run here.
- **`Z-W91-S4`, the vendor-egress row** (the round's most consequential row):
  - **What happened.** `verification.py`'s press-and-hold fallback called `verification_locator.locate`. That function reads
    secret `astn/kimi/api-key` and POSTs a base64 page screenshot to `https://api.moonshot.ai/v1/chat/completions`. **It fired once
    at 09:39Z** on bbg's anonymous census page: the request was sent and the response timed out. That is an external vendor call made
    without Andrew's per-use word (CLAUDE.md, Agent Autonomy). The call was inherited code, not a choice, but it happened.
  - **The disarm holds for callers.** At HEAD no file in `lib/opal_data_harvest` imports `verification_locator`. The two references
    are tests asserting its absence (`test_ae5_hookup.py:102`, `test_ae5_challenge_path.py:234`). `220a74350a` moved the locator to
    the page's own DOM.
  - **What remains.** `verification_locator.py` itself (`:15` the secret read, `:19` the POST) is still in the tree. It is also still
    named in `build_release.py:13`, so it ships with every release, one import away from firing again. Removing the module, or
    dropping it from the release list, makes the disarm structural rather than by-absence-of-caller.
- **FWD-11's evidence limit (`W91-S8`)** is honestly stated. The box's last-input clock moves without a human, so "no human hand" is
  INFERRED. The bbg press-and-hold PASS is real (HTTP 200 after). wsj and barrons met no challenge, and ft and sa were not met.
  FWD-11 names all five, so it is not met, and the packet says so.

## 2. DEPTH AGAINST ANDREW'S BAR (FWD-14)

Per the packet: 11 of 89 names with any silver since 2026-01-01, 6 at 50+, 1 at 100+. Andrew's bar is "50+ articles per security
going back to January, ideally 100+". **6 of 89 meet it.** The packet states the bar is not met and not re-based, which is the rule.
`Z-S51` (the census population's two key spaces share 0 keys) means FWD-14's own census is not yet well-formed. The 6-of-89 is the
issuer's universe-key read, not the PRD's census.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W90-S2`, `Z-W92-S1`, `Z-W92-S4` (BLOCKING/ARMED) | **GRADUATED** | fixed @`cec6fb0ba6`+`03457e5899`, `254ea37cf6`, `3669bd0f0a`+`6039cefc48` per `Z-S52`; the close run reads 12 of 12 rc 0 |
| `Z-W91-S4` (ARMED, vendor egress) | **GRADUATED** for callers | verified (section 1); the module remains packaged, an enrichment item to make it structural |
| `Z-W91-S5` (ARMED) | **GRADUATED** | fixed @`791616d9b6`, `3cdb41b7e2` per `Z-S52` |
| `Z-W91-S8`, `Z-W91-S10` (ARMED) | **CARRIED**, ruled by `Z-S52` | an instrument gap (input source) and a transient; neither blocks a criterion |
| `Z-S52` (the disposition record) | **GRADUATED** | as above |
| `Z-S51` (census key spaces) | **CARRIED**, INERT | round 33 item 4 |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4 (+ the first-light cell graded). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** 7 ARMED, 5 graduated, 2 carried as ruled. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

## 5. FOR THE ROUND-32 ANALYSIS

1. **The 09:39Z vendor call is a fact Andrew should have.** It was unintended and short, but it was egress off Opal infrastructure
   without his word. One line in his 09:00 ET list. Remove `verification_locator.py` from the tree, or at least from
   `build_release.py`.
2. FWD-11 needs ft's and sa's challenges met, wsj/barrons challenged (not merely unchallenged), and an input-source instrument.
3. FWD-14: 6 of 89 at Andrew's bar; fix the census key space (`Z-S51`) before quoting a figure against it.

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S52",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-01T11:45:00Z",
    "one_line": "L8 round 32: quarantine object holds 33 keys / 35 silver parts; the served mention part exists; Z-W91-S4's vendor egress verified: verification_locator POSTed a page screenshot to api.moonshot.ai once at 09:39Z without Andrew's per-use word; no caller remains at HEAD but the module still ships via build_release.py:13; FWD-11 not met (bbg passed; wsj/barrons unchallenged; ft, sa unmet); FWD-14 at 6 of 89 names at 50+.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-ae-1, ae-2, ae-4, ae-5 read 'complete' on their LAST <status> tag.",
        "s3://opal-data-harvest/seeking-alpha/harvest/silver/quarantine/date=2026-10-01/20261001T064759Z.json: 3908 bytes, article_keys 33, silver_parts 35; amgt/harvest/gold/article_security_mention/date=2026-10-01/part-20261001T064839Z.parquet present.",
        "lib/opal_data_harvest at HEAD: verification_locator referenced only by test_ae5_hookup.py:102 and test_ae5_challenge_path.py:234 (absence asserts) and build_release.py:13 (release list); verification_locator.py:15 SecretId astn/kimi/api-key, :19 requests.post https://api.moonshot.ai/v1/chat/completions.",
        "Row AMGT_HARVST-Z-W91-S4 world_is: fired once at 09:39Z on bbg's anonymous census page, requests ReadTimeout (request sent)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W90-S2",
      "AMGT_HARVST-Z-W92-S1",
      "AMGT_HARVST-Z-W92-S4",
      "AMGT_HARVST-Z-W91-S4",
      "AMGT_HARVST-Z-W91-S5",
      "AMGT_HARVST-Z-S52"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @e781945d21 asserts 4/4 complete, the close run 12/12, every round-32 ARMED row disarmed or ruled, and FWD-11/FWD-14 not yet met.",
    "world_is": "True as read; plus one external vendor call already made at 09:39Z, and the module that made it still shipped by the release list.",
    "notes": "FOR THE ROUND-32 ANALYSIS: put the 09:39Z vendor call on Andrew's list; remove verification_locator.py or drop it from build_release.py; FWD-11 needs ft/sa met and wsj/barrons challenged; fix Z-S51 before quoting FWD-14."
  }
]
```
