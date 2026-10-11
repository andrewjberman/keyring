# MDPF_HEALGAP -- round 2 remediations (dell1)

<sweep_watermark>2026-10-11T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T02:45:00Z. Graduated at ADJUDICATION_v2: 9 rows (1 BLOCKING, 8 observations), all disarmed. The round-1 rows in REMEDIATION_v1 stay open with their owners.

```json
[
  {
    "id": "MDPF_HEALGAP-D1-S7",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The satellites producer reads same-day bronze at 07:00Z with no re-attempt, so a day the runner lands after 07:00Z serves a one-day-stale registry; HG-t-5 (FWD-5) is held behind it. Disarmed for round 2 by holding HG-t-5 (the runner still fires 06:00Z) and by ruling (a)'s re-run; the coupling stands.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-S7",
      "aws events: cot-satellites-registry-producer-daily cron(0 7 * * ? *), cot-rebalancer-runner-daily cron(0 6 * * ? *)",
      "CTO batch @6c538a0bfd section D (ruling b)"
    ],
    "remedy": "Round 3 per ruling (b): one scheduled 12:00Z satellites fire keyed on the completion stamp, then HG-t-5's apply. Close when: a day the runner lands after 07:00Z serves the fresh registry from 12:00Z (read on served registry.json as_of), and FWD-5 grades APPLIED.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Four pulls on five schedules lean on a lapsing login with neither FWD-6 answer; pre-existing, not widened by this project. Plus the population drift in D1-C-S15 (a third Schwab SDD master and teams-global-transcripts-pull-hourly, both absent from the census).",
    "evidence": [
      "investigation rows MDPF_HEALGAP-D1-W6-S1, -D1-S6",
      "adjudication row MDPF_HEALGAP-D1-C-S15"
    ],
    "remedy": "Round 3 per ruling (section E): heal cells for bd-asset-dim-pipeline-trigger and astn-wsjft-3am-run; the Schwab pulls either get one of FWD-6's two answers or FWD-6 is amended to admit a named manual exposure (an ENDPOINT change, CVO re-sign). Close when: the census re-sweeps the live denominator and every exposed row carries RECOVERS or NOT-EXPOSED.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S12",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "FWD-3's named-in-advance repair act (repair.py manifest then --execute) has never run in the world; the only same-day heal was the automatic re-attempt, which announces nothing before it fetches.",
    "evidence": [
      "adjudication row MDPF_HEALGAP-D1-C-S12",
      "TO-HG-t6 AC1 stubs, AC2 dry run"
    ],
    "remedy": "One round-3 act: an induced same-day hole (FWD-1's pattern) repaired by repair.py --date <today> printing its MANIFEST before --execute, under its own never-widen pair, read on served bronze (exactly the named feed lands, nothing else changes). Close when: that act's ledger is CLOSED and FWD-3's repair arm grades EXERCISED.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-C-S15",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The FWD-6 census denominator (162, 10-08) is stale against the live estate (164): schwab-canonical-si2-08403355-pull-daily and teams-global-transcripts-pull-hourly are unanswered.",
    "evidence": [
      "adjudication row MDPF_HEALGAP-D1-C-S15"
    ],
    "remedy": "Fold both into the round-3 census re-sweep (D1-W6-S1). Close when: the census names both with an answer and its denominator equals a live recount at the sweep.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-S11",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "dell1's agent principal cannot iam:SimulatePrincipalPolicy on roles it deploys, so every WORLD IAM order on dell1 meets the wall at its verify step.",
    "evidence": [
      "investigation rows MDPF_HEALGAP-D1-S10, -D1-S11"
    ],
    "remedy": "Either extend the dell1 agent principal with iam:SimulatePrincipalPolicy on the roles dell1 deploys, or make the C5a/C5b split standard in the order template. Close when: one of the two is on record and the next dell1 IAM order verifies without an amendment.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-S12",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Act 3's restore chain named two actors on the same box; when it stopped, the induce sat 14h23m until a seat on another device restored it.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-S12",
      "ledger healgap-r2-act3-induced-partial-repair-20261010 (@9dee79a23a)"
    ],
    "remedy": "The half of any later induced act names a restore actor on a DIFFERENT device than the seat that sets the induce, with the ledger path it reads. Close when: the next induced act's half carries it.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S2",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "In the worker environment the native Grep tool fails (ENOENT, uv_spawn rg) and comp-find --all over the worktree exceeds the 120 s Bash bound; the census used git ls-files plus Python scans (same facts, different instrument).",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W6-S2"
    ],
    "remedy": "Box tooling owner provisions ripgrep for worker sessions on dell1 or records the fallback. Close when: Grep runs in a dell1 worker worktree.",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-D1-W6-S3",
    "project": "MDPF_HEALGAP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "TO-HG-t7 told the worker to mint MDPF_HEALGAP-W6-S<k>; the row gate on fabric dell1 requires MDPF_HEALGAP-D1-W6-S<k>.",
    "evidence": [
      "investigation row MDPF_HEALGAP-D1-W6-S3",
      "R2_DRAIN_END_REPORT_DRAFT.md 'For the next cut' (D1-W6-S3)"
    ],
    "remedy": "The issuer's order template names the fabric coordinate in the row-id format. Close when: the round-3 orders carry the D1 form.",
    "owner": "2.0.0_SA_COO~G1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~G1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~G1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_HEALGAP-S1",
    "project": "MDPF_HEALGAP",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The mdpf-daily-runner EC2 (i-02448edb624a7a7cf) still launches daily beside mdpf-gold-lambda; if its staged tree carries the slice script it re-publishes the slice later the same day without the catch-up step (newest assignment date only). Outside this project's ingest layer (C-LAYERS); missed by the round-1 sweep (legacy flat channel).",
    "evidence": [
      "org/surprise_channel/MDPF_HEALGAP/INVESTIGATION_v1.md row MDPF_HEALGAP-S1 (2.0.0_SA_COO~M)"
    ],
    "remedy": "Route to the mdpf-daily-runner owner to confirm whether the runner's tree dispatches the slice, and retire or align it. Close when: the runner's dispatch list is read and either it is retired or its slice run is shown to be a no-op.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v3",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v3"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
