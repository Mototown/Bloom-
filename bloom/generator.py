class BloomGenerator:
    def generate_model(self, business_question: str, record):
        model_sql = f"""-- Bloom Generated Model
-- {record.title}: {record.decision}
SELECT * FROM stg_users"""

        schema_yml = f"""version: 2
models:
    - name: {record.related_model or 'my_model'}
    description: {record.title}
"""
        return {
            "model.sql": model_sql,
            "schema.yml": schema_yml,
            "decision_record.md": record.to_markdown()
        }
