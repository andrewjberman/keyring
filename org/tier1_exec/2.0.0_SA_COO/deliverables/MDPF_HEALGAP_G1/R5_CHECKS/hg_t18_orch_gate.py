"""MDPF_HEALGAP round 5, HG-t-18 criterion (b): the ASTN orchestrator Lambda gains mode `ft_reattempt` and leaves modes `run`
and `absence_check` as they were. Pure stub test: no AWS call, no sleep (a fake clock), no network.

Handler under test: infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py (override with HG_T18_ORCH).

Contract:
  - {"mode": "run"} and the default: the last SSM command line is EXACTLY
      su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py'
    and the post-success guard reads the digest (one s3 get_object) as before.
  - {"mode": "ft_reattempt"}: the same start / wait-online / send_command / ALWAYS-stop sequence; the last command line is
      su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py --ft-reattempt'
    and, with "dry_run": true, ... python3 run.py --ft-reattempt --dry-run'. On SSM Success it makes NO s3 get_object (the
    main-run "usable brief" guard does not apply to a refill) and raises no alert; on SSM Failed it alerts (SNS publish)
    and still stops the box.
  - the budget-expiry path (status never terminal) leaves the box RUNNING in both modes, as before.
  - {"mode": "absence_check"}: no SSM call, unchanged.
Last line: GATE-OK or GATE-BAD <reasons>. At the base this is GATE-BAD.
"""
from __future__ import annotations

import importlib.util
import os
import sys
import types
from pathlib import Path

ORCH = Path(os.environ.get("HG_T18_ORCH") or "infra/aws/lambda/astn-wsjft-orchestrator/lambda_function.py")
BASE_CMD = "su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py'"
FT_CMD = "su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py --ft-reattempt'"
FT_DRY_CMD = "su - ec2-user -c 'cd /opt/astn-wsjft/scripts && python3 run.py --ft-reattempt --dry-run'"


