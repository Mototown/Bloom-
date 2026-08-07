from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .agent import BloomAgent
from .decision_record import DecisionRecord


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="bloom",
        description="Bloom — Decision-aware dbt model generator",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    gen = sub.add_parser("generate", help="Generate a dbt model from a decision")
    gen.add_argument("--question", "-q", required=True, help="Business question")
    gen.add_argument("--title", "-t", required=True, help="Decision title")
    gen.add_argument("--decision", "-d", required=True, help="The actual decision")
    gen.add_argument("--context", "-c", default="", help="Context / background")
    gen.add_argument("--model-name", "-m", default=None, help="dbt model name")
    gen.add_argument("--id", default="ADR-001", help="Decision record ID")
    gen.add_argument("--author", default=None)
    gen.add_argument("--output", "-o", default="./generated", help="Output directory")
    gen.add_argument(
        "--no-llm",
        action="store_true",
        help="Force template mode (no OpenAI call)",
    )

    args = parser.parse_args(argv)

    if args.command == "generate":
        record = DecisionRecord(
            id=args.id,
            title=args.title,
            context=args.context or args.question,
            decision=args.decision,
            related_model=args.model_name,
            author=args.author,
        )

        agent = BloomAgent()
        artifacts = agent.run(
            business_question=args.question,
            record=record,
            use_llm=not args.no_llm,
            output_dir=args.output,
        )

        print(f"✓ Generated into {Path(args.output).resolve()}")
        print(f"  model   : {artifacts.get('model_name')}.sql")
        print(f"  schema  : schema.yml")
        print(f"  decision: {artifacts.get('model_name')}__decision.md")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())