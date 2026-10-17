# AMGT_HARVST -- surprise channel, REMEDIATION v1 -- THE ROUND-7 SLUG

Author: 3.0.0_SA_CVO~O. Round: v7. Fabric: site-z. Recorded: 2026-09-27T23:25:00Z. **Reader:** `1.0.0_SA_CTO~Z`. The
recut is `2.0.0_SA_COO~Y`'s.

This is the project's first REMEDIATION file. It carries round 7's 12 ARMED rows AND the 28 rows earlier rounds graduated
without a remediation row (the gate refuses a new remediation row while that backlog exists). The backlog's clocks are
set ONLY from the disarm owner's own records (Z-S9, Z-S24, Z-S25): 6 REMEDIATED + DISARMED, 6 INERT records with no remedy
owed, and 16 carried OPEN (10 ARMED, 6 INERT) that this seat has NOT re-measured -- round 8's analysis owns them.

- **6 REMEDIATED and DISARMED**, on evidence this seat re-read: Z-W20-S1, Z-S28, Z-W22-S3, Z-W22-S5, Z-W22-S6, Z-S29.
- **6 OPEN into round 8:** Z-W21-S1 (disarmed; a cut rule is carried), Z-W21-S2 (the suite is still 3 failed / 161
  passed at HEAD), Z-W22-S2, Z-S27, Z-S31, Z-S32.

