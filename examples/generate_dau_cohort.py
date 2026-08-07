"""
Example: generate a decision-aware dbt model for daily active users by cohort.

Run from the repo root:
    python examples/generate_dau_cohort.py
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from bloom import BloomAgent, DecisionRecord


def main() -> None:
    record = DecisionRecord(
        id="ADR-2026-08-001",
        title="Daily active users by signup cohort",
        context=(
            "Product wants to understand retention by the week a user first signed up. "
            "We already have a clean stg_users and stg_events layer."
        ),
        decision=(
            "Create a daily snapshot model at user-day grain. "
            "Cohort key = date_trunc('week', signup_at). "
            "A user is active on a day if they have ≥1 event that day."
        ),
        alternatives_considered=[
            "Pure event-level retention curve (too heavy for most dashboards)",
            "Weekly-only rollup (loses daily seasonality)",
            "Pre-aggregate inside an Airflow job (harder to test & version)",
        ],
        consequences=(
            "Table grows ~1 row per active user per day. "
            "Easy to incrementalize later with a date filter. "
            "Downstream models can freely slice by cohort and activity date."
        ),
        related_model="fct_dau_by_cohort",
        author="bloom-demo",
    )

    agent = BloomAgent()
    out_dir = Path(__file__).parent / "output" / "dau_by_cohort"

    artifacts = agent.run(
        business_question="How many daily active users do we have by signup cohort?",
        record=record,
        output_dir=out_dir,
    )

    print("\n=== model.sql (preview) ===")
    print(artifacts["model.sql"][:800], "...\n")

    print("=== decision_record.md ===")
    print(artifacts["decision_record.md"])

    print(f"\nFull artifacts written to: {out_dir.resolve()}")


if __name__ == "__main__":
    main()