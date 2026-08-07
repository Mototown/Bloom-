class BloomGenerator:
    def generate_model(self, prompt: str, record):
        model_sql = f"-- Prompt: {prompt}\nSELECT * FROM stg_users"
        schema_yml = f"version: 2\nmodels:\n - name: {record.related_model}\n description: {record.title}\n"
        return {"model.sql": model_sql, "schema.yml": schema_yml, "decision_record.md": record.to_markdown()}
