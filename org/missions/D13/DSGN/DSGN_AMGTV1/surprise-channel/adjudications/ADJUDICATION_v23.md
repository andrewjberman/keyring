# DSGN_AMGTV1 ROUNDS 24-26 -- L8 COMPILE + L9 -- FWD-16 met on the face; BA's timeline day route TIMES OUT on every call since 10:14Z

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~10:4xZ
**Input:** `2.0.0_SA_COO~D`'s `round26/ROUNDS24_26_CLOSE.md` @`a5a1458e4a` (3,598 B, read to EOF), read off the tree; no message had
arrived. Candidate portal `0ab75973` (LOCAL, worktree 70). CTO content review @`65177a507f` APPROVED.
**L7 re-measured (LAST `<status>` tag):** AV-zc-1, zc-2, zc-3, zd-1 `complete`. **0 judgment criteria.**
**Rows past v22:** `Z-S16` (1 of 47).

---

## 1. GRADES AND READS

| item | grade / read |
|---|---|
| AV-zc-3 against this seat's v21 conditions | **MET.** (a) The check is renamed `claims_resolved_count_stated`. (b) `POSTURE_HARNESS_PLANT=zero` drives one claim's cites down the 0-resolved path. This seat's runs at 0ab75973: clean rc 0, `CHECKS-OK 32 of 32`; zero plant rc 0, 32 of 32 (the honest 0-resolved claim is credited); zero plant with `LEGACY_PREDICATE=1` rc 1, `CHECKS-WRONG-WAY BABA_US_Equity:claims_resolved_count_stated` (the control). The dishonest case (a page that drops the notice) rests on the separate `unresolved_cites_say_so` predicate (posture.harness.cjs:515); no plant exercises it |
| VLO Peers, walk `20261002T101105Z` shot 021 | **12 of 12 absent columns state a reason in reader words**: "the data source does not report this figure for these peers", "only a ratio is reported, not the amount", "estimates go out one year only", "the source's leverage measure is not defined as debt to equity", "growth is reported over at most three years". **FWD-16 and FWD-8 are both met on the face** |
| VLO Exec, shot 015 | the Lusha line prints once (S14 fixed); the CEO basis is in words (no SERP) |

## 2. FINDING -- `Z-C-S29`, BLOCKING, ARMED (disarm owner `1.0.0_SA_CTO~Z`): the timeline day route times out, demo-visible

The walk's "one API issue", a 503 on `GET .../security/BA_US_Equity/timeline/day/2026-09-08`, is not one-off.
- This seat invoked the deployed `opal-amgt-scoped-api` (read-only) for BA's day 2026-09-08 (twice) and 2026-09-03.
- **Every call failed**: `errorType Sandbox.Timedout`, "Task timed out after 29.00 seconds", REPORT `Status: timeout`, Max
  Memory 408 MB of 1,769.
- CloudWatch over 8 hours (paginated, 3 pages per query): **0 timeouts in 694 invocations from 05Z to 09Z; 5 timeouts at 10Z,
  the first at 10:14:25Z** (the walk's call, then this seat's).
- The deployed code has not changed since 07:45:38Z.
- On the earlier walks (07:28Z, 08:49Z) the same route served BA's Sept 8 articles.

Sept 8 is BA's coverage-event day ("Boeing Delivers 51 Jets in August ... 2 articles"), the link the page invites the reader to
press. At the demo it opens to a failure.

**Mechanism (measured, not proven):**
- The day route reads silver article prefixes per publisher (`lib/research/harvest/timeline_api.py:324`, the read path at
  `publication_gold.py:915`). bbg silver is now 622 parts / 85.0 MB (it was 576 / 69.1 MB at 05:2xZ) and wsj is 396 / 76.3 MB.
- Only 1 bbg part was added after 08:49Z, so the data barely moved. A cold container cannot read that much in 29 s, while a
  warm one served from its per-process cache.
- A timed-out invocation kills its sandbox, so every following call starts cold again.

The fix belongs to the read path's owner (HARVST's timeline code, served on RESAPP's function). It is not a page defect.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S16` | DISMISSED_WITH_REASON | the correction row records the true times of W71-S1/S2 (08:37Z), as the gate requires instead of an in-place edit |
| `Z-S14` (REMEDIATION_v1) | **REMEDIATED** (clock only) | AV-zc-1; the Lusha line prints once on walk 101105Z shot 015 |

## 4. L10 PRECONDITION

4 of 4 terminal; 0 judgment; Z-S16 dispositioned. `Z-C-S29` is this seat's own row; it does not count against the slug, but it
is the demo's live risk. **MET.**

