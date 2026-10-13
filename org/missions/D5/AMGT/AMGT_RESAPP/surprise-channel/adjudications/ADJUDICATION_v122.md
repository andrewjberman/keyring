# AMGT_RESAPP -- round 101 L8/L9 adjudication, packet FINAL (dell1)

<sweep_watermark>2026-10-13T14:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T14:00:00Z. L8 packet: 2.0.0_SA_COO~R1 msg 4856,
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101/DRAIN_END_PACKET.md @1dc1c89ed9 (blob c2d327c769, verified).
4 of 4 orders complete. bh-2 read live and resolved by content (C-S106). The two JUDGMENT criteria, bh-3 AC2 and bh-4 AC2, are MET (C-S107, C-S108),
each graded against the order's own AC2 wording, printed in the row. 4 rows swept since v121 (watermark 2026-10-12T05:25Z; 4 of 1081 investigation rows
after it): all dismissed. No BLOCKING or ARMED row is open from this round.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S106",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:00:00Z",
    "one_line": "bh-2 (WORLD, the calendar-rule redeploy) read live and resolved BY CONTENT: CodeSha256 j+j1k5r7IY1ZCh9NijT8GSLaqEL3FhamwT8V3tYofCk=, its zip sha256 equal to it, 408 members; 151 map to merged pin 7da642c1ff (an ancestor of box/dell1 HEAD) and all 151 are byte-equal to its blobs; against bg-3's pin ba22af15f5 the packaged code differs in exactly lib/research/freshness/snapshot.py (64fa354a1e1c, bh-1's), so ONE member differs as the order states; scoped_amgt.py 9f72b58aa87e and dossier.py 7b67bf62afdd unchanged. 'No served byte moved' holds on RA1's compare (deliverables/0.7.0_AE_CloudOps~RA1/BH2_POST_APPLY_COMPARE_20261013.json): 527 requests, status moved none, missing none, function errors 0, 36 changed paths all clocks (generated_at, read_at), non-clock 0, outside the table 0; warm max 23.0 -> 2.87 s. This seat at 13:53Z: r101_snapshot_equal.py YES (302 against 302, differing 0), r101_snapshot_rule_check.py YES, test_freshness_snapshot.py 18 passed. bh-1 (LOCAL) is covered by the same blob and runs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "bh-2 (WORLD, the calendar-rule redeploy) read live and resolved BY CONTENT: CodeSha256 j+j1k5r7IY1ZCh9NijT8GSLaqEL3FhamwT8V3tYofCk=, its zip sha256 equal to it, 408 members; 151 map to merged pin 7da642c1ff (an ancestor of box/dell1 HEAD) and all 151 are byte-equal to its blobs; against bg-3's pin ba22af15f5 the packaged code differs in exactly lib/research/freshness/snapshot.py (64fa354a1e1c, bh-1's), so ONE member differs as the order states; scoped_amgt.py 9f72b58aa87e and dossier.py 7b67bf62afdd unchanged. 'No served byte moved' holds on RA1's compare (deliverables/0.7.0_AE_CloudOps~RA1/BH2_POST_APPLY_COMPARE_20261013.json): 527 requests, status moved none, missing none, function errors 0, 36 changed paths all clocks (generated_at, read_at), non-clock 0, outside the table 0; warm max 23.0 -> 2.87 s. This seat at 13:53Z: r101_snapshot_equal.py YES (302 against 302, differing 0), r101_snapshot_rule_check.py YES, test_freshness_snapshot.py 18 passed. bh-1 (LOCAL) is covered by the same blob and runs.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO lambda get-function + package download 2026-10-13T13:5xZ; per-member git blob hash vs git ls-tree -r 7da642c1ff: 151 of 151 equal",
        "git diff --name-only ba22af15f5 7da642c1ff -- lib/ infra/aws/lambda/research/scoped_amgt_api/ (non-test): lib/research/freshness/snapshot.py only",
        "deliverables/0.7.0_AE_CloudOps~RA1/BH2_POST_APPLY_COMPARE_20261013.json",
        "3.0.0_SA_CVO ran deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_equal.py and r101_snapshot_rule_check.py: YES x2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "bh-2 (WORLD, the calendar-rule redeploy) read live and resolved BY CONTENT: CodeSha256 j+j1k5r7IY1ZCh9NijT8GSLaqEL3FhamwT8V3tYofCk=, its zip sha256 equal to it, 408 members; 151 map to merged pin 7da642c1ff (an ancestor of box/dell1 HEAD) and all 151 are byte-equal to its blobs; against bg-3's pin ba22af15f5 the packaged code differs in exactly lib/research/freshness/snapshot.py (64fa354a1e1c, bh-1's), so ONE member differs as the order states; scoped_amgt.py 9f72b58aa87e and dossier.py 7b67bf62afdd unchanged. 'No served byte moved' holds on RA1's compare (deliverables/0.7.0_AE_CloudOps~RA1/BH2_POST_APPLY_COMPARE_20261013.json): 527 requests, status moved none, missing none, function errors 0, 36 changed paths all clocks (generated_at, read_at), non-clock 0, outside the table 0; warm max 23.0 -> 2.87 s. This seat at 13:53Z: r101_snapshot_equal.py YES (302 against 302, differing 0), r101_snapshot_rule_check.py YES, test_freshness_snapshot.py 18 passed. bh-1 (LOCAL) is covered by the same blob and runs."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S107",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:00:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-bh-3.read-the-cold-first-overlay-on-the-live-function-with-a-fresh-snapshot AC2: MET. The reading states only what its numbers show: this seat's log re-run reproduces each figure (cold 20049.86 ms with init 686.71 ms, warm 594.71 ms, 1 prior invocation), and the reading draws no cause, no lever verdict and no comparison with the pre-Monday figure, naming what one request pair cannot show. The packet's '2.3 s' comes from one request on each side and is the issuer's, not the reading's. Unread: the client side and per-phase timing; the gateway, function-URL and bucket logs do not exist (measured).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Criterion wording (the order's own text; the <criterion id=\"AC2\" judgment=\"true\"/> tag carries none): 'AC2 is the CVO's judgment (the reading states only what the numbers show).' This seat's re-run from the function log: the cold probe is request d6d9ce24-c675-45de-8389-b74317dbb3bc, REPORT 2026-10-12T12:41:31.793Z, duration 20049.86 ms, init 686.71 ms; the next request 7bb5a02f.. at 12:41:32.518Z, 594.71 ms, no init (warm); REPORT lines in 12:26:04Z-12:41:04Z: 1 -- each equal to the reading (20.05 s cold, init 686.71 ms; ADBE 0.59 s warm; 1 invocation in the preceding 15 minutes). r101_snapshot_equal.py re-run now reads YES (302 against 302, differing 0, the 12:30Z write of 2026-10-13), consistent with the reading's after-amendment line. What the reading claims: the numbers and the verdict lines, and it names what they do not show (one pair is not a rate; the counted invocation is not identified; the day's logs are bh-4's). What it does NOT claim, correctly: no comparison with the pre-Monday 22.39 s, no 'snapshot is or is not the lever' verdict, no route or phase for the 20 s. The packet's 'the snapshot buys about 2.3 s' is the issuer's inference from one cold request on each side (n = 1 against n = 1), not the reading's. Surfaces not read: the client side (the script prints a wall time of 22.03 s, so the client's own latency is unread beyond that one figure), the API gateway access log, the function URL log and the bucket request log (the last three do not exist on this stack: measured), and any per-phase timing inside the handler (none is logged; round 102's first cell). None of them could change what the reading states, since it states no cause.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_RESAPP~399/BH3_COLD_LIVE_OUTPUT_20261012.txt (read whole)",
        "3.0.0_SA_CVO Logs Insights + CloudWatch metric re-run 2026-10-13T13:4xZ (session scratch r101_repro.py)",
        "3.0.0_SA_CVO 2026-10-13T13:5xZ: apigatewayv2 stage $default AccessLogSettings None; lambda get-function-url-config ResourceNotFoundException; s3 get-bucket-logging opal-data-harvest None"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-bh-3.read-the-cold-first-overlay-on-the-live-function-with-a-fresh-snapshot AC2: MET. The reading states only what its numbers show: this seat's log re-run reproduces each figure (cold 20049.86 ms with init 686.71 ms, warm 594.71 ms, 1 prior invocation), and the reading draws no cause, no lever verdict and no comparison with the pre-Monday figure, naming what one request pair cannot show. The packet's '2.3 s' comes from one request on each side and is the issuer's, not the reading's. Unread: the client side and per-phase timing; the gateway, function-URL and bucket logs do not exist (measured)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S108",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:00:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-bh-4.read-the-first-weekday-of-the-s3-client-build-from-the-function-log AC2: MET. The counts follow from the queries (this seat reproduces 625 / 1 / 6 / 0 / 3 lines / 16 minutes over the fixed window), the splits sum, no route is inferred, and the rate comparison is stated as not distinguishable. The silence the reading could not explain is closed here by the Invocations metric by hour (no invocation from 14Z on 10-12 to 11Z on 10-13): no traffic reached the function, nothing was lost, and the window's one slow run is bh-3's own probe. Unread: the client side; the gateway, function-URL and bucket logs do not exist (measured).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Criterion wording (the order's own text): 'AC2 is the CVO's judgment (the counts follow from the queries, the splits sum, no route is inferred, the rate comparison is stated).' This seat's re-run over the reading's fixed window 2026-10-12T12:40Z..2026-10-13T12:40Z: REPORT 625; over 20 s 1 (d6d9ce24.., 20049.86 ms, init 686.71 ms, 385 MB); cold among all 6; invocations carrying the pool-full warning 0 (the query returns an empty result); lines of d6d9ce24 3; non-empty minutes 16 -- each equal to the reading. The splits sum (over 20 s 1 = attributed 0 + unattributed 1; pool-full 0 + no pool-full 1). No route or name is inferred (3 lines, START, END, REPORT). The rate comparison is stated (1.60 against 1.63 per 1,000 over 20 s, 'cannot be told apart'; the 0-, 1- and 6-counts are said to show no comparison). The one silence question the reading leaves open (no invocation, or lost logs) is closed by the Lambda Invocations metric by UTC hour, read here: 2026-10-12 12Z 308 and 13Z 317, no datapoint from 14Z through 2026-10-13 11Z, 2026-10-13 12Z 1: no invocation reached the function, the logs lost nothing. And the one over-20 s event is bh-3's deliberate cold probe (same request id), so the window held no organic traffic and its rates measure seats' acts, not the build; the reading does not claim otherwise. Surfaces not read: the API gateway access log, the function URL log and the bucket request log (none exists: measured), and the client side; none could change a count from the function's own log.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_AMGT_RESAPP~400/BH4_FIRST_WEEKDAY_READING_20261013.md (read whole)",
        "3.0.0_SA_CVO Logs Insights + CloudWatch metric re-run 2026-10-13T13:4xZ (session scratch r101_repro.py)",
        "3.0.0_SA_CVO 2026-10-13T13:5xZ: apigatewayv2 stage $default AccessLogSettings None; lambda get-function-url-config ResourceNotFoundException; s3 get-bucket-logging opal-data-harvest None"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-bh-4.read-the-first-weekday-of-the-s3-client-build-from-the-function-log AC2: MET. The counts follow from the queries (this seat reproduces 625 / 1 / 6 / 0 / 3 lines / 16 minutes over the fixed window), the splits sum, no route is inferred, and the rate comparison is stated as not distinguishable. The silence the reading could not explain is closed here by the Invocations metric by hour (no invocation from 14Z on 10-12 to 11Z on 10-13): no traffic reached the function, nothing was lost, and the window's one slow run is bh-3's own probe. Unread: the client side; the gateway, function-URL and bucket logs do not exist (measured)."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S109",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:00:00Z",
    "one_line": "D1-W399-S1 (BLOCKING, INERT) and D1-W399-S2 (INERT) dismissed: S1's NO was the issuer's instrument (the packaged list files' deployed path), resolved by bh-3 AMENDMENT 1, and this seat's re-run of r101_snapshot_equal.py reads YES with that path blanked on both sides; S2 is a verdict-wording fact of r101_cold_live.py (NO rather than NOT QUIET when the cold pass misses its 20.0 s gate by 0.05 s), stated in the reading itself.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W399-S1",
      "AMGT_RESAPP-D1-W399-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W399-S1 (BLOCKING, INERT) and D1-W399-S2 (INERT) dismissed: S1's NO was the issuer's instrument (the packaged list files' deployed path), resolved by bh-3 AMENDMENT 1, and this seat's re-run of r101_snapshot_equal.py reads YES with that path blanked on both sides; S2 is a verdict-wording fact of r101_cold_live.py (NO rather than NOT QUIET when the cold pass misses its 20.0 s gate by 0.05 s), stated in the reading itself.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W399-S1, D1-W399-S2",
        "bh-3 AMENDMENT 1 @92c9b10d50",
        "3.0.0_SA_CVO r101_snapshot_equal.py 2026-10-13T13:53Z: YES"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W399-S1 (BLOCKING, INERT) and D1-W399-S2 (INERT) dismissed: S1's NO was the issuer's instrument (the packaged list files' deployed path), resolved by bh-3 AMENDMENT 1, and this seat's re-run of r101_snapshot_equal.py reads YES with that path blanked on both sides; S2 is a verdict-wording fact of r101_cold_live.py (NO rather than NOT QUIET when the cold pass misses its 20.0 s gate by 0.05 s), stated in the reading itself."
  },
  {
    "id": "AMGT_RESAPP-D1-C-S110",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T14:00:00Z",
    "one_line": "D1-W400-S1 and D1-W400-S2 (INERT) dismissed: S1's silent hours are closed by the Invocations metric by hour (C-S108: no invocation reached the function, the logs lost nothing); S2's 29 s gap between the order's apply time and the function's LastModified is the update's completion lag, and both precede the window.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-W400-S1",
      "AMGT_RESAPP-D1-W400-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W400-S1 and D1-W400-S2 (INERT) dismissed: S1's silent hours are closed by the Invocations metric by hour (C-S108: no invocation reached the function, the logs lost nothing); S2's 29 s gap between the order's apply time and the function's LastModified is the update's completion lag, and both precede the window.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows AMGT_RESAPP-D1-W400-S1, D1-W400-S2",
        "adjudication row AMGT_RESAPP-D1-C-S108"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W400-S1 and D1-W400-S2 (INERT) dismissed: S1's silent hours are closed by the Invocations metric by hour (C-S108: no invocation reached the function, the logs lost nothing); S2's 29 s gap between the order's apply time and the function's LastModified is the update's completion lag, and both precede the window."
  }
]
```
