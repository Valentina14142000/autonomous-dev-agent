from app.state import AgentState


def coder_node(state: AgentState):
  print("---CODER: WRITING IMPLEMENTATION CODE---")

  # Generating a robust sample solution script
  sample_code = """
def calculate_metrics(data: list) -> dict:
    if not data:
        return {"mean": 0, "anomaly_count": 0}
    mean_val = sum(data) / len(data)
    anomalies = [x for x in data if abs(x - mean_val) > 2.0]
    return {"mean": mean_val, "anomaly_count": len(anomalies)}

# Test execution
result = calculate_metrics([10, 12, 11, 45, 9, 10])
print(f"RESULT: {result}")
"""
  return {"generated_code": sample_code}