---

```json
[
  {
    "id": "DSGN_AMGTV1-Z-C-S28",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T10:35:00Z",
    "one_line": "Rounds 24-26 L8/L9: 4 of 4 complete, 0 judgment; zc-3 meets this seat's v21 conditions (renamed; zero plant credited, legacy-predicate control red); walk 20261002T101105Z: VLO Peers 12 of 12 reasons in reader words (FWD-16 and FWD-8 met on the face), VLO Lusha line once (S14 remediated); Z-S16 closed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: AV-zc-1, zc-2, zc-3, zd-1 complete; 0 judgment=\"true\".",
        "posture.harness.cjs at portal 0ab75973 (worktree 70), this seat: clean rc 0 CHECKS-OK 32 of 32; PLANT=zero rc 0 32 of 32; PLANT=zero + LEGACY_PREDICATE=1 rc 1 CHECKS-WRONG-WAY BABA_US_Equity:claims_resolved_count_stated.",
        "tmp/ui-walk/20261002T101105Z/shots/021-VLO-US-Peers-expanded.png: 12 absent columns, each '<Column>: <reason in reader words>'.",
        "tmp/ui-walk/20261002T101105Z/shots/015-VLO-US-Exec-Management.png: 'Contact enrichment was skipped: no company web domain is on record for this name, ...' once."
      ]
    },
    "adjudicates": [
      "DSGN_AMGTV1-Z-S16"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S16 is the gate-required correction record of W71-S1/S2's placeholder times; nothing further owed.",
    "spec_asserts": "Close record @a5a1458e4a: 4 of 4 drained, candidate 0ab75973, VLO Peers 12 of 12 class reasons.",
    "world_is": "True as read.",
    "notes": "REMEDIATION_v1 Z-S14 advanced to REMEDIATED in the same commit (clock only)."
  },
  {
    "id": "DSGN_AMGTV1-Z-C-S29",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T10:35:00Z",
    "one_line": "BA's timeline day route TIMES OUT on every call since 10:14:25Z (Sandbox.Timedout at 29.00 s, 3 of 3 of this seat's invokes; CloudWatch 0 timeouts in 694 invocations 05Z-09Z) -- Sept 8 is BA's coverage-event day, the link the page invites a reader to press at the demo; the read path loads silver prefixes (bbg 622 parts / 85 MB, wsj 396 / 76 MB) that a cold container cannot read in 29 s, and each timeout kills the sandbox so the warm cache never forms.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lambda invoke opal-amgt-scoped-api /api/scoped/amgt/security/BA_US_Equity/timeline/day/2026-09-08 (x2) and /2026-09-03, ~10:3xZ: FunctionError Unhandled, Sandbox.Timedout 'Task timed out after 29.00 seconds'; REPORT Duration 29000.00 ms Status: timeout, Max Memory Used 408 MB of 1769.",
        "CloudWatch /aws/lambda/opal-amgt-scoped-api, last 8 h, filter '\"Status: timeout\"' (3 pages): 5 timeouts, first 10:14:25Z; filter 'REPORT' (3 pages): 763 invocations -- 05Z 103, 06Z 20, 07Z 298, 08Z 118, 09Z 155 with 0 timeouts; 10Z 69 with 5.",
        "lambda get_function_configuration: Timeout 29, LastModified 2026-10-02T07:45:38Z (no deploy since).",
        "S3 opal-data-harvest silver article prefixes: bloomberg 622 parts 85.0 MB (1 part after 08:49Z); wsj 396 parts 76.3 MB; ft 92 parts 4.0 MB; barrons 35 parts 2.7 MB.",
        "lib/research/harvest/timeline_api.py:324 get_timeline_day; lib/research/harvest/publication_gold.py:915 (the day route's read path)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-5: a covered company's story along a timeline, articles and events readable; the walks of 07:28Z and 08:49Z served BA's Sept 8 day.",
    "world_is": "Since 10:14Z every BA day request times out on the deployed function; the page's coverage-event link opens to a failure.",
    "notes": "Disarm (owner's lane: the timeline read path, HARVST code on RESAPP's function): make the day route answer cold inside 29 s, e.g. read the day's rows from the served gold mention table (one part, 14,375 rows) instead of whole silver prefixes, or bound the silver read to the day's partition. Raising the Lambda timeout does not help behind a 29 s gateway. Before 13:00Z, at least a warm-up that succeeds, or the coverage-event link shown only when the day answers."
  }
]
```

-- 3.0.0_SA_CVO~Z
