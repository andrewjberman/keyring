"""Cross-producer return contract tests; load pure production functions without AWS I/O."""
import ast
import logging
import math
import unittest
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[5]
YANG = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline"
POSITIONING = YANG / "positioning/yang-generate-positioning/lambda_function.py"
ETF = YANG / "portfolios/yang-generate-etf-returns/lambda_function.py"
BENCHMARK = YANG / "portfolios/yang-model-portfolio-benchmarks/lambda_function.py"
MARKET = ROOT / ("infra/aws/lambda/v2_portal/01_market_overview/lambdas/"
                 "market-overview-tiered-generator/lambda_function.py")
PERIODS = ("1D", "WTD", "MTD", "1M", "QTD", "1Q", "YTD", "1Y")


def functions(path, names, constants=()):
    """Compile actual source AST, excluding module-level network initialization."""
    tree = ast.parse(path.read_text(encoding="utf8"))
    selected = [n for n in tree.body if
                (isinstance(n, ast.FunctionDef) and n.name in names) or
                (isinstance(n, ast.Assign) and any(
                    isinstance(t, ast.Name) and t.id in constants for t in n.targets))]
    namespace = dict(pd=pd, np=np, datetime=datetime, timedelta=timedelta,
                     math=math, List=List, Dict=Dict, Optional=Optional,
                     logger=logging.getLogger(__name__))
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(path), "exec"), namespace)
    return namespace


def expected(series, end, period, full_window=False):
    series = series.loc[:end].dropna()
    if period == "1D":
        selected = series.tail(1)
    elif period in {"1M", "1Q", "1Y"}:
        cutoff = end - pd.Timedelta(days={"1M": 30, "1Q": 91, "1Y": 365}[period])
        if full_window and series.index.min() > cutoff:
            return None
        selected = series[series.index > cutoff]
    else:
        start = {"WTD": end - pd.Timedelta(days=end.weekday()),
                 "MTD": end.replace(day=1),
                 "QTD": end.replace(month=3 * ((end.month - 1) // 3) + 1, day=1),
                 "YTD": end.replace(month=1, day=1)}[period]
        selected = series.loc[start:]
    if selected.empty:
        return None
    return round(100 * (math.prod(1 + float(r) / 100 for r in selected) - 1), 2)


class PeriodContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = functions(POSITIONING, ["calculate_etf_period_returns"])
        cls.e = functions(ETF, ["calculate_etf_returns_long", "calculate_etf_returns_wide",
                                "get_period_start"], ["PERIODS", "INCEPTION_DATE"])
        cls.b = functions(BENCHMARK, ["calculate_period_returns", "compound_returns",
                                     "calculate_volatility"], ["INCEPTION_DATE"])
        cls.m = functions(MARKET, ["calculate_period_return", "calculate_all_returns",
                                  "calculate_trailing_sessions_return"], ["PERIOD_CALENDAR_DAYS"])

    def assert_producers(self, series):
        end = series.index.max()
        frame = pd.DataFrame({"date": series.index, "ticker": "TEST", "return": series.values})
        position = self.p["calculate_etf_period_returns"](frame, end.strftime("%Y-%m-%d"))["TEST"]
        long = self.e["calculate_etf_returns_long"](frame)
        wide = self.e["calculate_etf_returns_wide"]("TEST", pd.DataFrame({"TEST": series / 100}))
        # A poisoned price field detects accidentally reverting to price return.
        points = [{"date": d.strftime("%Y-%m-%d"), "return": float(r), "price": 1}
                  for d, r in series.items()]
        market = self.m["calculate_all_returns"](points)
        for period in PERIODS:
            want = expected(series, end, period)
            benchmark = self.b["calculate_period_returns"](series, end, period)["return"]
            for producer, value in [("Positioning", position[period]), ("ETF long", long[period]),
                                    ("ETF wide", wide[period]), ("Benchmark", benchmark),
                                    ("Market", round(market[period] * 100, 2))]:
                with self.subTest(as_of=str(end.date()), period=period, producer=producer):
                    self.assertEqual(value, want)

    def test_opening_days_and_holiday_gaps(self):
        for end in ["2024-01-01", "2024-04-01", "2024-07-01", "2026-09-25"]:
            dates = pd.bdate_range(pd.Timestamp(end) - pd.Timedelta(days=420), end)
            # Nonuniform income-inclusive returns, and extra missing sessions: calendar
            # periods must not silently become counts of the last 21/63/252 rows.
            dates = dates.delete(list(range(10, len(dates) - 3, 19)))
            values = np.array([0.31 if i % 7 == 0 else -0.02 for i in range(len(dates))])
            self.assert_producers(pd.Series(values, index=dates))

    def test_exact_rolling_cutoffs(self):
        end = pd.Timestamp("2026-09-25")
        series = pd.Series(0.0, index=pd.date_range(end - pd.Timedelta(days=420), end))
        for days in [30, 91, 365]:
            series.loc[end - pd.Timedelta(days=days)] = 7.0
            series.loc[end - pd.Timedelta(days=days - 1)] = 2.0
        self.assert_producers(series)

    def test_positioning_respects_as_of_and_short_history(self):
        frame = pd.DataFrame({"date": pd.to_datetime(["2026-09-24", "2026-09-25", "2026-09-28"]),
                              "ticker": "TEST", "return": [1.0, 2.0, 99.0]})
        result = self.p["calculate_etf_period_returns"](frame, "2026-09-25")["TEST"]
        self.assertEqual(result["1D"], 2.0)
        self.assertEqual(result["WTD"], 3.02)
        self.assertIsNone(result["1Y"])

    def test_wide_format_is_date_sorted(self):
        series = pd.Series([1.0, 2.0, 3.0], index=pd.to_datetime(
            ["2026-09-25", "2026-09-23", "2026-09-24"])) / 100
        result = self.e["calculate_etf_returns_wide"]("TEST", pd.DataFrame({"TEST": series}))
        self.assertEqual(result["1D"], 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
