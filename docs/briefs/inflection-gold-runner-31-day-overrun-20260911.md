# The inflection gold runner ran for 31 days, and every control that should have stopped it reported success

**2026-09-11 · `0.0.0_AB_MSTR` · ad-hoc investigation on Andrew's question: "why are the inflection
boxes costing so much, do we have duplicate pipelines"**

**Answer: no duplicate pipeline.** One `c6a.4xlarge` never turned off, for 31 days, while accumulating
135 stuck processes. The box was stopped tonight on Andrew's word. **The cost is stopped; the two
mechanisms that produced it are not.**

---

## 1. What was measured

| | |
|---|---|
| instance | `inf-gold-layer-runner`, `i-0ed5afded2ebd4ed4`, **`c6a.4xlarge`** (16 vCPU) |
| running since | **2026-08-11T05:14:20Z** — 31 days 13 hours at time of stop |
| stuck processes | **135** `orion-gold-dispatch.sh`, oldest started 05:14:51 on 11 Aug — 37 seconds after boot |
| CPU trend | 23.6% → 35.5% average over the 7 days to 11 Sep, **rising every day, no plateau** |
| load / memory | load avg 6.3 on 16 vCPU; 27 GB of 30 GB free — **a stuck-process problem, not resource exhaustion** |

**Process breakdown:** 68 `--chain full`, 33 `--single INF_API_SILVER_ASSETS_V2`, 33 `--single
INF_API_PULL_ASSETS_V2`, 2 other. Roughly **4.4 accumulating per day**.

⚠ **COST IS DERIVED, NOT BILLED.** `c6a.4xlarge` on-demand us-east-1 is ~$0.61/hr, so 31 days is
**~$450, continuing at ~$440/month**. This is instance-type × uptime arithmetic. **Cost Explorer was
not read.** Treat as order-of-magnitude.

---

## 2. ⛔ The watchdog did not fail. It worked exactly as written, and that is the defect.

`infra/aws/ec2/inf-gold-layer-runner/watchdog-shutdown.sh` runs every 5 minutes and shuts the box down
when no gold activity is seen. Its activity test:

```bash
GOLD_REGEX="orion_gold_scripts/|orion-gold-dispatch"
if pgrep -f "$GOLD_REGEX" >/dev/null 2>&1; then
    echo "$NOW_EPOCH" > "$LAST_GOLD_FILE"
    log "SKIP: gold process running (stamped last-sighting)"
    exit 0
fi
```

>> **THE STUCK PROCESSES ARE THE ONES THE WATCHDOG WATCHES FOR.** They are not invisible to it — they
   are its **proof of life**. Every cycle it saw 135 hung dispatchers, concluded work was in progress,
   and correctly skipped shutdown. **The worse the pileup got, the more certain the watchdog became
   that it must not intervene.** <<

Its own log, read live, shows that decision repeating to 18:14 on 11 Sep:
`SKIP: gold process running (stamped last-sighting)`.

⛔ **THE WATCHDOG HAS NO CONCEPT OF DURATION.** It asks *"is a gold process alive"*, never *"has one
been alive too long"*. It was built to catch an **idle** box. **A hang defeats it completely and
silently**, and a hang is the failure that actually costs money.

⚠ **`Type=oneshot` with `TimeoutStartSec=7200` did not help either.** The boot service reports
`Result=success`, `ActiveState=inactive`, having finished on 11 Aug. **The dispatchers outlived their
own parent unit.**

---

## 3. ⛔ The boot script's job is to DELETE the safety net

`run-gold-layer.sh`, pulled fresh from S3 on every boot, does not merely pause the watchdog:

```bash
sudo systemctl stop watchdog-shutdown.timer
sudo systemctl stop watchdog-shutdown.service
for _D in /etc/systemd/system /run/systemd/system /usr/lib/systemd/system /lib/systemd/system; do
    sudo rm -f "$_D/watchdog-shutdown.timer"
    sudo rm -f "$_D/watchdog-shutdown.service"
done
```

**It removes the unit files from four directories.** Stated reason: *"prevent automatic shutdown
before SSM RunCommand arrives."* So the sanctioned boot path **deliberately disarms the only
automatic stop** and then waits for work to be pushed to it.

⚠ **AND THIS CONTRADICTS A LIVE MEASUREMENT, WHICH IS NOT RESOLVED HERE.** The boot script deletes the
watchdog, yet on 11 Sep the timer read **`active`** and was logging every 6 minutes. **Either the
deletion failed, or something re-installed it after 11 Aug.** Not investigated. Stated rather than
smoothed, because the answer changes which control is trustworthy.

---

## 4. ⛔ The sanctioned trigger is OFF. Two unsanctioned senders fire daily.

`comp-trigger inf-gold-trigger` — **all three EventBridge rules DISABLED**:

| rule | schedule |
|---|---|
| `inf-canonical-prices-daily` | `cron(47 14 * * ? *)` |
| `inf-gold-incremental-daily` | `cron(0 18 * * ? *)` |
| `inf-gold-full-on-bronze-complete` | event-pattern (bronze complete) |

comp-trigger notes DISABLED may be a deliberate hold, in which case **the control is working**.

**But the work arrived anyway.** SSM command history for this instance, every day since at least
1 September, from **two senders that bypass EventBridge entirely**:

```
mode=full source=aggregator lock_run_id=lock-full-<hash>     (daily)
assets_v2 daily chain 2026-09-NN (AUDIT-008.PERM)            (daily)
```

⭐ **The boot script states the split itself:** *"this script does NOT dispatch chains autonomously.
Lambda (inf-gold-trigger) starts the EC2 then dispatches via SSM RunCommand."* The Lambda's triggers
are disabled — **so these SSM RunCommands did not come from the sanctioned path.**

⛔ **AND EVERY ONE REPORTS `Success`.** SSM `Success` means the command was **delivered and started**,
never that the work **finished**. A dispatcher that hangs forever still reads Success. **That is the
second control reporting health over a failure.**

---

## 5. A third instrument disagrees with itself

Today's run wrote both of these, 11 seconds apart:

```json
gold/meta/pipeline-failed.json        {"chain":"full","failed_at":"2026-09-11T12:43:44Z","exit_code":1}
gold/eclipse/_meta/dispatch_eclipse_status.json
                                      {"overall":"ok", "results":"...ok ...ok ...ok",
                                       "chain_exit":1, "completed_at":"2026-09-11T12:43:55Z"}
```

>> **The status summary reads `overall: ok` while carrying `chain_exit: 1` inside itself.** Anything
   reading the summary sees success. Anything reading the failure marker sees failure. **Same run,
   same second, opposite verdicts.** <<

---

## 6. ⭐ What is NOT wrong — stated because the obvious theories were checked and killed

**The gold layer is NOT dead.** Today's outputs landed 12:41–12:43 on 11 Sep: canonical performance
through 2026-09-11, Eclipse model portfolios, `gold_complete.json`. **Most dispatchers complete
normally**; a minority hang and are never reaped. This is a leak, not an outage.

**There is NO duplicate gold runner.** One of each, serving different pipelines, and the siblings are
all long-stopped: `inf-gold-qa-runner` (since 11 May), `bd-gold-qa-runner` (4 May),
`bd-gold-detail-generator` (17 Feb), `consolidation-gold-runner` (15 Jul). **None is costing compute.**

**The estate is otherwise well-behaved.** Of **33 instances, 30 were stopped**; the ephemeral
start-work-stop pattern is demonstrably working across bd, cot, mdpf, etfs, estate and irpt. One box
running 31 days was a **genuine outlier**, not the house style.

**Duplicates DO exist, but elsewhere:** **8 × `historical-prices-fetcher`** (`t3.xlarge`, launched on
8 separate dates 15 Apr – 1 Jun) and **2 × `seeking-alpha-scraper`**. All stopped, so they cost **EBS
storage only** — real but small, and unexamined here.

---

## 7. What was done tonight

On Andrew's explicit word (*"shut that box off immediately and kill all associated processes"*):

1. **135 processes killed** — all died on a plain `TERM`; `KILL` was never needed. **They were not
   busy with anything they were unwilling to abandon.**
2. **Instance stopped.** Verified: all four inflection instances now read `stopped`.

Everything prior to those two acts was **read-only**.

---

## 8. ⛔ Open, and none of it closed by stopping the box

- **Why `orion-gold-dispatch.sh` never exits.** The two oldest started **37 seconds after boot**,
  which points at something structural in startup rather than data-dependent work. A runtime-hang
  diagnosis already exists at
  `org/tier2_senior/0.4.0_DE_ClientPlatform/logs/2026-07-06/inf_gold_freeze_runtime_hang_diagnosis_reconcile.md`
  and was not read for this brief.
- **Who owns the two SSM senders** (`source=aggregator`, `AUDIT-008.PERM`). **They are still armed.
  Stopping the box does not stop them**, and the next dispatch may start it again.
- **Whether the watchdog deletion succeeded** (§3 contradiction).
- **`canonical-schwab-si2`** — `t3.large`, running **74 days**. May be legitimately always-on; may be
  the same pattern in slower motion. **Not examined.**
- **Cost Explorer** was never read; all figures are derived.

---

## The pattern worth keeping

**Three independent controls all reported health while the failure ran for a month:** a watchdog whose
liveness test was satisfied *by the stuck processes themselves*, an SSM sender that reports `Success`
on delivery rather than completion, and a status writer that prints `overall: ok` while embedding a
failing exit code.

>> **NONE OF THEM MEASURED DURATION OR OUTCOME. ALL OF THEM MEASURED PRESENCE.** A control that asks
   *"is something there"* cannot detect *"the thing there is broken"* — and it fails toward
   reassurance, which is why nobody looked for 31 days. <<