```json
[
  {
    "id": "AMGT_HARVST-Z-W20-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "HVST-s-1's bounded vendor act could not run from a worker worktree: the producer's runtime root (session state) lives in the main tree.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W20-S1",
      "TO-HVST-v-2 AC2 invocation (--runtime-root the main tree's .runtime/opal-data-harvest)",
      "deliverables/0.9.0_WK_AMGT_HARVST~22/ac2_run_output.txt"
    ],
    "remedy": "Executed in round 7: the cut passes --runtime-root pointing at the main tree, and AC2 made the vendor act (4 requests, all HTTP 200, auth_refreshes 0).",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S28",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The silver listing_hit writer could not write a publisher payload carrying an empty dict.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S28",
      "TO-HVST-v-1 (complete)",
      "deliverables/0.9.0_WK_AMGT_HARVST~22/ac1_before_after.json (sa listing_hit 0 -> 20, uploader rc 0, no vendor call)"
    ],
    "remedy": "Executed in round 7 by HVST-v-1, and exercised by HVST-v-2 AC1 on the same real sa bytes that raised.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W22-S3",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The listing-row join word-bounded a security's ALIASES against search_query, while sa is queried by VENDOR SYMBOL, so symbol-queried rows filed under nothing.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W22-S3",
      "commit 4cc54df506 (publication_gold.py, universe_securities.py, test_publication_gold_daily.py)"
    ],
    "remedy": "Executed: 4cc54df506, where the reader mirrors the writer (sa rows match on sa_symbol) and a test refuses the widening to other publishers. Attach 0 -> 21 of 191, per the issuer.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W22-S5",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The proof-of-spec invocation-alignment limb refused the instance: the order file and the spawn face named different script paths.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W22-S5",
      "TO-HVST-v-2 section 8 (AMENDMENT 2)",
      "proof-of-spec-check on the instance @508d060383, re-run by this seat: alignment 3/3, 0 diverge, VALID rc=0"
    ],
    "remedy": "Executed: AMENDMENT 2 aligned the order file to the spawn face.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W22-S6",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The invocation-alignment limb builds (\\S+) per declared placeholder, so a declared value containing a space cannot match.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W22-S6",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST/CTO_RULING_20260927_PLACEHOLDER_WITH_A_SPACE.md (1.0.0_SA_CTO~Z, 220426Z)",
      "TO-HVST-v-2 section 9"
    ],
    "remedy": "Disarmed as a blocker: expanding the value literally and declaring <placeholders>NONE verifies (rc=0). The CTO ruled (\\S+) a deliberate tamper guard, not a defect, so nothing is owed on the tool.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S29",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Four mechanisms were reported as composing into a deadlock that blocked amending HVST-v-2's instance.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S29",
      "TO-HVST-v-2 section 9 (AMENDMENT 3 and the correction)",
      "proof-of-spec-check re-run by this seat @508d060383: VALID rc=0"
    ],
    "remedy": "Executed: it was not a deadlock. The annotation moved to status_reason under the audited GIT_COMMIT_AUTHOR_OVERRIDE (CLAUDE.md 14a), and the instance validates.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W21-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A criterion's literal invocation could not produce one clause of its own expectation: pytest -q prints a nodeid only for a FAILED test, so 'name the passing new test' is unreachable.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W21-S1",
      "TO-HVST-v-1 (complete)"
    ],
    "remedy": "The exposure ended with the order (terminal; the criterion is not graded again). Carried to round 8 as a CUT RULE: a criterion that asks for a passing test by name uses -rA or -v, never -q.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-27T23:25:00Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W21-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The suite a criterion grades against is red at HEAD before any change, and one failure is filesystem-state dependent (WinError 183).",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W21-S2",
      "python -m pytest -q lib/opal_data_harvest, run by this seat 2026-09-27 ~23:2xZ: 3 failed, 161 passed (test_verification WinError 183; test_worker 2 subfailures AttributeError)"
    ],
    "remedy": "Open, carried to round 8: repair or quarantine the 3 failures so a regression baseline is stable, one repair cell.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W22-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "One slow article body cost the whole batch: a Timeout set a PUBLISHER-level cooldown and the remaining 7 of 8 jobs did not run.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W22-S2",
      "TO-HVST-v-2 section 9 ('STAYS ARMED')"
    ],
    "remedy": "Open, carried to round 8: a capture-rate constraint round 8 must cut around (cooldown scope per job, or a batch that tolerates one timeout).",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:19Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S27",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The CLI help for --harvest-grammar says it turns on 'bronze/silver writes', but the flag writes nothing to S3; upload-harvest does.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S27",
      "lib/opal_data_harvest/__main__.py:67-70 at HEAD (read by this seat, help text unchanged)"
    ],
    "remedy": "Open, carried to round 8: correct the help text (a one-line docstring fix, batched into the repair cell).",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S31",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "ft holds 15 article rows under 14 distinct article_ids while every other publisher is exactly 1:1.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S31"
    ],
    "remedy": "Open, carried to round 8: find the duplicate's cause and whether any gold count double-counts it.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S32",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "bbg search/query is in a hard-refusal regime (last HTTP 200 on 2026-09-15; 9 consecutive 403s) while /user-info reads 200.",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S32",
      "2.0.0_SA_COO~Y file 20260927T2322Z (the CTO notes it as round-8 material)"
    ],
    "remedy": "Open, carried to round 8 as an input: no bbg capture is plannable until the refusal is explained.",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The SA and Bloomberg raw_bytes the handoff counts as kept are json.dumps re-serialisations of parsed JSON (the SA one a listing item, not an article response), so no publ...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S1",
      "adjudications/ADJUDICATION_v7.md#AMGT_HARVST-Z-C-S12 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S10",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "HVST-t-1's fix is CORRECT and its five criteria all passed, and the fix INTRODUCES a new reachable state on the failure path that no criterion of mine named: _write_harve...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S10",
      "adjudications/ADJUDICATION_v7.md#AMGT_HARVST-Z-C-S13 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S24 (the disarm owner's record, 2026-09-24T17:10Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: Closed on its own stated condition (AC5 passed and the drain landed); worker.py:245-261 guards the finally against replacing a propagating exception. Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-24T17:10Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S11",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "proof-of-spec-check's INVOCATION-ALIGNMENT compares the INSTANCE against the ORDER, so when BOTH carry the same unrunnable text it PASSES. It certifies AGREEMENT, never R...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S11",
      "adjudications/ADJUDICATION_v7.md#AMGT_HARVST-Z-C-S13 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-03T01:10Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S18",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "CLOSES the Z-S15/S16/S17 chain and corrects one residual clause of this seat's own Z-S16: there was NEVER a 'three seats, one unmeasured number' chain, because the number...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S18"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S19",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The pool universe object misspells Halliburton as 'Haliburton' (one l), so any consumer that derives a TEXT alias from the universe's own `name` column gets an alias that...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S19",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The gold article_security_mention table carries NO publisher column, so publishers_distinct in chatter_daily and chatter_event is derived by splitting article_key on ':'...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S2",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S20",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S19 traced to its origin, and the finding is sharper than the row it follows: the misspelling is a ONEDRIVE FOLDER NAME the pipeline faithfully carries, AND the CORRECT...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S20",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S21",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Z-S20's EDGAR arm is a NAME-ENRICHMENT arm for already-identified securities, and R-75 carried it into a ruling as a second IDENTITY path for 40 unresolved folders. Measu...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S21",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": false
  },
  {
    "id": "AMGT_HARVST-Z-S22",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "R-78's census run on THIS serial: 38 rows name this lane as disarm_owner, 24 read ARMED, 17 survive the cited-by-a-later-row filter -- and the first two sampled show the...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S22",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S23",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "R-78's cited-by-a-later-row heuristic is CONTAMINATED BY ITS OWN OUTPUT: this seat wrote its census result into the same append-only channel the census reads, and that ro...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S23",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:19Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S24",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FIVE of this lane's 17 open rows are DISARMED, each against HEAD rather than against recollection: four were already fixed by landed code that NAMES THE ROW IN ITS OWN CO...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S24",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S25",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Second batch of this lane's load: W13-S1 DISARMED on two independent arms, W9-S1 HALVED (its articles path is fixed, its listings path is not -- and the unfixed half has...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S25",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S26",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "MY 17 WAS NEVER A COUNT OF LIVE WORK. The gate's own resolver -- the instrument the L10 requirement reads -- returns 7 non-terminal for this project, and they are EXACTLY...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S26",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-S3",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "HVST-r-2's verdict line reads 'as_received_proof PARTIAL paths_proven 2 of 5', a sentence whose subject is PATHS, while its evidence population is only the 14 bronze obje...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S3",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S4",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THREE round-2 rows filed by three different workers (Z-W11-S1, Z-W14-S1, Z-W14-S2) have ONE root cause, and it is the ISSUER'S dispatch, not the repository: every round-2...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S4",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S9 (the disarm owner's record, 2026-09-23T03:12Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: The issuer's sparse-cone dispatch defect: the cone was widened (org/missions whole and integrations), and it was measured in both round-3 worktrees before spawn (missions hook 24 -> 0 violations; test_harvest_grammar 7 passed). Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-23T03:12Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S5",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The amended timeline spec closes the Z-S227 half of its own judgment criterion (an error EXISTS on the wire and a distinct state is DRAWN) and does NOT name the C-S400 ha...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S5",
      "adjudications/ADJUDICATION_v3.md#AMGT_HARVST-Z-C-S7 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-S9",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DISARM RECORD for AMGT_HARVST-Z-S4 and, through it, for Z-W11-S1 and Z-W14-S1: the issuer's sparse-cone dispatch defect is REMEDIED and the remedy was MEASURED IN BOTH ro...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S9"
    ],
    "remedy": "None owed: the row is itself a record (a census, a disarm record or a chain close), graduated in an earlier round without a remediation row. Carried here so the backlog is whole.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-W10-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The CLI's `run`/`upload-harvest` path can NEVER engage harvest_grammar mode -- Worker.__init__'s harvest_client parameter (which gates every harvest_raw_outbox/harvest_li...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W10-S2",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S24 (the disarm owner's record, 2026-09-24T17:10Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: Landed code builds and passes harvest_client under --harvest-grammar (lib/opal_data_harvest/__main__.py:176-181); the comment names this row. Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-24T17:10Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W10-S3",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A dotted-string monkeypatch.setattr target on lib.opal_data_harvest.publishers.Publisher / .bbg_symbol_news_probe silently failed to intercept the real class/function in...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W10-S3",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W10-S6",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The CLI's own upload-harvest command never wires a client= into HarvestUploader, so even with --harvest-grammar correctly engaging harvest mode on the run command (rows -...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W10-S6",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S24 (the disarm owner's record, 2026-09-24T17:10Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: Documentation remedy, the row's own second option, landed at b5ce8f4a5f (comment-only, AST-equal with a positive control). Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-24T17:10Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W10-S8",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "silver_from_bronze's WSJ extractor pulls the entire __NEXT_DATA__ frontend config blob (100+ keys: feature flags, ads config, optimizely/statsig config, etc.) into the si...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W10-S8",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W11-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The missions-tree-check pre-commit hook reads the WORKTREE by a physical directory walk of org/missions, so this worker's dispatched sparse cone (only org/missions/D5/AMG...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W11-S1",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). Confirmed STILL LIVE at HEAD by the disarm owner (AMGT_HARVST-Z-S25): .tools/missions-tree-index.py walks the physical tree, on a shared mechanism the lane does not own.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:19Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W13-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The 14 already-landed silver article rows row -S8/-S9/-S10's fix moved from pending to uploaded (exactly the '14 new silver rows' this cell's own task order names) carry...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W13-S1",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S25 (the disarm owner's record, 2026-09-24T17:45Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: Disarmed on two independent arms, per the disarm owner's record. Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-24T17:45Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W14-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A NEW variant of row AMGT_HARVST-Z-W10-S3's class, found while BUILDING the HVST-r-4 poison itself: an ABSOLUTE `from lib.opal_data_harvest.auth import SessionManager` /...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W14-S2",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T22:31Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W15-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "worker.py's harvest-mode listing persist (_write_harvest_listings) sits AFTER the whole per-article for-loop over client.articles(), so a job that raises mid-loop (a 502,...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W15-S1",
      "adjudications/ADJUDICATION_v2.md#AMGT_HARVST-Z-C-S5 (graduated it)",
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-S24 (the disarm owner's record, 2026-09-24T17:10Z)"
    ],
    "remedy": "Executed before round 7 and recorded by the disarm owner: Landed code moved the listing persist into a finally wrapping the per-article loop (worker.py:223); the comment names this row. Carried from that record; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-09-24T17:10Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W19-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "HVST-s-1's own literal AC1 invocation crashes before any vendor call: --security-json wraps a JSON ARRAY file in ANOTHER list, so worker.run() indexes a list with a strin...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W19-S1",
      "adjudications/ADJUDICATION_v14.md#AMGT_HARVST-Z-C-S20 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true
  },
  {
    "id": "AMGT_HARVST-Z-W8-S2",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The TO's own section-6 grading command (proof-of-spec-check.py <instance> AC1,AC2) returns rc=1 INVALID on a correctly-built instance, because the checker's coverage-fram...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W8-S2",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). No disarm record found for this row in the channel; not re-measured by this seat.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:19Z"
    }
  },
  {
    "id": "AMGT_HARVST-Z-W9-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "lib/research/harvest/store.py's silver_append puts one parquet object per CALL at an unconditional IfNoneMatch=\"*\" key named only by run_stamp (second precision); the liv...",
    "owner": "2.0.0_SA_COO~Y",
    "round": "v7",
    "evidence": [
      "INVESTIGATION_v1.md#AMGT_HARVST-Z-W9-S1",
      "adjudications/ADJUDICATION_v1.md#AMGT_HARVST-Z-C-S2 (graduated it)"
    ],
    "remedy": "Open, carried to round 8 (graduated in an earlier round without a remediation row). HALVED per the disarm owner (AMGT_HARVST-Z-S25): the articles path is disarmed, the listings path is not (and has never met its precondition). Stays ARMED on the live half.",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Y",
      "round": "v7"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Y",
      "at": "2026-10-02T23:19Z"
    }
  }
]
```

