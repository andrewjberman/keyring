"""Bounded AMGT research reads; no credentials, writes to S3, or login actions.

Outputs only research market/company data beside this script. DAPI deadlines
are explicit and a timeout fails the run rather than declaring missing fields.
"""

import datetime as dt
import json
import sys
import time
from pathlib import Path

import blpapi
import boto3

OUT = Path(__file__).resolve().parent
BUCKET = "opal-data-harvest"


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")


def request(kind, securities, fields, overrides=None, **params):
    opts = blpapi.SessionOptions()
    opts.setServerHost("127.0.0.1")
    opts.setServerPort(8194)
    session = blpapi.Session(opts)
    try:
        if not session.start() or not session.openService("//blp/refdata"):
            raise RuntimeError(
                "Existing Bloomberg session unavailable; no reauth attempted"
            )
        req = session.getService("//blp/refdata").createRequest(kind)
        for sec in securities:
            req.append("securities", sec)
        for fld in fields:
            req.append("fields", fld)
        for key, val in (overrides or {}).items():
            ov = req.getElement("overrides").appendElement()
            ov.setElement("fieldId", key)
            ov.setElement("value", val)
        for key, val in params.items():
            req.set(key, val)
        session.sendRequest(req)
        responses = []
        deadline = time.monotonic() + 55
        while time.monotonic() < deadline:
            event = session.nextEvent(1000)
            for msg in event:
                if msg.hasElement("securityData") or msg.hasElement("responseError"):
                    responses.append(msg.toPy())
            if event.eventType() == blpapi.Event.RESPONSE:
                return {
                    "as_of": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "kind": kind,
                    "securities": securities,
                    "fields": fields,
                    "overrides": overrides,
                    "parameters": params,
                    "responses": responses,
                }
        raise TimeoutError(
            "DAPI request exceeded 55 seconds; partial response not scored"
        )
    finally:
        session.stop()


def inventory():
    s3 = boto3.client("s3")
    keys = {}
    for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=BUCKET, Prefix="peers/v1/"
    ):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            if not key.endswith(".json"):
                continue
            security_key = key[len("peers/v1/") :].rsplit("/", 1)[0]
            if security_key.startswith("_"):
                continue
            if (
                security_key not in keys
                or obj["LastModified"] > keys[security_key]["LastModified"]
            ):
                keys[security_key] = obj
    data = {}
    for sec, obj in sorted(keys.items()):
        res = s3.get_object(Bucket=BUCKET, Key=obj["Key"])
        data[sec.replace("_", " ")] = {
            "key": obj["Key"],
            "etag": res["ETag"],
            "version_id": res.get("VersionId"),
            "document": json.loads(res["Body"].read()),
        }
    write("pool_inventory.json", data)
    print(
        json.dumps(
            {
                "pool_n": len(data),
                "nonempty": sum(
                    bool(r["document"].get("members")) for r in data.values()
                ),
                "first_nonempty": next(
                    (
                        r["document"]
                        for r in data.values()
                        if r["document"].get("members")
                    ),
                    None,
                ),
                "empty_reasons": {
                    s: r["document"].get("reason")
                    for s, r in data.items()
                    if not r["document"].get("members")
                },
            },
            default=str,
        )
    )


def probe():
    data = json.loads((OUT / "pool_inventory.json").read_text())
    names = sorted(data)
    fields = [
        "NAME",
        "ID_BB_GLOBAL",
        "GICS_SECTOR_NAME",
        "CRNCY",
        "EQY_FUND_CRNCY",
        "BEST_PERIOD_END_DATE",
        "BEST_CPS",
        "BEST_CPS_STDDEV",
        "BEST_CPS_NUMEST",
        "BEST_EPS",
        "BEST_EPS_STDDEV",
        "BEST_EPS_NUMEST",
        "BEST_ESTIMATE_FCF",
        "BEST_CALCULATED_FCF",
        "BEST_SALES",
        "IS_AVG_NUM_SH_FOR_EPS",
        "EXECUTIVE_AVERAGE_TENURE",
        "TOTAL_TENURE_OF_CEO_COMPANY",
        "CHIEF_EXECUTIVE_OFFICER_TENURE",
        "SUPPLY_CHAIN_SUM_TOP_REVENUES",
    ]
    for period in ("1FY", "2FY"):
        res = request(
            "ReferenceDataRequest",
            names,
            fields,
            {"BEST_FPERIOD_OVERRIDE": period, "SUPPLY_CHAIN_SUM_COUNT_OVERRIDE": "1"},
        )
        write(f"pool_{period}.json", res)
        print(f"saved {period}: {len(names)} securities")


