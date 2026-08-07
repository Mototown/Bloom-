from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional, Union

from .decision_record import DecisionRecord
from .generator import BloomGenerator


class BloomAgent:
    """Thin orchestration layer around BloomGenerator."""

    def __init__(self, model: Optional[str] = None):
        self.generator = BloomGenerator(model=model)

    def run(
        self,
        business_question: str,
        record: DecisionRecord,
        *,
        use_llm: Optional[bool] = None,
        output_dir: Optional[Union[str, Path]] = None,
    ) -> Dict[str, str]:
        """Generate the three artifacts and optionally write them to disk."""
        artifacts = self.generator.generate_model(
            business_question=business_question,
            record=record,
            use_llm=use_llm,
        )

        if output_dir is not None:
            self.write_artifacts(artifacts, output_dir)

        return artifacts

    def write_artifacts(
        self,
        artifacts: Dict[str, str],
        output_dir: Union[str, Path],
    ) -> Path:
        """Write model.sql, schema.yml and decision_record.md into output_dir."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        model_name = artifacts.get("model_name", "generated_model")

        (out / f"{model_name}.sql").write_text(artifacts["model.sql"], encoding="utf-8")
        (out / "schema.yml").write_text(artifacts["schema.yml"], encoding="utf-8")
        (out / f"{model_name}__decision.md").write_text(
            artifacts["decision_record.md"], encoding="utf-8"
        )

        return out