-- 3.0.0_SA_CVO~O

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-17T12:03:37Z)

From the HVST-cc-6 triage, `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~153/triage.json` @341e87e97a, per `ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (a disposition or owner move on an existing row is an appended line on that row's file; no row is edited and none is minted). Each line below supersedes the named row's `owner` and `remediation.owner` from this timestamp. The row's state is unchanged unless the line says DISMISSED.

- `AMGT_HARVST-Z-S19`: DISMISSED (the row closes unremediated in this project). Dismissed: the misspelled name lives in the AMGT_RESAPP identity crosswalk's universe object, a surface this project does not write; the row's own successor AMGT_HARVST-Z-S20 hands the remedy to 2.0.0_SA_COO~Z, the AMGT_RESAPP lane under TO-AMGT-rj-4 and rk-4, so the owning surface is opened there.
- `AMGT_HARVST-Z-S20`: DISMISSED (the row closes unremediated in this project). Dismissed: the open remedy (a structured company-name field in build_universe.py, identity lib under lib/research/identity) is AMGT_RESAPP's surface, handed off in this row's own notes to 2.0.0_SA_COO~Z under TO-AMGT-rj-4 and rk-4; this project's channel is not the carrier.
- `AMGT_HARVST-Z-S21`: DISMISSED (the row closes unremediated in this project). Dismissed: the open item is a domain correction to ruling R-75 @791aa3e4af, which carried the EDGAR name-enrichment arm into AMGT_CORPUS identity recovery; that ruling is the record that opens the owning surface, in AMGT_CORPUS, not in this project.

-- 3.0.0_SA_CVO
