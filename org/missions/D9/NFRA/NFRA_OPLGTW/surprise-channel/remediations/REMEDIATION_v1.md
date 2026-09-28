# NFRA_OPLGTW -- surprise channel, REMEDIATION v1 -- THE ROUND-1 SLUG

Author: 3.0.0_SA_CVO~O. Round: v1. Fabric: laptop (the items' own fabric; this seat writes from site Z). Recorded: 2026-09-28T16:59:50Z. **Reader:** `1.0.0_SA_CTO~O`.

48 rows:
- **16 INERT graduated, OPEN.** Not re-measured unless the row says so.
- **23 ARMED REMEDIATED + DISARMED.** 21 on the disarm owner's own record, plus W2-S7 and S42 measured here.
- **1 ARMED DISARMED with its cleanup OPEN:** S36.
- **8 ARMED OPEN:** W3-S9, S61, W2-S8, S43, S45, W2-S10, S49, S48.

```json
[
  {
    "id": "NFRA_OPLGTW-W3-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Running the Gateway suite appends to the tracked audit.jsonl.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S2"
    ],
    "remedy": "Point the test audit sink at a temp path. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W3-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "tests/test_ratelimit.py replaces time.monotonic process-wide and never restores it, so a whole-suite single-process run hangs (W3-S12).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S6"
    ],
    "remedy": "Scope the patch to the test (monkeypatch) so the suite completes in one process. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W6-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The per-module sweep is non-deterministic: a timing assertion (test_ogq1_ac02, 0.25 s) fails under load.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S9"
    ],
    "remedy": "Make the timing assertion load-tolerant or isolate it from suite criteria. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W3-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Dynamic Client Registrations are stored with no expiry and accumulate without bound.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S5"
    ],
    "remedy": "The contract names a registration lifetime (L4, 1.0.0_SA_CTO) and the store applies it. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W3-S11",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GET /ms/site_children validates its parameter (400) before checking any credential.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S11"
    ],
    "remedy": "Authenticate before validating parameters. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W3-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The browser OIDC routes fall in the fail-open global bucket; AUTH_PATHS (ratelimit.py:42) lists 4 paths only.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S18"
    ],
    "remedy": "Add the browser login and callback paths to AUTH_PATHS. Measured still true here.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W6-S2",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No carrier declares the unique grain of the three datasets, and the real 2026-09-15 dim_position snapshot has colliding (account_id, cusip, l_s) keys.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S2"
    ],
    "remedy": "The contract declares each grain (L4, 1.0.0_SA_CTO), and the served behaviour on a colliding real snapshot is graded. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W5-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The 500-row response cap is counted across both representations, so 250 rows is the effective page.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S6"
    ],
    "remedy": "Count the cap once per row, or state 250 as the page limit. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-S57",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The export materialises the whole result (up to three copies) and raises LIMIT_EXCEEDED after the allocation.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S57"
    ],
    "remedy": "Stream the producer (S59) or refuse before allocating; the R-OG-22 revision is L4 (1.0.0_SA_CTO). Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-S4",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Each 08335338 marker date was PUT ~10 times and each PUT dispatched the whole 49F chain (94 dispatches, 61 lock refusals in 14 days).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S4"
    ],
    "remedy": "OG-c-1's exactly-one-qualified-closure is the named mechanism; measure the dispatch count after it. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The completion burst dispatched the 49F chain before its named silver existed; one lock holder hung to the 3600 s timeout.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S5"
    ],
    "remedy": "Gate the dispatch on the closure's named objects. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W4-S12",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "advi-49f-gold-dispatch classifies a chain terminal by the first SSM output line, so it logged ERROR on a CHAIN OK run.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W4-S12"
    ],
    "remedy": "Route to the dispatcher's owner: classify on the CHAIN terminal line. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "In a linked worktree the halt gate scans a missing inbox root and passes rc=0, so a [STOP] to the issuer would not halt a worker's apply (W1-S7).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S19"
    ],
    "remedy": "Resolve HALT_GATE_INBOX_ROOT to the shared tree, as R-53 did for safe-ec2-deploy.sh. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W4-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "build-and-upload.sh aborts under set -e when a package declares no blobs, before its SKIP branch.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W4-S10"
    ],
    "remedy": "Capture the probe's exit before set -e can abort. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W1-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The naming limb REFUSEs the PRD-fixed role names (3 verdicts, W1-S11); WARN today, exit 7 under ENFORCE.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W1-S9"
    ],
    "remedy": "Registry rows or an R20 departure before LGIC_ENFORCE. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W2-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "8 synthetic probe items (og_i1/og_i5) sit in the production access-state table.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S6"
    ],
    "remedy": "Delete the probe items under an owner's word, and give probes a TTL. Not re-measured by this seat; carried to the round-2 analysis.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_OPLGTW-W3-S1",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S1.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S1",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S2",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S32"
    ],
    "remedy": "Executed: The access-state table's key and TTL attributes are pinned identically by Terraform, the live table and the adapter. Disarm evidence S2, S32 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W6-S3",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S3.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S3",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S34"
    ],
    "remedy": "Executed: The CTO ruled the narrow reading; the catalog makes 0 fact_ calls, enforced by test_ogk1_ac17. Disarm evidence S6, S34 (the owner's own record; not re-measured by this seat).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S7.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S7",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S12",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S30"
    ],
    "remedy": "Executed: OG-a-2's green re-run merged; the named tests pass at HEAD per S30's sweep. Disarm evidence S12, S30 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S13",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S13.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S13",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S11",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S12"
    ],
    "remedy": "Executed: Ruling 97141 re-targeted the three assertions; green re-run merged. Disarm evidence S11, S12 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S16",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S16.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S16",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S15",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S60"
    ],
    "remedy": "Executed: test_oga2_ac04 PASS at HEAD (S60's run). Disarm evidence S15, S60 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S17",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S17.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S17",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S15",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S60"
    ],
    "remedy": "Executed: test_oga3_ac07 PASS at HEAD after both route-adding cells (S60's run). Disarm evidence S15, S60 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S25",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S25.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S25",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S20"
    ],
    "remedy": "Executed: The secret's variable and shape are carried as a bound into OG-i-2 and OG-r-1. Disarm evidence S20 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W1-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W1-S6.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W1-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S18"
    ],
    "remedy": "Executed: The session serial file was provisioned; the halt gate resolves the worker. Disarm evidence S18 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W6-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S5.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S5",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S23"
    ],
    "remedy": "Executed: R-OG-12 fixes RQ1-RQ6 to 2026-09-15, so a newer closure cannot fail a correct Gateway. Disarm evidence S23 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W6-S6",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S6.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S6",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S33"
    ],
    "remedy": "Executed: Additivity and grouping guards are wired on the live path (OG-q-4, OG-q-6). Disarm evidence S33 (the owner's own record; not re-measured by this seat).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W6-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S8.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S8",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S33"
    ],
    "remedy": "Executed: The dim_asset CUSIP restriction is wired (OG-q-5). Disarm evidence S33 (the owner's own record; not re-measured by this seat).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W5-S18",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S18.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S18",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S33"
    ],
    "remedy": "Executed: A guard denial sets MCP isError (OG-z-4). Disarm evidence S33 (the owner's own record; not re-measured by this seat).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S24",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S24.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S24",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S25"
    ],
    "remedy": "Executed: conftest.py reads the role names from the contract; the ARN-class failures are gone. Disarm evidence S25 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S26",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S26.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S26",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S30"
    ],
    "remedy": "Executed: The named test passes at HEAD per S30's sweep. Disarm evidence S30 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W5-S19",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S19.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S19",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S27",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S30"
    ],
    "remedy": "Executed: The pre-wiring assertions were corrected in OG-q-6's re-open (@e58d9d2b04). Disarm evidence S27, S30 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W5-S20",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S20.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W5-S20",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S27",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S30"
    ],
    "remedy": "Executed: As W5-S19. Disarm evidence S27, S30 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W6-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S10.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W6-S10",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S27",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S30"
    ],
    "remedy": "Executed: As W5-S19; the failing module is green at HEAD. Disarm evidence S27, S30 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W2-S5",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S5.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S5",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S29"
    ],
    "remedy": "Executed: The halt-gate identity redirect in safe-ec2-deploy.sh was repaired under R-53 and graded by OGR1-AC15..AC18. Disarm evidence S29 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W2-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S9.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S9",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S28"
    ],
    "remedy": "Executed: og_r1.py ac8() was fixed at 1304801ca6 and graded against the failing case with a mutant. Disarm evidence S28 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S46",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S46.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S46",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S47"
    ],
    "remedy": "Executed: End-to-end login restored (register 201, authorize 307, callback 302, token 200) after the DeleteItem fix. Disarm evidence S47 (the owner's own record; not re-measured by this seat).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S55",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As filed at investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S55.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S55",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S56"
    ],
    "remedy": "Executed: The adopted remedy (the audited override) is consumed as a presence test, so the new owner can write G-C's path. Source-read, not exercised. Disarm evidence S56 (the owner's own record; not re-measured by this seat).",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W2-S7",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The runbook's rollback target (the then-previous deploy 7bd89b5d71) lacked app/data_entitlement.py.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S7",
      "infra/aws/ec2/EC2_MANIFEST.json (deployed_commit 6a98a0553a; prior fe94911257, 110d93fb73)"
    ],
    "remedy": "Overtaken: measured here, the live and the two prior deployed releases all carry app/data_entitlement.py, so a guard-carrying rollback target exists. Runbook 7.2 still says none exists (see Z-C-S11, OGO2-J1).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S42",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The original seal salt lived only in C:/tmp and was lost, so the sealed hashes could not be reproduced.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S42",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S50",
      "commit d5af54a90a (the re-seal)",
      "ssm describe-parameters (names only, no value read) 2026-09-28T16:5xZ: 7 SecureStrings /opal/nfra_oplgtw/ogv4/reseal_20260918/{RQ1..RQ6,SALT}, written 2026-09-18T23:30Z"
    ],
    "remedy": "Executed: re-sealed @d5af54a90a, and the salt and six answers are held in 7 SSM SecureStrings -- measured present here by name. The salt is not lost; OG-v-4 is gradeable when re-cut.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-S36",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three principal_profile records at sk=PROFILE in the live access-state table.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S36",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S37",
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S39"
    ],
    "remedy": "DISARMED: they are OG-i-1's probe fixtures under synthetic keys, and no real principal is named (S37). Removing them is OPEN under W2-S6.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": "2026-09-28T16:59:50Z"
    }
  },
  {
    "id": "NFRA_OPLGTW-W3-S9",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Authorization after the principal guard keys on email: resolve_tier(email) at four production sites, including token_broker.py:143 minting token scopes (S61).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W3-S9"
    ],
    "remedy": "OPEN: re-key tier and allowlist on principal_key -- a security-class design change owned at L4 by 1.0.0_SA_CTO. The forgery controls do not cover re-assignment (S61).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-S61",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "As W3-S9, confirmed at HEAD and wider (a fifth consumer).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S61"
    ],
    "remedy": "OPEN with W3-S9.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-W2-S8",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A Windows-worktree deploy ships CRLF for extensions with no eol rule (9 of 68 files in OG-r-1).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S8"
    ],
    "remedy": "OPEN: measured here, .gitattributes still has no eol rule for .service, .txt, .yaml, .json, .md, .html or .jsonl. Add the rules, or deploy from an LF checkout.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-S43",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "All 16 out-of-repo evidence paths the project cites are absent.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S43"
    ],
    "remedy": "OPEN: the seal inputs are now durable (7 SSM SecureStrings, see S42); the other cited paths (the nfra-oplgtw-handoff tree) are not shown restored. Evidence lives in the repo or a named durable store.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-S45",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "No Elastic IP, so every stop/start moves the Gateway's egress identity.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S45"
    ],
    "remedy": "OPEN: an EIP, or a statement that no allowlist depends on the address. Owner 1.0.0_SA_CTO.",
    "owner": "1.0.0_SA_CTO",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-W2-S10",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "OGR2-AC6's 'zero failures' bar was unsatisfiable on the windows the cell built.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-W2-S10"
    ],
    "remedy": "OPEN: R-OG-23A names 09-11..09-17 (19,473 requests, 0 5xx, S53); regrade in OG-r-2's re-cut.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-S49",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The 5xx behind AC6 were attributable (the S46 outage and 19 graph 502s, S52), not ambient.",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S49"
    ],
    "remedy": "OPEN with W2-S10.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  },
  {
    "id": "NFRA_OPLGTW-S48",
    "project": "NFRA_OPLGTW",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "OGR2-AC2's cap_respected grades a LIMIT_EXCEEDED job as respected without reading its RSS (282,021,888 against 268,435,456).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-S48"
    ],
    "remedy": "OPEN: the instrument repair is draft cell R2-b (@94b0c19f27); the R-OG-22 cap revision is L4 (1.0.0_SA_CTO).",
    "owner": "2.0.0_SA_COO~O",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~O",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": null
    }
  }
]
```

-- 3.0.0_SA_CVO~O