def main() -> int:
    if not ORCH.is_file():
        print(f"GATE-BAD no handler file {ORCH}")
        return 1
    import boto3
    import time as real_time

    os.environ["ASTN_INSTANCE_ID"] = "i-0000000000000000"
    os.environ["ASTN_SNS_TOPIC"] = "arn:aws:sns:us-east-1:000000000000:astn-test"
    st = {"cmds": [], "starts": 0, "stops": 0, "alerts": [], "s3_gets": 0, "status": "Success", "rc": 0, "ssm_calls": 0}

    class NoSuchKey(Exception):
        pass

    class Ssm:
        class exceptions:
            InvocationDoesNotExist = type("InvocationDoesNotExist", (Exception,), {})

        def describe_instance_information(self, **kw):
            return {"InstanceInformationList": [{"PingStatus": "Online"}]}

        def send_command(self, **kw):
            st["ssm_calls"] += 1
            st["cmds"].append(kw["Parameters"]["commands"][-1])
            return {"Command": {"CommandId": "c-1"}}

        def get_command_invocation(self, **kw):
            return {"Status": st["status"], "ResponseCode": st["rc"], "StandardErrorContent": ""}

    class Ec2:
        def start_instances(self, **kw):
            st["starts"] += 1

        def stop_instances(self, **kw):
            st["stops"] += 1

        def describe_instances(self, **kw):
            return {"Reservations": [{"Instances": [{"State": {"Name": "running"}}]}]}

    class Sns:
        def publish(self, **kw):
            st["alerts"].append(kw.get("Subject"))

    class S3:
        class exceptions:
            pass

        def get_object(self, **kw):
            st["s3_gets"] += 1
            return {"Body": types.SimpleNamespace(read=lambda: b'{"total_articles_out": 3}')}

    S3.exceptions.NoSuchKey = NoSuchKey
    fakes = {"ec2": Ec2(), "ssm": Ssm(), "sns": Sns(), "s3": S3()}
    real_client = boto3.client
    boto3.client = lambda svc, *a, **k: fakes[svc]

    clock = [1_000_000.0]
    real_time_fn, real_sleep = real_time.time, real_time.sleep
    real_time.time = lambda: clock[0]
    real_time.sleep = lambda s: clock.__setitem__(0, clock[0] + float(s))

    bad: list[str] = []
    try:
        try:
            spec = importlib.util.spec_from_file_location("hg_t18_orch_under_test", str(ORCH))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        except Exception as exc:  # noqa: BLE001
            print(f"GATE-BAD handler does not import: {type(exc).__name__}: {exc}")
            return 1

        def reset(**kw):
            st.update({"cmds": [], "starts": 0, "stops": 0, "alerts": [], "s3_gets": 0, "status": "Success", "rc": 0,
                       "ssm_calls": 0})
            st.update(kw)

        def call(event, tag):
            try:
                return mod.handler(event, None)
            except Exception as exc:  # noqa: BLE001
                bad.append(f"{tag}: raised {type(exc).__name__}: {exc}")
                return None

        # A: the default / run mode
        reset()
        call({}, "A")
        if st["cmds"] != [BASE_CMD]:
            bad.append(f"A: run command {st['cmds']!r}, want [{BASE_CMD!r}]")
        if st["s3_gets"] != 1 or st["stops"] != 1 or st["alerts"]:
            bad.append(f"A: run mode: s3_gets={st['s3_gets']} stops={st['stops']} alerts={st['alerts']} (want 1, 1, none)")
        reset()
        call({"mode": "run"}, "A2")
        if st["cmds"] != [BASE_CMD]:
            bad.append(f"A2: explicit run command {st['cmds']!r}")

        # B: ft_reattempt
        reset()
        res = call({"mode": "ft_reattempt"}, "B")
        if st["cmds"] != [FT_CMD]:
            bad.append(f"B: ft_reattempt command {st['cmds']!r}, want [{FT_CMD!r}]")
        if st["s3_gets"] != 0:
            bad.append(f"B: ft_reattempt made {st['s3_gets']} s3 get_object call(s) (the main-run guard must not run)")
        if st["alerts"]:
            bad.append(f"B: an alert on a successful refill: {st['alerts']}")
        if st["starts"] != 1 or st["stops"] != 1:
            bad.append(f"B: starts={st['starts']} stops={st['stops']}, want 1 and 1")
        if not isinstance(res, dict) or res.get("mode") != "ft_reattempt":
            bad.append(f"B: handler returned {res!r}, want mode ft_reattempt")

        # C: dry run
        reset()
        call({"mode": "ft_reattempt", "dry_run": True}, "C")
        if st["cmds"] != [FT_DRY_CMD]:
            bad.append(f"C: dry-run command {st['cmds']!r}, want [{FT_DRY_CMD!r}]")

        # D: SSM Failed -> alert and still stop
        reset(status="Failed", rc=1)
        call({"mode": "ft_reattempt"}, "D")
        if not st["alerts"]:
            bad.append("D: a failed refill raised no alert")
        if st["stops"] != 1:
            bad.append(f"D: the box was stopped {st['stops']}x after a failed refill, want 1")

        # G: the budget never terminal -> the box is LEFT RUNNING, both modes
        for mode in ("run", "ft_reattempt"):
            reset(status="InProgress", rc=None)
            call({"mode": mode}, "G-" + mode)
            if st["stops"] != 0:
                bad.append(f"G-{mode}: the box was stopped {st['stops']}x on budget expiry (must be left running)")
            if not st["alerts"]:
                bad.append(f"G-{mode}: no overran-budget alert")

        # H: absence_check unchanged
        reset()
        call({"mode": "absence_check", "date": "2026-07-11"}, "H")
        if st["ssm_calls"] != 0:
            bad.append("H: absence_check made an SSM call")
    finally:
        boto3.client = real_client
        real_time.time, real_time.sleep = real_time_fn, real_sleep

    if bad:
        print("GATE-BAD " + "; ".join(bad))
        return 1
    print("GATE-OK arms A(run unchanged) A2(explicit run) B(ft_reattempt: command, no s3 guard, stop) C(dry run) "
          "D(failed -> alert + stop) G(budget expiry leaves running, both modes) H(absence_check unchanged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