def supply():
    data = json.loads((OUT / "pool_inventory.json").read_text())
    res = request(
        "ReferenceDataRequest",
        sorted(data),
        ["NAME", "SUPPLY_CHAIN_CUSTOMERS_ALL_DATA", "SUPPLY_CHAIN_SUM_TOP_REVENUES"],
        {"SUPPLY_CHAIN_SUM_COUNT_OVERRIDE": "1"},
    )
    write("supply_chain.json", res)
    five = [
        "BA US Equity",
        "COST US Equity",
        "HD US Equity",
        "SAP GY Equity",
        "BABA US Equity",
    ]
    res = request(
        "ReferenceDataRequest",
        five,
        ["BEST_CPS_BRK_GRID", "BEST_CAPEX_BROKER_GRID", "BEST_PERIOD_END_DATE"],
        {"BEST_FPERIOD_OVERRIDE": "1FY"},
    )
    write("broker_detail.json", res)
    print("saved supply-chain and broker-detail responses")


def peers():
    inventory = json.loads((OUT / "pool_inventory.json").read_text())
    fixes = {
        "7203": "7203 JP Equity",
        "9983": "9983 JP Equity",
        "712387": "NESN SW Equity",
        "588950": "IFX GY Equity",
        "637248": "2454 TT Equity",
    }
    subjects = {
        sec: r["document"]
        for sec, r in inventory.items()
        if r["document"].get("members")
    }
    members = {}
    for doc in subjects.values():
        for member in doc["members"]:
            raw = member["ticker"]
            requested = fixes.get(
                raw, raw if raw.endswith(" Equity") else raw + " Equity"
            )
            members[requested] = {
                "raw": raw,
                "expected_name": member["name"],
                "country": member["country"],
            }
    write(
        "peer_requests.json",
        {
            "subjects": subjects,
            "members": members,
            "candidate_fixes_require_name_validation": fixes,
        },
    )
    securities = sorted(set(subjects) | set(members))
    fields = [
        "NAME",
        "ID_BB_GLOBAL",
        "ID_BB_GLOBAL_COMPANY",
        "GICS_SECTOR_NAME",
        "EQY_FUND_CRNCY",
        "CRNCY",
        "FREE_CASH_FLOW_YIELD",
        "BEST_PE_RATIO",
        "BEST_EPS",
        "PE_RATIO",
        "TRAIL_12M_DVD_PAID",
        "CF_DECR_CAP_STOCK",
        "CRNCY_ADJ_MKT_CAP",
        "CURRENT_EV_TO_T12M_EBITDA",
        "BEST_CUR_EV_TO_EBITDA",
        "EV_TO_T12M_SALES",
        "CURRENT_EV_TO_12M_SALES",
        "BEST_CURRENT_EV_BEST_SALES",
        "TRAIL_12M_EBITDA",
    ]
    res = request(
        "ReferenceDataRequest",
        securities,
        fields,
        {"BEST_FPERIOD_OVERRIDE": "BF", "EQY_FUND_CRNCY": "USD"},
    )
    write("peers_BF.json", res)
    for period in ("1FY", "2FY"):
        res = request(
            "ReferenceDataRequest",
            sorted(members),
            [
                "NAME",
                "BEST_PERIOD_END_DATE",
                "BEST_CPS",
                "BEST_CPS_STDDEV",
                "BEST_CPS_NUMEST",
                "BEST_EPS",
                "BEST_EPS_STDDEV",
                "BEST_EPS_NUMEST",
                "EQY_FUND_CRNCY",
            ],
            {"BEST_FPERIOD_OVERRIDE": period},
        )
        write(f"peer_members_{period}.json", res)
    print(
        f"saved valuation and both annual dispersion probes: {len(subjects)} subjects, {len(members)} unique member requests"
    )


