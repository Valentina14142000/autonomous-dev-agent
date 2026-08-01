from app.graph import app_graph
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Autonomous Multi-Agent Software Engineer",
    description="Supervisor-Worker multi-agent automation with secure execution",
    version="1.0.0",
)


class TaskRequest(BaseModel):
  task_description: str


@app.post("/run-agent")
async def run_autonomous_agent(request: TaskRequest):
  initial_state = {
      "task_description": request.task_description,
      "plan": [],
      "current_step": 0,
      "generated_code": "",
      "execution_output": "",
      "test_passed": False,
      "error_message": "",
      "iteration_count": 0,
  }

  result = app_graph.invoke(initial_state)

  return {
      "task": result["task_description"],
      "plan": result["plan"],
      "generated_code": result["generated_code"],
      "execution_output": result["execution_output"],
      "test_passed": result["test_passed"],
      "error_message": result["error_message"],
  }