def history():
    names = sorted(json.loads((OUT / "pool_inventory.json").read_text()))
    fields = [
        "EBIT",
        "IS_INT_EXPENSE",
        "TRAIL_12M_EBITDA",
        "NET_DEBT",
        "BS_CASH_NEAR_CASH_ITEM",
        "BS_TOTAL_AVAIL_LINE_OF_CREDIT",
        "BS_YEAR_1_PRINCIPAL",
        "BS_YEAR_2_PRINCIPAL",
        "BS_TOTL_DEBT_DEBT_SCHEDULE",
        "TRAIL_12M_FREE_CASH_FLOW",
        "TRAIL_12M_NET_SALES",
        "SUPPLY_CHAIN_SUM_TOP_REVENUES",
        "EXECUTIVE_AVERAGE_TENURE",
        "TOTAL_TENURE_OF_CEO_COMPANY",
        "BS_CONTRACTUAL_OBLIG_YEAR_1",
        "BS_CONTRACTUAL_OBLIG_YEAR_2",
    ]
    res = request(
        "HistoricalDataRequest",
        names,
        fields,
        {"SUPPLY_CHAIN_SUM_COUNT_OVERRIDE": "1"},
        startDate="20230101",
        endDate="20260915",
        periodicitySelection="QUARTERLY",
    )
    write("history_quarterly.json", res)
    res = request(
        "HistoricalDataRequest",
        names,
        [
            "BS_YEAR_1_PRINCIPAL",
            "BS_YEAR_2_PRINCIPAL",
            "BS_CONTRACTUAL_OBLIG_YEAR_1",
            "BS_CONTRACTUAL_OBLIG_YEAR_2",
            "SUPPLY_CHAIN_SUM_TOP_REVENUES",
            "EXECUTIVE_AVERAGE_TENURE",
            "TOTAL_TENURE_OF_CEO_COMPANY",
        ],
        {"SUPPLY_CHAIN_SUM_COUNT_OVERRIDE": "1"},
        startDate="20170101",
        endDate="20260915",
        periodicitySelection="YEARLY",
    )
    write("history_annual.json", res)
    print(
        "saved quarterly and annual history; field-period semantics still require verification"
    )


def corrected_history():
    names = sorted(json.loads((OUT / "pool_inventory.json").read_text()))
    fields = [
        "EBIT",
        "IS_INT_EXPENSE",
        "TRAIL_12M_EBITDA",
        "NET_DEBT",
        "BS_CASH_NEAR_CASH_ITEM",
        "BS_TOTAL_AVAIL_LINE_OF_CREDIT",
        "BS_YEAR_1_PRINCIPAL",
        "BS_YEAR_2_PRINCIPAL",
        "BS_TOTL_DEBT_DEBT_SCHEDULE",
        "TRAIL_12M_FREE_CASH_FLOW",
        "TRAIL_12M_NET_SALES",
        "SUPPLY_CHAIN_SUM_TOP_REVENUES",
    ]
    for fund_per, periodicity, start in (
        ("Q", "QUARTERLY", "20230101"),
        ("Y", "YEARLY", "20170101"),
    ):
        res = request(
            "HistoricalDataRequest",
            names,
            fields,
            {"FUND_PER": fund_per, "SUPPLY_CHAIN_SUM_COUNT_OVERRIDE": "1"},
            startDate=start,
            endDate="20260915",
            periodicitySelection=periodicity,
        )
        write(f"history_fund_{fund_per}.json", res)
    res = request(
        "ReferenceDataRequest",
        names,
        [
            "NAME",
            "COMPANY_EXEC_OFFICERS",
            "LAST_CFO_START_DATE",
            "LAST_COO_START_DATE",
            "PRIMARY_PERIODICITY",
            "BS_CONTRACTUAL_OBLIG_YEAR_1",
            "BS_CONTRACTUAL_OBLIG_YEAR_2_3",
            "BS_YEAR_1_PRINCIPAL",
            "BS_YEAR_2_PRINCIPAL",
        ],
        {},
    )
    write("management_and_obligations.json", res)
    print("saved FUND_PER Q/Y history and management/obligations control")


if __name__ == "__main__":
    {
        "inventory": inventory,
        "probe": probe,
        "supply": supply,
        "peers": peers,
        "history": history,
        "corrected_history": corrected_history,
    }[sys.argv[1]]()
